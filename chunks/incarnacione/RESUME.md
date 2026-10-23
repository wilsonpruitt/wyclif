# RESUME — *De benedicta incarnacione* (ed. Harris 1886; the first B+ volume)

*Read this first in a new session, then `WORKFLOW.md` (stages 7–10), this volume's `CARD.md` and `WAVE-PROMPTS.md`
(with its "Notes from waves" at the end). Translation started 2026-10-22 on Wilson's "Opus go".*

## ✅ TRANSLATION DONE 2026-10-23 — 61/61 chunks, every one through the per-wave checks

- Waves 12–19 + 06-e this session (06-e and 08-e had been skipped by the earlier wave lists; both done). Ledger closed for
  every row I08e … I13d + I06e (RESULTS-12 … -20); connectives checked for all (RESULTS-12, -14, -16, -18, -20); lint 0.
  Cost this session ≈3.3M Opus (9 translators ≈1.6M, 9 ledgers ≈1.3M, 4 connective passes ≈0.4M).
- **Stage 9 close-out DONE 2026-10-23** (except the headnote sentence, drafted and waiting on Wilson's wording OK):
  four-class review of 11-a, 06-e, 13-a, 13-c, 10-a, 09-a (`_review/REVIEW-*.md`, 58 rows, 2 errors; all applied
  but 13-c row 8, a note the chunk's density does not need; 13-c row 6 put as its own T note at *ut qui*); line
  markers closed (below); GLOSSARY *ypostaticus*; PLAN cost row. **Next = stage 10:** `site/build.py`,
  `site/pdf.py incarnacione both`; deploy = Wilson's per-deploy OK.
- Left from the reviews: LEDGER I11a-1 (Scotus "reports and rejects" what Wyclif calls the Doctor's proofs,
  186.18–20) wants a second look; 06-e 103.29 *eciam* is O's alone (borderline T note); `italics:` is `none` in
  every chunk of every volume (a placeholder), though 163.6–7 and 227.5 are italic in the print.
- Recurring patterns worth knowing at review: Wyclif's Anselm *De inc. Verbi* numbers run one above Migne's; he counts
  Thomas's *Scriptum* III d. 1 articles serially ("q. 8 et 9" = q. 2 a. 4–5); his "De Spiritu Sancto III" for Ambrose
  is the Lombard's mislabel of *De incarn. dom. sacr.*; his *Enchiridion* chapter numbers are not consistent.

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

- **Line markers in `bt/`: CLOSED 2026-10-23.** All 8 suspect pages checked on the plate. p. 2, 16, 22, 24, 32, 116 had
  markers one line late (and the `.tok.jsonl` `ln` one low); moved to where the plate prints them, `ln` recomputed, chunk
  section ranges / `pages:` and 5 note citations corrected (02-c, 03-a, 03-b). p. 47 and 75 already matched the plate.
  Rule: a marker sits where Harris prints the figure, even where Harris miscounts (p. 16 prints 30 on the 29th line;
  p. 47 and 75 likewise irregular). Margin-reference lists were row-based and already right.

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
