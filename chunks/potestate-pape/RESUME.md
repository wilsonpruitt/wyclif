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
- Pushed to GitHub 2026-10-07 (cf1ae5b). NOT deployed: the analytics snippet waits for an OK'd deploy, and the Vercel CLI is logged in to the covenant-austin account; run `npx vercel login` (wilson-pruitts-projects) first.

## Running log (stage 7–8)
- **Wave 1** (01-b … 02-c, 2 briefs, 332K): 14 scars, 4 print misprints kept with T notes, 3 connective fixes; ledger 45 rows closed (`_verify/RESULTS-1.md`: 38 verified, 2 editor, 5 untraced; Loserth wrong 4×, incl. *De civ. dom.* II ch. 8 "non extat"); 26 note changes applied. Verify agent cost 267K / 140 tool calls: give it fewer rows per run.
- **Wave 2a** (02-d … 03-b, 184K): 13 scars; *emissa* for printed *omissa* at 47.18 accepted (T note, our emendation).
- ⚠ **Folio-mark scar:** the editor's folio change `|` (with 167ᵃ etc. in the margin) is read as a stray *I*, *j* or *!* (7 so far). Translators catch it; read each on the plate (the vote cannot, every scan has it).
- ⬜ **Outside sources wanted** (untraced for want of a text): FitzRalph, *Summa in quaest. Armen.* (Paris 1512: **HathiTrust `ucm.5320228710`, full view**, Complutense copy, likely also on Google Books; Cloudflare blocks scripted fetches, so Wilson would download the PDF by hand into `sources/`; recurs all volume), Guido de Baysio *Rosarium* (incunables), Wyclif *De universalibus* (Mueller 1985). Hus parallels checked in Schaff's English only.
- **Wave 2b** (03-c … 03-e, 160K): 20 scars incl. lost *In* (55.9); [Christ,] at 56.14 and *cementum* at 58.9 accepted (T notes); *Lincolniensis* "Lincoln" (De ecclesia precedent), *seculares domini*. **Comma rule** added to vote.py (WORKFLOW 4b): 501 stops → commas volume-wide, 7 side-note leaks removed; 9 line-end cases unread (`commas_eol.tsv` after a full vote).
- **Wave 2 checks done:** connectives 63 / 1 fix; ledger 32 rows (25 verified, 6 corrected; 3 editor; 3 untraced: P03b-4 *Sermo IV*, P03c-7 prayer, P02d-4 needs PG 56; P03a-1 awaits FitzRalph), 29 note changes; Wyclif's own misattributions stay in the English, facts in the note. FitzRalph *Summa* 1512: Wilson downloading from MDZ (2026-10-07).
- **Wave 3a** (04-a … 04-c, 164K): 6 scars; `vote.py` pair rows now skip emptied tokens (and a folio mark can glue on: `se| quela`); *orator* gets a third CONTEXTUAL sense "suppliant" (one praying to God); *sequela* CONTEXTUAL; *dyasones* (64.33) left untranslated with T note (cf. 1 Cor 13:1 *aes sonans*).
- **Wave 3b** (04-d … 05-d, 2 briefs, 287K): 24 scars, 6 more folio marks (now 15) and a second *lost word beside a side-note* (*ita*, 80.12); *stragulare* (MSS) adopted over the print's *strangulare* at p. 92 (variant gives the sense: card rule); *dampnacio* CONTEXTUAL (judicial "condemnation"); *archivicarius* conformed to "archvicar". Wave 3 connectives: 75 / 3 fixed. Ledger wave 3 (28 rows + 4 FitzRalph) running.
- **Wave 4a** (05-e … 06-a, 157K): 12 scars; a WHOLE short line lost in every scan (p. 95 *mor-|tale.* ¶ *Sed*), so lostruns cannot see it: watch for a hyphen-broken word that does not join. *negociatores* "dealers" (vs *mercantes* "traders"). ⚠ Run `vote.py` in the foreground: background runs twice lost their output.
- **FitzRalph** *Summa* 1512 (MDZ bsb00034856, 363 pp., split in 100-page PDFs, each with a cover sheet): `sources/fitzralph-summa-1512-p001-100.pdf`, `-p101-200.pdf` (gitignored); pp. 201–363 still to come from Wilson.
