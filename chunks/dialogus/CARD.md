# TRANSLATOR CARD — one *Dialogus* chunk, one agent

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Read it, then `GLOSSARY.md` (all of it; it is short), then your scaffold. Consult CONVENTIONS.md
only when the card sends you there. Work in `~/wyclif`. Wyclif is approached with **daggers drawn**:
the two most recent English translations were "worse than useless" because of four error
classes (below). Your English must survive a hostile reader with the Latin open.

## Work lean (cost is per tool call: each call re-sends your whole context)

Aim for **about 10 tool calls** in all:
1. One call reading CARD + GLOSSARY + your scaffold together (`cat` them).
2. **One** `bible.py` call with every scripture reference you need (it takes many refs).
3. Plates **only** for a Latin doubt or a side-note you cannot fix by the OCR rules below.
   Not to "check" the side-notes generally.
4. Write the finished chunk in **one** Write of the whole file (Latin blocks copied unchanged).
5. Lint once; fix; done. Draft in your head, not in the file.

## The job

The Latin in your scaffold is **established and frozen**. Fill: `[TITLE]` (short, lower case: "the
first law: Numbers 18"), each `[ENGLISH]`, the notes, the side-notes, the transcription notes; set
`status: translated`; lint; report.

- **Headings:** rename `## ¶k · range` to the speaker(s): `## Truth · 5.13–7.10`, `## Falsehood · …`,
  `## Truth and Falsehood · …`. VERITAS = Truth, MENDACIUM = Falsehood. **Never change a range; never
  split a paragraph.**
- **Never alter the Latin.** A word that looks wrong: open the plate (`text/dialogus/raw/leaves/nLEAF.jpg`,
  LEAF = page + 31; if missing, `curl -sL -o text/dialogus/raw/leaves/n0LEAF.jpg https://archive.org/download/latinworks22wycl/page/nLEAF.jpg`),
  read the apparatus at the page foot, and then: a variant that gives the sense → translate it + **T**
  note citing the siglum; a compelling emendation → translate it + **T** note "(our emendation)"; neither →
  translate the print and flag it. Never smooth nonsense into sense. Report every such case.
- **English layout:** speech opens `TRUTH.` / `FALSEHOOD.`. `[N]` at the same word as `[p. N]` in
  the Latin (the chunk's first `[p. N]` is implicit). Supplied words in `[brackets]`, sparingly.
  Quotations in quotation marks (italics are `none` in this volume; find quoted matter by sense).

## The four error classes (Thakkar) — check every sentence

1. **Terms:** GLOSSARY.md governs, one term one rendering. Tag the **first occurrence in the chunk**
   of every §A–C term: `[lordship]{g:dominium}`. The key must exist in GLOSSARY.md. A term that looks
   technical but has no row: render it sensibly, untagged, and propose it in your report.
   **CONTEXTUAL** rows (e.g. *inconveniencia*: absurdity / troubles) hold two senses English splits:
   choose the English by context, and write a **C** note at the first occurrence in the chunk and
   wherever it leans to the other sense (the dikaiosune rule, CONVENTIONS §6).
   Key rulings: *caritas* charity (never love) · *dominium* lordship · *presciti* the foreknown ·
   *predestinati* the predestinate · *viator* wayfarer · *patria* homeland · *ex fide* as faith teaches
   (with a genitive: "from the faith of scripture") · *limitare* assign (noun *limites* limits) ·
   *indispositus* unfit · *liberum arbitrium* free choice · *sensibilis* perceptible · *sentencia* teaching ·
   *evidencia* evidence · *reditus* revenue(s) · *conversacio* manner of life (the rest: GLOSSARY).
2. **Connectives carry the argument.** ⛔ Never omit one, never turn one into filler.

   | Latin | English | Never |
   |---|---|---|
   | enim, nam | for | "now", "indeed" |
   | ergo, igitur, ideo | therefore, so, then | "now", "and", "indeed" |
   | sed / autem, marking the **minor premiss or next step** | now | (omitted) |
   | sed / autem, adversative | but | (omitted) |
   | autem, continuative | and | (omitted), and **not "now"** |
   | cum (concessive / causal) | although / since | "whenever" |
   | tamen | yet, nevertheless | "therefore" |
   | item | again, also | "now" |
   | per idem | by the same token | "in the same way" |
   | ymmo | indeed, rather (correcting upward) | (omitted) |
   | patet; constat | it is clear; it is evident | |

   "Now" is reserved for the minor premiss. *Quia autem vellem* opening a speech is "And because I
   wished", not "Now because".
3. **Ordinary words with a medieval sense:** GLOSSARY §D; look up any word whose classical and
   Wyclifite senses may differ, and propose additions.
4. **Syntax:** construe before rendering (main verb, subject, what every relative and genitive
   hangs on). Keep quantifier order where it is meaning. Keep Wyclif's long periods where English
   tolerates them. **A doubtful construal is never chosen silently:** translate the likelier reading
   and write a **C** note giving the alternative.

## Scripture

`python3 scripts/w3/bible.py "Num 18:20-24"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering)
or `python3 scripts/w3/bible.py --find "maledicti qui declinant"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and
write an **S** note giving the Vulgate. Modern references in the English (Num. 18:20); the verse
numbers are Pollard's.

## Notes

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter:
  **T** text · **C** construal · **G** glossary (passage-specific only; otherwise a tag) · **S** source ·
  **R** reception/context.
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your
  report with a status: `editor` (Pollard's margin reference, listed in the scaffold's Transcription
  notes), `to-verify` (from memory: every patristic or canon-law identification you did not read in
  this session), `verified` (you read the source text this session: say where). ⛔ Never pass memory
  off as verified. Id `D<chunk>-<n>` (`D12-1`), cited in the note: "(LEDGER D12-1)".

## Worked example (chapter 3, batch A, reviewed)

> VERITAS. Quia autem vellem quod ista lex et cleri specialiter esset recencius memorata, feci illam
> scribi sepius in duplici testamento. Et sicut nemo potest excusari quin noscat in gradum qui sibi
> pertineat legem dei, sic nemo potest excusari quin noscat quodammodo matrem suam.

TRUTH. And because I wished that this law, and the clergy's especially, should be remembered the
more freshly, I had it written more than once in the twofold testament. And as no one can be
excused from knowing [God's law]{g:lex-dei} in the degree that pertains to him, so no one can be
excused from knowing, in some manner, his mother.[^1]

[^1]: **C/T.** *In gradum qui sibi pertineat*: "in the degree that pertains to him", with *qui*
    agreeing with *gradum*. B, C omit *in gradum* and read *quid*: "knowing what pertains to him
    according to God's law".

## Side-notes

The scaffold's list is a machine OCR draft. Keep only notes whose page.line falls **inside your
range**. Fix unambiguous OCR confusions (i/l, 0/o, rn/m, stray digits); for anything else read the
plate. Pollard's wording verbatim, no paraphrase. Join a note split over two draft lines. Delete the
`OCR DRAFT` comment.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/dialogus/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?
