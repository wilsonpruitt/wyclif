# RESUME — *De potestate pape* (queue 3; M5, the second volume after the Dialogus)

*Read this first in a new session, then `WORKFLOW.md` (stages 7–10), this volume's `CARD.md` and `WAVE-PROMPTS.md`. Started 2026-10-07
on Wilson's "opus go" (estimate given: ≈12–13M Opus for the volume).*

## ⏸ PAUSED 2026-10-12 (Wilson: "pause after this") — 90/107 translated (01-a … 12-f, pp. 1–338); 17 left (12-g … 12-u, comp-a, comp-b)

- **Translated: 33 of 107 chunks** (01-a … 06-d, pp. 1–118), every one through the per-wave checks: scars fixed + relatin'd, connectives (waves 1–4: 309 checked, 8 fixed), ledger closed for all rows P01a … P06d (waves 1–4), glossary conformed, lint 0.
- **Next:** `.venv/bin/python scripts/w3/brief.py potestate-pape 06-e 06-f 06-g` → one Opus agent per brief (≤ 2 at once); then 06-h 06-i 07-a … in order. After each wave: scars (plate-read every real-word/numeral row) → `tokenfix.tsv` → `vote.py SLUG p p` (FOREGROUND) → `relatin.py SLUG --also <ids>`; ledger rows → LEDGER.md; every ~2 briefs run the connective + ledger agents (WAVE-PROMPTS.md; `_connectives/extract.py W ids`, `_connectives/apply.py W`; ledger note changes applied by script).
- **Cost so far ≈ 6.2M** (2.5M stages 1–6; translation 1.43M for 30 chunks ≈ 12K/page; checks 1.25M; coordinator ~1M). Projected total ≈ 13–14M, slightly over the estimate because of the per-wave ledger agents (130–270K each).
- **FitzRalph** *Summa* 1512 on disk, scan pp. 1–200 (book VII located: VII.3–5 at scan p. 98, VII.18–21 at pp. 107–108). Wyclif's "II.4" (P01a-4, P02c-1) is NOT the print's book II: try book XI.8 ff. (scan p. 178 ff.) or later books when pp. 201–363 arrive (Wilson downloading from MDZ; save as `sources/fitzralph-summa-1512-p201-300.pdf`, `-p301-363.pdf`).
- Untraced, waiting on outside sources: two Aristotle rows (P04a-2, P05b-1: Perseus was down), Guido de Baysio *Rosarium*, *De universalibus*, PG 56 (*Opus imperfectum*), the 1377 bulls (P05b-2).

## Earlier status (stages 1–6)


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
- **Wave 5** (06-e … 07-a, 2 briefs run in parallel, 312K; resumed 2026-10-08): 9 scars; 6 doubts read on the plates, all the print's own (*que processit Cayn* 119.15, [from] supplied as our emendation; *integra individua* 127.23; *status primum* 128.18; *gracia concomitante* 132.14, read *concomitancie* as our emendation; 121.20 apparatus *supositum* keys to no clear word, left). 9 glossary rows ruled (*status*, *preeminencia*, *primas*, *dominari* "lord it", *correpcio fraterna*, *dileccio*, *gracia concomitancie* ⚠, *Pseudo* "the Pseudo", *illapsus*). *minor* (Luke 22:26): DR "younger" in quotation, "the lesser" in Wyclif's prose (07-a n3), accepted. Pope's hired *milites* → "soldiers" (GLOSSARY 10-02 row). 29 ledger rows filed; connectives (35) + ledger agents running.
- **Wave 5 checks done:** connectives 35 / 0 fixed. Ledger 29 rows (24 verified, 4 editor, 1 untraced: P07a-1 Ambrose "epistola"); 23 note changes. Loserth wrong: X 5.32.2 for X 5.7.12 (same incipit *Quum ex iniuncto*), Boethius PL 63, 724 not 720, Bernard *De cons.* III.1.2 PL 182, 759 not 769. Wyclif merges *Quaest. VNT* q. 35 and q. 101 (Caiaphas); Higden's voice is the devil's, Wyclif's an angel's (facts in the notes).
- **Wave 6a** (07-b … 07-d, 147K): 5 scars; plates confirm the PRINT has *erivatis* (147.16), *sol iusticia* (143.18), *Si tu est* (145.18): Latin kept, English follows the emendation with a T note. ⚠ A Loserth misprint can look exactly like an OCR scar: plate-read before writing a tokenfix row for any letter-loss "scar". 4 glossary rows (+ *exproprietarius* adj., *capitaliter* "at her head" of a crown). 12 ledger rows filed (to verify with wave 6).
- Running: 07-e … 07-g and 07-h … 08-b.
- **Wave 6b** (07-e … 08-b, 2 briefs, 336K): 18 scars, all read on the plates. Print confirmed (Latin kept, English emends with T note where needed): *electis* → *elementis* 155.8, *venaices* → *vendices* 170.27, *cece* 170.15 (left untranslated, T note), *fit* 167.29 ("is made"), *prodessendum*, *ex corpore*, *mellifluum*; no lost *non* at 151.9 or 156.6. A word split by the folio mark across a page turn (*no|mine* 147 / *tenus* 148): tokenfix pair `no| mine` (the mark is still on the token when pairs apply) + `^tenus` → empty. A whole reference lost (*Genes. III, 5*, 148.20) found via commas_eol. 8 glossary rows + 3 extended; 44 ledger rows filed.
- **Wave 6 checks:** ledger 6a (P07b … P07g, 33 rows) running; ledger 6b (P07h … P08b, 23 rows) + connectives (07-b … 08-b) next.
- **Wave 6 checks:** connectives 97 / 0 fixed. Ledger 6a (33 rows: 22 verified, 8 editor, 3 untraced), 21 note changes: three notes said "no reference" where Loserth's foot has one (read his foot FIRST); Gregory's journey is John the Deacon, not Bede. `_verify/apply.py W` now applies any RESULTS file. Ledger 6b (P07h … P08b, 23 rows) running.
- **Wave 7a** (08-c … 08-h, 2 briefs, 292K; ch. 8 done): 19 scars on the plates. Print confirmed: *XLVI distinccione* (read XCVI, our emendation), *affflixit*, *Chrisus* (T note), *cecata*, *universalibus*, *magis facit*, *erant dampnati*. OCR word order (*Ex ut quibus* → *Ex quibus ut*: two chained pair rows); a lost verse number (*15—16*); side-note English *be* leaked into ch. 9's first line (found through commas_eol). 9 glossary rows; 30 ledger rows filed (P08c … P08h not yet verified).
- Running: 09-a … 09-c.
- **Wave 6b ledger** (23 rows: 18 verified, 3 untraced): Ep. 112 is Jerome's (Aug. Ep. 75); FitzRalph's capital reasons VII.15, the empire list VII.16 is John's (interlocutor).
- **Wave 7** (08-c … 09-f, 4 briefs): ledger 7a (P08c … P08h, 30 rows: 28 verified, 1 untraced; Higden IV.26 not IV.36, Sermo 129.9). Print confirmed: *cursiv* 207.7 (read *vita*, our emendation), *ad implere*, *uti*, impossible verses Mark IX, 3 / Matth. XVI, 29 (English gives the true verse, T note). *Cestrensis* ruled "the Chester [chronicler]" and conformed. ⚠ `~/douay-glossa/raw/DRC.json` Acts 20:27 reads "spread" for "spared" (other project's data; told Wilson). Connectives wave 7 (110) running; ledger 7b (P09a … P09f, 24 rows) next.
- Running: 09-g … 10-a.
- ⛔ **08-c lost and redone (2026-10-08):** its translation was overwritten by a `relatin.py` run (vote range 159–173 touched p. 173 while 08-c was still a draft in an agent's hands); found by the wave-7 connective agent (¶2 still `[ENGLISH]`), not by lint. Re-translating as a single brief (P08c-1 kept). Rule now in WORKFLOW 7. Wave-7 connectives: 104 checked, 3 fixed (09-a, 09-c, 09-d); 08-c's 6 *sed* to check after the redo.
- **08-c redone** (97K, single brief). **Wave 8a** (09-g … 10-a, 130K; ch. 9 done): the OCR had LOST *non* in *qui Christi non est* (216.24, every scan) — the translator caught it from the italics and the repeat at 217.4; restored by pair tokenfix. Print confirmed: *dominio* 218.23, *inconsequens* 222.21. 6 glossary rows; 15 ledger rows (P08c-2, P09g, P09h, P10a).
- Running: 10-b … 10-d; ledger 7b (P08c-2 + P09a … P09f, 24 rows). Then: connectives for 08-c + 09-g … 10-d; ledger 8 (P09g … P10d).
- **Waves 8–9** (09-g … 11-a; ch. 9 and 10 done): ledgers 7b (24), 8 (32) closed — Loserth slips: PL 192, 885–89; Tract. 121.4; Sermo 354; Flores II; Ypodigma 284; D.40 c.2 *loco Pauli … gradum Petri* (his *Petri et Pauli* is his emendation); FitzRalph VII.24 350 / *caput aliarum*. Connectives waves 8 (67/5), 9 (58/1). Rulings: *replicatur* "it is rejoined" (conformed); *summus pontifex* "highest pontiff" (stray "supreme" conformed in 03-c, 08-g, 10-j); *papa cesareus* "caesarean pope"; *imperium* "command"; *corripere* "reprove"; *subtiliare* CONTEXTUAL. Side-note OCR typos fixed in tsv AND chunks. ⚠ Folio mark is still on the token when pair rows apply (`an| tipapa.`).
- Running: 11-b … 11-d; ledger 9 (P10e … P10j, 29 rows). Next: ledger P10k … P11a (19 rows), connectives 10-k … 11-d.
- **Wave 11a** (11-e … 11-g, 171K): 20 scars, a lost verse number (Act. primo, 1:); translator's plate-checked emendations accepted: *electorum/electa* → *elementorum/elementa* (279–280), *tinccionem* → *cinccionem* (279.18), *occupat* → *occiput* (284.29), all "our emendation" T notes. OT *summus pontifex* = "high priest" (GLOSSARY *summi pontifices*); OT *pontifex* "pontiff". 5 glossary rows; 16 ledger rows filed. Side-note typos (vestmemts, and and, hishop) fixed in tsv + chunks.
- ⚠ **Disk full during the run** (Mac at 100%, ~820 MB free after deleting scratch crops): one agent write failed and was retried. Check `df -h ~` before resuming; ledger agents download djvu texts.

## ⏸ Pause state (2026-10-12) — where to pick up
- **Translated and per-wave checked through 11-m** (scars, connectives, ledger all closed; ch. 11 done). **12-a … 12-f:** translated, scars fixed on the plates + relatin'd, glossary ruled, ledger rows filed — still owed: **connectives (12-a … 12-f)** (`_connectives/extract.py 13 12-a … 12-f`) and **ledger P12a … P12f** (15 + 15 = 30 rows; split in two runs, rows-13a / rows-13b).
- **Next translation:** `.venv/bin/python scripts/w3/brief.py potestate-pape 12-g 12-h 12-i` → then 12-j … 12-u, comp-a, comp-b (17 chunks left).
- **Cost:** ≈17.5M so far (this session ≈1.8M: 12 chunks + their checks ≈1.43M in agents, coordinator ≈0.4M). Measured ≈0.15M per chunk with checks → remaining ≈2.6–3M → volume ≈20–20.5M.
- **Open, editor's calls (track only):** 11-k ¶5 puts Wyclif's paraphrase of C. 5 q. 5 c. 2 ("deprived of his sword") in quotation marks; the canon says *ligat*.
- **Wanting outside sources:** PG 56 cols. 849–859 (*Opus imperf.*, P11m-2): NOT in ~/patrologia (PG 100–161 only); both archive.org scans (`patrologiae_cursus_completus_gr_vol_056`, `bim_early-english-books-1641-1700_1859_56`) lack those columns. ✅ *Rosarium* (Guido de Baysio): MDZ **bsb00093258** (Venice 1481, 833 images; fetch single pages by IIIF, `https://api.digitale-sammlungen.de/iiif/image/v2/bsb00093258_00NNN/full/900,/0/default.jpg`, no OCR). Orientation: D. 50 ≈ image 150, D. 60–61 = 166, D. 92 = 218, D. 93–94 = 222. P11m-4 closed (D. 93 c. 24 gloss).
- Committed locally; **NOT pushed** (push is Wilson's per-action OK). Site not built or deployed for this volume.
- **FitzRalph *Summa* 1512 complete on disk:** `sources/fitzralph-summa-1512-p{001-100,101-200,201-363}.pdf` (PDF page = scan page − 199 for the last; book XI at scan p. 176 ff.).
- **Wave 12b** (12-a … 12-f, 2 briefs, ≈304K): scars on the plates — the folio mark sticks to a token (`do| tacionem`), a hyphen join can run before a pair row (key `posset de-? esse`), side-note English *is* leaked onto p. 328; *capitulo II* 324.12 and Loserth's "330—352" (309 foot) are the print's. Ledger 12a (P11h … P11j: 12 verified, 1 untraced) and 12b (P11k … P11m: 13 verified, 4 editor, 2 untraced). English emended after the sources: *vanitatem* for *unitatem* (11-j, Gregory/Gratian), *cum quisque voluerit* for *cum quibus* (11-m, Augustine). Connectives wave 12 (11-h … 11-m): 65 / 2 fixed. 15 glossary rows; 30 ledger rows filed (P12a … P12f).
