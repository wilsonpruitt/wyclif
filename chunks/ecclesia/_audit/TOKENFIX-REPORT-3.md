# Tokenfix audit, part 3 (plate reads)

Rows from `tokenfix-3.tsv`, each checked against the Loserth plate in `text/ecclesia/raw/leaves/`.
Verdicts: OCR = print does not show the "printed" form (fix right); PRINT = print shows the "printed" form (fix emends the print); OTHER = print shows something else; NOT-FOUND.

| tsv_line | page | printed | fixed | verdict | what the print shows |
|---|---|---|---|---|---|
| 493 | 406 | 0 | O | OCR | "O mulier magna est fides tua" (l.10) |
| 495 | 407 | 3 | 31: | OCR | "Matthei XIV°, 31:" (spaced "3 1:") (l.14) |
| 496 | 407 | 1: | (del) | OCR | second half of "31:" (l.14) |
| 497 | 408 | act | (del) | OCR | side-note "Faith is the act of believing" |
| 498 | 409 | 2 | (del) | OCR | margin division numeral "2" (left of "modo dicta", l.23) |
| 499 | 409 | 111° | III° | OCR | "ut patet III° De Doctrina Christiana" |
| 501 | 409 | Presentem | presentem | OCR | "O 185ᵉ presentem iusticiam" (l.1; folio mark in margin) |
| 510 | 413 | bed | Sed | OCR | "in eternum. Sed revera" |
| 512 | 413 | dicitur! | dicitur | OCR | "qua dicitur quod descripcio" — no "!" (l.5) |
| 514 | 415 | respons | responsio | OCR | "Prima autem responsio" (l.11) |
| 516 | 416 | to | (del) | OCR | side-note "Authorities to show..." beside l.20 |
| 519 | 419 | 111 | in | OCR | "est Cardinalis in VI°" (l.2) |
| 520 | 421 | in. | in | OCR | "triumphans in nudo spiritu" — a tiny speck below baseline after "in", far smaller than the page's stops; blemish, not a point |
| 526 | 423 | Continue | continue | OCR | "15 continue una" (line number 15 in margin) |
| 527 | 424 | that | (del) | OCR | side-note "allows that the Church..." |
| 528 | 426 | XX | XXVII°, | OCR | "Matthei XXVII°, 40." |
| 530 | 427 | francie, | Francie, | OCR | "regnum Francie," (l.20) |
| 534 | 430 | not | (del) | OCR | side-note "We ought not to be silent..." |
| 536 | 434 | 5, | 15, | OCR | "CXXXI°, / 15, dicit sponsus" |
| 537 | 434 | Opus | opus | OCR | "Ulterius foret opus doctole" |
| 548 | 439 | 25— | 25—27°: | OCR | "Ephes. V°, 25—27°:" (one token in print) |
| 549 | 439 | 27°: | (del) | OCR | second half of "25—27°:" |
| 552 | 443 | lude | Iude | OCR | italic "Iude bene usus est" (capital I) |
| 553 | 443 | ludas | Iudas | OCR | "habuit Iudas officium" |
| 554 | 444 | ludas | Iudas | OCR | "Quod autem Iudas / fuit apostolus" (l.25) |
| 566 | 447 | lude | Iude | OCR | "Iude propter causam multiplicem" |
| 569 | 451 | mimine | minime | **PRINT** | italic "patres se esse mimine / recognoscunt" (l.25) — the print reads *mimine* (clear at 4x: m-i-m-i-n-e) |
| 570 | 457 | 111° | III° | OCR | "(ut patet III° Regum XII°" (l.15) |
| 583 | 461 | quosdam. | quosdam | OCR | "audivi quosdam instructos" — no stop |
| 584 | 463 | temporales- | temporales. | OCR | "divicie temporales. Et ex" |
| 585 | 463 | roret | foret | OCR | "non foret ut sic utilis" (l.6) |
| 587 | 463 | 1°, | I°, | OCR | "Joh. / I°, 12 exprimit" |
| 589 | 467 | 1° | I° | OCR | "scriptura I° Regum" (l.5) |
| 591 | 468 | iusti- | iusticiam, | OCR | "iusti-" line-end / "ciam," next line (l.1-2) |
| 592 | 468 | ciam, | (del) | OCR | second half of iusti-/ciam, |
| 597 | 470 | 111°, | III°, | OCR | "Johannis / III°, 1:" |
| 606 | 482 | bene. | bene | OCR | "christianus scit bene quid fecerit" — no stop |
| 607 | 486 | the | (del) | OCR | side-note "She gives the girdle in preaching to the heathen." |
| 609 | 490 | portis. | portis | OCR | italic "laudent eam in portis opera sua." — no stop after portis |
| 616 | 492 | 11°, | II°, | OCR | "Marci II°, 20" |
| 618 | 494 | ludas | Iudas | OCR | "Iudas est dyabolus" |
| 621 | 497 | io: | 10: | OCR | "Psalmi LXXVI, 10:" (l.1 marker "1" in margin) |
| 622 | 497 | 2in | in | OCR | "Sed vir iustus in casu" — no numeral in the text line |
| 630 | 512 | of | (del) | OCR | side-note "makes the ministration of the ordained effectual" |
| 631 | 512 | 4— | 4—7: | OCR | "Iª Cor. XII°, 4—7:" (one token) |
| 632 | 512 | 7: | (del) | OCR | second half of "4—7:" |
| 627 | 503 | domnino | omnino | OCR | margin letter "d" + italic "omnino inconveniens" |
| 639 | 515 | male | male. | OCR | "sive bene fieri sive / male. Nam in primitiva" — stop printed |
| 640 | 515 | apostolos. | apostolos | OCR | "apostolos suos sacerdotes" — no stop |
| 641 | 515 | eccle- | ecclesie | OCR | "ad alleviamen eccle-" line-end / "sie non habere" (tsv context points at an unhyphenated "ecclesie" earlier on the page; the hyphen is at the alleviamen line) |
| 642 | 515 | sie | (del) | OCR | second half of eccle-/sie |
| 644 | 516 | sed! | sed | OCR | "non legem solvere sed 199ᶜ 1" — folio mark and margin letter, no "!" |
| 649 | 524 | QUIS | quis | OCR | italic "ut cum quis suspendit se" — lowercase |
| 654 | 527 | G2oo°debite | debite | OCR | margin "G 200ᶜ" + "debite oraciones" (l.1) |
| 657 | 532 | are | (del) | OCR | side-note "All prayers are conditioned by the divine will" |
| 659 | 532 | tate, | (del) | OCR | "ex eius incapaci-" line-end / "tate, sed intencio" |
| 663 | 538 | COntraria | contraria | OCR | "purgandis contraria vel neutra" — lowercase |
| 672 | 558 | do | (del) | OCR | "alterius satisfaciendo pro" — printed whole, no break |
| 677 | 559 | 111°, | III°, | OCR | "Iª, Corinth. III°, 9" |
| 680 | 562 | of | (del) | OCR | side-note "The head of the Church is Christ's divinity;" |
| 681 | 564 | of | (del) | OCR | side-note "The merits of Christ and his Saints..." |
| 684 | 565 | -sufficerent | sufficerent | OCR | "requisita eque sufficerent ad" — no hyphen |
| 685 | 567 | 111,6), | III, 6), | OCR | "Act. III,6)," (print sets no space after the comma; spacing only) |
| 687 | 572 | can | (del) | OCR | side-note "If the Pope can excuse a part of penance he can excuse all." |
| 691 | 576 | may | (del) | OCR | side-note "The laity may give indulgence to the clergy." |
| 692 | 584 | far | (del) | OCR | side-note "4. And so far as the bishop's instruction..." |
| 693 | 584 | 1: | 13: | OCR | "Judith VIII°, 13:" |
| 698 | 202 | 111°), | III°), | OCR | "Canti-/corum III°), et sunt" (l.25) |

## Counts

- Rows checked: 68
- OCR: 67
- PRINT: 1 — **569** (p. 451, l.25): Loserth prints *mimine*; our Latin's *minime* is a silent emendation. Latin should keep *mimine* (English may follow *minime* with a T note).
- OTHER: 0
- NOT-FOUND: 0

Notes:
- 520 (p. 421 "in.") is the only borderline OCR call: there is ink after *in*, but it is a speck well below the baseline and far smaller than the page's full stops (compared at 4x with "triumphans." on the same page). Read as a blemish, not a point.
- 641 the tsv context points at an unhyphenated *ecclesie* earlier on p. 515; the actual *eccle-|sie* break is at "ad alleviamen eccle-/sie non habere". The fix is right either way.
