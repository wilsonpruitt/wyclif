# Review: *De eucharistia*, chunk 08-a (pp. 232.5–236.30)

Reviewer: independent, fresh session, 2026-11-09. Method: I went sentence by sentence through Loserth's Latin (the `>` blocks) against the English, using `CARD.md` (read whole), CONVENTIONS §§6–9, 12, 14 and the 2026-11 log rows, and GLOSSARY.md (grepped per term). I accounted for every *enim / nam / ergo / igitur / ideo / sed / autem / vero / tamen / itaque / unde / ymmo / quia* in the chunk. *Sed tunc* at 233.12 is rightly "now", the minor premiss before *ergo* (233.14). *Autem* at 232.18 and *vero* at 235.25 are rightly "and". *Sed* at 232.9 is rightly "but": it corrects "not this, but how". The one connective problem is an added "for" (row 3). I counted every page.line from `text/eucharistia/bt/p232–p236.txt`. I checked every T note and variant line against `apparatus.json` (leaves 303–307, which carry pp. 232–236), and they agree. I read one plate (n0303, p. 232, ll. 5–13) for the doubt below. Lint is clean. I did not re-verify the sources in the notes, and I did not check quotation bounds against the italics.

Classes: 1 terms · 2 connectives · 3 medieval sense · 4 construal, or a note/title contradicting the text.

**Exact strings.** "Current" and "proposed" are copied exactly from the file and are meant for find/replace. I checked each "current" string with grep, and each occurs once in the file. Where a string runs across a line break, **⏎** stands for the newline plus the next line's own indentation. No string in this review needs one.

| # | page.line | Latin | current English | class | severity | proposed English | reason |
|---|---|---|---|---|---|---|---|
| 1 | 235.5 (n. 12) | *ut accidens spirituale … multiplicetur et alibi … impediatur a multitudine; sed superinducatur eius contrarium* | "but [let] its contrary be brought in over it," | 4 | weak | "but its contrary is brought in over it," | n. 12 says that *sed superinducatur* is "still inside the *ut* clause". The bracketed "[let]" makes it a main-clause jussive, so the English contradicts its own note. The note is right: the subjunctive continues *multiplicetur … impediatur*. |
| 2 | 234.20 | *ut eliciunt illi qui … sollicitantur … ad eliciendum conclusiones mirabiles* | "as those infer who are" | 1 | weak | "as those elicit who are" | One term, one rendering. *Eliciunt* is "elicit" at 234.1 and again in *ad eliciendum*, three words on ("to elicit"). "Infer" here also collides with *infert* / *concludere*. |
| 3 | 235.9 | *quod si Deus potest facere maius, potest facere et minus* | "for if God can do the greater" | 2 | weak | "and if God can do the greater" | *Quod si* is continuative ("and if"). The Latin has no *enim / nam*, and "for" invents a causal link. |
| 4 | 234.31 | *nam actus sensibiles individuantur a loco et tempore* | "for [perceptible]{g:sensibilis} acts" | 3 | weak | "for acts of sense" | These are the acts of sensing: the pain Peter feels in both places (*utrobique sentit dolorem*). They are not acts that can be perceived. The §D row "perceptible" fits sensible objects. Here the medieval *actus sensibilis* is the act of the sense power. Proposed GLOSSARY row: *actus sensibilis* "act of sense". |
| 5 | 234.1 | *Et hic eliciunt quidam conclusiones mirabiles* | "And here some elicit wondrous" | 1 | style | "And here some [elicit]{g:elicere} wondrous" | This is the first *elicere* in the chunk, and it is untagged. The row is "of an act of … judgement", and drawing a conclusion is one. |
| 6 | 235.20 | *ut sancti ipsas describunt* | "as the saints [define]{g:describere} them" | 1 | style | "as [the saints]{g:sancti} [define]{g:describere} them" | This is the first *sancti* in the chunk, and it is untagged. |
| 7 | 236.14 | *idem corpus posset infinicies esse* | "infinitely many times through the same place" | 1 | style | "[infinitely many times]{g:infinicies} through the same place" | The row *infinicies* (ruled from 237.10, wave 21) postdates this chunk and was not conformed back. |
| 8 | 233.1–2 | *non tamen est dimensionaliter in aliqua earum* | "Yet it is not dimensionally in any of them," | 4 | style | "Yet it is not dimensionally in any of them [the hosts]," | *Earum* is feminine, so it means the hosts (*hostia*), not the places (*loca*, which would be *eorum*). In the English, "them" reads as the places. |

## Latin doubts

- 232.7 · printed *cum sit singula eius singularia … condistincta* · a singular verb with a neuter-plural subject; one might suspect *sint* · settled on the plate (n0303): the print reads *sit*. It construes as Wyclif's agreement with the neuter plural, and the English ("its singulars are") is right. No note needed.
- 233.5 · *occupatum* agrees with no noun in sight · already handled in n. 5 (ABCD *partem corpore*). The English follows the sense. No change.

## Point for the headnote / coordinator

- **Title:** "the absurdities drawn against the first". ¶7 (236.5–30) is the first way's own evidence for multiplication (side-note 236.5: "Argument for multiplication from the miracles…"), not an absurdity. This is not counted as a row because the title's first clause ("the two ways") covers it. If the title is touched: "…the absurdities drawn against the first, and its proofs from the miracles".

## Counts

| class | error | weak | style |
|---|---|---|---|
| 1 terms | 0 | 1 | 3 |
| 2 connectives | 0 | 1 | 0 |
| 3 medieval sense | 0 | 1 | 0 |
| 4 construal | 0 | 1 | 1 |
| **total** | **0** | **4** | **4** |

Overall: a good chunk. The hard *sed tunc* minor premiss is right, the predicate-logic passage (235.25–31, n. 14) is construed correctly, and the notes match the apparatus. The fixes are one note/English contradiction, two connective and term drifts, and missing tags.

## Applied 2026-11-09

- Rows 1–3, 5–8: applied.
- Row 4: applied ("for acts of sense", tag removed). The proposed GLOSSARY row *actus sensibilis* "act of sense" is not added (GLOSSARY not edited; referred to the coordinator).
- Title point (headnote section): not a row, not applied.

Lint after application: 0 problems (93 chunks).
