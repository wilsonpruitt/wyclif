# M5 RESUME — *De ecclesia* (the first volume after the Dialogus)

*Read this first in a new session, then `WORKFLOW.md` (the stages) and `PLAN.md` § Cost. Written 2026-09-29
at the end of the M3/M4 session.*

## Where things stand
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
