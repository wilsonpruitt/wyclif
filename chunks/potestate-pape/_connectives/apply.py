"""Apply the ## Changes tables of RESULTS-NN.md: exact `was` → `now` in the named chunk, only if `was` occurs
exactly once in the chunk. Usage: apply.py NN [NN …] [--skip 04-f,12-d]. Prints applied / refused per row."""
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]; skip = set()
if '--skip' in args:
    i = args.index('--skip'); skip = set(args[i+1].split(',')); args = args[:i] + args[i+2:]
for nn in args:
    t = open(os.path.join(here, f'RESULTS-{nn}.md')).read()
    sec = t.split('## Changes', 1)[1].split('\n## ', 1)[0]
    for line in sec.splitlines():
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 6 or c[0] in ('chunk', '') or set(c[0]) <= set('-'): continue
        cid, was, now = c[0], c[3], c[4]
        tag = f'{nn} {cid} p{c[1]}'
        if cid in skip: print('SKIP   ', tag); continue
        f = os.path.join(here, '..', f'wyc-potestate-pape-{cid}.md')
        s = open(f).read(); n = s.count(was)
        if n != 1: print(f'REFUSED {tag}: "was" found {n}×: {was[:60]}'); continue
        open(f, 'w').write(s.replace(was, now)); print('applied', tag)
