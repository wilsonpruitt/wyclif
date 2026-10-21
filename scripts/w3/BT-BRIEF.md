# Blind transcription brief (B+, WORKFLOW stage 2B)

You transcribe printed pages of a Wyclif Society volume from page images. Your text becomes the
established Latin. Two independent OCR witnesses check it afterwards, so read what the page prints,
nothing else.

**Your task gives you:** SLUG, the page list, and OFFSET (leaf = page + OFFSET).
**Input:** `~/wyclif/text/SLUG/raw/leaves/nLLLL.jpg`, LLLL = page + OFFSET, four digits.
**Output:** `~/wyclif/text/SLUG/bt/pNNN.txt` (NNN = page, three digits). Write each page once.

⛔ Open no other file in `text/SLUG/` and no Fordham text. This is a blind transcription: another text in
view spoils it (measured: the corrector kept an error the blind reader did not make).

## What to transcribe: the main text column only
In: the chapter heading, the editor's bracketed argument or summary when it is printed in the column, and
every line of the body down to the last line above the footnotes. Out: the running head and page number, the
margin side-notes (English), manuscript sigla in the margin (`[C 37b]`, `[A 75b]`), and the footnote
apparatus at the page foot.

## Format: one printed line per line
- **Keep the print's line breaks.** One printed line = one line of your file. A word hyphenated at line end
  keeps its hyphen (`incommuni-`), and the next line starts with the rest (`cantes:`). The same applies at
  the page foot: end the page with `consideran-` if that is what it prints.
- **Line numbers:** where the print has a line number in the margin (5, 10, 15 …), start that line with
  `N| ` (`5| videntur inperitis contraria ;`).
- **Heading lines** start with `# ` (`# Cap. I.`). **The editor's argument/summary lines** (bracketed,
  usually italic, in the column above the body) start with `> `.
- **Paragraphs:** a line that begins a new paragraph (indented in print) starts with `¶`. The first line on a
  page continuing the previous page's paragraph has no `¶`.
- **Footnote reference numbers** (small raised figures in the text) go as `^N` right after the word they
  follow, no space (`scripta^2`).
- **Manuscript folio bars** (`|` inside the text) are left out.
- Words: exactly as printed. Medieval spelling stays (*michi*, *set*, *sicud*, *nichil*, *Cristus*); never
  normalise or modernise; u/v and i/j as printed; capitals and punctuation as printed. Superscript letters
  as modifier letters (`3ᵃ`, `Psⁱ`), the degree sign as printed (`3°`). A word printed in brackets keeps them.
- A word you cannot read: `[?word]` with your best guess. Never skip a line: if a line is unreadable,
  write `[?line]`.

Report briefly at the end: pages done, `[?…]` marks, anything on a page that this format could not hold.
