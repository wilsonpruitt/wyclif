# M5 RESUME — *De ecclesia* (the first volume after the Dialogus)

*Read this first in a new session, then `WORKFLOW.md` (the stages) and `PLAN.md` § Cost. Written 2026-09-29
at the end of the M3/M4 session.*

## Status 2026-10-02 — brief 31 (16-a, 16-b, 16-c) DONE — HANDOFF to a fresh session
- Opus 143K; Sonnet plates + sources 130K. **Lost words:** *sua,* and *, 34,* at 360.13–14 (*sufficit diei
  malicia sua, Matthei VI°, 34,*); English now "its own evil". 16 tokenfixes (glued words, alinea B, folio
  mark 180a inside *inor-|dinate*, stray *us*, punctuation).
- Print confirmed, no departure: 362.20 *cum approbabili:* (no noun; "[argument]" supplied), 362.30 no verb,
  *Jeronynum*, *asumptum*, *sucessionem*, 368.13 *in reduplicacionem*. Print spells *Bolonie* (366.17).
- Sources: D.95 c.5 *Olim* = Jerome on Titus (Friedberg); *De doctr. christ.* 2.42.63 is a paraphrase (cf.);
  Ep. 82 probable by content; Jerome Ep. 52.5; Nicholas = Aug. *De haer.* 5. Open: E16a-4, E16c-3, E16c-7.
- GLOSSARY: *elemosinatus* = "almsman" (09-28 row governs; row 362's "one given alms" conformed).
- Session total for briefs 29–31 ≈ 860K tokens (Opus ~140–160K + Sonnet ~130–150K per brief).

### Per-brief loop (a fresh session starts HERE)
1. **Opus agent** (background): "Read chunks/ecclesia/_briefs/<brief>.md and follow it exactly … Standing rules
   … do not commit … give each scar token exactly as it appears including attached punctuation."
2. **Process its report:** look each scar up in `text/ecclesia/pNNN.tok.jsonl` (python, by token text, with
   neighbours and count) → rows in `text/ecclesia/tokenfix.tsv` (`page⇥token⇥fix⇥reason`; empty fix = delete;
   hyphen split = first half → whole word, second half → empty). Apply only clear ones; leave doubtful
   spellings for the plate check. Run `.venv/bin/python scripts/w3/vote.py ecclesia` and grep `pNNN.la.txt` to
   confirm each took. LEDGER rows (`| E16d-1 | ecclesia-16-d / n3 | claim | status | how |`) and GLOSSARY rows
   (append at file end; grep first for clashes, the earlier frozen row wins) appended.
3. **Sonnet agent** from `chunks/ecclesia/_briefs/CHECK-TEMPLATE.md` (fill: pages, already-fixed list, the
   Opus Latin doubts as plate items, `to-verify` rows as source items). Friedberg OCR may still be in the old
   session scratchpad; otherwise it re-fetches.
4. **Apply:** tokenfix rows → English + note fixes (python exact-string replace, assert count 1) → LEDGER
   statuses → `vote.py ecclesia` → `relatin.py ecclesia --also 16-d,16-e,16-f` → `relatin.py ecclesia --dry`
   (0) → `lint.py chunks/ecclesia/wyc-*.md` (0) → **grep the chunks for every old token (must be 0)** →
   M5-RESUME entry → `brief.py ecclesia <next three ids>` → commit (local main; no push).
- ⚠ Traps (all bit this session): token keys include attached punctuation; `--also` takes ids, not paths
  (paths silently do nothing); **pair keys match RAW tokens before unstar()** (`XXIII*,`); single-token
  keys are matched after unstar. Run scripts with `.venv/bin/python` (vote.py needs spylls).
- Common plate finds worth listing every time: ª/º lost after roman numerals, words lost at line ends
  (349 *a*, 360 *sua,*), alinea letters glued or stray, folio marks inside hyphenated words.

- **Next:** brief 32 = 16-d, 16-e, 16-f. Built: `chunks/ecclesia/_briefs/ecclesia-16-d-16-f.md`. Then 16-g, 16-h
  (+17-a) finish chapter 16.
- **Still owed:** the lost-word pass over chapters 1–13 (computation first, `scripts/w3/lost.py` prototype)
  before the site build. Open questions for Wilson: the two print departures (346.22 *nos*; 356.13 B no *si*).

## Status 2026-10-02 — brief 30 (15-f, 15-g, 15-h) DONE: chapter 15 translated
- Opus 134K; Sonnet plates + sources 142K. **One lost word:** *a* at a line end, 349.20 (*racio a similitudine*).
  16 tokenfixes: 4 hyphen/truncation, 3 alinea letters, lost ª/º after numerals (349.14, 352.28, 356.32),
  *deliquent* → *deliquerit* (355.27, plate). *ecclesiasticie* (349) is the PRINT's misprint, fixed by ruling 2.
- Departure: 356.13 B's reading (no *si*) translated, T note. 352.23 *papa* (dative) and 358.14 *extere* are print.
- Sources: 15-f n3 corrected (Loserth's foot-note 13 IS *De Liguribus*; *Si papa* is ours); 15-g n17 *Due sunt* =
  Gratian's dictum after C.23 q.4 c.23 (Boethius); Ambrose "Ep. 38" doesn't match Maurist Ep. 38 (Ep. 21 §25 closest).
- ⚠ **Pair keys match the RAW pivot tokens, before unstar():** *XXIII,* was raw `XXIII*,`, so the key is
  `faceret, XXIII*,`. If a fix doesn't take, print the raw pair in vote.py's pair loop (temporary debug line).
- **Next:** brief 31 = 16-a, 16-b, 16-c. Built: `chunks/ecclesia/_briefs/ecclesia-16-a-16-c.md`. Loop: brief 28 entry.

## Status 2026-10-02 — brief 29 (15-c, 15-d, 15-e) DONE
- Opus 161K; Sonnet plates + sources 152K. Full plate pass pp. 336–348: **no lost or doubled words**; 9 tokenfixes
  (incl. *no* = line number 20 at 338.20; *Privilegium:* incipit at 341.23; *XXXVIIª* at 347.10).
- Departure from the print (ruling 2): 346.22 *Quis non* → *nos* (Augustine Ep. 93 = C.5 q.5 c.2 both read
  *nos*; no apparatus). The other flagged non-constructions (336.21, 343.22–27, 345.31, 346.6) are the print.
- Sources: 15-d n5 is Gregory to Brunhild, NOT D.86 c.3 (John VIII); C.11 q.3 c.63 and C.23 q.4 c.37/24/23
  verified; the *eius est interpretari* maxim rooted in Cod. 1.14.12 and C.25 q.1 §2. Still open: E15c-2, E15c-4,
  E15d-3, E15e-1/2/4/5/6/13.
- ⚠ **tokenfix keys include attached punctuation** (*jnvitis,* not *jnvitis*): a bare key silently doesn't
  apply. Check by grepping the chunks for the old token after the pipeline.
- **relatin `--also` takes chunk ids, comma-separated** (`--also 15-c,15-d,15-e`), not paths. Paths silently
  refresh nothing. `vote.py` needs `.venv/bin/python` (spylls).
- **Next:** brief 30 = 15-f, 15-g, 15-h. Built: `chunks/ecclesia/_briefs/ecclesia-15-f-15-h.md`.
  Per-brief loop: see brief 28 entry below (unchanged). The lost-word pass for chs. 1–13 is still owed.

## Status 2026-10-02 — brief 28 (14-h, 15-a, 15-b) DONE: chapter 14 translated
- Opus 158K; Sonnet plates + sources + page-head sweep 139K. Lost/doubled words: *II.* (332.10), *Tercia* doubled
  (333.1); departures by ruling 2 (print won't construe): 328.12 *Vident* (B), 331.33 *nimis*. 330.30 paragraph
  break is spurious but left as structure (PLATE-FLAGS).
- **Page-head sweep resolved:** of 7 candidates only p. 431 *Non* is real; p. 21 *illo* (mid-line) found on the way.
- **vote.py tokenfix bug fixed:** a fix whose result contains the printed word was re-applied word by word
  (*debui* → *Non Non debui*); it had already doubled *Si* at 244.30 in translated chunk 11-d. Fixes now chain
  (XXXVII → XXXVIIª → XXXVIIª,) but never re-apply; whole-volume diff changed only pp. 244, 332, 431.
- Verified: D.83 c.3; Bernard *De consid.* II.6.10; D.40 c.12 (*Opus imperf.* hom. 43); C.23 q.4 c.22.
- **Owed:** mid-line lost words (21 *illo*, 332 *II.*) are found only by a word-by-word plate comparison, which
  briefs before 26 did not get: chapters 1–13 likely hold some. Plan a lost-word pass (computation first:
  scratchpad lost.py prototype, untested) before the site build.
- **Next:** brief 29 = 15-c, 15-d, 15-e. Built: `chunks/ecclesia/_briefs/ecclesia-15-c-15-e.md`.
- **Per-brief loop (a fresh session starts here):** (1) one Opus agent: "Read <brief> and follow it exactly …
  pay attention to its Standing rules"; (2) process its report: scar tokens → tokenfix, LEDGER rows, GLOSSARY
  rows (append at file end, §D), normalise anything off-format; (3) one Sonnet agent from
  `chunks/ecclesia/_briefs/CHECK-TEMPLATE.md`; (4) apply, run the pipeline, commit (template's last section).
  Then `brief.py ecclesia` for the next three chunks. Measured ~300K tokens per brief, both agents.
- Sweep scripts now in the repo: `scripts/w3/heads.py` (page heads, noisy), `scripts/w3/lost.py` (prototype).

## Status 2026-10-02 — brief 27 (14-e, 14-f, 14-g) DONE
- Opus 158K; Sonnet plates + sources 146K. **Two more lost words:** *in* at the head of p. 317 and *sed non
  assero.* at 318.3 (Henry's hedge on the Constantine poison story) — restored, English and n17 fixed. All other
  flagged gaps (315.7–8, 318.22–24, 320.1, 325.9–10) are the print. 16 tokenfixes.
- GLOSSARY clash fixed: *locus a simili* = "the topic from likeness" (frozen 09-28 row wins over my 10-02 row);
  09-d, 14-f conformed. New rows: *ritus*, *civilitas*, *ydiota*, *catholicare/hereticare*.
- Verified: *De doctr. christ.* II.42.63; Bernard *De consid.* II.6.10–11; Hugh *De sacr.* II.2.3/4/7; D.96 c.14.
  The *venenum* legend is not in the PL.
- **Page-head sweep (scratchpad heads.py; witnesses' word just before each page's first words):** candidate
  lost words at the heads of pp. 21, 184, 341, 342, 393, 431 (*Ni88biVo7z* before *debui*), 497 (*pena*?).
  Most are probably apparatus/running-head noise; read them on the plates with brief 28's check. Cause to
  examine: vote.py `align_page` deletes insertions at gap 0 as window slack, so a pivot-lost page-head word
  can never be voted in.
- **Next:** brief 28 = 14-h, 15-a, 15-b.

## Status 2026-10-02 — brief 26 (14-b, 14-c, 14-d) DONE
- Opus 157K; Sonnet plates + sources 151K. First brief built with the standing rules in brief.py: note format
  came back clean. No lost words on 302–315 (every line-end hyphen and page edge checked); the suspected gaps
  (309.8–17, 314.24–27) and the doubled *Augustinus recitat super Joh.* (314.16–18) are the print.
- **vote.py GLUE2 rule:** *consumeret* (291.25) was lost because the pivot glued *qui.consumeret* and the
  scans, which split it, out-voted it with *qui* alone. The rule keeps the glued second word; run over the
  whole volume it fires once (291.25), so the mechanism was a one-off. Its tokenfix row is retired.
- Ruling 2 applied: 302.27 punctuation and 304.19 *mala oblata* stand in the Latin; notes give the sense.
- Verified: Aug. Ep. 153.20, .21, .26; Gregory *Mor.* XXIII.1.2 (Wyclif XXXIII); C.12 q.1 c.5; Bernard
  *De consid.* IV.3.7; Aug. *In Ioh.* 5.7–11. *De doctr. christ.* IV untraced. 22 tokenfixes.
  GLOSSARY: *nolicio*, *dispensator*, *clericatus*, *in capite*.
- **Next:** brief 27 = 14-e, 14-f, 14-g (14-h with 15-a after).

## Status 2026-10-02 — brief 25 (13-e, 13-f, 14-a) DONE: chapter 13 translated
- Opus 149K; Sonnet plates + sources 136K. **Lost word again:** *consumeret* (291.25, hyphenated *con-|sumeret*
  across a line) — restored by tokenfix pair. Line-end hyphens are a third loss mechanism (after page heads and
  dittography); a sweep for relative/subordinate clauses lacking a verb would catch more. The other flagged
  gaps (297.3, 298.19) are the print. *penun* = *periuri* (plate).
- The agent wrote bare note codes (`S `, `T ` mid-note): normalised to `**S/T.**` by script. brief.py now
  carries the standing rules (no source search, house note format, scars to the report only, lost-word flags).
- Verified: D.8 c.1 and Aug. *Tr. in Ioh.* 6.25 read *recitemus* (print *reticeamus*, kept); Bede *In Luc.* III
  (Wyclif: II) borrowing Jerome *In Matth.* I; *ius poli* = Aug. *Sermo* 355; C.23 q.4 c.24, C.24 q.3 c.25.
  12 tokenfixes. GLOSSARY: *elemosinator*, *elemosinacio*, *ius poli / ius fori*, *mundialis*.
- **Next:** brief 26 = 14-b, 14-c, 14-d.

## Status 2026-10-02 — brief 24 (13-b, 13-c, 13-d) DONE
- Opus 168K; Sonnet plates + sources 123K. **Lost word again:** *Et* at 281.1 (page head) — restored by tokenfix pair.
  The four flagged suspects were the print: *ditarius*; *tenentur* (281.21, translated from A A₁); *maior* twice
  (288.9–10); 290.4–6 has no main verb (Loserth's own anacoluthon, "[gave theirs]" supplied). 281.18 *ad
  continuandum*: the print, translated "discontinue" after Loserth's *discontinuandum (?)*, noted.
- Verified: Aug. *En. in Ps.* 148.2 (PL 37.1938, free quotation); *par in parem* = X 1.6.20, Clem. 5.11.1.
  14 tokenfixes. GLOSSARY: *ecclesia cesarea*, *elemosina cartalis*, *ditarius*, *pseudomonachus*.
- **Next:** brief 25 = 13-e, 13-f, 14-a.

## Status 2026-10-02 — brief 23 (12-e, 12-f, 13-a) DONE: chapter 12 translated
- Opus 176K; Sonnet plates + Friedberg 88K. No lost words (asked to flag). Plates: *perturbacio* doubled in our Latin
  (dittography) — fixed; *celeberrime* is the print and a Friedberg variant. *Nisi bella* (Gratian "Gregorius") is
  Origen. 10 tokenfixes. GLOSSARY: *vicarius Christi* (row at last), *elemosinans*, *elemosina temporalis/perpetua*,
  *autenticus*, *manucapcio*, *satispassio*, *compossibilis*, *distribucio accomoda*.
- **Next:** brief 24 = 13-b, 13-c, 13-d.

## Status 2026-10-02 — brief 22 (12-b, 12-c, 12-d) DONE
- Opus 177K; Sonnet plates + sources 106K. **Dropped words again:** 258.2 *carte impossibile* lost from the Latin
  (the agent had supplied a negative); restored, English fixed. *Ad* (258.23) restored. *ociosis*, *oblata*,
  *promittendum* are the print.
- *regnum* ruling (Wilson: "kingdom", never "realm") enforced: 8 English lines in 08-a, 11-a–d, 12-a fixed.
- Verified: *Sext* reg. 27; *De vera rel.* 14.27; Anselm CDH I.21; C.23 q.4 c.22 (pseudo-Aug.), c.33 (= Ambrose
  *In Ps. 118*). 15 tokenfixes. GLOSSARY: *subintelligere*, *privilegiandus*, *pietas*, *irreligiositas*.
- **Next:** brief 23 = 12-e, 12-f, 13-a … .

## Status 2026-10-02 — brief 21 (11-d, 11-e, 12-a) DONE: chapter 11 translated
- Opus 147K; Sonnet plates + sources 119K. **PLATE-FLAGS p. 245 closed:** the print has *coronarius*; *Si* (244.30)
  restored. *propriatorie*, *abicio oblati* are the print (notes stand).
- vote.py: tokenfix now also applies word by word inside a token covering two printed words (*pociora, sicutaperiens*
  had dodged it since the scar pass).
- Verified in Friedberg: C.11 q.3 c.100 (both "fathers" inside it), C.19 q.2 c.2, C.22 q.5 c.20, C.16 q.1 c.68,
  C.11 q.3 c.55 (*Inter verba* = incipit); Gregory's saying is Gratian's dictum. Isidore *Sent.* III.42.
- **Next:** brief 22 = 12-b, 12-c, 12-d.

## Status 2026-10-02 — brief 20 (11-a, 11-b, 11-c) DONE
- Opus 176K; Sonnet sources 185K (14 canons in Friedberg). Finds: Wyclif's "C.25 q.1 c.16" text is Gratian's
  dictum; 11-c C.23 q.4 c.52 *non* = the pre-Correctores reading; C.5 q.5 and C.23 now in the English (modern refs).
  *debitori* (231.11) translated "[their creditor]". GLOSSARY: *suffragari* "to aid" (non-prayer), *franchisia*,
  *facinus*, *irreatus*. 7 tokenfixes.
- **Next:** brief 21 = 11-d, 11-e … .

## Status 2026-10-02 — brief 19 (10-d, 10-e, 10-f) DONE: chapter 10 translated
- Opus 157K; Sonnet sources 86K: C.17 q.4 c.9, D.38 c.10, *X* 5.12.1, and the maxim *frustra legis auxilium* =
  *X* 3.49.10 (closes E07c-2 too). Plate: *sedacionem* print. 7 tokenfixes.
- GLOSSARY: *sentencia* CONTEXTUAL (teaching / judicial sentence, C note); *limitare* "limit" where it restricts.
- **Next:** brief 20 = 11-a, 11-b … .

## Status 2026-10-02 — brief 18 (10-a, 10-b, 10-c) DONE
- Opus 185K; Sonnet plates + sources 110K. *Excommunicatorum* = C.23 q.5 c.47; *De serm. Dom.* II.8.28 (Wyclif "c. 10").
  Plates: *apostoliter*, *caritatem ignoscere* print; *a terrenis* (OCR *o*) fixed. 9 tokenfixes.
  GLOSSARY: *membrum*, *perquisitum*, *contribules*. Open: Nicholas II or III (Westminster bull; Kemble not local).
- **Next:** brief 19 = 10-d, 10-e, 10-f.

## ⚠ GLOSSARY tidy owed
Rows the coordinator added 2026-10-01/02 by script sit at the END of the section BEFORE the intended one (the
script inserted above the target heading). Harmless (lint and tags go by key), but move them one section down in a
tidy pass; from brief 18 on rows are inserted above the NEXT section's heading.

## Status 2026-10-02 — brief 17 (09-d, 09-e, 09-f) DONE: chapter 9 translated
- Opus 165K; Sonnet sources 96K. Loserth's c.15 clash settled: Augustine *Quantus arrogancie tumor* = C.23 q.4
  **c.14** (*De bapt.* IV.12 quoting Cyprian); c.15 is Gregory. *Omnis iniquus bonorum est inimicus* = Gratian's own
  dictum. 18 tokenfixes (verse numbers the OCR misread). GLOSSARY: *mortificacio privilegii*, *iugum*, *ociatores*.
- **Next:** brief 18 = 10-a … .

## Status 2026-10-02 — brief 16 (09-a, 09-b, 09-c) DONE
- Opus 164K; Sonnet sources 117K (Friedberg I/II: *Pudenda*, *Non mediocriter*, *Te quidem*, Leo epp. 51/52,
  *Relatum*). **Construal fixed:** 09-a C.24 q.1 c.33 — Wyclif truncates the canon; *excludi non possit* describes
  the malice; verb "extinguish" supplied from the canon (C note).
- GLOSSARY: *privilegium* (key term), *exempcio*, *furce et puteus*, *expropriacio* "renunciation of property",
  *laureola* "aureole", *uxoratus* "married", *philargiria*, *mundialitas/secularitas* … 9 tokenfixes.
- **Next:** brief 17 = 09-d, 09-e, 09-f.

## Status 2026-10-02 — brief 15 (08-d, 08-e, 08-f) DONE: chapter 8 translated
- Opus 175K; Sonnet sources 98K. Lower-case margin letters (a–f) glue onto words from ~p. 170: a rule would hit
  genuine medieval forms (*Isaie*, *regalie*, *abbathie*), so 30 curated tokenfixes instead (incl. pp. 186–581, two
  of them the preposition *a*: *a iurisdiccione*, *clericorum a laycis*).
- Open crux: 182.4 *ciresorum* (print confirmed, apparatus silent): untranslated in brackets; conjectures
  *cesareorum* / *cirographorum* in the note. Untraced: the "fourth letter to Volusianus"; *honor fugientem*.
- GLOSSARY: *minoritas*, *insolubilia*, *exproprietarie*, *globus* (things) "mass", *habitudo ad*.
- **Next:** brief 16 = 09-a … .

## Status 2026-10-02 — brief 14 (08-a, 08-b, 08-c) DONE
- Opus 146K (told to keep OCR scars out of the chunks: no cleanup needed); Sonnet plates + sources 107K.
- The midwives' lie verified throughout (Aug. *Enarr.* 5, *Contra mend.*, *Quaest. in Hept.*; Comestor *De dolo*;
  Gregory *Mor.* XVIII.3). Plates: *tertii*, *cateclismus* print; *proficiencium* (OCR) fixed. 7 tokenfixes.
- GLOSSARY: *orator* CONTEXTUAL (bedesman / advocate), *allegare* "allege" (= cite), *indoles* "promise",
  *colorare*.
- **Next:** brief 15 = 08-d, 08-e (+ 08-f?).

## Status 2026-10-02 — brief 13 (07-b … 07-e) DONE: chapter 7 translated (MS D)
- Opus 159K; Sonnet sources 89K. Verified: Aug. *Ep.* 153.20; *Serm.* 9.3, 251.8; *X* 3.40.10 (pollution);
  Isidore *Etym.* V.18 = D.3 c.3; C.11 q.3 c.63; D.86 c.3. 07-d n5 had misread a hypothetical (spittle) — fixed;
  the English was right.
- Side-notes: "Jaw" → "law" (32.18, 146.1, 147.1) in sidenotes.fixed.tsv and the chunks. 10 tokenfixes (pairs for
  line-divided words). GLOSSARY: *regalia*, *forisfacere*, *ecclesia laycalis*, *suffragium* (law) "aid",
  *ingratitudo*; *instancia* also "urgency".
- **Next:** brief 14 = 08-a … .

## Status 2026-10-02 — brief 12 (06-f, 06-g, 07-a) DONE: chapter 6 translated
- Opus 166K; Sonnet sources 114K (Friedberg I + II now reachable; C.23 q.4 cc.11/15/23 re-checked there).
- Printed misnumbered references (Eph. "V°, 27", "XXXIIIª") now given in modern form in the English, the printed
  figure in the Transcription notes (card: modern references in the English).
- *leges patrie* kept "laws of the homeland" + note, per the Dialogus *via / patria* ruling (Wilson may want an
  exception for the legal idiom "laws of the land").
- Sanctuary: *X* 3.49.6, 3.49.10 give three excluded classes; Wyclif's "four" not found. 10 tokenfixes.
  GLOSSARY: *locus a maiori*, *ficticia*, *inobedienciarius*, *gracia preveniens* …
- **Next:** brief 13 = 07-b … (chapter 7, MS D).

## Status 2026-10-02 — brief 11 (06-c, 06-d, 06-e) DONE
- Opus 171K; Sonnet plates + verifier 107K. 131.12 *debitor* (Loserth's own suggestion) accepted over the print
  *creditor*, which gives no sense (ruling 2). Plates: *Paulum*, *aliquam*, *creditor* are the print.
- Verified: *De Gen. ad litt.* X.19.34; *De vita christiana* (pseudo-Aug., PL 40); D.40 c.2 (Jerome); C.27 q.1
  c.41 = *De bono viduitatis* 10.13. Open: Anselm wording (not in *De conc. virg.* 11), the Jerome letter.
- 11 tokenfixes; drift 0 over 38 chunks. GLOSSARY: *distrahens* "diminishing qualifier", *tyriaca* "theriac".
- **Next:** brief 12 = 06-f, 06-g, 07-a.

## Status 2026-10-02 — brief 10 (05-f, 06-a, 06-b) DONE: chapter 5 translated
- Opus 159K; Sonnet plates + Gratian 78K. **archive.org back:** Friedberg I (BD1141951) read — D.21 c.3 reads
  *nullis sinodicis constitutis*, no *multis* in the apparatus (coordinator re-read). E04e-4 closed.
- Plates: *VIIIⁱ* (raised ordinal), 2 Cor. 6:**15** (old-style figures). *De cons.* D.2 c.63 incipit is Wyclif's
  *Hoc sacramentum*. 10 tokenfixes; drift 0 over 35 chunks. GLOSSARY: *de virtute sermonis*, *capitari/capitatus*.
- Owed to Friedberg now that it is up: C.23 q.4 cc.11/15/23 (E04f-1/4, Migne only), *Damnamus* (E06a-2, Friedberg II).
- **Next:** brief 11 = 06-c … .

## Status 2026-10-02 — brief 9 (05-c, 05-d, 05-e) DONE
- Opus 166K; Sonnet plates + verifier 103K. archive.org still offline (Friedberg I owed).
- tokenfix now takes TWO-token entries ("nec essitate" → necessitate) for a split whose first half recurs on the
  page. Plates: *caritatis*, *discontinuacio* (OCR), *personaliter* (print). Bernard's eight unities verified
  (*De consid.* V.8.18); *unitas principalis* = *Serm. de div.* 80. Drift 0 over 32 chunks.
- GLOSSARY: *conclusio*, *terminus communis* "common term".
- **Next:** brief 10 = 05-f, 06-a, … .

## Status 2026-10-02 (end) — brief 8 (04-f, 05-a, 05-b) DONE: chapter 4 translated
- Opus 182K; Sonnet plates + verifier 132K. archive.org still offline: Gratian in Migne only (Friedberg I owed for
  D.21 c.3, C.23 q.4 cc.11/15/23). *Recurrat*'s *caro est caro est* is Augustine's *De baptismo* I.17.26.
- Plates: *iusticium*, *amare* are the print; *unio,*, *iudicio* (OCR losses) fixed. 16 tokenfixes. Drift 0 over
  29 chunks. GLOSSARY: *iuvencula* "young girl" vs *adolescentula* "young maiden" (02-d, 05-a aligned),
  *prepositura*, *filii imitacionis*, *suffragium sensus*, *dyameter/costa*, *dulia/latria*.
- **Next:** brief 9 = 05-c, 05-d, … .

## Status 2026-10-02 (later still) — brief 7 (04-c, 04-d, 04-e) DONE
- Opus 158K; Sonnet plates + verifier 163K. archive.org was DOWN (503): canon-law rows verified in Migne's Gratian
  (PL 187), not Friedberg — re-check D.21 c.3 in Friedberg I when archive.org is back (E04e-4).
- D.21 c.3 *Quamvis*: Gratian/Gelasian decree/Ivo all read *nullis synodicis constitutis*; Wyclif *multis*; nearest
  attested *nonnullis* (PL 13:374B). The note states the facts; it no longer says Wyclif "inverts" the canon.
- Plates: *fuit*, *prius*, *loquuntur* (OCR errors, fixed); *domus*, *non*, *filius*, *papa*, *fluent* are the print.
- vote.py: tokenfix now also applied after scar_fix (*impossibile®* → ° had dodged it). 15 tokenfixes. Drift 0
  over 26 chunks. GLOSSARY: *ecclesiastici* CONTEXTUAL (clergy / those of the church), *placitare*, *penaliter*,
  *participium*.
- **Next:** brief 8 = 04-f, 05-a … .

## Status 2026-10-02 (late) — brief 6 (03-f, 03-g, 04-a, 04-b) DONE: chapter 3 translated
- Opus 167K (told not to search the PL: 16 tool calls); Sonnet plates + verifier 153K (8 rows verified).
- Under the "print governs" ruling the print is kept where a source differs, with the source in the note:
  *seculum* (Aug. *oscula*), *audeat* (Bernard *minime audet*), *non potuit* (Aug. *potuit … et noluit*),
  *conformiter* (MSS and Richard *conformitatis*). Faustinus is Augustine's, not a slip.
- tokenfix: 12 more; drift 0 over 23 translated chunks. GLOSSARY: *habitudo*, *humidum radicale*,
  *concorporacio*, *capitaliter*.
- **Next:** brief 7 = 04-c … (chapter 4).

## Status 2026-10-02 (night) — brief 5 (03-b–03-e) DONE
- Opus brief 205K (the costliest yet: 3,000 words, 26 tool calls); Sonnet verifier 114K, first run with
  Friedberg's *CIC* II (archive.org BD1141952, `_djvu.txt`): all *Unam sanctam* rows verified (II, 1245–46);
  *A nobis* is *X* 5.39.28, not Loserth's 5.39.21 (coordinator re-read).
- Alinea letters L, M added to the rule (15 sites); tokenfix: *verius*, *salvator*, stray points, side-note *the*.
  20 Latin changes, drift 0 over 19 translated chunks.
- GLOSSARY: *caput* row (head), *speculator* watchman, *fucus* disguise, *glosa*, *vocatus* so-called,
  *libertas arbitrii*, *digestio*.
- **Next:** brief 6 = 03-f, 03-g, 04-a, 04-b.

## Rulings 2026-10-02 (Wilson: "recommendations yes") — logged in CONVENTIONS, card updated
*color* → "colour" (C note per chunk); **Loserth's printed text governs** (A₁ never alone; 02-c 34.20, 02-d 38.1
returned to the print); our emendations stand; Clement 37.21 open; verifier MAY fetch Friedberg's *CIC* from
archive.org for *Unam sanctam* rows (do it in the next verifier run: E01c-5, E01e-1, E01g-4, E02a-2 …);
delegated glossary rulings confirmed; "now" rule confirmed; vote.py stops trusting `agreed.txt` from
*De officio regis* on (not this volume).

## Status 2026-10-02 (evening) — brief 4 (02-e, 02-f, 03-a) DONE: chapter 2 translated
- Opus brief 150K; one Sonnet agent (112K) read 4 plate words AND verified 6 rows in the local PL (combine the
  two jobs from now on). Jerome on Micah: Loserth's 1281 = 1221; *dicamus scriptum* is Jerome's. *Moralia* XXXI
  = PL 76:583D–585C. *austerna* (49.18) is printed and is Wyclif's own paraphrase: *austrina* kept as our
  emendation (T note). *speculo*, *meriti* are the print (OCR had *specu*, *menti*).
- tokenfix: 10 more (alinea L, M; *sumiter*, *hn*, *chnsticolis*, side-note *of*). Drift 0 over 15 chunks.
- GLOSSARY: *confuse/confusus* "indistinct" (never "confused"), *obedienciarius*, *elemosinarius*, *viacio*,
  *citra Christum*.
- **Next:** brief 5 = 03-b … (chapter 3).

## Status 2026-10-02 (later) — brief 3 (02-a–02-d) DONE
- Opus brief 170K. Ledger: E02b-1 = E01h-4 (verified); E02d-1 verified by the coordinator (Aug. *Serm.* 292.6,
  PL 38:1323); the rest are *Unam sanctam*/tradition rows (not local) or editor.
- New leak class: Loserth's PAGE FOOT read into the Latin as paragraphs (p. 33 apparatus + English note on
  Celestine V; p. 160 apparatus). vote.py now drops a paragraph that opens with a line number and carries
  apparatus marks or English (only these 3 in the volume). 02-c rebuilt to its true paragraphs (notes renumbered);
  drafts 08-a/08-b given the fresh paragraphs, their side-notes kept.
- tokenfix.tsv: 02-a/02-b scars (glued alinea letters a/b, *opmcis*, side-note "a."). Drift check over all 12
  translated chunks: 0. bible.py: Sap/Wis/Act aliases.
- GLOSSARY ruled: *aggregative*, *de inesse*, *sillogismus expositorius*, *influxus/influere* (not "influence"),
  *universitas fidelium*, *necessitas ex supposicione*.
- Open: Clement at 37.21 (V or VII?) left open in the note; *color* ruling still with Wilson.
- **Next:** brief 4 = 02-e, 02-f (finishes chapter 2), perhaps with 03-a.

## Status 2026-10-02 — brief 2 (01-e–01-h) DONE: chapter 1 translated
- Opus brief 164K; Sonnet ledger verifier 116K (11 rows read in local PL; Wyclif's own *Moralia* refs often wrong:
  XXVIII.11 is XVIII.35.56; XIX.9/IV.9 untraced). Notes corrected.
- The agent found scars the first sweep missed: `scars.py` skipped every non-letter token (folio/margin numerals
  glued into words, `j` for `i`, stray marks). Second sweep: vote.py `scar_fix` extended; NEW
  `text/ecclesia/tokenfix.tsv` (page, printed, fixed): one-off fixes applied by the vote's writer, no position
  needed; scan-confirmed glued words (*caputvel*) added there. Rules that misfired and were fixed: split on a
  stray capital (*inVocare*) now needs the joined form to be a non-word; digit-strip needs >= 3 letters left.
- Chapter 1 (01-a–01-h) Latin now equals the established text (`relatin.py --also … --dry` shows 0 drift).
- GLOSSARY ruled: *capitaneus* captain, *matrix ecclesia* mother church (C note), *capitas* headship,
  *obicitur per*. **For Wilson:** *color* (*non est color*) — "colour" (plausible ground), or another word?
- Residue in the Latin: ~30 LEFT-odd tokens the rules cannot settle (`scars.tsv`); 20.4 *Per*, 20.7 *regina Sed*.
- **Next:** brief 3 (02-a …).

## Status 2026-10-01 (night) — Latin scar pass DONE (WORKFLOW 4b)
- Root cause: vote.py's Lexicon trusts `agreed.txt`, which holds shared garbles (*omcio*, *lhnsti*). Not
  changed for *De ecclesia* (it would reshuffle settled votes); fix it before the next volume.
- New: `scars.py`, `scarqueue.py`, `relatin.py`, `pl_lexicon.py` (402K PL forms, gitignored, rebuild with one
  command), vote.py `scar_fix` + alinea pre-pass, crops.py `--queue/--out`, `catalog/lexicon/ocr_artifacts.tsv`
  (109 confirmed garble→print pairs, for the next volumes).
- Result: 326 word-level changes to the established Latin (all ≤3 words; *ecclesiasticus* 14.5 and *attendimus*
  514/515 restored). Decisions applied 2,436, stale 0. 134 draft chunks' Latin refreshed; 01-a–01-d untouched.
  Cost: 2 Sonnet plate agents, 224K.
- Residue (not fixed): p. 410 *two* (English, an inserted token: no position); `evenietjs` 194.1; word-split
  rule unreliable (most "splits" are hyphenated words) — plates only.
- **Next:** brief 2 (01-e … 01-h or similar).

## Status 2026-10-01 (evening) — brief 01-b–01-d DONE; Latin clean-up DONE (see above)
- Brief 01-b/c/d: one Opus agent, **164K** (on estimate); lint clean. Ledger: Sonnet verifier (135K) read
  14 rows in the local PL; all verified except E01c-7 (Amalarius), E01c-5 (*Unam sanctam*, not local), E01c-6
  (Aristotle), E01d-6. E01d-1 corrected: *De corr. Donat.* (Ep. 185) 9.42, not Ep. 93 (coordinator re-read).
- GLOSSARY ruled: *viantes* "those on the road", *plenitudo potestatis*, *bigamia* (C note), *formido* "misgiving".
- ⚠ **The frozen Latin is not clean.** In these 3 chunks: 15 OCR scars corrected in the chunk Latin against
  the plates (14.5 *ecclesiasticus* LOST at the break *qui-|bus*; side-note English *like* in the Latin;
  `.'` for `?`; alinea letters; `3o`/`3i`; `%`; `■`). NOT yet propagated to `text/ecclesia/pNNN.la.txt`.
  Volume-wide: ~200 character scars in the scaffold Latin, and `nonwords.tsv` singletons (1,644) are ~20%
  garbles (*Lhnsti*, *omcio* p. 450) that the suspect filter never sent to the plates ≈ 400 more.
  **Wilson to decide:** one Latin clean-up pass (~600 items, ≈ 1.1M at the plate-pass rate) before the next
  brief, vs. per-wave plate checks (≈ 15 crops per brief, coordinator).
- Not done mechanically: the *sed/autem* check (agent's own report only).

## Status 2026-10-01 (later) — 01-a REVIEWED
- Fixed in 01-a: 1.17 *Illos autem* back to "Now" (the pilot's; 1.19 stays "And"); *suffragium* "aid"
  (pilot), untagged: the *suffragia* row is the church's shared-out prayers, not a parent's help;
  2.15 maxim de-quoted (n9 says it is not a quotation); n7 Rufinus verified, §36 not 37 (V-05);
  n8 adds the *contra hereticos* construal; n13 says XLVI (plate-checked) ≠ modern 56.
  n2 plate-checked: print as scaffold, note stands. Card: plate path (`n0038.jpg`), "now" rule clarified.
- Open: side-note 1.2 runs two notes together ("…faithful How it may be known."); density 13 notes /
  477 words (card: 1 per 70–100); GLOSSARY proposal *suffragium* (a person's help) "aid", §D.
- **Next:** commit; then briefs of 3–5 chunks from 01-b.

## Status 2026-10-01 — side-note pass DONE (stage 5b)
- Method changed from "one plate agent per ~10 chapters": the margin column cut alone is clean modern
  type, so `sideocr.py` re-OCRs every note with tesseract (free) and places it at page.line;
  `sidesheets.py` cuts plate sheets only for notes a marker fires on (non-word, conf < 70, glyph,
  short) + `missed` places; `sidesplice.py` merges the reads and writes every scaffold's section.
  Control (`--spot 40`): 16/16 unflagged notes exact, line included.
- 1,383 re-OCR'd → 524 bands / 136 sheets → 4 **Sonnet** agents (`sidenotes.reads.part01–04.tsv`) +
  coordinator `part99` (α/β at 491.28/492.11, joins at 155.6, 417.24, 542.29). Result:
  **1,293 notes, 407 read on the plate**, in `text/ecclesia/sidenotes.fixed.tsv`; lint clean.
- **Cost: ≈ 0.55M** (127–145K per agent) against the 1M estimate.
- ⚠ Note ids in the reads are row numbers of `sidenotes.ocr.tsv`: never re-run `sideocr.py` without
  re-reading. Known residual class: a note tesseract split at a gap with no marker on either half
  (3 found by the lower-case-continuation check, fixed in part99).
- **Card done (2026-10-01):** `chunks/ecclesia/CARD.md`. Disputation formulae (*instatur* / *obicitur*
  "it is objected", *dicitur* "it is said" / "the answer is", *respondetur* "the reply is") are ruled
  into GLOSSARY §C (Wilson, 2026-10-01). 01-a/01-b start from the pilot's English (GLOSSARY governs).
  Post-pass fixes: one note wrongly deleted by an agent restored (181.11), stale "Omitted per §3.5"
  margin lines removed from 20 scaffolds (all were side-notes or page-foot sources); brief.py wording
  defers to the card; bible.py takes *Luc/Luce*.
- **01-a translated (2026-10-01):** one Opus agent, ≈ 95K tokens, 7 tool calls; 13 notes; lint clean.
  Per-wave: V-03 verified, and its title corrected (*Hus und Wiclif*, as Loserth cites it; the pilot
  had *Wiclif und Hus*); V-05 (Rufinus) not found in the local PL by phrase search, still to-verify;
  V-04, V-07 still to-verify.
- **Next: review 01-a in a FRESH session** against the four classes, then card changes, then briefs of
  3–5 chunks (from 01-b). For the reviewer: (1) the agent made *Illos autem parentes* (1.17) and
  *Illis autem cultis* "And" where the pilot had "Now": minor premiss or continuative? (2) the C note
  n2 on *et fides est ecclesia que …* (1.2–4), plate not checked; (3) *suffragium* → "suffrage"
  under the *suffragia* row (singular is fine, coordinator's view).

## Status 2026-09-30 (end of the first M5 session)

**Done (stages 1–5a):** Latin established and plate-read; 159 scaffolds cut. All committed locally on `main`
(nothing pushed; the Vercel project is not git-connected).
- Chunk size: **≤ 5 pp (Wilson)**, greedy at the editor's ¶ → **159 chunks** (23 chapters; median ~900 words;
  8 chunks run 6–7 pp because one ¶ does; ids `wyc-ecclesia-NN-x`).
- Extraction fixes (djvu.py) found by the completeness test (`complete.py`, now a standing step): whole pages
  had gone to the apparatus, ~35 pages had apparatus in the Latin, line-final verse numerals dropped. Dialogus
  checked old-vs-new: unaffected.
- Vote (vote.py) new rules, all logged in CONVENTIONS §3.3 **for Wilson to confirm**: R4a, NW, TAIL/GAP, EDGE;
  plate decisions key on the pivot token and always apply; an OVERRIDE wins. Writer normalises the z glyph
  (`^ \ $`), degree sign as 0/", old-style verse 1 read as *i*. `wordsplits.tsv` holds glued/fused forms.
- Plate pass: 2,236 decisions (`plate_decisions.part01–15.tsv` + `part99` coordinator OVERRIDEs, merged into
  `plate_decisions.tsv`). Brief: `text/ecclesia/PLATE-BRIEF.md`. Queue 0, stale 0.
- Open flags for translation: `text/ecclesia/PLATE-FLAGS.md` (p. 515 English side-note bleed; p. 245
  *coronanus*; p. 93 *limi[t]avi*; p. 188 join; superscripts pp. 239/243).
- Leftover generated files `text/ecclesia/p589–p600.*` (index; deletion was blocked) are ignored by
  `last_page` = 587.

**Cost so far:** plate pass ≈ 4.2M new tokens (measured ~14K/sheet; estimate was 1.5M).
**Remaining estimate:** side-note pass ~1M · CARD + first-chunk review ~0.3M · translation ~12.3M
(587 pp × ~21K) · per-wave ledger checks ~3M · close-out ~0.5M ≈ **17M more; volume total ≈ 21–22M**
(first estimate 17–18M).

**Next, in order (fresh session):**
1. Side-note pass (WORKFLOW 5): one plate agent per ~10 chapters corrects each scaffold's OCR side-notes.
2. `chunks/ecclesia/CARD.md` from `chunks/dialogus/CARD.md` (Loserth; sigla A, A₁, B, D from the pilot headnote).
3. Translate **01-a** and review it in a fresh session against the four classes; card changes land first.
4. Then briefs of 3–5 chunks with per-wave checks (WORKFLOW 7–8). Glossary/ledger as for the Dialogus.

## Where things stood at the handoff (2026-09-29)
- **M3 *Dialogus*: done** (38 chunks, close-out, rulings; `chunks/dialogus/RESUME.md`, `RULINGS-PENDING.md` §D).
- **M4 site: live** at wyclif.wrootpress.com (home = the whole Society edition; Dialogus at `/dialogus/`).
  Deploy recipe in memory, `reference_wyclif-deploy`; the Vercel project is NOT git-connected.
- **Method for M5:** `WORKFLOW.md`, the single-pass brief workflow (`scripts/w3/brief.py`), measured at
  ~55k tokens/chunk against ~93k for one agent per chunk. Runs on the Claude Code plan: **no API budget**
  (the API method, `scripts/pilot/translate_api.py`, is priced at $0.22/page for reference only).

## *De ecclesia* facts
- Slug `ecclesia`; ed. J. Loserth, 1886; primary scan `latinworks10wycl` (644 leaves); 5 other free scans;
  **no Fordham text**. Plate offset: printed page = leaf − 37 (`catalog/plate_offsets.tsv`).
- ~136,500 Latin words (5.8× the Dialogus). Old measurement: 24.1 plate items / 1,000 words, 3,296 items,
  but on the OLD extraction (see stage 1).
- A pilot exists: `pilots/wyc-ecclesia-01a.md`, bk I ch. 1, alineae A–C (pp. 1–5), plate-read, 29 notes.
  Its ledger rows are V-01…V-12 and V-19 in `LEDGER.md`; several are still `to-verify`.

## Before anything else: confirm the chunk size
The Dialogus chapters average ~2.6 pages; *De ecclesia*'s run to ~26. `chapters.py` already splits any chapter
over 8 pages into parts of at most 7, at the editor's ¶ (CONVENTIONS §1), so the volume comes out at roughly
100 chunks. The single-pass measurements were on 2–6-page chunks; 7 pages of dense Latin in one pass is
untested. **Decide with Wilson:** keep ≤7, or lower the split to ~4–5 pages (a one-line change at
`chapters.py:116`). Cost is per page either way; the question is quality on the longest chunks.

## First steps (in order)
1. **Hard stop for Wilson** (volume estimate + "which model, and go?"). Rough estimate on the plan, from the
   Dialogus rates: witnesses + vote ~0 (computation) · Latin plate pass ~1.5M · side-note pass ~0.5M ·
   translation ~12M (≈ 600 pages at ~21k/page, the brief rate) · per-wave ledger verification ~3M · close-out review ~0.5M
   ≈ **17–18M tokens**. Restate it with the chunk count once stage 5 has cut the scaffolds.
2. **Rebuild the witnesses** (WORKFLOW stage 1). The current `text/ecclesia/` (untracked, generated, from the
   old extraction) must be regenerated: remove `text/ecclesia/witnesses/*.jsonl`, then
   `.venv/bin/python scripts/w3/witness.py ecclesia`. This also writes `text/ecclesia/apparatus.json`.
   Generated data, re-derivable by re-running; say so when doing it. Same later for `officio-regis`.
3. **Completeness test without Fordham:** diff the established text against a full independent witness
   (e.g. `iohanniswycliftr00wycluoft`) for runs of ≥3 words present on one side only (PLAN, the M2
   extraction defect). Then the numeral sweep (PLAN, "Numerals").
4. Vote, then look at whether the big R4 / THIN / R3 classes can be settled by a rule before cutting crop
   sheets (PLAN notes this as open), then the plate pass and `nonword.py ecclesia`.
5. Scaffolds (with the chunk-size decision), side-note pass, `chunks/ecclesia/CARD.md` from the Dialogus
   card (Loserth's sigla A, A₁, B, D are in the pilot's headnote), first chunk reviewed in a fresh session.
6. Translate in briefs of 3–5 chunks, with the per-wave checks (WORKFLOW stage 8).

## Suggested opening prompt for the new session
> Continue Wyclif M5 on *De ecclesia*. Read `~/wyclif/M5-RESUME.md`, then `WORKFLOW.md`. Start with the
> chunk-size question and the volume estimate (hard stop) before running anything.
