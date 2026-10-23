# RESUME — *De benedicta incarnacione* (ed. Harris 1886; the first B+ volume)

*Read this first in a new session, then `WORKFLOW.md` (stages 7–10), this volume's `CARD.md` and `WAVE-PROMPTS.md`
(with its "Notes from waves" at the end). Translation started 2026-10-22 on Wilson's "Opus go".*

## ⏸ PAUSED 2026-10-22 (Wilson: pause after wave 11 and its ledger, push, new session) — 36/61 chunks translated (prol + chs 1–8, pp. 1–138)

- **Translated:** prol, 01-a … 08-d (36 chunks), every one through the per-wave checks: lint 0, connectives
  (waves 1–11: 357 checked, 5 fixed: three minor premisses "but" → "now", two *non autem* → "but not"), ledger closed for all rows Iprol … I08d (waves 1–11), glossary conformed.
- **Next (corrected 2026-10-23: 08-e was still a draft, chapter 8 was NOT done):** wave 12 = 08-e 09-a 09-b (running
  2026-10-23); then 09-c 09-d 09-e, 10-a 10-b 10-c, 10-d 10-e 10-f, 10-g 11-a 11-b, 11-c 11-d 12-a, 12-b 12-c 12-d,
  13-a 13-b 13-c 13-d (8 waves after 12). `.venv/bin/python scripts/w3/brief.py incarnacione <ids>` → one Opus agent
  per brief with the one-line prompt plus the standing addenda (this file's § Prompt). Two agents can overlap (a
  translator + the previous wave's ledger); the coordinator applies results between them.
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
