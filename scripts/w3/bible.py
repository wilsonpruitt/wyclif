"""Look up a verse in the Clementine Vulgate and the Douay–Rheims (Challoner) (CONVENTIONS §10).

    python3 scripts/w3/bible.py "John 14:6" ["Ps 108:28" ...]
    python3 scripts/w3/bible.py --find "maledicent illi"      (search the Vulgate text)

Texts: ~/douay-glossa/raw/{VulgClementine,DRC}.json (scrollmapper; book names in the English
Protestant form, e.g. "I Samuel", "Psalms", "Sirach"). ⚠ Check the psalm numbering on each lookup:
Wyclif cites the Vulgate numbering (Ps 108 = Hebrew 109); print both neighbours when in doubt.
"""
import json, os, re, sys

RAW = os.path.expanduser('~/douay-glossa/raw')
ALIAS = {'ps': 'Psalms', 'psalm': 'Psalms', 'prov': 'Proverbs', 'eccl': 'Ecclesiastes', 'eccles': 'Ecclesiastes',
         'ecclus': 'Sirach', 'ecclesiasticus': 'Sirach', 'sir': 'Sirach', 'cant': 'Song of Solomon',
         'isa': 'Isaiah', 'is': 'Isaiah', 'jer': 'Jeremiah', 'ezek': 'Ezekiel', 'dan': 'Daniel', 'mal': 'Malachi',
         'matt': 'Matthew', 'mt': 'Matthew', 'mk': 'Mark', 'lk': 'Luke', 'jn': 'John', 'rom': 'Romans',
         'gal': 'Galatians', 'eph': 'Ephesians', 'phil': 'Philippians', 'col': 'Colossians', 'heb': 'Hebrews',
         'jas': 'James', 'rev': 'Revelation of John', 'apoc': 'Revelation of John', 'gen': 'Genesis',
         'exod': 'Exodus', 'ex': 'Exodus', 'lev': 'Leviticus', 'num': 'Numbers', 'deut': 'Deuteronomy',
         'josh': 'Joshua', 'judg': 'Judges', 'tit': 'Titus', 'wisd': 'Wisdom', 'hos': 'Hosea', 'mic': 'Micah'}
ORD = {'1': 'I', '2': 'II', '3': 'III', 'i': 'I', 'ii': 'II', 'iii': 'III'}
# Vulgate/Douay names for the books of Kings: 1-2 Kings = 1-2 Samuel, 3-4 Kings = 1-2 Kings
KINGS = {'1 reg': 'I Samuel', '2 reg': 'II Samuel', '3 reg': 'I Kings', '4 reg': 'II Kings',
         '1 kings': 'I Samuel', '2 kings': 'II Samuel', '3 kings': 'I Kings', '4 kings': 'II Kings'}


def load(name):
    return {b['name']: {c['chapter']: {v['verse']: v['text'] for v in c['verses']} for c in b['chapters']}
            for b in json.load(open(f'{RAW}/{name}.json'))['books']}


def book(s, books):
    s = s.strip().rstrip('.').lower()
    if s in KINGS:
        return KINGS[s]
    m = re.match(r'^(i{1,3}|[123])\s*(.*)$', s)
    pre, rest = (ORD[m.group(1)] + ' ', m.group(2)) if m and m.group(2) else ('', s)
    rest = ALIAS.get(rest, rest)
    for b in books:
        if b.lower() == (pre + rest).lower() or b.lower().startswith((pre + rest).lower()):
            return b
    raise SystemExit(f'unknown book: {s}')


def main(args):
    V, D = load('VulgClementine'), load('DRC')
    if args and args[0] == '--find':
        q = ' '.join(args[1:]).lower()
        for b, chs in V.items():
            for c, vs in chs.items():
                for n, t in vs.items():
                    if q in t.lower():
                        print(f'{b} {c}:{n}  {t}')
        return
    for ref in args:
        m = re.match(r'^(.*?)\s+(\d+):(\d+)(?:[-–](\d+))?$', ref.strip())
        if not m:
            raise SystemExit(f'bad reference: {ref}')
        b = book(m.group(1), V)
        c, v1, v2 = int(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3))
        for v in range(v1, v2 + 1):
            print(f'{b} {c}:{v}')
            print('  VULG ', V.get(b, {}).get(c, {}).get(v, '—'))
            print('  DR   ', D.get(b, {}).get(c, {}).get(v, '—'))


if __name__ == '__main__':
    main(sys.argv[1:])
