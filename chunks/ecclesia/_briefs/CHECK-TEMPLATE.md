# Per-brief plate + source check (Sonnet) — template

*Used for briefs 24–28 (2026-10-02), ~120–150K tokens each. Fill the brackets from the Opus agent's report
(its scar list, lost/doubled-word flags, Latin doubts, `to-verify` ledger rows), then launch one Sonnet agent.*

---

You are checking Wyclif, De ecclesia (ed. Loserth 1886), chunks [NN-x, NN-y, NN-z] in ~/wyclif (pp. [A–B]).
Do NOT edit any files; report only. Be economical.

Plates: ~/wyclif/text/ecclesia/raw/leaves/nLLLL.jpg, LLLL = printed page + 37, 4 digits (p. 316 → n0353.jpg).
Read the image; margin line numbers are by fives. Established Latin: text/ecclesia/pNNN.la.txt. Chunks:
chunks/ecclesia/wyc-ecclesia-{…}.md. Loserth's print governs; report what the print shows incl. page-foot
apparatus for the line.

Known loss mechanisms: words lost at PAGE HEADS, at LINE-END HYPHENS, mid-line drops, and DOUBLINGS.
Already fixed (ignore): [tokens already in tokenfix.tsv for this brief].

PLATE ITEMS (PRINT = "…", OUR = "…", ACTION):
1. [each flagged lost/doubled word, Latin doubt, uncertain scar: page.line + what to check]
N. Systematic: compare EVERY line of pp. [A–B] word by word with pNNN.la.txt (this found mid-line losses:
   21 *illo*, 332 *II.*); every line-end hyphen; every page's first/last words. List only discrepancies.
   Plus any other garbage token (stray letters, line numbers, glued/broken words, numerals).

SOURCE ITEMS. Friedberg *Corpus iuris canonici* OCR: vol. I (Decretum) = archive.org BD1141951, vol. II
(Decretals) = BD1141952; fetch `https://archive.org/download/<ID>/<ID>_djvu.txt` with curl -sL into the
session scratchpad once (grep with ' +' between words: the OCR doubles spaces). PL TEI:
~/patrologia/sources/pl/tei/*.xml (grep -l a phrase; Gratian = 21354.xml).
A. [each to-verify ledger row: the work, the wording to compare, the chunk/note]

Report: numbered verdicts, PRINT/OUR/ACTION or SOURCE/WORDING/ACTION. Under 800 words.

---

**Applying the report (coordinator):** raw tokens via `pNNN.tok.jsonl` → `text/ecclesia/tokenfix.tsv` rows
(single token, or a two-token pair key; check the key is unique on the page) → English + note fixes → LEDGER
statuses → `vote.py ecclesia` → `relatin.py ecclesia --also <chunks>` → `relatin.py ecclesia --dry` (must be 0)
→ `lint.py chunks/ecclesia/wyc-*.md` → M5-RESUME status → commit.
