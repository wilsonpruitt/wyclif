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
