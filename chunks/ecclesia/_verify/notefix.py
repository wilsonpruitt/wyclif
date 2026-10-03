"""Robust re-parse of batch note changes (the first apply.py cut text at inner straight quotes and silently
skipped unparsed cells). For each part 'NN-x nN: "old" → "new"': report OK (new present), APPLY (old present,
new absent), or DAMAGED (neither). Usage: notefix.py G [G …] [--apply]."""
import re, sys, os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
apply_ = '--apply' in sys.argv
def flex(t):  # whitespace-insensitive literal pattern ('…' never a wildcard here)
    return r'\s+'.join(re.escape(w) for w in t.split())
def parts(nc):
    for p in re.split(r'(?:;\s*|\s+·\s+|\s+)(?=\d\d-[a-z][^:"]{0,40}:\s*")', nc):
        m = re.match(r'\s*(\d\d-[a-z])[^:"]{0,40}:\s*"', p)
        if not m or '" → "' not in p: continue
        a, b = p[m.end():].split('" → "', 1)
        b = b.rstrip().rstrip('.').rstrip()
        if b.endswith('"'): b = b[:-1]
        yield m.group(1), a.replace('\\"', '"'), b.replace('\\"', '"')
for g in [a for a in sys.argv[1:] if not a.startswith('--')]:
    for line in open(os.path.join(root, f'chunks/ecclesia/_verify/batch-{g}.md')):
        if not re.match(r'\| [A-Z]\w*-\w+ \|', line): continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]]
        nc = cells[3] if len(cells) > 3 else ''
        if nc in ('—', '-', ''): continue
        ps = list(parts(nc))
        if not ps: print(f'UNPARSED {g} {cells[0]}: {nc[:90]}'); continue
        for cid, old, new in ps:
            f = os.path.join(root, f'chunks/ecclesia/wyc-ecclesia-{cid}.md'); s = open(f).read()
            if re.search(flex(new), s): continue
            h = list(re.finditer(flex(old), s))
            if len(h) == 1:
                print(f'APPLY   {g} {cells[0]} {cid}')
                if apply_: s = s[:h[0].start()] + new + s[h[0].end():]; open(f, 'w').write(s)
            else: print(f'DAMAGED {g} {cells[0]} {cid} (old {len(h)}×): {old[:60]}')
