# Close-out prompts — *De eucharistia* (stage 9). Adapted from `chunks/ecclesia/CLOSEOUT-PROMPTS.md` §A/A2.
Run on Wilson's "Opus go" 2026-11-09. Opus, at most 2 agents at once, 2 chunks per agent, one REVIEW file per chunk.

Chunks (10 densest by file size, + 03-c for ch. 3): 07-j, 08-a · 04-e, 06-e · 05-a, 02-e · 05-i, prol-b · 09-c, 03-c.

## A. Four-class review — chunks {A} and {B}

You are an independent reviewer of Wyclif, *De eucharistia* (ed. Loserth 1892), in ~/wyclif. Review chunks
{A} and {B} (files `chunks/eucharistia/wyc-eucharistia-{id}.md`) sentence by sentence, Latin (the `>` lines)
against English, for the four error classes. Do NOT edit any chunk or any other file; write exactly two files,
`chunks/eucharistia/_review/REVIEW-{A}.md` and `REVIEW-{B}.md`, each once.

Read first: `chunks/eucharistia/CARD.md` whole (the four classes, the connective table, the variant rule:
Loserth's print governs; two works, two sets of sigla); `CONVENTIONS.md` §§6–9, 12, 14 (and the 2026-11 rows
naming this volume); `chunks/incarnacione/_review/REVIEW-11a.md` — your format model (header paragraph, the
"Exact strings" paragraph, the table columns, the closing counts). GLOSSARY.md is large: grep it per term, don't
read it whole; note that some keys carry two rows of different sense (*continuacio, sentencia, cognacio,
conficere, species, fantasticus, singulariter, per se*) — check the tag points at the sense the passage needs.

Classes: 1 terms (GLOSSARY, first-occurrence tags, CONTEXTUAL C notes) · 2 connectives (every *enim / nam /
ergo / igitur / ideo / sed / autem / vero / at / tamen / itaque / unde / ymo / quia*; a minor premiss before
*ergo* is "now", not "but") · 3 medieval sense · 4 construal, incl. a note, title or headnote that contradicts
the Latin or the English beside it, and a T note that misdescribes the apparatus.

Sources: page.line citations count from `text/eucharistia/bt/pNNN.txt` (margin numbers mark the line they
stand level with). The apparatus is in `text/eucharistia/apparatus.json` (OCR, rough); where a T note or a
variant matters, read the plate foot: `text/eucharistia/raw/leaves/nLEAF.jpg`, LEAF = page + 71, four digits
(p. 1 = n0072.jpg). Crop with Python/PIL to the foot or the line before viewing (don't view whole leaves
more than needed). Do not re-verify ledger sources. Do not report taste. Quotation bounds and italics are the
editor's: not a review item.

Severity: **error** = says something the Latin does not, or omits an argument-bearing word; **weak** =
defensible but a doubtful choice made silently or against the card; **style**. Every row: page.line, Latin,
current English (copied EXACTLY from the file, grep-checked to occur once; ⏎ for a line break), class,
severity, proposed English (exact replacement text), reason. Also list, after the table, any **Latin doubts**
(page.line · printed · suspicion · settled on the plate? how) and any point for the headnote. End each file with
counts by class and severity and one line on the chunk's overall state. Read each chunk once; be economical.
Reply to me in under 100 words: counts per chunk, and any error-class row in one line each.

## A2. Apply the reviews

Working directory ~/wyclif. Apply the rows in `chunks/eucharistia/_review/REVIEW-{ids}.md` to the chunks they
name, English and notes only. Coordinator's rulings: {RULINGS}. Rules: never touch the `>` Latin lines or the
front matter; keep note numbering 1..n in order of anchors (renumber if you add or remove a note, and fix
every cross-reference "n. N" in the same chunk and in LEDGER.md rows that cite it); a new tag uses a key that
exists in GLOSSARY.md (grep it). Where "current English" is not found verbatim, find the passage by the Latin
and apply the intent; if it cannot be applied safely, skip it. Then run
`.venv/bin/python scripts/w3/lint.py chunks/eucharistia/wyc-eucharistia-*.md` (must be 0 problems) and append
to each review file `## Applied 2026-11-09` listing every row: applied / applied-adjusted (how) / skipped (why).
Reply in under 80 words.
