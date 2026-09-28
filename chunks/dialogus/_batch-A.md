# Batch A: *Dialogus* chapters 1–5 (`wyc-dialogus-01` … `-05`)

M3, 2026-09-28. All five chunks at `status: translated`, lint clean.

## Chapter 1: pilot carried into the scaffold

- Headnote, English, notes 1–12 and transcription notes carried from `pilots/wyc-dialogus-01.md`
  unchanged, except one headnote sentence. The pilot said "Our Latin is the Fordham transcription,
  collated word by word against the plates", which is no longer true of this file. It now says the
  Latin is Pollard's printed text checked against six witnesses, with the unsettled words read on
  the plates. `[verify which is which]` and V-13 are kept as they were. **Wilson to confirm the
  rewording.**
- Section labels: Prologue · 1.1–1.12; Truth · 1.13–2.11; Truth (cont.) · 2.12–3.13 (the pilot
  labels, with the scaffold's ranges).
- Side-notes re-keyed on plates n32–n34: 1.6 and 1.9, not the pilot's 1.7 and 1.10. The pilot's 2.5
  note is three marginal blocks (2.5, 2.7, 2.9).

## Ledger rows

| id | chunk / note | claim | status | how / next step |
|---|---|---|---|---|
| D02-1 | dialogus-02 n1 | The eagle, gazing at the sun, as a medieval figure of contemplation and of John the Evangelist | to-verify | From memory. Check e.g. Augustine, *Tract. in Ioh.* 36.5, or a bestiary text |
| D02-2 | dialogus-02 n3 | Augustine reads the Psalms' *montes* as the great men of the church (apostles, preachers): *En. in Ps.* 71.5, 120.4 | to-verify | From memory; Pollard gives no reference. augustinus.it, *En. in Ps.* 71 and 120 |
| D02-3 | dialogus-02 n5 | John 10:38 at 5.11 | editor | Pollard's margin reference *John x. 38* (plate n36); text checked with bible.py |
| D03-1 | dialogus-03 n2 | "First commandment of the second table" = Honour thy father and mother; the Augustinian division counts it fourth and Wyclif follows it; Pollard's "fifth" is the Protestant count | to-verify | From memory. Check Augustine, *Quaest. in Hept.* II.71, and Wyclif, *De mandatis divinis* |
| D03-2 | dialogus-03 n4 | Truth's voice changes after chapter 3 | editor | Pollard, intro p. vi (as cited in the pilot, n. 3) |
| D03-3 | dialogus-03 n7 | Matt. 21:2 at 7.10 | editor | Pollard's margin reference *Mat. xxi. 2* (plate n38); text checked with bible.py |
| D04-1 | dialogus-04 n2 | *Concessio stulta cesaris* = the imperial endowment; the *Dialogus* calls it *ista stulta donacio* (p. 18) and blames Constantine for it (p. 72) | verified | Read this session in `text/dialogus/p018.la.txt` (*stulta donacio … capitale dominium supra cesarem*) and `p072.la.txt` (*dicitur constantinum anglicum istam vesaniam diabolicam presumpsisse*). Line numbers not yet taken from the plates |
| D05-1 | dialogus-05 n7 | *Pauperes … sacerdotes* anticipates the "poor priests", the preachers associated with Wyclif | to-verify | From memory. Not found by a search of the *Dialogus* Latin for *pauperes sacerdotes*. Check a standard account (e.g. Workman; Hudson, *Premature Reformation*) |
| D05-2 | dialogus-05 n7 | In canon law the secular arm carried out the church's sentences on heretics | to-verify | From memory. Check e.g. *Ad abolendam* (X 5.7.9) |

Scripture identifications were checked with `scripts/w3/bible.py` (Num. 18:20–24; Deut. 18:1–2;
Ezek. 44:27–31; John 8:7; 10:37–38; Matt. 4:8–10; 5:17; 21:2; Jer. 3:3; Apoc. 2:9, 3:9;
Ps. 118:21; Rom. 1:32; Mal. 4:2), so they have no rows. The DR wordings belong under V-18.

## Glossary proposals

Rendered as below in the chunks, untagged.

| Latin | proposed English | where / why |
|---|---|---|
| liberum arbitrium | free choice | 4.15 (*corpus liberi arbitrii*). The scholastic term. Pollard's side-note has "free judgment". |
| heretica pravitas | heretical depravity | 7.5, 7.8. The formula of the heresy courts; keep it recognisable. |
| indispositus; (se) indisponere | unfit; make (oneself) unfit | 4.1–2, 5.2, 7.5–8. ⛔ Not "indisposed", which now means "unwell". |
| ex fide | as faith teaches | 9.2, 9.5, 9.24 (and 11.7). "It is of faith", i.e. on scripture's authority. The alternative, "in good faith", is noted at ch. 4 n. 5. |
| limitare (officium) | assign | 4.5, 4.26–27. Not "limit". |
| prevaricator; prevaricancia | transgressor; transgression | 10.10. At 9.24 *basali prevaricancia* seems to need the root sense ("going beyond"); see ch. 5 n. 2. |
| carecter (sensibilis) | (perceptible) character | 5.7. The mark of orders; not "reputation". |
| lex gracie | the law of grace | 10.3. The new law, opposed to *lex vetus*. |
| curia romana | the Roman curia | 7.8. |

## Latin doubts

| page.line | printed | doubt | settled? |
|---|---|---|---|
| 1.10 | *jo 14°, et* | The scaffold has *14° et* with no comma; the pilot (Fordham) has the comma | **Plate n32: comma printed.** The scaffold lost it in normalisation. Not edited; fix it in the Latin if the text is regenerated |
| 3.13 / 3.14 | — | The pilot ended chapter 1 at 3.14 | Plate n34: the last line is 13, so the scaffold is right |
| 3.19 | *dominaret* | B, B¹, C *dominaretur* | Print form kept; the sense is the same |
| 5.16 | *noscat in gradum qui sibi pertineat legem dei* | Awkward. B, C: *noscat quid sibi pertineat secundum legem dei* | The print construes ("in the degree that pertains to him"); kept, with a C note (ch. 3 n. 1) |
| 9.17 | *omnium pecorum progenitorum* | Does not construe. B: *primogenitorum* | Plate n40 confirms the print. **Translated B's reading** under §5.2, with a T note (ch. 5 n. 1) |
| 9.20 | scaffold *domuisue* | A word-division artefact | Plate n40: *domui sue*. Not edited |
| 9.21–22 | scaffold *Et de pecoribus*, *ut Patet* | Capitals in mid-sentence | Plate n40: lower case, *et*, *patet*. Case artefacts; not edited |
| 9.24 | *cum basali prevaricancia* | Obscure. B, B¹, C *in* for *cum* | Plate n40 confirms the print. Translated as printed with a C note (ch. 5 n. 2); the construal is still doubtful |
| 10.4 | scaffold *nisiistam nephariam,quod* | A word-division artefact | Plate n41: *nisi istam nephariam, quod*. Not edited |
| pp. 9–10 apparatus | — | The apparatus line numbers often run one line ahead of the text | Noted in ch. 5's transcription notes. Our notes cite text lines |

## Counts

| chunk | Latin words | notes | words per note |
|---|---|---|---|
| wyc-dialogus-01 | 457 | 12 (pilot) | 38 |
| wyc-dialogus-02 | 385 | 5 | 77 |
| wyc-dialogus-03 | 382 | 7 | 55 |
| wyc-dialogus-04 | 421 | 6 | 70 |
| wyc-dialogus-05 | 380 | 7 | 54 |

Chapters 3 and 5 are above the target density because each carries a long Old Testament quotation
that departs from the Vulgate. Plates n35 and n41 were missing and were fetched into
`text/dialogus/raw/leaves/`.
