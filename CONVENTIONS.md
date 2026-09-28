# CONVENTIONS — pilot draft, 2026-09-28 (freezes when Wilson approves the pilot)

*Set by the pilots `pilots/wyc-ecclesia-01a.md` (plate-read) and `pilots/wyc-dialogus-01.md`
(Fordham text, collated). §3 was revised the same day to the three-witness check; the pilots
predate it and become its acceptance test (PLAN M2). These rules govern every chunk in the corpus. Change one only by a
dated decision recorded here, never silently in a chunk.*

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

## 3. The Latin: copy-text, and how it is established (revised 2026-09-28)

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

### 3.3 The decision table

| Rule | Situation | Action | Plate? |
|---|---|---|---|
| R1 | All witnesses agree | Accept | No |
| R2 | One witness outvoted, and its form is a **non-word** | Accept the majority | No |
| R3 | One witness outvoted, but **every competing form is a real word** (*humani / humane*, *sum / sim*, *quod / quid*) | Plate decides | **Yes** |
| R4 | No majority (three-way split) | Plate decides | **Yes** |
| R5 | All agree on a **non-word** | Plate decides; never "correct" on sight | **Yes** |
| R6 | The majority form is itself a non-word | Plate decides | **Yes** |

- **Non-word vs real word** follows the house rule ([[reference_plate-read-triage]]). Corpus
  frequency settles non-words; it is worthless for real words. A real word that reads oddly is the
  source's until the plate says otherwise. The lexicon test is the corpus itself: a form counts as
  real if it is attested in agreeing positions in at least two volumes, or is in a standard Latin
  wordlist.
- **R5 is where the print's own oddities live.** *wltfacere* (*Off. reg.* 69.4) is what the plate
  prints: the MS spelling of *vult facere*. Phase 0 wrongly called it a Fordham error. A form that
  looks corrupt may be the source's, and only the plate can say.

### 3.4 Plate reads: the line, not the word

- A plate read is a **crop of the line with the line above and below**, fetched by its hOCR box
  (archive.org IIIF region request, or a local crop), never the whole page. The whole line is read
  every time, because the normalisation class (the digitised text silently *corrects* the print,
  and the corrected form reads perfectly) is found in the neighbours of the word being checked
  ([[reference_plate-read-triage]]).
- Every non-R1 decision is logged in `text/<slug>/pNNN.check.tsv` (position · the witnesses' forms ·
  rule · resolution · plate y/n), and the chunk's `check` field summarises the log.

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
- Each note opens with a **type letter**:
  - **T**: text (reading, variant, emendation)
  - **C**: construal (a syntactic choice and its alternative)
  - **G**: glossary (a term's first occurrence in the work, or a hard rendering)
  - **S**: source (scripture, patristic, Aristotle, canon law)
  - **R**: reception and context (Hus, Constance, Lollards, the editor's era)
- **Density:** as many as the text needs, no more. The pilots run about one note per 30–40 Latin
  words, because first chapters carry every first-occurrence gloss. Later chunks should thin out.
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
