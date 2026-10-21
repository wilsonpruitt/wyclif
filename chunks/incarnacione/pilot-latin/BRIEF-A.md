# Pilot arm A: correct Fordham against the plate

Wyclif, *De benedicta incarnacione* (ed. Harris, Wyclif Society 1886). For each page NNN in the list
you are given:

1. Read the page image `~/wyclif/pilots/plates/incarnacione_pNNN.jpg`.
2. Read Fordham's transcription `~/wyclif/chunks/incarnacione/pilot-latin/fordham_pNNN.txt`. It is
   uncorrected OCR: expect wrong letters, dropped or added words, lost lines, wrong punctuation.
3. Write `~/wyclif/chunks/incarnacione/pilot-latin/armA/pNNN.txt`: the MAIN TEXT of the page exactly as
   printed, made by correcting Fordham's text.

**Scope = the main text column only:** the chapter heading and any argument or summary printed in the
column count; leave out the running head, page number, margin side-notes, line numbers, and the
editor's footnote apparatus at the page foot. Keep the print's spelling (*michi*, *set*, *Cristus*,
*sicud*); never normalize or modernize. Keep the printed punctuation and capitals. Hyphenated
line-end words: join them. One paragraph per paragraph, blank line between. A word you cannot read on
the plate: `[?word]` with your best guess.

Also append one row per change to `armA/changes.tsv` (tab-separated: page, fordham, print, note),
where `fordham` is Fordham's form ('' if Fordham omitted it) and `print` is the plate's ('' if Fordham
added it). Do not add rows for paragraph breaks.

Write each page's file once. End with a short report: pages done, number of changes, any page where
Fordham's text did not match the plate at all.
