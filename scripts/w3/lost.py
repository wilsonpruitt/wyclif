# PROTOTYPE (2026-10-02, untested: first run found nothing on a simulated loss). Run from repo root.
"""Words most scans have that the established Latin lacks (fuzzy forms), page by page."""
import json, glob, re, sys, difflib
from collections import defaultdict
sys.path.insert(0, 'scripts/w3')
from vote import norm
W = {}
for f in sorted(glob.glob('text/ecclesia/witnesses/*.jsonl')):
    W[f.split('/')[-1][:-6]] = [n for n in (norm(json.loads(l)['t']) for l in open(f)) if n]
def find(s, key):
    k = len(key)
    return [i for i in range(len(s) - k) if s[i:i + k] == key]
pos_cache = {}
out = []
pages = int(sys.argv[2]) if len(sys.argv) > 2 else 600
for pg in range(int(sys.argv[1]) if len(sys.argv) > 1 else 1, pages):
    try:
        E = [norm(json.loads(l)['t']) for l in open(f'text/ecclesia/p{pg:03d}.tok.jsonl')]
    except FileNotFoundError:
        continue
    E = [x for e in E for x in ([e] if e else [])]
    E = [n for n in (norm(w) for t in [json.loads(l)['t'] for l in open(f'text/ecclesia/p{pg:03d}.tok.jsonl')] for w in t.split()) if n]
    if len(E) < 20: continue
    ins = defaultdict(list)   # position in E -> [(wit, form)]
    for w, s in W.items():
        a = find(s, E[:4]); b = find(s, E[-4:])
        if len(a) != 1 or len(b) != 1 or not (0 < b[0] - a[0] < 3 * len(E)): continue
        seg = s[a[0]: b[0] + 4]
        sm = difflib.SequenceMatcher(None, E, seg, autojunk=False)
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op == 'insert' or (op == 'replace' and b2 - b1 > a2 - a1):
                extra = seg[b1:b2] if op == 'insert' else seg[b1 + (a2 - a1):b2]
                for x in extra[:2]:
                    if re.fullmatch(r'[a-z]{2,}', x):
                        ins[a1].append((w, x))
    for p, lst in ins.items():
        wits = {w for w, _ in lst}
        if len(wits) < 4: continue
        forms = [x for _, x in lst]
        best = max(forms, key=lambda c: sum(difflib.SequenceMatcher(None, c, y).ratio() >= 0.7 for y in forms))
        sup = {w for w, x in lst if difflib.SequenceMatcher(None, best, x).ratio() >= 0.7}
        if len(sup) >= 4:
            out.append((pg, p, best, len(sup), ' '.join(E[max(0, p - 4):p]) + ' [_] ' + ' '.join(E[p:p + 3])))
for r in out: print(*r, sep='\t')
