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

## Owed at work close (the gate)

- Merge `_batch-A.md` + `_reports.md` ledger rows into LEDGER.md; ledger-verification pass (fetch and
  read the sources; statuses to `verified` / `untraced`).
- Tag the 9 terms ruled 2026-09-28 in chunks 01–05 (rendered there untagged, before the ruling);
  "ex fide scripture" sites follow the genitive rule.
- Tag the 12 wave-2 terms and 13 wave-3 terms (ruled 2026-09-28) at first occurrence in chunks 10–17; *inconveniencia* C notes already in 11, 12.
- Ch. 18 Isa. 1:23: D–R wording missing (bible.py gave none); supply it.
- Plate-check ch. 14 side-note 26.28 "Mend. objects" (kept from the OCR draft).

- Four-class spot check across chunks; lint all; rewrite PLAN's cost table from the measured rate.

## Next

Wave 4 done (≈91k/chunk). Awaiting Wilson: *regnum* split (realm vs kingdom) + wave-4 glossary proposals, then
go + model for wave 5 = chunks 22–25.
