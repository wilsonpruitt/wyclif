# Tokenfix audit, part 2 (plate reads)

Rows from `tokenfix-2.tsv`, each checked against the Loserth plate in `text/ecclesia/raw/leaves/`.
Verdicts: OCR = print does not show the "printed" form (fix right); PRINT = print shows the "printed" form (fix emends the print); OTHER = print shows something else; NOT-FOUND.

| tsv_line | page | printed | fixed | verdict | what the print shows |
|---|---|---|---|---|---|
| 231 | 180 | quoa | quo | OCR | "in quo" + margin letter "a" (l.17) |
| 232 | 180 | de: | de | OCR | "de * affeccione": folio asterisk, no colon (l.27) |
| 246 | 182 | Pri- | (del) | OCR | side-note "Objection: Pri-vilege..." |
| 247 | 182 | mais | magis | OCR | "magis infigitur" (l.14) |
| 249 | 184 | are | (del) | OCR | side-note "Exemptions are bad in kind" |
| 251 | 188 | incita- mento | incitamento | OCR | "incita-" line-end / "mento" next line (l.14-15) |
| 253 | 192 | for | (del) | OCR | side-note "It is wrong for the clergy" |
| 255 | 196 | 1 | 15 | OCR | "II°, 15" (spaced "1 5") (l.7) |
| 256 | 196 | 1: | 13: | OCR | "III°, 13:" (l.10) |
| 258 | 197 | 56° | (del) | OCR | margin folio marks "156ᵃ"/"156ᵇ" |
| 261 | 198 | 111°, | III°, | OCR | "Johannis III°, 29," (l.9) |
| 262 | 198 | christiani? | christiani | OCR | "christiani" + margin letter "7"(=?), no "?" (l.14) |
| 264 | 198 | 5, | (del) | OCR | "II°, 15," (second half of spaced 15; paired row gives 15,) (l.17) |
| 268 | 201 | 111°, | III°, | OCR | "Cor. III°, 6," (l.31) |
| 269 | 202 | Iiii | hii | OCR | "ibunt hii" (l.28) |
| 270 | 204 | ii°, | 11, | OTHER | print "VI°, 11°," — degree sign IS printed after 11; fix "11," drops it (l.10) |
| 271 | 202 | 111°) | III°) | OCR | "Canticorum III°)," (l.25) |
| 274 | 208 | 1: | 13: | OCR | "IX°, 13:" (l.10) |
| 275 | 210 | 35,- | 35, | OCR | "35," (comma with a faint speck above, broken type; no dash) (l.17) |
| 278 | 212 | cantatis | caritatis | OCR | "caritatis amorem" (l.2) |
| 279 | 213 | quia- | quia | OCR | "quia" (l.23 clean; l.25 "quia" has a stray struck mark over the a, print blemish, not a hyphen) |
| 281 | 219 | [quin | quin | OCR | "L 159ᵇ quin" — no bracket (l.1) |
| 282 | 221 | 1, | 15, | OCR | "XVIII°, 15," (l.28) |
| 283 | 222 | the | (del) | OCR | side-note "At least the criminals" |
| 286 | 224 | 111° | III° | OCR | "III° Decretalium" (l.15) |
| 290 | 230 | is | (del) | OCR | side-note "Forgiveness is good" |
| 292 | 233 | ahenis | alienis | OCR | "bonis alienis" (l.28) |
| 295 | 244 | of | (del) | OCR | side-note "The period of immunity" |
| 297 | 250 | quodam-, | quodam | OCR | "quodam-" at line-end (l.15) + "modo" (l.16); no comma. NB the print hyphenates one word across the break (quodam-/modo); our "quodam modo" splits it |
| 306 | 258 | est?. | est? | OCR | "ideo necesse est" + line no. 25 (l.25): no "?" or "." in the print (witness box leaf 295 line 24); fixed form "est?" itself not in print |
| 314 | 269 | domum:,: | domum | OCR | "domum * materialem" (folio asterisk) (l.5) |
| 319 | 274 | 1 | 11 | OCR | "Baruch I°, 11," (spaced "1 1") (l.5). NB print has roman "I°", our context shows "1°" |
| 325 | 280 | not | (del) | OCR | side-note "An heir is not bound" |
| 327 | 282 | is | (del) | OCR | side-note "but the King is bound" / line no. 15 |
| 328 | 284 | of | (del) | OCR | side-note "The clergy of the O.T." |
| 330 | 288 | to | (del) | OCR | side-notes "We ought to give to the clergy" / "to the poor" |
| 339 | 298 | to | (del) | OCR | side-note "It is heretical to infringe" |
| 345 | 302 | est';— | est? — | OCR | "factus est? —" (l.7) |
| 347 | 302 | not | (del) | OCR | side-note "If Christ could not rule" / "Christ could not" |
| 349 | 305 | possess | possessio | OCR | "nec possessio" (l.11), next to side-note |
| 351 | 308 | be | (del) | OCR | side-note "There should be no distinction" |
| 356 | 310 | -Christus | Christus | OCR | "manda. Christus" (l.17) |
| 359 | 312 | corum. | eorum. | OCR | "eorum." (l.1), e clear on zoom |
| 372 | 319 | perrecta | perfecta | OCR | "est perfecta" (l.31) |
| 374 | 322 | acci- pit | accipit | OCR | "acci-" line-end / "pit" (l.5-6) |
| 375 | 322 | his | (del) | OCR | side-note "Christ bade his clergy" |
| 383 | 323 | maior( ut | maior (ut | OCR | "maior (ut patet" (l.22-23) |
| 387 | 330 | qual | qua | OCR | "prima qua" + margin numeral "1" (l.13) |
| 402 | 338 | no | (del) | OCR | side-note "If he had no power" / line no. 20 |
| 406 | 349 | exemp | exemplo | OCR | "innituntur exemplo" (l.17) |
| 408 | 350 | puni- | punitiva | OCR | "puni-" line-end / "tiva" (l.12-13) |
| 410 | 351 | quia ut | quia (ut | OCR | "quia (ut" (l.19) |
| 415 | 358 | Gre- | Gregorium | OCR | "Gre-" line-end / "gorium XI." (l.19-20) |
| 424 | 360 | us | (del) | OCR | side-note "Christ bade us" |
| 430 | 364 | recipere,; | recipere, | OCR | "suum recipere," (l.8) |
| 432 | 365 | fui-t | fuit | OCR | "fuit nude" (l.17) |
| 433 | 368 | inor-i8o°H | inordinate | OCR | "inor-" line-end + margin folio "180ᵃ H" / "dinate" (l.1-2) |
| 444 | 377 | nro | pro | OCR | "et pro iterata" (l.1) |
| 445 | 378 | 111° | III° | OCR | "cap. III° et VII°" (l.29) |
| 447 | 380 | of | (del) | OCR | side-notes "Falseness of" / "Example of" |
| 448 | 380 | terre-2 | terrenorum | OCR | "terre-" line-end + margin numeral "2" / "norum" (l.6-7) |
| 449 | 380 | norum | (del) | OCR | second half of the same split (l.7) |
| 462 | 381 | ,5priorem | priorem | OCR | line no. "15" in margin + "priorem" (l.15) |
| 467 | 387 | populo, | populo | OCR | "populo laicali" — no comma (l.12) |
| 478 | 393 | ilia | illa | OCR | "tunc illa est" (l.2) |
| 479 | 394 | the | (del) | OCR | side-note "In denying the previous" |
| 483 | 394 | 1 | 1: | OCR | "Isaie IV°, 1 :" (colon printed, spaced) (l.25) |
| 486 | 398 | SUnt | sunt | OCR | "sunt cum Christo" (l.12) |
| 487 | 398 | to. | (del) | OCR | side-note "He tries to prove" |
| 491 | 404 | falsum. | falsum, | OCR | "fuit tunc falsum," (zoom) (l.7) |

## Counts

- OCR: 69
- PRINT: 0
- OTHER: 1 (270, p.204 l.10: print "Canticorum VI°, 11°," — the ° after 11 is printed; our "11," silently drops it)
- NOT-FOUND: 0

Side notes (not tokenfix verdicts): 319 our Latin has "Baruch 1°" where the print has roman "I°"; 297 the print hyphenates "quodam-/modo" across the line, our Latin splits it as two words.
