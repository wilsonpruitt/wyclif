# Tokenfix audit, batch 1 (tokenfix-1.tsv, 70 rows)

Each row read on the plate (`text/ecclesia/raw/leaves/`). Verdicts: OCR = fix right; PRINT = the print shows the "printed" form (fix is an emendation); OTHER = print shows neither, and the fix does not give what the print shows; NOT-FOUND.

| tsv_line | page | printed | fixed | verdict | what the print shows |
|---|---|---|---|---|---|
| 2 | 14 | pon-i, | pontifici | OCR | *pon-* / *tifici* across the line break |
| 5 | 36 | Matth.XXlV0 | Matth. XXIV° | OCR | Matth. XXIV° |
| 6 | 46 | XL1, | XLI, | OTHER | **XLⁱ,** (superscript i, ordinal ending = Ps. XL, Vulg. 40:10), not XLI (41) |
| 7 | 76 | JeremiasVII0, | Jeremias VII°, | OCR | Jeremias VII°, (tight spacing) |
| 8 | 79 | impossibile° | impossibile | OCR | impossibile, no mark |
| 10 | 103 | 111% | IIIª | OTHER | **III°,** (degree sign and comma; our Latin has *IIIª* and no comma) |
| 11 | 125 | artii46aculum | articulum | OCR | *arti-* / *culum*; 146ª is the margin folio mark |
| 16 | 175 | i53"Petrus | Petrus | OCR | Petrus; margin folio mark |
| 17 | 214 | iuxtaposiHi58ccionem | iuxtaposicionem | OCR | *iuxtaposi-* / next line; margin mark |
| 23 | 294 | XXXIII0)? | XXXIII°)? | OCR | XXXIII°)? |
| 28 | 400 | XL.IV0, | XLIV°, | OCR | XLIV°, (no point) |
| 29 | 409 | mixtim= | mixtim | OCR | mixtim |
| 32 | 488 | 11% | IIª | OTHER | **II°,** (Canticorum II°, 4); already superseded by tokenfix.tsv line 611 (IIª→II°,) |
| 33 | 572 | 11% | IIª | OCR | IIª, (note: print has a comma after IIª that our Latin lacks: "q. IIª super") |
| 36 | 565 | i5(rogo) | (rogo) | OCR | (rogo); 15 is the line number |
| 37 | 584 | tanto4X | tanto | OCR | tanto; 4 X in the margin |
| 74 | 479 | inquibus | in quibus | OCR | *in quibus* (italic, narrow space) |
| 82 | 16 | be | | OCR | side-note "We must be careful…"; nothing in the Latin |
| 98 | 32 | is | | OCR | side-note "The Church is…"; nothing in the Latin |
| 106 | 48 | of | | OCR | side-note "Our pretence of…"; nothing in the Latin |
| 110 | 60 | the | | OCR | side-note "Answer to the…"; nothing in the Latin |
| 111 | 59 | quod. | quod | OCR | quod, no stop |
| 112 | 62 | eis,. | eis, | OCR | *eis,* then a faint grey speck, smaller than a stop and above the baseline; not a stop |
| 113 | 60 | sal- | salvator | OCR | *sal-* / *vator* across the line break |
| 116 | 65 | 3 | 31: | OCR | 31: (letterspaced figures) |
| 117 | 65 | 1: | | OCR | second half of 31: |
| 120 | 70 | [illud | illud | OCR | illud, no bracket |
| 124 | 75 | 9% | 9: | OTHER | **9°,** (degree sign and comma; our Latin has "9:") |
| 125 | 70 | dic | dicit: | OCR | dic˙t: (broken i, only its dot inked); *dicit:* reads damaged type |
| 130 | 80 | ex-i | expresse | OCR | *ex-* / *presse* across the line break |
| 131 | 80 | presse | | OCR | second half of ex-presse |
| 133 | 84 | 111° | III° | OCR | III° |
| 140 | 90 | Si | Sic | **PRINT** | **Si cenim** (the space is misplaced in the print) |
| 142 | 90 | not | | OCR | side-note "Knowledge not going beyond…" |
| 143 | 91 | 11°, | II°, | OCR | II°, |
| 144 | 92 | desceni4iadunt | descendunt | OCR | *descen-* / *dunt*; margin mark |
| 145 | 93 | limi | limitavi | **PRINT** | **limı avi**: the t is missing (blank sort), second i undotted, a damaged |
| 149 | 96 | no | | OCR | side-note "Separation is no bar to unity" |
| 170 | 116 | to | | OCR | side-note "We have to solve…" |
| 157 | 108 | 111° | III° | OCR | XVIII° (Sap. XVIII° 14, 15) |
| 158 | 109 | 143° | | OCR | margin folio mark *143ᵉ* (with P) |
| 160 | 109 | linquit, | inquit, | OCR | inquit,; margin line number 1 |
| 173 | 120 | 111° | III° | OCR | III° |
| 175 | 123 | quod. | quod | OCR | *eo quod* at line end; the "." is from the side-note number "4." |
| 177 | 124 | ad- | | OCR | side-note "At the last ad-/vent" |
| 178 | 125 | 111° | III° | OCR | III° Reg. |
| 179 | 125 | 1 | | OCR | first figure of the letterspaced "1 1:" (= 11:) |
| 180 | 125 | 1: | 11: | OCR | Hebr. IX°, 1 1: (letterspaced 11) |
| 181 | 126 | ht | Et | OCR | Et |
| 183 | 127 | est. | est | OCR | "Christus est homo", no stop |
| 184 | 127 | nostra! | nostra: | OCR | nostra: |
| 187 | 133 | IIª. | IIª | **PRINT** | **IIª. Corinthiorum**: a clear stop after IIª (italic) |
| 188 | 134 | be | | OCR | side-note "We must be careful…" |
| 195 | 143 | 111° | III° | OCR | III° Regum |
| 196 | 144 | of | | OCR | side-note "3. because of danger…" |
| 197 | 145 | peccata. | peccata | OCR | peccata at line end, no stop |
| 200 | 149 | testimonis | testimonio | **PRINT** | **testimonis** ("quia ex testimonis Christi"), clearly printed |
| 202 | 152 | in Nec | Nec | OCR | Nec; no "in" in the text |
| 204 | 154 | Eta | Et | OCR | Et patet |
| 206 | 156 | nudei5o"0 | nude | OCR | nude; 150ª O in the margin |
| 208 | 158 | ab- | | OCR | side-note "2. That we ab-/jure…" |
| 212 | 162 | extraDi5ibneos | extraneos | OCR | *extra-* at foot of page, folio mark in margin |
| 216 | 169 | [enim | enim | OCR | enim; 152ª I in the margin |
| 217 | 170 | cis | eis | OCR | eis |
| 221 | 173 | domne | omne | OCR | omne; 152ᵈ in the margin |
| 222 | 174 | to | | OCR | side-note "A case as to privilege." |
| 225 | 176 | et- | et | OCR | et (potestate, et omnis) |
| 226 | 176 | of | | OCR | side-note "Divestment of…" |
| 228 | 178 | principaliter] | principaliter | OCR | *prin-*/*cipaliter*, no bracket |
| 229 | 179 | 1 | 11: | OCR | Matthei XI°, 1 1: (letterspaced 11) |

## Counts

- OCR: 62
- PRINT: 4 (140 *Si* [cenim] p. 90; 145 *limi avi* p. 93; 187 *IIª.* p. 133; 200 *testimonis* p. 149)
- OTHER: 4 (6 XLⁱ p. 46; 10 III°, p. 103; 32 II°, p. 488, already superseded by tokenfix line 611; 124 9°, p. 75)
- NOT-FOUND: 0

Side observation: at 572 (row 33) the print has a comma after IIª ("q. IIª, super") that our Latin lacks.
