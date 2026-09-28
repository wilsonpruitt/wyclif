"""The print's own marginal line numbers (5, 10, 15 ...), for citing by page.line.

    .venv/bin/python scripts/w3/linemarks.py SLUG [DJVU_XML]

Reads the primary scan's djvu.xml (downloaded to text/<slug>/raw/ if not given), finds margin
groups that read as a multiple of 5, and records which main-text row (0-based, as in the
witness and .tok.jsonl files) each sits beside. Writes text/<slug>/linemarks.tsv:
    leaf  row  printed
A mark more than 2 lines from row+1 is discarded (a note number or a stray, not a line mark).
chapters.py uses the marks to correct row+1 where the extraction added or dropped a row.
"""
import csv, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import djvu

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FIX = str.maketrans({'I': '1', 'i': '1', 'l': '1', 'o': '0', 'O': '0', 'S': '5', 's': '5'})


def main(slug, xml=None):
    v = next(r for r in json.load(open(f'{ROOT}/catalog/volumes.json')) if r['slug'] == slug)
    ident = v['primary_scan']
    if not xml:
        xml = f'{ROOT}/text/{slug}/raw/{ident}_djvu.xml'
        if not os.path.exists(xml):
            os.makedirs(os.path.dirname(xml), exist_ok=True)
            subprocess.run(['curl', '-sL', '-o', xml, f'https://archive.org/download/{ident}/{ident}_djvu.xml'], check=True)
    leaves = list(djvu.parse(xml))
    W = djvu.measure(leaves)
    out, dropped = [], 0
    for lf in leaves:
        sp = djvu.split_leaf(lf, W)
        ys = [sum(w[4] for w in m) / len(m) for m in sp['main']]
        if not ys:
            continue
        for g in sp['margin']:
            t = ''.join(w[0] for w in g).strip(' .,').translate(FIX)
            if not re.fullmatch(r'(5|10|15|20|25|30|35|40)', t):
                continue
            y = sum(w[4] for w in g) / len(g)
            k = min(range(len(ys)), key=lambda i: abs(ys[i] - y))
            n = int(t)
            if abs(n - (k + 1)) <= 2:
                out.append((lf['leaf'], k, n))
            else:
                dropped += 1
    with open(f'{ROOT}/text/{slug}/linemarks.tsv', 'w') as f:
        f.write('leaf\trow\tprinted\n')
        for r in out:
            f.write('\t'.join(map(str, r)) + '\n')
    off = sum(1 for _, k, n in out if n != k + 1)
    print(f'{slug}: {len(out)} line marks ({off} disagree with row+1), {dropped} discarded')


if __name__ == '__main__':
    main(*sys.argv[1:])
