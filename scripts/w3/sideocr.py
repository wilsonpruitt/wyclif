"""Re-OCR the editor's side-notes with tesseract on the margin column alone (WORKFLOW stage 5).

    .venv/bin/python scripts/w3/sideocr.py SLUG [LEAF ...]

The archive OCR reads the margin as part of a two-column page and garbles it; cut alone, the
notes are clean modern English type. For each body leaf with notes in sidenotes/<slug>.tsv:
crop the note column (outside the main text, below the running head), upscale 2x, tesseract
(psm 4), group lines into notes at tesseract's paragraph breaks, and place each note at the
page.line of the main-text row nearest its first line. Writes text/<slug>/sidenotes.ocr.tsv:
    page  line  leaf  y  y1  conf  flags  text
`flags` are the markers the side-note pass reads on the plate (sidesheets.py); a note with no
flag ships as read (memory: plate-read triage).
"""
import csv, json, os, re, statistics as st, subprocess, sys, tempfile
from collections import defaultdict
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from chapters import pg_line
from crops import leaf_image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WORDS = set()
for p in ('/usr/share/dict/words', f'{ROOT}/catalog/lexicon/english_extra.txt'):
    if os.path.exists(p):
        WORDS |= {w.strip().lower() for w in open(p)}


def norm(w):
    return w.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')


def word_ok(w, freq={}):
    w = norm(w).strip('.,;:()[]\'"?-—–!').lower()
    if freq.get(w, 0) >= 3 and re.fullmatch(r"[a-z']{4,}", w):
        return True                 # an OCR error is rarely repeated letter for letter
    if not w or w.isdigit() or re.fullmatch(r'[ivxlc]+|\d+[.)]?|[a-h][.)]', w):
        return True
    if w.endswith("'s"):
        w = w[:-2]
    for c in (w, w.rstrip('s'), w[:-2] if w.endswith('es') else w, w[:-2] if w.endswith('ed') else w,
              w[:-1] if w.endswith('d') else w, w[:-3] if w.endswith('ing') else w,
              w[:-3] + 'y' if w.endswith(('ies', 'ied')) else w, w[:-3] + 'e' if w.endswith('ing') else w,
              w[:-2] if w.endswith('ly') else w, w[:-1] if w.endswith('r') else w):
        if c in WORDS:
            return True
    return False


def main(slug, only=None):
    off = {r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t')}[slug]
    item, offset = off['item'], int(off['offset'])
    last = int(off.get('last_page') or 10 ** 6)
    base = f'{ROOT}/text/{slug}'
    marks = defaultdict(list)
    if os.path.exists(f'{base}/linemarks.tsv'):
        for r in csv.DictReader(open(f'{base}/linemarks.tsv'), delimiter='\t'):
            marks[int(r['leaf'])].append((int(r['row']), int(r['printed'])))
    rowtok = defaultdict(list)
    headb = defaultdict(int)
    for l in open(f'{base}/witnesses/{item}.jsonl'):
        t = json.loads(l)
        if t.get('head'):
            if t['box'][1] < 400:                   # the running head, not a chapter heading
                headb[t['leaf']] = max(headb[t['leaf']], t['box'][3])
            continue
        rowtok[(t['leaf'], t['line'])].append(t['box'])
    rows = defaultdict(list)                  # leaf -> [(baseline, row, left, right)]
    for (lf, rw), bs in rowtok.items():
        rows[lf].append((st.median(b[3] for b in bs), rw, min(b[0] for b in bs), max(b[2] for b in bs)))
    notes = defaultdict(list)
    for r in csv.DictReader(open(f'{ROOT}/sidenotes/{slug}.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
        lf = int(r['leaf'])
        if 1 <= lf - offset <= last:
            notes[lf].append(int(r['x']))

    outp = f'{base}/sidenotes.ocr.tsv'
    keep = []
    if only and os.path.exists(outp):
        keep = [r for r in csv.DictReader(open(outp), delimiter='\t', quoting=csv.QUOTE_NONE)
                if int(r['leaf']) not in only]
    res = []
    tmp = tempfile.mkdtemp()
    for lf in sorted(notes):
        if only and lf not in only:
            continue
        if not rows.get(lf):
            continue
        im = Image.open(leaf_image(slug, item, lf)).convert('L')
        W = im.width
        left = st.median(notes[lf]) < W / 2
        body = [r for r in rows[lf] if r[3] - r[2] > 0.5 * W]   # full-measure rows only
        if not body:
            body = rows[lf]
        if left:
            x0, x1 = 0, int(st.median(r[2] for r in body)) - 6
        else:
            x0, x1 = int(st.median(r[3] for r in body)) + 6, W
        y0 = headb.get(lf, 0) + 8
        crop = im.crop((x0, y0, x1, im.height)).resize(((x1 - x0) * 2, (im.height - y0) * 2))
        p = f'{tmp}/c.png'
        crop.save(p)
        tsv = subprocess.run(['tesseract', p, '-', '--psm', '4', 'tsv'], capture_output=True, text=True).stdout
        lines = defaultdict(list)
        for r in csv.DictReader(tsv.splitlines(), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not r['text'].strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            lines[k].append((int(r['left']), int(r['top']) / 2 + y0, (int(r['top']) + int(r['height'])) / 2 + y0,
                             float(r['conf']), r['text']))
        # group lines into notes: same block, no vertical gap over 1.2 line heights; a line that
        # starts lower-case after one that ends without a stop continues across a wider gap
        cur, prev = None, None
        for k in sorted(lines, key=lambda k: min(w[1] for w in lines[k])):
            ws = sorted(lines[k])
            top, bot = min(w[1] for w in ws), max(w[2] for w in ws)
            txt = ' '.join(w[4] for w in ws)
            if re.fullmatch(r'[\dIlOoL|\s.,*]+|[\W_]+', txt) or (len(txt) <= 3 and not txt[0].isalpha()):
                continue            # a printed line number, a folio digit, a speck
            gap, lh = top - prev[1] if prev else 0, bot - top
            if cur and cur['text'].endswith('-') and gap < 3 * lh:
                cur['words'] += ws
                cur['text'] = cur['text'][:-1] + txt
            elif cur and k[0] == prev[0] and (gap < 1.2 * lh or (
                    (txt[0].islower() or cur['text'].endswith('-'))
                    and not cur['text'].endswith(('.', ':', ';', '?')) and gap < 3 * lh)):
                cur['words'] += ws                      # cur['bot'] stays the first line's
                cur['text'] = cur['text'][:-1] + txt if cur['text'].endswith('-') else cur['text'] + ' ' + txt
            else:
                cur = dict(leaf=lf, y=top, bot=bot, words=list(ws), text=txt)
                res.append(cur)
            prev = (k[0], bot)
    freq = {}
    for n in res:
        for w in n['text'].split():
            w = norm(w).strip('.,;:()[]\'"?-—–!').lower()
            freq[w] = freq.get(w, 0) + 1
    for n in res:
        lf = n['leaf']
        b = min(rows[lf], key=lambda r: abs(r[0] - n['bot']))     # first line's baseline
        n['page'], n['line'] = pg_line(marks, offset, lf, b[1])
        conf = min(w[3] for w in n['words'])
        n['conf'] = round(conf)
        fl = []
        bad = [w for w in n['text'].split() if not word_ok(w, freq)]
        if bad:
            fl.append('word:' + ','.join(bad[:4]))
        if conf < 70:
            fl.append('conf')
        if re.search(r'[|!{}\[\]<>~^_\\@#$%&*=+]', n['text']):
            fl.append('glyph')
        if len(n['words']) <= 2 or not re.search(r'[A-Za-z]{4,}', n['text']):
            fl.append('short')
        n['flags'] = ' '.join(fl)
    with open(outp, 'w') as f:
        f.write('page\tline\tleaf\ty\ty1\tconf\tflags\ttext\n')
        for r in keep:
            f.write('\t'.join(r[c] for c in ('page', 'line', 'leaf', 'y', 'y1', 'conf', 'flags', 'text')) + '\n')
        for n in res:
            f.write(f"{n['page']}\t{n['line']}\t{n['leaf']}\t{int(n['y'])}\t{int(max(w[2] for w in n['words']))}\t{n['conf']}\t{n['flags']}\t{n['text']}\n")
    fl = sum(1 for n in res if n['flags'])
    print(f'{len(res)} notes on {len(set(n["leaf"] for n in res))} leaves; {fl} flagged; -> {outp}')


if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], {int(x) for x in a[1:]} or None)
