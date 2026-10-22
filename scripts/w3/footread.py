#!/usr/bin/env python3
"""Read the editor's page-foot apparatus from the plates through the Anthropic API (no agent overhead).
The scans' OCR of the foot loses figures and sigla (De incarn. first-chunk review, 2026-10-22: 3 of 4
errors), so for B+ volumes the brief takes the foot from this read instead of apparatus.json.
The key comes from the macOS Keychain (service "anthropic-api"), never from ANTHROPIC_API_KEY.
  uv run --with anthropic --with pillow scripts/w3/footread.py SLUG PAGE [PAGE ...]   # one by one
  uv run --with anthropic --with pillow scripts/w3/footread.py SLUG --submit [FIRST LAST]  # Batch API, -50%
  uv run --with anthropic --with pillow scripts/w3/footread.py SLUG --fetch BATCH_ID
  uv run --with anthropic --with pillow scripts/w3/footread.py SLUG --json   # foot/pNNN.txt -> apparatus_read.json
Writes text/SLUG/foot/pNNN.txt; --json writes text/SLUG/apparatus_read.json ({leaf: text}, as apparatus.json).
"""
import sys, os, io, re, csv, json, base64, subprocess, glob
import anthropic
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL = 'claude-sonnet-5-5'
CROP = 0.42          # the lower part of the leaf: the foot plus the last lines of text above it

PROMPT = """This image is the lower part of one printed page of a Latin critical edition (Wyclif Society, 1880s). Below the main text, in smaller type, is the editor's apparatus of variant readings: entries keyed by footnote figures, e.g. "10 ppcones A; pciones B; p°es C. 11 predicaciones secundum humanitatem O." The sigla are capital letters (A, B, C, O, M, D …); "om." = omits, "add." = adds; Latin words may be abbreviated, with superscript letters or a raised ° (e.g. "7°", "p°es").

Transcribe ONLY the apparatus at the foot. Skip the main text, the English side-notes in the margin, line numbers, the running head, the page number and the printer's signature line.

Rules:
1. One output line per apparatus entry, starting with its figure: "10 ppcones A; pciones B; p°es C."
2. Reproduce exactly what is printed, letter by letter: never expand an abbreviation, never correct a spelling, never substitute the word you expect. Keep the punctuation and the sigla as printed.
3. A letter or word you cannot read with confidence: give your best guess followed by [?]. Never guess silently.
4. For reference, the page's main text carries these footnote figures (in order): {figs}. Every figure should have an entry; if a figure has no entry at the foot, or the foot has an entry whose figure is not in this list, write a final line "CHECK: …" saying so. A long note (e.g. a source quotation) is transcribed whole.
5. If the page has no apparatus at all, output exactly: NONE

Output only the transcription: plain text, no commentary, no code fence."""


def client():
    key = subprocess.run(['security', 'find-generic-password', '-s', 'anthropic-api', '-w'],
                         capture_output=True, text=True, check=True).stdout.strip()
    return anthropic.Anthropic(api_key=key)


def offset(slug):
    for r in csv.DictReader(open(os.path.join(ROOT, 'catalog', 'plate_offsets.tsv')), delimiter='\t'):
        if r['slug'] == slug:
            return int(r['offset'])
    sys.exit(f'no plate offset for {slug}')


def figures(slug, page):
    """Footnote figures in the B+ transcription of the page (`word^12`)."""
    p = os.path.join(ROOT, 'text', slug, 'bt', f'p{page:03d}.txt')
    return re.findall(r'\^(\d+)', open(p).read()) if os.path.exists(p) else []


def pages(slug):
    return sorted(int(re.search(r'p(\d+)', f).group(1)) for f in glob.glob(os.path.join(ROOT, 'text', slug, 'bt', 'p*.txt')))


def params(slug, page):
    leaf = page + offset(slug)
    im = Image.open(os.path.join(ROOT, 'text', slug, 'raw', 'leaves', f'n{leaf:04d}.jpg')).convert('L')
    w, h = im.size
    buf = io.BytesIO()
    im.crop((0, int(h * (1 - CROP)), w, h)).save(buf, 'JPEG', quality=90)
    figs = figures(slug, page)
    content = [{'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/jpeg',
                                            'data': base64.b64encode(buf.getvalue()).decode()}},
               {'type': 'text', 'text': PROMPT.replace('{figs}', ', '.join(figs) if figs else '(none recorded)')}]
    return {'model': MODEL, 'max_tokens': 4000, 'messages': [{'role': 'user', 'content': content}]}


def save(slug, page, msg):
    text = ''.join(b.text for b in msg.content if b.type == 'text').strip()
    out = os.path.join(ROOT, 'text', slug, 'foot')
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, f'p{page:03d}.txt'), 'w', encoding='utf-8').write(text + '\n')
    u = msg.usage
    return {'page': page, 'input': u.input_tokens, 'output': u.output_tokens, 'unsure': text.count('[?]'),
            'check': 'CHECK:' in text, 'stop': msg.stop_reason}


slug, args = sys.argv[1], sys.argv[2:]
if args[0] == '--json':
    off, app = offset(slug), {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'text', slug, 'foot', 'p*.txt'))):
        page = int(re.search(r'p(\d+)', f).group(1))
        t = open(f).read().strip()
        if t != 'NONE':
            app[str(page + off)] = t
    json.dump(app, open(os.path.join(ROOT, 'text', slug, 'apparatus_read.json'), 'w'), ensure_ascii=False, indent=0)
    print(len(app), 'pages with apparatus')
    sys.exit()
c = client()
if args[0] == '--submit':
    ps = pages(slug)
    if len(args) == 3:
        ps = [p for p in ps if int(args[1]) <= p <= int(args[2])]
    b = c.messages.batches.create(requests=[{'custom_id': f'p{p}', 'params': params(slug, p)} for p in ps])
    log = os.path.join(ROOT, 'text', slug, 'foot', 'batches.log')
    os.makedirs(os.path.dirname(log), exist_ok=True)
    open(log, 'a').write(f'{b.id}\t{ps[0]}-{ps[-1]}\t{len(ps)} pages\n')
    print(b.id, b.processing_status, len(ps), 'pages')
elif args[0] == '--fetch':
    b = c.messages.batches.retrieve(args[1])
    print(b.processing_status, b.request_counts)
    if b.processing_status == 'ended':
        tin = tout = 0; bad = []; checks = []
        for r in c.messages.batches.results(b.id):
            if r.result.type != 'succeeded':
                bad.append((r.custom_id, r.result.type)); continue
            row = save(slug, int(r.custom_id[1:]), r.result.message)
            tin += row['input']; tout += row['output']
            if row['stop'] != 'end_turn': bad.append((r.custom_id, row['stop']))
            if row['check'] or row['unsure']: checks.append((row['page'], row['unsure'], row['check']))
        print(json.dumps({'input': tin, 'output': tout, 'usd_batch': round((tin * 3 + tout * 15) / 2e6, 2),
                          'problems': bad, 'to_look_at': sorted(checks)}))
else:
    for p in args:
        print(json.dumps(save(slug, int(p), c.messages.create(**params(slug, int(p))))))
