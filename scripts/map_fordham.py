"""Match each Fordham transcription to the Princeton latinworks scan it came from,
by shared 6-word shingles (OCR on both sides, so we count hits rather than demand exact runs)."""
import re, glob, os, random, json
norm = lambda s: re.sub(r'[^a-z ]', ' ', s.lower().replace('j','i').replace('v','u'))
def shingles(words, n=6): return {' '.join(words[i:i+n]) for i in range(len(words)-n)}
ia = {}
for f in sorted(glob.glob('sources/ia-ocr/latinworks*.txt')):
    ia[os.path.basename(f)[:-4]] = shingles(norm(open(f, errors='ignore').read()).split())
out = {}
for f in sorted(glob.glob('sources/fordham/*.md')):
    t = re.sub(r'\[p\. \d+\]', ' ', open(f).read())
    s = list(shingles(norm(t).split())); random.seed(1); samp = random.sample(s, min(400, len(s)))
    scores = sorted(((sum(x in v for x in samp) / len(samp), k) for k, v in ia.items()), reverse=True)
    pages = [int(p) for p in re.findall(r'^\[p\. (\d+)\]', open(f).read(), re.M)]
    out[os.path.basename(f)] = dict(best=scores[0][1], hit=round(scores[0][0], 3), runner=scores[1][1], runner_hit=round(scores[1][0], 3), first_page=min(pages), last_page=max(pages))
    print(f"{os.path.basename(f):48} {scores[0][1]} {scores[0][0]:.2f}  (next {scores[1][1]} {scores[1][0]:.2f})  pp. {min(pages)}-{max(pages)}")
json.dump(out, open('catalog/fordham_map.json', 'w'), indent=1)
