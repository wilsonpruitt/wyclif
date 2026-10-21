"""Fetch the primary scan's page images for a page range (for the B+ transcription, WORKFLOW stage 2B).

    .venv/bin/python scripts/w3/fetchleaves.py SLUG FIRST LAST

Saves text/<slug>/raw/leaves/nLLLL.jpg (leaf = page + offset, catalog/plate_offsets.tsv), the cache crops.py
uses; a file already there is kept.
"""
import csv, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from crops import leaf_image, ROOT   # noqa: E402


def main(slug, first, last):
    off = {r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t')}[slug]
    for pg in range(int(first), int(last) + 1):
        leaf_image(slug, off['item'], pg + int(off['offset']))
    print(f'pages {first}–{last} → text/{slug}/raw/leaves/')


if __name__ == '__main__':
    main(*sys.argv[1:4])
