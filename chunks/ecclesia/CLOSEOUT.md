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

## Log
| stage | agent | tokens | result |
|---|---|---|---|
| A | R1 (02-b, 02-f, 04-b, 05-d) | 192K | 25 rows: 4 error, 9 weak, 12 style. Lost word *plus* 46.24 (false ¶ break) → tokenfix; quotation bounds in early chunks set by sense, not italics |
| A | R2 (05-f, 06-a, 06-d, 06-g) | 184K | 30 rows: 2 error, 24 weak, 4 style (12 terms, 2 conn., 8 construal/note, 8 italics-rule) |
| D | coordinator | — | lint.py widened: 278 tag keys with space/capital had been skipped; 2 stray `{g:per idem}` removed; lint 0 |
