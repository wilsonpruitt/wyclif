"""The editor's italic runs, from the primary scan's ABBYY XML (WORKFLOW stage 5, 2026-10-07).

    python3 scripts/w3/italics.py SLUG        → text/SLUG/italics.tsv (page, text) and a count

Italics are the EDITOR's call (Loserth marking what he took for a quotation), tracked, never verified
(Wilson, 2026-10-04). archive.org's djvu.xml has no font styles, but the `_abbyy.gz` of the same scan marks
`italic="true"` on its formatting runs, so the runs are taken from there instead of from the plates.
brief.py inlines them per page, as evidence for the translator.

ABBYY page indices are NOT the djvu leaves (the gap drifts: +62 at p. 2, +64 at p. 402 of De potestate pape),
so each page is numbered from its own running head, and pages without a legible head take the offset of the
nearest page that has one. Runs shorter than 2 words of 2+ letters are dropped (margin specks, side-note
fragments), and so is any run found in the page's foot apparatus (text/SLUG/apparatus.json, from witness.py):
the apparatus is in the brief already. Consecutive italic runs are joined; a side-note between them splits
a run in two, which is harmless for evidence.
"""
import csv, gzip, json, os, re, subprocess, sys
from xml.etree.ElementTree import iterparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def pages(path):
    """Yield (index, [(italic, text, left)]) per ABBYY page, one entry per formatting run."""
    idx, runs = -1, []
    for ev, el in iterparse(gzip.open(path), events=('start', 'end')):
        tag = el.tag.rsplit('}', 1)[-1]
        if ev == 'start' and tag == 'page':
            idx, runs = idx + 1, []
        elif ev == 'end' and tag == 'formatting':
            chars = list(el)
            txt = ''.join(c.text or '' for c in chars)
            left = int(chars[0].get('l', 0)) if chars else 0
            runs.append((el.get('italic') == 'true', txt, left))
            el.clear()
        elif ev == 'end' and tag == 'page':
            yield idx, runs
            el.clear()


def head_number(runs, first, last):
    """The printed page number from the running head (the first two runs), or None."""
    for _, txt, _ in runs[:2]:
        for m in re.findall(r'(?<![\d,])(\d{1,3})(?![\d,])', txt):
            if first <= int(m) <= last:
                return int(m)
    return None


def main(slug):
    off = {r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t')}[slug]
    item, first, last = off['item'], int(off['first_page']), int(off['last_page'])
    raw = f'{ROOT}/text/{slug}/raw/{item}_abbyy.gz'
    if not os.path.exists(raw):
        os.makedirs(os.path.dirname(raw), exist_ok=True)
        subprocess.run(['curl', '-sL', '-o', raw, f'https://archive.org/download/{item}/{item}_abbyy.gz'], check=True)
    app_path = f'{ROOT}/text/{slug}/apparatus.json'
    app = json.load(open(app_path)) if os.path.exists(app_path) else {}
    squash = lambda t: re.sub(r'[^a-z]', '', t.lower())
    allp = list(pages(raw))
    anchors = {i: i - n for i, runs in allp if (n := head_number(runs, first, last)) is not None}
    # an anchor whose offset disagrees with both neighbours is a misread number (a line number, a date)
    keys = sorted(anchors)
    good = {k: anchors[k] for j, k in enumerate(keys)
            if anchors[k] in {anchors[keys[j - 1]] if j else None, anchors[keys[j + 1]] if j + 1 < len(keys) else None}}
    gk = sorted(good)
    rows = []
    for i, runs in allp:
        if not gk:
            break
        near = min(gk, key=lambda k: abs(k - i))
        pg = i - good[near]
        if not first <= pg <= last:
            continue
        cur = []
        for it, txt, _ in runs[2:] + [(False, '', 0)]:          # skip the running head
            if it:
                cur.append(txt.strip())
                continue
            if cur:
                text = re.sub(r'\s+', ' ', ' '.join(cur)).strip()
                text = re.sub(r'\s*-\s+(?=[a-z])', '', text)     # rejoin a word broken at the line end
                in_app = squash(text) and squash(text) in squash(app.get(str(pg + int(off['offset'])), ''))
                if len(re.findall(r'[A-Za-z]{2,}', text)) >= 2 and not in_app:
                    rows.append((pg, text))
                cur = []
    out = f'{ROOT}/text/{slug}/italics.tsv'
    with open(out, 'w') as f:
        f.write('page\ttext\n')
        for pg, text in rows:
            f.write(f'{pg}\t{text}\n')
    print(f'{len(rows)} italic runs on {len({p for p, _ in rows})} pages → {os.path.relpath(out, ROOT)} '
          f'(page heads read: {len(good)} of {len(allp)} ABBYY pages)')


if __name__ == '__main__':
    main(sys.argv[1])
