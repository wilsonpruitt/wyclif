# RESUME — *De potestate pape* (queue 3; M5, the second volume after the Dialogus)

*Read this first in a new session, then `WORKFLOW.md` (stages 7–10) and this volume's `CARD.md`. Started 2026-10-07
on Wilson's "opus go" (estimate given: ≈12–13M Opus for the volume).*

## Status 2026-10-07 — stages 1–6 DONE; next: stage 7 (translate in briefs)

- **Latin established** (406 pp.: 12 chapters pp. 1–397 + the medieval *compendium* pp. 398–406; indexes excluded).
  4 scans, no Fordham. Offset 61 (p. 2 = n63, checked). p. 266 is faded blank in Princeton: `pivotpatch.tsv`
  takes it from `tractatusdepotes00wycl` n327.
- Plate pass 1,405 items (4 Opus agents, 1.03M) · scars 135 (2 Sonnet, 0.21M) + 27 by rule · side-notes 559 bands
  (4 Sonnet, 0.66M; control 12/13 exact) · boundaries read on the plate by the coordinator. `vote.py`: 1,528
  decisions, stale 0; `lostruns.py`: 0 likely lost; `boundaries.py`: 3, all legitimate (verse, compendium end).
- **107 scaffolds** `wyc-potestate-pape-NN-x.md` (01-a … 12-u, comp-a, comp-b), side-notes spliced.
- **Chunk 01-a translated** (Opus 114K) and reviewed fresh (0 errors, 11 weak, 6 style: `_review/REVIEW-01a.md`);
  review applied (row 3 rejected: *descripcio* stays "definition"; notes now 1–20). Ledger P01a-1…11 filed, NOT yet verified (verify with wave 1, stage 8).
- **Ruled 2026-10-07:** *potestas* "power"; *potencia* CONTEXTUAL potency/power (Wilson); coordinator rows
  *potentatus*, *potestas dominativa*, *relacio racionis*, *maneries*, *debitum* (marriage debt). Card updated
  (scar rule, italics in indirect speech, ordinals, *vero/verumtamen/unde*, *nunc … aliquando*).

## Next: stage 7, in briefs of 3–5 chunks, in order 01-b … comp-b (106 chunks)
`.venv/bin/python scripts/w3/brief.py potestate-pape 01-b 01-c 01-d` → one Opus agent per brief, at most 2 at once.
After EACH wave (WORKFLOW 8): scars from the reports → `text/potestate-pape/tokenfix.tsv` → `vote.py SLUG p p` →
`relatin.py SLUG --also <translated ids>`; ledger rows → LEDGER.md AND verify them that wave; *sed/autem* check;
glossary conform; split-tag grep; lint. Commit per wave. Measured rate to track: ~21K/page translation.

## Pipeline changes made on this volume (all in WORKFLOW)
`italics.py` (ABBYY italics → briefs) · `paramerge.tsv` · `pivotpatch.tsv` · `lostruns.py` (stage 3b) ·
tokenfix `^word` (page's first token) and pair `a || b` · vote drops signature lines and citation-only page
feet · `chapters.py` takes unflagged CAPITULUM + ordinal word, part letters to z · `boundaries.py` lists
lower-case ¶s (a false ¶ = a word the side-note swallowed) · `scarqueue.py` / `scars.py` per-volume.

## Cost so far (agents + coordinator, Opus unless noted)
Plate 1.03M · scars 0.21M (Sonnet) · side-notes 0.66M (Sonnet) · 01-a 0.11M + review 0.12M + apply · coordinator
~0.3M ≈ **2.5M**. Remaining estimate: translation ~9M (106 chunks, ~400 pp.) + per-wave checks ~2M + close-out ~0.5M.

## Open, non-blocking
- `text/potestate-pape/PLATE-FLAGS.md`: p. 267 fragmented blurred line (filled in print order; read once more).
- Nothing pushed; nothing deployed (the site's analytics snippet is committed, waiting for the next OK'd deploy).
