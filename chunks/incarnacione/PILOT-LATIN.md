# Latin-method pilot: *De benedicta incarnacione* pp. 3–12 (2026-10-21)

**Question (Wilson):** is it cheaper to have a vision model (A) correct Fordham against the plate, or (B)
transcribe the plate blind and then settle its disagreements with Fordham? Arm C, the existing three-witness
vote (`WORKFLOW.md` stages 1–3b), is the baseline. Vision arms on Sonnet. The ruling read was by the Opus
coordinator.

**Pages:** pp. 3–12, main column only (Fordham has no side-notes or apparatus), ≈2,780 words. Pp. 1–2 (the
prologue) are not in Fordham. Leaf = page + 39 (`catalog/plate_offsets.tsv`).

## Result

| Arm | Agent tokens | Per page | Word errors left (vs reference) |
|---|---|---|---|
| Fordham as it stands | 0 | 0 | 13 sites, incl. two lost runs (p. 5 a line, p. 6 ≈185 words) |
| **A** correct Fordham | 112K | 11.2K | **1**: kept Fordham's *a* in the English argument (p. 3), the anchoring error |
| **B** blind transcription | 94K | 9.4K | **0** |
| B, step 2: rule its 14 diffs with Fordham on full pages | +78K | +7.8K | 0 words; 1 scope slip (it deleted the *Cap. I.* heading the brief keeps) |
| **C** vote + 173 plate crops + lost-runs check | 180K | 18K | **30**: see below; stages 4–5 not run |

**Reference.** Outside 32 spots, all four texts (A, B, C, Fordham) agree word for word, and three of them are
independent readings. The 32 spots were ruled on the plate. The coordinator also read pp. 3 and 11 against
the plates word by word: A matches exactly except the *a*.

**C's 30 errors, by kind:**
- lost runs that no scan has: the last printed line of pp. 3 and 4, and on p. 11 nine line openings after
  a hyphen (*concer-*|*nunt. Tercio*: *nunt. Tercio* lost);
- scan scars stages 4/4b would fix (*lesus* ×4, *tanof quam*, *f uit*, *philo sophi*, *Yeteris*, a folio
  bar read as *I*);
- English side-note words (*the*, *also*, *of*) and a footnote block (p. 9) in the Latin;
- a dropped numeral (*Epistula 3ᵃ*).

The lost lines are the M2 lesson again: correlated layout loss is invisible to a vote. Arm C would
need the full-text Fordham diff to find them, and the plate to fix them.

## What it means

1. **Blind transcription is the cheapest accurate arm.** 0 errors in ≈2,780 words. That's a small
   sample: by the rule of three, the true rate is under ~1 per 1,000 at 95%. It also costs half of C's
   plate pass.
2. **A costs about the same but anchors.** It caught 12 of the 13 Fordham errors in scope and kept one.
   Anchoring is the failure a reviewer cannot see.
3. **B's step 2 was the waste.** 78K for 14 items, because the agent opened whole pages. 12 of the 14 were
   Fordham non-words or truncations that a script can rule (one side a non-word or a cut-off fragment, the
   other a dictionary word). With crops for the remainder, step 2 drops to a few K per volume.
4. **Fordham covers ≈94% of the volume's words.** 12 pages are mostly missing (1, 2, 6, 15, 19, 41, 73, 94,
   101, 113, 128, 144). There, B's second witness should be the vote text, which is free once stages 1–2
   have run.

## Proposed method (for Wilson's ruling, not yet in WORKFLOW)

**B+**: a blind Sonnet transcription per page. A script diffs it against Fordham and the vote text. Where
the other side is a non-word or a fragment, the script rules it; only real word-against-word disputes go
to a Sonnet crop read. Projected for the volume: ≈230 pages × ≈10K ≈ **2.3–2.5M**, against C ≈ 18K/page
before stages 4–5 (≈4M+) and A ≈ 2.6M with anchoring risk. Stages 4/4b and the lost-runs pass (3b) would
retire for volumes run this way. Boundaries, italics, side-notes and apparatus still come from the scans.

**Not tested:** Loserth's volumes, which have no Fordham on some (B+ would then rest on the vote alone);
pages with dense apparatus or verse; side-notes.

## Files
`pilot-latin/`: `BRIEF-A.md`, `BRIEF-B.md`, `armA/` (+ `changes.tsv`), `armB/`, `armB2/`,
`armB_adjudicated.tsv`, `armC/` (vote text after decisions; `armC_s/` without page headers),
`armC/lostruns_reads.tsv`, `disputes_CA.tsv`, `disputes_CB.tsv`, `diff.py`. Stage-3 plate decisions for
pp. 3–12 are real output: `text/incarnacione/plate_decisions.tsv`.
