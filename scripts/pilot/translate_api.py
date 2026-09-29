"""Cost pilot: translate one Dialogus chunk in ONE Messages API call (no agent loop).

    cd ~/wyclif && .venv/bin/python scripts/pilot/translate_api.py 02 14 30

Cached prefix: a short method preamble + CARD.md + GLOSSARY.md (identical bytes on every call).
Per-chunk request: the untranslated scaffold (first commit of the chunk), Pollard's corrected
side-notes and the page-foot apparatus for the chunk's pages. The model returns the whole chunk
plus a report. Output: chunks/dialogus/_pilot/wyc-dialogus-NN.api.md and usage.jsonl.
"""
import json, os, re, subprocess, sys, time
import anthropic

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'chunks', 'dialogus', '_pilot')
APPARATUS = os.environ.get('APPARATUS_JSON')        # page -> apparatus text, from djvu.py split_leaf
MODEL = 'claude-opus-5-5'
EFFORT = os.environ.get('EFFORT', 'high')
PRICE = {'in': 4.00, 'cache_write': 5.00, 'cache_read': 0.20, 'out': 20.00}   # $/MTok, Opus 5.5 (5-min cache write = 1.25x)

PREAMBLE = """You are translating John Wyclif's Latin *Dialogus* (ed. Pollard, 1886) into English for a scholarly
edition, one chunk at a time. The working card and the frozen glossary follow; they govern every choice.

You work in a single pass and cannot open files, plates or sources. Where the card says to open a plate,
run a script, or look something up, do this instead:
- Pollard's apparatus for each page is given with the chunk. Use it as the card says (a variant that gives
  the sense: translate it with a T note citing the siglum; otherwise translate the print and flag it).
- A word you would check on the plate: translate the print, flag it in a T note, and list it under
  "Latin doubts" in your report.
- Scripture: quote the Douay-Rheims (Challoner) wording as closely as you know it, and list every
  reference you quote under "DR quotations" so it can be checked against the text.
- Sources and dated facts: identify them in the notes as the card says and list each as a ledger row
  with status to-verify.
- Pollard's side-notes are given already corrected: copy that section through unchanged.
- The "Transcription notes" section is given: copy it through unchanged.

Return exactly two things, in this order:
1. The complete chunk file in Markdown: the front matter with `status: translated`, the title, every
   section with its Latin block unchanged followed by the English, Pollard's side-notes, Notes, and
   Transcription notes, in the card's layout.
2. After a line containing only `===REPORT===`: "Ledger rows" (a table: id | chunk / note | claim | status |
   how / next step), "Glossary proposals", "Latin doubts", "DR quotations" (one reference per line).
"""


def scaffold(n):
    f = f'chunks/dialogus/wyc-dialogus-{n}.md'
    first = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%h', '--', f], cwd=ROOT,
                           capture_output=True, text=True).stdout.split()[-1]
    return subprocess.run(['git', 'show', f'{first}:{f}'], cwd=ROOT, capture_output=True, text=True).stdout


def section(text, head):
    m = re.search(rf'^## {re.escape(head)}.*?$(.*?)(?=^## |\Z)', text, re.M | re.S)
    return m.group(0).strip() if m else ''


def request_text(n):
    scaf = scaffold(n)
    current = open(os.path.join(ROOT, f'chunks/dialogus/wyc-dialogus-{n}.md')).read()
    # Latin: the scaffold's Latin blocks were plate-corrected later; use the current established Latin.
    cur_la = [p for p in current.split('\n\n') if p.startswith('>')]
    parts = [p for p in scaf.split('\n\n')]
    i = 0
    for k, p in enumerate(parts):
        if p.startswith('>') and i < len(cur_la):
            parts[k] = cur_la[i]; i += 1
    scaf = '\n\n'.join(parts)
    scaf = re.sub(r'^## Pollard.s side-notes.*?(?=^## |\Z)', section(current, "Pollard's side-notes") + '\n\n', scaf, flags=re.M | re.S)
    scaf = re.sub(r'^## Transcription notes.*?(?=^## |\Z)', section(current, 'Transcription notes') + '\n\n', scaf, flags=re.M | re.S)
    if 'Transcription notes' not in scaf:
        scaf += '\n\n' + section(current, 'Transcription notes')
    pages = re.search(r'pages: "(\d+)\.\d+–(\d+)\.\d+"', current)
    app = json.load(open(APPARATUS))
    apparatus = '\n\n'.join(f'p. {p}:\n{app.get(str(p), "").strip()}' for p in range(int(pages.group(1)), int(pages.group(2)) + 1))
    return (f'Translate this chunk.\n\n<scaffold>\n{scaf.strip()}\n</scaffold>\n\n'
            f'<apparatus note="Pollard\'s page-foot apparatus, OCR; line numbers refer to the printed page">\n{apparatus}\n</apparatus>')


def main(ns):
    os.makedirs(OUT, exist_ok=True)
    system = [{'type': 'text', 'text': PREAMBLE + '\n\n<card>\n' + open(os.path.join(ROOT, 'chunks/dialogus/CARD.md')).read()
               + '\n</card>\n\n<glossary>\n' + open(os.path.join(ROOT, 'GLOSSARY.md')).read() + '\n</glossary>',
               'cache_control': {'type': 'ephemeral'}}]
    client = anthropic.Anthropic()
    for n in ns:
        t0 = time.time()
        with client.beta.messages.stream(
            model=MODEL, max_tokens=64000, system=system,
            output_config={'effort': EFFORT},
            betas=['server-side-fallback-2026-07-01'], fallbacks='default',
            messages=[{'role': 'user', 'content': request_text(n)}],
        ) as stream:
            msg = stream.get_final_message()
        if msg.stop_reason != 'end_turn':
            print(f'{n}: stop_reason={msg.stop_reason}', getattr(msg, 'stop_details', None))
        text = ''.join(b.text for b in msg.content if b.type == 'text')
        open(os.path.join(OUT, f'wyc-dialogus-{n}.api.md'), 'w').write(text)
        u = msg.usage
        row = dict(chunk=n, model=msg.model, effort=EFFORT, seconds=round(time.time() - t0),
                   input=u.input_tokens, cache_write=u.cache_creation_input_tokens or 0,
                   cache_read=u.cache_read_input_tokens or 0, output=u.output_tokens, stop=msg.stop_reason)
        row['dollars'] = round((row['input'] * PRICE['in'] + row['cache_write'] * PRICE['cache_write'] +
                                row['cache_read'] * PRICE['cache_read'] + row['output'] * PRICE['out']) / 1e6, 3)
        row['total_tokens'] = row['input'] + row['cache_write'] + row['cache_read'] + row['output']
        open(os.path.join(OUT, 'usage.jsonl'), 'a').write(json.dumps(row) + '\n')
        print(json.dumps(row))


if __name__ == '__main__':
    main(sys.argv[1:])
