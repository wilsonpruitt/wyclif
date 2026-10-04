# WORKFLOW — one volume, from scans to site (from M5 on)

*The score for every volume after the Dialogus. Current volume: see `M5-RESUME.md`. Built from what the Dialogus measured (PLAN § Cost,
2026-09-29). Runs on the Claude Code plan, not the API (no API budget); `scripts/pilot/translate_api.py`
stays as the priced alternative. Hard stop before each volume: state the estimate, ask "which model, and go?"*

**The one cost rule.** Cost is round trips, not reading: every agent turn re-sends its whole context.
So each stage hands an agent everything it needs in one file, and the agent writes its output once.
Measured on Dialogus ch. 2 + 14: one agent per chunk ≈ 93k tokens/chunk; one agent per brief ≈ 55k/chunk;
the same shape as a single API call ≈ 40k/chunk at $0.22/page.

## Stages (SLUG = the volume, e.g. `ecclesia`)

1. **Witnesses.** `.venv/bin/python scripts/w3/witness.py SLUG` — all free scans + Fordham → token streams;
   also writes `sidenotes/SLUG.tsv` and **`text/SLUG/apparatus.json`** (the editor's page-foot apparatus,
   by leaf; the briefs need it). ⚠ *De ecclesia* and *De officio regis* must be rebuilt: delete their
   `text/SLUG/witnesses/` first (witness.py skips existing files).
2. **Vote.** `.venv/bin/python scripts/w3/vote.py SLUG` → `text/SLUG/pNNN.la.txt` + `plate_queue.tsv`.
3. **Plate pass (Latin).** `scripts/w3/crops.py SLUG` → crop sheets; one Opus agent per ~40 sheets writes
   `plate_decisions.tsv`; re-run vote.py.
4. **Majority-error sweep.** `.venv/bin/python scripts/w3/nonword.py SLUG` → `text/SLUG/nonwords.tsv`.
   Filter to OCR-confusion suspects (rn/m, ni/h, c/e, u/n, a bracket read as *j* …) and read those on the
   plates in the same pass as stage 3 or 5. Never trust `catalog/lexicon/agreed.txt` as evidence.
4b. **Scar sweep (from 2026-10-01; De ecclesia found ~600 scars left after stage 4).** vote.py's `scar_fix`
   now strips the character class (`%`, `3o`, quote marks, `numerUS`, alinea letters) on every run. Then:
   `python3 scripts/w3/pl_lexicon.py` (once per machine) → `scars.py SLUG` → `scarqueue.py SLUG`
   (rule fixes as `plate_decisions.part97.tsv`; the rest as `scar_queue.tsv`) → `crops.py SLUG --queue
   scar_queue.tsv --out crops_scars` → one **Sonnet** agent per ~9 sheets with `crops_scars/BRIEF.md` →
   readings as OVERRIDE rows → merge into `plate_decisions.tsv` → `vote.py` (stale must be 0) →
   `relatin.py SLUG` (Latin of DRAFT chunks only). Add confirmed pairs to `catalog/lexicon/ocr_artifacts.tsv`.
   Measured on *De ecclesia*: ~230 by rule, 142 on the plates, 224K tokens.
   One-off fixes no rule reaches and no position can carry: `text/SLUG/tokenfix.tsv` (page, printed, fixed),
   applied by the vote's writer. After any Latin change, `relatin.py SLUG --also <translated> --dry` must show 0.
   ⛔ **tokenfix repairs the OCR, never the print.** If the plate shows the "wrong" form (Loserth's misprint:
   *faciendo*, *69*, *novam* in *De ecclesia*), the Latin keeps it and the English follows a conjecture with a
   T note "our emendation" (standing rule). A row whose printed form is a real word or a numeral needs "plate:"
   in its note, i.e. it was read on the plate, not inferred.
5. **Scaffolds + side-notes.** `.venv/bin/python scripts/w3/chapters.py SLUG` → `chunks/SLUG/wyc-SLUG-NN.md`.
   Then ONE plate agent per ~10 chapters corrects the OCR side-notes against the plates (it is image work;
   kept out of translation, where it cost extra round trips). The same agent, on the same pages, does two
   more things (lessons of the *De ecclesia* close-out, which paid for them at the end instead):
   - **Italics — track, don't verify.** Italics are the editor's call (Loserth marking what he took for a
     quotation), not the manuscript's (Wilson, 2026-10-04). So: record the italic runs only as a by-product of
     this plate pass (page.line, first and last words → `text/SLUG/italics.tsv`), and `brief.py` inlines them
     (⬜ build before the next volume's stage 7) so the translator sees the editor's quotation bounds as
     evidence. No separate italics pass, no review rows for quotation bounds, no close-out check of them.
     First see whether a witness already carries italics (`vote.py` keeps an `it` flag per token, empty for
     *De ecclesia*); if the Fordham text or the hOCR has font styles, take them from there instead.
   - **Boundaries.** `python3 scripts/w3/boundaries.py SLUG` lists every ¶ or chunk end without a stop
     (*De ecclesia*: 58). Read each on the plate: a false ¶ break (an alinea letter read as a break) is
     merged before translation; it lost *plus* at 46.24 (and the S2 plate check found four more lost words).
     A merge needs a `vote.py` override (⬜ not built: a page/token list that clears the `para` flag), since
     `pNNN.la.txt` is regenerated on every vote. A chunk split inside a sentence is moved to the
     nearest stop (12-c ended on *patet*). Verse lines and headings stay.
6. **Volume card.** `chunks/SLUG/CARD.md`, adapted from `chunks/dialogus/CARD.md` (editor, sigla, the
   volume's register). Per PLAN, the FIRST chunk is translated and reviewed in a fresh session against the
   four classes before the rest run; card changes land before stage 7.
7. **Translate, in briefs.** `.venv/bin/python scripts/w3/brief.py SLUG NN NN NN` (3–5 chunks) →
   `chunks/SLUG/_briefs/…md` and the one-line agent prompt. One Opus agent per brief, one brief at a time
   (8 GB). Between briefs the coordinator rules glossary proposals (census + dikaiosune rule; Wilson for
   genuinely doubtful register) and commits.
8. **Per-wave checks, not at the end** (the Dialogus close-out cost 1.3M doing them at the end; *De ecclesia*
   ~5.3M, because two of these were skipped or deferred):
   - ledger rows from the agent's report → `LEDGER.md`, and verify THAT wave's rows against the sources
     (local PL at `~/patrologia/sources/pl/tei/`; `bible.py`; the editor's intro OCR). "Not local" is not a
     reason to defer: use the web sources in `chunks/ecclesia/CLOSEOUT-PROMPTS.md` §C (corpusthomisticum for
     Thomas incl. *In Sent.*; archive.org Friedberg, Quaracchi Bonaventure; Wyclif's own works in
     `sources/ia-ocr/`, *Summa* book 4 = *De civ. dom.* II, book 5 = *De civ. dom.* III). *De ecclesia*
     deferred 243 rows and paid ~1.9M to close them at the end;
   - *sed/autem*: run `chunks/ecclesia/_connectives/extract.py` adapted to the wave's chunks, and the check
     agent on it (~45K per brief), then `apply.py`. *De ecclesia* skipped this ("agent's own report only")
     and found 69 errors at the end, mostly a minor premiss before *ergo* rendered "but";
   - **glossary conform:** when a term is ruled, grep the already-translated chunks for it and conform tags,
     renderings and notes in the same commit. Most class-1 review rows were tags and notes that predated a
     ruling made on those very lines;
   - split-tag check (`grep -o '\]{g:[^}]*}[A-Za-z]'`) and `lint.py chunks/SLUG/*.md` (it now checks every
     tag key, incl. ones with spaces or capitals, which the site cannot render).
9. **Close-out.** A four-class review of the long, dense chunks only (short ones were clean), and the
   Latin doubts on the plates. If stages 5 and 8 ran as written, there is no connective pass and no ledger
   backlog here. Rewrite PLAN's cost row from the measured rate.
10. **Site.** `site/build.py` renders the Dialogus only: generalize it to render every translated work
    under `/SLUG/` and add the volume to `READ_NOW`; then `build.py` and the CLI deploy
    ([[reference_wyclif-deploy]] in memory; the Vercel project is NOT git-connected — keep it so).
    ⛔ Every deploy is Wilson's per-deploy OK.

## Standing traps (all met on the Dialogus)
- `bible.py` book aliases: check a new abbreviation resolves to the right book (Isaiah once returned 1 Samuel).
- Speaker and chapter structure comes from the Latin; data shown on the site must be computed, not written
  from expectation (the home-page caption was wrong once).
- The site's `scrub()` strips process words (LEDGER ids, scaffold, pilot, OVERRIDE, review codes); grep
  `site/dist` for leaks after every build.
- `vercel link` git-connects the project silently: run `npx vercel git disconnect` after any new link.
