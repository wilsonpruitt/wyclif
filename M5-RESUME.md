# M5 RESUME — *De ecclesia* (the first volume after the Dialogus)

*Read this first in a new session, then `WORKFLOW.md` (the stages) and `PLAN.md` § Cost. Written 2026-09-29
at the end of the M3/M4 session.*

## Status 2026-10-01 — side-note pass DONE (stage 5b)
- Method changed from "one plate agent per ~10 chapters": the margin column cut alone is clean modern
  type, so `sideocr.py` re-OCRs every note with tesseract (free) and places it at page.line;
  `sidesheets.py` cuts plate sheets only for notes a marker fires on (non-word, conf < 70, glyph,
  short) + `missed` places; `sidesplice.py` merges the reads and writes every scaffold's section.
  Control (`--spot 40`): 16/16 unflagged notes exact, line included.
- 1,383 re-OCR'd → 524 bands / 136 sheets → 4 **Sonnet** agents (`sidenotes.reads.part01–04.tsv`) +
  coordinator `part99` (α/β at 491.28/492.11, joins at 155.6, 417.24, 542.29). Result:
  **1,293 notes, 407 read on the plate**, in `text/ecclesia/sidenotes.fixed.tsv`; lint clean.
- **Cost: ≈ 0.55M** (127–145K per agent) against the 1M estimate.
- ⚠ Note ids in the reads are row numbers of `sidenotes.ocr.tsv`: never re-run `sideocr.py` without
  re-reading. Known residual class: a note tesseract split at a gap with no marker on either half
  (3 found by the lower-case-continuation check, fixed in part99).
- **Card done (2026-10-01):** `chunks/ecclesia/CARD.md`. Disputation formulae (*instatur* / *obicitur*
  "it is objected", *dicitur* "it is said" / "the answer is", *respondetur* "the reply is") are ruled
  into GLOSSARY §C (Wilson, 2026-10-01). 01-a/01-b start from the pilot's English (GLOSSARY governs).
  Post-pass fixes: one note wrongly deleted by an agent restored (181.11), stale "Omitted per §3.5"
  margin lines removed from 20 scaffolds (all were side-notes or page-foot sources); brief.py wording
  defers to the card; bible.py takes *Luc/Luce*.
- **Next:** translate 01-a (`brief.py ecclesia 01-a`, one Opus agent), then review it in a FRESH session
  against the four classes; card changes land before stage 7.

## Status 2026-09-30 (end of the first M5 session)

**Done (stages 1–5a):** Latin established and plate-read; 159 scaffolds cut. All committed locally on `main`
(nothing pushed; the Vercel project is not git-connected).
- Chunk size: **≤ 5 pp (Wilson)**, greedy at the editor's ¶ → **159 chunks** (23 chapters; median ~900 words;
  8 chunks run 6–7 pp because one ¶ does; ids `wyc-ecclesia-NN-x`).
- Extraction fixes (djvu.py) found by the completeness test (`complete.py`, now a standing step): whole pages
  had gone to the apparatus, ~35 pages had apparatus in the Latin, line-final verse numerals dropped. Dialogus
  checked old-vs-new: unaffected.
- Vote (vote.py) new rules, all logged in CONVENTIONS §3.3 **for Wilson to confirm**: R4a, NW, TAIL/GAP, EDGE;
  plate decisions key on the pivot token and always apply; an OVERRIDE wins. Writer normalises the z glyph
  (`^ \ $`), degree sign as 0/", old-style verse 1 read as *i*. `wordsplits.tsv` holds glued/fused forms.
- Plate pass: 2,236 decisions (`plate_decisions.part01–15.tsv` + `part99` coordinator OVERRIDEs, merged into
  `plate_decisions.tsv`). Brief: `text/ecclesia/PLATE-BRIEF.md`. Queue 0, stale 0.
- Open flags for translation: `text/ecclesia/PLATE-FLAGS.md` (p. 515 English side-note bleed; p. 245
  *coronanus*; p. 93 *limi[t]avi*; p. 188 join; superscripts pp. 239/243).
- Leftover generated files `text/ecclesia/p589–p600.*` (index; deletion was blocked) are ignored by
  `last_page` = 587.

**Cost so far:** plate pass ≈ 4.2M new tokens (measured ~14K/sheet; estimate was 1.5M).
**Remaining estimate:** side-note pass ~1M · CARD + first-chunk review ~0.3M · translation ~12.3M
(587 pp × ~21K) · per-wave ledger checks ~3M · close-out ~0.5M ≈ **17M more; volume total ≈ 21–22M**
(first estimate 17–18M).

**Next, in order (fresh session):**
1. Side-note pass (WORKFLOW 5): one plate agent per ~10 chapters corrects each scaffold's OCR side-notes.
2. `chunks/ecclesia/CARD.md` from `chunks/dialogus/CARD.md` (Loserth; sigla A, A₁, B, D from the pilot headnote).
3. Translate **01-a** and review it in a fresh session against the four classes; card changes land first.
4. Then briefs of 3–5 chunks with per-wave checks (WORKFLOW 7–8). Glossary/ledger as for the Dialogus.

## Where things stood at the handoff (2026-09-29)
- **M3 *Dialogus*: done** (38 chunks, close-out, rulings; `chunks/dialogus/RESUME.md`, `RULINGS-PENDING.md` §D).
- **M4 site: live** at wyclif.wrootpress.com (home = the whole Society edition; Dialogus at `/dialogus/`).
  Deploy recipe in memory, `reference_wyclif-deploy`; the Vercel project is NOT git-connected.
- **Method for M5:** `WORKFLOW.md`, the single-pass brief workflow (`scripts/w3/brief.py`), measured at
  ~55k tokens/chunk against ~93k for one agent per chunk. Runs on the Claude Code plan: **no API budget**
  (the API method, `scripts/pilot/translate_api.py`, is priced at $0.22/page for reference only).

## *De ecclesia* facts
- Slug `ecclesia`; ed. J. Loserth, 1886; primary scan `latinworks10wycl` (644 leaves); 5 other free scans;
  **no Fordham text**. Plate offset: printed page = leaf − 37 (`catalog/plate_offsets.tsv`).
- ~136,500 Latin words (5.8× the Dialogus). Old measurement: 24.1 plate items / 1,000 words, 3,296 items,
  but on the OLD extraction (see stage 1).
- A pilot exists: `pilots/wyc-ecclesia-01a.md`, bk I ch. 1, alineae A–C (pp. 1–5), plate-read, 29 notes.
  Its ledger rows are V-01…V-12 and V-19 in `LEDGER.md`; several are still `to-verify`.

## Before anything else: confirm the chunk size
The Dialogus chapters average ~2.6 pages; *De ecclesia*'s run to ~26. `chapters.py` already splits any chapter
over 8 pages into parts of at most 7, at the editor's ¶ (CONVENTIONS §1), so the volume comes out at roughly
100 chunks. The single-pass measurements were on 2–6-page chunks; 7 pages of dense Latin in one pass is
untested. **Decide with Wilson:** keep ≤7, or lower the split to ~4–5 pages (a one-line change at
`chapters.py:116`). Cost is per page either way; the question is quality on the longest chunks.

## First steps (in order)
1. **Hard stop for Wilson** (volume estimate + "which model, and go?"). Rough estimate on the plan, from the
   Dialogus rates: witnesses + vote ~0 (computation) · Latin plate pass ~1.5M · side-note pass ~0.5M ·
   translation ~12M (≈ 600 pages at ~21k/page, the brief rate) · per-wave ledger verification ~3M · close-out review ~0.5M
   ≈ **17–18M tokens**. Restate it with the chunk count once stage 5 has cut the scaffolds.
2. **Rebuild the witnesses** (WORKFLOW stage 1). The current `text/ecclesia/` (untracked, generated, from the
   old extraction) must be regenerated: remove `text/ecclesia/witnesses/*.jsonl`, then
   `.venv/bin/python scripts/w3/witness.py ecclesia`. This also writes `text/ecclesia/apparatus.json`.
   Generated data, re-derivable by re-running; say so when doing it. Same later for `officio-regis`.
3. **Completeness test without Fordham:** diff the established text against a full independent witness
   (e.g. `iohanniswycliftr00wycluoft`) for runs of ≥3 words present on one side only (PLAN, the M2
   extraction defect). Then the numeral sweep (PLAN, "Numerals").
4. Vote, then look at whether the big R4 / THIN / R3 classes can be settled by a rule before cutting crop
   sheets (PLAN notes this as open), then the plate pass and `nonword.py ecclesia`.
5. Scaffolds (with the chunk-size decision), side-note pass, `chunks/ecclesia/CARD.md` from the Dialogus
   card (Loserth's sigla A, A₁, B, D are in the pilot's headnote), first chunk reviewed in a fresh session.
6. Translate in briefs of 3–5 chunks, with the per-wave checks (WORKFLOW stage 8).

## Suggested opening prompt for the new session
> Continue Wyclif M5 on *De ecclesia*. Read `~/wyclif/M5-RESUME.md`, then `WORKFLOW.md`. Start with the
> chunk-size question and the volume estimate (hard stop) before running anything.
