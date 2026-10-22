# Per-wave agent prompts — *De benedicta incarnacione* (WORKFLOW stage 8). Fill {…}. Opus, at most 2 at once.

Adapted from `chunks/ecclesia/CLOSEOUT-PROMPTS.md` §§B–C so these checks run per wave, not at the end.

## B. Connective check — wave {W}

Build: `.venv/bin/python chunks/incarnacione/_connectives/extract.py {W} <chunk ids>` → `body-{W}.md`.
Apply: `.venv/bin/python chunks/incarnacione/_connectives/apply.py {W}` (exact `was` → `now`, once-only).

> You are checking *sed* and *autem* in Wyclif, *De benedicta incarnacione* (ed. Harris), ~/wyclif. Read
> `chunks/incarnacione/CARD.md` § "The four error classes", item 2 (connective table and the "now" rule), and
> `chunks/ecclesia/_connectives/RESULTS-01.md` (your format and the classes, worked). Then read
> `chunks/incarnacione/_connectives/body-{W}.md`: each ¶ gives the Latin (every *sed/autem* in **bold**) and
> our English. For EVERY bold occurrence decide: (a) minor premiss / next step → "now"; (b) adversative →
> "but"; (c) continuative *autem* → "and"; *non … sed* → "but" ("rather" is *ymmo/pocius*). Check the
> English has it, rendered per its class; an omitted *sed/autem* is an error unless the English
> construction carries it (say how).
> Do NOT edit chunks. Write ONE file `chunks/incarnacione/_connectives/RESULTS-{W}.md`: ## Changes (table:
> chunk | page | Latin phrase | was | now | reason — "was"/"now" exact English strings, each occurring once in
> the chunk, so a find/replace works) · ## Doubtful, left as they are · ## Totals (occurrences checked, by
> class; changes). Changes only where the card decides it; a defensible reading stays and goes under Doubtful
> if it is a real toss-up. Reply in under 60 words.

## C. LEDGER — wave {W}

Rows: `chunks/incarnacione/_verify/rows-{W}.md` (the wave's to-verify / editor rows, cut from LEDGER.md).

> You are closing source-identification rows for Wyclif, *De benedicta incarnacione* (ed. Harris 1886), in ~/wyclif.
> Your rows: `chunks/incarnacione/_verify/rows-{W}.md`. For each row, find the claim's source and check it:
> work, locus, wording against Wyclif's Latin (in the chunk named in column 2,
> `chunks/incarnacione/wyc-incarnacione-NN-x.md`; the Latin is in the `>` lines, the note is `[^n]`).
> Do NOT edit LEDGER.md or any chunk. Write ONE file `chunks/incarnacione/_verify/RESULTS-{W}.md`.
>
> Sources. Local PL TEI: ~/patrologia/sources/pl/tei/*.xml (`grep -l` a distinctive phrase; Gratian =
> 21354.xml). Wyclif's other works, Society OCR: `sources/ia-ocr/latinworksNNwycl.txt` (which volume is which:
> `sources/wyclif_society_archive_org.csv`); Harris's own foot-notes and introduction to this work are in
> latinworks03wycl.txt. Scripture: `.venv/bin/python scripts/w3/bible.py "Luc 17:23"`. Friedberg OCR:
> archive.org BD1141951 (Decretum), BD1141952 (Decretals): `curl -sL https://archive.org/download/<ID>/<ID>_djvu.txt`
> into your scratchpad once, grep with ' +' between words. Web (WebFetch / archive.org advancedsearch):
> corpusthomisticum.org (Thomas), perseus.tufts.edu or the Bekker text for Aristotle, archive.org for
> FitzRalph's *Summa in quaestionibus Armenorum* (Paris 1511/12) and Hus's *De ecclesia*, thelatinlibrary.com.
> Never grep the whole PL with -r on a broad pattern twice; narrow by phrase.
>
> Each row ends in exactly one status: `verified` (you read the source at that locus; give source + locus +
> how, dated {DATE}), `editor` (Harris's identification, which you could not check further but which he
> gives explicitly — quote his foot), or `untraced` (looked for in at least the obvious two places; say
> where). "Not local" is not a reason to stop: try the web source. For a wrong identification, give the
> corrected one. Where the chunk note overstates (asserts what is now untraced, or a wrong locus), give the
> exact replacement note text (chunk, note number, old phrase → new phrase). Format: a table
> `id | status | how / source | note change (or —)`, then a short list of anything the coordinator must
> decide. Be economical: don't re-read a source for each row that shares it. Reply in under 60 words.

## Notes from waves 1–2 (2026-10-22)

- Ledger ids are `I…` (`P` is *De potestate pape*); `_verify/apply.py` matches `I\d\d[a-z]-n` and `Iprol-n`.
- Tell the ledger agent: note changes as `02-b n3: "old exact phrase" → "new phrase"`, no `|` inside a row, never an
  empty cell (use —); point it at earlier RESULTS-*.md for shared sources. A LEDGER row with an empty last cell breaks
  apply.py, and a failed apply has already written the rows before it: `git checkout` the files and re-run.
- Connective checks: waves 1–2 found 0 changes in 63 occurrences.
- A bt fix that removes or adds a token shifts B+ positions on that page: a `bplus_decisions.tsv` row for a later
  position then goes back to the queue. Shift its `pos` by hand and re-run bplus.py (queue must be 0).
- Ledger agents: Wyclif often takes his fathers **through Scotus (Ord. III) and Bonaventure (In III Sent.)**: Damascene's
  chapter numbers, *De sermone Domini*, a ps.-Augustine sermon cited as "Leo" (RESULTS-4, -8). Look there first when a
  patristic citation's number or attribution is odd.

