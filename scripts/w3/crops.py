"""Plate-crop sheets for the words the vote cannot settle (CONVENTIONS §3.4).

    .venv/bin/python scripts/w3/crops.py SLUG [FIRST_PAGE LAST_PAGE] [--per 8] [--queue scar_queue.tsv --out crops_scars] [--decisions bplus_decisions.tsv]

For each open queue item (text/<slug>/plate_queue.tsv minus plate_decisions.tsv):
fetch the page image (cached in text/<slug>/raw/leaves/), cut a strip of the line
with the line above and below, box the word in red, and stack strips into numbered
sheets text/<slug>/crops/sheet_NNN.jpg with an index sheet_NNN.tsv.

Reading a sheet: for each numbered strip, read the WHOLE middle line (the
normalisation class lives in the neighbours), then write one row per item to
text/<slug>/plate_decisions.tsv:
    page  pos  rule  forms  reading  note
`reading` is the print's form exactly as printed (medieval spelling, no
normalisation), `∅` if the print has no word there, or the heading text for HEAD.
vote.py applies decisions on the next run; a decision whose `forms` no longer
matches the queue is reported as stale and re-queued.
"""
import csv, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def leaf_image(slug, item, leaf, other=False):
    d = f'{ROOT}/text/{slug}/raw/leaves'
    os.makedirs(d, exist_ok=True)
    p = f'{d}/{item}_n{leaf:04d}.jpg' if other else f'{d}/n{leaf:04d}.jpg'   # another scan's leaf (pivotpatch)
    if not os.path.exists(p) or os.path.getsize(p) < 5000:
        subprocess.run(['curl', '-sL', '-o', p, f'https://archive.org/download/{item}/page/n{leaf}.jpg'],
                       check=True)
    return p


def main(slug, first=None, last=None, per=8, queue='plate_queue.tsv', outdir='crops', decisions='plate_decisions.tsv'):
    off = {r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t')}[slug]
    item = off['item']
    q = list(csv.DictReader(open(f'{ROOT}/text/{slug}/{queue}'), delimiter='\t', quoting=csv.QUOTE_NONE))
    dpath = f'{ROOT}/text/{slug}/{decisions}'      # B+: bplus_decisions.tsv
    done = set()
    if os.path.exists(dpath):
        done = {(r['page'], r['pos']) for r in csv.DictReader(open(dpath), delimiter='\t', quoting=csv.QUOTE_NONE)}
    q = [r for r in q if (r['page'], r['pos']) not in done]
    if first:
        q = [r for r in q if int(first) <= int(r['page']) <= int(last)]
    out = f'{ROOT}/text/{slug}/{outdir}'
    os.makedirs(out, exist_ok=True)
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 44)
    except OSError:
        font = ImageFont.load_default()
    sheets = 0
    for s in range(0, len(q), per):
        batch = q[s:s + per]
        strips = []
        for n, r in enumerate(batch, 1):
            src, _, leaf = r['leaf'].rpartition(':')      # 'witness:leaf' = a page pivot-patched from another scan
            leaf = int(leaf)
            l, t, rr, b = (int(x) for x in r['box'].split(','))
            im = Image.open(leaf_image(slug, src or item, leaf, other=bool(src))).convert('RGB')
            h = max(b - t, 20)
            box = (0, max(0, int(t - 2.2 * h)), im.width, min(im.height, int(b + 2.0 * h)))
            strip = im.crop(box)
            dr = ImageDraw.Draw(strip)
            dr.rectangle((l - 6, t - box[1] - 6, rr + 6, b - box[1] + 6), outline=(220, 0, 0), width=5)
            # label column
            lab = Image.new('RGB', (strip.width + 260, strip.height), 'white')
            lab.paste(strip, (260, 0))
            ImageDraw.Draw(lab).text((12, 12), f'{s // per + 1}.{n}\np.{r["page"]}\n{r["rule"]}', fill=(0, 0, 180), font=font)
            strips.append(lab)
        W = max(x.width for x in strips)
        H = sum(x.height for x in strips) + 12 * len(strips)
        sheet = Image.new('RGB', (W, H), (200, 200, 200))
        y = 0
        for x in strips:
            sheet.paste(x, (0, y)); y += x.height + 12
        if sheet.width > 1800:
            sheet = sheet.resize((1800, int(sheet.height * 1800 / sheet.width)))
        sheets += 1
        sheet.save(f'{out}/sheet_{sheets:03d}.jpg', quality=82)
        with open(f'{out}/sheet_{sheets:03d}.tsv', 'w') as f:
            extra = [k for k in ('printed', 'proposed') if k in batch[0]]          # scar_queue.tsv carries these
            f.write('n\tpage\tpos\trule\tforms' + ''.join('\t' + k for k in extra) + '\n')
            for n, r in enumerate(batch, 1):
                f.write(f'{s // per + 1}.{n}\t{r["page"]}\t{r["pos"]}\t{r["rule"]}\t{r["forms"]}' + ''.join('\t' + r[k] for k in extra) + '\n')
    print(f'{len(q)} open items -> {sheets} sheets in {out}/')


if __name__ == '__main__':
    argv = sys.argv[1:]
    opt = {}
    for k in ('--per', '--queue', '--out', '--decisions'):
        if k in argv:
            i = argv.index(k); opt[k[2:]] = argv[i + 1]; del argv[i:i + 2]
    main(*argv, per=int(opt.get('per', 8)), queue=opt.get('queue', 'plate_queue.tsv'), outdir=opt.get('out', 'crops'),
         decisions=opt.get('decisions', 'plate_decisions.tsv'))
