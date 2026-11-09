# CONVENTIONS — FROZEN 2026-09-28 (Wilson's pilot review)

*Set by the pilots `pilots/wyc-ecclesia-01a.md` (plate-read) and `pilots/wyc-dialogus-01.md`
(Fordham text, collated). §3 was revised the same day to the three-witness check; the pilots
predate it and become its acceptance test (PLAN M2). These rules govern every chunk in the corpus. Change one only by a
dated decision recorded in the decision log at the foot of this file, never silently in a chunk.*

**The standing attitude, from Thakkar:** *"Wyclif must always be approached with daggers
drawn."* The two most recent English translations (Penn 2019, Lahey 2013) were published,
reviewed warmly, and turned out to be "worse than useless" (Thakkar, *Vivarium* 58 (2020),
357–83, in `reference/`). Their errors fall into four classes. §§6–9 below are one rule per
class, and every chunk is checked against all four before it is marked done.

---

## 1. Chunk = one printed chapter, split at the editor's own divisions

- One *capitulum*, one chunk, when the chapter is under ~8 Society pages.
- Longer chapters split **only at the editor's own divisions**: Loserth's alinea letters
  (A, B, C… in the outer margin), Pollard's paragraphs, or Dziewicki's sections. Never mid-argument,
  never at a bare page break.
- ⛔ Never take chapter structure from the Fordham `##` headings (PHASE0 finding 6). Structure comes
  from the plate.

## 2. Chunk id, citation, front matter

- **Id:** `wyc-<slug>-<cap>[<part>]`, with the slug from `catalog/volumes.tsv`: `wyc-ecclesia-01a`,
  `wyc-dialogus-01`.
- **Citation = work + Society page.line**, e.g. *De eccl.* 5.11, *Dial.* 2.14. That is how Wyclif
  is cited in the literature, and it is stable across every scan. Archive.org item digits are never
  a citation (PHASE0 finding on `latinworksNN`).
- **Front matter, minimum:** `chunk_id · work_la · work_en · volume_slug · editor · year ·
  pages (from.line–to.line) · divisions · latin_source · witnesses · check · italics · plates ·
  status`.
- `latin_source` is `three-witness` (the normal method, §3) or `plate-read` (the pilots, and the
  fallback). **It is never blank.**
- `witnesses` lists the text witnesses used, by archive.org id plus `fordham` or `tesseract`
  where used. `check` gives the counts from §3's decision table: words accepted without a plate,
  words settled by vote, words sent to the plate, and what the plate said. `italics` is `plate`,
  `fordham` or `none` (§3.6).
- `plates` gives the archive.org item and leaf range. `catalog/plate_offsets.tsv` holds each
  volume's calibrated leaf↔page offset.

## 3. The Latin: copy-text, and how it is established (revised 2026-09-28; B+ from 2026-10-21)

> **From *De benedicta incarnacione* on (Wilson, 2026-10-21): B+.** The words come from a blind
> transcription of the page image (Sonnet), checked word by word against Fordham and the vote. A run that
> neither supports goes to the plate unless both witnesses plainly garble it; a run both witnesses have
> and the transcription lacks always goes to the plate. Still an exhaustive check: every word is compared
> with two independent witnesses. The vote (§3.1–3.4) stays as one of those witnesses. It remains the method
> of record for the volumes already published. Measurement: `chunks/incarnacione/PILOT-LATIN.md`. Procedure:
> WORKFLOW § B+.

**Copy-text = the Society edition's printed text.** We don't re-OCR it. We **check** it: several
independent transcriptions of the same printed page vote word by word, and only the words they
cannot settle go to the page image. Every word is compared, so this is an exhaustive check, not a
sample ([[feedback_exhaustive-over-cheap-passes]]). What it saves is looking at the image where
three witnesses already agree.

*Why:* measured 2026-09-28 on 22,302 triple-aligned words of *De officio regis* (Fordham + the
Princeton OCR + the Boston College 1966-reprint OCR). All three agreed on 93.7%. On 6.0% one witness
was outvoted by the other two, and in every sampled case the majority matched the print. 0.35% was a
three-way split. The Fordham file there is raw OCR, but its errors are not the scans' errors.

### 3.1 Witnesses

- **At least three independent witnesses per chunk.** Independent means a different scan, or a
  transcription not made from the same OCR. Two OCRs of one scan count as one witness.
- Sources, in order of use: the **Princeton scan's OCR** (`latinworksNN`, the primary scan); **other
  free archive.org scans** of the same volume (`catalog/volumes.json` → `other_free_scans`; the 1966
  Johnson reprint is a photo-reprint of the same setting, so its page and line breaks match, but it
  is a separate scan with its own OCR); **Fordham**, where it exists. Fordham is **a witness, not the
  copy-text**. Its files range from corrected (*Dialogus*) to raw OCR (*De officio regis*).
- **Fewer than three available** (Polemical Works I, *Civ. dom.* III tome 2, *Opera minora*,
  *De veritate*): add a **local Tesseract OCR** (Latin model) of the Princeton plates as the third.
  It is free CPU work, run one volume at a time.
- Use the **hOCR** (word boxes), not the plain `_djvu.txt`. The boxes let the main-text column be
  separated from running heads, line numbers, side-notes and apparatus, and give each line's position
  on the page for §3.4.

### 3.2 Alignment

Word by word, per Society page, main text only. Comparison is on a normalised form (case, *u/v*,
*i/j*, punctuation, and ligature and OCR hyphen artefacts). ⛔ **The normalisation is only for
comparing.** The established text keeps the printed spelling (§3.5).

### 3.3 The decision table (refined in M2 against measurement, 2026-09-28; see decision log)

The frozen table below was built from first principles. Running it on real witnesses (the Dialogus
complete, *De ecclesia* 1–5, *Off. reg.* 68–69) showed three things it had not foreseen, and
the rules were refined to meet them. The principle is unchanged: **a disagreement the evidence
can explain mechanically is settled by the evidence; only a real doubt goes to the plate.**

1. **Systematic OCR confusions recur across scans.** Ligature *fi* read as *ii*, *ff* as *tf*, *li* as
   *h*, long-*s* as *b* and so on, so several witnesses can share the *same* non-word (*iilii*,
   *speciah*, *bicut*). "Shared non-word = the print's" was wrong for these.
2. **Layout errors are correlated.** Every scan is a photograph of the same page, so a side-note
   glued to a main-text word (*hectruth*, *Lords*) or a line number read into it (*estis* = *est*
   + 15) recurs in several witnesses at once. Character errors are independent; layout is not.
3. **The Latin hunspell dictionary is too generous** (it accepts *iu*, *dommus*, *nou*, *st*), so
   "real word" alone cannot decide a dispute.

**Before the vote, each non-word vote is attributed to the reading it is evidence for** (`unglue`
in `vote.py`):
- a non-word within **two known OCR confusions** (the list in `vote.py`) of another voter's form is
  a vote for that form, however many scans share it;
- a non-word seen **once** that closely resembles another voter's form (similarity ≥ 0.75) is a
  misreading of it;
- a non-word that is another voter's form **plus ≥ 3 glued letters** is that form with a side-note
  or line number attached.
Targets are real forms, or a non-word the plurality shares (proper names, medieval spellings the
dictionary lacks: *israelis*, *auffert*).

| Rule | Situation | Action | Plate? |
|---|---|---|---|
| R1 | All witnesses agree on a real word | Accept | No |
| R5a | All ≥ 4 witnesses agree on a non-word | Accept: the print's own form (*idemptitas*, *wltfacere*) | No |
| R5 | All agree on a non-word, only 3 witnesses | Plate | **Yes** |
| R2 | Majority real form, every rival a non-word | Accept | No |
| R3a | Majority real form ≥ 3, one lone real-word rival | Accept: a single outlier is OCR noise | No |
| R3b | Majority real form ≥ 3 and ≥ 2× any rival, every real rival an OCR confusion of it | Accept (*dommus*, *nou*; *30* for *3°*) | No |
| R6a | A non-word holds a strict majority of **all** voters, rivals only singletons | Accept: the print's form | No |
| R4a | No majority, but exactly one real form and every other form a known OCR confusion of it (≤ 2) | Accept (*speciah / speciab* → *speciali*) | No |
| DEL | A strict majority of witnesses lack the pivot's word | Drop it; plate only if a real rival has ≥ 2 votes | if so |
| INS | A strict majority of witnesses have a word the pivot lost | Insert it | No |
| R3 | Real-word dispute with ≥ 2 votes on each side (*fide / ride*, *sto / isto*) | Plate | **Yes** |
| R4 | No majority | Plate | **Yes** |
| R6 | A non-word majority short of the R6a test | Plate | **Yes** |
| THIN | Fewer than 3 witnesses aligned here | Plate | **Yes** |
| INS? | ≥ 2 witnesses (not a majority) insert a word | Plate | **Yes** |
| HEAD | A chapter heading (structure is checked once per heading) | Plate | **Yes** |
| NW | An accepted non-word (R5a/R6a) that one known OCR confusion turns into a dictionary word; rare (< 4 in the volume), not a name or numeral | Plate: a shared misreading (*pnncipio*, *supenus*) | **Yes** |
| EDGE | Page edge, outside the anchored alignment (first to last ≥ 3-word match): other scans give no vote; the pivot's real word stands (a non-word goes to the plate as THIN) | Accept the pivot | No |
| TAIL / GAP | The pivot OCR lost whole lines (page foot / mid-page) that a majority of the other scans carry, agreeing fuzzily; not apparatus, not on a neighbouring page | Insert the best-read witness's run | **Yes** |

- **Non-word vs real word** still follows the house rule ([[reference_plate-read-triage]]): a
  non-word is evidence of an error; a real word that reads oddly is the source's until the plate
  says otherwise, and in a real-word dispute the plate decides unless the dispute is explained
  mechanically (R3a, R3b). The lexicon is hunspell Latin tried on classicised variants (*ci→ti*,
  *y→i*, *e→ae*, *michi→mihi*), plus `catalog/lexicon/agreed.txt` (forms ≥ 4 independent
  witnesses have agreed on anywhere in the corpus), minus English side-note words.
- **The print's oddities are kept, never "corrected".** *wltfacere* (*Off. reg.* 69.4) is what the
  plate prints: the MS spelling of *vult facere*. Phase 0 wrongly called it a Fordham error.

**Measured** (Dialogus complete, 23,120 words, 6 witnesses): 89.6% unanimous; 99.0% settled
without a plate; **10.3 plate items per 1,000 words** (~2.4 per Society page, of which ~0.3 are
chapter headings). Numerals (*3°*/*30*) and real-word disputes are most of the rest.

### 3.4 Plate reads: the line, not the word

- `scripts/w3/crops.py SLUG` cuts, for every open queue item, **the line with the line above and
  below** from the page image, boxes the word in red, and stacks eight strips per numbered sheet
  (`text/<slug>/crops/sheet_NNN.jpg` + `.tsv`). The whole middle line is read every time, because
  the normalisation class (the digitised text silently *corrects* the print, and the corrected form
  reads perfectly) lives in the neighbours of the word being checked ([[reference_plate-read-triage]]).
- When a strip is not decisive (italic *t / l*, a degree sign), **zoom the full-resolution page**
  on that word before deciding. ⛔ Never decide on the sense or on the Vulgate. The plate decides,
  and the note says how (e.g. *Dial.* 9.15 *dabitis*: "short ascender with crossbar = t").
- Readings go in `text/<slug>/plate_decisions.tsv` (page · pos · rule · forms · reading · note):
  the print's form **exactly as printed**, `∅` for no word, the full heading text for HEAD. The next
  `vote.py` run applies them. A decision whose voted forms no longer match is reported **stale** and
  re-queued, so a change to the extraction can never silently misplace a decision.
- Every non-R1 decision is logged in `text/<slug>/pNNN.check.tsv`, and the chunk's `check` field
  summarises the log.

### 3.5 What the established text keeps

- **Spelling as printed**, medieval forms included (*eciam, racio, ymmo, quiditas, ypocritis,
  wlt*), and the editor's *u/v, i/j* as printed. Degree-sign ordinals (*LXI°*) are kept.
- **Editor's brackets kept** (*[conse]quendam*). The editor's own emendations ("Correxi") are
  accepted as the text and recorded in the transcription notes.
- **Left out of the reading text:** line numbers, MS folio markers and their asterisks, the
  editor's marginal alinea letters and sub-letters (*a b c*), and pencil marks from readers of the
  scanned copy. Page breaks **are** marked, as `[p. N]` in the Latin and `[N]` in the English, at
  the same word.
- ⛔ **Never correct the printed Latin silently, and never put our own emendation into the Latin
  block.** See §5.

### 3.6 What OCR cannot supply: italics and structure

- **Italics.** The editors italicise quotations, and that shows where Wyclif stops speaking and his
  authority starts. OCR does not carry italics. Take them from Fordham where it exists (its data
  has `<i>` tags); otherwise mark `italics: none`. The translator then identifies quoted matter
  from the sense and the editor's source notes, and marks it in the **English**. Italics in the
  Latin block are added from the plate only when a chunk is otherwise being read there.
- **Structure** (paragraphs, chapter headings, the editor's alinea letters) comes from the hOCR
  layout (indentation, centred capitals, the margin column), checked against the plate at each
  chapter opening. ⛔ Never from the Fordham `##` headings.

### 3.7 The sense check stays

The vote establishes what the page prints; it cannot tell whether the print makes sense. The
translator still reads the Latin with daggers drawn (§5). If the established text makes nonsense,
read the plate and the apparatus, and budget for it.

### 3.8 Plate-read (fallback)

Where hOCR is unusable for a page (a bad scan, or a table or diagram in *De logica*), read the
plate for that page and set `latin_source: plate-read` for that chunk.

## 4. The editor's layers: side-notes, sources, apparatus

- **Side-notes** (the editor's English marginal summaries) are PD and go in their own section,
  verbatim, keyed to page.line and credited ("Loserth's side-notes"). They are the free navigation
  layer. ⛔ They are **not** our translation and are never quoted as Wyclif.
- **Source footnotes:** the editor's identifications are kept in our notes. Where a Society
  reference is out of date, give the modern reference and say it is ours.
- **Apparatus:** not transcribed wholesale; it stays on the plate, which every chunk links. A
  variant is cited in our notes **when it bears on the sense or on a construal**, with the editor's
  sigla. A medieval marginal gloss printed in the apparatus (e.g. MS B at *Eccl.* 3.24) gets a
  note when it shows how an early reader construed the text.
- **Scripture references in the printed text:** the chapter is Wyclif's. **The verse numbers are
  the editor's**, since Bibles were first divided into verses in the 1550s. The English gives
  modern references (Isa. 61:10), and this sentence stands once in each work's headnote.

## 5. ⭐ Daggers drawn: when the printed Latin is wrong

The Society editions are not clean. Thakkar documents omitted negations (*De logica* III 169:
"omne necessarium ⟨non⟩ absolute…"), misreadings (*recidive* for *recitative*, *redemit* for
*redeunt*), and editors who printed a base manuscript's error against the others (Buddensieg
especially, *Polemical Works* II 419).

1. If the Latin as printed makes nonsense, or makes Wyclif say something outrageous,
   **check the apparatus on the plate first**.
2. If a reading in the apparatus gives the sense, **translate that reading** and write a
   **T** note saying so, citing the siglum.
3. If nothing in the apparatus does, and an emendation is compelling, translate it and write a
   **T** note that gives the printed reading, the emendation, and the reason, marked *(our
   emendation)*. Where a published emendation exists (Kilcullen's for *Civ. dom.* I, Thakkar's
   anywhere), cite it rather than re-deriving it.
4. If neither holds, **translate the printed text** and flag it: never smooth nonsense into sense.
5. **Risk by editor:** Buddensieg (*Polemical Works*, *De veritate*) highest; Dziewicki's
   *De logica* high (T. p. 364 n. 23). Give these volumes a slower collation pass.

## 6. Error class 1 — terminology (T. pp. 364–5)

`GLOSSARY.md` governs. One term, one rendering, every time. Opposable pairs stay opposable
(*simpliciter / secundum quid*). If a word looks like a technical term, look it up in the glossary
before rendering it. If it isn't there, add it by recorded decision and don't improvise.

**The dikaiosune rule (Wilson, 2026-09-28, from the Jeong project).** Some words hold together senses
that English splits between two words, the way δικαιοσύνη covers both "righteousness" and "justice"
(*inconveniencia*: the absurd consequence in argument, the disorder that follows in affairs). Don't let
the English split decide the meaning. The glossary marks such a term **CONTEXTUAL**: choose the
English by context each time, and write a **C** note at its first occurrence in each chunk and
wherever the context leans toward the other sense, saying what the Latin holds together and which
sense the English chose. The rule is for real two-sense words only, not a licence to vary a fixed
rendering.

## 7. Error class 2 — the connectives that carry the argument (T. p. 365)

⛔ **An argument-bearing connective is never omitted and never turned into filler.**

| Latin | English | Never |
|---|---|---|
| enim, nam | for | "now", "indeed", "paradoxically" |
| ergo, igitur, ideo | therefore, so, then | "now", "and", "nevertheless", "indeed" |
| sed / autem (marking the minor premiss or the next step) | now | (omitted) |
| sed / autem (adversative) | but | (omitted) |
| autem (continuative) | and | (omitted) |
| cum (concessive / causal) | although / since | "whenever", "indeed" |
| tamen | yet, nevertheless | "therefore" |
| item | again, also (announcing the next argument) | "now", "indeed", "so" |
| principaliter (with *secundo* etc.) | the second main argument… | reading it with the verb |
| per idem | by the same token | "in the same way" |
| ad hoc quod | for it to be the case that | "to whatever" |
| arguitur ad idem per hoc quod | the same conclusion is argued on the grounds that | |
| Et tantum (sufficiat) de | so much for | |
| ymmo | indeed, rather (correcting upward) | (omitted) |
| queso | I ask | (omitted) |
| patet; constat | it is clear; it is evident | |

"Now" is the English logic-book word for the minor premiss ("all men are mortal; now Socrates is a
man"). Reserve it for that job.

## 8. Error class 3 — ordinary words (T. p. 366)

Look up every word whose classical sense and Wyclif's sense might differ. The glossary's §D is the
running list (*sciolus*, *sensibilis*, *infidelitas*, *ignorare*…). Add to it every time one catches
you.

## 9. Error class 4 — syntax (T. pp. 366–8)

- **Construe before rendering.** Find the main verb, the subject, and what every relative and
  genitive depends on. Don't reorder clauses until the construal is fixed.
- **Keep scholastic word order where it carries logic** (*alicuius hominis non omnis filius* = "of
  some man not every son"). Quantifier order is meaning.
- **Keep Wyclif's periods where English tolerates it.** He argues in long sentences with the
  reasons stacked; flattening them hides the argument.
- **A doubtful construal is never chosen silently.** Translate the likelier reading, and write a
  **C** note giving the Latin, the alternative, and why (pilot: *Eccl.* 1.2–4, *fides est
  ecclesia*).
- Supplied words go in `[square brackets]`, sparingly. They mark English that has no Latin behind
  it.

## 10. Scripture

- Wyclif's Bible is the Vulgate. **Where his quotation agrees with the Clementine Vulgate, the English
  follows the Douay–Rheims (Challoner) wording**, archaisms included (*thee*, *falleth*). That keeps
  house consistency with glossa.wrootpress.com.
- **Where he departs from the Vulgate** (conflation, adaptation, memory), translate *his* Latin and
  write an **S** note giving the Vulgate. Pilot: *Eccl.* 2.30, Isa. 61:10.
- Where he paraphrases rather than quotes, translate the paraphrase and don't restore the text.

## 11. Notes: numbered, anchored, typed

⛔ **Every note gets a number, and its marker goes in the English in the same edit that writes the
note.** Never a note keyed by catchword, and never "markers later" (Wilson's standing rule; see
*Church in Palestine*, 796 unanchored notes).

- Markdown footnotes `[^n]`, numbered from 1 in each chunk.
- **Glossary tags, not glossary notes** (decided 2026-09-28). A term whose only need is its
  glossary definition gets an inline tag on its first occurrence in each chunk:
  `[quiddity]{g:quiditas}`. The key is the Latin form as it appears in its `GLOSSARY.md` row, in
  lower case with hyphens (`fides-formata`, `vicarius-deitatis`). The site renders it as a hover
  gloss from the glossary. **A term gets a numbered G note only when the note says something about
  *this* passage**: a construal, an escalation, a false friend at work, a pair the argument turns
  on. Tags go on every §A–C term the chunk uses.
- Each note opens with a **type letter**:
  - **T**: text (reading, variant, emendation)
  - **C**: construal (a syntactic choice and its alternative)
  - **G**: glossary (a term's first occurrence in the work, or a hard rendering)
  - **S**: source (scripture, patristic, Aristotle, canon law)
  - **R**: reception and context (Hus, Constance, Lollards, the editor's era)
- **Density:** as many as the text needs, no more. After the tag conversion the pilots run about
  one note per 45–50 Latin words. First chapters are dense because they carry a work's first
  occurrences; later chunks should thin out.
- Short, and factual first. A note says what the Latin does, then stops.
- **A source identification is not published until it is in `LEDGER.md` with a status.** An
  identification from memory is `to-verify` until checked against a text. The editor's own
  identifications are `editor`.

## 12. Headnote: one per work, four movements, ~200 words

It sits in the work's first chunk only, in this order:

1. **Occasion:** date, circumstance, place in the corpus.
2. **The text:** editor, year, manuscripts (with sigla), our copy-text, how reliable the edition is.
   It includes the verse-number sentence (§4).
3. **The move:** how the opening builds the argument, not what it concludes.
4. **Where it is answered:** Hus, Constance, opponents, or explicitly "nowhere yet traced".

⛔ A reading guide, not an evaluation. No modern theology, no argument for the edition's thesis.
Any claim not yet verified carries `[verify]` until the ledger clears it, and **a chunk with an
open `[verify]` is not publishable.**

## 13. What a finished chunk contains, in order

Front matter · Headnote (first chunk of a work only) · for each editor's paragraph: the Latin
(blockquote, `[p. N]` breaks), then the English (`[N]` breaks, note markers) · the editor's
side-notes · Notes · Transcription notes (plate readings, collation, the editor's corrections).

## 14. The four-class check (done before `status: done`)

- [ ] Every glossary term rendered per `GLOSSARY.md`, and every new term added by decision.
- [ ] Every *enim / nam / ergo / igitur / sed / autem / item / cum / tamen / per idem* accounted
      for, none omitted.
- [ ] Every word with a classical/medieval gap looked up (§8).
- [ ] Every sentence construed; doubtful ones carry a **C** note.
- [ ] Every note anchored; every source identification in the ledger; no open `[verify]`.
- [ ] The Latin's check log is complete: every R3–R6 word has a plate resolution, and `check` is
      filled in.

---

## Decision log

| date | decision | by |
|---|---|---|
| 2026-09-28 | §3: the Latin is established by the three-witness check, not full plate reads | Wilson |
| 2026-09-28 | Scripture in English: Douay–Rheims (Challoner) where Wyclif quotes the Vulgate exactly (§10) | Wilson |
| 2026-09-28 | *Presciti* → "the foreknown", explained per work; never "the reprobate" (GLOSSARY §A) | Wilson |
| 2026-09-28 | *Dominium* → "lordship"; titles *On Civil Lordship*, *On Divine Lordship* (GLOSSARY §B) | Wilson |
| 2026-09-28 | Note register: glossary tags + hover glossary; G notes only for passage-specific points (§11) | Wilson |
| 2026-09-28 | CONVENTIONS and GLOSSARY frozen on pilot review | Wilson |
| 2026-09-28 | GLOSSARY: 15 terms added from wave 1 after a census (*sentencia* teaching, *evidencia* evidence, *reditus* revenue(s), …) | Wilson |
| 2026-09-28 | GLOSSARY: 9 terms added from *Dialogus* batch A, after a census (*ex fide* and *limitare* split by use) | Wilson |
| 2026-09-28 | §6: the dikaiosune rule for two-sense words (CONTEXTUAL entries); first case *inconveniencia* | Wilson |
| 2026-09-28 | GLOSSARY: 12 terms added from wave 2 after a census (*opinio*, *suffragia*, *canonizare*, *litere fraternitatum*, …) | Wilson |
| 2026-09-28 | GLOSSARY: 13 terms added from wave 3 after a census (*infidelis*, *cautela*, *apocrifa*, *citra fidem*, …) | Wilson |
| 2026-09-28 | GLOSSARY: *regnum* → "kingdom" in every sense, not "realm" (ch. 18 conformed); 15 more wave-4 terms after a census | Wilson |
| 2026-09-28 | GLOSSARY: *ordinacio* ordinance / ordination (sacrament) by referent; *oratores* bedesmen; *ingratus* displeasing (to God); 13 more wave-5 terms | Wilson (on Opus's recommendations) |
| 2026-09-28 | **Glossary rulings delegated.** From wave 6 the coordinator rules new-term proposals itself, by census and the dikaiosune rule (§6): one term one rendering; a split decided by referent where the senses are distinct things, CONTEXTUAL only where the word holds them together. Rulings are logged here and reported to Wilson after each wave; he may overturn any | Wilson |
| 2026-09-28 | GLOSSARY: wave-6 terms (*insensibilis* split by referent, *globus* band, *secularis* a secular, …; see `chunks/dialogus/_reports.md`) | Opus (coordinator, delegated) |
| 2026-09-28 | GLOSSARY: wave-7 terms (*repplicacio* split by referent, *castra caynitica* Caim's castles, *objectum* objection, …; see `chunks/dialogus/_reports.md`) | Opus (coordinator, delegated) |
| 2026-09-28 | GLOSSARY: wave-8 terms (*predicamentum* category, *infidelis* split by construction, *temporales domini* temporal lords, …; see `chunks/dialogus/_reports.md`) | Opus (coordinator, delegated) |
| 2026-09-28 | §2: an unnumbered section takes a short Latin tag for `<cap>` (`wyc-dialogus-epil-a`), and parts of a split section a hyphenated letter | Opus (M3), mechanical |
| 2026-09-28 | §3.3 refined in M2 against measurement: non-word attribution (OCR confusions, glue, singletons); R3a/R3b/R5a/R6a/DEL/INS/THIN/HEAD; §3.4 crop sheets + decisions file. Principle unchanged | Opus (M2) · **confirmed by Wilson 2026-09-28** |
| 2026-09-30 | §3.3 for M5 (*De ecclesia*): R4a (one real form, the rest its OCR confusions: 411 settled, sample all correct) and TAIL/GAP (lines the pivot OCR lost, carried by the other scans, always plate-read); the vote runs over the body only (`last_page`, index excluded). Also EDGE (the other scans' window slack had voted the neighbouring page's words at page starts: p. 297 *dat* for *recipiunt*, pp. 341, 373); plate decisions now key on the pivot's token and always apply. Also NW (the majority-error sweep folded into the vote) and `agreed.txt` no longer vouches for a form one OCR confusion from a dictionary word (*ahquis*). Plate queue 3,271 → 1,931. Principle unchanged: a real-word dispute still goes to the plate | Opus (M5), mechanical — for Wilson to confirm |
| 2026-10-02 | Wilson, "recommendations yes": (1) *color* → "colour" (plausible ground), C note per chunk; (2) Loserth's printed text governs, his emendations included, unless it will not construe; A₁ alone never outweighs the print; T note for every departure (02-c 34.20 and 02-d 38.1 returned to the print); (3) our emendations where the print gives no sense stand with T notes (*austrina* 49.18, *quam* 11.15, "[Roman]" 15.22); (4) the Clement at 37.21 stays open in the note; (5) the verifier may fetch Friedberg's *Corpus iuris canonici* from archive.org (read-only) to check *Unam sanctam* and other canon-law wording; (6) the coordinator's glossary rulings of 2026-10-01/02 confirmed; (7) the "now" rule as clarified in the card (minor premiss, or the step that brings a new premiss; a continuing *autem* is "and"); (8) vote.py stops trusting `agreed.txt` from the NEXT volume (*De officio regis*), not *De ecclesia*. |
| 2026-10-21 | §3: **B+** adopted for *De benedicta incarnacione* and every later volume: blind Sonnet transcription is the text, Fordham + the vote check it (`scripts/w3/bplus.py`); stages 3/3b/4/4b retire for B+ volumes. Pilot pp. 3–12: blind 0 word errors / ~2,780 at 9.4K tok/page; correct-Fordham 1 kept error at 11.2K; vote+plate 30 errors at 18K | Wilson |
| 2026-11-06 | GLOSSARY (*De eucharistia* prol-a review): *solvere / dissolvere* (an objection) both "resolve"; the 13 mode adverbs one row and one word each (*sacramentaliter* … *dimensionaliter*; *realiter* never "actually", *vere* never "really"); *sentencia (verborum)* "sense" as a separate row, the CONTEXTUAL row unchanged. With them 23 delegated rows (38 new rows in all) for the eucharistic vocabulary (`chunks/eucharistia/_review/REVIEW-prol-a.md` (b)) | Wilson (3) · Opus (coordinator, delegated) |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 1, prol-b–01-a; coordinator, delegated): 12 rows — *cultores accidencium / signorum* "worshippers of accidents / of signs", *inpanacio* "impanation", *cognacio* "kinship", *claritas* (glorified body) "clarity" (agent proposed "brightness"; overruled for the technical dowry), *sumpcio* "reception", *missantes* "mass-priests", *pontifex* (Christian bishop) "pontiff", *epikeya* "epikeia", *incompetens / incompetencia* "unfitting / unfittingness", *locucio tropica* "tropical speech", *Doctor Communis* "the Common Doctor", *multitudo* (of one body) "multitude". Conformed in prol-b, prol-c, 01-a. |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 2, 01-b–01-d; coordinator, delegated): 9 rows — *tegumentum* "covering", *fractio / fractura* "breaking", *species* (of bread and wine) "species", *sensus communis* "the common sense", *laudative / effective* "by way of praise / of effect", *sensacio* "sensation", *figurare* "figure" (one word keeps the prefigure/shape pun), *conus* "apex", *supponere pro* "stand for". Wilson confirmed ("confect works"): *conficere* beside *consecrare* (*consecrat et conficit*, 16.10) "confect", so the pair stays two; elsewhere "consecrate" as ruled. Tag-key hyphen rule added to the card. |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 3, 01-e–02-b; coordinator, delegated): 7 rows — *sacer / sacrare* "sacred / hallow", *sacramentum tantum* "a sacrament only", *peregrinacio* "pilgrimage", *sensualiter* "sensually" (Berengar's oath; apart from *sensibiliter*), *inprecative* "by way of imprecation", *sentire* (an opinion) "hold", *predicacio figurativa* "figurative predication". 01-e keeps "confect" throughout: 27.20 glosses Jerome's *consecrat*, 28.22–29.9 sets the verbs against each other. |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 4, 02-c–02-e; coordinator, delegated): 11 rows — *canoniste* "canonists", *conversio* (eucharistic) "conversion", *loyca* (of speaking) "logic" (conformed back to prol-a, 01-e, 02-a, 02-b), *mixtum* "mixed body", *veraciter* "verily" (apart from *vere*), *describere* "define", *expositorie* (of preaching) "by way of exposition", *elicere* "elicit", *feria* "day of the week", *cognacio* (family) "kindred", *pius pater* "loving father". Departures from the print accepted under the card: 44.2 *Factus* → "touched" (Gen 6:6 and Wyclif at 40.17, 46.2), 44.8 *ab inusu* → C *ab usu* (print will not construe). 45.21–22 *serenitas* kept (no variant; Wyclif's own word at 45.20). *virtus* among God's attributes "virtue" beside *potencia* "power" (C note). |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 5, 03-a–03-c; coordinator, delegated): 10 rows — *anichilacio* "annihilation", *desicio* "ceasing", *illusio* "illusion", *aliquitas* "somethingness", *cedere (in)* "give way (into)", *informacio* "informing", *linire* "smear (on)", *accidens predicamentale* "accident of the categories", *revera* "in truth" (apart from *vere*), *irregulariter* "irregularly". Conformed back through the volume only where the paragraph's Latin has the term (5 tags reverted by that check). 63.7 *univoce sufficimus* and 64.10 *substancia* kept as printed (both construe). |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 6, 03-d–03-f; coordinator, delegated): 7 rows — *decretalis* "decretal" (conformed back, Latin-checked), *principaliter / principalitas* (the body's presence) "principally / principality", *contiguacio* "contiguity", *pedalitas* "foot-length", *veritas predicamentalis* "truth of the categories" (agent's "categorial truth" changed to match *accidens predicamentale*), *calculatorius* "calculatory", *ex tibi / sibi dubio* "for all you / he knows". Departures accepted: 68.13 Loserth's own *recte: contiguacionem substancie*, 69.18 ABCD *quo* (print will not construe). Plates: 66.22 *a*, 69.4 *quante* as printed. |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 7, 03-g–04-a; coordinator, delegated): 9 rows — *convincere / conviccio* "prove conclusively / conclusive proof" ("convict" of a witness; conformed back in 03-d, Latin-checked), *armatura* "armament", *transaccidentacio* "transaccidentation", *transinferioracio / transsubieccio*, *baptiste signorum* "baptizers of the signs", *concomitanter* "concomitantly", *extense loquendo* "speaking in an extended sense", *esse situale / intencionale / potenciale*, *divinitus* "divinely"; *singulariter* made CONTEXTUAL ("in a singular way" where "alone" will not construe). Phil 3:20 adapted by Wyclif (*conversacio apostolorum*): his Latin translated, glossary "manner of life" kept. 79.9, 80.1, 85.6 as printed (vote-supported). |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 8, 04-b–04-d; coordinator, delegated): 9 rows — *sensus* (of words) "meaning" (apart from Wilson's *sentencia (verborum)* "sense"; bodily *sensus* and *sensus literalis* stay "sense"), *interpolatus / interpolacio* "interrupted / interruption", *famosius* "as best known", *quintimembris* "fivefold", *methonomatice* "metonymically", *organisare* "form (sounds) with the organs", *accepcio personarum* "respect of persons", *dies artificialis* "the artificial day", *plaga* "region". 88.4 *Exodi XII*, 89.18 *interpollacio*, 92.31 *omnis isti*, 96.10 *ait supra* as printed (OCR = transcription). ⚠ No nested brackets inside a tag (`[a [b] c]{g:k}`): the site cannot render them. |
| 2026-11-07 | GLOSSARY (*De eucharistia* wave 9, 04-e–04-g; coordinator, delegated): 9 rows — *consecracio* "consecration" (and *confeccio* set against it "confecting", following Wilson's "confect"), *curia Avinonica*, *insensibiliter* "imperceptibly", *locus a maiori* "the topic from the greater", *tropus* "trope", *pertinenter* "fittingly", *essencialiter* "essentially", *noticia confusa / distincta* "indistinct / distinct knowledge", *opinative* "as an opinion"; *per se* made CONTEXTUAL (spatial "apart, by itself", 104.16). |
| 2026-11-07 | *De eucharistia* wave 10 (04-h–05-a): **117.11 ABCD *glossa Bernhardi* adopted for the print's *Beringarii*** (coordinator, under the card: Wyclif pairs it with *glossa ordinaria decretorum*, the two ordinary glosses; Berengar wrote none, so the print gives no sense). 119.8 *capitulo . . .* Loserth's own gap, kept. GLOSSARY 9 rows (delegated): *ponderositas / ponderosum*, *bonitas naturalis / moralis*, *suscipere magis et minus*, *locucio effectiva*, *relacio ydemptitatis*, *analogum*, *questio si est / quid est*, *commenta scripture*, *denarius* (coin) "penny". |
| 2026-11-07 | *De eucharistia* wave 11 (05-b–05-d): 120.26 *avis* kept (a parrot uttering the words makes sense; Loserth's *rectius anus* in a T note); 128.21 *humiliacionem*, 129.8 *epistolatus* (plate) as printed; 130.20 *Es istis* is a misprint on the plate, translated *Ex* (our emendation, T note). GLOSSARY 8 rows (delegated): *verba sacramentalia conversiva*, *concomitancia*, *provecciores doctores*, *coefficiencia*, *dogmatisare* "teach as dogma", *universitas sua* "his universe", *bonificacio* "bettering", *mistice* "mystically" (mode adverb); conformed back, Latin-checked. |
| 2026-11-07 | *De eucharistia* wave 12 (05-e–05-g): departures accepted 134.17 C *cuilibet*, 140.27 C corr. *ponunt*; 142.11 stop after *suam* a fleck (plate n213), removed (bplus 0). GLOSSARY 11 rows (delegated): *figuracio*, *neutraliter / adiective*, *naturalitas obediencialis*, *actuacio*, *accidentalitas*, *quantitas successiva*, *corpus mathematicum*, *fantasiare* "fancy", *insolidus* "unsolid", *pseudofrater* "false friar", *ydolatrare* "idolatrize"; *impanacio* added to the *inpanacio* row; *viare* conformed to the *viator* row. Nested-tag scan (Python, volume-wide): 2 found and fixed (05-e, 03-b page marker). |
| 2026-11-07 | *De eucharistia* wave 13 (05-h–05-j): 154.4 stop before *et* a red ink fleck (plate n225), removed (bplus 0); 147.1 *amiccione* kept (A marg. *annichilacione* in a T note). GLOSSARY 10 rows (delegated): *transaccidencia*, *ubi / ubicans*, *inpossibilitare*, *utrobique* "on both sides" (conformed back through 6 chunks, Latin-checked), *localiter*, *conversivus*, *fasciculus accidentis*, *yronice*, *pertinencior*, *pictacia* "patchwork". |
| 2026-11-07 | *De eucharistia* wave 14 (05-k–06-b): **164.4 *unitatoriam* → *imitatoriam*** (our emendation: no variant, word unattested, the same heads at 158.23 read *imitatoriam*, the sequel speaks of *imitacio*); 163.9 Loserth's foot *cap. L* read on the plate; side-note 162.23 rejoined, *tor* → *for* (also in `sidenotes.fixed.tsv`). GLOSSARY 7 rows (delegated): *katholicacio*, *pena talionis*, *corpus dominicum* "the Lord's body" (conformed back through 9 chunks, Latin-checked), *in circulo*, *signum nature* "instant of nature", *inpastare* "knead", *generancia* "begetting". |
| 2026-11-07 | *De eucharistia* wave 15 (06-c–06-e): 06-c is Gregory throughout, marked as a continued quotation (opening quote per ¶, closing at 169.26, inner scripture in single quotes); side-note 169.26 moved to 06-d (169.27). **175.19 *maximum hereticum* → *Maximinum*** (our emendation: the work is *Contra Maximinum haereticum*); 176.18 *ant* a misprint for *aut* (plate). GLOSSARY 4 rows: *nominacio (baptismatis)*, *paplardus*, *cultor / cultus (sacramenti)*, *adopcio* "choice". **Convention:** a quotation that runs on across ¶s opens each ¶ with a double quote and closes only at its end; quotations inside it take single quotes. |
| 2026-11-07 | *De eucharistia* wave 16 (06-f–06-h): plates: 184.14 raised fleck after *ponderosum* removed (bplus 0); 189.27 *virtutas* a misprint (→ *virtutes*); 182.24 Loserth's D reading has no lemma. GLOSSARY 9 rows (delegated): *suscepcio (sacramenti)* "receiving", *usus (ecclesie)* "use", *sanctificacio*, *ponderacio* "weighing", *cifra* "cipher", *cordatus* "stout-hearted", *pertinaciter*, *ineptus*, *exsufflare* "blow out". |
| 2026-11-07 | *De eucharistia* wave 17 (07-a–07-c): 190.19 *equale* kept (construes; ABCD *essenciale* in a note). Side-notes on p. 192 re-placed from the plate (n263): 192.1 "+" an OCR scar; *Yet identification…* → 192.13; *Absurdities…* → 192.26 (also `sidenotes.fixed.tsv`); 196.4 garbled-looking but verbatim. GLOSSARY 5 rows (delegated): *ydemptifice* "by identification" (apart from *ydemptice*), *universitas* (bare) "the whole universe", *qualitas prima*, *subiectare*, *eukaristia* "the Eucharist" (⚠ PROVISIONAL capital, Wilson to rule; 36 lower-case in the English not yet conformed); *protestacio* row extended to Berengar's confession. |
| 2026-11-07 | *De eucharistia* wave 18 (07-d–07-f): 205.5 *false quantitatis* and 210.20 *excedunt* kept as printed (no variant; plate n276 for 205.5; flagged, not smoothed). GLOSSARY: *fantasticus* made CONTEXTUAL (imaginary / phantastic of the faculty); *illacio* (logical) "illation" split from *illacio mali*; *visio corporalis / ymaginaria / intellectualis* and *visio intuitiva / abstractiva / enigmatica*. |
| 2026-11-07 | *De eucharistia* wave 19 (07-g–07-i): 216.20 Loserth's foot reads *dist. XXI* (plate n287), note corrected; 220.13 *conveniencia* kept "agreement" per the row (Loserth's side-note paraphrases). GLOSSARY 10 rows (delegated): *secta signorum*, *invinacio*, *proditorius seductor*, *immolacio*, *locus a completa similitudine*, *diffinitive*, *sensus tropicus*, *contentive / causaliter / subiective / obiective*, *rima* "chink"; *singulariter* gains "in the singular" (grammar). |
| 2026-11-07 | *De eucharistia* wave 20 (07-j–08-a): 229.24 *sanguinis* (plate n300) → *sanguis*, our emendation (the genitive will not construe); side-notes 227.5 (fleck) and 228.24 (*o* → *of*) fixed (also `sidenotes.fixed.tsv`). GLOSSARY 9 rows (delegated): *glossa / glossator*, *inpanans* "the impanator", *verba adiectiva*, *multiplicacio corporis*, *predicatum infinitum / finitum*, *demultiplicare*, *qualitas secunda*, *corea* "ring-dance", *cilba* "board". |
| 2026-11-07 | *De eucharistia* wave 21 (08-b–08-d): 239.26 *piimo* → *primo* (broken r on plate n310; bt fixed, bplus 0); departures accepted: 247.20–21 E *synodochice* (print *synonymice* gives no sense), 246.3 *ticionis* (our emendation; Loserth queries the print); 08-c n13 aligned with Kprolb-11 (Gregory of Tours, not Paulinus). GLOSSARY 9 rows (delegated): *immediatus / immediacio*, *infinicies*, *dos subtilitatis*, *non communicans*, *simultas adequacionis / inmediacionis*, *principative*, *situaliter*, *corulus columpnaris*, *ioculacio*. |
| 2026-11-07 | *De eucharistia* wave 22 (08-e–08-g): departures accepted: 255.3 C *angelico* (print *evangelice*; Loserth *rectius*); **256.33 *commune evangelium* → *evum*** (our emendation: the same *ev-* confusion; no variant). GLOSSARY 9 rows (delegated): *evum* "aeviternity", *evitas* "aeveity", *vicissitudo* "alternation", *mora* "abiding", *punctale*, *humidum cibale*, *argumentum temptativum*, *creancia*, *precavicio*. |
| 2026-11-07 | *De eucharistia* wave 23 (08-h–08-j): 267.15–16 ABC *quandalitatem* (print *quandamlitatem*, not a word; Loserth prints *quandalitas* at 268.6); 268.6 stop after *mensurantur* restored (plate n339; bplus 0). GLOSSARY 9 rows (delegated): *intuicio*, *quando* "the when", *quandalitas* "whenness", *eviternitas* "eviternity", *punctalitas*, *linea girativa*, *diuturnitas* "length", *sollempnior* "more eminent", *sectivagus*. ⏸ Wilson: pause after this wave (2026-11-07). |
| 2026-11-07 | Wilson: **"Eucharist"** capitalised as the sacrament's name (unlike *ecclesia* "church", which stays lower case because Wyclif's church is often the body of the predestined); the adjective *eucharistic* lower case. All lower-case *eucharist* in the *De eucharistia* English conformed. |
| 2026-11-09 | *De eucharistia* wave 24 (09-a–09-c): OCR scars fixed in `bt/` (logged in `bt_normalised.tsv`; bplus queue 0): 272.21 *catholicus*, 273.31 *itaque*, 276.7 *ut*. Plate-checked: 275.7 the print reads *Medium magnum quippe* (n346): kept in the Latin, left out of the English (T note; DE *Meum*); 280.6 the print reads *immediate* (n351) against codd. *quo mediante est*. 280.23 print *concludit* (A margin) kept against A text + BDE *coniungit* (T note). GLOSSARY 5 rows (delegated): *inpeccabilis*, *secta signa colencium*, *informacio (ecclesie)* "instruction", *sollempnius*, *poletici*; *Asiani*, *senex* no row. |
