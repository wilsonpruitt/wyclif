"""Rebuild Fordham-style .md files from sources/fordham/data/data.json
(= `node sources/fordham/extract_wyclif.js` run on the site's main-es2015.*.js, fetched 2026-09-28).

usage: python3 scripts/fordham_to_md.py SLUG [OUT.md]   # SLUG = manuscript.title slug, e.g. opera-minora
"""
import json, sys
d = json.load(open('sources/fordham/data/data.json'))
title = next(t for t in d['manuscript.title'] if t['fields']['slug'] == sys.argv[1])
page_no = {p['pk']: p['fields']['number'] for p in d['manuscript.page']}
chapters = sorted((c for c in d['manuscript.chapter'] if c['fields']['title'] == title['pk']), key=lambda c: c['pk'])
paras = {}
for p in d['manuscript.paragraph']:
    paras.setdefault(p['fields']['chapter'], []).append(p['fields'])
f = title['fields']
out = [f"# {f['text']} (Wyclif Society, {f['publication_year']})\n\n"]
for c in chapters:
    out.append(f"\n## {c['fields']['heading']}\n\n")
    for p in sorted(paras.get(c['pk'], []), key=lambda p: p['_order']):
        out.append(f"[p. {page_no.get(p['page'], p['old_page_number'])}] {p['text']}\n\n")
s = ''.join(out)
open(sys.argv[2], 'w').write(s) if len(sys.argv) > 2 else sys.stdout.write(s)
