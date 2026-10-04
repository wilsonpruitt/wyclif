# *De ecclesia* — rulings from the close-out (CLOSEOUT.md)

## RULED 2026-10-04 (Wilson)
- R1 keep (12-d n17: an unidentified incident, not the 1378 killing) · R2 note only (Nicholas III kept in the
  English) · R3 standard names added (07-a n2) · R4/R8 keep `verified`, how-column names the source · R5/R6 keep
  as reported; book-level mapping is enough · R7 English "Boulogne" (16-c) · C: 11-a recast as a syllogism
  ("now" for the minor, C note); the other ~75 doubtful connectives stay as rendered.
- S2 run (58 boundaries on the plates) · S3 run (208 tokenfix rows: 140 real-word, 68 numeral, none plate-read)
  · S1 **closed, not run** (Wilson, 2026-10-04): italics are the editor's call, not the manuscript's; the early
  chunks' quotation bounds stand as rendered. For later volumes italics are tracked, not verified (WORKFLOW stage 5).
- **S2 result (2026-10-04, `_audit/BOUNDARIES-REPORT.md`):** 4 lost words restored (47.5 *Christi etc.*, 95.2 *a*,
  265.1 *et*, 372.2 *tripliciter*) + 3 stops; English/notes follow. **Deferred to stage 10:** 28 false ¶ breaks,
  11 chunk splits inside a sentence, 06-e/06-f *Sed* at 133.26, 5 merged print paragraphs: they need a `vote.py`
  para override and chunk restructuring, and the site's chapter rendering decides how visible they are.
  **Ruled 2026-10-04 (Wilson): the web edition stays one page per part.** A continuous reading text is for a later
  PDF or print edition, where the false breaks and chunk-end splits are joined at build time (the audit report
  `_audit/BOUNDARIES-REPORT.md` says which are false, which are verse/headings), notes renumbered per chapter,
  page markers shown once. Design notes: 23 chapters of 5–12 parts, ~9,000 English words each.

The items as they were put:

## S. Scope questions
- **S1. Quotation bounds by the print's italics in the unreviewed chunks.** The italics rule dates from brief 45
  (chunk 21-g on). Reviews R1 and R2 found 14 mis-bounded quotations in 8 early chunks (quoted by sense: roman
  stretches quoted, italic runs split or left unquoted). The other ~110 pre-brief-45 chunks (01-a…21-f, outside
  the review set) were never checked against the plates' italics. Checking them is plate work, page by page
  (~470 pages). Not started; needs a cost estimate and your go. Tied to the stage-10 question of whether the site
  shows italics at all (front matter says `italics: none` in every chunk).

- **S2. Chunk boundaries that cut a sentence.** 12-c ends at 263.26 mid-sentence (*patet* | *quod hoc est
  contra fidem catholicam*); with 02-f ¶4/¶5 (46.23–24) and 23-i ¶4/¶5 these are left as structure (M5-RESUME
  precedent). On the site a chunk would end on "it is clear". Decide at stage 10: render chapters continuously
  (boundary invisible) or move the boundary.
  Now measured: `scripts/w3/boundaries.py ecclesia` → `text/ecclesia/boundaries.tsv`, 58 ends without a stop
  (43 ¶, 15 chunk; some are verse lines). Reading the 58 on the plates (~1 agent) would find any other lost
  word at a false break like *plus* (46.24). Not started; needs your go.

- **S3. Tokenfix rows that emend the print.** The reviews found 4 rows in `text/ecclesia/tokenfix.tsv` labelled
  "OCR" that in fact corrected Loserth's misprints (263.29 *faciendo*, 270.29 *69*, 424.4 *novam*; plus a lost
  stop) — silent emendations, against the standing rule. Undone in the close-out (print restored, T notes). The
  other ~695 rows were not audited; most are true OCR scars, but any row whose "printed" form is a real Latin
  word (or a numeral) could be the same case. A filtered audit (real-word / numeral rows only, checked on the
  plates) is possible; not started, needs your go.

## R. Translation items (doubtful; left as they are until ruled)
- **R1. 12-d n17 (E12d-6).** The LEDGER verifier reads *occisio religiosi* (267.27–32) as NOT the 1378 Westminster
  killing but an unidentified incident (a monk killed in the church; another's head broken), set against the 1378
  killings. Applied to the note; the English text was not reframed. Confirm or reverse.
- **R2. Nicholas II, not III (E11a-5).** The Westminster bull is Nicholas II's (Kemble IV no. 825; Sawyer 1041, a
  forgery); Wyclif, B and Loserth all say III. Latin and English keep "III" (Wyclif's slip); the note says so.
  Flag it in the English too (e.g. "Nicholas III [read II]")? Default: note only. Same at 10-a (E10a-4).
- **R5. Wyclif's misnumbered cross-references** (E19g-4 c. 27 for c. 26; E22f-2 "second" for first *commentum*;
  E23a-3 "last chapter" fits only in part). Reported in the notes, not emended (the Latin is the print). Default: keep.
- **R7. *Bolonia* → Boulogne?** The philosophy verifier identifies Wyclif's *Bolonia* as Boulogne (see
  `_verify/batch-philosophy.md`). The English still says "Bolonia". Default: "Boulogne" with a note.
- **R8. "Verified" on secondary sources.** E16h-3, E14h-1, E16c-3 rest on secondary literature, not the
  primary text. Default: keep `verified`, the how-column names the source.
- **R6. Book-only mappings not chapter-checked** (wyclif batch, coordinator item 1): 09-b, 09-e, 22-f/g, 10-d
  cross-references now mapped by book (*De civ. dom.* I/III, *De veritate*); their chapters are not checked.
- **R3. Westminster victim's name (07-a n2).** Loserth's *Eulogium* has "Johannes Hawle / Ricardus Shakyll"; the
  standard names are Robert Hauley and John Shakell. Add the standard names to the note? Default: yes, if you agree.
- **R4. Printed authorities.** E12c-6, E13b-5 (1213), E15g-1, E15h-2, E15b-3 dates rest on web pointers
  (Wikipedia/Britannica/abbey site). Printed authorities to cite if wanted: Cox 1911 (sanctuary), PROME,
  Cheney–Semple (Innocent III letters).

## C. Doubtful connectives (left as they are)
~75 *sed/autem* toss-ups (now/and/but), listed under "Doubtful, left as they are" in
`_connectives/RESULTS-01.md` … `RESULTS-09.md`. All 1,313 occurrences outside the review set were checked; 69
changes the card decides were applied. The doubtful ones are defensible as rendered; rule only if you want to.
Notable: 11-a "and [since] the king" (a minor premiss inside a *cum*-clause; needs a recast, RESULTS-04).
