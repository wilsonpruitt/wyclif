"""Build a single-pass translation brief for a batch of chunk scaffolds (PLAN § Cost, 2026-09-29).

    .venv/bin/python scripts/w3/brief.py SLUG NN [NN ...]      e.g.  brief.py ecclesia 01 02 03
    (--from-git-scaffold: brief a chunk's first committed scaffold, to re-pilot a translated chunk)

Why: the translation cost is the agent LOOP (every turn re-sends the growing context), not the reading.
So the agent gets everything in ONE file and writes each chunk once. The brief holds: the working
instructions, the volume's CARD.md, only the GLOSSARY rows whose Latin occurs in the batch, and per chunk
its scaffold plus the editor's page-foot apparatus for its pages (text/<slug>/apparatus.json, from
witness.py) and his italic runs (text/<slug>/italics.tsv, from italics.py). Output: chunks/<slug>/_briefs/<slug>-NN-NN.md, and the agent prompt to paste is printed.
"""
import csv, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

INSTRUCTIONS = """# Translation brief: {label}

You translate these {n} chunk(s) of Wyclif's *{work}* in a single pass. Everything you need is in this file:
the working card, the glossary rows these chunks use, and for each chunk its scaffold and the editor's
apparatus for its pages. Work so as to use few tool calls:

1. Read this brief once (it is the only file you need to read, unless the card names one for your chunk).
2. For each chunk, write the COMPLETE chunk file ONCE with the Write tool to its path (given in the chunk's
   header below): the scaffold with `status: translated`, the title, the English after every Latin block,
   headings and side-notes as the card says, Notes, and Transcription notes, in the card's
   layout. Never alter the Latin. Do not make a series of small edits.
3. Use the apparatus given here for variants (the card's rule: a variant that gives the sense is translated
   with a T note citing the siglum; otherwise translate the print and flag it). Open a plate image only if a
   word cannot be construed at all from the print plus the apparatus; otherwise flag it as a Latin doubt.
4. Scripture: quote the Douay-Rheims as you know it. At the END, check every reference you quoted in ONE
   command: `cd {root} && .venv/bin/python scripts/w3/bible.py "Ref 1" "Ref 2" ...` and fix any wording
   that differs, in the same chunk file (this is the one allowed round of edits).
5. Run `cd {root} && .venv/bin/python scripts/w3/lint.py {paths}` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.

Standing rules (from the *De ecclesia* briefs, 2026-10-02):
- Do NOT search the Patrologia or other sources; a separate checker verifies them afterwards. Give the
  editor's reference, the modern form in the English, and "to be checked" with a fresh LEDGER id per item
  (never reuse an id).
- Notes open with their bold class codes, `**S/C.**`, never bare letters mid-note. No process words in
  the notes ("the report", "the coordinator", "brief").
- OCR scars (stray English or margin letters, line numbers read as words, glued or broken words,
  numerals read as letters) stay out of the chunk: translate the print's word and list each scar in your
  final message only (page.line, token, likely print reading). The coordinator fixes the Latin.
- Flag every place the established Latin may have LOST a word (it does not construe, especially at a page
  head or foot) or DOUBLED one: page.line and the suspicion. Translate the print as it stands; supply a
  missing word only in brackets with a T note. The editor's print governs; list any departure.
"""


def glossary_rows(latin):
    """GLOSSARY rows (with their section headings) whose Latin forms occur in the batch's Latin."""
    lat = latin.lower().replace('j', 'i').replace('v', 'u')
    out, section_head, header_done = [], None, False
    lines = open(os.path.join(ROOT, 'GLOSSARY.md')).read().split('\n')
    head = []
    for l in lines:                                     # keep the glossary's own preamble (the rules)
        if l.startswith('## '):
            break
        head.append(l)
    kept = 0
    for l in lines:
        if l.startswith('## '):
            section_head = l; header_done = False; continue
        if not l.startswith('| ') or l.startswith('| Latin') or l.startswith('|---'):
            continue
        cell = re.sub(r'\(.*?\)', '', l.split('|')[1].lower())
        forms = [re.sub(r'[^a-z ]', '', f).strip() for f in re.split(r'[;/,]', cell)]
        stems = [f.split()[0][:5].replace('j', 'i').replace('v', 'u') for f in forms if f]
        if any(s and s in lat for s in stems):
            if not header_done:
                out += ['', section_head, '', '| Latin | English | Note |', '|---|---|---|']; header_done = True
            out.append(l); kept += 1
    return '\n'.join(head).strip() + '\n' + '\n'.join(out), kept


def main(slug, nums):
    card = os.path.join(ROOT, 'chunks', slug, 'CARD.md')
    if not os.path.exists(card):
        sys.exit(f'no {card}: write the volume card first (from the first-chunk review), then brief')
    off = {r['slug']: r for r in csv.DictReader(open(os.path.join(ROOT, 'catalog', 'plate_offsets.tsv')), delimiter='\t')}
    offset = int(off[slug]['offset']) if slug in off else None
    app_path = os.path.join(ROOT, 'text', slug, 'apparatus.json')
    app = json.load(open(app_path)) if os.path.exists(app_path) else {}
    it_path = os.path.join(ROOT, 'text', slug, 'italics.tsv')      # the editor's italic runs (italics.py)
    italics = {}
    if os.path.exists(it_path):
        for r in csv.DictReader(open(it_path), delimiter='\t', quoting=csv.QUOTE_NONE):
            italics.setdefault(int(r['page']), []).append(r['text'])
    chunks, latin, paths = [], [], []
    for n in nums:
        rel = f'chunks/{slug}/wyc-{slug}-{n}.md'
        text = open(os.path.join(ROOT, rel)).read()
        if FROM_GIT:                                    # test/re-pilot: the chunk's first committed scaffold
            first = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%h', '--', rel], cwd=ROOT,
                                   capture_output=True, text=True).stdout.split()[-1]
            text = subprocess.run(['git', 'show', f'{first}:{rel}'], cwd=ROOT, capture_output=True, text=True).stdout
        if 'status: translated' in text:
            sys.exit(f'{rel} is already translated; brief only scaffolds')
        latin.append(' '.join(l for l in text.split('\n') if l.startswith('>')))
        m = re.search(r'pages: "(\d+)\.\d+[–-](\d+)\.\d+"', text)
        pages = range(int(m.group(1)), int(m.group(2)) + 1) if m else []
        a = '\n\n'.join(f'p. {p}:\n{app.get(str(p + offset), "(none)").strip()}' for p in pages) if offset is not None and app else \
            '(no apparatus extracted for this volume: run witness.py, which now saves it)'
        dest = os.path.join(ROOT, 'chunks', slug, '_pilot', 'brief-test', os.path.basename(rel)) if FROM_GIT else os.path.join(ROOT, rel)
        it = '\n'.join(f'p. {p}: ' + ' | '.join(italics[p]) for p in pages if p in italics) or '(none recorded)'
        chunks.append(f'\n\n---\n\n## Chunk {n}: write to `{dest}`\n\n### Scaffold\n\n````markdown\n{text.strip()}\n````\n\n'
                      f'### Apparatus (editor\'s page-foot notes, OCR; line numbers are the printed page\'s)\n\n```\n{a}\n```\n\n'
                      f'### Italics (the editor\'s italic runs, OCR, one per |: his quotation bounds, evidence only)\n\n```\n{it}\n```')
        paths.append(os.path.relpath(dest, ROOT))
    gl, kept = glossary_rows(' '.join(latin))
    work = re.search(r'^work_la:\s*(.+)$', chunks[0], re.M).group(1).strip()
    if FROM_GIT:
        os.makedirs(os.path.join(ROOT, 'chunks', slug, '_pilot', 'brief-test'), exist_ok=True)
    label = f'{slug} {nums[0]}' + (f'–{nums[-1]}' if len(nums) > 1 else '')
    body = (INSTRUCTIONS.format(label=label, n=len(nums), work=work, root=ROOT, paths=' '.join(paths)) +
            '\n\n## The working card\n\n' + open(card).read().strip() +
            f'\n\n## Glossary (the {kept} rows these chunks use; the full file is GLOSSARY.md)\n\n' + gl + ''.join(chunks) + '\n')
    os.makedirs(os.path.join(ROOT, 'chunks', slug, '_briefs'), exist_ok=True)
    out = os.path.join(ROOT, 'chunks', slug, '_briefs', f'{slug}-{nums[0]}-{nums[-1]}.md')
    open(out, 'w').write(body)
    print(f'{out}\n  ~{len(body) // 4 // 1000}k tokens; glossary rows {kept}; chunks {", ".join(nums)}')
    print(f'\nAgent prompt:\n  Read {out} and follow it exactly. It is your input; read another file only where it says so.')


FROM_GIT = '--from-git-scaffold' in sys.argv

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) < 2:
        sys.exit(__doc__)
    main(args[0], args[1:])
