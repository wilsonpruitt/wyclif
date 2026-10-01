"""From scars.tsv to (a) OVERRIDE decisions for the rule fixes and (b) a plate queue for the rest.

    .venv/bin/python scripts/w3/scarqueue.py SLUG
      -> text/<slug>/plate_decisions.part97.tsv   OVERRIDE-SCAR rows (S-* rules, W1, W-split), ready to merge
      -> text/<slug>/scar_queue.tsv               the plate_queue.tsv format, for crops.py --queue
Then: crops.py SLUG --queue scar_queue.tsv --out crops_scars; a plate agent reads the sheets; scarmerge.py.

Classes applied without the plates: every S-* except S-split; W1; and W-split = an S-split (or a non-word)
whose two words stand side by side on the same leaf in a full scan (the scans divide what our pivot glued).
Everything else (LEFT-*, W2, an unconfirmed S-split) goes to the plates. Rows at a position already read on
the plate are left alone. A row is applied by the vote only if its `forms` match the position's voted forms,
which come from pNNN.check.tsv; a position with no check row (a unanimous real word) cannot take a decision
and is listed as `nosig` for the coordinator.
"""
import csv, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from vote import norm  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FULL = ['iohanniswycliftr00wycluoft', 'tractatusdeeccle00wycl']      # the full independent scans
PIVOT = 'latinworks10wycl'
RULE_OK = {'S-glyph', 'S-pct', 'S-num', 'S-deg', 'S-quote', 'S-amp', 'S-dot', 'S-caps', 'S-alinea', 'S-eng',
           'S-J', 'S-edge', 'W1'}


def main(slug):
    base = f'{ROOT}/text/{slug}'
    off = int({r['slug']: r for r in csv.DictReader(open(f'{ROOT}/catalog/plate_offsets.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE)}[slug]['offset'])
    rows = list(csv.DictReader(open(f'{base}/scars.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE))
    sigs = {}
    for r in rows:
        pg = int(r['page'])
        if pg not in sigs:
            sigs[pg] = {}
            p = f'{base}/p{pg:03d}.check.tsv'
            if os.path.exists(p):
                for c in csv.DictReader(open(p), delimiter='\t', quoting=csv.QUOTE_NONE):
                    sigs[pg].setdefault(int(c['pos']), c['forms'])
    piv = {}                                    # (leaf, line) -> pivot tokens
    for l in open(f'{base}/witnesses/{PIVOT}.jsonl'):
        t = json.loads(l)
        piv.setdefault((t['leaf'], t['line']), []).append(t)
    pairs = {}                                  # page -> adjacent word pairs on that page in a full scan
    for w in FULL:
        # the scan's own leaf offset: the commonest leaf - page in its completeness report
        offs = {}
        for c in csv.DictReader(open(f'{base}/complete.{w}.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
            d = int(c['leaf']) - int(c['page']); offs[d] = offs.get(d, 0) + 1
        ow = max(offs, key=offs.get)
        toks = [json.loads(l) for l in open(f'{base}/witnesses/{w}.jsonl')]
        for a, b in zip(toks, toks[1:]):
            for pg in (a['leaf'] - ow - 1, a['leaf'] - ow, a['leaf'] - ow + 1):     # a page's text can run onto the next leaf
                pairs.setdefault(pg, set()).add((norm(a['t']), norm(b['t'])))
    dec, queue, nosig, cls = [], [], [], {}
    for r in rows:
        c = r['cls']
        if c in ('PRINT', 'FREQ') or r['plate_read']:
            continue
        if r['pos'] in ('', 'None'):
            nosig.append(r); continue
        pg, pos = int(r['page']), int(r['pos'])
        sig = sigs.get(pg, {}).get(pos)
        core = re.sub(r'^[(\[*]+|[.,;:?!)\]*]+$', '', r['printed'])
        trail = r['printed'][len(r['printed'].rstrip('.,;:?!)]*')):]
        if c == 'S-split' or c.startswith('LEFT'):
            low = core.lower()
            for k in range(2, len(low) - 1):
                if (low[:k], low[k:]) in pairs.get(pg, ()):
                    r = dict(r, cls='W-split', proposed=(core[:k] + ' ' + core[k:] + trail))
                    c = 'W-split'
                    break
        cls[c] = cls.get(c, 0) + 1
        if c in RULE_OK or c == 'W-split':
            if not sig:
                nosig.append(r); continue
            dec.append(dict(page=pg, pos=pos, rule='OVERRIDE-SCAR', forms=sig, reading=r['proposed'],
                            note=f"{c}: {r['printed']} -> {r['proposed']} ({r['evidence'][:80]})"))
        else:
            leaf, line = pg + off, int(r['line']) - 1 if r['line'] else 0
            toks = piv.get((leaf, line), [])
            pf = sig.split(' | ')[0].split('=', 1)[1] if sig else ''
            t = next((t for t in toks if norm(t['t']) == pf), toks[0] if toks else None)
            if not t:
                nosig.append(r); continue
            queue.append(dict(page=pg, pos=pos, rule=c, forms=sig or f"{PIVOT}={pf}", leaf=leaf,
                              box=','.join(map(str, t['box'])), printed=r['printed'], proposed=r['proposed']))
    with open(f'{base}/plate_decisions.part97.tsv', 'w') as f:
        f.write('page\tpos\trule\tforms\treading\tnote\n')
        for d in dec:
            f.write('\t'.join(str(d[k]) for k in ('page', 'pos', 'rule', 'forms', 'reading', 'note')) + '\n')
    with open(f'{base}/scar_queue.tsv', 'w') as f:
        f.write('page\tpos\trule\tforms\tleaf\tbox\tprinted\tproposed\n')
        for q in queue:
            f.write('\t'.join(str(q[k]) for k in ('page', 'pos', 'rule', 'forms', 'leaf', 'box', 'printed', 'proposed')) + '\n')
    print(f'{len(dec)} OVERRIDE-SCAR rows -> plate_decisions.part97.tsv; {len(queue)} plate items -> scar_queue.tsv; '
          f'{len(nosig)} without a voted position (nosig)')
    print('  by class:', ', '.join(f'{k} {v}' for k, v in sorted(cls.items())))
    for r in nosig[:40]:
        print(f"  nosig {r['page']}.{r['line']} {r['cls']} {r['printed']} -> {r['proposed']}")


if __name__ == '__main__':
    main(sys.argv[1])
