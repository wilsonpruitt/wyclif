# Page-head lost-word sweep (2026-10-02): the word most scans have just before each page's first words.
# Noisy (apparatus, running heads): 7 candidates -> 1 real (p. 431). Run from repo root.
import json, glob, re, sys
from collections import Counter
sys.path.insert(0, 'scripts/w3')
from vote import norm
W = {}
for f in glob.glob('text/ecclesia/witnesses/*.jsonl'):
    toks = [norm(json.loads(l)['t']) for l in open(f)]
    W[f.split('/')[-1][:-6]] = [t for t in toks if t]
idx = {w: {} for w in W}
for w, s in W.items():
    for i in range(len(s) - 2):
        idx[w].setdefault((s[i], s[i+1], s[i+2]), []).append(i)
out = []
for pg in range(1, 600):
    try: t = [norm(json.loads(l)['t']) for l in open(f'text/ecclesia/p{pg:03d}.tok.jsonl')]
    except FileNotFoundError: continue
    t = [x for x in t if x]
    if len(t) < 4: continue
    try: prev = [norm(json.loads(l)['t']) for l in open(f'text/ecclesia/p{pg-1:03d}.tok.jsonl')]
    except FileNotFoundError: prev = []
    prev = [x for x in prev if x]
    key = tuple(t[:3]); before = Counter()
    for w, s in W.items():
        hits = idx[w].get(key, [])
        if len(hits) != 1: continue
        i = hits[0]
        if i and s[i-1] not in (prev[-1:] or ['']) and re.fullmatch(r'[a-z]+', s[i-1]):
            before[s[i-1]] += 1
    if before:
        w0, n = before.most_common(1)[0]
        if n >= 3: out.append((pg, w0, n, ' '.join(t[:4]), prev[-1] if prev else ''))
for r in out: print(*r, sep='\t')
