"""Apply a verification batch: replace LEDGER rows by id; apply '### ... `file`' Current/Replacement pairs.
   .venv/bin/python chunks/dialogus/_verify/apply.py chunks/dialogus/_verify/batchN.md [--dry]"""
import re, sys, textwrap
src, dry = sys.argv[1], '--dry' in sys.argv
B = open(src).read()
rows = {l.split('|')[1].strip(): l for l in B.splitlines() if re.match(r'^\| [A-Z][A-Z0-9]*-\d', l)}
led = open('LEDGER.md').read().splitlines()
n = 0
for i, l in enumerate(led):
    m = re.match(r'^\| ([A-Z][A-Z0-9]*-\d+) ', l)
    if m and m.group(1) in rows:
        led[i] = rows.pop(m.group(1)); n += 1
print(f'ledger rows replaced: {n}; unmatched: {sorted(rows)}')
if not dry: open('LEDGER.md', 'w').write('\n'.join(led) + '\n')
for sec in re.split(r'\n### ', B.split('## Chunk corrections', 1)[-1])[1:]:
    fm = re.search(r'`(wyc-dialogus-[\w-]+\.md)`', sec)
    cur = re.search(r'\*\*Current:\*\* `(.*?)`\n', sec, re.S)
    rep = re.search(r'\*\*Replacement:\*\* `(.*?)`\n', sec, re.S)
    head = sec.splitlines()[0]
    if not (fm and cur and rep):
        print('SKIP (manual):', head); continue
    path = f'chunks/dialogus/{fm.group(1)}'
    txt = open(path).read()
    pat = r'\s+'.join(re.escape(w) for w in cur.group(1).split())
    hits = list(re.finditer(pat, txt))
    if len(hits) != 1:
        print(f'SKIP ({len(hits)} matches):', head); continue
    h = hits[0]
    # re-wrap only if the matched span was wrapped
    new = rep.group(1)
    if '\n' in h.group(0):
        linestart = txt.rfind('\n', 0, h.start()) + 1
        first = h.start() - linestart
        w = textwrap.fill(' ' * first + new, width=110, subsequent_indent='    ', break_long_words=False, break_on_hyphens=False)
        new = w[first:]
    txt = txt[:h.start()] + new + txt[h.end():]
    print('applied:', head)
    if not dry: open(path, 'w').write(txt)
