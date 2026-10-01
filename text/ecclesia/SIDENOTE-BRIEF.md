# Side-note pass brief: *De ecclesia* (Loserth 1886), WORKFLOW stage 5

You read crop sheets of Loserth's English side-notes (his marginal summaries) and record what the
PRINT has, and at which line. You do not translate, paraphrase or improve them.

**How the drafts were made.** Each note was re-OCR'd with tesseract from the margin column alone
(`scripts/w3/sideocr.py`). A control of 16 notes with no flag was exact, line included, so notes
with no flag ship as they are. **You read only the notes a marker fired on**, plus the places where
the archive OCR saw margin words and the re-OCR found no note (`missed`).

**Inputs (repo `~/wyclif`):** `text/ecclesia/sidecrops/sheet_NNN.jpg` + `sheet_NNN.tsv` (columns
`band id page leaf flags draft`). Each band shows the margin column and the edge of the Latin. The
blue label at the left of each Latin row is that row's printed **page.line**, written at its
baseline. Full page images if a band is cut off: `text/ecclesia/raw/leaves/nLLLL.jpg`.

**For every band, in order:**
1. Find the note the draft means and read it **exactly as printed**: Loserth's spelling and
   punctuation (*shew*, *honour*, *predestinate*), his numbering (*1.*, *a.*, *b.*), his capitals.
   A word hyphenated at a line-break is joined (*predes-/tinate* → *predestinate*); a hyphen that
   is part of the word stays (*wrong-doer* if printed so).
2. `line` = the label beside the note's **first** line. If the first line sits between two labels,
   take the one its baseline is level with.
3. Write one row. `text`:
   - `ok` if the draft (after its `page.line:`) is right letter for letter and the line is right;
   - the note as printed, if the draft is wrong anywhere (a letter, a lost word, two notes run
     together, a note cut in two);
   - `∅` if there is no side-note there: a page number of the running head, a printed line number
     (5, 10, 15 …), a folio mark (`131c`, `*`), an alinea letter (A, B, C …), a speck.
4. The band shows more than one note, or the draft runs two notes together: one row per note in
   the print, the first with the band's `id`, each further one with id `+`. A note the draft cut in
   two: give the whole note on the first part's row and `∅` on the other part's row (it has its
   own band or id; if it has none, say so in your report).
5. `missed` bands (id `M`): write each side-note you see there with id `M`, or one row `∅` if the
   band shows none (the archive OCR saw something else, or the note is already in a neighbouring
   band; then `∅`).

⛔ Read only the ink. Do not complete a note that is cut off by the band from what it "should"
say: open the full leaf image (leaf = page + 37) and read it there.

**Output: your part file only**, `text/ecclesia/sidenotes.reads.partNN.tsv`, header then one row
per read, tab-separated:

    band	id	page	line	text

Write it **once**, at the end (or once per 10 sheets if you prefer a checkpoint, rewriting the
whole file each time). Read **four sheets per turn** (four Read calls in one message): every turn
re-sends your whole context, so fewer turns is cheaper.

**Report** (your final message, short): sheets read, rows written, counts of ok / corrected / ∅ /
added, and anything you could not settle (band number + why). Do not paste the rows.
