"""Shared parser for close-out note changes (see notefix.py)."""
import re
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
