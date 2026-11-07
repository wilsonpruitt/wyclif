# Per-wave agent prompts — *De eucharistia* (WORKFLOW stage 8). Fill {…}. Opus, at most 2 at once (never while a
# translation agent is writing the same chunks; never alongside `relatin.py`).

Adapted from `chunks/ecclesia/CLOSEOUT-PROMPTS.md` §§B–C so these checks run per wave, not at the end.

## B. Connective check — wave {W}

Build: `.venv/bin/python chunks/eucharistia/_connectives/extract.py {W} <chunk ids>` → `body-{W}.md`.
Apply: `.venv/bin/python chunks/eucharistia/_connectives/apply.py {W}` (exact `was` → `now`, once-only).

> You are checking *sed* and *autem* in Wyclif, *De eucharistia* (ed. Loserth), ~/wyclif. Read
> `chunks/eucharistia/CARD.md` § "The four error classes", item 2 (connective table and the "now" rule), and
> `chunks/ecclesia/_connectives/RESULTS-01.md` (your format and the classes, worked). Then read
> `chunks/eucharistia/_connectives/body-{W}.md`: each ¶ gives the Latin (every *sed/autem* in **bold**) and
> our English. For EVERY bold occurrence decide: (a) minor premiss / next step → "now"; (b) adversative →
> "but"; (c) continuative *autem* → "and"; *non … sed* → "but" ("rather" is *ymmo/pocius*). Check the
> English has it, rendered per its class; an omitted *sed/autem* is an error unless the English
> construction carries it (say how).
> Do NOT edit chunks. Write ONE file `chunks/eucharistia/_connectives/RESULTS-{W}.md`: ## Changes (table:
> chunk | page | Latin phrase | was | now | reason — "was"/"now" exact English strings, each occurring once in
> the chunk, so a find/replace works) · ## Doubtful, left as they are · ## Totals (occurrences checked, by
> class; changes). Changes only where the card decides it; a defensible reading stays and goes under Doubtful
> if it is a real toss-up. Reply in under 60 words.

## C. LEDGER — wave {W}

Rows: `chunks/eucharistia/_verify/rows-{W}.md` (the wave's to-verify / editor rows, cut from LEDGER.md).

> You are closing source-identification rows for Wyclif, *De eucharistia* (ed. Loserth 1892), in ~/wyclif.
> Your rows: `chunks/eucharistia/_verify/rows-{W}.md`. For each row, find the claim's source and check it:
> work, locus, wording against Wyclif's Latin (in the chunk named in column 2,
> `chunks/eucharistia/wyc-eucharistia-NN-x.md`; the Latin is in the `>` lines, the note is `[^n]`).
> Do NOT edit LEDGER.md or any chunk. Write ONE file `chunks/eucharistia/_verify/RESULTS-{W}.md`.
>
> Sources. Local PL TEI: ~/patrologia/sources/pl/tei/*.xml (`grep -l` a distinctive phrase; Gratian =
> 21354.xml). Wyclif's other works, Society OCR: `sources/ia-ocr/latinworksNNwycl.txt` (which volume is which:
> `sources/wyclif_society_archive_org.csv`); Loserth's own foot-notes and introduction to this work are in
> latinworks13wycl.txt (and `_djvu.txt`). Scripture: `.venv/bin/python scripts/w3/bible.py "Luc 17:23"`. Friedberg OCR:
> archive.org BD1141951 (Decretum), BD1141952 (Decretals): `curl -sL https://archive.org/download/<ID>/<ID>_djvu.txt`
> into your scratchpad once, grep with ' +' between words. Web (WebFetch / archive.org advancedsearch):
> corpusthomisticum.org (Thomas), perseus.tufts.edu or the Bekker text for Aristotle, archive.org for
> FitzRalph's *Summa in quaestionibus Armenorum* (Paris 1511/12) and Hus's *De ecclesia*, thelatinlibrary.com.
> Never grep the whole PL with -r on a broad pattern twice; narrow by phrase.
>
> Each row ends in exactly one status: `verified` (you read the source at that locus; give source + locus +
> how, dated {DATE}), `editor` (Loserth's identification, which you could not check further but which he
> gives explicitly — quote his foot or apparatus), or `untraced` (looked for in at least the obvious two places; say
> where). "Not local" is not a reason to stop: try the web source. For a wrong identification, give the
> corrected one. Where the chunk note overstates (asserts what is now untraced, or a wrong locus), give the
> exact replacement note text (chunk, note number, old phrase → new phrase). Format: a table
> `id | status | how / source | note change (or —)`, then a short list of anything the coordinator must
> decide. Be economical: don't re-read a source for each row that shares it. Reply in under 60 words.

## Notes carried from *De incarn.* (2026-10-22)

- Ledger ids are `K…` (`Kprolb-1`, `K01a-1`, `Kpen01-1`, `Kquest-1`); `_verify/apply.py` matches those. Note
  changes as `01-a n3: "old exact phrase" → "new phrase"` (also `prol-b n3`, `pen01 n2`, `quest n1`), no `|` inside
  a row, never an empty cell (use —); point the agent at earlier RESULTS-*.md for shared sources. A failed apply has
  already written the rows before it: `git checkout` the files and re-run.
- Ledger agents: Wyclif often takes his fathers **through Scotus (Ord. IV d. 8–13 for the eucharist) and
  Bonaventure / Thomas on IV Sent.**; Gratian *De cons.* D. 2 is the eucharist distinction (Friedberg I).
- A bt fix that removes or adds a token shifts B+ positions on that page: re-run bplus.py (queue must be 0).
- (2026-11-07, wave 3) Tell the ledger agent: **no plain `"` inside a quoted old/new phrase** — write `\"` or use
  typographic quotes / italics. RESULTS-3 had two (`OCR "LXXVf"`) that apply.py skipped silently; it now prints
  `WARN … not parsed` — apply those by hand.
