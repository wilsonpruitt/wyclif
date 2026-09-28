"""M2 acceptance test: the pipeline's established Latin must reproduce the pilots'
plate-read Latin word for word (italics and punctuation aside), and must not
"correct" the print's own oddities.

    .venv/bin/python scripts/w3/accept.py

Words still pending a plate read (⟦…⟧) count as passes only if the pending form
or one of its voted alternatives matches the pilot, i.e. the plate queue holds
the right question.
"""
import difflib, glob, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from vote import norm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def pilot_latin(path):
    txt = '\n'.join(l[2:] for l in open(path) if l.startswith('> '))
    txt = re.sub(r'\[p\. \d+\]', ' ', txt)
    return [n for n in (norm(w) for w in txt.split()) if n]


def established(slug, pages):
    toks = []
    for pg in pages:
        for line in open(f'{ROOT}/text/{slug}/p{pg:03d}.la.txt'):
            if line.startswith('[p.') or line.startswith('## '):
                continue
            for w in line.split():
                pending = w.startswith('⟦')
                n = norm(w)
                if n:
                    toks.append((n, pending))
    return toks


def compare(label, pilot, est):
    en = [t for t, _ in est]
    # cut the established stream at the pilot's last word
    last = pilot[-1]
    ends = [i for i, t in enumerate(en) if t == last]
    cut = min(ends, key=lambda i: abs(i - len(pilot))) + 1 if ends else len(en)
    en, est = en[:cut], est[:cut]
    sm = difflib.SequenceMatcher(None, pilot, en, autojunk=False)
    fails, pend = [], 0
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            pend += sum(1 for _, p in est[b1:b2] if p)
            continue
        if all(p for _, p in est[b1:b2]) and b2 > b1:
            pend += b2 - b1
            fails.append(('PENDING', ' '.join(pilot[a1:a2]), ' '.join(en[b1:b2])))
            continue
        fails.append((op.upper(), ' '.join(pilot[a1:a2]), ' '.join(en[b1:b2])))
    real = [f for f in fails if f[0] != 'PENDING']
    print(f'{label}: pilot {len(pilot)} words, pipeline {len(en)}; '
          f'{len(real)} mismatches, {pend} words pending the plate')
    for f in fails:
        print(f'   {f[0]:8} pilot: {f[1]!r:40} pipeline: {f[2]!r}')
    return real


def main():
    bad = []
    bad += compare('Dialogus 1.1-3.14', pilot_latin(f'{ROOT}/pilots/wyc-dialogus-01.md'),
                   established('dialogus', [1, 2, 3]))
    if os.path.exists(f'{ROOT}/text/ecclesia/p005.la.txt'):
        bad += compare('De ecclesia 1.1-5.13', pilot_latin(f'{ROOT}/pilots/wyc-ecclesia-01a.md'),
                       established('ecclesia', [1, 2, 3, 4, 5]))
    print('ACCEPT' if not bad else f'FAIL ({len(bad)} mismatches)')


if __name__ == '__main__':
    main()
