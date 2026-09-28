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

**M1: Pilot.** ✅ Drafted 2026-09-28 (Fable): `CONVENTIONS.md`, `GLOSSARY.md`, `LEDGER.md`, and two
chunks that test both text paths:
- `pilots/wyc-ecclesia-01a.md`: *De ecclesia* I, alineae A–C (pp. 1–5), **plate-read**, 32 notes.
  This is the paragraph Thakkar uses to show Penn's errors, so the pilot can be checked directly
  against a published correction.
- `pilots/wyc-dialogus-01.md`: *Dialogus* cap. 1 (pp. 1–3), **Fordham-collated**: 0 word errors, 1
  structural error (a chapter heading Fordham invented), 13 notes.
- ⏳ **Freeze = Wilson's review.** On approval, CONVENTIONS and GLOSSARY lose "pilot draft" and are
  changed only by dated decision. Decisions for the review are at the foot of this file.

**M2: Tooling (Sonnet, with file paths given; Opus if it fights back).**
- Calibrate `catalog/plate_offsets.tsv` for all 33 volumes: offset from `_page_numbers.json`, then
  **one visual check per volume** (the file was right for the three checked, but a stated
  confidence of 86 is not proof).
- Side-note extraction from hOCR (the margin column) into `sidenotes/<slug>.tsv` keyed page.line.
  Spot-check against three plates per volume.
- A chunk template, plus a lint that fails a chunk with an unanchored note, an open `[verify]`,
  empty `latin_source`/`collation`, or a Latin block containing folio asterisks.
- Optional: a connective counter (enim/nam/ergo/igitur/sed/autem/item in the Latin vs. "for /
  therefore / now / but / again" in the English) that **flags** a chunk for review. It is never a
  gate, because the counts need not match.

**M3: The Dialogus complete (Opus).** 36 chapters + Epilogus, Fordham-collated, headnote cleared of
`[verify]`, every ledger row closed. Est. ~1–1.5M tokens.

**M4: Site v0 (Opus).** A static build on the house pattern (look at the Arminius site before
designing). Latin | English columns, the editor's side-notes as a navigation rail, a plate link on
every page, citation by work + page.line, `/rights`, the credit line for Fordham. Content: the
Dialogus plus the De ecclesia opening. ⛔ **Deploy to wyclif.wrootpress.com only on Wilson's
per-deploy OK** (DNS via Cloudflare, per [[reference_domains-cloudflare]]).

**M5: Tier 1 in queue order (Opus),** one volume at a time. **Stop before each volume** with its
token estimate and ask "which model, and go?" (hard stop 6). The first chunk of each volume gets a
fresh-session review against the §14 four-class check before the rest of the volume runs.

**M6–M8: Tiers 2, 3, 4.** Same loop. Tier 3 (logic and metaphysics) is the hardest register.
**Re-pilot before starting De logica**, in a Fable session, to extend the glossary's §C. The
existing entries were made on theology.

## Cost (rough, and to be re-measured after M3)

A text page costs roughly: the plate image read (~3k tokens), amortised conventions and glossary
(~2–3k), and output of Latin + English + notes (~1.5k) plus reasoning. Call it **8–10k tokens per
Society page**, and about 12,000 text pages in the corpus:

| Scope | Text pages (est.) | Tokens (est.) |
|---|---|---|
| Dialogus (M3) | ~100 | ~1–1.5M |
| Tier 1 | ~4,400 | ~35–45M |
| Whole corpus | ~12,000 | ~100–120M |

⚠ These are estimates, not measurements. **Re-measure on the Dialogus** and rewrite this table.
Fordham-collated volumes are not much cheaper, because the plate must still be read in full to
collate.

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

## Decisions for Wilson at the pilot review

1. **Scripture in English: Douay–Rheims (Challoner) wording where Wyclif quotes the Vulgate
   exactly.** *Recommended*: it is his Bible's English, and it matches glossa.wrootpress.com. The
   alternatives are the AV (Arminius's choice, but it translates a different text) or fresh
   translation throughout.
2. ***Presciti* → "the foreknown", explained per work, never "the reprobate".** *Recommended*: it
   keeps Wyclif's distinction from *reprobi*. Loserth's own side-notes say "reprobate".
3. ***Dominium* → "lordship"** (titles *On Civil Lordship*, *On Divine Lordship*). *Recommended*.
4. **Note density.** The pilots run at ~1 note per 30–45 Latin words. Is that the right register
   for the site, or should first-occurrence glossary notes move into a hover glossary so the
   notes thin out?
5. **The Dialogus is the first complete work and the site launch** (rather than De ecclesia).
