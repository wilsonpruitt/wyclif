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

## ✅ Stage 7, first chunk: `prol-a` translated 2026-11-06 (Opus agent, 113K; commit 3a58d352, local)

795 Latin words, 20 notes (dense: the compendium is all references), lint clean, 1 Cor 10:16 bible.py-checked.
Headnote has 4 `[verify]` (date c. 1379–80; Oxford 1381 / Blackfriars 1382; Bohemian reception; no complete
English translation). Ledger **Kprola-1…10** appended (to-verify; Gratian D. 2 cc. 27, 42, 49 and X 3.41.6 → Friedberg).
Agent's open points, for the reviewer and the coordinator:
- **To rule before ch. 2:** *solvit / dissolvit* (answer / resolve? the compendium alternates them);
  *predicacio ydemptica / tropica* (identical / tropical predication — the treatise's key pair).
- Other glossary proposals: *hostia* host · *panis* bread · *substancia* substance · *accidens sine subiecto* accident
  without a subject · *figurative* figuratively · *sacramentaliter* sacramentally · *invisibiliter* invisibly ·
  *fingere* (miracles) feign · *esus corporalis / spiritualis* bodily / spiritual eating · *novella ecclesia* the
  newer church (per *novelli*) · *confeccio* consecration.
- Latin: 2.4–5 *.Beringarii*, *.Jeronimi* — stray stop, probably an OCR scar (plate p. 2 = n73; fix by tokenfix +
  relatin while NO agent runs). 1.24–2.5 whether the three decrees resolve the objections or ground them (C n. 8).
  3.22 print *varietate* kept vs ABCD *vanitate* (T n. 16). 4.20 whose *sanctitas* (C n. 19). Apparatus scars:
  p. 3 l. 22 "ARGQ" ≈ ABCD, p. 1 "1>" ≈ D.

## ✅ First-chunk review DONE and applied 2026-11-06 (Fable review, Sonnet coordinator close-out)

`_review/REVIEW-prol-a.md`: 1 error, 9 weak, 16 style (+ the plate read). All rows applied to `prol-a` (26 rows;
notes renumbered, a new C note 1 on *sentencia*); 2.4–5 stops removed from `bt/p002.txt` (ink flecks on n0073),
full vote re-run (same counts, queue 0) + `relatin.py` (dry run 0). Wilson's rulings: *solvere / dissolvere* both
"resolve"; the 13 mode adverbs one row each; *sentencia (verborum)* "sense" a separate row. 38 new GLOSSARY
rows (15 + 23 delegated), logged in CONVENTIONS. CARD updated (reviewed, not DRAFT). Scaffold front matter:
Fordham wording removed from all 93 chunks and from `chapters.py` (conditional on slug). Ledger Kprola-1
reworded, note numbers +1.

⬜ Still open before the waves:
- ✅ **Headnote "Occasion"** settled 2026-11-07 from Loserth Introd. §4 (pp. LX–LXII, read in the
  `latinworks13wycl` djvu text): "before 1382–1383", last four years of Wyclif's life, contemporary with
  *Sermones* III (325 ≈ *Sermo* III.25), *De blasphemia* later. ⚠ His third argument (the treatise never says
  *substancia*/*materialis* of the bread) **fails on the printed text**: *substancia panis* in Wyclif's own voice
  at 34.19, 131.19 (≈13 hits in all); the headnote says so. Matthew (Introd. §1, *EHR* 1890) puts the Oxford
  condemnation before Berton left office 30 May 1381. Modern c. 1379–80 stays `[verify]`. Chunks of a live
  volume stay `status: translated` (*De incarn.* 61/61), so no status change.
- ✅ **Italics field** settled: plate n73 confirms 2.24 *panem et calicem;* in italic (already quoted in the
  English); `italics.tsv` p. 4 *Ego Beringarius* is 4.31 → **prol-b**. ⚠ `italics.tsv` page numbers drift (its
  other "p. 2" rows are ch. 1 text): check against `bt/` by text, not by page.
- **The waves** (3 chunks per brief, Opus, stage-8 per-wave checks): ≈16–18M, its own "which model, and go?".
  `prol-b`, `prol-c` first, then `01-a…`.

## Open (non-blocking)

- Loserth notes Hus's and the Hussites' reuse in his Introd. §3 (pp. ~XXXV–LX): R notes where the apparatus
  marks it.
- The *Questio*'s remainder is Hus's (*De tribus dubiis*, 1412): not in this volume, not ours.

## Waves (stage 7–8), from 2026-11-07

Waves 1–6 done (prol-b … 03-f; 21 of 93 chunks), each followed by connectives + ledger checks; see git log and
CONVENTIONS for the per-wave GLOSSARY rulings. Tooling: `WAVE-PROMPTS.md`, `_connectives/`, `_verify/` (apply.py
warns on unparsed note changes). ⚠ For stage 10 (site): several GLOSSARY keys are shared by two rows of different
sense (*continuacio*, *sentencia*, *cognacio*, *conficere*, *species*): the hover may show the wrong row. Fix in the
site build (key on the row whose sense the chunk note names) or split keys before deploying.
- For the headnote / close-out: in ch. 3 (03-d, K03d-1/4) Wyclif turns Ockham's own parsimony argument (*De sacramento altaris* c. 28) against him on quantity; worth a sentence in "Where it is answered" or a chapter headnote.

## ⏸ PAUSED 2026-11-07 after wave 23 (Wilson: "pause after the next wave")

**Done:** prol-a … 08-j translated = **69 of 93 chunks**; every wave checked (connectives + ledger) through
wave 23 once RESULTS-23 is applied (see git log). All local commits; **nothing pushed, nothing deployed.**

**Restart:** the next brief is `brief.py eucharistia 09-a 09-b 09-c`, then 09-d…09-n (14 chunks, ~5 waves), then
`pen01…pen06` and `quest` (7 chunks, ~3 waves) — **24 chunks left, ~8 waves**. Per wave: translate (Opus) →
glossary census + Latin-checked conform → ledger rows → commit → connectives + ledger agents
(`WAVE-PROMPTS.md`; ledger prompt must demand quoted note changes and notes-only targets) → apply → commit.
`pen01` starts a second work (*De eucharistia et penitencia*, its own sigla A–F and headnote; see CARD).

**Measured cost:** translation ≈150–190K per 3-chunk wave; connectives ≈65–80K; ledger ≈100–160K. ≈0.4M per
wave all in; the remaining ~8 waves ≈3.3M.

**Settled:** *Eucharist* capitalised (Wilson 2026-11-07, conformed).

**Open for the close-out (stage 9) / site (stage 10):**
- Shared GLOSSARY keys with two senses (*continuacio, sentencia, cognacio, conficere, species, fantasticus,
  singulariter, per se*…): the site hover needs to pick the row the note names.
- Headnote sentence on Wyclif answering Ockham (*De sacr. alt.* c. 28) in ch. 3.
- Untraced rows listed in LEDGER (status `untraced`); e.g. K08i-5 wants the Aristoteles Latinus *Liber sex principiorum*, K08j-2 may be Loserth's italics for emphasis only; K08h-2 Averroes not read.
- *Dialogus* and *De ecclesia* have `(LEDGER …)` in English body text (site scrub handles it; check after build).

