# Review: *De eucharistia*, chunk 09-c (pp. 280.17–284.31)

Reviewer: independent, fresh session, 2026-11-09. Method: I went sentence by sentence through Loserth's Latin (the `>` blocks) against the English, using `CARD.md` (read whole), CONVENTIONS §§6–9, 12, 14 and the 2026-11 log rows, and GLOSSARY.md (grepped per term). I accounted for every *enim / nam / ergo / igitur / ideo / sed / autem / vero / tamen / itaque / unde / ymmo / quia* in the chunk. None is omitted or rendered as filler. The *sed* at 281.13 (*Sed Deus non tardaret*) is "but", and that is defensible, because it answers the escape clause *nisi forte declaretur revelacione*. I counted the page.line citations from `text/eucharistia/bt/p280–p284.txt`. I checked every T note against the apparatus (`apparatus.json`, leaves 351–355), and all of them match the foot. One plate was read, n0354 (p. 283), line 18: the print does read *Quantum ad doctores legis, dicit primus,*, so n. 17's flag stands. Lint is clean. Sources were not re-verified. Quotation bounds and italics were not checked. Three GLOSSARY rows were ruled from this very chunk in wave 24 (*poletici*, *sollempnius*, *informacio (ecclesie)*), but the chunk's English was never conformed to them (rows 3–5).

Classes: 1 terms · 2 connectives · 3 medieval sense · 4 construal, or a note/title contradicting the text.

**Exact strings.** "Current" and "proposed" are copied exactly from the file and are meant for find/replace. I checked each "current" string with grep, and each occurs once in the file. Where a string runs across a line break, **⏎** stands for the newline plus the next line's own indentation. No string in this review needs one.

| # | page.line | Latin | current English | class | severity | proposed English | reason |
|---|---|---|---|---|---|---|---|
| 1 | 280.23 (n. 1) | *pastores et doctores (ut concludit Apostolus)* | (a) "(as the Apostle [infers]{g:concludere}),[^1]"; (b) n. 1 "which fits the sense better. The print is translated and the reading flagged." | 3 | weak | (a) "(as the Apostle puts [them] together),[^1]"; (b) "the same sense as the print's *concludit* taken in its root sense, \"shuts together, includes\" (not the logical \"infers\" of the *concludere* row). The print is translated." | Eph. 4:11 lists pastors and doctors as one office and draws no inference, so "infers" makes the Apostle conclude something he only names. *Concludere* also means "shut together, include". In that sense the print says what A's text and BDE (*coniungit*) say. The note itself grants that "joins" fits better, which leaves the English rendering a word in a sense the note disowns. |
| 2 | 283.24–26 | *quia sine evidencia nunc contendit … et nunc simulat falsa* | "for now he contends without [evidence]{g:evidencia}, in the way an abbot is wont to address his novices, and now he feigns falsehoods" | 4 | style | "for at one time he contends without [evidence]{g:evidencia}, in the way an abbot is wont to address his novices, and at another he feigns falsehoods" | "For now" reads as "for the present", and "now" is reserved for the minor premiss (card, class 2). *Nunc … nunc* is "at one time … at another". |
| 3 | 282.12–13 | *secundum poleticos* | "according to the political [writers]," | 1 | style | "according to the [political]{g:poletici} [writers]," | The row *poletici* "political [writers]" was ruled from this place (wave 24) but is not tagged here. The tag goes on the bare word, without nesting brackets. |
| 4 | 283.32 (n. 18) | *foret sollempnius* | (a) "would be more eminent than our sacrament"; (b) n. 18 "(GLOSSARY *sollempnior*)" | 1 | style | (a) "would be [more eminent]{g:sollempnius} than our sacrament"; (b) "(GLOSSARY *sollempnius*, extending *sollempnior*)" | The row *sollempnius (of teaching)* was ruled from this place (wave 24). The note still points to the older row. |
| 5 | 284.17 (n. 21) | *secundum informacionem ecclesie* | (a) "according to the instruction of the church"; (b) n. 21 "*Informacio*: \"instruction\", the church's teaching of Berengar, not GLOSSARY's *informacio* of a form in its subject." | 1 | style | (a) "according to the [instruction]{g:informacio} of the church"; (b) "*Informacio*: \"instruction\", the church's teaching of Berengar (GLOSSARY *informacio (ecclesie)*), not the *informacio* of a form in its subject; the two rows share the tag key." | The row *informacio (ecclesie)* "instruction" was ruled from 284.17 (wave 24). The note still says GLOSSARY has only the other sense. The key `informacio` is shared by two rows, so the C note has to name the row it means. |
| 6 | 284.22 (n. 22) | foot "28. Cf. De Apostasia, pag. 164" | n. 22 "Loserth compares Wyclif, *De apostasia*, p. 164 (LEDGER K09c-6)." | 4 (note) | style | "Loserth's foot, at 284.28 (the next sentence), compares Wyclif, *De apostasia*, p. 164 (LEDGER K09c-6)." | Loserth's reference stands at line 28 (*quod verum corpus Christi sit vere et realiter ibi presens*), not at 284.22, which is where note 22 places it. |
| 7 | 284.6–7 | *cum secta ista ponit quoad essenciam sacramentum illud vel unum nichil vel unum abiectissimum* | "since this sect lays down that [sacrament]{g:sacramentum}, as to its [essence]{g:essencia}, as either a nothing" | 4 | style | "since this sect lays down that [sacrament]{g:sacramentum}, as to its [essence]{g:essencia}, to be either a nothing" | *Ponit* + accusative + predicate means "posits X to be Y". "Lays down that … as" does not construe in English, and "that" reads first as a conjunction. |

## Latin doubts

- 283.18 · printed *dicit primus* · abrupt (perhaps for *dicitur*) · plate n0354: the print reads so, and the apparatus has no line-18 entry. N. 17 translates it and flags it, which is right.
- 283.3 · *quia usque ad indebitos cultores* · *quia* will not construe as "because" · there is no variant in the apparatus, and n. 15 flags it. Not plate-checked, since the reading itself is not in doubt.
- No side-note is misplaced.

## Outside the four classes (process; not counted)

- **bt not refreshed:** `bt/p281.txt` line 2 still reads *currremus*. The chunk's Latin and its transcription note give the plate reading *curremus*.
- n. 2 carries DE *non fide* (281.3) and n. 16 carries 283.6–7 variants. Each note is anchored a sentence or more away from its line. The descriptions are accurate, so this is not flagged.
- *Doctores legis* (283.18), "doctors of law", follows Loserth's side-note. Lanfranc as a doctor of law is arguable (he trained in law), and the chunk does not settle whether *lex* here is canon law or God's law. Not flagged.
- **Headnote:** none owed.

## Counts

| class | error | weak | style |
|---|---|---|---|
| 1 terms | 0 | 0 | 3 |
| 2 connectives | 0 | 0 | 0 |
| 3 medieval sense | 0 | 1 | 0 |
| 4 construal | 0 | 0 | 3 |
| **total** | **0** | **1** | **6** |

Overall: a sound chunk, with its connectives clean and its construals flagged where they are open. The work left is conforming three wave-24 rows and one sense of *concludere*.

## Applied 2026-11-09

- Rows 1–7: applied.
- Not rows, not applied: bt p281 *currremus* (process item).

Lint after application: 0 problems (93 chunks).
