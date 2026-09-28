# BRIEF — translating the *Dialogus* (M3)

You are filling chunk scaffolds in `chunks/dialogus/`. The Latin in them is **established and
frozen** (three-witness vote + 238 plate readings). Your job is the English, the notes, the title,
the corrected side-notes, and the §14 check. Work from `~/wyclif`.

## Read first, in this order (all of it)

1. `CONVENTIONS.md`: the rules. §§5–14 govern everything you write.
2. `GLOSSARY.md`: one term, one rendering. Tag keys must match a row.
3. `pilots/wyc-dialogus-01.md`: **the model**. Match its register, its English, its note style
   and its density logic.
4. `reference/thakkar.txt`, lines 380–600: the four error classes with his examples
   (terminology, connectives, ordinary words, syntax). *Daggers drawn.*

## For each chunk assigned to you

1. **Title.** Replace `[TITLE]` with a short descriptive title in the pilot's style (lower case,
   e.g. "the three parts of the church militant").
2. **Section headings.** Rename `## ¶k · range` to the speaker(s) of that paragraph, keeping the
   range exactly: `## Truth · 3.15–4.2`, `## Falsehood · …`, or `## Truth and Falsehood · …` when one
   paragraph holds both. VERITAS = Truth, MENDACIUM = Falsehood. **Never change a range and never
   split a paragraph.** The ranges are computed from the print's line numbers.
3. **Never alter the Latin.** If a word looks wrong, follow CONVENTIONS §5 (open the plate, read the
   apparatus at the page foot, write a T note) and report it in your batch file. Don't edit it.
   Plates: `text/dialogus/raw/leaves/nLEAF.jpg`, where LEAF = page + 31. If a leaf is missing:
   `curl -sL -o text/dialogus/raw/leaves/n0LEAF.jpg https://archive.org/download/latinworks22wycl/page/nLEAF.jpg`
   (4-digit zero-padded file name, unpadded URL).
4. **English** replaces each `[ENGLISH]`. Speech opens with `TRUTH.` / `FALSEHOOD.` as in the
   pilot. Page breaks `[N]` go at the same word as `[p. N]` in the Latin (the first `[p. N]` of a
   chunk is implicit in the English, as in the pilot). Supplied words go in `[square brackets]`,
   sparingly. Glossary tags `[English]{g:key}` go on the **first occurrence in this chunk** of every
   §A–C term, and only with a key that exists in GLOSSARY.md. Quoted matter (italics are `none` in
   this volume) goes in quotation marks, identified from the sense and the references.
5. **Scripture** (§10): look up every quotation with
   `python3 scripts/w3/bible.py "Matt 8:20"` (Vulgate + Douay–Rheims; psalms in Vulgate
   numbering) or `python3 scripts/w3/bible.py --find "vulpes foveas"`. Where Wyclif's Latin agrees
   with the Clementine Vulgate, use the Douay–Rheims wording. Where he departs, translate *his*
   Latin and write an **S** note giving the Vulgate. References in the English are modern (Matt.
   8:20). The verse numbers are Pollard's, not Wyclif's.
6. **Notes** (§11): `[^n]`, numbered from 1 in each chunk, each marker placed in the same edit as
   its note, each opening with its type letter (T, C, G, S, R). **Density:** the pilot is dense
   because chapter 1 carries the work's first occurrences. Later chapters should thin out, to
   roughly one note per 70–100 Latin words, fewer where the text is plain. Short and factual.
   No modern theology, no evaluation.
7. **Source identifications** (§11, LEDGER): every identification you make (scripture excepted,
   when checked with bible.py) needs a ledger row in your batch file, with a status:
   `editor` (Pollard's own reference: the margin references listed in the scaffold's Transcription
   notes are his), `to-verify` (from your memory, including every patristic or canon-law
   identification you have not checked against a text), or `verified` (only if you actually read
   the source text in this session: say where). **Never present a memory identification as
   verified.** Use ids `D<chunk>-<n>` (`D07-1`, `Depila-2`). Put the id in the note: "(LEDGER D07-1)".
8. **Side-notes.** The scaffold's list is an OCR draft grouped by machine. Keep only notes whose
   page.line falls **inside this chunk's range** (notes before it belong to the previous chunk).
   Correct unambiguous OCR confusions (i/l, 0/o, rn/m, stray digits, glued line numbers). For
   anything else, open the plate and read it. Pollard's wording is kept verbatim: no paraphrase,
   no modernising. A note split across two draft lines is joined. Delete the `OCR DRAFT` comment
   when done.
9. **Transcription notes.** Keep the generated list. Add what you found: an apparatus variant you
   used, a plate check you made.
10. **Front matter.** Set `status: translated`. It is not `done`: the ledger is verified in a
    later pass. Change nothing else there.
11. **Lint** each chunk until clean: `.venv/bin/python scripts/w3/lint.py chunks/dialogus/wyc-dialogus-NN.md`
12. **§14 four-class check**, chunk by chunk, before you report: every glossary term; every
    *enim / nam / ergo / igitur / ideo / sed / autem / item / cum / tamen / per idem* accounted for,
    none omitted or turned into filler; every classical/medieval gap looked up; every sentence
    construed, doubtful ones with a **C** note.

## Shared files: DO NOT EDIT

`LEDGER.md`, `GLOSSARY.md`, `CONVENTIONS.md`, `PLAN.md`, anything in `text/`, `scripts/`,
`pilots/`, and other agents' chunks. Put everything that belongs in a shared file in **your batch
file** `chunks/dialogus/_batch-<B>.md` (B = your batch letter):

- `## Ledger rows`: in LEDGER.md's table format, one row per identification or dated claim.
- `## Glossary proposals`: a term that looked technical but has no row, with your proposed
  rendering and why. Use the rendering in the chunk, **without** a tag.
- `## Latin doubts`: page.line, the printed word, what you suspect, whether the plate/apparatus
  settled it.
- `## Counts`: per chunk, Latin words and notes.

## Report back (≤ 150 words)

Chunks finished, notes per chunk, ledger rows (how many `to-verify`), glossary proposals, Latin
doubts. Nothing else: the work is in the files.
