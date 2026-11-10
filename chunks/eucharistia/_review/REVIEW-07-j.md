# Review: *De eucharistia*, chunk 07-j (pp. 226.1–230.31)

Reviewer: independent, fresh session, 2026-11-09. Method: I went sentence by sentence through Loserth's Latin (the `>` blocks) against the English, using `CARD.md` (read whole), CONVENTIONS §§6–9, 12, 14 and the 2026-11 log rows, and GLOSSARY.md (grepped per term). I accounted for every *enim / nam / ergo / igitur / ideo / sed / autem / vero / tamen / itaque / unde / ymmo / quia* in the chunk. None is omitted. *Autem* at 226.11 and 230.14 is rightly "but" (adversative). *Autem* at 227.1 is rightly "and" (it continues the same step). *Vero* at 228.12 is rightly "but" (the second horn after *Si non*). *Sed* at 229.12 is rightly "but": no *ergo* follows, so it is not a minor premiss. I counted every page.line from `text/eucharistia/bt/p226–p230.txt`. I checked every T note and variant line against `apparatus.json` (leaves 297–301, which carry pp. 226–230). They agree, except for one line reference in the transcription notes (see below). Lint is clean. I did not re-verify the sources in the notes, and I did not check quotation bounds against the italics.

Classes: 1 terms · 2 connectives · 3 medieval sense · 4 construal, or a note/title contradicting the text.

**Exact strings.** "Current" and "proposed" are copied exactly from the file and are meant for find/replace. I checked each "current" string with grep, and each occurs once in the file. Where a string runs across a line break, **⏎** stands for the newline plus the next line's own indentation. No string in this review needs one.

| # | page.line | Latin | current English | class | severity | proposed English | reason |
|---|---|---|---|---|---|---|---|
| 1 | 228.8–10 | *Non enim fit panis caro Christi qui secundum se totum destruitur, antequam fieret caro Christi* | "For the bread does not become the flesh of Christ, which is destroyed according to its whole self before it became the flesh of Christ;" | 4 | weak | "For the bread, which is destroyed according to its whole self before it became the flesh of Christ, does not become the flesh of Christ;" | *Qui* is masculine and so refers to *panis*. In the current English, "which is destroyed" attaches to "the flesh of Christ", and the sentence then says that Christ's flesh is destroyed. |
| 2 | 230.5–6 | *quomodo referri debet ad signum quod teritur et non Christus* | "the sign which is ground, and not [to] Christ." | 4 | weak | "the sign which, and not Christ, is ground." | *Christus* is nominative. Like *quod*, it is the subject of *teritur*: it is the sign that is ground, and Christ is not. "[To] Christ" construes it as *ad Christum*, a second goal of *referri*, which the case rules out. |
| 3 | 229.10–11 (n. 16) | *Verbum enim infinite potencie* | (a) "For [the Word]{g:verbum} of infinite power"; (b) n. 16 "**C.** *Quia aliter foret ydemptificacio*" | 1 | weak | (a) "For [the Word]{g:verbum} of infinite [power]{g:potencia}"; (b) "**C.** *Infinite potencie*: \"power\", God's might (CONTEXTUAL row), not Aristotle's potency. *Quia aliter foret ydemptificacio*" | This is the first and only *potencia* in the chunk. The row is CONTEXTUAL (potency / power), so the card requires a tag and a C note at its first occurrence. Both are missing. 08-a n. 6 does this. |
| 4 | 226.4 | *Recoleret, inquam, de textu Augustini … tunc enim verecundaretur* | "Let him recall, I say," | 4 | style | "He should recall, I say," | *Recoleret* is imperfect subjunctive: an unfulfilled "should / were he to". The following *tunc enim verecundaretur* ("for then he would be ashamed") depends on it. "Let him" is a present jussive. |
| 5 | 230.7 | *variacio loyce fidelium* | "the variation of the logic of the faithful" | 1 | style | "the variation of the [logic]{g:loyca} of the faithful" | This is the first *loyca* in the chunk, in the row's own sense (the manner of speaking about the sacrament), and it is untagged. The volume tags it 19 times. |
| 6 | 227.26 | *omnis natura vel quidditas corporis* | "every nature or quiddity of a body" | 1 | style | "every nature or [quiddity]{g:quiditas} of a body" | This is the first *quidditas* in the chunk, and it is untagged. |
| 7 | 228.7–8 | *totam substanciam annichilari* | "the whole [substance]{g:substancia} is said to be annihilated" | 1 | style | "the whole [substance]{g:substancia} is said to be [annihilated]{g:anichilacio}" | The row *anichilacio; anichilare* covers the verb, and this is its only occurrence in the chunk. |
| 8 | 230.26 | *determinaciones ecclesie* | "[determinations of the church]{g:determinaciones-ecclesie}" | 1 | style | "[the church's determinations]{g:determinaciones-ecclesie}" | The row's rendering is "the church's determinations". (Two other places in the volume carry the same drift; for the coordinator.) |

## Latin doubts

- 229.24 · printed *sanguinis* · the genitive does not construe with *forent* · already settled (wave 20, plate n300). It is our emendation to *sanguis*, with a T note (n. 17). The note is accurate: the apparatus (leaf 300) has no line-24 entry.
- No others. I found no side-note at the wrong line.

## Outside the four classes (process; not counted)

- **The transcription notes' "Emendation" line** gives the place as "229 (about l. 22)". *Sanguinis* is at 229.24 (bt p229 l. 24, and the wave-20 log row). Proposed: replace "229 (about l. 22)" with "229.24".
- **n. 9** (the referent of *istam sentenciam*, 227.6). The note prefers impanation and gives the glossators' teaching as the alternative. The paragraph's own target (227.22–25, "not … an unknown accident") argues for the alternative at least as strongly, but the choice is not silent and both readings are given, so it is not flagged.
- **Headnote:** none owed.

## Counts

| class | error | weak | style |
|---|---|---|---|
| 1 terms | 0 | 1 | 4 |
| 2 connectives | 0 | 0 | 0 |
| 3 medieval sense | 0 | 0 | 0 |
| 4 construal | 0 | 2 | 1 |
| **total** | **0** | **3** | **5** |

Overall: a sound chunk. The connectives are clean, the notes agree with the apparatus, and the predication is kept in Wyclif's order. The fixes are two relative/case construals and a few missing tags.

## Applied 2026-11-09

- Rows 1–8: applied (row 3 both parts: tag and C note opening n. 16).
- Not rows, not applied: the transcription notes' "229 (about l. 22)" → "229.24" (process item); the drift of *determinaciones ecclesie* in two other chunks (for the coordinator).

Lint after application: 0 problems (93 chunks).
