"""Plate sheets for the side-notes the re-OCR cannot vouch for (WORKFLOW stage 5).

    .venv/bin/python scripts/w3/sidesheets.py SLUG [--height 1500] [--all | --spot N]

--spot N cuts every Nth UNflagged note instead: the control on what ships unread.

Input: text/<slug>/sidenotes.ocr.tsv (sideocr.py). A band is cut for every note with a flag,
and for every place where the archive OCR (sidenotes/<slug>.tsv) saw margin words and the
re-OCR has no note (`missed`). Each band shows the margin column and the edge of the text, with
every main-text row's printed page.line written at its baseline, so a note is read and placed
in one look. Bands stack into text/<slug>/sidecrops/sheet_NNN.jpg; sheet_NNN.tsv lists, per
band, the note id (row number in sidenotes.ocr.tsv, or M for missed), its draft and flags.

Reading a sheet, one row per band to the part file the brief names:
    id  page  line  text
`text` is the note exactly as printed (hyphenated line-breaks joined), `ok` if the draft is
right as it stands, `∅` if there is no side-note there (a folio mark, a line number, a speck).
Several notes in one band: one row each, the first with the band's id, the rest with id `+`.
"""
import csv, json, os, re, statistics as st, sys
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from chapters import pg_line
from crops import leaf_image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LAB = 150          # label column width
TEXT = 260         # px of the text column kept beside the notes


def main(slug, height=1500, every=False, spot=0):
    off = {r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t')}[slug]
    item, offset = off['item'], int(off['offset'])
    last = int(off.get('last_page') or 10 ** 6)
    base = f'{ROOT}/text/{slug}'
    marks = defaultdict(list)
    if os.path.exists(f'{base}/linemarks.tsv'):
        for r in csv.DictReader(open(f'{base}/linemarks.tsv'), delimiter='\t'):
            marks[int(r['leaf'])].append((int(r['row']), int(r['printed'])))
    rowy, lefts, rights = defaultdict(list), defaultdict(list), defaultdict(list)
    for l in open(f'{base}/witnesses/{item}.jsonl'):
        t = json.loads(l)
        if t.get('head'):
            continue
        rowy[(t['leaf'], t['line'])].append(t['box'][3])
        lefts[t['leaf']].append(t['box'][0]); rights[t['leaf']].append(t['box'][2])
    rows = defaultdict(list)                  # leaf -> [(baseline, row)]
    for (lf, rw), ys in rowy.items():
        rows[lf].append((st.median(ys), rw))

    ocr = list(csv.DictReader(open(f'{base}/sidenotes.ocr.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE))
    items = []                                # (leaf, y0, y1, id, draft, flags)
    spans = defaultdict(list)
    for i, r in enumerate(ocr, 1):
        lf, y, y1 = int(r['leaf']), int(r['y']), int(r['y1'])
        spans[lf].append((y - 25, y1 + 25))
        if (every or r['flags']) if not spot else (not r['flags'] and i % spot == 0):
            items.append((lf, y, y1, str(i), f"{r['page']}.{r['line']}: {r['text']}", r['flags']))
    # missed: archive-OCR margin rows with real letters that no re-OCR note covers
    side, arch = defaultdict(list), []
    for r in csv.DictReader(open(f'{ROOT}/sidenotes/{slug}.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
        lf = int(r['leaf'])
        if 1 <= lf - offset <= last:
            side[lf].append(int(r['x']))
            arch.append((lf, int(r['y']), int(r['x']), r['text'].strip()))
    mid = {lf: (st.median(lefts[lf]) + st.median(rights[lf])) / 2 for lf in side if lefts[lf]}
    for lf, y, x, txt in arch:
        if lf not in mid or (x < mid[lf]) != (st.median(side[lf]) < mid[lf]):
            continue                          # the other margin: folio marks, line numbers
        if not spot and re.search(r'[A-Za-z]{3,}', txt) and not any(a - 30 <= y <= b + 30 for a, b in spans[lf]):
            if items and items[-1][3] == 'M' and items[-1][0] == lf and y - items[-1][2] < 150:
                items[-1] = items[-1][:2] + (y + 30,) + items[-1][3:]
            else:
                items.append((lf, y - 10, y + 30, 'M', txt, 'missed'))

    out = f'{base}/sidecrops'
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(f'{out}/{f}')
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 26)
        big = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 32)
    except OSError:
        font = big = ImageFont.load_default()

    bands, n = [], 0
    for lf, y, y1, nid, draft, flags in sorted(items, key=lambda t: (t[0], t[1])):
        n += 1
        im = Image.open(leaf_image(slug, item, lf)).convert('RGB')
        W = im.width
        left = st.median(side[lf] or [W]) < W / 2
        L = sorted(lefts[lf]); R = sorted(rights[lf])
        colL, colR = L[len(L) // 20], R[-len(R) // 20 - 1]
        x0, x1 = (0, min(W, colL + TEXT)) if left else (max(0, colR - TEXT), W)
        y0, y1 = max(0, y - 90), min(im.height, y1 + 80)
        crop = im.crop((x0, y0, x1, y1))
        band = Image.new('RGB', (LAB + crop.width, crop.height + 44), 'white')
        band.paste(crop, (LAB, 44))
        dr = ImageDraw.Draw(band)
        dr.text((8, 4), f'[{n}]  p. {lf - offset}', fill=(200, 0, 0), font=big)
        for by, rw in sorted(rows[lf]):
            if y0 + 20 <= by <= y1:
                yy = by - y0 + 44
                p, ln = pg_line(marks, offset, lf, rw)
                dr.text((8, yy - 28), f'{p}.{ln}', fill=(0, 0, 190), font=font)
                dr.line((LAB - 40, yy, LAB - 4, yy), fill=(120, 120, 230), width=2)
        bands.append((n, lf - offset, lf, band, nid, draft, flags))

    sheets, cur, h = [], [], 0
    for b in bands:
        if cur and h + b[3].height > height:
            sheets.append(cur); cur, h = [], 0
        cur.append(b); h += b[3].height + 14
    if cur:
        sheets.append(cur)
    for i, s in enumerate(sheets, 1):
        Wd = max(b[3].width for b in s)
        sheet = Image.new('RGB', (Wd, sum(b[3].height + 14 for b in s)), (190, 190, 190))
        y = 0
        for b in s:
            sheet.paste(b[3], (0, y)); y += b[3].height + 14
        sheet.save(f'{out}/sheet_{i:03d}.jpg', quality=85)
        with open(f'{out}/sheet_{i:03d}.tsv', 'w') as f:
            f.write('band\tid\tpage\tleaf\tflags\tdraft\n')
            for b in s:
                f.write(f'{b[0]}\t{b[4]}\t{b[1]}\t{b[2]}\t{b[6]}\t{b[5]}\n')
    kinds = defaultdict(int)
    for b in bands:
        kinds['missed' if b[4] == 'M' else 'flagged'] += 1
    print(f'{len(bands)} bands ({dict(kinds)}) -> {len(sheets)} sheets in {out}')


if __name__ == '__main__':
    a = sys.argv[1:]
    h = int(a[a.index('--height') + 1]) if '--height' in a else 1500
    main(a[0], h, '--all' in a, int(a[a.index('--spot') + 1]) if '--spot' in a else 0)
