# Review: *De eucharistia*, chunk 02-e (pp. 44.1–48.22)

Reviewer: independent, fresh session, 2026-11-09. Method: I went sentence by sentence through Loserth's Latin (the `>` blocks) against the English, using `CARD.md` (read whole), CONVENTIONS §§6–9, 12, 14 and the 2026-11 log rows, and GLOSSARY.md (grepped per term). I accounted for every *enim / nam / ergo / igitur / ideo / sed / autem / vero / tamen / itaque / unde / ymmo / quia* in the chunk. None is omitted. *Autem* at 47.30 is rightly "now": it brings the minor premiss of the third main argument, which *ergo* (47.31) closes. *Sed* at 46.15, 46.17 and 46.25 and *autem* at 44.24, 45.14 and 48.5 are rightly "but". *Vero* at 44.17 and *autem* at 44.7, 46.16 and 46.21 are rightly "and". *Tamen* at 47.5 is the only connective row (row 5). I counted every page.line from `text/eucharistia/bt/p44–p48.txt`. I checked every T note against `apparatus.json` (leaves 115–119, which carry pp. 44–48), and they agree, except for note 25's AB reading, which I read on the plate foot (n0119; row 6). I also read the plate at 48.13 (row 6 and Latin doubts). Lint is clean. I did not re-verify the sources in the notes, and I did not check quotation bounds against the italics.

Classes: 1 terms · 2 connectives · 3 medieval sense · 4 construal, or a note/title contradicting the text.

**Exact strings.** "Current" and "proposed" are copied exactly from the file and are meant for find/replace. I checked each "current" string with grep, and each occurs once in the file. Where a string runs across a line break, **⏎** stands for the newline plus the next line's own indentation. No string in this review needs one.

| # | page.line | Latin | current English | class | severity | proposed English | reason |
|---|---|---|---|---|---|---|---|
| 1 | 45.30–32 | *Ex istis patet quod non oportet si Deus intelligit … quod nos in toto debemus loqui conformiter* | "it does not follow, if God understands" | 4 | weak | "it is not necessary, if God understands" | *Non oportet … quod* says the thing need not be so. It does not say that it fails to follow. "It does not follow" turns a claim of necessity into a claim about an inference, and the card keeps the language of inference (*sequitur*, *consequencia*) for those words. |
| 2 | 44.2 (n. 1) | *Factus* (emended *tactus*) | "\"[Touched] inwardly" | 4 | style | "\"Touched inwardly" | Note 1 translates the emendation *tactus*, so "touched" renders a word of the established text (as emended), and it is not a supplied word. Brackets mark English with no Latin behind it. |
| 3 | 47.17–18 | *panem post consecracionem* | "the [bread]{g:panis} after consecration to be" | 1 | style | "the [bread]{g:panis} after [consecration]{g:consecracio} to be" | This is the chunk's first *consecracio* (row *consecracio* "consecration"), and it is untagged. |
| 4 | 48.20 (n. 25) | *quia ipsis remanentibus committeretur ydolatria* | "since, if they remained, idolatry" | 4 | style | "since, if they [the bread and wine] remained, idolatry" | Note 25 rightly takes *ipsis* as the bread and wine. In the English, though, "they" comes straight after "the accidents remain", and it reads as the accidents, which is the construal the note rejects. The bracket makes the English carry the note's choice. |
| 5 | 47.5 | *dum tamen debemus niti apciori modo* | "whereas we ought to strive" | 2 | style | "while yet we ought to strive" | *Tamen* has no word of its own in the English. The table gives "yet". "Whereas" carries the contrast but merges *dum* and *tamen*. |
| 6 | 48.15 (n. 25) | foot "15. AB: corr." | n. 25 "AB *corri[mpitur]*" | 4 (note) | style | "AB *corr.* (abbreviated)" | On the plate (n0119 foot), the reading is *corr* with an abbreviation mark. It is not *corri…*: the `apparatus.json` OCR turned the mark into "i". The supplied ending invents a misspelling. |
| 7 | 44.13–15 (n. 5) | *non enim punit Deus predestinatum ut prescitum* | n. 5 "**G.** *Prescitus*: \"the foreknown\", Wyclif's term for those God foreknows will be damned, against *predestinatus*, \"the predestinate\". *Ad puniti demeritum*" | 1 (note) | style | "**C.** *Ad puniti demeritum*" | The *prescitus* row asks for a note at the first occurrence per work. That is 01-b (n. 11, already given). Here the G sentence only restates the row, and the tag already does that job. What is left of the note is a construal. |

## Latin doubts

- **45.20, 45.23** · printed *serenitate*, *serenitatem* · The Vulgate (Rom. 11:22) reads *severitatem*, and the run *austeritate et usura … severitate* would read better with it. Both the print and the four-scan vote give *serenitatem*, and the foot has no variant except D's *Rom. XI* and ABCE *dicit* for *Dei*. · Not settled. Under the card's rule the print governs, and note 13 already gives the Vulgate. I suspect an early error (*seve-/sere-*). I recommend that note 13 say so, as "possibly an error for *severitatem*", if the coordinator agrees.
- **44.25** · printed *per punicionem* · CDE *per penitudinem*. The clause then speaks of *finis penitudinis* and *imperfeccionem in penitente*, which suggests that the subject is God's repenting (Gen. 6:6). With the print, the clause comes close to tautology. · The print construes, and note 8 gives both readings, so it is left as it stands under the rule. I flag it only as a doubt.
- **48.13** · printed *remanent* (plate n0119 confirms) · The foot gives "B: *remanent*", which is the same as the print. Either Loserth's lemma was meant to be *remanet*, or the entry is null. · Read on the plate. It does not affect the English.
- **44.8** · printed *ab inusu* · Possibly a misprint for *abusu*. C *ab usu* is translated (n. 3). · Not settled on the plate. The English stands either way ("use" or "misuse" of earthly things); I note it for the coordinator.

## Outside the four classes (process; not counted)

- **Transcription notes, variants line**: "45.2? ABCE *exponentes*". The line is 45.28 (*exposiciones*, bt p045 l. 28). Proposed: replace "45.2?" with "45.28".
- **Transcription notes, "Omitted per §3.5" line**: "reference 2. Gen. VI, 6. (). ib. 7. 22. ib. 1 [. (44.31)" is OCR noise from Loserth's source block (Gen. 6:6 at l. 2, 6:7 at l. 9, 6:11 at l. 22). It should be cleaned or deleted.
- **n. 10**: "inextricably" for *insolubiliter* follows the row. The note's gloss "beyond loosing" is fine.
- **Headnote:** none owed.

## Counts

| class | error | weak | style |
|---|---|---|---|
| 1 terms | 0 | 0 | 2 |
| 2 connectives | 0 | 0 | 1 |
| 3 medieval sense | 0 | 0 | 0 |
| 4 construal | 0 | 1 | 3 |
| **total** | **0** | **1** | **6** |

Overall: a clean, careful chunk. The objection's syllogism (47.28–31) is rendered right, and the hard construals all carry notes. The fixes are one modal (*non oportet*), a stray bracket, a missing tag, and two note touches. The *serenitatem* doubt (45.20–23) is the one textual point worth a ruling.

## Applied 2026-11-09

- Rows 1–7: applied.
- *Serenitatem* doubt (45.20–23): ruled by the coordinator, print and "serenity" kept, n. 13 unchanged.
- Not rows, not applied: the transcription notes' "45.2?" → "45.28" and the OCR noise in the "Omitted per §3.5" line (process items).

Lint after application: 0 problems (93 chunks).
