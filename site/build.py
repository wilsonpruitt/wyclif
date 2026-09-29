"""Build the Wyclif reading site (static HTML) from chunks/dialogus/*.md and GLOSSARY.md.

    cd ~/wyclif && .venv/bin/python site/build.py        -> site/dist/

Stdlib only. Design: site/DESIGN.md. Deploy is a separate, per-deploy-approved step.
"""
import html, json, os, re, shutil, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'site', 'dist')
CHUNKS = os.path.join(ROOT, 'chunks', 'dialogus')
SITE = 'https://wyclif.wrootpress.com'
PLATE = 'https://archive.org/details/latinworks22wycl/page/n{leaf}/mode/1up'
LEAF_OFFSET = 31

# Pollard's four movements (intro pp. vi–vii), then the Epilogue.
MOVEMENTS = [('The case from scripture', 1, 10), ('Falsehood appeals to authority', 11, 23),
             ('Practical objections', 24, 33), ('Conclusion', 34, 36)]


# ------------------------------------------------------------------ glossary
def glossary():
    rows, keys, section = [], {}, None
    for line in open(os.path.join(ROOT, 'GLOSSARY.md')):
        m = re.match(r'^## ([A-D])\. (.*)', line)
        if m:
            section = (m.group(1), m.group(2).strip())
            continue
        if not line.startswith('| ') or line.startswith('| Latin') or line.startswith('|---') or not section:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        la, en, note = cells[0], cells[1], (cells[2] if len(cells) > 2 else '')
        row = {'la': la, 'en': en, 'note': scrub(note), 'section': section}
        rows.append(row)
        for form in re.split(r'[;/,]', la):                       # same normalisation as scripts/w3/lint.py
            form = re.sub(r'\(.*?\)', '', form).strip().lower()
            form = re.sub(r'[^a-z ]', '', form).strip()
            if form:
                keys.setdefault(form.replace(' ', '-'), row)
                keys.setdefault(form.split()[0], row)
    return rows, keys


# ------------------------------------------------------------------ text
def scrub(t):
    """Remove internal process references from reader-facing text (the chunks keep the record)."""
    t = re.sub(r'\s*\(LEDGER [A-Z0-9-]+(?:,\s*[A-Z0-9-]+)*\)', '', t)
    t = re.sub(r'\s*\((?:see )?LEDGER [^)]*\)', '', t)
    t = re.sub(r';?\s*ruled \d{4}-\d\d-\d\d', '', t, flags=re.I)
    t = re.sub(r'Ruled \d{4}-\d\d-\d\d[^.|]*\.?', '', t)
    t = re.sub(r'plate checked \d{4}-\d\d-\d\d', 'checked on the plate', t)
    t = re.sub(r'\bGLOSSARY\s*§[A-D],?\s*', 'the glossary, ', t)
    t = re.sub(r'\(GLOSSARY ', '(glossary: ', t)
    t = re.sub(r'\bGLOSSARY\b', 'the glossary', t)
    t = re.sub(r'\s*\(?CONVENTIONS §[\d.]+\)?', '', t)
    t = re.sub(r'\s*\[(?:OVERRIDE|R\d[ab]?|THIN|DEL|INS\??|PLATE|HEAD)\]', '', t)
    t = re.sub(r'\s*\(OVERRIDE\)', '', t)
    t = re.sub(r',\s*OVERRIDE\)', ')', t)
    t = re.sub(r'\s*\bOVERRIDE\b', '', t)
    t = re.sub(r"\bthe scaffold's\b", "the working transcription's", t)
    t = re.sub(r'\b(?:as )?scaffolded\b', 'as first transcribed', t)
    t = re.sub(r'\b(?:in )?the scaffold\b', 'the working transcription', t)
    t = re.sub(r'\bscaffold\b', 'working transcription', t)
    t = re.sub(r'\s*\bPilot\b(?:\s*\([^)]*\))?\.?', '', t)
    t = re.sub(r'\s*\(OVERRIDE ∅\)', '', t)
    t = re.sub(r'\s*\(coordinator[^)]*\)', '', t)
    t = re.sub(r'\bfrom the plate \(OVERRIDE\)', 'from the plate', t)
    t = re.sub(r"\b([Tt])he pilot's\b", r"\1he first draft's", t)
    t = re.sub(r'\b([Tt])he pilot\b', r'\1he first draft', t)
    t = t.replace('( )', '').replace('()', '')
    return re.sub(r'  +', ' ', t)


def inline(s, gl, lang='en'):
    s = scrub(s)
    s = s.replace('\\*', '\x00')
    s = re.sub(r'\bB1\b', 'B¹', s)                        # Pollard's siglum, written both ways in the chunks
    s = html.escape(s, quote=False)

    def tag(m):
        text, key = m.group(1), m.group(2)
        row = gl.get(key)
        if not row:
            return text
        tip = f'<span class="gl-tip" role="tooltip"><i>{html.escape(row["la"])}</i>: {html.escape(row["en"])}</span>'
        return f'<span class="gl" tabindex="0">{text}{tip}</span>'
    s = re.sub(r'\[([^\]\[]+)\]\{g:([a-z-]+)\}', tag, s)
    s = re.sub(r'\[\^(\d+)\]', lambda m: f'<sup class="nref"><a id="r{m.group(1)}" href="#n{m.group(1)}">{m.group(1)}</a></sup>', s)
    if lang == 'la':
        s = re.sub(r'\[p\. (\d+)\]\s*', lambda m: f'<a class="pg" id="p{m.group(1)}" href="{plate(m.group(1))}" title="Pollard p. {m.group(1)}: the printed page">{m.group(1)}</a>', s)
    else:
        s = re.sub(r'\[(\d{1,3})\]\s*', lambda m: f'<span class="pg-en" aria-label="page {m.group(1)}">{m.group(1)}</span>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'\1', s)
    return s.replace('\x00', '*')


def la_html(s, gl):
    s = inline(s, gl, 'la')
    return re.sub(r'\b(MENDACIUM|VERITAS)\.', lambda m: f'<span class="who-la">{m.group(1).lower()}.</span>', s)


def plate(page):
    return PLATE.format(leaf=int(page) + LEAF_OFFSET)


SPEAK = re.compile(r'(?:^|(?<=[.”"?!] ))(TRUTH|FALSEHOOD)\. ')


def speeches(para, current):
    """Split an English paragraph into (speaker, text) runs; returns runs and the speaker after it."""
    runs, pos = [], 0
    for m in SPEAK.finditer(para):
        if m.start() > pos and para[pos:m.start()].strip():
            runs.append((current, para[pos:m.start()].strip(), False))
        current = m.group(1).lower()
        pos = m.end()
        runs.append((current, None, True))                        # marker: a new speech starts here
    tail = para[pos:].strip()
    out, opening = [], False
    for sp, txt, start in runs:
        if start:
            opening = True
            continue
        out.append((sp, txt, opening)); opening = False
    if tail:
        out.append((current, tail, opening))
    return out, current


# ------------------------------------------------------------------ chunks
def order_key(f):
    n = re.search(r'wyc-dialogus-(\w+(?:-\w)?)\.md', f).group(1)
    return (1, n) if n.startswith('epil') else (0, int(n))


def parse(path):
    raw = open(path).read()
    fm, body = {}, raw
    if raw.startswith('---'):
        _, front, body = raw.split('---', 2)
        for line in front.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"')
    title = re.search(r'^# (.+)$', body, re.M).group(1)
    parts = re.split(r'^## (.+)$', body, flags=re.M)
    sections, sidenotes, notes, transcription = [], [], {}, ''
    for head, text in zip(parts[1::2], parts[2::2]):
        if head.startswith("Pollard's side-notes"):
            for m in re.finditer(r'^- (\d+)\.(\d+):\s*(.+)$', text, re.M):
                sidenotes.append((int(m.group(1)), int(m.group(2)), m.group(3).strip()))
        elif head.strip() == 'Notes':
            for m in re.finditer(r'^\[\^(\d+)\]:\s*(.+?)(?=^\[\^\d+\]:|\Z)', text, re.M | re.S):
                notes[int(m.group(1))] = re.sub(r'\s*\n\s*', ' ', m.group(2)).strip()
        elif head.strip() == 'Transcription notes':
            transcription = text.strip()
        else:
            sections.append((head.strip(), [p.strip() for p in text.strip().split('\n\n') if p.strip()]))
    return fm, title, sections, sidenotes, notes, transcription


def slug(cid):
    n = cid.split('wyc-dialogus-')[1]
    return f'epilogus/{n[-1]}' if n.startswith('epil') else f'cap/{int(n)}'


# ------------------------------------------------------------------ html
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" '
         'href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?'
         'family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">')


def page(title, body, depth, desc='', canonical=''):
    up = '../' * depth
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
{f'<link rel="canonical" href="{SITE}/{canonical}">' if canonical is not None else ''}
{FONTS}<link rel="icon" href="{up}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{up}style.css"></head>
<body>
<header class="top"><a class="home" href="{up}">Wyclif, <i>Dialogus</i></a>
<nav><a href="{up}glossary/">Glossary</a><a href="{up}about/">About this edition</a><a href="{up}rights/">Rights</a></nav></header>
<main>{body}</main>
<footer><p>Latin: Pollard’s edition (1886), public domain. English, notes and encoding: Wroot Press, <a href="{up}rights/">CC BY-NC 4.0</a>. A working draft.</p></footer>
<script src="{up}site.js" defer></script>
</body></html>'''


def build():
    gl_rows, gl = glossary()
    files = sorted((f for f in os.listdir(CHUNKS) if re.match(r'wyc-dialogus-[\w-]+\.md$', f)), key=order_key)
    if len(files) != 38:
        sys.exit(f'expected 38 chunks, found {len(files)}')
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    chunks, speaker, page_to = [], None, {}
    for f in files:
        fm, title, sections, sidenotes, notes, trans = parse(os.path.join(CHUNKS, f))
        if 'epil' in f:
            speaker = None                                          # the Epilogue is Wyclif's own voice
        chunks.append(dict(f=f, fm=fm, title=title, sections=sections, sidenotes=sidenotes, notes=notes,
                           trans=trans, slug=slug(fm['chunk_id']), start_speaker=speaker))
        for _, paras in sections:
            for p in paras:
                if not p.startswith('>'):
                    _, speaker = speeches(p, speaker)

    for i, c in enumerate(chunks):
        render_chunk(c, i, chunks, gl, page_to)
    render_index(chunks)
    render_glossary(gl_rows)
    render_static(chunks, page_to)
    print(f'built {len(chunks)} chunks, {len(page_to)} page anchors -> {OUT}')


def label(c):
    n = c['fm']['chunk_id'].split('-')[-1]
    if 'epil' in c['fm']['chunk_id']:
        return 'Epilogue, part ' + ('one' if n == 'a' else 'two')
    return f'Chapter {int(n)}'


def render_chunk(c, i, chunks, gl, page_to):
    depth = 2
    words = {'truth': 0, 'falsehood': 0, None: 0}
    speaker = c['start_speaker']
    rows = []
    cur_page = int(re.match(r'(\d+)', c['fm']['pages']).group(1))
    side = list(c['sidenotes'])
    for head, paras in c['sections']:
        if head == 'Headnote':
            rows.append('<section class="headnote"><h2>About this chapter</h2>' +
                        ''.join(f'<p>{inline(p, gl)}</p>' for p in paras) + '</section>')
            continue
        m = re.match(r'(.*?)\s*·\s*([\d.–-]+)$', head)
        htxt, hrange = (m.group(1), m.group(2)) if m else (head, '')
        rows.append(f'<h2 class="sec">{inline(htxt, gl)}<span class="range">{hrange}</span></h2>')
        group_la, group_en = None, []

        def flush():
            nonlocal group_la, group_en, cur_page
            if group_la is None and not group_en:
                return
            pages = [int(p) for p in re.findall(r'\[p\. (\d+)\]', group_la or '')]
            span = set([cur_page] + pages)
            mine = [s for s in side if s[0] in span]
            for s in mine:
                side.remove(s)
            if pages:
                cur_page = pages[-1]
            for p in pages:
                page_to.setdefault(p, f"{c['slug']}/#p{p}")
            rail = ''.join(f'<p class="sn"><span class="sn-at">{s[0]}.{s[1]}</span> {inline(s[2], gl)}</p>' for s in mine)
            la = f'<div class="la" lang="la">{la_html(group_la.strip(), gl)}</div>' if group_la else '<div class="la"></div>'
            en = ''.join(group_en)
            rows.append(f'<div class="passage"><aside class="rail">{rail}</aside>{la}<div class="en">{en}</div></div>')
            group_la, group_en = None, []

        for p in paras:
            if p.startswith('>'):
                flush()
                group_la = ' '.join(l.lstrip('> ').strip() for l in p.splitlines())
            else:
                text = re.sub(r'\s*\n\s*', ' ', p)
                runs, speaker = speeches(text, speaker)
                for sp, t, opening in runs:
                    words[sp] += len(re.sub(r'\{g:[^}]*\}|\[\^\d+\]', '', t).split())
                    who = f'<span class="who">{"Truth" if sp == "truth" else "Falsehood"}.</span> ' if opening and sp else ''
                    cls = sp or 'author'
                    group_en.append(f'<p class="sp {cls}{" open" if opening else ""}">{who}{inline(t, gl)}</p>')
        flush()
    c['words'] = words
    notes = ''.join(f'<li id="n{n}"><a class="back" href="#r{n}" aria-label="Back to the text">{n}</a> '
                    f'{inline(re.sub(r"^\*\*[A-Z/]+\.\*\*\s*", "", t), gl)}</li>' for n, t in sorted(c['notes'].items()))
    trans = ''
    if c['trans']:
        trans = ('<details class="trans"><summary>How the Latin of this chapter was established</summary>' +
                 trans_html(c['trans'], gl) + '</details>')
    prev_ = chunks[i - 1] if i else None
    next_ = chunks[i + 1] if i + 1 < len(chunks) else None
    pn = '<nav class="pn">' + (f'<a rel="prev" href="../../{prev_["slug"]}/">{label(prev_)}</a>' if prev_ else '<span></span>') + \
         (f'<a rel="next" href="../../{next_["slug"]}/">{label(next_)}</a>' if next_ else '') + '</nav>'
    heading = re.sub(r'^\*Dialogus\*,\s*(?:chapter \d+|Epilog(?:us|ue),? part \w+)\s*[:.]\s*', '', c['title'])
    body = (f'<article class="chapter"><header class="ch-head"><p class="ch-n">{label(c)}</p>'
            f'<h1>{inline(heading[0].upper() + heading[1:], gl)}</h1>'
            f'<p class="ch-pages">Pollard pp. {c["fm"]["pages"]}</p></header>'
            f'<div class="cols-head" aria-hidden="true"><span></span><span>Latin</span><span>English</span></div>'
            + ''.join(rows) +
            (f'<section class="notes"><h2>Notes</h2><ol>{notes}</ol>{trans}</section>' if notes else '') +
            pn + '</article>')
    d = os.path.join(OUT, c['slug'])
    os.makedirs(d, exist_ok=True)
    desc = f'{label(c)} of Wyclif’s Dialogus (1379), Latin and English: {re.sub(r"[*]", "", heading)}.'
    open(os.path.join(d, 'index.html'), 'w').write(page(f'{label(c)}: {re.sub(r"[*]", "", heading)} · Wyclif, Dialogus', body, depth, desc, c['slug'] + '/'))


def trans_html(text, gl):
    """Top-level '- ' bullets (continuation lines joined), nested '  - ' bullets as a sub-list."""
    out = []
    for item in re.split(r'\n(?=- |\S)', text.strip()):
        item = item.strip()
        if not item or re.match(r'^-?\s*\*\*Pilot vs scaffold', item):   # internal pilot-to-draft comparison
            continue
        head, *subs = re.split(r'\n\s+- ', item)
        head = re.sub(r'\s*\n\s*', ' ', re.sub(r'^-\s*', '', head))
        sub = ''.join(f'<li>{inline(re.sub(r"\s*\n\s*", " ", s), gl)}</li>' for s in subs)
        out.append(f'<li>{inline(head, gl)}{f"<ul>{sub}</ul>" if sub else ""}</li>')
    return '<ul>' + ''.join(out) + '</ul>'


def render_index(chunks):
    maxw = max(sum(c['words'].values()) for c in chunks)
    groups = [(t, [c for c in chunks if 'epil' not in c['f'] and a <= int(c['fm']['chunk_id'].split('-')[-1]) <= b]) for t, a, b in MOVEMENTS]
    groups.append(('Epilogue', [c for c in chunks if 'epil' in c['f']]))
    strip = []
    for t, cs in groups:
        cols = []
        for c in cs:
            w = c['words']; tot = sum(w.values())
            segs = ''.join(f'<span class="seg {k or "author"}" style="flex-grow:{v}"></span>' for k, v in
                           (('falsehood', w['falsehood']), ('truth', w['truth']), (None, w[None])) if v)
            n = c['fm']['chunk_id'].split('-')[-1]
            short = n.upper()[-1] if 'epil' in c['f'] else str(int(n))
            title = re.sub(r'[*]', '', re.sub(r'^\*Dialogus\*,\s*', '', c['title']))
            cols.append(f'<a class="col" href="{c["slug"]}/" style="--h:{tot / maxw:.3f}" '
                        f'title="{html.escape(label(c))}: {html.escape(title)} ({tot:,} words)">'
                        f'<span class="bar">{segs}</span><span class="cn">{short}</span></a>')
        strip.append(f'<div class="mv"><div class="cols">{"".join(cols)}</div><p class="mv-t">{t}</p></div>')
    toc = []
    for t, cs in groups:
        toc.append(f'<h3>{t}</h3><ol class="toc">' + ''.join(
            f'<li><a href="{c["slug"]}/"><span class="toc-n">{label(c)}</span> '
            f'{html.escape(re.sub(r"[*]", "", re.sub(r"^.*?:\s*", "", c["title"], count=1)))}</a></li>' for c in cs) + '</ol>')
    body = f'''<section class="hero">
<h1 class="title"><span class="t-la">Dialogus</span><span class="t-sub">sive Speculum Ecclesie Militantis</span></h1>
<p class="lede">John Wyclif’s dialogue between Truth and Falsehood on whether the church should own property,
written in 1379. The Latin of Alfred Pollard’s edition, with a new English translation and notes.</p>
<figure class="strip" aria-label="The Dialogus chapter by chapter">
<div class="mvs">{"".join(strip)}</div>
<figcaption>Each column is a chapter, as tall as it is long. <span class="key truth">Truth</span> speaks in russet, the colour of
the undyed gowns of Wyclif’s poor priests, and <span class="key falsehood">Falsehood</span> in gilt, the endowed church’s gold.
<span class="key author">Grey</span> is Wyclif in his own voice, in the prologue and the Epilogue. Falsehood gets a few lines at a time,
and in a dozen chapters none at all; Truth answers at length. After the third chapter, Pollard notes, “Veritas is Wyclif, and Wyclif only.”</figcaption>
</figure></section>
<section class="contents"><h2>Contents</h2>{"".join(toc)}</section>'''
    open(os.path.join(OUT, 'index.html'), 'w').write(page('Wyclif, Dialogus: Latin and English', body, 0,
        'John Wyclif’s Dialogus sive Speculum Ecclesie Militantis (1379): the Latin of Pollard’s edition with a new English translation and notes.', ''))


def render_glossary(rows):
    secs, out = {}, []
    for r in rows:
        secs.setdefault(r['section'], []).append(r)
    for (letter, name), rs in secs.items():
        out.append(f'<h2>{html.escape(name)}</h2><dl class="gloss">' + ''.join(
            f'<div><dt lang="la">{inline(r["la"], {})}</dt><dd><span class="g-en">{inline(r["en"], {})}</span>'
            f'{f"<span class=g-note>{inline(r["note"], {})}</span>" if r["note"].strip() else ""}</dd></div>' for r in rs) + '</dl>')
    body = ('<article class="prose wide"><h1>Glossary</h1><p>One Latin term, one English rendering, throughout. '
            'Wyclif’s arguments turn on his words coming back, so the translation keeps them recognisable. '
            'In the text, a dotted underline marks a glossary term; hover over it or focus it to see the Latin.</p>' + ''.join(out) + '</article>')
    d = os.path.join(OUT, 'glossary'); os.makedirs(d)
    open(os.path.join(d, 'index.html'), 'w').write(page('Glossary · Wyclif, Dialogus', body, 1, 'The fixed English renderings of Wyclif’s key terms.', 'glossary/'))


def render_static(chunks, page_to):
    src = os.path.join(ROOT, 'site', 'static')
    for name in os.listdir(src):
        if name.endswith('.html'):
            d = os.path.join(OUT, name[:-5]); os.makedirs(d)
            title, _, body = open(os.path.join(src, name)).read().partition('\n')
            open(os.path.join(d, 'index.html'), 'w').write(page(title + ' · Wyclif, Dialogus', body, 1, title, name[:-5] + '/'))
        else:
            shutil.copy(os.path.join(src, name), OUT)
    for p, target in page_to.items():                                   # /p/27/ -> the chapter, at page 27
        d = os.path.join(OUT, 'p', str(p)); os.makedirs(d)
        open(os.path.join(d, 'index.html'), 'w').write(
            f'<!doctype html><meta charset="utf-8"><title>Page {p}</title><link rel="canonical" href="{SITE}/{target}">'
            f'<meta http-equiv="refresh" content="0; url=../../{target}"><a href="../../{target}">Pollard p. {p}</a>')
    urls = [''] + [c['slug'] + '/' for c in chunks] + ['glossary/', 'about/', 'rights/']
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        ''.join(f'<url><loc>{SITE}/{u}</loc></url>' for u in urls) + '</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')


if __name__ == '__main__':
    build()
