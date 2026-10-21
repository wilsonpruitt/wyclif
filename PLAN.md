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

**Second change (Wilson, 2026-10-21): *De benedicta incarnacione* (queue 23) runs before *De
eucharistia*.** It is the surviving work closest to Wyclif's lost *Sentences* lectures (book III). It
opens with a Latin-method pilot on its first pages: (A) a vision model corrects Fordham, against (B) a
blind transcription diffed with Fordham, against (C) the three-witness vote. Scorecard:
`chunks/incarnacione/PILOT-LATIN.md`; **B+ (blind transcription) adopted for this and every later volume**,
WORKFLOW § B+. The first chunk's review runs in a Fable session (metaphysics
terms for GLOSSARY §C).

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

**M5: Tier 1 in queue order (Opus),** one volume at a time, by **`WORKFLOW.md`** (the single-pass brief workflow, 2026-09-29). **Stop before each volume** with its
token estimate and ask "which model, and go?" (hard stop 6). The first chunk of each volume gets a
fresh-session review against the §14 four-class check before the rest of the volume runs.

**M6–M8: Tiers 2, 3, 4.** Same loop. Tier 3 (logic and metaphysics) is the hardest register.
**Re-pilot before starting De logica**, in a Fable session, to extend the glossary's §C. The
existing entries were made on theology.

## Cost — MEASURED on the *Dialogus* (M3, 2026-09-29); the estimate below it is superseded

*Dialogus*: 98 Society pages, 23,601 Latin words, 38 chunks. Agent tokens (coordinator not counted):

| Stage | Tokens | Per page |
|---|---|---|
| Translation (38 chunks, one Opus agent each) | 3.55M | ~36k |
| Close-out: ledger verification (3 batches), tagging, plate pass, targeted review, connective check | 1.29M | ~13k |
| **Total** | **~4.85M** | **~49k** (~205 per Latin word) |

At that rate: **Tier 1 (~4,400 pp.) ≈ 215M; whole corpus (~12,000 pp.) ≈ 590M.** That is ~10× the
estimate below. Why it is higher:
- NOT the context files: measured 2026-09-29, card ~2k + glossary ~6k + scaffold 3–9k = ~11–17k tokens per
  chunk, against ~93k spent. The cost is the agent LOOP: every turn (read, bible.py, edit) re-sends the whole
  growing context plus the harness's instructions, so 15–20 turns pay for it 15–20 times. Evidence: batch A
  (5 chapters, one agent) cost ~47k/chunk, half the one-agent-per-chunk rate, and reviewed clean.
- Levers, in order: (1) 3–5 chunks per agent (measured ~2×); (2) fewer turns: inline card + glossary FILTERED
  to the chunk's rows (58–102 of 219 measured) + scaffold with scripture pre-computed, one final write;
  (3) translation as ONE API call per chunk (Messages API, card+glossary as a cached prefix, Batch API for
  a further ~50%), est. ~20–25k/chunk, checks moved to the existing verification passes. ▶ Pilot (3) vs (1)
  on 2–3 De ecclesia chunks before M5 and re-cost from the result.
- ⚠ Agent token counts as reported may include cheap cached reads; the billed cost may be below the figure.

**PILOT RESULT (2026-09-29, `scripts/pilot/translate_api.py`, `chunks/dialogus/_pilot/`).** Option (3) run on
Dialogus ch. 2, 14, 30 (~10 Society pages; the same untranslated scaffolds the agents had, plus the corrected
side-notes and the page-foot apparatus extracted from the djvu layout with `djvu.py`). Opus 5.5, effort high,
card+glossary cached (15.3k prefix, read at 0.05× after the first call):

| ch. | agent method (tokens) | one API call (tokens) | billed |
|---|---|---|---|
| 2 | ~93k (47k batched) | 36.6k | $0.44 |
| 14 | 87k | 43.4k | $0.51 |
| 30 | 141k | 86.0k | $1.28 |

≈ **16.6k tokens and $0.22 per Society page** for translation, against ~36k/page by agents; 63% of it is output
(the model's reasoning at effort high). **Quality, blind A/B review against the reviewed chunks: the API version
was equal or better in all three** (errors 0 vs 0; weak points 2 vs 13; its lead grows with the Latin's
difficulty). Caveats: it had today's refined card and glossary, which the original translators did not; three
chunks only; the Latin was already established (a dirtier text will raise more Latin doubts).
**Projection for Tier 1 (~4,400 pp.):** translation ≈ 73M tokens ≈ $1,000; the Batch API halves that (~$500).
Verification passes are extra and could be scripted the same way. ▶ **Adopt for M5** at effort **high**, through the Batch API.

**Effort `medium` measured (2026-09-29, same three chunks, blind review vs `high`):** $1.37 vs $2.23 (−39%; ch. 2
$0.34, ch. 14 $0.34, ch. 30 $0.69). Quality: `high` 1 error / 3 weak / 12 style, `medium` 1 / 9 / 15; the gap is almost
all in ch. 30, the long dense chapter (7 weak vs 1). `medium` also misreported more variants in its notes and once
dropped the front matter. **Keep `high`**: the Batch API's 50% costs no quality, `medium`'s 39% does. (API errors seen:
one `timeout_error`, one `overloaded_error` on ch. 30; the script now retries 6×.)
**Funding (Wilson, 2026-09-29): no API budget for a full run.** The dollar figures here price the method; the
translation itself runs on the Claude Code plan, where the lesson that transfers is the single-pass shape: give the
agent card + filtered glossary + scaffold + apparatus INLINE and have it write the chunk once (few turns), several
chunks per agent.
- The notes are a large share of the output (source identifications, variants, construal), and the ledger
  then has to be verified by reading sources (~9k per row).
- The *Dialogus* witnesses are clean; *De ecclesia* and *Off. reg.* send 2× the plate items per 1,000 words.
Close-out lessons that cut cost next time: verify ledger rows as they are written, per wave, not at the
end; run the *sed*/*autem* and split-tag checks per wave (they are cheap and found real errors: 9/207
connectives, 4 broken tags); a four-class review of the long, dense chunks only (short chunks were clean).
⚠ `catalog/lexicon/agreed.txt` holds majority errors (*chnstus*): the non-word sweep must use Hunspell only.

**MEASURED, *De ecclesia* close-out (2026-10-03), 587 pp., all Opus:** four-class review of 25 chunks 1.30M
+ applying it 0.47M · *sed/autem* check of the other 134 chunks 1.32M · LEDGER backlog of 243 rows 2.14M
(~8.8K/row, mostly web lookups) + note repair 0.10M · ≈ **5.3M agents (~9K/page)**, against an estimate of
0.5M (M5-RESUME) and 3.3M (the plan). It was dear because the per-wave gates were skipped (connectives) or
deferred ("not local" ledger rows), and italics were never captured (52 of 174 review rows). WORKFLOW stages
4b/5/8 now make those gates; with them the close-out should be the targeted review alone (~1.8M for a
volume this size, ~3K/page).

**MEASURED, *De potestate pape* (2026-10-07 … 10-12), 406 pp., 107 chunks:** stages 1–6 2.5M · translation +
per-wave gates (scars, connectives, ledger verified each wave) ≈18M · close-out ≈1.25M: four-class review of
the 16 longest chunks 0.67M Opus (3 errors, 42 weak, 31 style), applying it 0.33M + *probabiliter/nimis*
conform 0.10M (Sonnet), coordinator incl. 12 plate reads ≈0.15M. **Volume ≈21.8M (~54K/page).** With the
per-wave gates the close-out came in at the ~1.8M forecast's lower end and needed no ledger or connective pass;
the per-wave ledger agents (130–270K each) were the overrun against the 12–13M estimate.

### Superseded estimate (2026-09-28)

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

⚠ **Measured 2026-09-28, full volumes** (`vote.py`, §3.3 as confirmed), and the "~3–6 per 1,000"
above does not hold outside the Dialogus:

| Volume | Pivot words | Voters (mean) | Unanimous | Plate items / 1,000 words |
|---|---|---|---|---|
| Dialogus | 23,120 | 6 | 89.6% | 10.3 |
| *De ecclesia* | 136,506 | 5.9 | 86.3% | **24.1** (3,296 items) |
| *De officio regis* | 78,074 | 6.6 | 82.2% | **20.3** (1,584 items) |

About 5 items per Society page, or ~400–450 crop sheets for *De ecclesia* alone. The biggest open
classes are R4 (no majority), THIN and R3. Before M5, check whether a sample of these is mechanical
and could be settled by a rule, as §3.3 did for the Dialogus, rather than read on the plate.

⛔ **M2 extraction defect, found and fixed in M3 (2026-09-28).** `djvu.py`'s apparatus split was
cutting real text at the foot of the page: (a) the last body line, when the notes' tight leading
started one line early; (b) a heading near the foot plus the lines under it; (c) the page's last
13–22 lines, when a one-word side-note row with an inflated box sat inside the column; and
(d) conversely, two or three note lines leaked into the text when too few gaps existed for the
leading test. Fixes: move the cut to the widest gap within two lines; capital-word rows (CAPITULUM,
VERITAS) never open the notes; a short row whose box starts in the margin is side-note; a sigla-density
test for short note blocks. Dialogus: **+254 words restored** (pp. 17, 34, 38, 74, 87, 96), 3 note
blocks removed (pp. 91–93); the established text now differs from Fordham only where Fordham omits.
Test that caught it: diff the whole established text against Fordham (or any full witness) for
runs of ≥3 words on one side. **Run it on every volume.** ⚠ The *De ecclesia* / *Off. reg.* rates
above were measured on the OLD extraction; rebuild their witnesses (`witness.py` skips existing
`.jsonl`, so delete them first) before M5.
⚠ **Numerals (found in M3 wave 1):** the extraction drops a line-final numeral (*prov. 30*,
*concedentibus 40*) and some ordinals (*Patet 2°*). A general fix let in marginal verse numbers, so
it was reverted. **Standing QA step: a numeral sweep against Fordham** (every numeral token present in
one text and not the other), each hit read on the plate. The Dialogus had 11. For a volume without
Fordham, this is a known residual gap; budget a numeral pass on the plates.

## Deferred layers (named so they aren't forgotten; none is in scope now)

- **Readers' glosses.** The editors print medieval marginal commentary in the apparatus (MS B's
  glosses in *De ecclesia*; a full *glossa* on *Off. reg.* 13). It is a real early-reception layer.
- **Hus parallels.** Hus's *De ecclesia* against Wyclif's, passage by passage (Loserth's own
  subject). The strongest reception layer the corpus has. **Parked as a companion work for after
  Wyclif** (2026-10-04): source locator in `reference/hus/` (with *Super IV Sententiarum*, which
  links to the Sentences work).
- **About-page narrative.** Why a name everyone knows was never translated: no Wycliffite revival,
  the German scholarship, the Society's origins. Notes (unverified) in `reference/about-narrative.md`.
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

## Stopping rule for passes over finished text (2026-10-02, Wilson)

**A pass over already-finished text needs a specific, located cause. "There might be more errors" is not one.**
Each repass costs more than the last and finds less; the copy can be repassed forever. So:
- Per-brief checks (Opus translation + Sonnet plate/source check, word by word while the plates are open) stay:
  that is the one full pass, done once, while it is cheap.
- After a chapter is committed, it is reopened only for a located cause: a reader report, a pattern found
  elsewhere that names specific places (e.g. a grep-able scar), or a note that already flags the spot.
- Measured yield that set the rule: the word-by-word plate check finds ~1 lost word per 12 pages, mostly
  sense-neutral (*, 34,*, *a*); a full Sonnet repass of chs. 1–13 would cost ~3M tokens (~130K per word found).
  Instead, the 22 spots where translators' notes already flagged a non-construing sentence were plate-checked
  (one Sonnet agent), and chs. 1–13 were then closed.
- Colophon: the site says the Latin is transcribed from Loserth (1886) and invites corrections.
