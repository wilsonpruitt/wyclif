"""Refresh the Latin of UNTRANSLATED scaffolds from the current established text, touching nothing else.

    .venv/bin/python scripts/w3/relatin.py SLUG [--dry]

Why (2026-10-01): after the scar pass changed pNNN.la.txt, the scaffolds still held the old Latin. chapters.py
--force would rebuild every scaffold and lose what was added since (the side-note splice, hand fixes). So: build
fresh scaffolds into a scratch copy of chunks/<slug>/, and for each existing chunk whose front matter says
`status: draft`, replace only its `> ` Latin lines, paragraph by paragraph, keyed on the `## ¶k · range` heading.
A chunk whose headings differ from the fresh build is left alone and reported. Translated chunks are never touched.
"""
import glob, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HEAD = re.compile(r'^## ¶\d+ · ')


def blocks(text):
    """heading -> list of its `> ` Latin lines, in order."""
    out, cur = {}, None
    for l in text.split('\n'):
        if HEAD.match(l):
            cur = l; out[cur] = []
        elif l.startswith('## '):
            cur = None
        elif cur and l.startswith('> '):
            out[cur].append(l)
    return out


def main(slug, dry=False):
    live = f'{ROOT}/chunks/{slug}'
    tmp = tempfile.mkdtemp(prefix='relatin-')
    keep = f'{tmp}/keep'
    shutil.copytree(live, keep)                    # the live chunks, restored below whatever happens
    try:
        subprocess.run([sys.executable, f'{ROOT}/scripts/w3/chapters.py', slug, '--force'], check=True,
                       stdout=subprocess.DEVNULL)
        fresh = {os.path.basename(p): open(p).read() for p in glob.glob(f'{live}/wyc-{slug}-*.md')}
    finally:
        shutil.rmtree(live)
        shutil.copytree(keep, live)
    changed, skipped, same = [], [], 0
    for p in sorted(glob.glob(f'{live}/wyc-{slug}-*.md')):
        name = os.path.basename(p)
        old = open(p).read()
        if not re.search(r'^status: draft$', old, re.M) or name not in fresh:
            continue
        ob, nb = blocks(old), blocks(fresh[name])
        if list(ob) != list(nb) or any(len(ob[h]) != len(nb[h]) for h in ob):
            skipped.append(name); continue
        new = old
        for h in ob:
            for a, b in zip(ob[h], nb[h]):
                if a != b:
                    new = new.replace(a, b, 1)
        if new != old:
            changed.append(name)
            if not dry:
                open(p, 'w').write(new)
        else:
            same += 1
    shutil.rmtree(tmp)
    print(f'{len(changed)} draft chunks refreshed{" (dry run)" if dry else ""}, {same} unchanged, '
          f'{len(skipped)} skipped (headings differ): {" ".join(skipped)}')


if __name__ == '__main__':
    main(sys.argv[1], '--dry' in sys.argv)
