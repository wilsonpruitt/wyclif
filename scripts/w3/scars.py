"""Scar sweep of the established Latin: propose fixes by rule and from the other scans, BEFORE any plate work.

    .venv/bin/python scripts/w3/scars.py SLUG        -> text/<slug>/scars.tsv + a summary

Why (2026-10-01, De ecclesia 01-b–d): the established Latin still carried OCR scars the vote let through:
  - character scars (XXIII%, 3o for 30, numerUS, est', nich.il, separa&bit, a stray ■, an alinea letter, side-note
    English such as *like* inside the Latin);
  - majority garbles (omcio for officio, lhnsti for Christi). Root cause: vote.py's Lexicon trusts
    catalog/lexicon/agreed.txt, which holds shared misreadings, so a garble two scans share counts as a word.
Nothing here edits the Latin. Each row is a proposal with its evidence; the class says how it was found:
  S-*   step 1, a character rule (no plate needed)
  W1    step 2, another scan has a dictionary word that is a known OCR confusion of the established form
  S-edge a stray capital or l/i at the end (ChristusE, manifestuml), or l/I at the start (lergo); classical dictionary
  S-J   J read for f (Jilium, Jinis)
  S-split two words run together (estvirgo), the only split into two dictionary words
  W2    step 2, no scan has it, but >=2 scans reach the same dictionary word by one known OCR confusion, and the
        established form is not the majority reading. ⚠ about half right (2026-10-01): send W2 to the plates
  LEFT-eng a scan's 'real' reading is English: a side-note word in the Latin, for the plates
  LEFT-odd / LEFT-j  (added after brief 2) digits or marks inside a word; a j inside a word. The first sweep
        skipped every non-letter token: never filter on isalpha() alone again.
  LEFT  neither: for the plates (LEFT-nw: rare non-word; LEFT-punct / LEFT-ord / LEFT-A: a mark rules cannot settle)
  PRINT every scan reads the same non-word: the print's own spelling or abbreviation; no plate
  FREQ  a non-word that recurs (>= 3 times): the print's own spelling, by the plate-read triage rule; no plate
"Dictionary word" = Hunspell OR catalog/lexicon/pl_forms.txt (the local PL, scripts/w3/pl_lexicon.py), so
medieval spellings Hunspell lacks are not scars.
Positions already read on the plate (plate_decisions.tsv) are skipped for W/LEFT, but still get S rules.
"""
import collections, csv, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from vote import Lexicon, CONFUSIONS, confusable  # noqa: E402
from pl_lexicon import OUT as PL_FORMS, key as pl_key  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SPLIT = re.compile(r'^([(\[*⟦]*)(.*?)([.,;:?!)\]*⟧]*)$')
GLYPHS = set('■|_=}{®&^\\~')
ALINEA = set('BCDEFGHJKNOPQRSTU')          # alinea letters; I V X L M are numerals, A is a word
ROMAN = re.compile(r'^[IVXLC]+$')


def variants(f):
    """Forms one known OCR confusion away from f."""
    def one(x):
        for p_, o_ in CONFUSIONS:
            i = x.find(o_)
            while i >= 0:
                yield x[:i] + p_ + x[i + len(o_):]
                i = x.find(o_, i + 1)
    out = set(one(f))                    # one step only: two steps cost ~10^4 dictionary lookups a word
    out.discard(f)
    return out


def recase(new, old):
    return new[:1].upper() + new[1:] if old[:1].isupper() else new


def main(slug):
    base = f'{ROOT}/text/{slug}'
    L = Lexicon(); L.agreed = set()                 # strict: Hunspell only (as nonword.py)
    pl = set(open(PL_FORMS).read().split()) if os.path.exists(PL_FORMS) else set()
    def real(w):                                 # Hunspell, or a form the PL holds (medieval spelling)
        w = w.lower()
        vs = L.variants(w) | {w}
        vs |= {w[:m.start()] + 'ti' + w[m.end():] for m in re.finditer(r'ci(?=[aeiou])', w)}   # one ci at a time
        return any(L.d.lookup(v) for v in vs if v) or L.real(w) or any(pl_key(v) in pl for v in vs)
    plate = set()
    with open(f'{base}/plate_decisions.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE):
            plate.add((int(r['page']), int(r['pos'])))
    side = collections.defaultdict(set)              # page -> words of its side-notes
    with open(f'{base}/sidenotes.fixed.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE):
            side[int(r['page'])].update(w.lower() for w in re.findall(r'[A-Za-z]+', r['text']))
    pages = {}
    last = LAST.get(slug, 10 ** 4)
    for p in sorted(glob.glob(f'{base}/p[0-9][0-9][0-9].tok.jsonl')):
        pg = int(re.search(r'p(\d+)', p).group(1))
        if pg > last:
            continue
        pages[pg] = [json.loads(l) for l in open(p)]
    freq = collections.Counter(SPLIT.match(t['t']).group(2).lower() for toks in pages.values() for t in toks)
    rows = []
    for pg, toks in pages.items():
        if pg % 50 == 0:
            print(f'  p. {pg}', file=sys.stderr, flush=True)
        checks = {}
        cp = f'{base}/p{pg:03d}.check.tsv'
        if os.path.exists(cp):
            with open(cp) as f:
                for r in csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE):
                    forms = [x.split('=', 1)[1] for x in r['forms'].split(' | ') if '=' in x]
                    checks.setdefault(int(r['pos']), forms)
        for i, t in enumerate(toks):
            raw, pos, line = t['t'], t.get('pos'), t.get('row')
            lead, core, trail = SPLIT.match(raw).groups()
            prev = toks[i - 1]['t'] if i else ''
            nxt = toks[i + 1]['t'] if i + 1 < len(toks) else ''
            done = (pg, pos) in plate
            def add(cls, new, ev):
                rows.append(dict(page=pg, line=line + 1 if line is not None else '', pos=pos, cls=cls,
                                 printed=raw, proposed=new, evidence=ev, plate_read='yes' if done else ''))
            # ---- step 1: character rules
            if raw and all(c in GLYPHS for c in raw):
                add('S-glyph', '∅', 'a stray mark, no letters'); continue
            m = re.fullmatch(r'([IVXLC]+)%([.,;:]*)', raw)
            if m:
                add('S-pct', m.group(1) + 'ª' + m.group(2), '% for the superscript a'); continue
            if re.fullmatch(r'[0-9oOil]+', core) and re.search(r'\d', core) and re.search(r'[oOil]', core):
                new = core.translate(str.maketrans('oOil', '0011'))
                add('S-num', lead + new + trail, 'o/i/l read for 0/1 in a numeral'); continue
            if ROMAN.match(re.sub(r'["\']+.*$', '', core) or 'x') and re.search(r'["\']', core):
                add('LEFT-ord', '', 'garbled ordinal mark after a numeral'); continue
            m = re.fullmatch(r'(\d+)"([.,;:]*)', raw)
            if m:
                add('S-deg', m.group(1) + '°' + m.group(2), '" for a degree sign after a numeral'); continue
            if re.search(r'["\']', raw):
                new = re.sub(r'["\']', '', raw)
                c2 = SPLIT.match(new).group(2)
                if re.fullmatch(r"\.'?", trail) or raw.endswith(".'"):
                    add('LEFT-punct', new, ".' : a stop or a question mark (p. 7: it was ?)"); continue
                if not c2 or real(c2):
                    add('S-quote', new or '∅', 'quote mark in the Latin (Loserth marks quotation by italics)'); continue
            if '&' in core and real(core.replace('&', '')):
                add('S-amp', lead + core.replace('&', '') + trail, '& inside a word'); continue
            if re.fullmatch(r'[a-z]+\.[a-z]+', core) and real(core.replace('.', '')):
                add('S-dot', lead + core.replace('.', '') + trail, 'stop inside a word'); continue
            if re.search(r'[a-z][A-Z]', core) and real(core.lower()):
                add('S-caps', lead + recase(core.lower(), core) + trail, 'capitals inside a word'); continue
            if (raw in ALINEA and (not prev or prev[-1:] in '.?!:') and nxt[:1].isupper()):
                add('S-alinea', '∅', "Loserth's alinea letter in the margin"); continue
            if raw == 'A' and (not prev or prev[-1:] in '.?!') and nxt[:1].isupper():
                add('LEFT-A', '', 'alinea A or the preposition'); continue
            if core and core.isalpha() and core.islower() and core in side[pg] and core in L_EN and not real(core):
                add('S-eng', '∅', "a word of this page's English side-note"); continue
            # ---- step 2: the other scans
            w = core.lower()
            if not done and core and not re.fullmatch(r"[A-Za-zæœ]+|[0-9]+°?|[IVXLCDM]+[°ªⁱᵘᵐᵗᵒˢᵛᵈ]*|[A-Za-z]+-", core):
                add('LEFT-odd', '', 'digits or marks inside a word (a glued folio/margin numeral, a broken hyphen)'); continue
            if not done and re.search(r'[a-z]j', core):
                add('LEFT-j', core.replace('j', 'i'), 'j inside a word: this edition prints i'); continue
            if done or len(w) < 3 or not w.isalpha() or real(w):
                continue
            forms = [f for f in checks.get(pos, []) if f and f != '∅']
            if not forms or all(f == w for f in forms):
                rows.append(dict(page=pg, line=line + 1 if line is not None else '', pos=pos, cls='PRINT', printed=raw,
                                 proposed='', evidence='every scan reads it: the print\'s own form', plate_read=''))
                continue
            cands = {f for f in forms if f.isalpha() and real(f) and (confusable(w, f) or confusable(f, w))}
            if cands & L_EN:
                add('LEFT-eng', '', 'reads as English (a side-note?): ' + ' | '.join(forms)); continue
            if len(cands) == 1:
                f = cands.pop()
                add('W1', lead + recase(f, core) + trail, 'scans: ' + ' | '.join(forms)); continue
            reach = collections.defaultdict(set)
            for k, f in enumerate([w] + forms):
                for v in variants(f):
                    if real(v):
                        reach[v].add(k)
            best = sorted(((len(s), v) for v, s in reach.items()), reverse=True)
            if forms.count(w) * 2 < len(forms) + 1 and best and best[0][0] >= 2 and (len(best) == 1 or best[1][0] < best[0][0]):
                v = best[0][1]
                add('W2', lead + recase(v, core) + trail, f'{best[0][0]} scans by confusion: ' + ' | '.join([w] + forms)); continue
            hun = lambda x: any(L.d.lookup(v) for v in L.variants(x.lower()) if v)   # classical dictionary only
            if re.fullmatch(r'[Jj][a-z]{2,}', core) and hun('f' + core[1:]) and not real(core):
                cap = not prev or prev[-1:] in '.?!'
                add('S-J', lead + ('F' if cap else 'f') + core[1:] + trail, 'J read for f (Jilium = filium)'); continue
            edge = None
            if len(core) >= 4 and (core[-1].isupper() or core[-1] in 'li') and core[-2].islower() and hun(core[:-1]):
                edge = core[:-1]
            elif len(core) >= 4 and core[0] in 'lI' and core[1].islower() and hun(core[1:]) and not hun(core):
                edge = core[1:]
            if edge and freq[w] < 3:
                add('S-edge', lead + edge + trail, 'a stray letter at the edge; scans: ' + ' | '.join(forms)); continue
            sp = [(core[:k], core[k:]) for k in range(2, len(core) - 1)
                  if hun(core[:k]) and hun(core[k:]) and (len(core[:k]) >= 3 or core[:k].lower() in SHORT)]
            if len(sp) == 1:
                add('S-split', lead + ' '.join(sp[0]) + trail, 'two words run together'); continue
            add('FREQ' if freq[w] >= 3 else 'LEFT-nw', '', f'x{freq[w]} in the volume; scans: ' + (' | '.join(forms) or 'unanimous'))
    out = f'{base}/scars.tsv'
    keys = ['page', 'line', 'pos', 'cls', 'printed', 'proposed', 'evidence', 'plate_read']
    with open(out, 'w') as f:
        f.write('\t'.join(keys) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[k]) for k in keys) + '\n')
    c = collections.Counter(r['cls'] for r in rows)
    print(f'{len(rows)} rows -> {out}')
    for k in sorted(c):
        print(f'  {k:11} {c[k]}')


SHORT = {'et', 'ex', 'in', 'ad', 'ab', 'de', 'si', 'ut', 'ne', 'ob', 'ac', 'nec', 'sed', 'non', 'est', 'per', 'cum', 'pro', 'sub', 'hoc', 'id'}
LAST = {'ecclesia': 587}                       # pp. 589-600 are the index (M5-RESUME)
L_EN = set()
_p = f'{ROOT}/catalog/lexicon/english_extra.txt'
if os.path.exists(_p):
    L_EN = set(open(_p).read().lower().split())
L_EN |= set('the of and that which who is are was be like as in on to a an it he his this by not no all one'.split())

if __name__ == '__main__':
    main(sys.argv[1])
