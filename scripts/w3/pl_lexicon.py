"""Medieval-Latin form list from the local Patrologia Latina, an INDEPENDENT lexicon for the scar sweep.

    python3 scripts/w3/pl_lexicon.py        -> catalog/lexicon/pl_forms.txt (one key per line, seen >= 2 times)

Why (2026-10-01): Hunspell is classical, so it rejects genuine medieval forms (morsellum, yemps, cauterizatam) and
the scar sweep cannot tell them from OCR garbles. The PL (~/patrologia/sources/pl/tei, 673 MB) is keyed text from a
different edition and a different OCR, so a form it holds is Latin, not our scans' shared misreading (unlike
agreed.txt). Keys are lower case with j->i and v->u (key() below); look a form up through key() too.
"""
import collections, glob, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PL = os.path.expanduser('~/patrologia/sources/pl/tei')
OUT = f'{ROOT}/catalog/lexicon/pl_forms.txt'
TAG = re.compile(r'<[^>]*>')
WORD = re.compile(r'[A-Za-zæœÆŒ]{2,}')


def key(w):
    return w.lower().replace('j', 'i').replace('v', 'u').replace('æ', 'ae').replace('œ', 'oe')


def main():
    c = collections.Counter()
    files = sorted(glob.glob(f'{PL}/*.xml'))
    for n, p in enumerate(files):
        with open(p, encoding='utf-8', errors='replace') as f:
            c.update(key(w) for w in WORD.findall(TAG.sub(' ', f.read())))
        if n % 500 == 0:
            print(f'  {n}/{len(files)} files, {len(c)} forms', file=sys.stderr, flush=True)
    keep = sorted(w for w, k in c.items() if k >= 2)
    with open(OUT, 'w') as o:
        o.write('\n'.join(keep) + '\n')
    print(f'{len(keep)} forms (of {len(c)}) -> {OUT}')


if __name__ == '__main__':
    main()
