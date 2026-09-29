"""Build witness token streams for one volume (CONVENTIONS §3.1).

    .venv/bin/python scripts/w3/witness.py SLUG

For the primary scan and every other free archive.org scan of the volume: download
_djvu.xml, split each leaf into main text / margin / apparatus (djvu.py), join
line-end hyphens, and write text/<slug>/witnesses/<id>.jsonl, one token per line:
    {"t": raw, "leaf": n, "line": k, "box": [l,t,r,b], "para": bool, "head": bool}
Side-notes of the PRIMARY scan go to sidenotes/<slug>.tsv (leaf, y, text); its page-foot apparatus
to text/<slug>/apparatus.json ({leaf: text}), which brief.py hands to the translator.
Fordham (where it exists) is written as witnesses/fordham.jsonl with "pg" (printed
page) and "it" (italic) instead of leaf/box.
The XML is deleted after parsing (8 GB machine; it can be re-fetched).
"""
import json, os, re, sys, subprocess, html
sys.path.insert(0, os.path.dirname(__file__))
import djvu

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def vol(slug):
    for v in json.load(open(f'{ROOT}/catalog/volumes.json')):
        if v['slug'] == slug:
            return v
    raise SystemExit(f'no volume {slug}')


def fetch(ident, dest):
    if not os.path.exists(dest) or os.path.getsize(dest) < 1000:
        subprocess.run(['curl', '-sL', '-o', dest,
                        f'https://archive.org/download/{ident}/{ident}_djvu.xml'], check=True)
    return dest


def stream_from_scan(path):
    leaves = list(djvu.parse(path))
    W = djvu.measure(leaves)
    out, notes, app = [], [], {}
    for lf in leaves:
        sp = djvu.split_leaf(lf, W)
        if sp['apparatus']:
            app[lf['leaf']] = '\n'.join(' '.join(w[0] for w in ln) for ln in sp['apparatus'])
        L = sp['band'][0]
        Wl = sp['band'][1] - sp['band'][0]
        prev_line = None
        for tok in djvu.main_tokens(sp):
            head = tok['t'] == '§HEADING§'
            para = False
            if tok['line'] != prev_line and not head:
                line = sp['main'][tok['line']]
                para = line[0][1] > L + 0.025 * Wl if Wl else False
            prev_line = tok['line']
            out.append(dict(t=tok['t'], leaf=lf['leaf'], line=tok['line'], box=list(tok['box']),
                            para=para, head=head, eol=tok.get('eol', False)))
        for g in sp['margin']:
            txt = ' '.join(w[0] for w in g)
            if sum(c.isalpha() for c in txt) >= 3:
                notes.append((lf['leaf'], int(sum(w[4] for w in g) / len(g)), g[0][1], txt))
    return join_hyphens(merge_digits(out)), notes, W, app


def merge_digits(toks):
    """'1 2' -> '12' when two digit tokens sit adjacent on one line (OCR splits numerals)."""
    out = []
    for t in toks:
        p = out[-1] if out else None
        if (p and p['leaf'] == t['leaf'] and p['line'] == t['line'] and re.fullmatch(r'\d+', p['t'])
                and re.fullmatch(r'\d+[^A-Za-z0-9]{0,3}', t['t']) and t['box'][0] - p['box'][2] < (t['box'][3] - t['box'][1]) * 0.6):
            out[-1] = dict(p, t=p['t'] + t['t'], box=[p['box'][0], p['box'][1], t['box'][2], t['box'][3]])
            continue
        out.append(t)
    return out


def join_hyphens(toks):
    """Join 'disputa-' + 'cionis' when the hyphen ends a line (also across leaves)."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if (t.get('eol') and t['t'].endswith(('-', '¬')) and len(t['t']) > 1
                and i + 1 < len(toks) and not toks[i + 1]['head']):
            n = toks[i + 1]
            t = dict(t, t=t['t'][:-1] + n['t'], joined=True)
            i += 2
        else:
            i += 1
        out.append(t)
    return out


def fordham_stream(slug):
    """Fordham witness from data.json, italics kept as a flag."""
    import unicodedata
    data = json.load(open(f'{ROOT}/sources/fordham/data/data.json'))
    fmap = json.load(open(f'{ROOT}/catalog/fordham_map.json'))
    v = vol(slug)
    files = [f for f, m in fmap.items() if m['best'] == v['primary_scan']]
    if not files:
        return []
    # map Fordham .md file names to manuscript.title pks via their page counts/slugs
    titles = {t['pk']: t['fields'] for t in data['manuscript.title']}
    want = []
    for f in files:
        stem = f[:-3].lower().replace('_', '-')
        cand = [pk for pk, t in titles.items() if t['slug'].replace('_', '-') in (stem, stem.replace('-i', '-1'))
                or stem.startswith(t['slug'])]
        want += cand
    page_no = {p['pk']: (p['fields']['number'], p['fields']['title']) for p in data['manuscript.page']}
    chap = {c['pk']: c['fields']['title'] for c in data['manuscript.chapter']}
    paras = [p['fields'] for p in data['manuscript.paragraph'] if chap.get(p['fields']['chapter']) in want]
    paras.sort(key=lambda p: (p['chapter'], p['_order']))
    out = []
    for p in paras:
        pg = page_no.get(p['page'], (p['old_page_number'], None))[0]
        it = False
        first = True
        for piece in re.split(r'(<i>|</i>)', p['text']):
            if piece == '<i>':
                it = True; continue
            if piece == '</i>':
                it = False; continue
            piece = re.sub(r'(\d)o(?=[\s,.;:]|$)', r'\1°', piece)   # Fordham writes 14° as 14o
            for w in html.unescape(re.sub(r'<[^>]+>', ' ', piece)).split():
                out.append(dict(t=w, pg=pg, it=it, para=first))
                first = False
    return out


def main(slug):
    v = vol(slug)
    base = f'{ROOT}/text/{slug}'
    os.makedirs(f'{base}/raw', exist_ok=True)
    os.makedirs(f'{base}/witnesses', exist_ok=True)
    os.makedirs(f'{ROOT}/sidenotes', exist_ok=True)
    ids = [v['primary_scan']] + v['other_free_scans']
    for ident in ids:
        outp = f'{base}/witnesses/{ident}.jsonl'
        if os.path.exists(outp):
            print('have', ident); continue
        xml = fetch(ident, f'{base}/raw/{ident}_djvu.xml')
        try:
            toks, notes, W, app = stream_from_scan(xml)
        except Exception as e:                      # a scan without usable XML
            print('SKIP', ident, e); continue
        with open(outp, 'w') as f:
            for t in toks:
                f.write(json.dumps(t, ensure_ascii=False) + '\n')
        if ident == v['primary_scan']:
            with open(f'{ROOT}/sidenotes/{slug}.tsv', 'w') as f:
                f.write('leaf\ty\tx\ttext\n')
                for n in notes:
                    f.write('\t'.join(str(x) for x in n) + '\n')
            with open(f'{base}/apparatus.json', 'w') as f:        # the editor's page-foot apparatus, by leaf (briefs use it)
                json.dump(app, f, ensure_ascii=False, indent=0)
        os.remove(xml)
        print(f'{ident}: {len(toks)} tokens, measure {W}')
    fs = fordham_stream(slug)
    if fs:
        with open(f'{base}/witnesses/fordham.jsonl', 'w') as f:
            for t in fs:
                f.write(json.dumps(t, ensure_ascii=False) + '\n')
        print(f'fordham: {len(fs)} tokens')


if __name__ == '__main__':
    main(sys.argv[1])
