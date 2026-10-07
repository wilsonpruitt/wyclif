"""Runs of words the other scans have and the established text lacks (stage 3b, after the plate pass).

    .venv/bin/python scripts/w3/lostruns.py SLUG [MIN]      → text/SLUG/lostruns.tsv (MIN words, default 3)

Why: the vote only queues a GAP where its alignment notices one, and *De potestate pape* p. 216 lost several
printed lines with no GAP queued (the plate pass found it by eye). For volumes with a Fordham witness, M2's
test (a full diff against Fordham for runs of >= 3 words) catches this class; a volume without Fordham has
only the other scans, so this diffs each page of the established text (pNNN.tok.jsonl) against each other
scan's words for that page and lists every run of MIN+ words missing from the text.

⚠ Layout errors are correlated across scans (all photograph the same page), so this catches the pivot's OWN
losses (a skipped line, a faded leaf), not losses every scan shares. A run carried by 2+ scans is reported
first; English side-note leaks and apparatus are filtered by a word test. `present` scores how much of the run
the text already has (fuzzy): rows under 0.75 are LIKELY LOST, read them on the plate; the rest are one scan's
garbled reading of words the text has (measured on De potestate pape: 1 real loss of 42 rows, at 0.21).
"""
import csv, difflib, glob, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from vote import norm, prep, load, anchor_index, locate, offsets, ROOT  # noqa: E402

EN = re.compile(r'^(the|of|and|to|is|that|in|be|by|which|it|this|as|his|not|are|he|from|with|for|was|on|an|or|but'
                r'|they|their|we|so|no|has|have|been|who|its|all|do|what|pope|power|church|christ|god)$')
NOTE = re.compile(r'^(codd|cod|marg|deest|om|corr|cf|ibid|ed|cap|lib|fol|pag)$')


def main(slug, mn=3):
    mn = int(mn)
    off = offsets()[slug]
    base = f'{ROOT}/text/{slug}'
    text = {}
    for f in sorted(glob.glob(f'{base}/p[0-9][0-9][0-9].tok.jsonl')):
        pg = int(os.path.basename(f)[1:4])
        text[pg] = [norm(t['t']) for t in load(f) if norm(t['t'])]
    found = defaultdict(dict)            # (pg, anchor word index) -> {witness: run}
    for fn in sorted(os.listdir(f'{base}/witnesses')):
        wid = fn[:-6]
        if wid == off['item'] or wid == 'fordham':
            continue
        s = prep(load(f'{base}/witnesses/{fn}'))
        idx = anchor_index(s)
        hint = None
        for pg in sorted(text):
            page = [dict(n=n) for n in text[pg]]
            st = locate(page, s, idx, hint)
            if st is None:
                continue
            lo = max(0, st - 30)
            win = s[lo:st + len(page) + 30]
            a, b = text[pg], [t['n'] for t in win]
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            blocks = [m for m in sm.get_matching_blocks() if m.size]
            if not blocks:
                continue
            hint = lo + blocks[-1].b + blocks[-1].size - len(page) // 2
            first_b, last_b = blocks[0].b, blocks[-1].b + blocks[-1].size
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op not in ('insert', 'replace') or j2 - j1 < mn:
                    continue
                if j1 < first_b or j2 > last_b:          # the window's overhang into the next/previous page
                    continue
                run = [t['t'] for t in win[j1:j2]]
                ns = [t['n'] for t in win[j1:j2]]
                if op == 'replace' and (j2 - j1) - (i2 - i1) < mn:
                    continue                             # a same-length misreading, not a loss
                near = set(text.get(pg - 1, [])[-80:]) | set(text.get(pg + 1, [])[:80])
                if sum(n in near for n in ns) >= 0.7 * len(ns):
                    continue                             # the neighbouring page's words, which the text has
                en = sum(bool(EN.match(n)) for n in ns)
                if en * 3 >= len(ns) or sum(bool(NOTE.match(n)) for n in ns) >= 2:
                    continue                             # an English side-note or the apparatus
                found[(pg, i1)][wid] = ' '.join(run)
    def present(pg, w):
        """Share of the run's letters found, in order, in the text around it: one scan's garbled reading of
        words the text HAS (italics read badly) scores 0.8+; a real loss scores low (p. 216: 0.21)."""
        q = ' '.join(n for n in (norm(x) for x in max(w.values(), key=len).split()) if n)
        hay = ' '.join(text.get(pg - 1, [])[-80:] + text[pg] + text.get(pg + 1, [])[:80])
        sm = difflib.SequenceMatcher(None, q, hay, autojunk=False)
        return sum(b.size for b in sm.get_matching_blocks()) / max(1, len(q))
    rows = sorted(((pg, i, len(w), f'{present(pg, w):.2f}', ' | '.join(f'{k}={v}' for k, v in w.items()),
                    ' '.join(text[pg][max(0, i - 4):i])) for (pg, i), w in found.items()), key=lambda r: (r[3], r[0], r[1]))
    out = f'{base}/lostruns.tsv'
    with open(out, 'w') as f:
        f.write('page\tpos\tscans\tpresent\truns\tafter\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')
    lost = [r for r in rows if float(r[3]) < 0.75]
    print(f'{len(rows)} runs of {mn}+ words absent from the text; {len(lost)} LIKELY LOST (present < 0.75, read on the plate): '
          + ', '.join(f'p. {r[0]} pos {r[1]}' for r in lost) + f' → {os.path.relpath(out, ROOT)}')


if __name__ == '__main__':
    main(*sys.argv[1:])
