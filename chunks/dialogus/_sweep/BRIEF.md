# Plate pass brief — majority-error sweep + open Latin doubts (Dialogus close-out, 2026-09-29)

Two queues, both settled by reading Pollard's printed page (the plates), not by the witnesses:

1. `chunks/dialogus/_sweep/candidates.tsv` (37 rows: form, count, pages[, fixes]). Forms in the established
   Latin (`text/dialogus/pNNN.la.txt`) that Hunspell-Latin rejects and that look like OCR confusions shared
   by a MAJORITY of witnesses (the *Chnstus* class: 4 of 6 witnesses shared it). Many will turn out to be
   genuine medieval forms printed so (e.g. *poterint*, *crederit*, *wult*) — that is a fine outcome.
   ⚠ `catalog/lexicon/agreed.txt` is contaminated (contains *chnstus*): never use it as evidence.
2. `chunks/dialogus/LATIN-DOUBTS.md` (28 rows LD-01…28): the table says what settles each.
   (Also: its closed list at the foot is already done — skip.)

## How to read a plate
- Leaf = printed page + 31. Image: `text/dialogus/raw/leaves/nLEAF.jpg` (4-digit zero-padded name, e.g.
  n0105.jpg); if missing: `curl -sL -o text/dialogus/raw/leaves/n0105.jpg https://archive.org/download/latinworks22wycl/page/n105.jpg`.
- Images are ~2672×4601. Crop the region with `sips -c HEIGHT WIDTH --cropOffset Y X in.jpg --out
  $SCRATCH/crop.jpg` then `sips -Z 1600` and Read it. Text lines run ~ y=450…3900; the apparatus is at
  the foot. Find the line by the printed line numbers in the margin (every 5th) and neighbouring words.
  Read the WHOLE line, not just the word; for sweep forms find the word via `grep -n` on the la.txt first.
- ⚠ Never rebuild a word across the side-note gutter. Letterform traps: rn/m, ni/h, c/e, u/n, long-s/f.

## Decide, per item
- **Print confirms the form** (a genuine medieval/printed form, or Pollard's own misprint): no Latin change.
  Sweep items: note "print confirms". LD items: the chunk's existing T/C note stands → mark closed.
- **Print differs from our established Latin** (a shared OCR error): this is a fix. Do ALL of:
  (a) append an OVERRIDE row to `text/dialogus/plate_decisions.tsv` in the existing format
      (`page pos OVERRIDE forms reading note`; get `pos`/`forms` by running
      `cd ~/wyclif && W3_DUMP=PAGE .venv/bin/python scripts/w3/vote.py dialogus 2>/dev/null | grep -n WORD` — if that is
      awkward, write the row with pos `?` and say so in your report; the coordinator will finish it);
  (b) regenerate the page: `cd ~/wyclif && .venv/bin/python scripts/w3/vote.py dialogus PAGE PAGE` (tested
      2026-09-29: a no-op on an unchanged page). Then `git diff text/dialogus/pNNN.la.txt` must show ONLY your
      fix. If it shows more, `git checkout text/dialogus/pNNN.la.txt pNNN.check.tsv` and hand-edit the word instead;
  (c) fix the same word in the chunk's Latin blockquote (`chunks/dialogus/wyc-dialogus-NN.md`; find by grep);
  (d) if the fix changes the sense, report the English sentence affected — do NOT rewrite the English;
      if a note says "left as printed"/"not a word", report it for rewording.
- **Emendation questions** (LD rows where the print is clear but may be wrong, e.g. *corporia*, *sapientem*,
  *senefectiore*): don't emend. Record what the plate AND Pollard's apparatus show, and give a recommendation.

## Output
Write `chunks/dialogus/_sweep/RESULTS.md`: one table for the sweep (form | page.line | plate reads | verdict |
action taken) and one for the LDs (id | plate reads | apparatus | verdict | action / recommendation), then a
list "English/notes to revise" with file, note/line, and why. Mark LEDGER-style dates "plate 2026-09-29".
Do not commit. Final message ≤200 words: counts, every Latin fix made, every recommendation needing a ruling.
Machine has 8 GB RAM: one image at a time, delete crops as you go, no background jobs.
