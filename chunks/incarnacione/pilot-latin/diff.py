"""Word diff of two page texts for the Latin-method pilot.

    python3 diff.py DIR_X DIR_Y PAGES... > out.tsv

Writes one row per disagreement: page, x, y, context (the words before it in X).
Words are compared with punctuation, capitals and ordinal marks folded, and u/v, i/j folded (the print
uses both; none of these is an error this pilot measures).
"""
import difflib, re, sys, os

def words(path):
    t = open(path).read()
    t = re.sub(r'-\n\s*', '', t)                  # join any line-end hyphen left in
    return [w for w in (re.sub(r'[^\w\[]|\[(?!\?)', '', w) for w in t.split()) if w]

SUP = str.maketrans('ᵃᵇᶜᵈᵉⁱᵒᵘᵐ°', 'abcdeioumo')

def fold(w):
    w = w.translate(SUP)
    w = re.sub(r'^(\d+)(o|a|i|um|us|e)$', r'\1', w)   # ordinal marks: 3° = 3o = 3, 2ᵃ = 2a = 2
    return w.lower().replace('v', 'u').replace('j', 'i')    # capitals: not measured either

def main():
    dx, dy, pages = sys.argv[1], sys.argv[2], sys.argv[3:]
    print('page\tx\ty\tcontext')
    for p in pages:
        fx = os.path.join(dx, f'p{int(p):03d}.txt') if not dx.endswith('fordham') else \
            os.path.join(os.path.dirname(dx), f'fordham_p{int(p):03d}.txt')
        fy = os.path.join(dy, f'p{int(p):03d}.txt') if not dy.endswith('fordham') else \
            os.path.join(os.path.dirname(dy), f'fordham_p{int(p):03d}.txt')
        x, y = words(fx), words(fy)
        sm = difflib.SequenceMatcher(None, [fold(w) for w in x], [fold(w) for w in y], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal':
                print(f"{p}\t{' '.join(x[i1:i2])}\t{' '.join(y[j1:j2])}\t{' '.join(x[max(0, i1-4):i1])}")

main()
