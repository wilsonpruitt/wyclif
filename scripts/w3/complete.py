"""Completeness test (PLAN, the M2 extraction defect): diff the established text against one full
witness for runs of >= 3 words present on one side only.  Run on every volume.

  .venv/bin/python scripts/w3/complete.py SLUG WITNESS_ID [MIN]
  -> text/SLUG/complete.WITNESS_ID.tsv   (side, established page, witness leaf, n, words, context)
"""
import csv, difflib, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from vote import ROOT, norm, load, prep


def established(slug):
    out = []
    for path in sorted(glob.glob(f'{ROOT}/text/{slug}/p[0-9][0-9][0-9].la.txt')):
        pg = int(re.search(r'p(\d+)\.la', path).group(1))
        for line in open(path):
            if re.match(r'\s*\[p\. \d+\]', line):
                continue
            for w in line.replace('⟦', ' ').replace('⟧', ' ').split():
                n = norm(w)
                if n:
                    out.append((n, w, pg))
    return out


def main(slug, wid, least=3):
    est = established(slug)
    wit = prep(load(f'{ROOT}/text/{slug}/witnesses/{wid}.jsonl'))
    a, b = [x[0] for x in est], [t['n'] for t in wit]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=True)
    rows = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        na, nb = i2 - i1, j2 - j1
        if op == 'equal' or abs(na - nb) < least:
            continue
        side = 'est-only' if na > nb else 'wit-only'
        pg = est[min(i1, len(est) - 1)][2]
        leaf = wit[min(j1, len(wit) - 1)]['leaf']
        words = ' '.join(x[1] for x in est[i1:i2]) if na > nb else ' '.join(t['t'] for t in wit[j1:j2])
        other = ' '.join(t['t'] for t in wit[j1:j2]) if na > nb else ' '.join(x[1] for x in est[i1:i2])
        rows.append((side, pg, leaf, abs(na - nb), words[:300], other[:120]))
    out = f'{ROOT}/text/{slug}/complete.{wid}.tsv'
    with open(out, 'w') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['side', 'page', 'leaf', 'n', 'words', 'other_side'])
        w.writerows(rows)
    for s in ('est-only', 'wit-only'):
        r = [x for x in rows if x[0] == s]
        print(f'{s}: {len(r)} runs, {sum(x[3] for x in r)} words')
    print(out)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3)
