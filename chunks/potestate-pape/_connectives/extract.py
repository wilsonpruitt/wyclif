"""Per-wave sed/autem extract (WORKFLOW stage 8): for the named chunks, the ¶ pairs (Latin + English) that
hold sed or autem; notes left out. Usage: extract.py WAVE ID [ID …]  → body-WAVE.md."""
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
wave, ids = sys.argv[1], sys.argv[2:]
pat = re.compile(r'\b(sed|autem)\b', re.I)
blocks, total = [], 0
for cid in ids:
    body = open(os.path.join(here, '..', f'wyc-potestate-pape-{cid}.md')).read()
    body = body.split('\n## Loserth')[0].split('\n## Notes')[0].split('\n## Transcription')[0]
    for sec in re.split(r'\n(?=## ¶)', body)[1:]:
        head, _, rest = sec.partition('\n')
        la = ' '.join(l[1:].strip() for l in rest.splitlines() if l.startswith('>'))
        en = '\n'.join(l for l in rest.splitlines() if l.strip() and not l.startswith('>')).strip()
        n = len(pat.findall(la))
        if n:
            total += n
            la = pat.sub(lambda m: '**' + m.group(0) + '**', la)
            blocks.append(f'### {cid} {head[3:]}  ({n} sed/autem)\n\nLATIN: {la}\n\nENGLISH: {en}\n')
open(os.path.join(here, f'body-{wave}.md'), 'w').write(
    f'# sed/autem extract, wave {wave}: chunks {" ".join(ids)}\n\n' + '\n'.join(blocks))
print(len(ids), 'chunks;', len(blocks), 'paragraphs;', total, 'occurrences')
