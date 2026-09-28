# PLAN — Wyclif's Latin works in English (Wroot Press)

*Plan of record, written 2026-09-28 (Fable) after Phase 0. The pilot drafts of `CONVENTIONS.md` and
`GLOSSARY.md` govern the chunk work; `LEDGER.md` governs every source claim. Volume work runs on Opus
against the frozen conventions. This file changes only when the scope or the order changes.*

## What this is

**The whole Wyclif Society corpus** (33 volumes, 1883–1922, ~2.6M Latin words, ~14,100 scan leaves)
in English, beside the Latin, at **wyclif.wrootpress.com**. It is queued so that the interesting
untranslated works come first.

**Why it is worth doing.** Apart from *De simonia* (McVeigh 1992) and the English *De universalibus*
(made from a different edition), no treatise in the series exists complete in English. The two
recent translations that promised to change this (Penn 2019, Lahey 2013) are, in Mark Thakkar's
documented judgement, "worse than useless" (*Vivarium* 58 (2020), 357–83), and were praised in
five reviews regardless. A careful translation is scarce here, and it is also the contribution:
no one yet has put Wyclif's own argument in English, sentence by sentence, with its terms held
steady. The conventions are built around the four error classes Thakkar documents.

**What it is not.** Not a critical edition: the Society text is the copy-text, corrected only in
notes (CONVENTIONS §5). Not the works outside the series (*Trialogus*, *De universalibus*, *De
Trinitate*, the *Postilla*). Not the vernacular English works.

## Rights

The Latin is PD. Fordham's transcription is used with credit to the Hornbeck & Adams project
(PHASE0 finding 8). The English, the notes and the encoding are CC BY-NC 4.0 per
[[wroot-press-licensing]], with the PD/encoding split stated on a `/rights` page. Thakkar's review is
CC BY 4.0 (a copy is in `reference/`).

## The queue (from PHASE0; recorded in `scripts/build_catalog.py`)

**Tier 1, church, papacy, eucharist, lordship (12 vols, 36% of leaves):** De ecclesia · Dialogus ·
De potestate pape · De eucharistia · De civili dominio I · De officio regis · De apostasia · De
blasphemia · Polemical Works I–II · Opus evangelicum I–II (incl. De Antichristo).
**Tier 2 (10 vols, 35%):** De civili dominio II–III · De mandatis divinis · Opera minora · De dominio
divino · Sermones I–IV.
**Tier 3, philosophy (9 vols, 20%):** De benedicta incarnacione · De compositione hominis · De ente
praedicamentali · De ente excerpta · Misc. phil. I · De logica I–III · Misc. phil. II.
**Tier 4, English exists (2 vols, 9%):** De veritate · De simonia.

**One change to the working order:** finish the **Dialogus first** as the first complete work. It is
short (178 leaves, ~24k Latin words), it has Fordham text that collated clean, and it is the work
the Bohemian Wycliffites read most. De ecclesia runs next, then the rest of Tier 1 in queue order.

## Milestones

**M0: Phase 0.** ✅ Done 2026-09-28 (`PHASE0.md`).

**M1: Pilot.** ✅ Done and FROZEN 2026-09-28 (Fable; Wilson's review): `CONVENTIONS.md`, `GLOSSARY.md`, `LEDGER.md`, and two
chunks that test both text paths:
- `pilots/wyc-ecclesia-01a.md`: *De ecclesia* I, alineae A–C (pp. 1–5), **plate-read**, 29 notes + glossary tags.
  This is the paragraph Thakkar uses to show Penn's errors, so the pilot can be checked directly
  against a published correction.
- `pilots/wyc-dialogus-01.md`: *Dialogus* cap. 1 (pp. 1–3), **Fordham-collated**: 0 word errors, 1
  structural error (a chapter heading Fordham invented), 12 notes + glossary tags.
- §3 of CONVENTIONS revised the same day (Wilson's OK): the Latin is established by the three-witness
  check, not by re-reading every plate. The pilots become M2's acceptance test.
- ✅ **Frozen on Wilson's review, 2026-09-28.** All five decisions went to the recommended option. They
  are recorded in CONVENTIONS' decision log, and the pilots were converted to the new note register.

**M2: The three-witness pipeline.** ✅ Built and passing its acceptance test, 2026-09-28 (Opus).
`scripts/w3/`: `djvu.py` (layout: main column / side-notes / apparatus / running heads / chapter
headings, from archive.org `_djvu.xml` word boxes, lines rebuilt from geometry) · `witness.py SLUG`
(all free scans + Fordham → token streams; side-notes → `sidenotes/`) · `vote.py SLUG [p q]`
(page-by-page alignment, the §3.3 table, established Latin `text/<slug>/pNNN.la.txt` + check logs +
plate queue) · `crops.py` (line-strip sheets) · `accept.py` · `lint.py`. Python in `.venv`
(spylls + Pillow); the Latin hunspell dictionary is GPL, fetched locally and never committed.
- ✅ **Acceptance:** *De eccl.* 1.1–5.13 = 858/858 words and *Dial.* 1.1–3.14 = 457/457 against the
  plate-read pilots (italics aside); *Off. reg.* 68 *Sicul*→*sicut* and *edifacta*→*edificata*
  corrected by vote; 69 *wltfacere* kept as printed.
- ✅ **Plate loop proven:** Dialogus pp. 1–10, 19 items on 3 sheets, all applied, none stale.
- ✅ **Measured:** see CONVENTIONS §3.3 and the table below.
- ⏳ **Open:** (a) the remaining Dialogus plate items (~215 → ~27 sheets): read them as the first
  step of M3; (b) **Tesseract** for the four volumes with fewer than 3 witnesses, deferred until the
  first of them is reached (Polemical Works I, queue 9); (c) **voting the side-notes** across
  witnesses (they are single-witness OCR English now: *ciergy*, *humiiity*); (d) punctuation is
  taken from Fordham or the pivot, not voted.
- ⚠ The §3.3 refinements are recorded in CONVENTIONS' decision log **pending Wilson's confirmation**.

**M3: The Dialogus complete (Opus).** 36 chapters + Epilogus. First: finish its plate items (~27
sheets, ~0.1M tokens). Then translate against the frozen conventions from `text/dialogus/`, with the
headnote cleared of `[verify]` and every ledger row closed. Est. ~0.5M tokens, nearly all translation.

**M4: Site v0 (Opus).** A static build on the house pattern (look at the Arminius site before
designing). Latin | English columns, the editor's side-notes as a navigation rail, hover glosses from the
`{g:…}` tags, a plate link on
every page, citation by work + page.line, `/rights`, the credit line for Fordham. Content: the
Dialogus plus the De ecclesia opening. ⛔ **Deploy to wyclif.wrootpress.com only on Wilson's
per-deploy OK** (DNS via Cloudflare, per [[reference_domains-cloudflare]]).

**M5: Tier 1 in queue order (Opus),** one volume at a time. **Stop before each volume** with its
token estimate and ask "which model, and go?" (hard stop 6). The first chunk of each volume gets a
fresh-session review against the §14 four-class check before the rest of the volume runs.

**M6–M8: Tiers 2, 3, 4.** Same loop. Tier 3 (logic and metaphysics) is the hardest register.
**Re-pilot before starting De logica**, in a Fable session, to extend the glossary's §C. The
existing entries were made on theology.

## Cost (rough; revised 2026-09-28 for the three-witness check; re-measure after M3)

The Latin is no longer established by reading every page image. The vote settles ~99.6% of words
from text alone (measured on *Off. reg.*); the plate is read as line crops for the rest (~3–6 per
1,000 words, so about one small crop per Society page). The witness download and the vote are
ordinary computation and cost no model tokens. What remains is **the translation itself**: read
the Latin, write the English and the notes, and work it out, plus the amortised conventions and
glossary. Call it **~4–5k tokens per Society page**, over ~12,000 text pages:

| Scope | Text pages (est.) | Tokens (est.) |
|---|---|---|
| Dialogus (M3) | ~100 | ~0.5M |
| Tier 1 | ~4,400 | ~20M |
| Whole corpus | ~12,000 | ~50–60M |

The earlier estimate (8–10k/page, 100–120M) assumed reading every page image. ⚠ These are still
estimates. **Re-measure on the Dialogus** and rewrite this table, and again on the first dirty-OCR
volume (the Dialogus's witnesses are unusually clean).

## Deferred layers (named so they aren't forgotten; none is in scope now)

- **Readers' glosses.** The editors print medieval marginal commentary in the apparatus (MS B's
  glosses in *De ecclesia*; a full *glossa* on *Off. reg.* 13). It is a real early-reception layer.
- **Hus parallels.** Hus's *De ecclesia* against Wyclif's, passage by passage (Loserth's own
  subject). The strongest reception layer the corpus has.
- **Wycliffite Bible.** The Early/Later Version English of the verses Wyclif quotes, as an
  optional scripture layer (PD).
- **FitzRalph, *De pauperie Salvatoris* I–IV**, printed in the De dominio divino volume. Context for
  *dominium*; not Wyclif.
- **The apparatus in full** (a scholarly edition layer); for now it stays on the plates.

## Decisions taken at the pilot review (2026-09-28, Wilson)

1. Scripture: **Douay–Rheims** (Challoner) where Wyclif quotes the Vulgate exactly.
2. *Presciti*: **"the foreknown"**, explained per work.
3. *Dominium*: **"lordship"**.
4. Notes: **glossary tags + hover glossary** on the site; G notes only for passage-specific points.
   M4's site build must render `{g:…}` tags from `GLOSSARY.md`.
5. **The Dialogus first**, and it carries the site launch.

Recorded with dates in CONVENTIONS' decision log; change any of them only there.
