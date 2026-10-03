# Close-out agent prompts (CLOSEOUT.md stages A–C). Fill {…}. All agents Opus, at most 2 at once.

## A. Four-class review — {RN}: chunks {LIST}

You are an independent reviewer of Wyclif, *De ecclesia* (ed. Loserth 1886), in ~/wyclif. Review chunks
{LIST} (files `chunks/ecclesia/wyc-ecclesia-NN-x.md`) sentence by sentence, Latin against English, for the
four error classes. Do NOT edit any chunk; write ONE file, `chunks/ecclesia/_review/REVIEW-{RN}.md`, once.

Read first: `chunks/ecclesia/CARD.md` (the four classes, the connective table, standing rules);
`CONVENTIONS.md` §§6–9 and §14; the header + first rows of `chunks/dialogus/_review/REVIEW-targeted.md`
(your format model). GLOSSARY.md is 56KB: grep it for each term, don't read it whole. Rules adopted later
than the early chunks, which apply to every chunk: quotations open and close at the print's italics (a
roman stretch is reported, not quoted) — M5-RESUME brief 45; the standing emendation rule — M5-RESUME
"Rulings 2026-10-02" (English may follow a marked conjecture; supplies in brackets with a T note).

Classes: 1 terms (GLOSSARY, first-occurrence tags, CONTEXTUAL C notes) · 2 connectives · 3 medieval
sense · 4 construal (incl. a note or headnote that contradicts the Latin or English beside it).
Do not re-verify sources. Do not report taste. Every row: chunk, page.line, the Latin, current English,
class, severity (**error** = says something the Latin does not / omits an argument-bearing word;
**weak** = defensible but a doubtful choice made silently or against the card; **style**), proposed
English (exact replacement text, so it can be applied), and the reason. End with per-chunk counts and
one line on each chunk's overall state. Be economical: read each chunk once.

## B. Connective check — extract {NN}

You are checking *sed* and *autem* in Wyclif, *De ecclesia* (ed. Loserth), ~/wyclif. Read
`chunks/ecclesia/CARD.md` § "The four error classes", item 2 (connective table and the "now" rule), and
`chunks/dialogus/_connectives/RESULTS.md` (your format and the classes, worked). Then read
`chunks/ecclesia/_connectives/body-{NN}.md`: each ¶ gives the Latin (every *sed/autem* in **bold**) and
our English. For EVERY bold occurrence decide: (a) minor premiss / next step → "now"; (b) adversative →
"but"; (c) continuative *autem* → "and"; *non … sed* → "but" ("rather" is *ymmo/pocius*). Check the
English has it, rendered per its class; an omitted *sed/autem* is an error unless the English
construction carries it (say how).
Do NOT edit chunks. Write ONE file `chunks/ecclesia/_connectives/RESULTS-{NN}.md`: ## Changes (table:
chunk | page | Latin phrase | was | now | reason — "was"/"now" exact English strings so a find/replace
works) · ## Doubtful, left as they are · ## Totals (occurrences checked, by class; changes). Changes only
where the card decides it; a defensible reading stays and goes under Doubtful if it is a real toss-up.

## C. LEDGER — group {G}

You are closing open source-identification rows for Wyclif, *De ecclesia*, in ~/wyclif. Your rows:
`chunks/ecclesia/_verify/groups/{G}.md` (some may belong to another source family; do them anyway).
For each row, find the claim's source and check it: work, locus, wording against Wyclif's Latin (in the
chunk named in column 2; the Latin is in the `>` lines, the note is `[^n]`). Do NOT edit LEDGER.md or any
chunk. Write ONE file `chunks/ecclesia/_verify/batch-{G}.md`.

Sources. Local PL TEI: ~/patrologia/sources/pl/tei/*.xml (`grep -l` a distinctive phrase; Gratian =
21354.xml). Wyclif's other works, Society OCR: `sources/ia-ocr/latinworksNNwycl.txt` (which volume is which:
`sources/wyclif_society_archive_org.csv`); Loserth's own foot-notes and introduction: latinworks10wycl.txt.
Scripture: `python3 scripts/w3/bible.py "Luc 17:23"`. Friedberg OCR: archive.org BD1141951 (Decretum),
BD1141952 (Decretals): `curl -sL https://archive.org/download/<ID>/<ID>_djvu.txt` into your scratchpad
once, grep with ' +' between words. Web (WebFetch): corpusthomisticum.org (Thomas, incl. *Scriptum super
Sententiis*), archive.org (Bonaventure Quaracchi *Opera* IV; Sarum missal/breviary), thelatinlibrary.com.
8 GB machine: never grep the whole PL with -r on a broad pattern twice; narrow by phrase.

Each row ends in exactly one status: `verified` (you read the source at that locus; give source + locus +
how, dated 2026-10-03), `editor` (Loserth's identification, which you could not check further but which he
gives explicitly — quote his foot), or `untraced` (looked for in at least the obvious two places; say
where). For a wrong identification, give the corrected one. Where the chunk note overstates (asserts what is
now untraced, or a wrong locus), give the exact replacement note text (chunk, note number, old phrase → new
phrase). Format: a table `id | status | how / source | note change (or —)`, then a short list of anything
the coordinator must decide. Be economical: don't re-read a source for each row that shares it.
