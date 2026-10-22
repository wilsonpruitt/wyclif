"""B+: the established Latin from a blind transcription, checked against two witnesses (WORKFLOW stage 2B).

    .venv/bin/python scripts/w3/bplus.py SLUG [FIRST LAST]

Adopted 2026-10-21 on the *De benedicta incarnacione* pilot (chunks/incarnacione/PILOT-LATIN.md): a blind
Sonnet transcription left 0 word errors in ~2,780 words, where the vote left 30 (lost foot lines, lost line
openings after a hyphen, scars, side-note leaks). Here the transcription is the text and the vote and Fordham
only check it.

Reads text/<slug>/bt/pNNN.txt (format in text/<slug>/bt/BRIEF.md), witnesses/fordham.jsonl (if the volume
has one), the vote's page tokens (text/<slug>/vote/pNNN.tok.jsonl when the volume has a BPLUS marker), the
primary witness (row boxes for crops) and bplus_decisions.tsv. Per page:

  - a transcribed word that Fordham or the vote supports is accepted;
  - a run that neither supports is accepted by rule when every counterpart is garbage: no real word, the
    same letters with other spacing (omnishome), or a cut-off fragment (secun); otherwise it is queued (SUB,
    or BT-ONLY when neither witness has anything there);
  - a run both witnesses have where the transcription has nothing is queued (OMIT): the reader skipped a line.

Writes text/<slug>/pNNN.la.txt and pNNN.tok.jsonl in the vote's format (plus `ln`, the printed line, which
chapters.py uses directly), bplus_queue.tsv in crops.py's queue format, and bplus_rules.tsv (every run ruled
by script, for audit). Decisions: bplus_decisions.tsv (page, pos, rule, forms, reading, note) from the crop
reads (`crops.py SLUG --queue bplus_queue.tsv --out crops_bplus --decisions bplus_decisions.tsv`). For SUB
and BT-ONLY, `reading` replaces the run (`∅` deletes it); for OMIT, it is inserted after `pos` (`∅` = nothing).
A decision whose `forms` no longer matches is reported as stale and re-queued.
"""
import csv, difflib, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from vote import Lexicon, confusable, norm, offsets, ROOT   # noqa: E402

LINE_NO = re.compile(r'^(\d+)\|\s*')
FOOT = re.compile(r'\^(\d+)')
TO_SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
PREFIX = {'head': '## ', 'arg': '> ', 'body': ''}
SUP = str.maketrans('ᵃᵇᶜᵈᵉⁱᵒᵘᵐᵗⁿʳˢ', 'abcdeioumtnrs')



# line-end hyphens that belong to a compound (Deus-homo), kept when the halves are joined
KEEP_HYPHEN = {'deus'}

def fold(w):
    return norm(w.translate(SUP))


def parse_page(path):
    """Transcription → list of lines: (kind, words) with kind 'head', 'arg' or 'body', plus printed marks."""
    lines = []
    for raw in open(path, encoding='utf-8'):
        s = raw.rstrip('\n').strip()
        if not s:
            continue
        mark = None
        m = LINE_NO.match(s)
        if m:
            mark, s = int(m.group(1)), s[m.end():]
        if s.startswith('# '):
            kind, s = 'head', s[2:]
        elif s.startswith('> '):
            kind, s = 'arg', s[2:]
        else:
            kind = 'body'
        para = s.startswith('¶')
        s = s.lstrip('¶').strip()
        s = s.replace(' | ', ' ').replace('|', '')          # manuscript folio bars are not text
        s = re.sub(r'(?<=\w)(\^\d+)(?=[^\W\d_])', r'\1 ', s)     # a footnote mark between two words (hec^3humanitas)
        lines.append(dict(kind=kind, mark=mark, para=para, words=s.split()))
    return lines


def tokens_of(lines, page):
    """Lines → tokens with the printed line number; line-end hyphens joined. Footnote marks become their own
    tokens (foot=True), as in the vote's text."""
    toks, ln, problems = [], 0, []
    # printed line numbers govern: Harris's margin figures do not always match a count of the body lines
    # (De incarn. p. 3: '5' beside the 4th), so the lines since the last mark shift to agree with it
    since = []
    for L in lines:
        if L['kind'] != 'body':
            L['ln'] = 0
            if L['mark'] is not None:              # Harris numbers some heading lines (De incarn. p. 105: '10' at
                ln, since = L['mark'], []          # Cap. VII.): the body goes on from there
            continue
        ln += 1
        L['ln'] = ln
        since.append(L)
        if L['mark'] is not None:
            if L['mark'] != ln:
                problems.append(f'p. {page}: printed line {L["mark"]} counted as {ln}; the print wins')
                for M in since:
                    M['ln'] += L['mark'] - ln
                ln = L['mark']
            since = []
    carry = None                                  # a hyphenated word waiting for its second half
    for L in lines:
        cur_ln = L['ln']
        for k, w in enumerate(L['words']):
            if carry is not None:                 # the second half of a line-end hyphenation
                carry['t'] += ('-' if carry.pop('keep', False) else '') + FOOT.sub('', w)
                for n in FOOT.findall(w):
                    toks.append(dict(t=n, ln=carry['ln'], para=False, head=carry['head'], foot=True))
                carry = None
                continue
            feet = FOOT.findall(w)
            base = FOOT.sub('', w)
            t = dict(t=base, ln=cur_ln, para=L['para'] and k == 0, head=L['kind'] == 'head', foot=False,
                     arg=L['kind'] == 'arg')
            if base:
                toks.append(t)
            for n in feet:
                toks.append(dict(t=n, ln=cur_ln, para=False, head=t['head'], foot=True))
            if k == len(L['words']) - 1 and base.endswith('-') and len(base) > 1 and w.endswith('-'):  # a figure before the word (`^15hu-`) still joins
                t['t'] = base[:-1]
                if t['t'].lower() in KEEP_HYPHEN:         # a compound's own hyphen, not a word split
                    t['keep'] = True
                carry = t
    # punctuation printed with a space (Harris: `est :`, `‘ Si`) belongs to a word
    merged, hold = [], ''
    for t in toks:
        if not t['foot'] and not re.search(r'\w', t['t']):
            if re.fullmatch(r'[‘“(\[]+', t['t']):
                hold += t['t']
            elif merged:
                merged[-1]['t'] += t['t']
            else:
                hold += t['t']
            continue
        if hold and not t['foot']:
            t['t'] = hold + t['t']; hold = ''
        merged.append(t)
    return merged, carry, problems


def load_witness_pages(path, key='pg'):
    pages = defaultdict(list)
    if os.path.exists(path):
        for l in open(path, encoding='utf-8'):
            t = json.loads(l)
            pages[t[key]].append(t['t'])
    return pages


def align(b, x):
    """Map transcription positions to a witness: support[i], replace runs, and inserts after i."""
    sm = difflib.SequenceMatcher(None, b, x, autojunk=False)
    support = [False] * len(b)
    sub = {}                                       # i → (i1, i2, witness words) for the block covering i
    gap = defaultdict(list)                        # i → witness words inserted after b[i] (i = -1: page head)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for i in range(i1, i2):
                support[i] = True
        elif op in ('replace', 'delete'):
            for i in range(i1, i2):
                sub[i] = (i1, i2, x[j1:j2])
        if op == 'insert':
            gap[i1 - 1].extend(x[j1:j2])
    return support, sub, gap


def garbage(counter, run, lex):
    """Is a witness's counterpart to a run plainly an OCR failure (so the transcription stands)?"""
    if not counter:
        return False
    c, r = ''.join(counter), ''.join(run)
    if c == r:                                     # same letters, other spacing (omnishome, tu genuisti)
        return True
    if len(c) >= 3 and r.startswith(c):            # cut off (secun, extran)
        return True
    if len(counter) == 1 and len(run) == 1 and (confusable(counter[0], run[0])
                                                or counter[0].replace('y', 'u') == run[0]):
        return True                                # a known OCR confusion (lesus = Iesus; Harris's V read as Y)
    # no real word the transcription lacks (footnote figures aside): partial garble around the same words
    return not any(lex.real(w) and w not in run for w in counter if not w.isdigit())


def main(slug, first=None, last=None):
    off = offsets()[slug]
    item = off['item']
    base = f'{ROOT}/text/{slug}'
    vdir = f'{base}/vote' if os.path.exists(f'{base}/BPLUS') else base
    first = int(first or off.get('first_page') or 1)
    last = int(last or off.get('last_page') or 9999)
    lex = Lexicon()
    ford = load_witness_pages(f'{base}/witnesses/fordham.jsonl')
    for pg in [p_ for p_, ws in ford.items() if re.match(r'\[?This work begins', ' '.join(ws[:4]))]:
        del ford[pg]                               # Fordham's placeholder for pages before its text
    rowbox = defaultdict(lambda: [10 ** 6, 10 ** 6, 0, 0])
    for l in open(f'{base}/witnesses/{item}.jsonl', encoding='utf-8'):
        t = json.loads(l)
        b = rowbox[(t['leaf'], t['line'])]
        l_, t_, r_, b_ = t['box']
        rowbox[(t['leaf'], t['line'])] = [min(b[0], l_), min(b[1], t_), max(b[2], r_), max(b[3], b_)]
    dec = {}
    dpath = f'{base}/bplus_decisions.tsv'
    if os.path.exists(dpath):
        for r in csv.DictReader(open(dpath, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            dec[(int(r['page']), int(r['pos']), r['rule'])] = r

    pages = sorted(int(m.group(1)) for f in os.listdir(f'{base}/bt')
                   if (m := re.fullmatch(r'p(\d+)\.txt', f)))
    parsed = {}
    for pg in pages:
        parsed[pg] = tokens_of(parse_page(f'{base}/bt/p{pg:03d}.txt'), pg)
    # a word hyphenated across pages: the whole word stands on the earlier page
    moved = {}
    for pg in pages:
        toks, carry, _ = parsed[pg]
        if carry is not None and pg + 1 in parsed and parsed[pg + 1][0]:
            nxt = parsed[pg + 1][0]
            k = next(i for i, t in enumerate(nxt) if not t['foot'])
            carry['t'] += nxt[k]['t']
            moved[pg + 1] = fold(nxt[k]['t'])      # the witnesses still have it at the head of the next page
            del nxt[k]

    queue, rules, stats = [], [], defaultdict(int)
    for pg in pages:
        if not first <= pg <= last:
            continue
        toks, _, problems = parsed[pg]
        for p_ in problems:
            print('  ', p_)
        words = [t for t in toks if not t['foot']]
        b = [fold(t['t']) for t in words]
        vtoks = []
        if os.path.exists(f'{vdir}/p{pg:03d}.tok.jsonl'):
            vtoks = [json.loads(l) for l in open(f'{vdir}/p{pg:03d}.tok.jsonl', encoding='utf-8')]
        v = [fold(t['t']) for t in vtoks]
        f = [fold(w) for w in ford.get(pg, [])]
        sF, subF, gapF = align(b, f)
        sV, subV, gapV = align(b, v)
        # transcription index → a vote token, for leaf/row (citation, side-notes, crops)
        smv = difflib.SequenceMatcher(None, b, v, autojunk=False)
        vmap = {}
        for op, i1, i2, j1, j2 in smv.get_opcodes():
            for i in range(i1, i2):
                if j2 > j1:
                    vmap[i] = min(j2 - 1, j1 + (i - i1))
        pos_of = {}                                 # word index → index in toks (decisions key on toks)
        k = 0
        for ti, t in enumerate(toks):
            if not t['foot']:
                pos_of[k] = ti; k += 1

        def where(i):
            j = next((vmap[x] for x in range(i, -1, -1) if x in vmap), None)
            if j is None:
                j = next((vmap[x] for x in range(i, len(b)) if x in vmap), None)
            return (vtoks[j]['leaf'], vtoks[j]['row']) if j is not None else (None, None)

        def enqueue(i, rule, forms):
            pos = pos_of.get(i, -1)
            d = dec.get((pg, pos, rule))
            if d and d['forms'] == forms:
                return d
            if d:
                print(f'   stale decision p. {pg} pos {pos} {rule}: re-queued')
            leaf, row = where(max(i, 0))
            box = rowbox.get((leaf, row), [0, 0, 0, 0]) if leaf is not None else [0, 0, 0, 0]
            queue.append((pg, pos, rule, forms, leaf, ','.join(str(x) for x in box)))
            stats['queued ' + rule] += 1
            return None

        replace = {}                                # word index → (end, reading) from a decision
        insert = defaultdict(list)                  # word index → words inserted after it
        i = 0
        while i < len(b):
            if sF[i] or sV[i]:
                stats['supported'] += 1
                i += 1
                continue
            j = i
            while j < len(b) and not (sF[j] or sV[j]):
                j += 1
            run = b[i:j]
            cF = subF[i][2] if i in subF else []
            cV = subV[i][2] if i in subV else []
            rw = ' '.join(t['t'] for t in words[i:j])
            have = [c for c in (cF if f else None, cV if v else None) if c is not None]
            # Fordham and the vote agreeing with each other against the transcription always go to the plate:
            # their agreement is evidence, whatever the lexicon says (De incarn. 83, 198: humanitus, a real word)
            jF, jR = ''.join(cF), ''.join(run)
            agree = bool(f and v and cF and cF == cV) and jF != jR and not (len(jF) >= 3 and jR.startswith(jF))
            if not agree and have and all(garbage(c, run, lex) for c in have if c) and any(have):
                rules.append((pg, pos_of[i], rw, ' '.join(cF), ' '.join(cV)))
                stats['ruled'] += j - i
            else:
                rule = 'BT-ONLY' if not any(have) else 'AGREE' if agree else 'SUB'
                forms = f'bt={rw} | fordham={" ".join(cF)} | vote={" ".join(cV)}'
                d = enqueue(i, rule, forms)
                if d:
                    replace[i] = (j, d['reading'])
            i = j
        for i in sorted(set(gapF) & set(gapV)):
            gf, gv = gapF[i], gapV[i]
            if i == -1 and pg in moved:            # the second half of a cross-page hyphenation
                gf = gf[1:] if gf[:1] == [moved[pg]] else gf
                gv = gv[1:] if gv[:1] == [moved[pg]] else gv
            common = [w for w in gf if w in gv and not w.isdigit()]
            # a real Latin word both have, or 3+ words of any language (the editor's English argument, De incarn.
            # p. 65: Fordham has no side-notes, so English in both is column text, not a leaked side-note)
            if not (any(lex.real(w) for w in common) or len(common) >= 3):
                continue
            forms = f'after={words[i]["t"] if i >= 0 else "^"} | fordham={" ".join(gf)} | vote={" ".join(gv)}'
            d = enqueue(i, 'OMIT', forms)
            if d and d['reading'] != '∅':
                insert[i] = d['reading'].split()

        # write the page: the transcription with decisions applied
        out, wi, ti = [], 0, 0
        if -1 in insert:
            for w in insert[-1]:
                out.append(dict(t=w, ln=toks[0]['ln'] if toks else 1, para=False, head=False, foot=False, wi=0))
        skip_to = -1
        for ti, t in enumerate(toks):
            if t['foot']:
                out.append(dict(t, wi=max(wi - 1, 0)))
                continue
            if wi < skip_to:
                wi += 1
                continue
            if wi in replace:
                end, reading = replace[wi]
                for k2, w in enumerate([] if reading == '∅' else reading.split()):
                    out.append(dict(t, t=w, para=t['para'] and k2 == 0, wi=wi))
                skip_to = end
            else:
                out.append(dict(t, wi=wi))
            for w in insert.get(wi, []):
                out.append(dict(t, t=w, para=False, wi=wi))
            wi += 1
        # the page text: a heading line `## `, an argument line `> ` (the editor's bracketed summary), body ¶s;
        # a footnote figure (Harris keys his apparatus by them) rides on the word before it as a superscript
        lines, cur, cur_kind = [], [], None
        for x in out:
            if x.get('foot'):
                if cur:
                    cur[-1] += x['t'].translate(TO_SUP)
                continue
            kind = 'head' if x['head'] else 'arg' if x.get('arg') else 'body'
            if kind != cur_kind and cur:
                lines.append(PREFIX[cur_kind] + ' '.join(cur)); cur = []
            if x['para'] and cur:
                lines.append(' '.join(cur)); lines.append(''); cur = []
            cur_kind = kind
            cur.append(x['t'])
        if cur:
            lines.append(PREFIX[cur_kind] + ' '.join(cur))
        with open(f'{base}/p{pg:03d}.la.txt', 'w', encoding='utf-8') as fh:
            fh.write(f'[p. {pg}]\n' + '\n'.join(lines) + '\n')
        with open(f'{base}/p{pg:03d}.tok.jsonl', 'w', encoding='utf-8') as fh:
            for n, x in enumerate(out):
                leaf, row = where(x['wi'])
                fh.write(json.dumps(dict(t=x['t'], leaf=leaf, row=row, ln=x['ln'], para=x['para'], head=x['head'],
                                         arg=bool(x.get('arg')), foot=bool(x.get('foot')), wi=x['wi'], pos=n),
                                    ensure_ascii=False) + '\n')
        stats['pages'] += 1
        stats['words'] += len(words)
        if not f:
            stats['pages without Fordham'] += 1

    with open(f'{base}/bplus_queue.tsv', 'w', encoding='utf-8') as fh:
        fh.write('page\tpos\trule\tforms\tleaf\tbox\n')
        for q in queue:
            fh.write('\t'.join(str(x) for x in q) + '\n')
    with open(f'{base}/bplus_rules.tsv', 'w', encoding='utf-8') as fh:
        fh.write('page\tpos\ttranscription\tfordham\tvote\n')
        for r in rules:
            fh.write('\t'.join(str(x) for x in r) + '\n')
    for k in sorted(stats):
        print(f'  {k:24} {stats[k]}')
    print(f'  queue: {len(queue)} items → bplus_queue.tsv; ruled by script: {len(rules)} runs → bplus_rules.tsv')


if __name__ == '__main__':
    main(sys.argv[1], *sys.argv[2:4])
