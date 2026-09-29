# Ledger verification brief (Dialogus close-out, 2026-09-29)

You verify rows of `~/wyclif/LEDGER.md` (read its header for the status vocabulary). You are given a list
of row ids. For EACH row:

1. Read the row, then the chunk note it cites (`~/wyclif/chunks/dialogus/wyc-dialogus-NN.md`, note `[^n]`;
   epil-a/epil-b = the epilogue files). Understand exactly what the note CLAIMS.
2. Find the source and READ the relevant passage. Do not verify from memory, from a secondary summary,
   or from a search-result snippet. Order of preference:
   - **Local Patrologia Latina** (TEI, 5,276 files): `~/patrologia/sources/pl/tei/*.xml`. Augustine =
     PL 32–47, Jerome 22–30, Gregory I 75–79, Gratian's Decretum = PL 187, Possidius = PL 32, Boethius
     63–64, Rufinus 21, Ambrosiaster PL 35 (*Quaestiones V. et N. T.*). Find the volume with
     `grep -l '<title' ... ` / `grep -l 'phrase'` on specific files; ⚠ never run an unbounded recursive
     grep with many patterns — one plain `grep -l -i 'phrase' ~/patrologia/sources/pl/tei/*.xml` at a time
     is fine. Column anchors are `<pb n="0473A"/>`: cite PL vol + column.
   - Scripture: `cd ~/wyclif && .venv/bin/python scripts/w3/bible.py "Isa 1:23"` (Clementine Vulgate +
     Douay–Rheims). "1–4 Kings" in that tool = Vulgate numbering (1 Kings = 1 Samuel); for Protestant
     1 Kings use "3 reg".
   - Pollard's edition (the *Dialogus* intro/notes): OCR under `~/wyclif/sources/ia-ocr/` (grep).
   - Web (load WebFetch/WebSearch via ToolSearch "select:WebFetch,WebSearch"): augustinus.it,
     thelatinlibrary.com, the Avalon Project / legislation.gov.uk / Statutes of the Realm scans for
     statutes, Perseus / Bekker text for Aristotle, archive.org full texts. A primary text, not a blog.
3. Decide:
   - `verified` — the source says what the note claims (reference numbers correct). "how" = source,
     locator (PL vol:col, section, URL), "read 2026-09-29".
   - `verified (corrected)` — the claim is right in substance but a reference/wording is wrong; give the
     correct reference and the EXACT replacement text for the chunk note.
   - `untraced` — looked properly, not found; "how" says where you looked and what's left to try.
   - `wrong` — the source contradicts the note; give the proposed replacement note text.
   Claims of historical interpretation (e.g. "CAIM = the four orders' initials") are verified by a
   reputable primary or standard reference that states it; say which.
4. Do NOT edit LEDGER.md or any chunk. Write your results to the output file you were given, as a
   markdown table with the LEDGER columns `| id | chunk / note | claim | status | how / next step |`
   (copy id/chunk/claim from the ledger), followed by a section "## Chunk corrections" listing, for each
   corrected/wrong row, file, note number, current text (exact), replacement text (exact).
5. Budget: ~5–8 tool calls per row. Don't spend more than ~15 on any one row: mark it untraced with the
   trail and move on.

Report back (final message) in under 200 words: counts by status, and the corrections list in one line each.
