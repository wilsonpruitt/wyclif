"""Parse an archive.org _djvu.xml into per-leaf layout, and split each leaf into
main text / margin (side-notes, line numbers, folio marks) / heads / apparatus.

Coordinates in djvu.xml are "left,bottom,right,top" with y growing downward
(bottom > top). Leaf index = order of <OBJECT> (0-based) = archive.org /page/nNN.

Classification is geometric, per leaf, and deliberately simple:
  * main column  = the widest contiguous band of x covered by words
                   (the gutter to the side-note column has ~zero coverage);
  * margin       = words whose x-centre lies outside that band;
  * apparatus    = lines below the main block set in a smaller type;
  * head         = a first line standing apart from the block (running title,
                   page number), or a centred short line with space around it
                   (chapter heading: kept, flagged as a heading).
"""
import re
import statistics as st
import xml.etree.ElementTree as ET

NUM_PREFIX = re.compile(r'^(?:10|1[oO0]|[iIl][oO0]|15|[iIl][5S]|20|2[oO0]|25|2[5S]|30|3[oO0]|35|3[5S]|5)(?=[A-Za-z])')   # line nos glued at left: 5, io, i5, 2o...
NUM_SUFFIX = re.compile(r'(?<=[a-z.,;:])(?:10|1[oO0]|[iIl][oO0]|15|[iI][5S]|20|2[oO0]|25|30|3[oO0]|35|5|[A-D])$')   # line no. or alinea letter glued at right
PURE_NUM = re.compile(r'^[0-9IiloOS.,*]{1,4}$')


def parse(path):
    """Yield leaves: dict(leaf, w, h, lines=[[ (text, l, t, r, b, conf), ...], ...])."""
    leaf = -1
    for ev, el in ET.iterparse(path, events=('end',)):
        if el.tag != 'OBJECT':
            continue
        leaf += 1
        lines = []
        for ln in el.iter('LINE'):
            words = []
            for w in ln.iter('WORD'):
                txt = (w.text or '').strip()
                if not txt:
                    continue
                l, b, r, t = (int(v) for v in w.get('coords').split(',')[:4])
                words.append((txt, l, t, r, b, int(w.get('x-confidence', 0) or 0)))
            if words:
                lines.append(words)
        yield dict(leaf=leaf, w=int(el.get('width')), h=int(el.get('height')), lines=lines)
        el.clear()


def _peak(vals, lo, hi, bin_=15):
    """Centre of the most populated bin of vals within [lo, hi)."""
    c = {}
    for v in vals:
        if lo <= v < hi:
            c[v // bin_] = c.get(v // bin_, 0) + 1
    if not c:
        return None
    k = max(c, key=lambda k: (c[k], -abs(k)))
    return k * bin_ + bin_ // 2


def right_edge(leaf):
    """The justified right margin of the main text: the sharpest peak of word
    right-edges in the page's right 60% (side-notes are ragged-right)."""
    return _peak([w[3] for ln in leaf['lines'] for w in ln], int(leaf['w'] * 0.4), leaf['w'])


def line_start_width(leaf):
    """R minus the modal line start: equals the text measure on pages whose
    side-notes are on the right, and is larger on pages with left side-notes."""
    R = right_edge(leaf)
    if R is None or len(leaf['lines']) < 12:
        return None
    L0 = _peak([ln[0][1] for ln in leaf['lines'] if len(ln) >= 4], 0, R)
    return R - L0 if L0 is not None else None


def res_class(leaf):
    """Resolution class of a leaf (scans can mix resolutions, e.g. Google's)."""
    import math
    return round(math.log(max(leaf['w'], 1), 1.3))


def measure(leaves):
    """Text measure per resolution class: {class: W}. The lower cluster of
    per-page widths (pages whose side-notes are on the right)."""
    by = {}
    for lf in leaves:
        x = line_start_width(lf)
        if x and x > 0:
            by.setdefault(res_class(lf), []).append(x)
    out = {}
    for k, ws in by.items():
        ws.sort()
        out[k] = st.median(ws[: max(1, len(ws) // 3)])
    return out


def regroup(lines):
    """Rebuild lines from word geometry: OCR engines can emit regions out of reading
    order and overlap them (duplicate lines). Cluster words by baseline, sort by x,
    drop near-duplicate boxes."""
    words = sorted((w for ln in lines for w in ln), key=lambda w: w[4])
    if not words:
        return []
    h = st.median([w[4] - w[2] for w in words]) or 1
    rows, cur, base = [], [], None
    for w in words:
        if base is not None and w[4] - base > 0.5 * h:
            rows.append(cur); cur = []
        cur.append(w)
        base = st.median([x[4] for x in cur])
    rows.append(cur)
    out = []
    for r in rows:
        r.sort(key=lambda w: w[1])
        keep = []
        for w in r:
            if keep:
                k = keep[-1]
                ov = min(k[3], w[3]) - max(k[1], w[1])
                if ov > 0.6 * min(k[3] - k[1], w[3] - w[1]):     # duplicate from overlapping regions
                    if len(w[0]) > len(k[0]):
                        keep[-1] = w
                    continue
            keep.append(w)
        out.append(keep)
    return out


def split_leaf(leaf, W):
    """Split a leaf given the scan's text measure W.
    Returns dict(main=[line words...], margin=[...], heads=[...], apparatus=[...], band=(L,R))."""
    if isinstance(W, dict):
        W = W.get(res_class(leaf)) or (max(W.values()) if W else None)
    R = right_edge(leaf)
    if R is None or W is None:
        return dict(main=[], margin=[], heads=[], apparatus=[], band=(0, 0))
    L = R - W
    tol = int(0.012 * leaf['w'])
    rows = []
    for ln in regroup(leaf['lines']):
        main, marg = [], []
        for w in ln:
            cx = (w[1] + w[3]) / 2
            # rescue a main word glued to the first side-note word at the RIGHT edge
            # ("adexamPle-"); left-edge boxes are often just inflated to the next word
            glued_right = w[1] <= R - 0.012 * leaf['w'] < R < w[3]
            inside = L - tol <= cx <= R + tol or glued_right
            (main if inside else marg).append(w)
        if main or marg:
            rows.append((main, marg))
    # small-type rows inside the band are side-note overflow or marks, not text
    body_h0 = st.median([st.median([w[4] - w[2] for w in m]) for m, _ in rows if len(m) >= 4] or [1])
    clean = []
    for m, g in rows:
        alpha = sum(ch.isalpha() for w in m for ch in w[0])
        hm = st.median([w[4] - w[2] for w in m]) if m else 0
        at_edge = bool(m) and abs(m[0][1] - L) <= 2 * tol          # a real line starts at the text edge
        if m and (alpha < 3 or (alpha < 12 and (hm < 0.72 * body_h0 or (hm < 0.85 * body_h0 and not at_edge)))):
            g = g + m
            m = []
        clean.append((m, g))
    rows = clean
    margin = [g for _, g in rows if g]
    main_rows = [m for m, _ in rows if m]
    if not main_rows:
        return dict(main=[], margin=margin, heads=[], apparatus=[], band=(L, R))
    hts = [st.median([w[4] - w[2] for w in m]) for m in main_rows]
    ys = [st.median([w[4] for w in m]) for m in main_rows]
    gaps = [b - a for a, b in zip(ys, ys[1:])]
    sg = sorted(gaps)
    lead = sg[int(0.6 * (len(sg) - 1))] if gaps else 1.0     # body leading: above apparatus, below headings
    body_h = st.median(sorted(hts)[len(hts) // 2:])

    # apparatus: first line (not near the top) after a gap, where the following
    # lines run on tighter leading than the body; everything after it
    app_start = len(main_rows)
    for i in range(3, len(main_rows)):
        small2 = i + 1 < len(hts) and hts[i] < 0.8 * body_h and hts[i + 1] < 0.8 * body_h
        tight = (len(gaps[i:i + 4]) >= 3 and st.median(gaps[i:i + 4]) < 0.8 * lead
                 and hts[i] < 0.93 * body_h and gaps[i - 1] > 0.9 * lead)
        if gaps[i - 1] > 1.2 * lead or small2 or tight:
            nxt = gaps[i:i + 4]
            if nxt and st.median(nxt) < 0.85 * lead:
                app_start = i
                break
            if not nxt and hts[i] < 0.9 * body_h:   # a single short footnote line
                app_start = i
                break
    apparatus = main_rows[app_start:]

    # running head = every row on the first row's baseline, if a gap follows the group
    run_n = 0
    if app_start:
        g = [k for k in range(app_start) if ys[k] - ys[0] <= 0.4 * lead]
        nxt = ys[g[-1] + 1] if g[-1] + 1 < len(ys) else None
        if nxt is not None and nxt - ys[g[-1]] > 1.35 * lead:
            run_n = len(g)
    main, heads = [], []
    for i in range(app_start):
        m, y = main_rows[i], ys[i]
        text = ' '.join(w[0] for w in m)
        width = m[-1][3] - m[0][1]
        gap_before = y - ys[i - 1] if i else 1e9
        gap_after = ys[i + 1] - y if i + 1 < app_start else 1e9
        if i < run_n:                                   # running title (+ page no., [CAP. I.])
            heads.append(('RUNNING', text, y))
            continue
        centred = width < 0.7 * W and abs((m[0][1] + m[-1][3]) / 2 - (L + R) / 2) < 0.12 * W
        if centred and gap_before > 1.3 * lead and len(m) <= 6:
            heads.append(('HEADING', text, y))
            main.append([('§HEADING§', *m[0][1:])] + m)
            continue
        if len(m) == 1 and PURE_NUM.match(m[0][0]) and width < 0.1 * W:
            continue
        main.append(m)
    return dict(main=main, margin=margin, heads=heads, apparatus=apparatus, band=(L, R))


def main_tokens(leaf_split, L=None):
    """Main-text word list for a leaf. Strips line numbers and alinea letters glued
    to either edge, drops stray marks; line-end hyphens are left in place (joined
    across lines/pages by the caller) and `eol` marks the last real word of a line."""
    toks = []
    L = L if L is not None else leaf_split['band'][0]
    R = leaf_split['band'][1]
    for li, line in enumerate(leaf_split['main']):
        kept = []
        for wi, w in enumerate(line):
            txt = w[0]
            if txt == '§HEADING§':
                toks.append(dict(t=txt, line=li, box=w[1:5]))
                continue
            if txt.strip('*') == '':
                continue                                    # folio-change asterisk
            if w[1] < L - 15:                               # protrudes into the left margin
                if PURE_NUM.match(txt) or re.fullmatch(r'[a-dA-D][.,]?', txt):
                    continue                                # line number / alinea letter
                txt = NUM_PREFIX.sub('', txt)
            if w[3] > R + 12:                               # protrudes into the right margin
                if PURE_NUM.match(txt) or re.fullmatch(r'[a-dA-D][.,]?', txt):
                    continue
                txt = NUM_SUFFIX.sub('', txt) or txt
            # editorial footnote superscripts: small numerals, alone or glued to a word
            hline = st.median([x[4] - x[2] for x in line]) or 1
            base = st.median([x[4] for x in line])
            raised = w[4] < base - 0.22 * hline                  # superscript sits above the baseline
            if re.fullmatch(r'\d{1,2}[^A-Za-z0-9]{0,2}', txt) and raised:
                continue
            txt = re.sub(r'(?<=[a-z])\d{1,2}(?=[^A-Za-z0-9]*$)', '', txt)
            if not txt:
                continue
            kept.append(dict(t=txt, line=li, box=w[1:5], eol=False))
        for x in kept:                                     # pencil tick after a hyphen: "prete-/"
            x['t'] = re.sub(r'-[/\\|\'`"]+$', '-', x['t'])
        # eol = last token with a letter (a pencil mark after "prete-" must not block the join)
        for k in range(len(kept) - 1, -1, -1):
            if any(c.isalpha() for c in kept[k]['t']):
                kept[k]['eol'] = True
                del kept[k + 1:]
                break
        toks += kept
    return toks
