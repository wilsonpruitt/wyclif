# Plate pass brief: *De ecclesia* (Loserth 1886), CONVENTIONS §3.4

You read crop sheets of the printed Latin and record what the PRINT has. You do not translate,
emend, or judge the sense.

**Inputs (repo `~/wyclif`):** `text/ecclesia/crops/sheet_NNN.jpg` + `sheet_NNN.tsv` (columns
`n page pos rule forms`). Each sheet stacks up to 8 numbered strips: the line holding the word
(boxed in red) with the line above and below. Full page images: `text/ecclesia/raw/leaves/nLLLL.jpg`
(leaf = page + 37).

**For every row of your sheets, in order:**
1. Read the WHOLE middle line, not just the boxed word (the error class lives in the neighbours).
2. Decide what the print has at the box, **exactly as printed**: medieval spelling kept (*eciam*,
   *racio*, *ymmo*, *michi*), the editor's u/v and i/j as printed, degree-sign ordinals kept (*XIII°*),
   the editor's brackets kept. `∅` if the print has no word there.
3. Not decisive on the strip (t/l, c/e, a degree sign, a broken letter)? Open the full page image
   and look closely at that word before deciding. ⛔ Never decide on the sense, on the Vulgate, or on
   what the Latin "should" be. Only on the ink.
4. Write one row.

**By rule:**
- `R3 / R4 / R5 / R6 / THIN / DEL / INS? / NW`: `reading` = the single printed word at the box
  (or `∅`). NW rows are words every scan read the same way, where the reading may be a shared
  misreading (*pnncipio* for *principio*) OR the print's genuine spelling. The print decides.
- `HEAD`: `reading` = the full heading line as printed (e.g. `CAP. XVII.`).
- `GAP / TAIL`: the other scans say lines are missing here; `forms` holds their text. `reading` =
  the whole run of words the print has at that point, exactly as printed, space-separated (the
  page's lost line(s)), or `∅` if the print has nothing there (then the scans were wrong).
- A line number (5, 10, 15 …) in the margin, a folio mark (`*`, `130b`), or an alinea letter is NOT
  text: if the boxed item is one, `reading` = `∅` and say so in the note.

**Conventions settled on sheets 1–40 (keep them):**
- Superscripts as printed: `Iª`, `XXIVª`, `III°`; no trailing punctuation in `reading`.
- A word hyphenated across lines: if the main scan's token holds the whole word, give the whole word;
  if it holds one half, give that half as printed (`sal-` then `vator`). The pipeline joins them.
- Where the main scan's one token covers two printed words, give both (`Timothei IV°`).
- Old-style arabic `1` and capital `I` look alike (*q. 1* vs *q. I*): decide on height, zoom the leaf.
- Glued folio marks (`130b`), line numbers, margin letters (a b c), or English side-note words: the
  reading is the Latin word alone; a standalone English word is `∅`.
- Text from the footnote block picked up by one scan: `∅` (notes are not the reading text).

**Output:** append rows to the file named in your task (NOT `plate_decisions.tsv` itself), TSV with
header `page	pos	rule	forms	reading	note`. Copy `page`, `pos`, `rule`, `forms` **exactly** from
the sheet's `.tsv` (the vote matches decisions on them). `note` = how the ink decided it, briefly
(e.g. "short ascender with crossbar = t", "15 is the line number"), empty when plain.

**Report back** (short): sheets done, rows written, and any row you could not decide (leave it out
of the file and list it with page/pos).
