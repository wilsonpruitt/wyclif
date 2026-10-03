"""Apply a close-out LEDGER batch (_verify/batch-G.md): set each row's status and how/next-step in LEDGER.md,
and make its note change ('NN-x nN: "old" → "new"', possibly several separated by ';' or ' · ') in the chunk,
only where "old" occurs exactly once in that chunk. Usage: apply.py G [--dry]. Prints refusals."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, '..', '..', '..')
g = sys.argv[1]; dry = '--dry' in sys.argv
B = open(os.path.join(here, f'batch-{g}.md')).read()
L = open(os.path.join(root, 'LEDGER.md')).read()
STAT = {'verified', 'editor', 'untraced'}
done = ref = notes = nref = 0
for line in B.splitlines():
    if not re.match(r'\| [A-Z]\w*-\w+ \|', line): continue
    cells = [c.strip() for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]]
    rid, st, how, nc = cells[0], cells[1].lower(), cells[2], cells[3] if len(cells) > 3 else '—'
    st = st.split()[0].strip('*`') if st else st
    if st not in STAT: print('REFUSED status', rid, cells[1]); ref += 1; continue
    m = re.search(r'^\| ' + re.escape(rid) + r' \|.*$', L, re.M)
    if not m: print('REFUSED no ledger row', rid); ref += 1; continue
    lc = [c.strip() for c in m.group(0).strip().split('|')[1:-1]]
    lc[3] = st; lc[4] = how.replace('\n', ' ') + ' (close-out 2026-10-03)'
    L = L[:m.start()] + '| ' + ' | '.join(lc) + ' |' + L[m.end():]; done += 1
    if nc in ('—', '-', ''): continue
    # notes: robust parser (notefix.py); anything it cannot place exactly is left for the repair agent
    import notefix_lib as NF
    ps = list(NF.parts(nc))
    if not ps: print(f'UNPARSED {rid}: {nc[:80]}'); nref += 1; continue
    for cid, old, new in ps:
        f = os.path.join(root, 'chunks', 'ecclesia', f'wyc-ecclesia-{cid}.md'); s = open(f).read()
        if re.search(NF.flex(new), s): notes += 1; continue
        hits = list(re.finditer(NF.flex(old), s))
        if len(hits) != 1: print(f'REFUSED note {rid} {cid}: old found {len(hits)}×: {old[:60]}'); nref += 1; continue
        if not dry: open(f, 'w').write(s[:hits[0].start()] + new + s[hits[0].end():])
        notes += 1
if not dry: open(os.path.join(root, 'LEDGER.md'), 'w').write(L)
print(f'{g}: ledger rows {done} set, {ref} refused; notes {notes} changed, {nref} refused' + (' (dry)' if dry else ''))
