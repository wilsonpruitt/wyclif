"""Delete the star-emoji (U+2B50) markers from text files in the repo.

    python3 scripts/strip_stars.py                    dry run over the whole repo: counts and context, changes nothing
    python3 scripts/strip_stars.py --apply            rewrite the files
    python3 scripts/strip_stars.py PATH [PATH …]      limit to files or directories (relative to the repo root)
    python3 scripts/strip_stars.py --skip-briefs      leave the generated briefs (chunks/*/_briefs) alone

Removes the star, its variation selector (U+FE0F) and the one space after it, so "## 5. <star> Daggers" becomes
"## 5. Daggers" and "**G.** <star> *Prescitus*" becomes "**G.** *Prescitus*". Nothing else in a line is touched.
Text files only (.md .txt .tsv .json .py .html .css .js); .git, .venv, node_modules and site/dist are skipped
(the site build never publishes a star, see scrub() in site/build.py). Undo with git.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EXT = ('.md', '.txt', '.tsv', '.json', '.py', '.html', '.css', '.js')
SKIP_DIRS = {'.git', '.venv', 'node_modules', 'dist', '__pycache__'}
STAR = re.compile('\u2b50\ufe0f? ?')                       # written as escapes so this file never matches itself


def files(paths, skip_briefs):
    for p in paths:
        p = os.path.join(ROOT, p)
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, fs in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not (skip_briefs and d == '_briefs')]
            for f in fs:
                if f.endswith(EXT):
                    yield os.path.join(root, f)


def main():
    args = sys.argv[1:]
    apply_, skip_briefs = '--apply' in args, '--skip-briefs' in args
    paths = [a for a in args if not a.startswith('--')] or ['.']
    total = changed = 0
    for f in sorted(set(files(paths, skip_briefs))):
        try:
            s = open(f, encoding='utf-8').read()
        except (UnicodeDecodeError, OSError):
            continue
        n = len(STAR.findall(s))
        if not n:
            continue
        total += n; changed += 1
        rel = os.path.relpath(f, ROOT)
        if apply_:
            open(f, 'w', encoding='utf-8').write(STAR.sub('', s))
            print(f'{n:4d}  {rel}')
        else:
            ctx = next(l.strip() for l in s.splitlines() if '\u2b50' in l)
            print(f'{n:4d}  {rel}   e.g. {ctx[:90]}')
    print(f'\n{total} star(s) in {changed} file(s)' + (' removed.' if apply_ else ' (dry run: nothing changed; add --apply).'))


if __name__ == '__main__':
    main()
