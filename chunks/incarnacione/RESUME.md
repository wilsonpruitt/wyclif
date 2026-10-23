# RESUME — *De benedicta incarnacione* (ed. Harris 1886; the first B+ volume)

*Read this first in a new session, then `WORKFLOW.md` (stages 7–10), this volume's `CARD.md` and `WAVE-PROMPTS.md`
(with its "Notes from waves" at the end). Translation started 2026-10-22 on Wilson's "Opus go".*

## ▶ 2026-10-23 session: waves 12–19 run — 60/61 translated; 06-e (skipped in wave 6, like 08-e in wave 11) being translated

- **Translated:** every chunk but 06-e (in hand 2026-10-23). Waves 12–18 fully checked (lint, glossary, ledger closed,
  connectives); wave 19 (13-a … 13-d) ledger running; connectives for waves 18–19 extracted (`_connectives/body-18.md`,
  51 occurrences, chunks 12-b … 13-d) — run § B prompt with W=18, then `apply.py 18`. 06-e then needs its own ledger
  (rows from its report → `_verify/rows-20.md`) and a connective pass (`extract.py 20 06-e`).
- **Then stage 9 close-out:** four-class review of the longest/densest chunks (11-a 1256w, 13-a 1188w, 06-e 1233w,
  10-a, 09-a; 13-c has 25 notes), the line-marker plate check below, the headnote sentence on the manuscripts rule,
  PLAN cost row. Then stage 10 site (`site/build.py`, `site/pdf.py incarnacione both`); deploy = Wilson's OK.

- **Per wave (coordinator):** (1) status/`[ENGLISH]`/Latin-unchanged check + lint; (2) scars: read on the plate
  (`/tmp` crop at y ≈ 0.125 + (line−1)·0.0205 of the leaf height); only split/glued words and lost hyphens are
  transcription errors (fix `text/incarnacione/bt/pNNN.txt` → `bplus.py` → shift any `bplus_decisions.tsv` pos the
  fix moved → queue 0 → `relatin.py incarnacione --also <ids,comma-separated>`); misprints, `*` conjectures and
  daggers are Harris's print and stay; (3) rule the glossary proposals (coordinator, delegated) and tag first uses;
  (4) ledger rows → LEDGER.md + `_verify/rows-W.md` → ledger agent → `_verify/apply.py W`; (5) every 2 waves the
  connective agent on `_connectives/extract.py W ids` → `apply.py W`; (6) commit.
- **Editorial rule (Wilson 2026-10-22): the manuscripts outrank Harris** — CARD.md paragraph + "Families" sentence
  (A B C one recension; cross-family agreement, or one witness + the source / a failing argument, outranks the print).
  Memory: `feedback_wyclif-manuscripts-outrank-harris`. Applied in dozens of places so far, each with a T note.
- **Apparatus:** read from the plates (`text/incarnacione/foot/`, Batch API, $2.29), not OCR. ~13 pages carry a
  coordinator CHECK line; most are range figures (4–4) and are fine.
- **Cost so far:** translation ≈190K Opus per wave of 3 chunks; ledger agents 110–235K each; connective batches
  ≈80–100K per 2 waves. Waves 1–11 ≈ 2.1M translation + ≈2.0M ledger + ≈0.6M connectives + review/conform ≈0.5M.
  Remaining ≈8 waves ≈ 3.5M. Then stage 9 close-out (review of the longest chunks + plate doubts) and stage 10
  site (`site/build.py` + `site/pdf.py`; deploy is Wilson's per-deploy OK).

## Open for Wilson / later

- **Line markers in `bt/`** (found 2026-10-23): on p. 204 and p. 220 the `NN|` markers for 20/25/30 sat one line late (fixed on
  the plate; 12-a citations corrected). Pages whose marker offsets change by one within the page, not yet checked on the plate:
  p. 2, 16, 22, 24, 32, 47, 75, 116. A late marker makes translators cite page.line one too low. Close-out: check each plate
  margin, fix the marker, then grep the chunk notes for that page's citations.

- Untraced rows waiting on outside books: Grosseteste *Hexaemeron* (Dales–Gieben 1982) I06a-5, I08b-5; Wyclif's
  own *De Trinitate* (Breck 1962) I01b-9; Cowton (I04c-1); a few *Physics* / commentary numberings.
- The headnote (prol) predates the manuscripts-outrank-Harris rule: one sentence saying the edition follows the
  manuscripts where they agree against Harris, with T notes, is owed before publication.

## Prompt (wave translator; fill the brief path and ids)

> Read <brief> and follow it exactly. It is your input; read another file only where it says so. Ledger ids use the
> prefix I (I09a-1 …). Notes open with the full-stop code (`**C.**`, `**S.**`, `**S/T.**`); lint enforces it. Check
> EVERY scripture quotation with bible.py (book names as "John", "I John", "II Chronicles", "Ps", "Sap"), never from
> memory. Never guess a page.line: cite a line only where you counted it from `text/incarnacione/bt/pNNN.txt`,
> otherwise cite the page alone. Glossary tag keys are lower case with hyphens, letters only. The card's rule "the
> manuscripts outrank Harris" (with its "Families" sentence) is binding: list the places you apply it under "Latin
> doubts", and declined places only where the decision was close. A misspelling or mark in the print itself
> (misprints, `*` conjectures, daggers) is not an OCR scar; nor is a footnote figure displayed against a dash. Report
> as a scar only a split or glued word or a lost hyphen.

Ledger and connective prompts: `WAVE-PROMPTS.md` §§ B–C, as sent in waves 8–11 (the ledger prompt names the earlier
RESULTS files to reuse and the machine-read note-change format `08-b n2: "old" → "new"`).
