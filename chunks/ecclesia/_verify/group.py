"""Sort the open De ecclesia LEDGER rows into source groups for the close-out verifiers (CLOSEOUT.md stage C)."""
import re, os, collections
here = os.path.dirname(os.path.abspath(__file__))
rows = []
for l in open(os.path.join(here, '..', '..', '..', 'LEDGER.md')):
    if not l.startswith('| ') or 'ecclesia' not in l: continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) < 5: continue
    s = c[3].lower()
    if s in ('verified', 'editor', 'untraced'): continue
    rows.append(l.rstrip('\n'))
G = [  # first match wins
 ('wyclif',   r'cross-ref|ut dixi|dixi superius|superius|libri (quarti|quinti|V\b)|libro|this work|this book|\bcap\. ?[IVX]|De ideis|De eucharistia|De veritate|De civili|De mandatis|De dominio|Wyclif\'s own|Summa de ente|De statu|De potestate|exposui|p\. \d{2,3}\b'),
 ('scholastic', r'Thomas|Aquinas|\bST\b|Bonaventur|Sent\.|Auxerre|Altissiodor|Hostiens|FitzRalph|Armachan|Bradwardine|Grosseteste|Lincolniens|Richard|Scotus|Lombard|Hugucci|Peter of Tarentaise|Durand|Ockham|Holcot'),
 ('liturgy',  r'missal|breviary|antiphon|collect|introit|Exsultet|hymn|preface|postcommunion|sequence|office|Te igitur|canon of the mass'),
 ('law',      r'Friedberg|gloss|Digest|Dig\.|Cod\.|Codex|\bX \d|Sext|Clem\.|Extrav|Decret|Gratian|C\.\d+ q|D\.\d+|canon law|civil law|English law|writ|statute|de excommunicato'),
 ('philosophy', r'Aristot|Cat\.|Metaph|\bEN\b|NE |Eth\.|Phys|Soph|APo|De gen|Liber XXIV|Boethius|Ovid|Seneca|Cicero|Juvenal|Porphyr|Avicenna|Averro|Plato|proverb|maxim|pentameter|verse'),
 ('history',  r'1378|1377|1379|parliament|Westminster|Gloucester|Denia|Dene|Urban|Clement|schism|Boniface|India|legend|pope|king|Edward|Richard II|Gaunt|history|historical|Brendan|Constantine'),
]
out = collections.defaultdict(list)
for r in rows:
    for g, p in G:
        if re.search(p, r, re.I): out[g].append(r); break
    else: out['fathers'].append(r)
# split the fathers in two by chunk order
f = out.pop('fathers'); h = len(f)//2
out['fathers-1'], out['fathers-2'] = f[:h], f[h:]
os.makedirs(os.path.join(here, 'groups'), exist_ok=True)
hdr = '| id | chunk / note | claim | status | how / next step |\n|---|---|---|---|---|\n'
for g, rs in out.items():
    open(os.path.join(here, 'groups', g + '.md'), 'w').write(f'# LEDGER rows to close — {g} ({len(rs)})\n\n' + hdr + '\n'.join(rs) + '\n')
    print(f'{g:12s} {len(rs)}')
print('total', len(rows))
