"""Paragraph and chunk boundaries that fall inside a sentence (stage 5, before translation).

    python3 scripts/w3/boundaries.py SLUG            → text/SLUG/boundaries.tsv (and a count)

Lists every ¶ block in chunks/SLUG/*.md whose Latin does not end with a stop (. ? ! : ;). Each is either a
false ¶ break (an alinea letter or side-note read as a break: *De ecclesia* lost *plus* at 46.24 this way),
a chunk split inside a sentence (12-c ends on *patet*), or legitimate (verse lines, a heading). Read every
row on the plate in the stage-5 plate pass; fix false breaks before the brief is built, not at close-out.
"""
import glob, os, re, sys

slug = sys.argv[1]
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
rows = []
for f in sorted(glob.glob(f'{root}/chunks/{slug}/wyc-{slug}-*.md')):
    cid = os.path.basename(f)[len(f'wyc-{slug}-'):-3]
    body = open(f).read().split('\n## Loserth')[0].split('\n## Notes')[0]
    secs = re.split(r'\n(?=## ¶)', body)[1:]
    for i, sec in enumerate(secs):
        la = ' '.join(l[1:].strip() for l in sec.splitlines() if l.startswith('>')).strip()
        la = re.sub(r'\s*\[p\. \d+\]\s*$', '', la)
        # a stop may be followed by a closing quote/bracket and, in a B+ volume, the editor's footnote figure (⁷)
        if la and not re.search(r'[.?!:;][\'’"»”)\]⁰-⁹¹²³*†]*$', la):
            kind = 'chunk end' if i == len(secs) - 1 else '¶ end'
            rows.append((cid, sec.split('\n')[0][3:].strip(), kind, la[-50:]))
        # a ¶ that opens in lower case: a false break even after a stop. In De pot. pape every one marked a line
        # whose FIRST word the side-note box had swallowed (in all scans alike), the shortened line reading as an
        # indent (2026-10-07: qui 76, in 106, Petri 142, sic 382); the lost word is on the plate, not in any scan.
        first = re.sub(r'^\[p\. \d+\]\s*', '', la)
        if i and first[:1].islower():
            rows.append((cid, sec.split('\n')[0][3:].strip(), 'lower-case ¶', first[:50]))
out = f'{root}/text/{slug}/boundaries.tsv'
with open(out, 'w') as w:
    w.write('chunk\tparagraph\tkind\tlast words\n')
    for r in rows:
        w.write('\t'.join(r) + '\n')
print(f'{len(rows)} boundaries without a stop → {os.path.relpath(out, root)}')
