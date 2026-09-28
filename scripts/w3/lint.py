"""Lint translation chunks against CONVENTIONS §§2, 3, 11, 14.

    .venv/bin/python scripts/w3/lint.py [FILES...]      (default: pilots/*.md chunks/*.md)

Fails (exit 1) on: missing/empty required front matter; `latin_source` not one of
three-witness / plate-read; a three-witness chunk without `witnesses`/`check`;
unanchored notes, notes without definitions, or numbering that is not 1..n in order;
a `{g:key}` tag with no GLOSSARY row; an open `[verify]` in a chunk whose status is
done/publish; plate-pending marks (⟦ ⟧) or stray folio asterisks in the Latin.
"""
import glob, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REQUIRED = ['chunk_id', 'work_la', 'work_en', 'volume_slug', 'editor', 'year', 'pages', 'latin_source', 'status']


def glossary_keys():
    keys = set()
    for line in open(f'{ROOT}/GLOSSARY.md'):
        if line.startswith('| ') and not line.startswith('| Latin') and not line.startswith('|---'):
            cell = line.split('|')[1]
            for form in re.split(r'[;/,]', cell):
                form = re.sub(r'\(.*?\)', '', form).strip().lower()
                form = re.sub(r'[^a-z ]', '', form).strip()
                if form:
                    keys.add(form.replace(' ', '-'))
                    keys.add(form.split()[0])
    return keys


def lint(path, gkeys):
    errs = []
    s = open(path).read()
    m = re.match(r'---\n(.*?)\n---\n', s, re.S)
    if not m:
        return [f'{path}: no front matter']
    fm = dict(re.findall(r'^(\w+):\s*(.*)$', m.group(1), re.M))
    for k in REQUIRED:
        if not fm.get(k, '').strip().strip('"'):
            errs.append(f'front matter: `{k}` missing or empty')
    src = fm.get('latin_source', '').strip()
    if src not in ('three-witness', 'plate-read', 'fordham-collated'):
        errs.append(f'latin_source `{src}` is not three-witness / plate-read')
    if src == 'three-witness':
        for k in ('witnesses', 'check', 'italics'):
            if not fm.get(k, '').strip():
                errs.append(f'three-witness chunk without `{k}`')
    body = s[m.end():]
    notes_at = body.find('\n## Notes')
    text = body[:notes_at] if notes_at >= 0 else body
    notes = body[notes_at:] if notes_at >= 0 else ''
    markers = re.findall(r'\[\^(\d+)\](?!:)', text)
    defs = re.findall(r'^\[\^(\d+)\]:', notes, re.M)
    if [int(x) for x in dict.fromkeys(markers)] != list(range(1, len(set(markers)) + 1)):
        errs.append('note markers are not numbered 1..n in order of appearance')
    for n in set(markers) - set(defs):
        errs.append(f'note [^{n}] has no definition')
    for n in set(defs) - set(markers):
        errs.append(f'note [^{n}] is defined but not anchored in the text')
    for k in re.findall(r'\{g:([a-z-]+)\}', text):
        if k not in gkeys and k.split('-')[0] not in gkeys:
            errs.append(f'glossary tag {{g:{k}}} has no GLOSSARY row')
    if fm.get('status', '').strip().split()[0:1] in (['done'], ['publish']) and '[verify' in s:
        errs.append('status is done/publish but a [verify] is open')
    latin = '\n'.join(l for l in text.splitlines() if l.startswith('>'))
    if '⟦' in latin or '⟧' in latin:
        errs.append('Latin still carries plate-pending marks ⟦ ⟧')
    if re.search(r'(^|\s)\*(\s|$)', latin.replace('> ', ' ')):     # a folio mark stands alone
        errs.append('stray asterisk in the Latin (folio marker?)')
    return [f'{os.path.relpath(path, ROOT)}: {e}' for e in errs]


def main(files):
    files = files or sorted(glob.glob(f'{ROOT}/pilots/*.md') + glob.glob(f'{ROOT}/chunks/*.md'))
    gkeys = glossary_keys()
    errs = [e for f in files for e in lint(f, gkeys)]
    for e in errs:
        print('LINT', e)
    print(f'{len(files)} chunk(s), {len(errs)} problem(s)')
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
