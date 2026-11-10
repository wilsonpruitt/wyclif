# Review: *De eucharistia*, chunk 05-a (pp. 115.6–119.26)

Reviewer: independent, fresh session, 2026-11-09. Method: I went sentence by sentence through Loserth's Latin (the `>` blocks) against the English, using `CARD.md` (read whole), CONVENTIONS §§6–9, 12, 14 and the 2026-11 log rows, and GLOSSARY.md (grepped per term). I accounted for every *enim / nam / ergo / igitur / ideo / sed / autem / vero / tamen / itaque / unde / ymmo / quia* in the chunk, and none is omitted. *Sed* at 117.23 is rightly "now", because it brings the minor premiss (the decretal cannot show the decree contrary to Christ's law, so the decree stands). *Sed* at 115.8 and 115.23 and *autem* at 118.30 are rightly "but". *Autem* at 116.17 and 116.29 is rightly "and". I counted every page.line from `text/eucharistia/bt/p115–p119.txt`. I checked every T note and every line of the transcription notes' variant list against `apparatus.json` (leaves 186–190, which carry pp. 115–119), and all of them agree. Lint is clean. I did not re-verify the sources in the notes, and I did not check quotation bounds against the italics.

Classes: 1 terms · 2 connectives · 3 medieval sense · 4 construal, or a note/title contradicting the text.

**Exact strings.** "Current" and "proposed" are copied exactly from the file and are meant for find/replace. I checked each "current" string with grep, and each occurs once in the file. Where a string runs across a line break, **⏎** stands for the newline plus the next line's own indentation. No string in this review needs one.

| # | page.line | Latin | current English | class | severity | proposed English | reason |
|---|---|---|---|---|---|---|---|
| 1 | 116.8–12 | *foret evidencius quod excludit figuram loquendo ydemptice quam dicendo, sicut dixit implicite, quod apostoli sunt palmites* | "it would be more evident that it excludes a figure, speaking [identically]{g:ydemptice}, than by saying" | 4 | weak | "it would be more evident that he excludes a figure by speaking [identically]{g:ydemptice} than by saying" | *Excludit* has the same subject as *dixit*, which is Christ. *Loquendo … quam dicendo* are two parallel gerunds of means. In the current English, "it" has no antecedent, and "speaking identically" does not run parallel with "by saying", so the comparison that carries the argument is blurred. |
| 2 | 116.5–12 (n. 6) | *cum antecedens locucio foret ad hoc efficacior; ut in isto dicto … Ego sum vitis vera* | n. 6 "a qualifier in the antecedent itself (as *vera* in \"the true vine\") would exclude figure more strongly than a following relative; the argument holds that even this would not exclude it." | 4 (note) | weak | "the antecedent speech itself, the identical predication *Hoc est corpus meum*, would exclude figure more strongly than the relative that follows it, as \"I am the true vine\", spoken identically (*ydemptice*), would more than the implied saying that the apostles are branches; the argument holds that even this does not exclude it." | *Antecedens locucio* is the preceding proposition as a whole, not a qualifier inside it. The Latin compares *loquendo ydemptice* ("I am the true vine") with *dicendo … quod apostoli sunt palmites*. It is not about the adjective *vera*. As written, the note misdescribes the comparison that the English beside it renders. |
| 3 | 115.18–20 | *Cum ergo Christus dicit Luce XXIIᵒ, 19: Hoc est corpus meum, statim subiungit* | "Since therefore Christ says in Luke 22:19, \"This is my body\", he at once adds" | 4 | weak | "When therefore Christ says in Luke 22:19, \"This is my body\", he at once adds" | *Cum* takes the indicative here (*dicit*) and is temporal. The point Scotus draws from Augustine's rule is that the words are followed at once by the relative, so the saying is not the cause of the adding. "Since" makes it the cause. *Ergo* is kept. |
| 4 | 115.28 | *quem demonstravit dicens: Hoc est corpus meum* | "which he pointed out, saying" | 1 | weak | "which he [demonstrated]{g:demonstrare}, saying" | GLOSSARY row *demonstrare (of a pronoun)* "demonstrate" (ruled 2026-11-09) covers exactly this: the bread is what *hoc* demonstrates, as note 5 says. The chunk's first occurrence should carry the row's word and its tag (as 09-g does). |
| 5 | 119.8 | *quod dominus Armachanus … declarat dici de hostia consecrata* | "makes clear is said" | 1 | style | "[makes clear]{g:declarare} is said" | This is the chunk's only *declarare*. The rendering follows the row, but the tag is missing (the card lists *declarare / ostendere* among the tagged rows). |
| 6 | 118.2 | *dampnificat suam universitatem* | "[damages]{g:dampnificare} his totality" | 3 | style | "[damages]{g:dampnificare} his [created] totality" | *Universitas* here is the created whole, God's universe, which is damaged by the destruction of created substances (*creatas substancias* just before). GLOSSARY renders the family "totality" (*universitas creata* "the created totality"). "His totality" on its own reads as Christ's own wholeness. |
| 7 | 119.17–18 | *suppono quod fiat interrogacio a periciori huius scole* | "by the more skilled of this school" | 4 | style | "by one of the more skilled of this school" | *A periciori* is singular and pairs with *a layco* ("a layman"). "The more skilled" reads as a plural group. |

## Latin doubts

- None open. *Ignorancie* (118.16) is absent from C's text and added in C's margin by another hand. The print keeps it and the note says so, so no plate read is needed. The Armachanus chapter number (119.8, *capitulo . . .*) is blank in the print, and note 15 says so.

## Outside the four classes (process; not counted)

- **n. 10** departs from the print (*glossa Beringarii* → ABCD *Bernhardi*). The card allows a departure only where the print will not construe. The print construes grammatically but names a gloss that does not exist, and the note gives both readings and the reason, so I have not flagged it. The coordinator may want to confirm this as a ruling under "Loserth's print governs".
- **n. 15**: *quem* (119.5) could grammatically take *Christum* as well as *panis*. The note sets *panis* only against *fraccione*, which is feminine and so impossible. The choice of *panis* is right (Augustine's *sacramentum panis*). Not flagged.
- **Headnote:** none owed.

## Counts

| class | error | weak | style |
|---|---|---|---|
| 1 terms | 0 | 1 | 1 |
| 2 connectives | 0 | 0 | 0 |
| 3 medieval sense | 0 | 0 | 1 |
| 4 construal | 0 | 3 | 1 |
| **total** | **0** | **4** | **3** |

Overall: a sound chunk. The connectives are clean, the variants are complete against the foot, and the predication is kept. The fixes are the John 15 comparison (English and note n. 6), one temporal *cum*, and two tags.

## Applied 2026-11-09

- Rows 1–7: applied.
- Not rows: n. 10 (*Bernhardi*) referred to the coordinator; n. 15 not flagged.

Lint after application: 0 problems (93 chunks).
