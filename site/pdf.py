"""Build PDFs of the finished Wyclif works with typst, from the same chunks the site reads.

    cd ~/wyclif && python3 site/pdf.py dialogus [bilingual|english|both]   -> pdf/<work>-<edition>.pdf

Reuses site/build.py's parser (scrub, curly, speeches, parse, load_work), so the PDF and the site cannot
disagree about the text. Editions: 'bilingual' (landscape, Latin | English, side-notes in a rail, notes at
the end of each chapter) and 'english' (6x9 reading edition, notes as footnotes, no Latin).
Needs typst on PATH and EB Garamond installed. Nothing here is deployed.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build as B                                                # noqa: E402  (importing does not build)

PDF_DIR = os.path.join(B.ROOT, 'pdf')
SPECIAL = {c: '\\' + c for c in '\\#$*_@<>[]~`'}
ESC = re.compile('[' + re.escape(''.join(SPECIAL)) + ']')


def esc(s):
    return ESC.sub(lambda m: SPECIAL[m.group(0)], s)


# ------------------------------------------------------------------ inline markup -> typst
def tx(s, lang, notes=None, foot=False):
    """One chunk string -> typst markup. notes = {n: text} for footnotes (English edition)."""
    s = B.scrub(s)
    s = s.replace('\\*', '\x00')
    if lang == 'en':
        s = B.curly(s)
    s = re.sub(r'\bB1\b', 'B¹', s)
    s = re.sub(r'\[([^\]\[]+)\]\{g:[a-z-]+\}', r'\1', s)          # glossary tags: text only in print
    toks = []

    def ph(t):
        toks.append(t)
        return f'\x01{len(toks) - 1}\x02'

    def noteref(m):
        n = int(m.group(1))
        if foot and notes and n in notes:
            return ph('#footnote[' + tx(strip_label(notes[n]), 'en') + '];')
        return ph(f'#nref[{n}];')
    s = re.sub(r'\[\^(\d+)\]', noteref, s)
    if lang == 'la':
        s = re.sub(r'\[p\. (\d+)\]\s*', lambda m: ph(f'#pg[{m.group(1)}];'), s)
    else:
        s = re.sub(r'\[(\d{1,3})\]\s*', lambda m: ph(f'#pg[{m.group(1)}];'), s)
    s = re.sub(r'\*\*(.+?)\*\*', '\x05\\1\x04', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', '\x03\\1\x04', s)
    s = re.sub(r'`([^`]+)`', r'\1', s)
    s = esc(s)
    s = s.replace('\x03', '#emph[').replace('\x05', '#strong[').replace('\x04', '];')
    s = re.sub('\x01(\\d+)\x02', lambda m: toks[int(m.group(1))], s)
    s = s.replace('\x00', '\\*')
    return s.strip()


def strip_label(t):
    return re.sub(r'^\*\*[A-Z/]+\.\*\*\s*', '', t)


def para(markup):
    """Guard a paragraph's first character against typst list/heading syntax."""
    return re.sub(r'^([=+\-/])', r'\\\1', markup)


# ------------------------------------------------------------------ structure
def heading_text(c):
    h = B.TITLE_RE.sub('', c['title'])
    return h[:1].upper() + h[1:]


def chapter_key(c):
    cid = c['fm']['chunk_id']
    if B.WORK == 'dialogus':
        return 'Epilogue' if 'epil' in cid else f'Chapter {int(cid.split("-")[-1])}'
    ch = cid.split('-')[-2]
    return 'Compendium' if ch == 'comp' else f'Chapter {int(ch)}'


def part_label(c):
    if B.WORK == 'dialogus':
        cid = c['fm']['chunk_id']
        return ('Part ' + ('one' if cid.endswith('a') else 'two')) if 'epil' in cid else ''
    return 'Part ' + str(ord(c['fm']['chunk_id'][-1]) - 96)


def groups(chunks):
    out = []
    for c in chunks:
        k = chapter_key(c)
        if not out or out[-1][0] != k:
            out.append((k, []))
        out[-1][1].append(c)
    return out


def chunk_rows(c, mode):
    """-> list of ('head', text, range) | ('headnote', [paras]) | ('passage', side, la, [en paras with speaker])."""
    rows, speaker, cur_page = [], c['start_speaker'], int(re.match(r'(\d+)', c['fm']['pages']).group(1))
    side = list(c['sidenotes'])
    for head, paras in c['sections']:
        if head == 'Headnote':
            rows.append(('headnote', paras))
            continue
        m = re.match(r'(.*?)\s*·\s*([\d.–-]+)$', head)
        rows.append(('head', m.group(1) if m else head, m.group(2) if m else ''))
        la, en = None, []

        def flush():
            nonlocal la, en, cur_page
            if la is None and not en:
                return
            pages = [int(p) for p in re.findall(r'\[p\. (\d+)\]', la or '')]
            span = set([cur_page] + pages)
            mine = [s for s in side if s[0] in span]
            for s in mine:
                side.remove(s)
            if pages:
                cur_page = pages[-1]
            rows.append(('passage', mine, la, en))
            la, en = None, []
        for p in paras:
            if p.startswith('>'):
                flush()
                la = ' '.join(l.lstrip('> ').strip() for l in p.splitlines())
            else:
                text = re.sub(r'\s*\n\s*', ' ', p)
                if B.WORK == 'dialogus':
                    runs, speaker = B.speeches(text, speaker)
                else:
                    runs = [(None, text, False)]
                en.append(runs)
        flush()
    return rows


def en_paragraph(runs, notes, foot):
    """One English paragraph (a list of speech runs) -> typst."""
    parts = []
    for sp, t, opening in runs:
        who = f'#who("{ "Truth" if sp == "truth" else "Falsehood"}", "{sp}")' if opening and sp else ''
        parts.append(who + tx(t, 'en', notes, foot))
    return para(' '.join(parts))


def trans_markup(text):
    out = []
    for item in re.split(r'\n(?=- |\S)', text.strip()):
        item = item.strip()
        if not item or re.match(r'^-?\s*\*\*Pilot vs scaffold', item):
            continue
        head, *subs = re.split(r'\n\s+- ', item)
        head = re.sub(r'\s*\n\s*', ' ', re.sub(r'^-\s*', '', head))
        line = '- ' + tx(head, 'en')
        for s in subs:
            line += '\n  - ' + tx(re.sub(r'\s*\n\s*', ' ', s), 'en')
        out.append(line)
    return '\n'.join(out)


# ------------------------------------------------------------------ typst preamble
PREAMBLE = r'''
#let russet = rgb("#7C3F24")
#let gilt = rgb("#7A5F12")
#let grey = rgb("#5A5E55")
#let rule-c = rgb("#B9BDB2")
#let pg(n) = text(size: 0.7em, fill: grey, weight: "regular", style: "normal")[#h(0.15em)\[#n\]#h(0.1em)]
#let nref(n) = super(typographic: false, text(fill: russet, size: 0.8em)[#n])
#let who(name, sp) = [#text(weight: "bold", fill: if sp == "truth" { russet } else { gilt }, features: ("smcp",))[#name.]#h(0.35em)]
'''

BILINGUAL = r'''
#set document(title: "__TITLE__", author: "John Wyclif; translated by Wilson Pruitt")
#set page(paper: "us-letter", flipped: true, margin: (x: 1.5cm, top: 1.8cm, bottom: 1.6cm),
  header: context {
    let here-pg = counter(page).get().first()
    let on-page = query(heading.where(level: 1).after(here())).filter(x => counter(page).at(x.location()).first() == here-pg)
    let prev = query(heading.where(level: 1).before(here()))
    let hs = if on-page.len() > 0 { (on-page.first(),) } else if prev.len() > 0 { (prev.last(),) } else { () }
    if hs.len() > 0 and here-pg > 3 {
      set text(size: 8.5pt, fill: grey)
      [#emph[__SHORT__] #h(1fr) #hs.first().body #h(1fr) #counter(page).display()]
    }
  })
#set text(font: "EB Garamond", size: 10.5pt, lang: "en", hyphenate: false)
#set par(justify: true, leading: 0.62em, spacing: 0.75em)
#show heading.where(level: 1): it => { pagebreak(weak: true); v(0.4em); text(size: 17pt, weight: "regular", fill: russet)[#it.body]; v(0.2em) }
#show heading.where(level: 2): it => { v(0.8em); text(size: 12pt, style: "italic")[#it.body]; v(0.3em) }
#let la-text(body) = text(size: 9.6pt, body)
#let passage(side, la, en) = grid(columns: (3.2cm, 1fr, 1.15fr), column-gutter: 0.5cm, row-gutter: 0.4em,
  { set text(size: 8pt, fill: grey); set par(justify: false, leading: 0.5em); side },
  la-text(la), en)
#let sidenote(at, body) = block(below: 0.5em)[#text(weight: "bold", size: 7.5pt)[#at] #emph[#body]]
#let colhead = grid(columns: (3.2cm, 1fr, 1.15fr), column-gutter: 0.5cm,
  [], text(size: 8.5pt, fill: grey, features: ("smcp",))[Latin], text(size: 8.5pt, fill: grey, features: ("smcp",))[English])
#let sechead(t, r) = block(above: 1em, below: 0.35em, sticky: true)[#text(size: 9pt, fill: grey, style: "italic")[#t #h(0.4em) #r]]
#let notes-block(body) = { set text(size: 9pt); set par(leading: 0.55em); v(0.6em); line(length: 100%, stroke: 0.4pt + rule-c); v(0.2em); text(size: 10pt, style: "italic")[Notes]; v(0.2em); body }
#let note(n, body) = block(below: 0.45em)[#text(fill: russet, weight: "bold")[#n.] #body]
'''

ENGLISH = r'''
#set document(title: "__TITLE__", author: "John Wyclif; translated by Wilson Pruitt")
#set page(width: 6in, height: 9in, margin: (inside: 0.95in, outside: 0.8in, top: 0.9in, bottom: 0.95in),
  header: context {
    let here-pg = counter(page).get().first()
    let on-page = query(heading.where(level: 1).after(here())).filter(x => counter(page).at(x.location()).first() == here-pg)
    let prev = query(heading.where(level: 1).before(here()))
    let hs = if on-page.len() > 0 { (on-page.first(),) } else if prev.len() > 0 { (prev.last(),) } else { () }
    if hs.len() > 0 and here-pg > 3 {
      set text(size: 8.5pt, fill: grey)
      if calc.even(counter(page).get().first()) [#counter(page).display() #h(1fr) #emph[__SHORT__]] else [#hs.first().body #h(1fr) #counter(page).display()]
    }
  })
#set text(font: "EB Garamond", size: 11pt, lang: "en", hyphenate: true)
#set par(justify: true, leading: 0.66em, spacing: 0.8em, first-line-indent: 0em)
#set footnote.entry(separator: line(length: 25%, stroke: 0.4pt + rule-c), gap: 0.5em)
#show footnote.entry: set text(size: 8.8pt)
#show footnote.entry: set par(leading: 0.5em)
#show heading.where(level: 1): it => { pagebreak(weak: true); v(2.2em); align(center, text(size: 17pt, weight: "regular", fill: russet)[#it.body]); v(0.6em) }
#show heading.where(level: 2): it => { v(1.1em); align(center, text(size: 11.5pt, style: "italic")[#it.body]); v(0.35em) }
#let headnote(body) = block(inset: (x: 0.8em, y: 0.2em), stroke: (left: 1.5pt + rule-c))[#set text(size: 10pt, style: "italic"); #body]
'''

FRONT = r'''
#let titlepage(la, sub, lede, editor, year) = {
  set page(header: none, footer: none)
  v(18%)
  align(center)[
    #text(size: 30pt, fill: russet, font: ("Libre Caslon Display", "EB Garamond"))[#la]
    #v(0.3em)
    #text(size: 13pt, style: "italic")[#sub]
    #v(2.2em)
    #text(size: 12pt)[John Wyclif]
    #v(0.3em)
    #text(size: 10.5pt, fill: grey)[Latin text of #editor’s edition for the Wyclif Society (#year),\ with a new English translation and notes]
    #v(1.4em)
    #text(size: 11pt)[Translated by Wilson Pruitt]
    #v(1fr)
    #text(size: 9.5pt, fill: grey)[Wroot Press · wyclif.wrootpress.com]
  ]
  pagebreak()
}
'''


def front_matter(w, kind):
    lede = re.sub(r'<[^>]+>', '', w.get('lede', '')).replace('\n', ' ')
    return lede


def build_typst(work, edition):
    B.use(work)
    w = B.WORKS[work]
    gl_rows, _ = B.glossary()
    chunks = B.load_work(work)
    name = w['name']
    sub = {'dialogus': 'sive Speculum Ecclesie Militantis'}.get(work, w.get('sub', ''))
    if work == 'dialogus':
        lede = ('John Wyclif’s dialogue between Truth and Falsehood on whether the church should own property, '
                'written in 1379. The Latin of Alfred Pollard’s edition, with a new English translation and notes.')
    else:
        nch = len({chapter_key(c) for c in chunks if chapter_key(c) != 'Compendium'})
        lede = re.sub(r'<[^>]+>', '', w['lede']).replace('\n', ' ').format(chapters=nch, parts=len(chunks), words=0)
        lede = re.sub(r'\s*about 0 words of English\.', '', lede)
    year_ed = {'dialogus': '1886', 'ecclesia': '1886', 'potestate-pape': '1907'}[work]
    foot = edition == 'english'
    title = f'{name}: ' + ('Latin and English' if edition == 'bilingual' else 'English')
    out = [PREAMBLE, (BILINGUAL if edition == 'bilingual' else ENGLISH).replace('__TITLE__', title).replace('__SHORT__', name), FRONT]
    out.append(f'#titlepage("{name}", "{sub or w["sub"]}", [], "{w["editor"]}", "{year_ed}")')
    # colophon + about
    out.append(f'''
#set page(numbering: none)
#v(1fr)
#block(width: 100%)[#set text(size: 9.5pt); #set par(justify: true)
*{name}*{": " + sub if sub else ""}. {"Latin and English" if edition == "bilingual" else "English translation"}. #linebreak()
{esc(lede)}

The Latin is the Wyclif Society’s edition, public domain. The English translation, notes and encoding are by Wilson Pruitt, Wroot Press,
and are offered under a Creative Commons Attribution-NonCommercial 4.0 licence (creativecommons.org/licenses/by-nc/4.0/). Ask before selling
this edition. Wroot Press is an imprint of Wroot Labs LLC. A working draft; the web edition, with the glossary and plates, is kept current at
wyclif.wrootpress.com, and corrections are welcome.
{"" if edition == "bilingual" else chr(10) + "Page numbers in the text, such as \\[4\\], mark the pages of the printed Latin edition, so a passage can be cited and found. Notes are footnotes."}
]
#pagebreak()
#align(center, text(size: 17pt, fill: russet)[Contents]) #v(0.5em)
#outline(title: none, depth: 2, indent: 1.2em)
''')
    page_line = (lambda c: '')
    for key, cs in groups(chunks):
        out.append(f'\n= {esc(key)}' + (f': {esc(heading_text(cs[0]))}' if len(cs) == 1 and work == 'dialogus' else '') + '\n')
        for c in cs:
            if not (len(cs) == 1 and work == 'dialogus'):
                out.append(f'== {esc(part_label(c))}: {esc(heading_text(c))}\n')
            out.append('#counter(footnote).update(0)\n' if foot else '')
            pages = c['fm']['pages']
            out.append(f'#align(center, text(size: 8.5pt, fill: grey)[{w["editor"]} pp. {esc(pages)}])\n')
            for row in chunk_rows(c, edition):
                if row[0] == 'headnote':
                    for p in row[1]:
                        out.append(f'#headnote[{tx(p, "en")}]\n' if foot else f'#block(width: 100%)[#set text(style: "italic", size: 9.5pt); {tx(p, "en")}]\n')
                elif row[0] == 'head':
                    if edition == 'bilingual':
                        out.append(f'#sechead[{tx(row[1], "en")}][{esc(row[2])}]\n')
                else:
                    _, mine, la, en = row
                    en_markup = '\n\n'.join(en_paragraph(r, c['notes'], foot) for r in en)
                    if edition == 'english':
                        out.append(en_markup + '\n')
                    else:
                        rail = ''.join(f'#sidenote[{s[0]}.{s[1]}][{tx(s[2], "en")}]\n' for s in mine)
                        lam = tx(la, 'la') if la else ''
                        out.append(f'#passage([{rail}], [{lam}], [{en_markup}])\n')
            if edition == 'bilingual':
                if c['notes']:
                    items = ''.join(f'#note({n})[{tx(strip_label(t), "en")}]\n' for n, t in sorted(c['notes'].items()))
                    out.append(f'#notes-block[{items}]\n')
                if c['trans']:
                    out.append('#block[#set text(size: 8.5pt); #set par(leading: 0.5em); #text(style: "italic")[How the Latin of this passage was established]\n'
                               + trans_markup(c['trans']) + ']\n')
    # glossary
    out.append('\n#pagebreak(weak: true)\n= Glossary\n')
    out.append('#text(size: 9.5pt)[The renderings held steady across the translation. Each row: the Latin term, its English, and a note where the choice needs defending.]\n')
    sect = None
    for r in gl_rows:
        if r['section'] != sect:
            sect = r['section']
            out.append(f'\n== {esc(sect[1])}\n')
        note = f' #text(fill: grey)[{tx(r["note"], "en")}]' if r['note'] else ''
        out.append(f'#block(below: 0.4em)[#text(size: 9.5pt)[#emph[{tx(r["la"], "la")}]: {tx(r["en"], "en")}.{note}]]\n')
    return '\n'.join(out)


def main():
    work = sys.argv[1] if len(sys.argv) > 1 else 'dialogus'
    which = sys.argv[2] if len(sys.argv) > 2 else 'both'
    os.makedirs(PDF_DIR, exist_ok=True)
    for ed in (['bilingual', 'english'] if which == 'both' else [which]):
        src = os.path.join(PDF_DIR, f'.{work}-{ed}.typ')
        open(src, 'w').write(build_typst(work, ed))
        dst = os.path.join(PDF_DIR, f'{work}-{ed}.pdf')
        r = subprocess.run(['typst', 'compile', src, dst], capture_output=True, text=True)
        print(f'{work} {ed}:', 'ok' if r.returncode == 0 else 'FAILED', dst if r.returncode == 0 else '')
        if r.returncode:
            print(r.stderr[:3000])


if __name__ == '__main__':
    main()
