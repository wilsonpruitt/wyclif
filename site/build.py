"""Build the Wyclif reading site (static HTML) from chunks/dialogus/*.md and GLOSSARY.md.

    cd ~/wyclif && .venv/bin/python site/build.py        -> site/dist/

Stdlib only. Design: site/DESIGN.md. Deploy is a separate, per-deploy-approved step.
"""
import html, json, os, re, shutil, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'site', 'dist')
SITE = 'https://wyclif.wrootpress.com'

# One entry per translated work. use(name) points the module globals below at it before each work is built.
WORKS = {
    'dialogus': dict(n=38, editor='Pollard', name='Dialogus', year='1379', offset=31,
                     plate='https://archive.org/details/latinworks22wycl/page/n{leaf}/mode/1up',
                     title_re=r'^\*Dialogus\*,\s*(?:chapter \d+|Epilog(?:us|ue),? part \w+)\s*[:.]\s*'),
    'ecclesia': dict(n=159, editor='Loserth', name='De ecclesia', year='1378–79', offset=37,
                     plate='https://archive.org/details/latinworks10wycl/page/n{leaf}/mode/1up',
                     title_re=r'^\*De ecclesia\*,\s*chapter \d+,\s*part \d+\s*[:.]\s*'),
}
WORK = WOUT = CHUNKS = PLATE = EDITOR = TITLE_RE = None
LEAF_OFFSET = 0


def use(name):
    global WORK, WOUT, CHUNKS, PLATE, EDITOR, TITLE_RE, LEAF_OFFSET
    w = WORKS[name]
    WORK, WOUT = name, os.path.join(OUT, name)
    CHUNKS = os.path.join(ROOT, 'chunks', name)
    PLATE, EDITOR, LEAF_OFFSET = w['plate'], w['editor'], w['offset']
    TITLE_RE = re.compile(w['title_re'])

import hashlib
ASSET_V = hashlib.sha1(b''.join(open(os.path.join(ROOT, 'site', 'static', n), 'rb').read() for n in ('style.css', 'site.js'))).hexdigest()[:8]

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
    t = re.sub(r'\s*\(LEDGER [A-Za-z0-9-]+(?:,\s*[A-Za-z0-9-]+)*\)', '', t)
    t = re.sub(r'\s*\((?:see )?LEDGER [^)]*\)', '', t)
    t = re.sub(r'\s*\((?:to be checked, |from memory, )?LEDGER [^)]*\)', '', t)
    t = re.sub(r'[;,]\s*(?:to be checked,?\s*)?LEDGER [A-Za-z0-9, -]+(?:\s*,\s*(?:editor|to-verify|to be checked))?(?=[);])', '', t)
    t = re.sub(r'\s*\(to be checked\)', '', t)
    t = re.sub(r'\s*\((?:Latin doubts)\)', '', t)                  # a pointer to an internal list
    t = re.sub(r'\s*\((?:translator|coordinator), \d{4}-\d\d-\d\d\)', '', t)
    t = re.sub(r'\s+by the coordinator,? \(?\d{4}-\d\d-\d\d(?:, tokenfix\.tsv)?\)?', '', t)
    t = re.sub(r',? by the coordinator\b', '', t)
    t = re.sub(r'\s*\((?:\d{4}-\d\d-\d\d, )?`?tokenfix\.tsv`?\)', '', t)
    t = re.sub(r'[;,]?\s*\b(?:see |cf\. )?LEDGER [A-Za-z]\d\d[a-z]-\d+(?:,\s*[A-Za-z]\d\d[a-z]-\d+)*', '', t)
    t = re.sub(r'\s*\(tokenfix\)', '', t)
    t = re.sub(r', S[23] audit \d{4}-\d\d-\d\d', '', t)
    t = re.sub(r'\s*\(\d{4}-\d\d-\d\d(?:, tokenfix\.tsv)?\)', '', t)
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
    t = re.sub(r'\s*\((?:approved|ruled|conformed) \d{4}-\d\d-\d\d\)', '', t)
    t = re.sub(r'[;,]?\s*\b\d{4}-\d\d-\d\d\b(?=\s*[:;,.)(]|\s*$)', '', t)       # bare process dates
    t = re.sub(r'\s*\(\d{4}-\d\d-\d\d row\)', '', t)
    t = re.sub(r'\b(approved|ruled|conformed) \d{4}-\d\d-\d\d', r'\1', t)
    t = re.sub('\u2b50\ufe0f? ?', '', t)                              # the star-emoji editorial marker is never published
    t = t.replace('( )', '').replace('()', '')
    return re.sub(r'  +', ' ', t)


def inline(s, gl, lang='en'):
    s = scrub(s)
    s = s.replace('\\*', '\x00')
    if lang == 'en':
        s = curly(s)
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
        s = re.sub(r'\[p\. (\d+)\]\s*', lambda m: f'<a class="pg" id="p{m.group(1)}" href="{plate(m.group(1))}" title="{EDITOR} p. {m.group(1)}: the printed page">{m.group(1)}</a>', s)
    else:
        s = re.sub(r'\[(\d{1,3})\]\s*', lambda m: f'<span class="pg-en" aria-label="page {m.group(1)}">{m.group(1)}</span>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'\1', s)
    return s.replace('\x00', '*')


def la_html(s, gl):
    s = inline(s, gl, 'la')
    return re.sub(r'\b(MENDACIUM|VERITAS)\.', lambda m: f'<span class="who-la">{m.group(1).lower()}.</span>', s)


def curly(s):
    s = re.sub(r"(\w)'(\w)", '\\1’\\2', s)
    return re.sub(r"(?<=s)'(?=[\s,.;:)]|$)", '’', s)


def cap1(s):
    s = curly(s)
    return s[:1].upper() + s[1:]


def short_title(c):
    return cap1(re.sub(r'[*]', '', TITLE_RE.sub('', c['title'])))


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
    n = re.search(rf'wyc-{WORK}-(\w+(?:-\w)?)\.md', f).group(1)
    if WORK == 'ecclesia':                                          # 01-a … 23-l
        ch, part = n.split('-')
        return (int(ch), part)
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
        if 'side-notes' in head:                                    # "Pollard's side-notes …" / "Loserth's side-notes …"
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
    n = cid.split(f'wyc-{WORK}-')[1]
    if WORK == 'ecclesia':
        ch, part = n.split('-')
        return f'cap/{int(ch)}/{part}'
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
{FONTS}<link rel="icon" href="{up}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{up}style.css?v={ASSET_V}"></head>
<body>
<header class="top"><a class="home" href="{up}">Wyclif’s Latin works</a>
<nav><a href="{up}ecclesia/"><i>De ecclesia</i></a><a href="{up}dialogus/"><i>Dialogus</i></a><a href="{up}glossary/">Glossary</a><a href="{up}about/">About this edition</a><a href="{up}rights/">Rights</a></nav></header>
<main>{body}</main>
<footer><p>Latin: the Wyclif Society edition (1883–1922), public domain. English, notes and encoding: Wroot Press, <a href="{up}rights/">CC BY-NC 4.0</a>. A working draft.</p></footer>
<script src="{up}site.js?v={ASSET_V}" defer></script>
</body></html>'''


def load_work(name):
    use(name)
    files = sorted((f for f in os.listdir(CHUNKS) if re.match(rf'wyc-{name}-[\w-]+\.md$', f)), key=order_key)
    if len(files) != WORKS[name]['n']:
        sys.exit(f'{name}: expected {WORKS[name]["n"]} chunks, found {len(files)}')
    chunks, speaker = [], None
    for f in files:
        fm, title, sections, sidenotes, notes, trans = parse(os.path.join(CHUNKS, f))
        if 'epil' in f:
            speaker = None                                          # the Epilogue is Wyclif's own voice
        chunks.append(dict(f=f, fm=fm, title=title, sections=sections, sidenotes=sidenotes, notes=notes,
                           trans=trans, slug=slug(fm['chunk_id']), start_speaker=speaker))
        if name == 'dialogus':                                      # only the Dialogus has speakers
            for _, paras in sections:
                for p in paras:
                    if not p.startswith('>'):
                        _, speaker = speeches(p, speaker)
    return chunks


def build():
    gl_rows, gl = glossary()
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):                                    # clear the output, keep the Vercel link
        if name != '.vercel':
            p = os.path.join(OUT, name)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    built = {}
    for name in WORKS:
        chunks, page_to = load_work(name), {}
        for i, c in enumerate(chunks):
            render_chunk(c, i, chunks, gl, page_to)
        (render_work if name == 'dialogus' else render_work_ecclesia)(chunks)
        built[name] = (chunks, page_to)
        print(f'{name}: {len(chunks)} chunks, {len(page_to)} page anchors')
    render_home(built)
    render_glossary(gl_rows)
    render_static(built)
    print(f'built -> {OUT}')


def label(c):
    n = c['fm']['chunk_id'].split('-')[-1]
    if WORK == 'ecclesia':
        ch, part = c['fm']['chunk_id'].split('-')[-2:]
        return f'Chapter {int(ch)}, part {ord(part) - 96}'
    if 'epil' in c['fm']['chunk_id']:
        return 'Epilogue, part ' + ('one' if n == 'a' else 'two')
    return f'Chapter {int(n)}'


def render_chunk(c, i, chunks, gl, page_to):
    depth = 2 + c['slug'].count('/')                               # dialogus/cap/1/ is 3 deep; ecclesia/cap/12/c/ is 4
    root = '../' * (depth - 1)                                      # the work's own index
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
                runs, speaker = speeches(text, speaker) if WORK == 'dialogus' else ([(None, text, False)], None)
                for sp, t, opening in runs:
                    words[sp] += len(re.sub(r'\{g:[^}]*\}|\[\^\d+\]', '', t).split())
                    who = f'<span class="who">{"Truth" if sp == "truth" else "Falsehood"}.</span> ' if opening and sp else ''
                    cls = sp or 'author'
                    group_en.append(f'<p class="sp {cls}{" open" if opening else ""}">{who}{inline(t, gl)}</p>' if WORK == 'dialogus'
                                    else f'<p>{inline(t, gl)}</p>')
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
    pn = '<nav class="pn">' + (f'<a rel="prev" href="{root}{prev_["slug"]}/">{label(prev_)}</a>' if prev_ else '<span></span>') + \
         (f'<a rel="next" href="{root}{next_["slug"]}/">{label(next_)}</a>' if next_ else '') + '</nav>'
    heading = TITLE_RE.sub('', c['title'])
    wname = WORKS[WORK]['name']
    body = (f'<article class="chapter"><header class="ch-head"><p class="ch-n"><a href="{root}"><i>{wname}</i></a>, {label(c)[0].lower() + label(c)[1:]}</p>'
            f'<h1>{inline(heading[0].upper() + heading[1:], gl)}</h1>'
            f'<p class="ch-pages">{EDITOR} pp. {c["fm"]["pages"]}</p></header>'
            f'<div class="cols-head" aria-hidden="true"><span></span><span>Latin</span><span>English</span></div>'
            + ''.join(rows) +
            (f'<section class="notes"><h2>Notes</h2><ol>{notes}</ol>{trans}</section>' if notes else '') +
            pn + '</article>')
    d = os.path.join(WOUT, c['slug'])
    os.makedirs(d, exist_ok=True)
    desc = f'{label(c)} of Wyclif’s {wname} ({WORKS[WORK]["year"]}), Latin and English: {re.sub(r"[*]", "", heading)}.'
    open(os.path.join(d, 'index.html'), 'w').write(page(f'{label(c)}: {re.sub(r"[*]", "", heading)} · Wyclif, {wname}', body, depth, desc, f"{WORK}/{c['slug']}/"))


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


def render_work(chunks):
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
            title = short_title(c)
            cols.append(f'<a class="col" href="{c["slug"]}/" style="--h:{tot / maxw:.3f}" '
                        f'title="{html.escape(label(c))}: {html.escape(title)} ({tot:,} words)">'
                        f'<span class="bar">{segs}</span><span class="cn">{short}</span></a>')
        strip.append(f'<div class="mv"><div class="cols">{"".join(cols)}</div><p class="mv-t">{t}</p></div>')
    toc = []
    for t, cs in groups:
        toc.append(f'<h3>{t}</h3><ol class="toc">' + ''.join(
            f'<li><a href="{c["slug"]}/"><span class="toc-n">{label(c)}</span> '
            f'<span>{html.escape(short_title(c))}</span></a></li>' for c in cs) + '</ol>')
    body = f'''<section class="hero">
<h1 class="title"><span class="t-la">Dialogus</span><span class="t-sub">sive Speculum Ecclesie Militantis</span></h1>
<p class="lede">John Wyclif’s dialogue between Truth and Falsehood on whether the church should own property,
written in 1379. The Latin of Alfred Pollard’s edition, with a new English translation and notes.</p>
<figure class="strip" aria-label="The Dialogus chapter by chapter">
<div class="mvs">{"".join(strip)}</div>
<p class="mv-legend">In Pollard’s divisions: the case from scripture (1–10), Falsehood’s appeals to authority (11–23), practical objections (24–33), conclusion (34–36), Epilogue.</p>
<figcaption>Each column is a chapter, as tall as it is long. <span class="key truth">Truth</span> speaks in russet, the colour of
the undyed gowns of Wyclif’s poor priests, and <span class="key falsehood">Falsehood</span> in gilt, the endowed church’s gold.
<span class="key author">Grey</span> is Wyclif in his own voice, in the prologue and the Epilogue. Falsehood gets a few lines at a time,
and in a dozen chapters none at all; Truth answers at length. After the third chapter, Pollard notes, “Veritas is Wyclif, and Wyclif only.”</figcaption>
</figure></section>
<section class="contents"><h2>Contents</h2>{"".join(toc)}</section>'''
    os.makedirs(WOUT, exist_ok=True)
    open(os.path.join(WOUT, 'index.html'), 'w').write(page('Dialogus: Latin and English · Wyclif', body, 1,
        'John Wyclif’s Dialogus sive Speculum Ecclesie Militantis (1379): the Latin of Pollard’s edition with a new English translation and notes.', ''))


def render_work_ecclesia(chunks):
    chapters = {}
    for c in chunks:
        chapters.setdefault(int(c['fm']['chunk_id'].split('-')[-2]), []).append(c)
    toc, words = [], 0
    for ch, cs in chapters.items():
        p0 = int(re.match(r'(\d+)', cs[0]['fm']['pages']).group(1))
        p1 = int(re.search(r'(\d+)\.\d+$', cs[-1]['fm']['pages']).group(1))
        words += sum(sum(c['words'].values()) for c in cs)
        toc.append(f'<h3>Chapter {ch}<span class="range"> · Loserth pp. {p0}–{p1}</span></h3><ol class="toc">' + ''.join(
            f'<li><a href="{c["slug"]}/"><span class="toc-n">Part {ord(c["fm"]["chunk_id"][-1]) - 96}</span> '
            f'<span>{html.escape(short_title(c))}</span></a></li>' for c in cs) + '</ol>')
    body = f'''<section class="hero">
<h1 class="title"><span class="t-la">De ecclesia</span><span class="t-sub">On the Church</span></h1>
<p class="lede">John Wyclif’s treatise on the church, written between early 1378 and early 1379, in the months after
Gregory XI’s bulls condemned his teaching and as the Great Schism opened. Wyclif settles what the church is before asking
what its bishops may claim of it, then takes up headship, membership, and the privileges and possessions that were being
fought over. The Latin of Johann Loserth’s edition (1886), with a new English translation and notes:
{len(chapters)} chapters in {len(chunks)} parts, about {words // 1000 * 1000:,} words of English.</p></section>
<section class="contents"><h2>Contents</h2>{"".join(toc)}</section>'''
    os.makedirs(WOUT, exist_ok=True)
    open(os.path.join(WOUT, 'index.html'), 'w').write(page('De ecclesia: Latin and English · Wyclif', body, 1,
        'John Wyclif’s De ecclesia (1378–79): the Latin of Loserth’s edition with a new English translation and notes.', f'{WORK}/'))


# Display titles for the shelf, from the title pages (catalog/volumes.json keeps the working notes).
SHELF_TITLES = {
    'polemical-1': 'Polemical Works I', 'polemical-2': 'Polemical Works II', 'compositione': 'De compositione hominis',
    'civ-dom-1': 'De civili dominio I', 'ecclesia': 'De ecclesia', 'dialogus': 'Dialogus', 'incarnacione': 'De benedicta incarnacione',
    'sermones-1': 'Sermones I', 'officio-regis': 'De officio regis', 'sermones-2': 'Sermones II', 'apostasia': 'De apostasia',
    'sermones-3': 'Sermones III', 'dominio-divino': 'De dominio divino', 'sermones-4': 'Sermones IV', 'ente-praed': 'De ente praedicamentali',
    'eucharistia': 'De eucharistia', 'blasphemia': 'De blasphemia', 'logica-1': 'De logica I', 'opus-evang-1': 'Opus evangelicum I–II',
    'opus-evang-2': 'Opus evangelicum III–IV', 'logica-2': 'De logica II', 'simonia': 'De simonia', 'logica-3': 'De logica III',
    'civ-dom-2': 'De civili dominio II', 'misc-phil-1': 'Miscellanea philosophica I', 'civ-dom-3a': 'De civili dominio III, part 1',
    'civ-dom-3b': 'De civili dominio III, part 2', 'misc-phil-2': 'Miscellanea philosophica II', 'veritate': 'De veritate sacrae scripturae I–III',
    'potestate-pape': 'De potestate pape', 'ente-excerpta': 'De ente librorum duorum', 'opera-minora': 'Opera minora', 'mandatis': 'De mandatis divinis',
}
READ_NOW = {'dialogus': 'dialogus/', 'ecclesia': 'ecclesia/'}


def render_home(built):
    chunks, e_chunks = built['dialogus'][0], built['ecclesia'][0]
    vols = json.load(open(os.path.join(ROOT, 'catalog', 'volumes.json')))
    leaves = {k: int(v) for k, v in json.load(open(os.path.join(ROOT, 'catalog', 'leaves.json'))).items()}
    vols.sort(key=lambda v: (int(v['year'][:4]), v['queue']))
    total = sum(leaves[v['slug']] for v in vols)
    spines, rows = [], []
    for v in vols:
        s, n = v['slug'], leaves[v['slug']]
        if s.startswith('civ-dom'):                                  # the catalogue lists all four volumes' editors together
            v['editor'] = 'R. L. Poole' if s == 'civ-dom-1' else 'J. Loserth'
        title = SHELF_TITLES[s]
        href = READ_NOW.get(s)
        inner = f'<span class="sp-t">{html.escape(title)}</span>'
        tip = f'{title}, ed. {v["editor"]}, {v["year"]}' + (' (Latin and English)' if href else '')
        spines.append(f'<a class="spine read" href="{href}" style="flex-grow:{n}" title="{html.escape(tip)}">{inner}</a>' if href else
                      f'<span class="spine" style="flex-grow:{n}" title="{html.escape(tip)}">{inner}</span>')
        status = f'<a href="{href}">Latin and English</a>' if href else 'Latin only, for now'
        rows.append(f'<tr{" class=read" if href else ""}><td class="v-y">{v["year"]}</td><td class="v-t"><i>{html.escape(title)}</i></td>'
                    f'<td class="v-e">{html.escape(v["editor"])}</td><td class="v-s">{status}</td></tr>')
    d_words = sum(sum(c['words'].values()) for c in chunks)
    e_words = sum(sum(c['words'].values()) for c in e_chunks)
    body = f"""<section class="hero">
<h1 class="title"><span class="t-la">Wyclif</span><span class="t-sub">The Latin works, in English</span></h1>
<p class="lede">John Wyclif (c. 1330–1384) wrote in Latin. The Wyclif Society printed his Latin works in {len(vols)} volumes
between 1883 and 1922, and most of them have never been translated into English in full. This site sets the Society’s
Latin beside a new English translation, one work at a time. Two are ready to read now, below.</p>
<figure class="shelf" aria-label="The Wyclif Society edition as a shelf of {len(vols)} volumes">
<div class="spines">{''.join(spines)}</div>
<figcaption>The Society’s edition on one shelf, in order of publication, each volume as thick as it is long
(about {round(total, -3):,} scanned pages in all). The dark spines can be read here now: <a href="ecclesia/"><i>De ecclesia</i></a>
(Loserth, 1886) and the <a href="dialogus/"><i>Dialogus</i></a> (Pollard, 1886).</figcaption>
</figure></section>
<section class="now"><h2>Read now</h2>
<div class="now-cards">
<a class="work-card" href="ecclesia/"><span class="wc-t"><i>De ecclesia</i></span><span class="wc-s">On the Church</span>
<span class="wc-d">What the church is, who belongs to it, and what its bishops may claim. Written in 1378–79;
23 chapters, about {e_words // 1000 * 1000:,} words of English.</span></a>
<a class="work-card" href="dialogus/"><span class="wc-t"><i>Dialogus</i></span><span class="wc-s">The Mirror of the Church Militant</span>
<span class="wc-d">Truth and Falsehood argue over whether the church should own property. Written in 1379;
36 chapters and an Epilogue, about {d_words // 1000 * 1000:,} words of English.</span></a>
</div></section>
<section class="catalogue"><h2>The Wyclif Society edition</h2>
<table class="vols"><thead><tr><th>Year</th><th>Volume</th><th>Editor</th><th>On this site</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
</section>"""
    open(os.path.join(OUT, 'index.html'), 'w').write(page('Wyclif’s Latin works, in English', body, 0,
        'The Latin works of John Wyclif, as the Wyclif Society printed them (1883–1922), with a new English translation, work by work.', ''))


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
    open(os.path.join(d, 'index.html'), 'w').write(page('Glossary · Wyclif’s Latin works', body, 1, 'The fixed English renderings of Wyclif’s key terms.', 'glossary/'))


def render_static(built):
    src = os.path.join(ROOT, 'site', 'static')
    for name in os.listdir(src):
        if name.endswith('.html'):
            d = os.path.join(OUT, name[:-5]); os.makedirs(d)
            title, _, body = open(os.path.join(src, name)).read().partition('\n')
            open(os.path.join(d, 'index.html'), 'w').write(page(title + ' · Wyclif’s Latin works', body, 1, title, name[:-5] + '/'))
        else:
            shutil.copy(os.path.join(src, name), OUT)
    urls = ['']
    for name, (chunks, page_to) in built.items():
        for p, target in page_to.items():                               # /dialogus/p/27/ -> the chapter, at page 27
            d = os.path.join(OUT, name, 'p', str(p)); os.makedirs(d)
            open(os.path.join(d, 'index.html'), 'w').write(
                f'<!doctype html><meta charset="utf-8"><title>Page {p}</title><link rel="canonical" href="{SITE}/{name}/{target}">'
                f'<meta http-equiv="refresh" content="0; url=../../{target}"><a href="../../{target}">{WORKS[name]["editor"]} p. {p}</a>')
        urls += [f'{name}/'] + [f"{name}/{c['slug']}/" for c in chunks]
    urls += ['glossary/', 'about/', 'rights/']
    json.dump({'redirects': [{'source': '/cap/(.*)', 'destination': '/dialogus/cap/$1', 'permanent': True},
                             {'source': '/epilogus/(.*)', 'destination': '/dialogus/epilogus/$1', 'permanent': True},
                             {'source': '/p/(.*)', 'destination': '/dialogus/p/$1', 'permanent': True}]},
              open(os.path.join(OUT, 'vercel.json'), 'w'), indent=1)
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        ''.join(f'<url><loc>{SITE}/{u}</loc></url>' for u in urls) + '</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')


if __name__ == '__main__':
    build()
