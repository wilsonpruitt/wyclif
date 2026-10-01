# Scar plate pass: *De ecclesia* (2026-10-01)

Read `text/ecclesia/PLATE-BRIEF.md` first: its rules (read the WHOLE middle line, the print exactly as
printed, never decide on the sense, the conventions list) all hold here. This file only adds what is new.

**Inputs:** `text/ecclesia/crops_scars/sheet_NNN.jpg` + `sheet_NNN.tsv`, columns
`n page pos rule forms printed proposed`. The word in the red box is the one in `printed`: what our
established Latin currently has there. `proposed` is a machine guess and **about half the guesses are
wrong**: it is a hint, never evidence. Full pages: `text/ecclesia/raw/leaves/nLLLL.jpg`, LLLL = page + 37
padded to four digits.

**What `reading` is, by rule:**
- `LEFT-nw`, `W2`, `LEFT-eng`: the printed word(s) at the box exactly as printed. Many are genuine medieval
  spellings (*yemps*, *dampnificat*): then `reading` = `printed` (strip only junk the print lacks). If the print
  has two words where we have one, give both, space-separated (`est virgo`). An English side-note word or a
  margin letter glued on: the Latin word alone; nothing Latin at the box: `∅`.
- `S-split`: does the print have ONE word or TWO here? Give exactly what it has (`intrusor`, or `post diem`).
- `LEFT-ord`: the numeral with its ordinal mark as printed, modifier letters for superscripts
  (`CXXXIᵘᵐ`, `XXIIIª`, `III°`).
- `LEFT-punct`: the word with the stop or question mark the print has after it (`ecclesie?` or `ecclesie.`).

**Output:** your task names a file `text/ecclesia/scar_reads.partNN.tsv`. One row per sheet row, header
`page	pos	rule	forms	reading	note`, `page pos rule forms` copied EXACTLY from the sheet `.tsv`.
`note`: what the ink showed, briefly; say "print = printed" when the print agrees with our text.
Write the file once at the end (one Write), not row by row.

**Report back** (short): sheets done, rows written, rows you could not decide (page/pos), and any pattern
you saw more than twice (it may become a rule for the next volume).
