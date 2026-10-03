"""Build the sed/autem extract for the connective check: per chunk, the ¶ pairs (Latin + English) that hold
sed or autem; notes left out. Chunks in the four-class review set are excluded. Writes body-NN.md (9 files)."""
import re, glob, os
REVIEW = set('02-b 02-f 04-b 05-d 05-f 06-a 06-d 06-g 08-f 09-a 09-c 09-e 10-b 10-c 12-b 12-c 12-d 12-e 13-a 14-g 18-c 21-d 21-f 23-h 23-k'.split())
here = os.path.dirname(os.path.abspath(__file__))
files = [f for f in sorted(glob.glob(os.path.join(here, '..', 'wyc-ecclesia-*.md')))
         if os.path.basename(f)[13:-3] not in REVIEW]
pat = re.compile(r'\b(sed|autem)\b', re.I)
blocks, total = [], 0
for f in files:
    cid = os.path.basename(f)[13:-3]
    body = open(f).read().split('\n## Loserth')[0].split('\n## Notes')[0]
    out = []
    for sec in re.split(r'\n(?=## ¶)', body)[1:]:
        head, _, rest = sec.partition('\n')
        la = ' '.join(l[1:].strip() for l in rest.splitlines() if l.startswith('>'))
        en = '\n'.join(l for l in rest.splitlines() if l.strip() and not l.startswith('>')).strip()
        n = len(pat.findall(la))
        if n:
            total += n
            la = pat.sub(lambda m: '**' + m.group(0) + '**', la)
            out.append(f'### {cid} {head[3:]}  ({n} sed/autem)\n\nLATIN: {la}\n\nENGLISH: {en}\n')
    if out:
        blocks.append((cid, '\n'.join(out)))
k = 9; per = -(-len(blocks) // k)
for i in range(k):
    part = blocks[i*per:(i+1)*per]
    if not part: continue
    open(os.path.join(here, f'body-{i+1:02d}.md'), 'w').write(
        f'# sed/autem extract {i+1:02d}: chunks {part[0][0]}–{part[-1][0]}\n\n' + '\n'.join(b for _, b in part))
print(len(files), 'chunks;', total, 'occurrences')
