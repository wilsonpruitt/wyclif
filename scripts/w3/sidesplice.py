"""Write each scaffold's side-note section from the corrected side-notes (WORKFLOW stage 5).

    .venv/bin/python scripts/w3/sidesplice.py SLUG [--force]

First builds text/<slug>/sidenotes.fixed.tsv (page  line  text  src) from the re-OCR
(sidenotes.ocr.tsv) and the plate reads (sidenotes.reads.part*.tsv, the side-note pass): a read
replaces, confirms (`ok`) or deletes (`∅`) its note; `+` and `M` rows add notes; a note with no
read ships as re-OCR'd (src `ocr`). Then replaces the section under
"## <Editor>'s side-notes" in chunks/<slug>/wyc-<slug>-*.md with the notes whose page.line lies
in the chunk's `pages:` span. Only scaffolds still carrying the OCR DRAFT comment are touched,
unless --force (a translated chunk is never overwritten by accident).
"""
import csv, glob, os, re, sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def tidy(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+([?;:!,])', r'\1', re.sub(r'\s+', ' ', t)).strip()


def merge(slug):
    base = f'{ROOT}/text/{slug}'
    rd = lambda p: list(csv.DictReader(open(p), delimiter='\t', quoting=csv.QUOTE_NONE))
    ocr = rd(f'{base}/sidenotes.ocr.tsv')
    reads = [r for p in sorted(glob.glob(f'{base}/sidenotes.reads.part*.tsv')) for r in rd(p)]
    by_id = defaultdict(list)
    for r in reads:
        r['line'] = (r.get('line') or '').split('.')[-1]       # `5` or `139.5`
        by_id[r['id']].append(r)
    out = []
    for i, r in enumerate(ocr, 1):
        rs = by_id.get(str(i))
        if not rs:
            out.append((int(r['page']), int(r['line']), tidy(r['text']), 'ocr'))
            continue
        x = rs[-1]
        if x['text'].strip() == '∅':
            continue
        txt = r['text'] if x['text'].strip() == 'ok' else x['text']
        out.append((int(x['page']), int(x['line']), tidy(txt), 'plate'))
    for r in reads:
        if r['id'] in ('+', 'M') and r['text'].strip() not in ('∅', 'ok', ''):
            out.append((int(r['page']), int(r['line']), tidy(r['text']), 'plate'))
    # a note the re-OCR cut at a line-break: its unread first half is dropped where the plate
    # read gives the whole note at the same page.line; likewise an unread tail (trailing specks
    # stripped) that a plate-read note within three lines already contains
    plate = [o for o in out if o[3] == 'plate']
    def covered(o):
        core = re.sub(r'(\s+\S{1,2})+$', '', o[2])
        return any(p[0] == o[0] and 0 <= o[1] - p[1] <= 3 and (p[2].startswith(o[2]) or core in p[2])
                   for p in plate)
    out = [o for o in out if not (o[3] == 'ocr' and covered(o))]
    out.sort()
    with open(f'{base}/sidenotes.fixed.tsv', 'w') as f:
        f.write('page\tline\ttext\tsrc\n')
        for o in out:
            f.write('\t'.join(map(str, o)) + '\n')
    print(f'{len(out)} notes ({sum(o[3] == "plate" for o in out)} read on the plate) -> sidenotes.fixed.tsv')
    return out


def main(slug, force=False):
    notes = [o[:3] for o in merge(slug)]
    used, n_files = set(), 0
    for path in sorted(glob.glob(f'{ROOT}/chunks/{slug}/wyc-{slug}-*.md')):
        s = open(path).read()
        if 'OCR DRAFT' not in s and not force:
            continue
        m = re.search(r'^pages: "(\d+)\.(\d+)–(\d+)\.(\d+)"', s, re.M)
        a, b = (int(m[1]), int(m[2])), (int(m[3]), int(m[4]))
        mine = [n for n in notes if a <= n[:2] <= b]
        used |= {n[:2] for n in mine}
        body = '\n'.join(f'- {p}.{l}: {t}' for p, l, t in mine)
        s2 = re.sub(r"(^## \S+'s side-notes \(PD, verbatim; not our translation\)\n).*?(?=^## Notes$)",
                    lambda mm: mm[1] + '\n' + body + ('\n\n' if body else ''), s, count=1, flags=re.S | re.M)
        if s2 != s:
            open(path, 'w').write(s2); n_files += 1
    orphans = [n for n in notes if n[:2] not in used]
    print(f'{n_files} scaffolds written; {len(notes)} notes; {len(orphans)} outside every touched span')
    for n in orphans[:20]:
        print('  orphan', n)


if __name__ == '__main__':
    main(sys.argv[1], '--force' in sys.argv)
