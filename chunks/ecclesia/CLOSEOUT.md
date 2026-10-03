# *De ecclesia* close-out (WORKFLOW stage 9) — plan, 2026-10-03

*Approved by Wilson 2026-10-03: run all agents on **Opus**; review set = the 25 computed chunks. No push, no deploy.*

## Where it stands (measured 2026-10-03)
- 159 chunks, 136,061 Latin words, all `translated`. Lint clean; split-tag check 0.
- The per-wave *sed/autem* check was never run mechanically (M5-RESUME: "agent's own report only"), so it is
  owed on the whole volume: 1,103 *sed*, 500 *autem*.
- LEDGER: 227 *De ecclesia* rows open (186 `to-verify`, 41 `open`) + 13 non-standard statuses
  (`verified (partial)`, `checked`, `probable`, `verified (loose)`…). These are the rows the per-wave passes
  could not close, mostly sources not on disk.

## Stages
**0. Coordinator prep.** Sort the open rows into source groups (`_verify/groups/`); build the Latin+English
¶ extract for the connective check (`_connectives/body-NN.md`, notes left out).

**A. Four-class review (Opus, 6 agents, fresh context).** Chunks chosen by rule: top 40% in Latin length AND
top 40% in **C**-notes per 1,000 words (`check` word count; C-note count). Method and table as
`chunks/dialogus/_review/REVIEW-targeted.md`. Output `_review/REVIEW-RN.md`.
- R1: 02-b, 02-f, 04-b, 05-d
- R2: 05-f, 06-a, 06-d, 06-g
- R3: 08-f, 09-a, 09-c, 09-e
- R4: 10-b, 10-c, 12-b, 12-c
- R5: 12-d, 12-e, 13-a, 14-g
- R6: 18-c, 21-d, 21-f, 23-h, 23-k

**B. Connective check (Opus, ~9 agents)** over the other 134 chunks: every *sed/autem* classed (a) next
step "now" · (b) adversative "but" · (c) continuative "and"; *non … sed* "but". Output
`_connectives/RESULTS-NN.md` in the Dialogus format (changes · doubtful, left as they are).

**C. LEDGER (Opus, ~8 agents, one per source group).** Every row ends `verified` / `editor` / `untraced`;
no partial statuses. An `untraced` row comes with hedged note wording. Output `_verify/batch-NN.md`.
Groups: scholastics (Thomas, Bonaventure IV *Sent.*, William of Auxerre, Hostiensis, FitzRalph,
Bradwardine, Grosseteste) · liturgy · canon & civil law · Aristotle & philosophy · Wyclif's own
cross-references (incl. book-V rows E19a-1, E22f-9, E22h-12, E23a-3; Society OCR in `sources/ia-ocr/`) ·
Fathers ×2 (local PL `~/patrologia/sources/pl/tei/`) · history & English law.

**D. Coordinator.** Apply fixes the card already decides; doubtful items → `RULINGS-PENDING.md` for Wilson.
Rewrite each report after its fixes (the rewrite is the deliverable). `lint.py`, `relatin.py ecclesia --dry`
(must be 0), scrub grep. Rewrite PLAN's cost row from the measured rate. Commit locally per stage.

Not in scope: a plate pass for Latin doubts (every brief checked its plates; the structural "not applied"
items go to RULINGS-PENDING); italics (decide at stage 10).

## Cost
Estimate: A ~0.7M · B ~0.7M · C ~1.5M · coordinator ~0.4M ≈ **3.3M, all Opus**. At most 2 agents at once (8 GB).

## Coordinator rulings for the appliers (A2)
- All rows apply; where a row offers alternatives, take the one the reviewer prefers, else the first.
  Skip rows that only fix a spaced/capitalised tag key (script at the end). Ledger-id splits → stage C.
- Latin restored to the print by deleting "OCR" tokenfix rows that were really silent emendations of
  Loserth's misprints (standing rule: the Latin is the print). The English stays; each gets a T note:
  12-d 263.29 *faciendo* (English follows *facienda*, Rom. 3:8, our emendation) · 12-e 270.29 *XXVII°, 69*
  (Loserth's misprint; Matt. 27:19) · 18-c 424.4 *novam* (R6 #4 wording). 12-d 267.3 *latronum?* and 12-c
  258.23/25 punctuation restored (no note). 02-f 46.24 *plus* and 09-e 202.22 *III°* restored from the plate.

## Log
| stage | agent | tokens | result |
|---|---|---|---|
| A | R1 (02-b, 02-f, 04-b, 05-d) | 192K | 25 rows: 4 error, 9 weak, 12 style. Lost word *plus* 46.24 (false ¶ break) → tokenfix; quotation bounds in early chunks set by sense, not italics |
| A | R2 (05-f, 06-a, 06-d, 06-g) | 184K | 30 rows: 2 error, 24 weak, 4 style (12 terms, 2 conn., 8 construal/note, 8 italics-rule) |
| A | R3 (08-f, 09-a, 09-c, 09-e) | 198K | 30 rows: 0 error, 23 weak, 7 style (13 terms, 4 conn., 3 medieval, 3 construal, 7 quotation). 202.22 *111°* → *III°* tokenfix |
| A | R4 (10-b, 10-c, 12-b, 12-c) | 244K | 27 rows: 0 error, 16 weak, 11 style; italics checked on all 20 pages; 4 notes contradict the plate; 1 Latin-text row |
| A2 | apply R1+R2 | 149K | all rows applied except 5 tag-key rows (script) and R1 #18 (ledger stage); 04-b notes renumbered, LEDGER pointers moved; lint 0 |
| A | R5 (12-d, 12-e, 13-a, 14-g) | 238K | 27 rows: 0 error, 22 weak, 5 style (9 terms, 3 conn., 1 medieval, 4 construal, 10 quotation); 3 silent Latin departures from the print (263.29, 267.3, 270.29) |
| B | extract 01 | 135K | 113 checked: 7 changes, 4 doubtful |
| B | extract 02 | 146K | 164 checked: 5 changes, 8 doubtful; 04-f p.91 {g:sponsa} on "bridegroom" (→ sponsus, end pass) |
| B | extract 03 | 146K | 132 checked: 1 change, 7 doubtful |
| A2 | apply R3+R4 | 167K | 57 rows applied (3 tag-key rows partly: tags added, keys left for script); LEDGER E10b-5 page 37→39; lint 0 |
| B | extract 04 | 154K | 144 checked: 15 changes, 10 doubtful (11-a cum-clause minor needs recast) |
| B | extract 05 | 158K | 163 checked: 9 changes, 6 doubtful |
| B | extract 06 | 150K | 160 checked: 6 changes, 11 doubtful; 17-b p.393 wrong tag fixed (→ ecclesia-triumphans) |
| A2 | apply R5+R6 | 158K | 62 rows applied; T notes for restored print readings; 04-f sponsus; new LEDGER row E14g-5 (routed to fathers-1); E04b-4 split → E04b-6 |
| B | extract 07 | 137K | 143 checked: 3 changes, 8 doubtful |
| B | extract 08 | 159K | 158 checked: 9 changes (8 rows), 9 doubtful |
| B | extract 09 | — | 136 checked: 15 changes, 10 doubtful |
| D | coordinator | — | lint.py widened: 278 tag keys with space/capital had been skipped; 2 stray `{g:per idem}` removed; lint 0 |
