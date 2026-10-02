"""Establish the Latin of one volume by three-witness vote (CONVENTIONS §3).

    .venv/bin/python scripts/w3/vote.py SLUG [FIRST_PAGE LAST_PAGE]

Pivot = the primary (Princeton) scan, whose leaves map to printed pages through
catalog/plate_offsets.tsv. Every other witness (other scans, Fordham) is aligned to
the pivot page by page and votes on each pivot token; witnesses may also vote to
DELETE a pivot token or INSERT a word the pivot lost.

Outputs, per printed page N:
    text/<slug>/pNNN.la.txt     established Latin (## headings, blank line = paragraph)
    text/<slug>/pNNN.check.tsv  every non-R1 decision
and text/<slug>/plate_queue.tsv: every word the table sends to the plate.
"""
import csv, difflib, json, os, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# ---------------------------------------------------------------- normalisation
def norm(t):
    t = t.lower().replace('æ', 'ae').replace('œ', 'oe').replace('ſ', 's')
    t = t.replace('j', 'i').replace('v', 'u')
    t = re.sub(r'(\d)[°º]', r'\1', t)
    t = re.sub(r'(?<=\d)o', '0', t)                           # OCR 3o = 30
    t = re.sub(r'[^a-z0-9]', '', t)
    return re.sub(r'^([iuxlcdm]{2,})0$', r'\1', t)          # XLVI° read as xlui0


# ---------------------------------------------------------------- lexicon
class Lexicon:
    """Is a form a real word?  Hunspell Latin (classical) tried on classicised
    variants of the medieval spelling, plus forms three independent witnesses
    have agreed on anywhere in the corpus (catalog/lexicon/agreed.txt)."""

    def __init__(self):
        from spylls.hunspell import Dictionary
        self.d = Dictionary.from_files(f'{ROOT}/catalog/lexicon/la.index')
        p = f'{ROOT}/catalog/lexicon/agreed.txt'
        self.agreed = set(open(p).read().split()) if os.path.exists(p) else set()
        self.cache = {}

    @staticmethod
    def variants(w):
        base = w
        base = re.sub(r'ci(?=[aeiou])', 'ti', base)
        base = base.replace('y', 'i').replace('michi', 'mihi').replace('nichil', 'nihil')
        base = base.replace('mpn', 'mn').replace('ph', 'f') if False else base
        out = {w, base, base.replace('ch', 'h'), base.replace('th', 't')}
        es = [m.start() for m in re.finditer('e', base)]
        for i in es[-4:]:                                   # e -> ae / oe at one position
            out.add(base[:i] + 'ae' + base[i + 1:])
            out.add(base[:i] + 'oe' + base[i + 1:])
        if len(es) >= 2:                                    # two positions (prae...ae)
            i, j = es[0], es[-1]
            out.add(base[:i] + 'ae' + base[i + 1:j] + 'ae' + base[j + 1:])
        return out

    def real(self, w):
        if w in self.cache:
            return self.cache[w]
        if not w or w == '∅':
            r = False
        elif w.isdigit():
            r = True
        elif len(w) == 1:
            r = w in ('a', 'e', 'o', 'i')
        elif w in ENGLISH:
            r = False
        elif any(self.d.lookup(v) for v in self.variants(w) if v):
            r = True
        elif w in self.agreed:
            # agreed.txt holds shared misreadings too (chnstus, ahquis): not one when a known OCR
            # confusion turns it into a dictionary word
            r = not any(self.d.lookup(v) for p_, o_ in CONFUSIONS for i in [w.find(o_)] if i >= 0
                        for v in self.variants(w[:i] + p_ + w[i + len(o_):]) if v)
        else:
            r = False
        self.cache[w] = r
        return r


# ---------------------------------------------------------------- inputs
def offsets():
    rows = list(csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t'))
    return {r['slug']: r for r in rows}


def load(path):
    return [json.loads(l) for l in open(path)]


def prep(toks):
    """Drop heading-line markers and punctuation-only tokens; keep raw forms."""
    out = []
    for t in toks:
        if t.get('head'):
            continue
        n = norm(t['t'])
        if n:
            t['n'] = n
            out.append(t)
        elif out:
            out[-1]['t'] = out[-1]['t'] + t['t']        # attach stray punctuation
    return out


# ---------------------------------------------------------------- alignment
def anchor_index(stream):
    idx = defaultdict(list)
    for i, t in enumerate(stream):
        if len(t['n']) >= 7:
            idx[t['n']].append(i)
    return idx


NOTE_WORDS = {'cap', 'codd', 'marg', 'deest', 'recte', 'corr', 'opp', 'comp', 'cf', 'ibid', 'decr', 'pag', 'tom'}


def tail_run(stream, end, head):
    """Words a witness has between the pivot page's last match and the next page's opening words:
    the pivot OCR's lost last lines (De ecclesia pp. 42, 451, 563).  None if the next page's head
    is not found within reach, so the run is never unbounded."""
    if len(head) < 4:
        return None
    for j in range(end, min(len(stream) - 4, end + 200)):
        if sum(stream[j + q]['n'] == head[q] for q in range(4)) >= 3:
            return [x for x in stream[end:j] if not LINE_NO.match(x['n'])]
    return None


def tail_vote(tails, nwit, lex):
    """A page-end run is accepted when a majority of the other witnesses carry it (fuzzy: OCR
    differs across scans) and it does not read as apparatus.  Returns the best-read witness run."""
    tails = {w: xs for w, xs in tails.items() if xs and len(xs) >= 3}
    if not tails:
        return None
    s = {w: ' '.join(x['n'] for x in xs) for w, xs in tails.items()}
    best = None
    for w in tails:
        sup = [v for v in tails if difflib.SequenceMatcher(None, s[w], s[v]).ratio() >= 0.75]
        if best is None or len(sup) > len(best):
            best = sup
    if len(best) < 2 or len(best) * 2 <= nwit:
        return None
    rep = max(best, key=lambda w: sum(lex.real(x['n']) for x in tails[w]))
    if any(x['n'] in NOTE_WORDS for x in tails[rep]):
        return None
    if sum(bool(re.match(r'^[AB][,1₁ij]?[:.;]?$', x['t'])) for x in tails[rep]) >= 2:
        return None                             # 'A: quilt. A,: qualiter' — the apparatus
    return tails[rep], len(best)


def locate(page, stream, idx, hint):
    """Estimated start of `page` in `stream` from rare-word anchors."""
    cands = []
    for k, t in enumerate(page):
        ps = idx.get(t['n'])
        if ps and len(ps) <= 4:
            cands += [p - k for p in ps]
    if not cands:
        return None
    if hint is not None:                        # prefer anchors near where we expect to be
        near = [c for c in cands if abs(c - hint) < 3 * len(page) + 200]
        cands = near or cands
    cands.sort()
    return cands[len(cands) // 2]


def align_page(page, stream, start):
    lo = max(0, start - 40)
    win = stream[lo:start + len(page) + 60]
    sm = difflib.SequenceMatcher(None, [t['n'] for t in page], [t['n'] for t in win], autojunk=False)
    votes = [None] * len(page)      # per pivot token: witness token dict, '∅', or None (unknown)
    ins = defaultdict(list)         # gap index -> list of inserted witness tokens
    matched = 0
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(a2 - a1):
                votes[a1 + k] = win[b1 + k]
            matched += a2 - a1
        elif op == 'replace':
            if a2 - a1 == b2 - b1:
                for k in range(a2 - a1):
                    votes[a1 + k] = win[b1 + k]
            elif ''.join(t['n'] for t in page[a1:a2]) == ''.join(t['n'] for t in win[b1:b2]):
                for k in range(a1, a2):             # split/merge only: agrees in substance
                    votes[k] = dict(page[k], split=True)
            elif b2 - b1 > a2 - a1 and a2 - a1 == 1:
                votes[a1] = win[b1]                 # take first, rest as insertions after
                ins[a2] += win[b1 + 1:b2]
            elif a2 - a1 > b2 - b1 and b2 - b1 == 1:
                votes[a1] = win[b1]
                for k in range(a1 + 1, a2):
                    votes[k] = '∅'
        elif op == 'delete':
            for k in range(a1, a2):
                votes[k] = '∅'
        elif op == 'insert':
            ins[a1] += win[b1:b2]
    # trim the window slack at both ends: unmatched leading/trailing inserts are context
    first_eq = next((a for op, a, *_ in sm.get_opcodes() if op == 'equal'), 0)
    last_eq = max((a2 for op, a1, a2, *_ in sm.get_opcodes() if op == 'equal'), default=len(page))
    for g in list(ins):
        if g <= first_eq and g == 0 or g >= last_eq and g == len(page):
            del ins[g]
    # votes outside the anchored stretch (first to last match of >= 3 words) are unknown: before it the
    # window's slack pairs the previous page's last words with this page's first (p. 297 'dat' for
    # 'recipiunt', pp. 341, 373), after it the next page's first words
    anchors = [b for b in sm.get_matching_blocks() if b.size >= 3]
    if anchors:
        for k in range(0, anchors[0].a):
            votes[k] = 'EDGE'
        for k in range(anchors[-1].a + anchors[-1].size, len(page)):
            votes[k] = 'EDGE'
    frac = matched / max(1, len(page))
    end = lo + (sm.get_matching_blocks()[-2].b + sm.get_matching_blocks()[-2].size
                if len(sm.get_matching_blocks()) > 1 else 0)
    return votes, ins, frac, end


# ---------------------------------------------------------------- decision
# Known OCR confusions in 19th-c. roman type (print side, OCR side): ligatures fi/ff/fl,
# long-s shapes, li->h, rn->m, c/e, u/n, f/t ... A non-word within two of these of a
# real voter form is evidence for that form, however many scans share it.
CONFUSIONS = [('fi', 'ii'), ('fi', 'fl'), ('ff', 'tf'), ('ff', 'if'), ('fi', 'h'), ('li', 'h'), ('li', 'b'),
              ('s', 'b'), ('s', 'h'), ('m', 'rn'), ('m', 'in'), ('m', 'iu'), ('n', 'ri'), ('n', 'u'), ('u', 'n'),
              ('e', 'c'), ('c', 'e'), ('f', 't'), ('t', 'f'), ('f', 'r'), ('d', 'cl'), ('h', 'b'), ('l', 'i'),
              ('i', 'l'), ('r', 'i'), ('ll', 'u'), ('ri', 'n'), ('a', 'u'), ('o', 'c'), ('e', 'o'), ('ui', 'm')]


CONFUSIONS += [(b, a) for a, b in CONFUSIONS]

# English side-note words that leak into the main text are never Latin
ENGLISH = set('the of and that which who whom his her their them they this these those with from by for '
              'was were are must should shall would not but church king god christ lord lords clergy '
              'people law laws how when what why note see'.split())


def confusable(f, g):
    """Can f be an OCR misreading of g (<=2 known confusions)? Numerals: a degree
    sign read as a trailing zero (3° -> 30)."""
    if f.isdigit() and g.isdigit():
        return f == g + '0' or g == f + '0'
    if abs(len(f) - len(g)) > 3:
        return False
    def one(x):
        for p_, o_ in CONFUSIONS:
            i = x.find(o_)
            while i >= 0:
                yield x[:i] + p_ + x[i + len(o_):]
                i = x.find(o_, i + 1)
    for x in one(f):
        if x == g:
            return True
        for y in one(x):
            if y == g:
                return True
    return False


def unglue(forms, lex):
    """Attribute non-word votes to the real form they are evidence for.
    1. A non-word seen ONCE that closely resembles another voter's real form is a
       misreading of it (habehitis -> habebitis). A non-word several witnesses share
       is left alone: coinciding OCR errors are rare, so it is likely the print's.
    2. A non-word that is a real voter form plus >=3 glued letters is that form with a
       side-note or line number attached (hectruth -> hec)."""
    c = Counter(forms)
    good = [f for f in c if f != '∅' and len(f) >= 2 and lex.real(f)]
    # a non-word that several witnesses share (a proper name, a medieval spelling the
    # dictionary lacks) is also a target for singletons and confusions, if it leads
    fake = [(k, f) for f, k in c.items() if f != '∅' and f not in good and k >= 2]
    if fake:
        k, f = max(fake)
        if k > max((c[g] for g in good), default=0):
            good.append(f)
    out = []
    for f in forms:
        if f != '∅' and f not in good and not lex.real(f) and good:
            h = next((g for g in good if confusable(f, g)), None)
            if h:
                out.append(h); continue
            if c[f] == 1:
                h = max(good, key=lambda g: difflib.SequenceMatcher(None, f, g).ratio())
                if difflib.SequenceMatcher(None, f, h).ratio() >= 0.75:
                    out.append(h); continue
            g = max((g for g in good if len(f) >= len(g) + 3 and (f.startswith(g) or f.endswith(g))),
                    key=len, default=None)
            if g:
                out.append(g); continue
        out.append(f)
    return out


def decide(forms, lex):
    """forms: normalised forms (or '∅') from each voting witness.
    Returns (rule, winner, plate?).  See CONVENTIONS §3.3 and its decision log:
    non-word votes carry no weight against real words (plate-read triage);
    one real-word outlier against >=3 agreeing witnesses is OCR noise;
    >=4 independent witnesses agreeing on a non-word is the print's own form."""
    n = len(forms)
    if n < 3:
        c = Counter(forms)
        return ('THIN', c.most_common(1)[0][0] if len(c) == 1 else None, True)
    forms = unglue(forms, lex)
    c = Counter(forms)
    if len(c) == 1:
        f = forms[0]
        if f == '∅':
            return ('DEL', f, False)
        if lex.real(f):
            return ('R1', f, False)
        return ('R5a', f, False) if n >= 4 else ('R5', f, True)
    nul = c.pop('∅', 0)
    if nul * 2 > n:
        return ('DEL', '∅', any(k >= 2 and lex.real(f) for f, k in c.items()))
    real = Counter({f: k for f, k in c.items() if lex.real(f)})
    fake = Counter({f: k for f, k in c.items() if not lex.real(f)})
    rs = real.most_common(2)
    rf, cr = rs[0] if rs else (None, 0)
    cr2 = rs[1][1] if len(rs) > 1 else 0
    nf, cn = fake.most_common(1)[0] if fake else (None, 0)
    if cr >= 2 and cr > cn and (cr2 == 0 or (cr2 == 1 and cr >= 3)):
        return ('R2' if cr2 == 0 else 'R3a', rf, False)
    # R3b: every competing real form is a known OCR confusion of a clear majority
    # reading (>=3 votes, at least twice any rival): a dictionary word by accident
    if (cr >= 3 and cr >= 2 * max(cr2, cn) and
            all(confusable(f, rf) for f in real if f != rf)):
        return ('R3b', rf, False)
    if cn >= 3 and cn * 2 > n and cr <= 1 and all(k == 1 for f, k in fake.items() if f != nf):   # strict majority of ALL voters
        return ('R6a', nf, False)
    if cr2 >= 2 or (cr2 == 1 and cr < 3 and cr >= 1):
        return ('R3', rf if cr > cr2 else None, True)
    if cn >= 2 and cr == 0 and len(fake) == 1:
        return ('R6', nf, True)
    # R4a: one real form, every other form a known OCR confusion of it (speciah/speciab -> speciali)
    if rf and cr2 == 0 and fake and all(confusable(f, rf) for f in fake):
        return ('R4a', rf, False)
    return ('R4', rf or nf, True)


LINE_NO = re.compile(r'^(5|10|15|20|25|30|35|40)$')


def ocr_suspect(w, lex):
    """A non-word the scans agree on (R5a/R6a) that one known OCR confusion turns into a dictionary
    word: a shared misreading, not the print's spelling, until the plate says otherwise (the
    majority-error class, WORKFLOW stage 4).  Hunspell only: agreed.txt holds these very errors."""
    if not w or w == '∅' or len(w) < 3 or w.isdigit():
        return False
    def dict_word(g):
        return any(lex.d.lookup(v) for v in lex.variants(g) if v)
    if dict_word(w):
        return False
    for p_, o_ in CONFUSIONS:
        i = w.find(o_)
        while i >= 0:
            if dict_word(w[:i] + p_ + w[i + len(o_):]):
                return True
            i = w.find(o_, i + 1)
    return False


# ---------------------------------------------------------------- main
def unstar(w):
    """MS folio asterisks are left out of the reading text (CONVENTIONS 3.5): 'ta*lis' -> 'talis',
    'omnes*Viantes' -> 'omnes Viantes' (a capital after the mark starts a new word)."""
    w = re.sub(r'\*(?=[A-Z])', ' ', w)
    return w.replace('*', '').strip()


ALINEA = set('BCDEFGHJKLMNOPQRSTU')     # L, M added 2026-10-02: 15 sites, all alinea letters


def scar_fix(w, lex):
    """Character scars the scans share, so the vote sees agreement and never queues them (scars.py, 2026-10-01):
    XXIII% (ª), 3o / 5i (30 / 51), 56" (56°), a quote mark (Loserth marks quotation by italics, never by quotes),
    capitals inside a word (numerUS), & or a stop inside a word (separa&bit, nich.il). A rule fires only when its
    result is a dictionary word or a numeral; `.'` (a stop or a question mark: p. 7) is left for the plate."""
    hun = lambda x: any(lex.d.lookup(v) for v in lex.variants(x.lower()) if v)
    # second sweep (brief 2): stray marks, ® for °, j for i inside a word, margin/folio numerals glued into a word,
    # words glued across a stop or a capital (diciturPsal.XLIV0)
    w = re.sub(r'[»«■}{>|_]', '', w).replace('®', '°')
    w = re.sub(r'^([IVXLC]+)[0](?=[.,;:)]*$)', r'\1°', w)
    if re.search(r'[a-z]j', w):
        v = re.sub(r'(?<=[a-z])j', 'i', w)
        if hun(v.strip('.,;:?!()')) or lex.real(v.strip('.,;:?!()').lower()):
            w = v
    core = w.strip('.,;:?!()')
    if re.search(r'[A-Za-z]', core) and re.search(r'\d', core):
        v = re.sub(r'^[il1]?\d+[o0"\'«ªᵃ]*(?=[A-Za-z])', '', w)                 # 2sed, i36quatuor, i3o"fuit
        v = re.sub(r'(?<=[a-z])[il1]?\d+[o0"\'«]*(?=[a-z])', '', v)            # mar2tirum, autonoi34«matice
        vc = v.strip('.,;:?!()')
        if v != w and len(vc) >= 3 and vc.isalpha() and (hun(vc) or lex.real(vc.lower())):   # only digits removed
            return v
    if re.search(r'[a-z][A-Z]|[a-z]\.[A-Za-z]|[a-z]\(', core) and ' ' not in w:
        parts = re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[a-z]\.)(?=[A-Za-z])|(?<=[a-z])(?=\()', ' ', w).split()
        ok = lambda p: (hun(p.strip('.,;:?!()')) or p.endswith('.') or re.fullmatch(r'\(?[IVXLC]+[0°]?[.,;:)]*', p))
        merged = re.sub(r'[^A-Za-z]', '', core).lower()
        if len(parts) > 1 and all(ok(p) for p in parts) and not lex.real(merged) and not hun(merged):   # inVocare stays one word
            return ' '.join(re.sub(r'^(\(?[IVXLC]+)0', r'\1°', p) for p in parts)
    m = re.fullmatch(r'([IVXLC]+)%([.,;:)]*)', w)
    if m:
        return m.group(1) + 'ª' + m.group(2)
    m = re.fullmatch(r'(\(?)([0-9oil]*[0-9][0-9oil]*)([.,;:)]*)', w)
    if m and re.search(r'[oil]', m.group(2)):
        return m.group(1) + m.group(2).translate(str.maketrans('oil', '011')) + m.group(3)
    m = re.fullmatch(r'([0-9]+)"([.,;:)]*)', w)
    if m:
        return m.group(1) + '°' + m.group(2)
    if re.search(r'["\']', w) and not w.endswith(".'") and not re.match(r'[IVXLC]+["\']', w):
        v = re.sub(r'["\']', '', w)
        core = v.strip('.,;:?!()[]*')
        if not core or hun(core) or core[:1].isupper():
            w = re.sub(r'([.,;:])\1+', r'\1', v)
    lead, core, trail = re.match(r'^([(\[*]*)(.*?)([.,;:?!)\]*]*)$', w).groups()
    if re.fullmatch(r'[A-Za-z]*[a-z][A-Z]', core) and core[-1] in ALINEA and hun(core[:-1]):   # glued alinea: sitH
        return lead + core[:-1] + trail
    if re.fullmatch(r'[A-Za-z]+', core) and re.search(r'[a-z][A-Z]', core) and hun(core.lower()):
        return lead + core[0] + core[1:].lower() + trail
    for ch in '&.':
        if ch in core and re.fullmatch(r'[A-Za-z&.]+', core) and hun(core.replace(ch, '')):
            return lead + core.replace(ch, '') + trail
    return w


def pivot_part(sig):
    return sig.split(' | ')[0]


def pick(decisions, pg, k, forms=None, rule=None, skip=()):
    """The plate decision for this page+position: several may share a position (a word
    and an insertion before it), so prefer the one whose voted forms match."""
    ds = [d for d in decisions.get((pg, k), []) if d['rule'] not in skip and (rule is None or d['rule'] == rule)]
    if forms is not None:      # a coordinator's OVERRIDE on the same pivot token is the later word
        ov = [d for d in ds if d['rule'].startswith('OVERRIDE') and pivot_part(d['forms']) == pivot_part(forms)]
        if ov:
            return ov[-1]
    return next((d for d in ds if forms is None or d['forms'] == forms), ds[0] if ds else None)


def run(slug, first=None, last=None):
    off = offsets()[slug]
    item, offset = off['item'], int(off['offset'])
    first = int(first or off.get('first_page') or 1)
    last = int(last or off.get('last_page') or 9999)
    base = f'{ROOT}/text/{slug}'
    raw_pivot = load(f'{base}/witnesses/{item}.jsonl')
    # heading lines in the pivot, by (leaf, line), for structure
    head_lines = {(t['leaf'], t['line']) for t in raw_pivot if t.get('head')}
    pivot = prep(raw_pivot)
    form_count = Counter(t['n'] for t in pivot)      # recurring forms are spellings, not misreadings
    for t in pivot:
        t['pg'] = t['leaf'] - offset
        t['hl'] = (t['leaf'], t['line']) in head_lines
    others = {}
    for fn in sorted(os.listdir(f'{base}/witnesses')):
        wid = fn[:-6]
        if wid == item:
            continue
        s = prep(load(f'{base}/witnesses/{fn}'))
        others[wid] = (s, anchor_index(s))
    lex = Lexicon()
    # plate decisions (crops.py): keyed by page+pos, checked against the forms voted
    decisions = {}
    dpath = f'{base}/plate_decisions.tsv'
    if os.path.exists(dpath):
        for r in csv.DictReader(open(dpath), delimiter='\t'):
            decisions.setdefault((int(r['page']), int(r['pos'])), []).append(r)
    stale = []
    splits = {}
    # tokenfix.tsv (page, printed, fixed, note): one-off scars no rule reaches and no position can carry (2026-10-01)
    tokenfix = {}
    if os.path.exists(f'{base}/tokenfix.tsv'):
        for r in csv.DictReader(open(f'{base}/tokenfix.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
            tokenfix[(int(r['page']), r['printed'])] = r['fixed']
    if os.path.exists(f'{base}/wordsplits.tsv'):
        splits = {r['form']: r['split'] for r in csv.DictReader(open(f'{base}/wordsplits.tsv'), delimiter='\t')}
    queue, stats = [], Counter()
    hints = {w: None for w in others}
    agreed_new = set()
    for pg in range(first, last + 1):
        page = [t for t in pivot if t['pg'] == pg]
        if not page:
            continue
        per_wit, tails = {}, {}
        nxt_head = [t['n'] for t in pivot if t['pg'] == pg + 1 and not t['hl']][:4]
        for wid, (s, idx) in others.items():
            st_ = locate(page, s, idx, hints[wid])
            if st_ is None:
                continue
            votes, ins, frac, end = align_page(page, s, st_)
            if frac < 0.5:                       # this witness does not have this page
                continue
            hints[wid] = end
            per_wit[wid] = (votes, ins)
            tails[wid] = tail_run(s, end, nxt_head)
        out_tokens, checks = [], []
        head_done = set()
        for k, t in enumerate(page):
            if t['hl']:                              # chapter heading: structure, checked on the plate
                key = (t['leaf'], t['line'])
                if key not in head_done:
                    head_done.add(key)
                    htxt = ' '.join(x['t'] for x in page if (x['leaf'], x['line']) == key)
                    d = pick(decisions, pg, k, rule='HEAD')
                    if d and d['rule'] == 'HEAD':
                        checks.append((k, 'HEAD', htxt, '', '', 'plate: ' + d['reading']))
                        out_tokens.append(dict(t=d['reading'], n=norm(d['reading']), hl=True, head_fixed=key, leaf=t['leaf'], line=t['line']))
                        stats['PLATE'] += 1
                    else:
                        checks.append((k, 'HEAD', htxt, '', '', 'plate'))
                        queue.append((pg, k, 'HEAD', htxt, t['leaf'], t['box']))
                        stats['HEAD'] += 1
                        out_tokens.append(dict(t=t['t'], n=t['n'], hl=True, leaf=t['leaf'], line=t['line']))
                elif not any(x.get('head_fixed') == key for x in out_tokens):
                    out_tokens.append(dict(t=t['t'], n=t['n'], hl=True, leaf=t['leaf'], line=t['line']))
                continue
            # insertions before token k
            gap_forms = defaultdict(list)
            raw_ins = {wid: [x for x in ins[k] if not LINE_NO.match(x['n'])]
                       for wid, (votes, ins) in per_wit.items() if ins.get(k)}
            firsts = [xs[0]['n'] for xs in raw_ins.values() if xs]
            # a run of lines the pivot OCR skipped mid-page (De ecclesia p. 42): the other scans agree
            # only fuzzily, so the exact-form vote below never carries it; taken, and read on the plate
            gv = tail_vote(raw_ins, len(per_wit), lex)
            if gv:
                # most long 'insertions' are alignment noise: the pivot has the words close by
                # (or on the neighbouring page: the alignment window's slack reaches into both)
                rn = [x['n'] for x in gv[0]]
                near = ([t2['n'] for t2 in pivot if t2['pg'] == pg - 1][-(len(rn) + 80):]
                        + [x['n'] for x in page[max(0, k - len(rn) - 10):k + len(rn) + 10]]
                        + [t2['n'] for t2 in pivot if t2['pg'] == pg + 1][:len(rn) + 80])
                cover = sum(b.size for b in difflib.SequenceMatcher(None, rn, near, autojunk=False).get_matching_blocks() if b.size >= 3)
                if cover > 0.3 * len(rn):
                    gv = None
            if gv:
                run_, nsup = gv
                form = ' '.join(x['t'] for x in run_)
                d = pick(decisions, pg, k, rule='GAP')
                if d and d['rule'] == 'GAP':
                    words = [] if d['reading'] == '∅' else d['reading'].split()
                    checks.append((k, 'GAP', form, nsup, 1 + len(per_wit), 'plate: ' + d['reading']))
                    stats['PLATE'] += 1
                else:
                    words = [x['t'] for x in run_]
                    checks.append((k, 'GAP', form, nsup, 1 + len(per_wit), 'plate'))
                    queue.append((pg, k, 'GAP', form, t['leaf'], t['box']))
                    stats['GAP'] += 1
                for w in words:
                    out_tokens.append(dict(t=w, n=norm(w), ins=True))
                raw_ins = {}
            for wid, xs in raw_ins.items():
                if not xs:
                    continue
                key = ' '.join(x['n'] for x in xs)
                if len(xs) == 1 and not lex.real(xs[0]['n']):
                    g = unglue([xs[0]['n']] + firsts, lex)[0]
                    if g != xs[0]['n']:
                        key, xs = g, [dict(xs[0], n=g, t=g)]
                gap_forms[key].append((wid, xs))
            nvot = 1 + len(per_wit)
            for form, sup in gap_forms.items():
                if len(sup) * 2 > nvot:
                    rep = next((x for w, x in sup if w == 'fordham'), sup[0][1])
                    for x in rep:
                        out_tokens.append(dict(t=x['t'], n=x['n'], it=x.get('it', False), ins=True))
                    checks.append((k, 'INS', form, len(sup), nvot, 'accept'))
                    stats['INS'] += 1
                elif len(sup) >= 2:
                    d = pick(decisions, pg, k, forms=form)
                    if d and d['rule'] == 'INS?' and d['forms'] == form:
                        if d['reading'] != '∅':
                            for w in d['reading'].split():
                                out_tokens.append(dict(t=w, n=norm(w), ins=True))
                        checks.append((k, 'INS?', form, len(sup), nvot, 'plate: ' + d['reading']))
                        stats['PLATE'] += 1
                    else:
                        checks.append((k, 'INS?', form, len(sup), nvot, 'plate'))
                        queue.append((pg, k, 'INS?', form, t['leaf'], t['box']))
                        stats['INS?'] += 1
            forms = {item: t['n']}
            edge_n = 0
            raws = {item: t['t']}
            ital = None
            for wid, (votes, ins) in per_wit.items():
                v = votes[k]
                if v == 'EDGE':
                    edge_n += 1
                    continue
                if v is None:
                    continue
                if v == '∅':
                    forms[wid] = '∅'
                else:
                    forms[wid] = v['n']
                    raws[wid] = v['t']
                    if wid == 'fordham':
                        ital = v.get('it')
            rule, win, plate = decide(list(forms.values()), lex)
            if rule == 'THIN' and edge_n and lex.real(t['n']) and all(f == t['n'] for f in forms.values()):
                rule, win, plate = 'EDGE', t['n'], False     # page edge, unaligned scans: the pivot's real word
            if (rule in ('R5a', 'R6a') and form_count[win] < 4 and not t['t'][:1].isupper()
                    and not re.fullmatch(r'[ivxlcdmu]+', win) and ocr_suspect(win, lex)):
                rule, plate = 'NW', True       # every scan shares one misreading: ahquis, luxta, pnncipio
            sig = ' | '.join(f'{w}={f}' for w, f in forms.items())
            d = pick(decisions, pg, k, forms=sig, skip=('HEAD', 'INS?', 'GAP', 'TAIL'))
            if os.environ.get('W3_DUMP') == str(pg):    # print every row's forms, to write an OVERRIDE
                print(f'{pg}\t{k}\t{sig}')
            if d:   # a plate reading is the print at that box, queued now or not (OVERRIDE: corrects an accepted row)
                if pivot_part(d['forms']) == pivot_part(sig):     # the box read is the pivot's token
                    rd = d['reading']
                    if rd != '∅':     # the plate gives the word; the pivot's punctuation around it stands
                        lead = re.match(r'^[(\[]+', t['t']); trail = re.search(r'[.,;:?!)\]]+$', t['t'])
                        if lead and not rd.startswith(lead.group()):
                            rd = lead.group() + rd
                        if trail and not re.search(r'[.,;:?!)\]]$', rd):
                            rd = rd + trail.group()
                    win = '∅' if rd == '∅' else norm(rd)
                    raws = {'plate': rd}
                    rule, plate = 'PLATE', False
                else:
                    stale.append((pg, k, d['forms'], sig))
            stats[rule] += 1
            if rule in ('R1', 'R5a', 'R6a') and len(forms) >= 4:
                agreed_new.add(win)
            if rule != 'R1':
                checks.append((k, rule, ' | '.join(f'{w}={f}' for w, f in forms.items()), '', len(forms),
                               'plate' if plate else 'accept'))
            if plate:
                queue.append((pg, k, rule, ' | '.join(f'{w}={f}' for w, f in forms.items()), t['leaf'], t['box']))
            if win == '∅' and not plate:
                continue
            if win == '∅':
                win = t['n']                         # deletion pending the plate: keep the word
            if win is None:
                win = t['n']                         # provisional: pivot, pending the plate
            rawf = next((raws[w] for w in ['plate', 'fordham', item] + list(raws) if w in raws and norm(raws[w]) == win), t['t'])
            # Fordham's surface form, but the print's letter case (Fordham capitalises editorially)
            # and a space where punctuation glues two words ('nephariam,quod')
            pv = raws.get(item, '')
            if ('plate' not in raws and pv and rawf and pv[0].islower() and rawf[0].isupper()
                    and pv[1:] == rawf[1:] and pv[0] == rawf[0].lower()):
                rawf = pv
            rawf = re.sub(r'(?<=[a-z])([,;:])(?=[a-z])', r'\1 ', rawf)
            out_tokens.append(dict(t=rawf, n=win, it=bool(ital), para=t.get('para'), hl=t['hl'],
                                   pending=plate, leaf=t['leaf'], line=t['line'], pos=k))
        # the pivot's lost last lines, carried by the other scans: taken, and always read on the plate
        tv = tail_vote(tails, len(per_wit), lex)
        if tv:
            run_, nsup = tv
            k, last_t = len(page), page[-1]
            form = ' '.join(x['t'] for x in run_)
            d = pick(decisions, pg, k, rule='TAIL')
            if d and d['rule'] == 'TAIL':
                words = [] if d['reading'] == '∅' else d['reading'].split()
                checks.append((k, 'TAIL', form, nsup, 1 + len(per_wit), 'plate: ' + d['reading']))
                stats['PLATE'] += 1
            else:
                words = [x['t'] for x in run_]
                l, t_, r_, b = last_t['box']
                nl = -(-len(run_) // 8)                     # ~8 words to a line
                box = [0, t_, 10 ** 5, b + int(1.8 * nl * (b - t_))]
                checks.append((k, 'TAIL', form, nsup, 1 + len(per_wit), 'plate'))
                queue.append((pg, k, 'TAIL', form, last_t['leaf'], box))
                stats['TAIL'] += 1
            for w in words:
                out_tokens.append(dict(t=w, n=norm(w), ins=True))
        # Loserth's alinea letters (A, B, C ... in the margin) read into the text: a lone capital between a
        # sentence's end and a capitalised word (scars.py, 2026-10-01; not A I V X, which are words or numerals; L, M from 2026-10-02)
        for i in range(1, len(out_tokens) - 1):
            a_, x_, b_ = out_tokens[i - 1]['t'], out_tokens[i]['t'], out_tokens[i + 1]['t']
            if (x_ in ALINEA and a_ and a_.rstrip('*⟧')[-1:] in '.?!:' and b_.lstrip('*(⟦')[:1].isupper()
                    and not out_tokens[i].get('pending')):
                out_tokens[i]['t'] = ''
        # Loserth's page foot read into the text as a paragraph (p. 33: '24. 25. B: nunciaretur …', '34. Celestine V.,
        # the predecessor …'): a paragraph that opens with a line number and carries apparatus marks or English is
        # dropped whole (2026-10-02; a Latin paragraph never opens with an arabic line number)
        starts = [i for i, x in enumerate(out_tokens) if i == 0 or x.get('para')] + [len(out_tokens)]
        for s_, e_ in zip(starts, starts[1:]):
            para = ' '.join(x['t'] for x in out_tokens[s_:e_])
            if re.match(r'\d{1,2}\.\s', para) and (re.search(r'in marg|[Cc]odd|\b[ABD]₁?[,:]|corr\.', para) or
                    len(re.findall(r'\b(?:the|of|was|and|from|to)\b', para)) >= 2):
                for x in out_tokens[s_:e_]:
                    x['t'] = ''
        # tokenfix entries naming TWO consecutive tokens ('nec essitate' -> necessitate), for a split word whose
        # first half recurs on the page (2026-10-02)
        for i in range(len(out_tokens) - 1):
            pair = (pg, out_tokens[i]['t'] + ' ' + out_tokens[i + 1]['t'])
            if pair in tokenfix:
                out_tokens[i]['t'], out_tokens[i + 1]['t'] = tokenfix[pair], ''
        # write page
        lines, cur, cur_head = [], [], False
        prev_t = ''
        for x in out_tokens:
            x['t'] = unstar(x['t'])
            # the print's z is read as ^ \ $ (bapti^ati, cauteri\atam, Balta\ar): only in -iz-/-az- before a vowel
            x['t'] = re.sub(r'(?<=[ia])[\^\\$](?=[aeiou])', 'z', x['t'])
            x['t'] = re.sub(r'^[\^\\](?=(?:el|iz)[a-z])', 'z', x['t'])            # zelus, zeli, zizania
            x['t'] = re.sub(r'^[\^\\]+(?=[a-z]{2,}[.,;:?!)]*$)', '', x['t'])     # a mark before a word (^facit)
            # a stray mark after a whole word (fide^, Matthei^,): dropped; after a numeral it stays for the plate
            if not re.search(r'[IVXLC][\^\\]', x['t']):
                x['t'] = re.sub(r'(?<=[a-z])[\^\\]+(?=[.,;:?!)]*$)', '', x['t'])
            # a degree sign read as 0 or " after a roman numeral (XLVI0, XXI"); the old-style verse 1 read as a
            # letter right after a cited chapter ('Eccl. IX°, i' -> 1)
            x['t'] = re.sub(r'^([IVXLC]{2,}|[IVX])[0"](?=[,.;:)]*$)', r'\1°', x['t'])
            if prev_t and re.fullmatch(r'[IVXLC]+[°ª],', prev_t) and re.fullmatch(r'[iIl][.,;:)]*', x['t']):
                x['t'] = '1' + x['t'][1:]
            x['t'] = tokenfix.get((pg, x['t']), x['t'])      # coordinator's per-page token fixes (tokenfix.tsv)
            x['t'] = scar_fix(x['t'], lex)
            x['t'] = tokenfix.get((pg, x['t']), x['t'])      # and after the rules (impossibile® -> °)
            prev_t = x['t']
            core = x['t'].rstrip('.,;:?!')
            if core in splits:                  # a word-division error in a witness (wordsplits.tsv)
                x['t'] = splits[core] + x['t'][len(core):]
            if not x['t']:
                continue
            if x.get('hl'):
                if not cur_head and cur:
                    lines.append(' '.join(cur)); cur = []
                cur_head = True
                cur.append(x['t'])
                continue
            if cur_head:
                lines.append('## ' + ' '.join(cur)); cur = []; cur_head = False
            if x.get('para') and cur:
                lines.append(' '.join(cur)); lines.append(''); cur = []
            w = x['t']
            if x.get('it'):
                w = f'*{w}*'
            if x.get('pending'):
                w = f'⟦{w}⟧'
            cur.append(w)
        if cur:
            lines.append(('## ' if cur_head else '') + ' '.join(cur))
        with open(f'{base}/p{pg:03d}.la.txt', 'w') as f:
            f.write(f'[p. {pg}]\n' + '\n'.join(lines) + '\n')
        # word positions (leaf, 0-based main-text row) for citation by page.line; insertions
        # take the position of the word before them
        last = (page[0]['leaf'], page[0]['line'])
        with open(f'{base}/p{pg:03d}.tok.jsonl', 'w') as f:
            for x in out_tokens:
                if not x['t'] or x['t'] == '∅' or (x.get('n') == '∅'):
                    continue
                last = (x.get('leaf', last[0]), x.get('line', last[1]))
                for j, w in enumerate(x['t'].split()):
                    f.write(json.dumps(dict(t=w, leaf=last[0], row=last[1], para=bool(x.get('para')) and j == 0,
                                            head=bool(x.get('hl')), pos=x.get('pos')), ensure_ascii=False) + '\n')
        with open(f'{base}/p{pg:03d}.check.tsv', 'w') as f:
            f.write('pos\trule\tforms\tsupport\tvoters\tresolution\n')
            for c in checks:
                f.write('\t'.join(str(x) for x in c) + '\n')
        stats['pages'] += 1
        stats['voters'] += 1 + len(per_wit)
    with open(f'{base}/plate_queue.tsv', 'w') as f:
        f.write('page\tpos\trule\tforms\tleaf\tbox\n')
        for q in queue:
            f.write('\t'.join(str(x) for x in q[:5]) + '\t' + ','.join(str(b) for b in q[5]) + '\n')
    # grow the corpus lexicon
    p = f'{ROOT}/catalog/lexicon/agreed.txt'
    old = set(open(p).read().split()) if os.path.exists(p) else set()
    open(p, 'w').write('\n'.join(sorted(old | agreed_new)) + '\n')
    words = sum(stats[r] for r in ('R1', 'R2', 'R3a', 'R3b', 'R4a', 'R5a', 'R6a', 'EDGE', 'R3', 'R4', 'R5', 'R6', 'THIN', 'DEL', 'PLATE'))
    print(f'{slug} pp.{first}-{last}: {stats["pages"]} pages, mean voters {stats["voters"] / max(1, stats["pages"]):.1f}, {words} pivot words')
    for r in ('R1', 'R2', 'R3a', 'R3b', 'R4a', 'R5a', 'R6a', 'EDGE', 'DEL', 'INS', 'R3', 'R4', 'R5', 'R6', 'THIN', 'INS?', 'HEAD', 'TAIL', 'GAP', 'NW'):
        print(f'  {r:5} {stats[r]:6}  {100 * stats[r] / max(1, words):5.2f}%')
    print(f'  plate queue: {len(queue)}  ({1000 * len(queue) / max(1, words):.1f} per 1,000 words); '
          f'plate decisions applied: {stats["PLATE"]}; stale: {len(stale)}')
    for st_ in stale:
        print('   STALE', st_)
    return stats, queue


if __name__ == '__main__':
    run(*sys.argv[1:])
