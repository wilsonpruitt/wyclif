# CONVENTIONS — pilot draft, 2026-09-28 (freezes when Wilson approves the pilot)

*Set by the pilots `pilots/wyc-ecclesia-01a.md` (plate-read) and `pilots/wyc-dialogus-01.md`
(Fordham text, collated). These rules govern every chunk in the corpus. Change one only by a
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
  pages (from.line–to.line) · divisions · latin_source · plates · collation · status`.
- `latin_source` is one of `plate-read` or `fordham-collated`. **It is never blank.**
- `plates` gives the archive.org item and leaf range. `catalog/plate_offsets.tsv` holds each
  volume's calibrated leaf↔page offset.

## 3. The Latin: copy-text and transcription

- **Copy-text = the Society edition's printed text**, read from the plate.
- **Fordham text is accepted only after full collation against the plate**, word by word, every
  chunk. No sampling ([[feedback_exhaustive-over-cheap-passes]]). Record the result in `collation`:
  the count of Fordham≠plate discrepancies, each listed in the transcription notes. Fordham's quality
  varies by file: *Dialogus* cap. 1 had zero word errors, while *De officio regis* shows raw OCR
  (`wltfacere`, `Sicul`). A clean first chapter does not license skipping the next one.
- **Spelling as printed**, medieval forms included (*eciam, racio, ymmo, quiditas, ypocritis*), and
  the editor's *u/v, i/j* as printed. Degree-sign ordinals (*LXI°*) are kept.
- **Italics as printed.** The editors italicise quotations. Keep them: they show where Wyclif
  stops speaking and his authority starts.
- **Editor's brackets kept** (*[conse]quendam*). The editor's own emendations ("Correxi") are
  accepted as the text and recorded in the transcription notes.
- **Left out of the reading text:** line numbers, MS folio markers and their asterisks, the
  editor's marginal alinea letters and sub-letters (*a b c*), and pencil marks from readers of the
  scanned copy. Page breaks **are** marked, as `[p. N]` in the Latin and `[N]` in the English, at
  the same word.
- ⛔ **Never correct the printed Latin silently, and never put our own emendation into the Latin
  block.** See §5.

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
