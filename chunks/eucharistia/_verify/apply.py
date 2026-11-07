"""Apply a ledger RESULTS-W.md: status + how into LEDGER.md, exact note changes into the chunks.
.venv/bin/python chunks/eucharistia/_verify/apply.py 6a"""
import re, sys
W = sys.argv[1]
res = f'chunks/eucharistia/_verify/RESULTS-{W}.md'
R = open(res).read()
L = open('LEDGER.md').read()
rows = [l for l in R.split('\n') if re.match(r'\| K(?:\d\d[a-z]|prol[a-c]|pen\d\d|quest)-\d+ ', l)]
nch = 0
for r in rows:
    cells = [c.strip() for c in r.strip().strip('|').split(' | ')]
    rid, st, how, chg = cells[0], cells[1], cells[2], ' | '.join(cells[3:])
    stat = st if ('corrected' in st or 'wrong' in st) else st.split(' ')[0]
    m = re.search(r'^\| %s \| ([^|]*) \| (.*) \| [^|]* \| [^|]* \|$' % re.escape(rid), L, re.M)
    assert m, rid
    new = f'| {rid} | {m.group(1)} | {m.group(2)} | {stat} | {how.replace("|", "/")} (see `{res}`) |'
    L = L[:m.start()] + new + L[m.end():]
    want = chg.count(' → '); got = sum(len(re.findall(r'"((?:[^"\\]|\\.)*)" → "((?:[^"\\]|\\.)*)"', cm.group(2))) for cm in re.finditer(r'((?:\d\d-[a-z]|prol-[a-c]|pen\d\d|quest)) n\d+: ((?:"(?:[^"\\]|\\.)*" → "(?:[^"\\]|\\.)*"(?: and )?)+)', chg))
    if want != got: print(f'WARN {rid}: {want - got} note change(s) not parsed (unescaped quotes?) — apply by hand')
    for cm in re.finditer(r'((?:\d\d-[a-z]|prol-[a-c]|pen\d\d|quest)) n\d+: ((?:"(?:[^"\\]|\\.)*" → "(?:[^"\\]|\\.)*"(?: and )?)+)', chg):
        f = f'chunks/eucharistia/wyc-eucharistia-{cm.group(1)}.md'
        s = open(f).read()
        for old, new_ in re.findall(r'"((?:[^"\\]|\\.)*)" → "((?:[^"\\]|\\.)*)"', cm.group(2)):
            old, new_ = old.replace('\\"', '"'), new_.replace('\\"', '"')
            assert s.count(old) == 1, (rid, old)
            s = s.replace(old, new_); nch += 1
        open(f, 'w').write(s)
open('LEDGER.md', 'w').write(L)
print(len(rows), 'rows;', nch, 'note changes')
