# Plate pass results: majority-error sweep + Latin doubts (plate 2026-09-29)

Every item below was read on Pollard's printed page (`text/dialogus/raw/leaves/nLEAF.jpg`, leaf = page + 31),
reading the whole line, and the apparatus at the foot where one was relevant. Line numbers come from the plate's margin
numbers. Nothing is committed.

## 1. Sweep (`_sweep/candidates.tsv`, 37 rows)

| form | page.line | plate reads | verdict | action taken |
|---|---|---|---|---|
| conse | 3.9 | *beatitudinem [conse]quendam.* (Pollard's supplement) | print confirms | none |
| vijdentur | 29.26 | *licet [vi]dentur esse beati* (the witnesses read the closing bracket as *j*) | **shared OCR error** | **FIXED**: OVERRIDE 29/198 → `[vi]dentur`; p029 regenerated (diff = that word only); chunk 15 blockquote synced |
| exiendo | 43.3 | *ymmo exiendo jerusalem* (apparatus 43.3: *exeundo* B, B¹, C) | print confirms | none |
| incollunt | 69.9 | *eo quod incollunt manen-/tem civitatem* | print confirms | none |
| necessitato | 71.1 | *et necessitato clero ex fide* | print confirms | none |
| Indii | 91.29 | *fideles Indii, qui tenent* | print confirms | none |
| deacceptum | 79.21–22 | *a domino de-/acceptum.* | print confirms (hyphenated across the line) | none |
| evidet | 67.3 | *et salubris evidet clero* | print confirms (already settled) | none |
| expergatum | 61.26–27 | *faciliter exper-/gatum.* | print confirms | none |
| sicitato | 38.24 | *ab homine sicitato di\*centi* | print confirms | none |
| senefectiore | 52.3 | *artis / senefectiore,* | print confirms; see LD-07 | none |
| corporia | 57.4 | *persecucio corporia sit* | print confirms; see LD-10 | none |
| dimutavit | 76.28 | *ordinem dimutavit.* | print confirms | none |
| fastidie | 1.1 | *mater fastidie et pulcra* | print confirms | none |
| pilativo | 9.2 | *judicio pilativo.* | print confirms | none |
| basali | 9.24 | *cum basali prevaricancia* | print confirms | none |
| derelinquerant | 69.12 | *fratres derelinquerant ab elemosinantibus* | print confirms | none |
| oculcius | 76.11 | *patencius vel oculcius conceperunt* | print confirms | none |
| sororisse | 39.7 | *sanctimoniales et sororisse cum* | print confirms | none |
| spissim | 34.19 | *heretici / spissim in ecclesia* | print confirms | none |
| simealis | 65.21 | *locus simealis a simili* | print confirms (already settled) | none |
| simiali | 70.14–15 | *locum a simi-/ali similitudine* | print confirms | none |
| simiali | 72.5 | *a simiali similitudine* | print confirms | none |
| simiali | 73.16 | *similitudine simiali;* | print confirms | none |
| recensius | 73.27 | *Sed demum recensius arguunt* | print confirms | none |
| iponences | 75.22 | *cives iponences reaccipere* | print confirms | none |
| iponenses | 31.3 | *cives iponenses illas possessiones* | print confirms | none |
| carectar | 47.5 | *vel carectar sensibilis*; see LD-03 | print confirms | none |
| extollenter | 50.1 | *hujusmodi extollenter;* (apparatus 50.1: *excellenter* B¹, C) | print confirms | none |
| crederit | 29.8 | *Quis ergo crederit tue sentencie* | print confirms | none |
| continuendum | 59.22 | *et non ad continuendum in sua culpa* | print confirms | none |
| wult | 89.31 | *nec deus / wult tale dominium* | print confirms | none |
| poterint | 96.21 | *Fundent sacerdotes nostri, si poterint,* | print confirms | none |
| cordate | 87.33 | *Sed excuciamus cordate* (last line of the page) | print confirms | none |
| duplicate | 9.25 | *ad sensum alium / duplicate.* | print confirms | none |
| papæ | 55.14 | *constitutiones papæ* (æ ligature printed) | print confirms | none |
| ecc | 47.23 | *sentencie eccᶜⁱ 34°* (superscript *ci*) | print confirms | none |
| luc | 81.30 | *dictum Christi lucᵉ 11°* | print confirms | none |
| malac | 47.26 | *ys. p°, Malac p°, cum aliis* | print confirms | none |

Result: 36 of 37 are genuine printed forms. There was one shared OCR error, *[vijdentur* → *[vi]dentur*.

OVERRIDE row appended to `text/dialogus/plate_decisions.tsv`:
`29  198  OVERRIDE  latinworks22wycl=uiidentur | … | iohanniswycliffe05wycl=uiidentur  [vi]dentur  plate n0060 2026-09-29 …`
After the change, `git diff` of `p029.la.txt` and `p029.tok.jsonl` shows only this word. `p029.check.tsv` changed its one row.

## 2. Latin doubts (`LATIN-DOUBTS.md`)

| id | plate reads | apparatus | verdict | action / recommendation |
|---|---|---|---|---|
| LD-01 | 43.28 *Ideo, ne in materia hujus fidei sim cecatus*: *ne* clear | 28. *credis quod, pro ne,* B¹, C | print confirms | closed; n2 stands |
| LD-02 | 45.16 *sive defendere quod \* vendebat*: clear | 16. *refundere corr. al. man. ex defendere,* B. *refundere,* B¹, C | print confirms | **Ruling for Wilson**: "warrant" (print) or "pay back" (B corr., B¹, C). I recommend keeping the print with n10, because Pollard's base MS and B's first hand agree on *defendere* |
| LD-03 | 47.5 *vel carectar sensibilis*: clear | 5. *caracter,* B, B¹, C | print confirms: a real base-MS spelling, not a misprint | closed; n5 stands |
| LD-04 | 47.13 *Similiter talis claustralis*; 48.10 *Ideo a talis oracionibus*: both clear | 47.13 *talis, om.* B, B¹, C; 48.10 *talibus,* B¹, C | print confirms | closed; n7 and n13 stand |
| LD-05 | 49.29 *indulgen-/ciarum in patria, tediose oneraciones fidelium hic in via*: clear | 29. *patria al. man. corr. ex papa,* B., *papa, sed al. man. in marg. patria,* B¹ | print confirms | closed. The *in patria / hic in via* antithesis on the same line supports the print. n8 stands |
| LD-06 | 50.30 *in angulo habitabilis / exaltatur*: clear | 30. *ab illis, pro habitabilis,* B, B¹, C | print confirms | closed; n12 stands |
| LD-07 | 52.3 *artis / senefectiore,*: clear | 3. *senefactorie corr. ex scenofactorie,* B, *scenofactorie,* B¹ (C not cited, so it agrees with the print) | print confirms | **Emendation question.** I recommend no Latin emendation: keep the print and n5, which already translates from B¹. An OVERRIDE to *scenofactorie* would put a witness reading into the established text, and that is a policy call for Wilson |
| LD-08 | 54.20–23 *sciencie que domini theologie graduacionem et confir-/macionem … vel omissionis vel commissionis sepius eveni-/unt … securitas est in istis*: all clear | 20. *ecclesie quemadmodum theologie ad decorem, pro sc. que dom. theol. grad.,* B, B¹, C; 22. *vel obmissius vel commissius,* B, B¹, C; 23. *multis, pro istis,* B, B¹, C | print confirms; no different word | closed; the construal stays in the C note (n6) |
| LD-09 | 55.23–24 *ultra ordinacionem domini prediligit / ordinantem*: no *non* in the print | 24. *non prediligit,* B, B¹, C | print confirms (Pollard's base MS lacks *non*) | **Emendation question for Wilson.** All three witnesses have *non*, and the sense "he does not love the Ordainer more" is the stronger argument. I recommend keeping the print (n11 already gives both), but this is the strongest emendation case in the list |
| LD-10 | 57.4 *cum persecucio corporia sit malum maximum*: clear | 3. *vivere vel, om.* B, B¹, C; 4. *non sit,* B, B¹, C (no variant for *corporia*) | print confirms | closed, no OVERRIDE: the plate has *corporia*. n6 stands |
| LD-11 | 57.32 *causa mundana / sapientem lucrum proprium*: clear | 32. *capiente, pro sapientem,* B, C, *sapiente corr. ex capiente,* B¹ | print confirms | **Emendation question.** I recommend no Latin emendation; keep the print and n13 (translated from B¹ *sapiente*) |
| LD-12 | 59.30 *non placet communitus deo suo*: clear | none | print confirms | closed |
| LD-13 | The bracket opens at 59.26 *[Ideo videtur quod domini tem-* and closes at 60.3 *domini capitalis.]* | 26. *Verba quae uncis inclusi, ut B, B¹, C, prorsus omittunt, ita codex noster non nisi in ima p[agina ap]posuit* (the letters are missing from the type on the plate; the identical formula at 61.28 prints *in ima pagina apposuit*) | the brackets are Pollard's; the passage stands in his text | closed; ch. 28 n8 is accurate |
| LD-14 | 60.21 *elemo-/sine perpetue a progenitoribus concessa*: clear | 20. *tempus, pro temporis*; *et, pro etiam*; 22. *licet, pro stat,* B, B¹, C | print confirms | closed. Minor point: the *licet/stat* variant is at 60.22 (*Stat ergo …*, the next sentence), not earlier in the same sentence. Ch. 29 n2 does not misstate it |
| LD-15 | 61.13–15 *nec sectis istis extraneis / aliquid elemosine corporalis, sed convertantur pure ad sectam / Christi, ut debent, et tunc potest eis talis elemosina impartiri*: clear. The THIN pivot 61.2 *ad quid nisi ad distribuendum pauperibus?* is also clear | 15. *sed, at al. man. nisi,* B, *nisi,* B¹, C | print confirms | closed. With the witnesses' *nisi*, *convertantur* has the sects as its subject beyond doubt ("unless they are converted"), and *et tunc … eis* supports the chunk's construal. Keep the C note. The [THIN] mark on 61.2 can be cleared |
| LD-16 | 63.8–9 *que a domino sunt pre-/cepta tollit qualitatem, quia virtutem cleri secundum limites / a domino nominatos*: *tollit* is printed | 8. *precipitanter tollunt, pro precepta, tollit,* B, B¹, C; *ewangelice, pro evangelacionis,* B, B¹, C | print confirms | closed. *Tollit* is in the print with *qualitatem*; the ellipsis is the second *tollit* in the *quia* clause, which is Wyclif's and not a dropped word. n12 is accurate |
| LD-17 | 90.14 *quod deus, concitor / eius, voluit*: clear; 90.9 *vocentur* | 9. *vocent,* C, D; no variant for *concitor* | print confirms | **Emendation question.** No witness supports *conditor*. I recommend keeping *concitor* and n20 as they are |
| LD-18 | 92.27 *esse veram. Quia aut, ut Averrois asserit,*: clear | none at 92.27 (the 92.5 lemma *vel, pro aut* is a different line) | print confirms | closed; n32 stands |
| LD-19 | 93.25 *attinet sunt ydonei in materia ista arguere*: clear | 25. *[non sunt?]*, Pollard's own conjecture; he reports no MS for it | print confirms | **Ruling for Wilson (it reverses the sense).** The whole paragraph goes on to disqualify the decretists, then the *iuriste* (*non valet tamen ipsorum loquela*), so the context favours Pollard's *non*. Options: (a) keep the print and n5 as now; (b) translate "are not fit" as Pollard's conjecture, with n5 reworded. I lean (b) |
| LD-20 | (no plate step) | — | — | still open: identifying *de bello clavo* is a source question (LEDGER DEB-2) |
| LD-21 | 81.1 *scilicet laboratores et alii*: clear | 1. *laborantes, pro laboratores,* B, B¹, C | print confirms | closed |
| LD-22 | 81.7 *debet / oracione vel merito*: clear | 7. *racione, pro oracione,* B, B¹, C | print confirms | closed |
| LD-23 | 83.5 *Et postmodum magister istius / ipocrisis*: *magister* printed | 5. *magister* B, B¹, C., *sed cod. nost. magisterio.* | print confirms (Pollard adopted the witnesses' reading) | closed. *Zelus magisterii* is a separate phrase at 83.15, also clear. n6 stands |
| LD-24 | 83.19 *in-/fundabilis et religioni Christi contraria*: clear | 19. *legi corr. al. man. in religioni,* B; *legi,* B¹, C | print confirms | closed; n7 stands |
| LD-25 | 84.28 *et tamen clerici remurmurarent*: clear | 28. *cum, corr. ex tamen,* B; *tamen, corr. ex cum,* B¹; *cum,* C | print confirms | closed; n4 stands |
| LD-26 | 85.17 *dotatos claustrales et alios onerosi.*: clear | 17. *onerosos,* B, B¹, C | print confirms | closed; n7 stands (translated from the witnesses) |
| LD-27 | 92.32 *legis dei \* expertes* (the \* is the D. 79 d. folio mark); 97.2 *obiectum / quadruplicem sunt quatuor responsiones* | 92.32 *sunt expertes,* C, D (and 31 *ludentes, pro videntes,* C, D); 97.2 *quadruplex,* C, D | print confirms both | closed. Both variants are in the chunk's notes: epil-b n1 (92.31–32) and n24 (97.2) |
| LD-28 | 97.30 *per idem enim non possit fingere* | 30. *antichristus, add. ante fingere,* C, D | print confirms | closed; located as epil-b n30 |

Tally: 22 closed with no change. 5 need a ruling: LD-02 and LD-19 (sense), LD-07, LD-09 and LD-11 (emendation). LD-17 comes with a recommendation to keep the print. LD-20 stays open as a source question.

## 3. English/notes to revise

- `chunks/dialogus/wyc-dialogus-15.md`: only the Latin changed (*[vi]dentur*). n6 already describes *[vi]dentur* as Pollard's supplement, so no English or note change is needed.
- `chunks/dialogus/wyc-dialogus-29.md`, n12 (LD-16): no change needed. n12 already says "*tollit* is understood again", which matches the plate.
- `chunks/dialogus/wyc-dialogus-29.md`, Transcription notes (lines 85–86): both [THIN] items, *ad quid nisi ad* and *distribuendum* (61.2), read clearly on plate n0092 (*sed / ad quid nisi ad distribuendum pauperibus?*), so both [THIN] flags can be removed.
- `chunks/dialogus/wyc-dialogus-epil-b.md`, n5 (LD-19): rewrite this note if Wilson adopts Pollard's *[non sunt?]*. The English sentence affected is "three kinds of men … are fit to argue in this matter".
- `chunks/dialogus/wyc-dialogus-26.md`, n11 (LD-09): the English sentence changes if Wilson emends to *non prediligit*.
- `chunks/dialogus/LATIN-DOUBTS.md`: mark rows LD-01, 03–06, 08, 10, 12–16, 18 and 21–28 closed, "plate 2026-09-29". LD-02, 07, 09, 11, 17 and 19 wait for a ruling. LD-20 stays open (source).
