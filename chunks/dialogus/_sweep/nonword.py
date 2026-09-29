import re,glob,collections,sys
sys.path.insert(0,'scripts/w3')
from vote import Lexicon
L=Lexicon(); L.agreed=set()
hits=collections.defaultdict(list)
for f in sorted(glob.glob('text/dialogus/p*.la.txt')):
    pg=int(re.search(r'p(\d+)',f).group(1))
    for w in re.findall(r"[A-Za-zÀ-ÿæœ]+",open(f).read()):
        if len(w)<3: continue
        lw=w.lower()
        if not L.real(lw): hits[lw].append(pg)
for w,p in sorted(hits.items(), key=lambda x:(-len(x[1]),x[0])):
    print(f'{w}\t{len(p)}\t{" ".join(map(str,sorted(set(p))[:8]))}')
