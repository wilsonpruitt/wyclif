# RESUME — *De eucharistia* (ed. Loserth 1892; the second B+ volume, the first with no Fordham)

*Read this first in a new session, then `WORKFLOW.md` (stages 7–10) and this volume's `CARD.md`. Stages 1–6 ran
2026-11-06 on Wilson's "in opus, get started" + "yes. go" (revised estimate ≈4.2M, mostly Sonnet).*

## ✅ STAGES 1–6 DONE 2026-11-06 — the Latin is established, 93 scaffolds written

- **Volume:** archive.org `latinworks13wycl`, **leaf = page + 71** (visual: p. 2 = n73, p. 358 index = n429), text
  pp. 1–348: the compendium under "Prologus" (pp. 1–10), the *Tractatus de eucharistia* Cap. I–IX (pp. 11–326),
  *De eucharistia et penitencia sive de confessione* Cap. I–VI (title p. 327, text pp. 329–343), the *Questio ad
  fratres de sacramento altaris* (title p. 345, text pp. 347–348). Blank: pp. 328, 344, 346. Indexes from p. 349.
- **Witnesses:** 4 scans (`india.history.resource.90246` skipped: malformed djvu.xml). **No Fordham.**
- **B+ (stage 2B):** 35 Sonnet transcription agents (10 pages each) ≈ 3.35M (≈9.6K/page, as *De incarn.*).
  Check against the vote alone: 75,380 words, 73,886 supported, 955 runs by rule (audited: every single-letter
  disagreement is an OCR non-word, no reader "correction" hiding), 241 to the plate (1 Sonnet agent, 0.21M):
  **4 transcription errors** (62 *subrepserant*, 111 *impericiores*, 281 *curremus*, 332 *liganti*), all fixed by
  decision; queue 0, stale 0. ⇒ **A volume with no Fordham works under B+**; the vote alone sends ~0.7 items/page.
- **Coordinator fixes to `bt/`** (log: `text/eucharistia/bt_normalised.tsv`): ⚠ **line markers one line late on 41
  even pages** (numbers in the right margin; the transcribers numbered the line below) — every marker on those
  pages moved up, plate-checked on pp. 4, 42, 46, 48, 236; the 13 pages still reported by bplus are heading pages
  where Loserth counts the heading line (markers right). Three vowel "accents" (type blemishes) plain; `[?…]`
  guesses unbracketed (all then supported by the vote); p. 211 `.exposui):` (the parenthesis opens on p. 210);
  p. 322 margin numerals written as text → markers; p. 348 Loserth's apparatus note to l. 5 removed from the column;
  p. 42 an invented blank `25|` line removed. ⇒ **BT-BRIEF lesson:** say "the margin number belongs to the line it
  stands level with; count from the top" — the late-marker slip is systematic on right-margin pages.
- **Side-notes (stage 5):** tesseract re-OCR 645 notes, 284 flagged → 3 Sonnet agents (0.40M); control of 11
  unflagged notes 11/11 exact; then a real-word OCR sweep found 9 more (*cat*/eat, *ditferent* ×3, *tor*/for ×2,
  *trom*/from — that one plate-read —, *Weight*, *Different.*): fixed in `sidenotes.reads.part99.tsv`. Kept as
  Loserth printed: *begger* (239.15), *doubtled* (240.12). 553 notes ship, all placed. ⚠ `sidesheets.py --spot`
  wipes `sidecrops/`: move it aside first (done: `sidecrops.spot/`).
- **Italics:** `italics.py` 1,094 runs on 174 pages (page heads read only 103/438: drift; card warns).
- **Scaffolds:** `chapters.py` gained `parts=` (a second work restarts at Cap. I under an id prefix). 93 chunks:
  `prol-a…c`, `01-a…09-n` (79), `pen01…pen06`, `quest`. `boundaries.py`: 0 (the transcription reads ¶ from the
  indents).
- **Card:** `CARD.md` (DRAFT until the first-chunk review): Loserth's print governs; two works, two sets of sigla
  (A–E / A–F); ledger prefix **K**; the eucharistic vocabulary expected (most terms have no GLOSSARY row yet:
  propose, coordinator rules); predication rule from *De incarn.* adapted (*Hoc est corpus meum*).
- **Cost, stages 1–6:** agents ≈3.96M (Sonnet) + coordinator (Opus). The ≈2.3M in the 2026-10-12 scope did not
  price the transcription.

## ▶ Next: stage 7, after Wilson's "which model, and go?"

1. **First chunk** `prol-a` (the compendium + the volume headnote): `brief.py eucharistia prol-a` is built
   (`_briefs/eucharistia-prol-a-prol-a.md`, ≈16K). Translate (Opus), then the **four-class review in a fresh
   session** (Fable, as *De incarn.*: this volume's term set — *sacramentaliter / realiter / figurative /
   ydemptice*, *accidens sine subiecto*, *remanencia* — is GLOSSARY work that compounds). Card changes land
   before the rest run.
2. Then the waves (3 chunks per brief, Opus), with the stage-8 per-wave checks (ledger K-rows, connectives,
   glossary conform). Estimate for translation + close-out, re-measured on *De incarn.* / *De pot. pape*: ≈16–18M.

## Open (non-blocking)

- Loserth notes Hus's and the Hussites' reuse in his Introd. §3 (pp. ~XXXV–LX): R notes where the apparatus
  marks it.
- The *Questio*'s remainder is Hus's (*De tribus dubiis*, 1412): not in this volume, not ours.
