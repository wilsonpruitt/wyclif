# Review: *De eucharistia*, chunk 05-i (pp. 147.9–151.23)

Reviewer: independent, fresh session, 2026-11-09. Method: sentence by sentence against Loserth's Latin (the `>` blocks), against `CARD.md` (read whole), CONVENTIONS §§6–9, 12, 14, and GLOSSARY.md (grepped per term). Every *enim / nam / ergo / igitur / ideo / sed / autem / vero / tamen / unde / quia* in the chunk was accounted for (also *per idem*, *quidem*, *inquam*). None is omitted. The one doubtful rendering is the *autem* at 149.4 (row 1). All six *enim* and all four *nam* are "for", and all three *ideo* and three *ergo* are "therefore / then". Every T note was checked against the page-foot apparatus (`apparatus.json`, keyed by leaf: p. 147 = leaf 218). Every page.line citation was counted from `text/eucharistia/bt/p147–p151.txt`, and all are correct except n. 20 (row 9). One plate foot was read, n0220 (p. 149), for n. 12: it prints "8. AB: *in manere fidei*" (row 10). The CONTEXTUAL rows are noted at their first occurrence: *inconveniens* (n. 1) and *sentencia* (n. 19). Lint is clean. Sources in the notes were not re-verified. Quotation bounds were not checked against the italics.

Classes: 1 terms · 2 connectives · 3 medieval sense · 4 construal, or a note/title contradicting the text.

**Exact strings.** "Current" and "proposed" are copied exactly from the file and are meant for find/replace. Each "current" string was checked with a script and occurs once in the file. No string in this review runs across a line break (⏎ is not needed).

| # | page.line | Latin | current English | class | severity | proposed English | reason |
|---|---|---|---|---|---|---|---|
| 1 | 149.3–4 | *ergo descripcio non est sana secundum eos. Quamvis autem hoc sit argumentum ad hominem* | "Now although this is an [argument to the man]" | 2 | weak | "But although this is an [argument to the man]" | The *autem* does not bring a minor premiss or a new premiss to bear. The syllogism has just closed with *ergo* (149.3), and *autem* turns against it: it concedes that the argument is only *ad hominem* and rests on a false principle. That is an adversative turn ("but"). Under the card, "now" is reserved for the minor premiss. |
| 2 | 148.24; 151.6 | *capiens suam speciem*; *quantum ad species quibus corpus Christi* | (a) "as it takes its [species]{g:species},[^9]"; (b) "understood as to the species, to which" | 1 | weak | (a) "as it takes its species,[^9]"; (b) "understood as to the [species]{g:species}, to which" | The `species` key resolves to the row "species (of bread and wine)", the sacramental species. N. 9 rightly says that 148.24 is the species of perception carried by the medium, which is not that sense, so the tag points at the wrong row. The first sacramental *species* in the chunk is 151.6, and it is untagged. |
| 3 | 148.4 | *non est terminus philosophicus ad sensum illum* | "in that [sense]{g:sensus}" | 1 | weak | "in that [meaning]{g:sensus}" | The tag resolves to the row "sensus (of words): meaning", which keeps "sense" for the bodily *sensus* and for *sentencia (verborum)*. Here the *sensus* is the meaning of a term, so the row's English is owed. |
| 4 | 150.15–17 (n. 19) | *Nec obviat ista pictacia directe nostre sentencie, cum panis convertitur in corpus Christi.* | n. 19, last sentence: "**C.** *Sentencia* \"teaching\", Wyclif's position." | 4 | weak | "**C.** *Sentencia* \"teaching\", Wyclif's position. *Cum panis convertitur* is taken as causal, \"since\" (our teaching also says that the bread is converted); it may be temporal, \"when [we say that] the bread is converted\"." | The construal of *cum* with the indicative is open. On the causal reading Wyclif grants a conversion; on the temporal reading he names the point of his teaching that the patchwork fails to meet. A doubtful construal is not to be chosen silently (card, class 4). The English is kept. |
| 5 | 147.13–14 | *ad quatuor differencias posicionis* | "toward the four [differences]{g:differencia} of [position]{g:posicio}" | 1 | style | "toward the four differences of position" | Both tags point at logical rows: *differencia* is the logical *differentia*, and *posicio* is "position" against "proposition / predication". Here the words are the spatial directions (n. 2: up, down, before, behind, right, left). The plain words are right; the hover glosses would mislead. |
| 6 | 147.12; 148.32; 150.26 | *sacerdotibus*; *demultiplicare*; *sacramentum istud esse panem* | (a) "if six priests are posited"; (b) "at other times demultiply it"; (c) "lays it down that \"this sacrament is bread\"" | 1 | style | (a) "if six [priests]{g:sacerdos} are posited"; (b) "at other times [demultiply]{g:demultiplicare} it"; (c) "lays it down that \"this [sacrament]{g:sacramentum} is bread\"" | These are the first occurrences in the chunk of three ruled rows (*sacerdos*; *demultiplicare*, Euch. 235.1; *sacramentum* (the Eucharist)), and none is tagged. |
| 7 | 150.18 | *Quantum ad ultimum Sancto impositum* | "As to the last [charge] imputed to the Saint" | 4 | style | "As to the last [point] imputed to the Saint" | *Impositum* is something ascribed to Thomas: the argument the opponents put in his mouth (n. 20). "Charge imputed to" can be read as an accusation brought against him. |
| 8 | 148.8 (n. 6) | foot "8. E: *et sanguinem*" | "E adds *et sanguinem* (148.8)" | 4 (note) | style | "E reads *et sanguinem* for *vel sanguinem* (148.8)" | The foot gives a reading, not an addition (no *addit*). The print already has *sanguinem*. |
| 9 | 150.30–151.1 (n. 20) | *imponitur [p. 151] sancto Thome* | "(so *sancto Thome* at 150.31–151.1)" | 4 (note) | style | "(so *imponitur sancto Thome* at 150.30–151.1)" | P. 150 has 30 lines, so there is no 150.31. *Imponitur* stands at 150.30, and *sancto Thome* at 151.1. |
| 10 | 149.8 (n. 12) | foot "8. AB: *in manere fidei*" (plate n0220) | "B reads *in manere fidei* (149.8)" | 4 (note) | style | "AB read *in manere fidei* (149.8)" | The plate foot prints the siglum AB, not B alone. |

**Latin doubts.**
- 151.10–11 · *de glossa super additis, distinccione IIᵃ, De Consecracione primo* · the phrase is obscure (which "additions"? what does *primo* qualify?), and Loserth's foot says the passage is not in Jenson's Gloss · not a plate matter: the print is clear and n. 27 translates it as printed and says so. Nothing is owed.
- No other doubt. The print construes throughout. The plate reading *IVᵃ* (151.12) is recorded in the transcription notes.

**Headnote.** None owed (not the work's first chunk).

**Counts.** Class 1: 4 (weak 2, style 2). Class 2: 1 (weak 1). Class 3: 0. Class 4: 5 (weak 1, style 4). Total 10: error 0, weak 4, style 6.

**Overall.** A sound chunk. The construal is careful through the difficult vacuum period (149.26–150.2) and the Thomas/Damascene passage, and every connective is present. The fixes are one "now" that is not a minor premiss, three tags that point at the wrong row, missing first-occurrence tags, and small slips in the notes.

## Applied 2026-11-09

- Rows 1–10: applied.

Lint after application: 0 problems (93 chunks).
