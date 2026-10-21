# B+ crop read: *De benedicta incarnacione* (Harris 1886), 2026-10-21

Each item is a place where a blind transcription (`bt`) disagrees with both OCR witnesses (`fordham`, `vote`), or
has words neither has. Decide what the PRINT has. The red box marks the whole printed line; the word(s) are in
the item's `forms`. Read the whole line, exactly as printed (medieval spelling, no normalising).

**Inputs:** `text/incarnacione/crops_bplus/sheet_NNN.jpg` + `sheet_NNN.tsv` (columns `n page pos rule forms`).
If a strip is not enough, the full page is `text/incarnacione/raw/leaves/nLLLL.jpg` (LLLL = page + 39, four
digits). Read no other file.

**`reading`, by rule:**
- `SUB` / `BT-ONLY`: the print's words for the `bt=` run, exactly as printed. If the print has the `bt` words,
  `reading` = the `bt` run. If the print has nothing there (the transcriber added it), `∅`. Main-column text only:
  margin side-notes, margin sigla and footnotes are never the reading.
- `OMIT`: the words the print has after `after=` that the transcription left out, or `∅` if none.

**Output:** `text/incarnacione/bplus_decisions.tsv`, header `page	pos	rule	forms	reading	note`, one row per
sheet row, `page pos rule forms` copied EXACTLY from the sheet `.tsv`. `note`: what the ink showed, briefly
("print = bt" when the transcription was right). Write the file once at the end.

**Report back** (short): rows written, how many the transcription had right, every row where it was wrong
(page, bt, print), any you could not decide.
