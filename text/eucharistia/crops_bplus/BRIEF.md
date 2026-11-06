# B+ crop read: *De eucharistia* (Loserth 1892), 2026-11-06

Each item is a place where a blind transcription (`bt`) disagrees with the four-scan OCR vote (`vote`; this volume has no Fordham text), or
has words neither has. Decide what the PRINT has. The red box marks the whole printed line; the word(s) are in
the item's `forms`. Read the whole line, exactly as printed (medieval spelling, no normalising).

**Inputs:** `text/eucharistia/crops_bplus/sheet_NNN.jpg` + `sheet_NNN.tsv` (columns `n page pos rule forms`).
If a strip is not enough, the full page is `text/eucharistia/raw/leaves/nLLLL.jpg` (LLLL = page + 71, four
digits). Read no other file.

**`reading`, by rule:**
- `SUB` / `BT-ONLY`: the print's words for the `bt=` run, exactly as printed. If the print has the `bt` words,
  `reading` = the `bt` run. If the print has nothing there (the transcriber added it), `∅`. Main-column text only:
  margin side-notes, margin sigla and footnotes are never the reading.
- `OMIT`: the words the print has after `after=` that the transcription left out, or `∅` if none.

**Output:** `text/eucharistia/bplus_decisions.tsv`, header `page	pos	rule	forms	reading	note`, one row per
sheet row, `page pos rule forms` copied EXACTLY from the sheet `.tsv`. `note`: what the ink showed, briefly
("print = bt" when the transcription was right). Write the file once at the end.

**Report back** (short): rows written, how many the transcription had right, every row where it was wrong
(page, bt, print), any you could not decide.

**This volume:** the vote often loses words at the line edge beside a side-note (the box swallows them in every scan),
so many `BT-ONLY` runs are real print the OCR lost: read the line and keep them if the ink has them. Superscript
ordinals (`VIᵒ`, `Iª`) are print when the plate shows the raised letter. Loserth's own misprints stay as printed.
