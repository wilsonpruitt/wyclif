"""Majority-error sweep: every word of the established Latin that Hunspell-Latin rejects (CONVENTIONS §3).

    .venv/bin/python scripts/w3/nonword.py SLUG            -> text/<slug>/nonwords.tsv (form, count, pages)

⚠ catalog/lexicon/agreed.txt is NOT used: it is built from forms the witnesses agreed on, so it contains the
very majority errors this sweep hunts (it holds *chnstus*). Most hits are genuine medieval spellings; read the
rest on the plates (the Dialogus: 514 forms -> 37 candidates -> 1 real error, 29.26 [vi]dentur).
"""
import collections, glob, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from vote import Lexicon

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def main(slug):
    L = Lexicon(); L.agreed = set()
    hits = collections.defaultdict(list)
    for f in sorted(glob.glob(f'{ROOT}/text/{slug}/p*.la.txt')):
        pg = int(re.search(r'p(\d+)', os.path.basename(f)).group(1))
        for w in re.findall(r"[A-Za-zÀ-ÿæœ]+", open(f).read()):
            if len(w) >= 3 and not L.real(w.lower()):
                hits[w.lower()].append(pg)
    out = f'{ROOT}/text/{slug}/nonwords.tsv'
    with open(out, 'w') as o:
        o.write('form\tcount\tpages\n')
        for w, p in sorted(hits.items(), key=lambda x: (-len(x[1]), x[0])):
            o.write(f'{w}\t{len(p)}\t{" ".join(map(str, sorted(set(p))))}\n')
    print(f'{len(hits)} forms -> {out}')


if __name__ == '__main__':
    main(sys.argv[1])
