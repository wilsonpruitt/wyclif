# RESUME — *Dialogus* translation (M3)

*The coordinator's pointer. Read this first in a new session, then act on "Next".*

## Shape (Wilson, 2026-09-28, after comparing the Bonaventure grind)

- **One chunk per Opus subagent, waves of 4**, sent in one message. Main thread coordinates only:
  it never translates.
- Each agent reads `chunks/dialogus/CARD.md` + `GLOSSARY.md` + its scaffold (not the full
  CONVENTIONS / pilot / Thakkar; the card is their working core).
- Agents edit only their chunk and report ledger rows, glossary proposals and Latin doubts. The
  coordinator appends them to `_reports.md`, commits after each wave (chunks + `_reports.md` + this
  file), and surfaces a two-line context update.
- Priced by **pace**, not a token cap: record tokens and minutes per chunk below.
- **Register rulings go to Wilson as they arise, before they spread** (the Sermones lesson), with a
  census of the term's sites.
- **From wave 6 (Wilson, 2026-09-28): the coordinator rules glossary proposals itself** (census + dikaiosune
  rule; referent split vs CONTEXTUAL), commits the rows before the next wave, and reports them after the
  wave for overturn. Only a genuinely doubtful register question still goes to Wilson first. Token
  go-aheads per wave are unchanged.

## Status

| chunk | status | notes | tokens | min |
|---|---|---|---|---|
| 01–05 | translated (batch A, 5-in-1 agent) | 12/5/7/6/7 | 235k for the five | 23 |
| 06 | translated (wave 1) | 5 | 90k | 3 |
| 07 | translated (wave 1) | 6 | 93k | 3 |
| 08 | translated (wave 1) | 7 | 94k | 3 |
| 09 | translated (wave 1) | 11 | 119k | 6 |
| 10 | translated (wave 2, lean) | 10 | 91k | 2.6 |
| 11 | translated (wave 2, lean) | 8 | 86k | 2.3 |
| 12 | translated (wave 2, lean) | 6 | 86k | 2.5 |
| 13 | translated (wave 2, lean) | 11 | 87k | 2.6 |
| 14 | translated (wave 3) | 11 | 87k | 2.4 |
| 15 | translated (wave 3) | 10 | 95k | 2.8 |
| 16 | translated (wave 3) | 8 | 87k | 2.1 |
| 17 | translated (wave 3) | 7 | 85k | 2.0 |
| 18 | translated (wave 4) | 11 | 91k | 2.7 |
| 19 | translated (wave 4) | 11 | 91k | 2.7 |
| 20 | translated (wave 4) | 12 | 87k | 1.9 |
| 21 | translated (wave 4) | 13 | 95k | 2.6 |
| 22 | translated (wave 5) | 10 | 94k | 2.4 |
| 23 | translated (wave 5) | 13 | 111k | 4.1 |
| 24 | translated (wave 5) | 12 | 101k | 3.0 |
| 25 | translated (wave 5) | 11 | 94k | 2.2 |
| 26 | translated (wave 6) | 11 | 102k | 3.0 |
| 27 | translated (wave 6) | 14 | 98k | 2.8 |
| 28 | translated (wave 6) | 10 | 97k | 2.4 |
| 29 | translated (wave 6) | 12 | 108k | 2.9 |
| 30 | translated (wave 7) | 24 | 141k | 5.5 |
| 31 | translated (wave 7) | 19 | 118k | 4.7 |
| 32 | translated (wave 7) | 19 | 124k | 4.8 |
| 33 | translated (wave 7) | 10 | 99k | 3.0 |
| 34 | translated (wave 8) | 8 | 95k | 2.2 |
| 35 | translated (wave 8) | 10 | 93k | 2.3 |
| 36 | translated (wave 8) | 9 | 99k | 3.2 |
| epil-a | translated (wave 8) | 32 | 135k | 5.3 |
| epil-b | translated (wave 8) | 31 | 138k | 6.4 |

## Owed at work close (the gate)

- Merge `_batch-A.md` + `_reports.md` ledger rows into LEDGER.md; ledger-verification pass (fetch and
  read the sources; statuses to `verified` / `untraced`).
- Tag the 9 terms ruled 2026-09-28 in chunks 01–05 (rendered there untagged, before the ruling);
  "ex fide scripture" sites follow the genitive rule.
- Tag the wave-2/3/4 terms (ruled 2026-09-28) at first occurrence in chunks 10–21; *inconveniencia* C notes already in 11, 12.
- Ch. 18 Isa. 1:23: D–R wording missing (bible.py gave none); supply it.
- Plate-check ch. 14 side-note 26.28 "Mend. objects" (kept from the OCR draft).

- ⚠ Majority-error sweep: 74.22 *Chnstus* passed by majority (4 of 6 witnesses share the OCR confusion). Run a
  non-word check of the established text against the lexicon (every word not in `catalog/lexicon/agreed.txt`
  and not a proper name), plate-check the survivors.
- Merge the 12 unresolved Latin doubts in `_reports.md` (waves 5–8) into the transcription notes review.
- Four-class spot check across chunks; lint all; rewrite PLAN's cost table from the measured rate.

## Next

**Translation complete: 38/38 chunks `translated` (2026-09-28).** Next is the close-out gate above (ledger merge +
verification pass, glossary tagging of rulings in 01–38, majority-error sweep, four-class spot check, lint all, PLAN
cost table). Ask Wilson before starting it: it is its own token run.
Estimate 400–700k (mostly the ledger verification: fetch and read sources). Suggested split: glossary tagging
and lint are mechanical (Sonnet); ledger verification, the majority-error sweep's plate checks and the spot
check want Opus. Wilson chose (2026-09-29) to run close-out in a fresh session.
