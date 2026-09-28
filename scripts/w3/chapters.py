"""Cut a volume's established Latin into chapter chunk scaffolds (CONVENTIONS §§1, 2, 13).

    .venv/bin/python scripts/w3/chapters.py SLUG [--force]

Reads text/<slug>/pNNN.tok.jsonl (vote.py), linemarks.tsv (linemarks.py), the primary witness
(row positions), sidenotes/<slug>.tsv and plate_decisions.tsv, and writes one scaffold per
chapter to chunks/<slug>/wyc-<slug>-NN.md: front matter filled mechanically, the Latin by the
editor's paragraphs with page.line ranges and [p. N] breaks, an [ENGLISH] slot after each, the
editor's side-notes as an OCR DRAFT keyed to page.line, and the transcription notes the pipeline
knows (plate readings, omitted margin matter). The translator fills the English, the notes, the
title and the headnote, and corrects the side-note draft.

A scaffold that already exists is never overwritten without --force (it may hold a translation).
"""
import csv, glob, json, os, re, statistics as st, sys
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
META = {  # per volume: what the scaffold cannot derive
    'dialogus': dict(work_la='Dialogus sive Speculum ecclesie militantis',
                     work_en='Dialogue, or The Mirror of the Church Militant',
                     short='Dial.', editor='Alfred W. Pollard', year=1886, label='Dialogus',
                     # a heading the extraction drops (a half-title read as a running head), checked on the plate
                     extra_heads=[(86, 'EPILOGUS', 'epil', 'Epilogus')]),
}
MS_MARK = re.compile(r'^[A-D][¹1l]?\s*\.?\s*\d{1,3}\s*[a-d]\s*\.?$|^\d{2,3}\s*[a-d]?\s*\.$')
BOOKS = ('Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Ruth', 'Sam', 'Kings', 'Chron', 'Ezra',
         'Neh', 'Esth', 'Job', 'Ps', 'Prov', 'Eccl', 'Cant', 'Isa', 'Jer', 'Lam', 'Ezek', 'Dan', 'Hos',
         'Joel', 'Amos', 'Obad', 'Jon', 'Mic', 'Nah', 'Hab', 'Zeph', 'Hag', 'Zech', 'Mal', 'Macc', 'Matt',
         'Mark', 'Luke', 'John', 'Acts', 'Rom', 'Cor', 'Gal', 'Eph', 'Phil', 'Col', 'Thess', 'Tim',
         'Tit', 'Philem', 'Heb', 'James', 'Pet', 'Jude', 'Rev', 'Apoc', 'Isaiah', 'Malachi', 'Ecclesiasti',
         'Greg', 'Aug', 'Past', 'Decret', 'Grat')


def pg_line(marks, offset, leaf, row):
    """Printed page.line for a main-text row, corrected by the nearest printed line mark."""
    ms = marks.get(leaf, [])
    above = [(r, n) for r, n in ms if r <= row]
    ref = max(above) if above else (min(ms) if ms else None)
    off = (ref[1] - (ref[0] + 1)) if ref else 0
    return leaf - offset, row + 1 + off


def main(slug, force=False):
    meta = META[slug]
    off = {r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t')}[slug]
    item, offset = off['item'], int(off['offset'])
    base = f'{ROOT}/text/{slug}'
    marks = defaultdict(list)
    if os.path.exists(f'{base}/linemarks.tsv'):
        for r in csv.DictReader(open(f'{base}/linemarks.tsv'), delimiter='\t'):
            marks[int(r['leaf'])].append((int(r['row']), int(r['printed'])))
    # row baselines of the primary scan, to place side-notes
    rowy = defaultdict(list)
    for l in open(f'{base}/witnesses/{item}.jsonl'):
        t = json.loads(l)
        rowy[(t['leaf'], t['line'])].append(t['box'][3])
    rowy = {k: st.median(v) for k, v in rowy.items()}
    witnesses = sorted(os.path.basename(p)[:-6] for p in glob.glob(f'{base}/witnesses/*.jsonl'))

    toks = []
    for p in sorted(glob.glob(f'{base}/p*.tok.jsonl')):
        pg = int(re.search(r'p(\d+)\.tok', p).group(1))
        for l in open(p):
            t = json.loads(l)
            t['pg'] = pg
            t['page'], t['ln'] = pg_line(marks, offset, t['leaf'], t['row'])
            toks.append(t)
    # chapters: split at heading runs that begin with CAPITULUM
    chapters, cur, head = [], [], None
    i = 0
    while i < len(toks):
        t = toks[i]
        numbered = (t['t'].upper() == 'CAPITULUM' and i + 1 < len(toks)
                    and re.fullmatch(r'[0-9IVXLivxl]+[°m.ᵐ]*\.?', toks[i + 1]['t']))
        if (t['head'] and t['t'].upper().startswith('CAPITUL')) or numbered:
            j = i + 1
            while j < len(toks) and (toks[j]['head'] or (numbered and j == i + 1)):
                j += 1
            if cur or head:
                chapters.append((head, cur))
            head = (' '.join(x['t'] for x in toks[i:j]), toks[i])
            cur = []
            i = j
            continue
        if not t['head']:
            cur.append(t)
        i += 1
    chapters.append((head, cur))

    def paras_of(body):
        ps, c = [], []
        for t in body:
            if t['para'] and c:
                ps.append(c); c = []
            c.append(t)
        return ps + ([c] if c else [])

    sections = []                       # (id, title label, divisions text, heading, paragraphs)
    for n, (head, body) in enumerate(chapters, 1):
        cut = None
        for pg, htxt, tag, lab in meta.get('extra_heads', []):
            k = next((i for i, t in enumerate(body) if t['pg'] == pg), None)
            if k:
                cut = (k, htxt, tag, lab)
        parts = [(f'{n:02d}', f'chapter {n}',
                  f"cap. {n}" + (f" (heading '{head[0]}' at {head[1]['page']}.{head[1]['ln']})" if head else ' (unheaded in print)'),
                  head, body[:cut[0]] if cut else body)]
        if cut:
            k, htxt, tag, lab = cut
            parts.append((tag, lab, f"{lab} (heading '{htxt}' above {body[k]['page']}.{body[k]['ln']}, read on the plate)",
                          None, body[k:]))
        for cid, lab, divs, hd, bd in parts:
            ps = paras_of(bd)
            span_pages = bd[-1]['page'] - bd[0]['page'] + 1
            k = -(-span_pages // 7) if span_pages > 8 else 1      # CONVENTIONS §1: split long ones at ¶
            if k == 1 or len(ps) < 2:
                sections.append((cid, lab, divs, hd, ps)); continue
            total = sum(len(x) for x in ps); groups, acc, g = [], 0, []
            for x in ps:
                g.append(x); acc += len(x)
                if acc >= total * (len(groups) + 1) / k and len(groups) < k - 1:
                    groups.append(g); g = []
            if g:
                groups.append(g)
            for j, g in enumerate(groups):
                sections.append((f'{cid}-{"abcdefgh"[j]}', f'{lab}, part {j + 1}',
                                 divs + f"; part {j + 1} of {len(groups)}, split at the editor's ¶ (CONVENTIONS §1)",
                                 hd if j == 0 else None, g))

    decisions = list(csv.DictReader(open(f'{base}/plate_decisions.tsv'), delimiter='\t'))
    checks = {}
    for p in glob.glob(f'{base}/p*.check.tsv'):
        pg = int(re.search(r'p(\d+)\.check', p).group(1))
        checks[pg] = [r for r in csv.DictReader(open(p), delimiter='\t')]
    notes = [r for r in csv.DictReader(open(f'{ROOT}/sidenotes/{slug}.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE)]

    OUT = os.environ.get('CHUNKS_OUT', f'{ROOT}/chunks/{slug}')
    os.makedirs(OUT, exist_ok=True)
    for cid, lab, divs, head, paras in sections:
        body = [t for p_ in paras for t in p_]
        path = f'{OUT}/wyc-{slug}-{cid}.md'
        if os.path.exists(path) and not force:
            print('keep', os.path.basename(path)); continue
        first, last = body[0], body[-1]
        span = f"{first['page']}.{first['ln']}–{last['page']}.{last['ln']}"
        # check counts over the pivot positions this chapter covers, page by page
        rng = defaultdict(lambda: [10 ** 9, -1])
        for t in body:
            if t.get('pos') is not None:
                r = rng[t['pg']]; r[0] = min(r[0], t['pos']); r[1] = max(r[1], t['pos'])
        rules = Counter()
        for pg, (a, b) in rng.items():
            for r in checks.get(pg, []):
                if a <= int(r['pos']) <= b:
                    rules[r['rule']] += 1
        plate = [d for d in decisions if int(d['page']) in rng and rng[int(d['page'])][0] <= int(d['pos']) <= rng[int(d['page'])][1]
                 or (head and d['rule'] == 'HEAD' and int(d['page']) == head[1]['pg'])]
        words = len(body)
        settled = sum(v for k, v in rules.items() if k in ('R2', 'R3a', 'R3b', 'R5a', 'R6a', 'DEL', 'INS'))
        leaves = sorted({t['leaf'] for t in body})
        out = ['---', f'chunk_id: wyc-{slug}-{cid}', f"work_la: {meta['work_la']}", f"work_en: {meta['work_en']}",
               f'volume_slug: {slug}', f"editor: {meta['editor']}", f"year: {meta['year']}", f'pages: "{span}"',
               f'divisions: "{divs}"',
               'latin_source: three-witness', f'witnesses: [{", ".join(witnesses)}]',
               f'check: "{words} words; {words - settled - len(plate)} unanimous or majority-real; {settled} settled by vote '
               f'({", ".join(f"{k} {v}" for k, v in sorted(rules.items()) if k in ("R2", "R3a", "R3b", "R5a", "R6a", "DEL", "INS"))}); '
               f'{len(plate)} read on the plate (see Transcription notes)"',
               'italics: none', f'plates: "archive.org {item}, leaves n{leaves[0]}–n{leaves[-1]} (printed p. = leaf − {offset})"',
               'status: draft', '---', '', f"# *{meta['label']}*, {lab}: [TITLE]", '']
        if cid == '01':
            out += ['## Headnote', '', '[HEADNOTE: see pilots/wyc-dialogus-01.md]', '']
        for k, par in enumerate(paras, 1):
            a, b = par[0], par[-1]
            out.append(f"## ¶{k} · {a['page']}.{a['ln']}–{b['page']}.{b['ln']}")
            out.append('')
            words, pg = [], None
            for t in par:
                if t['page'] != pg:
                    if pg is not None or t is not body[0]:
                        words.append(f"[p. {t['page']}]")
                    pg = t['page']
                words.append(t['t'])
            if words and words[0].startswith('[p.'):
                words = words[1:] if a is body[0] else words
            text = ' '.join(words)
            if a is body[0]:
                text = f"[p. {a['page']}] " + text
            out += ['> ' + text, '', '[ENGLISH]', '']
        # side-notes: group lines, place at page.line
        pages = {t['leaf'] for t in body}
        grp, groups = [], []
        rows_by_leaf = defaultdict(list)
        for (lf, rw), y in rowy.items():
            rows_by_leaf[lf].append((y, rw))
        for r in notes:
            lf, y, x, txt = int(r['leaf']), float(r['y']), float(r['x']), r['text'].strip()
            if lf not in pages:
                continue
            if grp and lf == grp[-1][0] and abs(x - grp[-1][2]) < 80 and y - grp[-1][1] < 70:
                grp.append((lf, y, x, txt))
            else:
                if grp:
                    groups.append(grp)
                grp = [(lf, y, x, txt)]
        if grp:
            groups.append(grp)
        side, margin = [], []
        for g in groups:
            lf, y = g[0][0], g[0][1]
            txt = ''
            for _, _, _, s in g:
                s = re.sub(r'\s+\d{1,2}\s*$', '', s)          # a glued line number
                txt = txt[:-1] + s if txt.endswith('-') else (txt + ' ' + s).strip()
            ry = min(rows_by_leaf.get(lf, [(y, 0)]), key=lambda v: abs(v[0] - y))[1]
            pgl = pg_line(marks, offset, lf, ry)
            where = f'{pgl[0]}.{pgl[1]}'
            if MS_MARK.match(txt) or re.fullmatch(r'[\d\s.]+', txt):
                margin.append(f'MS mark {txt} ({where})')
            elif any(txt.startswith(b) or f' {b}' in txt[:14] for b in BOOKS) and len(txt) < 40:
                margin.append(f'reference {txt} ({where})')
            else:
                side.append(f'- {where}: {txt}')
        out += [f"## {meta['editor'].split()[-1]}'s side-notes (PD, verbatim; not our translation)", '',
                '<!-- OCR DRAFT, grouped by machine: correct every note against the plate (leaf images in',
                f'     text/{slug}/raw/leaves/ or archive.org/download/{item}/page/nLEAF.jpg), fix the',
                '     page.line where a note is misplaced, and delete this comment. -->', ''] + side + ['']
        out += ['## Notes', '', '## Transcription notes', '']
        if plate:
            out.append('- **Plate readings** (CONVENTIONS §3.4; page · reading · note):')
            for d in plate:
                out.append(f"  - {d['page']}: *{d['reading']}*" + (f" ({d['note']})" if d['note'] else '') + f" [{d['rule']}]")
        if margin:
            out.append('- **Omitted per §3.5 / kept in the English** (margin matter): ' + '; '.join(margin) + '.')
        out.append('')
        open(path, 'w').write('\n'.join(out))
        print(f"wrote {os.path.basename(path)}: {span}, {len(body)} words, {len(paras)} ¶, {len(side)} side-notes, {len(plate)} plate")


if __name__ == '__main__':
    main(sys.argv[1], '--force' in sys.argv)
