# Translation brief: potestate-pape 11-k–11-m

You translate these 3 chunk(s) of Wyclif's *Tractatus de potestate pape* in a single pass. Everything you need is in this file:
the working card, the glossary rows these chunks use, and for each chunk its scaffold and the editor's
apparatus for its pages. Work so as to use few tool calls:

1. Read this brief once (it is the only file you need to read, unless the card names one for your chunk).
2. For each chunk, write the COMPLETE chunk file ONCE with the Write tool to its path (given in the chunk's
   header below): the scaffold with `status: translated`, the title, the English after every Latin block,
   headings and side-notes as the card says, Notes, and Transcription notes, in the card's
   layout. Never alter the Latin. Do not make a series of small edits.
3. Use the apparatus given here for variants (the card's rule: a variant that gives the sense is translated
   with a T note citing the siglum; otherwise translate the print and flag it). Open a plate image only if a
   word cannot be construed at all from the print plus the apparatus; otherwise flag it as a Latin doubt.
4. Scripture: quote the Douay-Rheims as you know it. At the END, check every reference you quoted in ONE
   command: `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/bible.py "Ref 1" "Ref 2" ...` and fix any wording
   that differs, in the same chunk file (this is the one allowed round of edits).
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-11-k.md chunks/potestate-pape/wyc-potestate-pape-11-l.md chunks/potestate-pape/wyc-potestate-pape-11-m.md` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.

Standing rules (from the *De ecclesia* briefs, 2026-10-02):
- Do NOT search the Patrologia or other sources; a separate checker verifies them afterwards. Give the
  editor's reference, the modern form in the English, and "to be checked" with a fresh LEDGER id per item
  (never reuse an id).
- Notes open with their bold class codes, `**S/C.**`, never bare letters mid-note. No process words in
  the notes ("the report", "the coordinator", "brief").
- OCR scars (stray English or margin letters, line numbers read as words, glued or broken words,
  numerals read as letters) stay out of the chunk: translate the print's word and list each scar in your
  final message only (page.line, token, likely print reading). The coordinator fixes the Latin.
- Flag every place the established Latin may have LOST a word (it does not construe, especially at a page
  head or foot) or DOUBLED one: page.line and the suspicion. Translate the print as it stands; supply a
  missing word only in brackets with a T note. The editor's print governs; list any departure.


## The working card

# TRANSLATOR CARD — one *De potestate pape* chunk

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Adapted from `chunks/ecclesia/CARD.md` (2026-10-07), with its close-out lessons written in. Read it, then `GLOSSARY.md`, then your
scaffold (or your brief, which carries all three). Consult CONVENTIONS.md only when the card sends
you there. Work in `~/wyclif`. Wyclif is approached with **daggers drawn**: the most recent English
versions were "worse than useless" because of four error classes (below). Your English must survive
a hostile reader with the Latin open.

## Work lean (cost is per tool call: each call re-sends your whole context)

1. One call reading what you need (the brief, or CARD + GLOSSARY + scaffold).
2. **One** `bible.py` call with every scripture reference you need (it takes many refs).
3. Plates **only** for a Latin doubt the print plus apparatus cannot settle.
4. Write each finished chunk in **one** Write of the whole file (Latin blocks copied unchanged).
5. Lint once; fix; done. Draft in your head, not in the file.

## The volume

*Tractatus de potestate pape*, ed. Johann Loserth (Wyclif Society, 1907), from the plates of archive.org
`latinworks19wycl` (**leaf = page + 61**). Written 1379 (Loserth), after *De ecclesia* and *De veritate
sacre scripture*, both of which it cites ("libri proximi" at 1.7 is the editor's crux: he takes the
nearest book to be *De officio regis*). A **treatise** in twelve chapters: Wyclif speaks in the first
person, states conclusions, raises objections (*instatur*, *obicitur*, *arguitur*) and answers them.
Its subject is power (*potestas*), what it is and how it is divided, then the papal power: Peter's
primacy, the pope as Christ's vicar, the election of a pope, the "Caesarean" pope and the endowment,
and Antichrist. **Richard FitzRalph** (*dominus Ardmacanus*, "the lord of Armagh"; *Summa in quaestionibus
Armenorum*) is a constant partner, quoted and answered. Pp. 398–406 are a medieval **compendium**
(*Sentencia libri … in compendio*), a summary of the chapters that came down with the work: translate it
like the text.

**Sigla** (Loserth): **A** Prague, Metropolitan Chapter C 73 (his base, "well-preserved", a copy made
"by a man of learning and ability"); **B** Prague, University Library III F 11 (early 15th c.; Loserth
argues A and B are closely related and A cannot have been copied from B); **C** Prague Univ. XI E 3,
variants only near the end (the *Protestationes* extract). Both A and B carry marginal notes, which
Loserth prints ("A in marg.: …", "B in marg.: …"); A's copyist was a Catholic reader who annotates
against Wyclif ("Cave … contradicit sibi"). Cite variants with these sigla.

**The page foot** (in your brief as "apparatus", by page) has two blocks, both keyed to the line:
the variants (`27, 28. B: et aliqua potencia est creata deest.`) and Loserth's source references (`27. Decret. Unam sanctam.
Extrav. comm. lib. I, tit. VIII, cap. I.`). The OCR of it is rough: read it for sense, not letter by letter.

## The job

The Latin in your scaffold is **established and frozen** (three-witness vote + plate reading). Fill
`[TITLE]` (short, lower case: "headship: the pope is not head of the church"), each `[ENGLISH]`, the
notes and the transcription notes; set `status: translated`; lint; report.

- **Headings:** keep `## ¶k · range` exactly. **Never change a range; never split a paragraph.**
  (The pilot headed its paragraphs with Loserth's alinea letters A, B, C; the scaffolds do not
  carry them, so leave the ¶ numbers.)
- **Never alter the Latin.** OCR scars you find (a stray mark, an English side-note word, a broken word) are
  REPORTED, never repaired in your file: the coordinator repairs the established text (`text/potestate-pape/
  tokenfix.tsv`) and refreshes the chunk's Latin. A Latin block you receive may already carry such repairs. A word that looks wrong: read the apparatus for that line first; then,
  if still doubtful, the plate (`text/potestate-pape/raw/leaves/nLEAF.jpg`, LEAF = page + 61 padded to four digits: p. 1 = `n0062.jpg`;
  ⚠ **p. 266** is faded blank in that scan: use `https://archive.org/download/tractatusdepotes00wycl/page/n327.jpg`). A variant
  that gives the sense → translate it + **T** note citing the siglum; a compelling emendation →
  translate it + **T** note "(our emendation)"; neither → translate the print and flag it. Never
  smooth nonsense into sense. Report every such case. **Loserth's printed text governs** (ruled
  2026-10-02): translate it, his own emendations included, unless it will not construe; a manuscript
  reading is chosen only then, and a single manuscript's reading never outweighs the print without cause; every departure gets a T note
  giving both readings. Open flags for this volume:
  `text/potestate-pape/PLATE-FLAGS.md` (read it if it exists and your pages are listed there).
- **English layout:** `[N]` at the same word as `[p. N]` in the Latin (the chunk's first `[p. N]` is
  implicit). Supplied words in `[brackets]`, sparingly. **Quotations** in quotation marks. Your brief
  carries Loserth's **italic runs** per page (from the scan's OCR; a side-note can split one run in two,
  and an apparatus phrase occasionally slips in). They are the editor's judgement of where a quotation
  runs, not the manuscript's: follow them by default, depart where the source shows otherwise (say so in
  a note). Reviews do not check quotation bounds against the italics. Italicised scripture inside
  indirect speech is quoted too (the italic words in quotation marks, the English syntax around them); where
  quoting would garble the sentence, leave it unquoted and give the reference in an **S** note.
- **Ordinals:** a degree-sign ordinal can print or OCR like a two-digit number (*30 et 10* = 3° and 1°, *Pot.
  pape* 3.28). Read both forms the same way, and check the plate when a citation looks impossible.
- **Formulae of the disputation** (GLOSSARY §C, ruled 2026-10-01), rendered the same way throughout: *instatur* "it is objected" ·
  *obicitur* "it is objected" · *arguitur* "it is argued" (with *per*: GLOSSARY) · *dicitur* "it is
  said" (in an answer: "the answer is") · *respondetur* "the reply is" · *conclusio* "conclusion" ·
  *antecedens / consequens* "antecedent / consequent" · *consequencia* "inference", ⛔ never
  "consequence" (GLOSSARY §C).

## The four error classes (Thakkar) — check every sentence

1. **Terms:** GLOSSARY.md governs, one term one rendering. Tag the **first occurrence in the chunk**
   of every §A–C term: `[quiddity]{g:quiditas}`. The key must exist in GLOSSARY.md. A term that looks
   technical but has no row: render it sensibly, untagged, and propose it in your report.
   **CONTEXTUAL** rows hold two senses English splits: choose by context and write a **C** note at
   the first occurrence in the chunk and wherever it leans to the other sense (the dikaiosune rule,
   CONVENTIONS §6).
   Key rulings carried from *De ecclesia*: *ecclesia* church (**lower-case**) · *caput* head ·
   *membrum* member · *predestinati* the predestinate · *presciti* the foreknown · *papa* pope ·
   *vicarius Christi* vicar of Christ · *caritas* charity (never love) · *dominium* lordship · *viator*
   wayfarer · *ex fide* as faith teaches · *sentencia* teaching (the rest: GLOSSARY).
   ⚠ **This volume's own term is *potestas*** and its kin (*potencia*, *auctoritas*, *iurisdiccio*,
   *primatus*, *dotacio*, *papa cesareus*): check GLOSSARY for each; where it has no row, render
   consistently within your brief and PROPOSE the row (the coordinator rules between briefs).
   **Ruled (Wilson, 2026-10-07):** *potestas* is always "power". *potencia* is CONTEXTUAL: "potency" inside
   Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated),
   "power" elsewhere (God's power, free choice, ordinary might); *potencia absoluta* stays "absolute power".
   Wyclif uses the two words interchangeably (*potestas vel potencia* 4.7, *potestatem sive potenciam* 4.11):
   render such a pair "power or potency" and write a **C** note at the first one in your chunk. Never write a
   note or headnote that claims the two words differ in sense; ch. 1 shows they do not.
2. **Connectives carry the argument.** ⛔ Never omit one, never turn one into filler.

   | Latin | English | Never |
   |---|---|---|
   | enim, nam | for | "now", "indeed" |
   | ergo, igitur, ideo | therefore, so, then | "now", "and", "indeed" |
   | sed / autem, marking the **minor premiss or next step** | now | (omitted) |
   | sed / autem, adversative | but | (omitted) |
   | autem, continuative | and | (omitted), and **not "now"** |
   | cum (concessive / causal) | although / since | "whenever" |
   | tamen | yet, nevertheless | "therefore" |
   | item | again, also | "now" |
   | vero (continuative) | and; but (adversative) | "now", "truly" |
   | verumtamen | nevertheless | "but truly" |
   | unde | hence, so | "whence" (archaic), "where" |
   | per idem | by the same token | "in the same way" |
   | ymmo | indeed, rather (correcting upward) | (omitted) |
   | patet; constat | it is clear; it is evident | |

   *nunc … aliquando* ("at one time … at another") is never "now". "Now" is reserved for the minor premiss, or the step that brings a new premiss to bear (*Illos
   autem parentes debemus …*, 1.17). An *autem* that only extends the same step is "and" (*Illis autem
   cultis …*, 1.19). ⚠ The commonest error in *De ecclesia* (close-out, ~50 of 69 connective fixes): a
   *sed* that brings the minor premiss of a syllogism closed by *ergo / ideo / igitur* rendered "but".
   Before writing "but" for a *sed*, look ahead for the *ergo*: if one follows, it is "now".
3. **Ordinary words with a medieval sense:** GLOSSARY §D; look up any word whose classical and
   Wyclifite senses may differ, and propose additions.
4. **Syntax:** construe before rendering (main verb, subject, what every relative and genitive
   hangs on). Keep quantifier order where it is meaning (*nullus papa … caput*; *quilibet papa*).
   Keep Wyclif's long periods where English tolerates them. **A doubtful construal is never chosen
   silently:** translate the likelier reading and write a **C** note giving the alternative.

## Scripture

`python3 scripts/w3/bible.py "Luc 17:23"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering) or
`python3 scripts/w3/bible.py --find "nolite ire neque sectemini"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and write
an **S** note giving the Vulgate. Modern references in the English (Luke 17:23). The chapter numbers
are Wyclif's, the verse numbers Loserth's (the headnote says so once).

## Already glossed in this work (no second first-occurrence note)

*prescitus* "the foreknown" (03-a) · *satrapa* (04-e) · *curatus* (02-d) · *potencia* CONTEXTUAL (01-a) · *dominus Ardmacanus* / *Armachanus* (01-a, 02-c) · *Lincolniensis* "Lincoln" (03-e). Gloss a term again only where its sense here differs.

## Notes

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter:
  **T** text · **C** construal · **G** glossary (passage-specific only; otherwise a tag) · **S** source ·
  **R** reception/context (e.g. a B marginal gloss that shows how an early reader construed the text,
  CONVENTIONS §4; Hus's reuse where Loserth notes it, e.g. "Hus, fol. 21b" in the apparatus).
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your
  report with a status: `editor` (Loserth's source reference at the page foot), `to-verify` (from
  memory: every patristic or canon-law identification you did not read in this session), `verified`
  (you read the source text this session: say where; local PL at `~/patrologia/sources/pl/tei/`).
  ⛔ Never pass memory off as verified. Id `P<chunk>-<n>` (`P02a-1`), cited in the note:
  "(LEDGER P02a-1)". FitzRalph: cite book and chapter of the *Summa in quaestionibus Armenorum* as
  Loserth gives them (he often says "mihi ad manum non est", i.e. he could not check: then `to-verify`). Loserth's references to the *Corpus iuris canonici* (Decretum, Extravagantes)
  are `editor`; give them in modern form (*Extrav. comm.* 1.8.1) and say the form is ours.

## Model of register

`pilots/wyc-ecclesia-01a.md` (De ecclesia pp. 1–5) is a reviewed model of register and note style:
read it for that only (it predates some GLOSSARY rulings; **GLOSSARY governs**). **Chunk 01-a** carries
the `## Headnote` (CONVENTIONS §12 order: occasion, text, the work's move, where it is answered; date, editor,
sigla, the compendium), each unverified claim marked `[verify]`.

## Side-notes

Already read against the plates (WORKFLOW 5, `text/potestate-pape/sidenotes.fixed.tsv`) and
placed in your scaffold's section. ⛔ Do not edit them. One that is plainly wrong (garbled, or at
the wrong line): report it under Latin doubts as `side-note page.line`.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/potestate-pape/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk(s)**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words per chunk, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?

## Glossary (the 314 rows these chunks use; the full file is GLOSSARY.md)

# GLOSSARY — FROZEN 2026-09-28 (Wilson's pilot review)

*One Latin term, one English rendering, every time, across the whole corpus. A reader must be able
to recognise the same word coming back, because Wyclif's arguments turn on it. A rendering changes
only by a dated decision in CONVENTIONS' decision log, never silently in a chunk. Entries may be
*added* by recorded decision as new terms appear. **Tag keys:** a chunk tags a term as
`[English]{g:latin-form}` (CONVENTIONS §11), and the key must match a Latin form in one of the rows
below. These rows are also the source of the site's hover glossary. Where a term has two senses,
the entry says so and each chunk's note picks one. A term marked **CONTEXTUAL** holds together
senses English splits: its English is chosen by context, under the dikaiosune rule (CONVENTIONS §6).*

**Sources of the decisions.** "Pilot" = settled in `pilots/` this session. "T. p. N" = Mark
Thakkar, "Duces caecorum," *Vivarium* 58 (2020), page N (`reference/`), which documents the
errors of the two most recent translations. His corrections are adopted here unless an entry says
otherwise.

**Orthography.** Headwords are given in the Society editions' medieval spelling (*eciam*,
*racio*, *quiditas*, *ymmo*), because that is what the translator will meet on the page.

---

## A. The church

| Latin | English | Note |
|---|---|---|
| ecclesia | church | Lower-case in English except in a proper title. |
| ecclesia militans / triumphans / dormiens | the church militant / triumphant / sleeping | *Dormiens* = the souls in purgatory. Not "dormant". |
| pars peregrinans; peregrinari | the pilgrim part; to be a pilgrim | Augustine's *peregrinatio* (Ench. 56). Pilot. |
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| presciencia | foreknowledge | |
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| claustrales | cloisterers | Ruled 2026-09-28 (20 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| Cestrensis | the Chester [chronicler] | Ranulf Higden, *Polychronicon* (S note at first occurrence in a chunk). Ruled 2026-10-08 (coordinator, delegated; conformed in 06-h … 09-b). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| carismata | charisms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 176.1). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 11-k: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-k.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-k
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "303.1–307.28"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 11 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1015 words; 977 unanimous or majority-real; 27 settled by vote (R2 15, R3a 7, R5a 5); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n364–n368 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 11: [TITLE]

## ¶1 · 303.1–304.3

> [p. 303] Hic videtur michi quod prima conclusio concedi debeat, cum totus numerus prescitorum, ymo omne peccatum, prosit per accidens sancte ecclesie. Nam Rom. VIII, 28 dicitur: Scimus quoniam diligentibus Deum omnia cooperantur in bonum. Unde solet esse distinccio quomodo aliqua prosunt per se directe et occasione data ad beatitudinem sanctorum, sicut bona virtutis et gracie, aliqua autem prosunt per accidens indirecte vel occasione ex gracia Dei accepta, cuiusmodi sunt peccata; et sic loquitur beatus Gregorius vocans felicem culpam, ymo Augustinus dicit quod expedit multos incidisse in multa peccata enormia, ut exemplificat de Petro. Et patet quod non est color quod si res prosit ecclesie tunc non est destruenda; oportet enim peccatum prodesse ecclesie, sed talia per accidens prosunt, sic quod illis ablatis non minus aliunde insurgeret profectus ecclesie, quia aliter quilibet foveret peccatum, ymo ageret, ut dampnetur, quia tunc Deus preter istos dampnatos produceret tantam ecclesiam quantam eternaliter diffinivit, cum nullum peccatum potest mutare divinum propositum vel tollere gloriam spirituum beatorum; et isti dampnati cederent beatis ad gaudium, quo aliter caruissent, ut deductum est in materia de necessitate futurorum. Ymo videtur quod omne peccatum tantum prodest ad salutem ecclesie, sicut totum meritum Christi, quia omne peccatum facit unite totum profectum ecclesie, cum aliter passio Christi infinitum plus prodesset ecclesie quam peccatum vel meritum membri Christi, et cum [p. 304] meritum Christi tantum finite prodest ecclesie, videtur quod omne aliud meritum proderit sub non gradu.

[ENGLISH]

## ¶2 · 304.4–304.18

> [p. 304] Et ex istis videtur quod dicentes omnem hominem sumi de corpore pro tempore quo magis prodesset ecclesie, periculose sompniant, quia vel posset universalis ecclesia esse perfeccior quam ista erit de facto vel non. Si sic, concedendum foret consequenter quod mors cuiuscumque presciti posset plus prodesse ecclesie et per consequens non; si alias vel aliter fuisset mortuus; minus prodesset ecclesie, quia sic omne factum bonum vel malum actum esset ad maturiorem profectum ecclesie. Si non; tunc consequenter concedendum foret quod omnia que evenient absolute necessario evenirent, cum contingencia, si ponatur, eque respicit omne opus Dei vel aliquod quo ad ipsum.

[ENGLISH]

## ¶3 · 304.19–305.6

> [p. 304] Dimissis autem istis stulticiis conceditur quod omne peccatum facit ad utilitatem et honorem ecclesie, non tamen est propterea faciendum, quia cum caritas incipit a se ipsa; nemo faceret aliquid nisi quod sibi proderit et sancte ecclesie. Sed quid prodest homini, quod sic peccat? Non enim sequitur: Hoc peccatum per accidens infert bonum homini, quia penam et alia; igitur sibi prodest; quia illo subducto et quocumque tam malo sequitur quod melius sibi esset. Ideo oportet concedere quod omne peccatum presciti obest sibi; et non prodest; licet prosit ecclesie. Nec oportet, si homo debet velle in casu damnacionem suam ad profectum ecclesie, quod propterea debet velle peccare, ut patet alibi. Unde videtur quod omnia tantum et ad tantum [p. 305] prosunt ecclesie ut aliud, licet dispariter. Deus enim utitur qualibet creatura ut organo ad profectum ecclesie, eciam ad proficiendum omnibus et singulis membris ecclesie, in quocumque profectu signabili, sicut multitudo trahencium trahit navem.

[ENGLISH]

## ¶4 · 305.7–305.18

> [p. 305] Tres autem gradus sunt notabiles habentes modos disparis racionis. Christus enim prodest fontaliter, predestinati directe parcialiter et peccata indirecte occasionaliter. Et patet quod multi heretici prosunt multum ecclesie et tamen propter sua opera sunt culpandi, ut proponens in casu intoxicare hominem infert sibi per accidens sanitatem. Ideo docet Magister quod in merito est simplicitas oculi principaliter attendenda. Et tota laus est architectonice autori omnium attribuenda. Ipse enim necessitat peccatum ad proficiendum ecclesie.

[ENGLISH]

## ¶5 · 305.19–306.18

> [p. 305] Ulterius dicitur quod non est color, si nescitur quibus prodesset dotacionis vel peccati destruccio, igitur non debet intendi, cum sufficit pro natura intencio honoris Dei. Et prudens reputacio utilitatis Christi quod de facili contingeret de ablacione temporalium, non intencione puniendi vel deteriorandi ecclesiam vel aliquod eius membrum, sed intencione exonerandi vel prodessendi mundo oppressis et perfeccionem status, quem Christus instituit renovandi. Hoc enim debet facere in lege veteri eciam extrahendo iumentum de puteo et exemplificat Augustinus, ut recitatur V questio V: Non omnis, quomodo ex caritate freneticus privandus est gladio et litargicus excitandus a sompno, et si expectaremus in istis revelacionem [p. 306] vel demonstracionem gignentem scienciam, raro vel nunquam faceremus bonum opus extrinsecum, ut recitat decretum ex declaracione Augustini XXIII questio V: De occidendis. Et sic nec medicus corporalis nec medicus spiritualis umquam apponeret medicinam. In talibus igitur innitendum est arti scripture, et tunc Dominus nedum habebit nos excusatos, sed subducta invidia premiatos, eciam licet dampnum multis eveniat, sicut sepe contigit ex predicacione Christi. Nec sequitur ex isto, quod quilibet debet spoliare proximum occupantem superflua, quia aliis ut sacerdotibus limitatur sermo sancte exhortacionis, aliis ut secularibus dominis limitatur sermo severe monicionis, et aliis ut stulte dotantibus limitatur in aliorum defectu operacio prudentis ablacionis; nam omnis homo debet modo suo prodesse ecclesie.

[ENGLISH]

## ¶6 · 306.19–306.25

> [p. 306] Ulterius notandum finaliter quod deficiente quocumque papa cesareo vel quocumque alio eius prelato usque ad simplicem sacerdotem ipse sufficeret ministrare qualiacumque sacramenta in scriptura sacra fundabilia, vel eciam sacramentalia que post dotacionem ecclesie licite sunt adiecta.

[ENGLISH]

## ¶7 · 306.26–306.33

> [p. 306] Probatur primo ex hoc quod sacramenta et ritus, quos Deus singulariter summo sacerdoti instituit, potuit et debuit inferior sacerdos in defectu summi sacerdotis perficere, ut patet ex dictis. Sed longe minoris auctoritatis sunt tradiciones humane post dotacionem in istis adiecte, igitur multo magis ipsas sufficit supplere inferior sacerdos.

[ENGLISH]

## ¶8 · 307.1–307.10

> [p. 307] Item, ut patet ex dictis et testimonio domini Ardmacani, omnes potestates ordinis sunt equales. nec minuitur eciam potestatis iurisdicionis execucio, nisi de quanto racionabiliter est restricta. Sed deficiente quocumque superiori pontifice et imminente necessitate ad aliquod necessarium sacerdotale ministerium, non superesset, qui racionabiliter ita restringeret, ergo de communi lege Dei liceret inferiori presbitero in casu posito perficere ministerium assignatum.

[ENGLISH]

## ¶9 · 307.11–307.28

> [p. 307] Confirmatur tercio per hoc quod ex fide scripture Christus assisteret sue ecclesie usque ad finem seculi, sed irracionalis et increpandus foret; si exigeret a clero suo officium et assistente potestate presbiteri ad faciendum hoc impediret ipsum presbiterum; ad supplendum igitur ex plenitudine potestatis Christi simplex sacerdos in tali casu haberet potenciam ac sufficienciam ad ministerium tam necessarium dispensandum. Sic enim propter necessitatem baptismi sufficit laycus in defectu cleri baptizare. Sic eciam sufficit quicumque sacerdos simplex eque plene cum papa absolvere in mortis articulo, quare igitur non eque sufficit deficiente superiori prelato ineque necessario sacramento? Leges enim vel constituciones humane non obviant legi Dei nec sunt credende nisi de quanto consonant racioni.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 303.1: All things, even evil, profit the Church accidentally.
- 304.19: Sin is not to be committed for its accidental benefits.
- 305.7: Three ways of profiting the Church.
- 305.19: We may not know who will profit by disendowment, it is enough that it is done in God's honour,
- 306.7: We must obey Scripture even though to the hurt of some, but we must not go beyond our authority.
- 306.19: Lacking prelates, simple priests may administer any sacrament,
- 307.1: All orders confer essentially the same powers.
- 307.11: Christ will not forbid a priest to fulfil the duties which he himself laid on the clergy.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 303: *facit* (30 is the line number) [R4]
  - 304: *∅* (folio bar after Et (237ᵃ in margin) read as i) [INS?]
  - 304: *infert* (25 is the line number) [R3]
  - 306: *∅* (even is the English side note (We must obey Scripture even ...)) [R3]
  - 306: *In* [R6]
  - 306: *et* [R3]
  - 306: *sed* [R3]
  - 306: *alio* (20 is the line number) [R4]
  - 307: *potestate* (15 is the line number) [R4]
  - 305: *fontaliter,* (S-split: one word, italic) [OVERRIDE-SCARPLATE]
  - 307: *iurisdicionis* (S-split: one word) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 303:
4. Codd. in marg.: Prodesse dupliciter capitur. 16. Codd. in rnarg. :
Peccatum prodest ecclesie mullum. 26. Codd.: reductum.
12. Cf. De Ecclesia pag. 164, Serm. II, 1 52, Op. Evang.
III, 198.

p. 304:
1. Codd. in marg. : Peccatum quomodo prodest ecctesie multum et
nocet suo peccanti.

p. 305:
7. Codd. in marg. : Prodesse tres sunt gradus. q. Codd.: pre-
De Potestate Pape. 20

p. 306:
19—23. Codd. in marg. : Sacerdos simplex dejiciente papa cesario vel
alio prelato ; Solnm B: potest sufficienter ministrare omnia sacramentd.
4. Cap. VIII.

p. 307:
21, 22. B: sufficiat. 22. Codd. in marg.: Ministrare sacramenta
dejiciente papa quis potest.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 303: Scimus quoniam | diligentibus Deum omnia cooperaniur in bonum. | felicem culpam, | expedit multos incidisse in multa peccata enormia, ut exempiificat de Petro.
p. 304: omnia que | evenient absolute necessario evenirent,
p. 305: Non omnis, | freneticus privandus est gladio et litargicus excitandus a sompno,
p. 306: De occidendis. | ± xr sr ~l x
```

---

## Chunk 11-l: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-l.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-l
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "307.29–311.33"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 12 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "863 words; 821 unanimous or majority-real; 37 settled by vote (R2 28, R3a 5, R5a 4); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n368–n372 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 12: [TITLE]

## ¶1 · 307.29–308.14

> [p. 307] Contra ista arguitur per hoc, quod iuxta hanc viam, sicut laycus sufficit baptizare sic et confirmare, conficere ac sacramenta quecumque alia ministrare. Quis igitur pro absolucione de percuciendo aut occidendo clericum adiret Romanum pontificem? Ad illud dictum est quod non sequitur. [p. 308] cum racio diversitatis sit necessarioritas baptismi supra alia sacramenta. Verumtamen subtiliantes in Dei potencia absoluta dicunt quod sicut Deus potest communicare nedum layco sed femine ac alii irracionali potenciam conficiendi ac ministrandi quelibet sacramenta, sic et ipsum potest ministrare huiusmodi sacramenta. Nec credo quod aliquis impugnabit illum articulum, quia cum multa absolute sunt necessaria, que est inefficax populo predicare; et grosse procedo in ista materia limitate loquendo de posse legali et Dei potencia ordinata, ideo dimitto scrutinium talium conclusionum detegens sentencias catholicas, quas credo prodesse ecclesie.

[ENGLISH]

## ¶2 · 308.15–309.27

> [p. 308] Videtur igitur michi quod licet et expedit in casu layco baptizare, et cum non sit de necessitate salutis cuiuscumque predestinati recipere corporaliter alia sacramenta, videtur michi quod non debet presumere ministrare alia sacramenta. et sic reservacio ac restriccio potestatis potest tam bene quam male fieri, sicut reus potest tam stulte quam pie adire Romanum pontificem pro absolucionis beneficio obtinendo. Et debet supponi, quod utrobique bene, nisi sit patens evidencia contradicens et specialiter superbia ac avaricia prelati et omnino utrimque preponderancia sacramenti. Videtur enim quod plus obesset monstruositas peccati in prescito masculo ad recipiendum vel ministrandum legittime quelibet sacramenta quam foret quantumcumque corporalis monstruositas vel distinccio sexus in femina predestinata et virtutibus perornata, sive ad recipiendum sive ministrandum quelibet sacramenta. et tamen in penam peccati multi de [p. 309] generacione adultera sic phariseice seducuntur, quod preponderant signum visibile humanitus institutum signato invisibili quod Deus preponderat, ut in casu et facto Romane ecclesie, quod narrat Cestrensis cap. Ill libri V scilicet quod quedam femina sedit in papatu duobus annis et quinque mensibus post Leonem. Hec dicitur fuisse puella Agnes vocata nacione Moguntina, a suo amasio Athenis in habitu virili adducta, et Johannes Anglicus nominata que in diversis scienciis sic profecit, quod Romam veniens magnos magistros habens auditores trivium legit, demum in papam electa, per suum amasium impregnatur, et dum Lateranensem ecclesiam ab ecclesia Petri pergeret, angustiata pariendi doloribus, inter Collosseum et sanctum Clementem peperit, et postmodum ibi fuit mortua et sepulta. Et hinc dicitur papam hanc viam communiter obliquare, unde non ponitur in cathalogo paparum. In isto casu saltem possibili dicunt leges hominum ipsam non fecisse actus papales nec fuisse electam legittime propter indisposicionem corporis, licet fuerit iam beata. Sed grave est hoc fundare vel fugere, quin generaliter desit eleccio quando eligitur inhabilis quoad Deum; unde angustiatur institucio humana describere verum papam.

[ENGLISH]

## ¶3 · 309.28–310.6

> [p. 309] Sed secundo obicitur per hoc, quod tam necessarium est sacramentum penitencie quam necessarium est sacramentum baptismi, sicut sacramentum ordinis est tam dignum vel dignius [p. 310] utrobique; igitur sicut licet layco propter necessitatem sacramenti ministrare baptismum, sic et in casu necessitatis licet sibi ministrare alia sacramenta. Antecedens videtur ex hoc, quod nullum istorum sacramentorum est necessarium ad salutem nisi necessitate ex supposicione.

[ENGLISH]

## ¶4 · 310.7–311.2

> [p. 310] Hic dicitur quod materia ista requirit fundabilem declaracionem sacramentorum cum suis passionibus. Ideo opportet leviter et breviter in istis transcurrere. Videtur enim quod baptismus habet maiorem auctoritatem scripture quam nostra penitencia humanitus circumstancionata. Unde videtur michi, quod sicut non est possibile peccatorem salvari nisi baptizetur baptismo flaminis, sic nec est possibile peccatorem salvari nisi mente peniteat; verumtamen videtur quod nulla scriptura obviat sed consonat, quod quantumcumque gravis peccator in fine contritus fuerit, et si nullum sacerdotem secum conversantem consuluerit aut peccata sua auriculariter ei ostenderit et dicendo verba humanitus inventa manum super caput penitentis imposuerit, non eo minus per absolucionem Christi quem opportet prius absolvere est vere de numero salvandorum, quia communiter in contricione precedenti peccatum deletur a Domino. Verumtamen meritorium atque legittimum est confiteri secundum formam iam currentem presbitero, sed preternecessarium quoad salvacionem, et licet posterius sufficiens et negligens confiteri proprio sacerdoti incurrit offensam Domini, tamen illa offensa per contricionem anime potest tolli, unde officium prelati foret ostendere libertatem Christi ecclesie et non [p. 311] propter fastum aut questum subditos infundabiliter in servitutem redigere.

[ENGLISH]

## ¶5 · 311.3–311.33

> [p. 311] Unde soleo dicere frequenter in ista materia, quod talia possunt bene fieri, sed si bene fiunt, trepido vel non dico. Et quando queritur si oportet sic fieri, detego libertates ecclesie. Unde credunt multi quod reservantes absoluciones ab excomunicacione, ab alio crimine vel alia censura imposita stulte sepe imponitur ad gravamen ecclesie, ut licet homo possit meritorie petere Romanam curiam, et talis ordinacio per accidens prosit multis, faciens eos timidos ad peccandum, verumtamen communius sapit peccatum in prelato et sollicitudinem preternecessariam in subdito. Sic quod melius foret multis domi satisfaciendo conteri, et quicumque dixerit quod cum hoc non potest salvari propter obedienciam faciendam ordinacioni prepositi, negando libertatem ecclesie transgreditur legem Dei. In votis quidem et obligacionibus stulte factis oportet penitere de stulticia et spiritum consilii flagitare. Unde videtur illis quod non est color concludere quod tale decretum reservandi est licitum, si subiectis timorem incutit ad peccandum; omne enim malum per accidens facit bonum, unde timor filialis debet incuti per sanctam predicacionem prelati, et non timor servilis iudicii per exaccionem prelati cesarei. Et sic videtur michi, quod in quocumque casu christianus non debet accipere dicta sacramenta a layco, cum hoc foret christianismum serviliter altrinsecus onerare. Dignitas autem sacramentorum pensanda consistit in dignitate rei, sacramenti et sua efficacia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 308.2: yclif refuses follow opponents into the conclusions they draw from this.
- 308.15: Lay baptism is allowed because of its necessity; other sacraments are less necessary.
- 308.27: Yet sin is the greatest obstacle to ministration of the sacraments.
- 309.8: Story of pope Joan.
- 310.7: Distinction between baptism and other sacraments.
- 310.16: Penitence.
- 310.27: Verbal confession not absolutely necessary.
- 311.3: Mischief of reserved absolution,
- 311.19: which is not made up for by accidental benefits.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 308: *conficiendi* (5 is the line number) [R4]
  - 308: *Nec* [R4]
  - 308: *illum* [R3]
  - 309: *Collosseum* (hyphenated Col-|losseum (italic); main token holds the whole word) [R4]
  - 310: *illa* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 307:
21, 22. B: sufficiat. 22. Codd. in marg.: Ministrare sacramenta
dejiciente papa quis potest.

p. 308:
i3. B in marg. : Bapli^are si potes laicns. 27. A in marg. : Cave

p. 309:
5. A in marg.: Hic contradicit sibi supra in cap. presenti, ubi signa-
tura 22Q, ubi aliter loquiiur de ista femina ; ib. Non est cap. III sed
XXXII. 8. Codd. in marg. : Mulier papa Agnes. 23. Bifuit.
5. Historiam Agnetis papisse in Polychronico tom. VI, pag.
33o — 352 leges. Johannes Hus (Opp. I, 22oa) hist. e libro Joh.
Wyclif De Pot. Pape deprompsit.

p. 310:
12. Codd. in marg. : Baptismus flaminis est necessarius ad salutem.
16. B: mentem. 26. Codd. in marg.: Confessio auricularis est meritoria.

p. 311:
11. Codd. in marg. : Romam adire pro peccato. ib. Recte: ei ne-
gando. icj. Codd. in marg. : Votum stulte faclum deletur per peniten-
ciam. 27. Codd. : iudici.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 308: Cave heresim.
p. 309: nacione Moguntina, | a suo amasio Athenis in liabitu virili adducta, et loJohannes Anglicus uominata, que in diversis scienciis sic profecit, quod Romam veniens magnos niagistros habens auditores trivium legit, demum in papam electa, per suxim amasium impregnatur, et dum Lateranensem ecclesiam ab ecclesia Petri | pergeret, angustiata pariendi doloribus, inter Collosseum et sanctum Clementem peperit. et postmodum ibi fuit mortua et sepulta. Et hiuc dicitur papam hanc viam communiter obliquare, unde non ponitur in cathalogo paparum.
```

---

## Chunk 11-m: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-m.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-m
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "312.1–316.23"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 13 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "993 words; 952 unanimous or majority-real; 27 settled by vote (R2 18, R3a 7, R5a 1, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n373–n377 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 13: [TITLE]

## ¶1 · 312.1–312.7

> [p. 312] Tercio obicitur per hoc, quod iuxta hic dicta nec oportet esse sacerdotes, nec oportet sacramentum ordinis iterari factum per unum non episcopum sed simplicem sacerdotem; et sic peccarent sacerdotes benedicendo aliquem, clericorum ordinem omittendo et subiectos ultra debitum onerando.

[ENGLISH]

## ¶2 · 312.8–312.21

> [p. 312] Hic dicitur negando primam consequenciam, cum oportet esse Christum et suos apostolos, ymo omnes sacerdotes sacramentales et devotum populum. Scribit enim Augustinus XX de civitate Dei, capitulo XII super illo, quod dicit propheta Apoc. XX 4: Sederunt sacerdotes Dei et Christi et regnabunt cum ipso mille annis; non utique de solis episcopis et presbiteris dictum est, qui proprie iam vocantur in ecclesia sacerdotes, sed sicut omnes christianos dicimus propter misticum carisma, sic omnes sacerdotes, quoniam membra sunt unius sacerdotis, de quibus apostolus Petrus ait: Plebs sancta, regale sacerdocium. Et idem dicit Crysostomus Omelia XL in Imperfecto.

[ENGLISH]

## ¶3 · 312.23–312.26

> [p. 312] Ex istis patet, primo quod femina est sacerdos, et (sic ut dictum est) non probabitur ex lure canonico vel civili quod supradicta femina non sit papa vel quod non valeant opera eius papalia.

[ENGLISH]

## ¶4 · 312.27–314.29

> [p. 312] Patet secundo ex dictis quod sicut omnes sancti viri et femine membra Christi sunt sacerdotes, quia sacramentum dantes ex vi communionis sanctorum, sic solum predestinati sunt membra Christi vel pars sancte matris ecclesie et [p. 313] proprie christiani, ut pulcre docet Crysostomus in Imperfecto Omelia XIX: Solum enim continuatos corpori Christi dicit esse christianos; cum itaque omnia que evenient de necessitate evenient, patet quod necesse est esse hos sacerdotes triplices eciam sacerdotes Baal. Sed quantum ad intentum conceditur quod sine quocumque sacerdote cesareo ecclesia posset viare prosperius quam nunc viat. Ideo non credamus eis, qui iurant quod nisi iste episcopus foret papa, perirent omnia ecclesiastica sacramenta; starent enim melius quam modo, licet non foret aliquis papa cesareus, cum post diem iudicii manebit corpus Christi, et sic sacramentum et res sacramenti, cessantibus aliis onerosis ritibus cum istis viancium sacramentis. Quantum ad secundam difficultatem, credo quod sepe peccant tam ordinantes clericos quam ipsi clerici, quam eciam populares; qui enim vadunt ad curiam Romanam, ut sint episcopi eciam Nullatenses, sed vivendo vitam suffraganeam prelati cesarei, ordinant clericos, benedicunt ecclesias et vivunt seorsum vitam lautam, laborantes propter commodum temporale, peccant graviter et sunt multi apostate. Sed gravius peccant, qui prava intencione menciuntur se esse a papa ad hoc officium deputatos. Gravissime autem qui prava intencione menciuntur in talia, dum tamen non sint infra sacros ordines ecclesiastice constituti. Et correspondenter peccant clerici ordinati, dum tamen manserint in eis; apud Deum humilitas non obest, sed consonat quod per simplices sacerdotes presumentes et sic ordinando peccantes sint legittime ordinati. [p. 314] Unde notando peccata sic ordinancium et dicta sanctorum de symonia episcopi ordinantis pauci vel nulli forent clerici a prelato cesareo ordinati. Ideo non debemus timere de talibus, dum secundum puram conscienciam de iustis operibus observamus ordinem clericalem, quia tunc Deus supplet vicem episcopi et omnia que sequuntur ex istis sunt intrepide concedenda, ut confessum in gravi infirmitate de peccato pro quo sedes apostolica foret petenda, dum contritus fuerit et satisfaciens convalescens non oportet petere Romanam curiam vel prelatum supra simplicem sacerdotem. Et iterum ordinatum per unum sacerdotem simplicem non oportet timere de presbiteratu vel alias ordinari, dum tamen rite fecerit officium clericale, quia sufficit prudens reputacio cum diligenti officio. Deus enim tunc supplet, quia aliter quilibet recipiens sacramentum de suo preposito fluctuaret. Nec convenit aliquem presumere quod immediate recipit ordinem sacerdotalem a Deo, sicut fecerunt Moyses et apostoli, licet concedi debeat, quod taliter potest esse, quia sine revelacione sic presumere foret stulticia scandalosa; ymo videtur quod homo pocius pateretur symoniam prepositi, dicens tamen ordinanti periculum qui sic mercatur cum ministerio sacramenti, quam temere confideret in insensibili Dei ordinacione mundo abscondita.

[ENGLISH]

## ¶5 · 314.30–315.5

> [p. 314] In istis tamen illusionibus prelatorum propter manifestam et onerosam multitudinem inconveniencium oportet divinam iusticiam ipsas detegere et errores modo absconditos tempore suo destruere. Modo enim servatur ut evangelium, [p. 315] quod sint quinque ordines celebrati; in tempore autem apostoli non erant nisi duo ordines ad ordinacionem ecclesie, scilicet dyaconus et sacerdos, ut patet legenti epistolas Pauli, et meminit archidyaconus cum sanctis doctoribus.

[ENGLISH]

## ¶6 · 315.6–315.27

> [p. 315] Ex veteri vero et novo testamento debent esse septem ordines, ideo eleccio quinarii mediividetur figurare fidelibus quod primus numerus superbus scilicet quinarius facit nostros prepositos taliter variare. Sicut enim omnis christianus et specialiter bonus presbiter est sacerdos, sic est spiritualiter hostiarius, ceroferarius, lector, exorcista, subdyaconus, dyaconus et sacerdos, ut alias diffuse exposui. Et sic videtur quod ecclesia posset viare facilius, contenta de duobus ordinibus., in quibus residua spiritualiter includuntur. Nec obest, quod Augustinus dicit in libello suo De Heresibus, quod Heriani ab Herio quodam sunt dicti, qui, cum esset presbiter, doluit fortiter quod episcopus non potuit ordinari, et in Arrianorum heresim lapsus propria queque doctrinata addidisse, nonnulla dicens offerri pro dormientibus non oportere, nec statuta sollempniter celebranda esse ieiunia, sed cum quibus voluerit esse ieiunandum, ne videatur esse sub lege. Dicebat eciam presbiterum ab episcopo nulla differencia debere discerni.

[ENGLISH]

## ¶7 · 315.28–316.23

> [p. 315] In capitulo Herrii videntur michi esse Fratres, qui sumptuose, laboriose et periculose aquirunt episcopatus officia, ut seculariter voluptuose et ociose dimissa prius commendata obediencia conversentur. Non enim sonat directe ad utilitatem ecclesie vel religionis augmentum quod sic vivunt, quia per idem quilibet frater aptus ad regimen [p. 316] sic dissolveret claustrale vinculum. Sed iuxta principia fidei dimitteret dotacionem et conversacionem cesaream proficiendo subiectis episcopaliter, sicut fecerunt apostoli. Hoc enim plus congrueret professioni sue primeve. Sed iste sanctus dicit quod Herius doluit, quod episcopus non potuit ordinari, quia noluit esse sub lege; et sic incidit in istum errorem, quod presbiterum simplicem et episcopum non oportet discrimen per potestatem iurisdicionis atque scienciam, quia tunc iste Herius propter inhabilitatem ad officium episcopale pateretur repulsam. Sed absit logicum istud credere illud dictum Augustini repugnare decreto Jeronymi: Quod olim idem fuit episcopus et sacerdos, olim enim erant pauci episcopi atque ydonei, qui seclusi a seculo non propter mundum, sed propter Deum et amorem ecclesie curam pastoralis officii perfecerunt; et sic error esset hodie negare presbiterum ab episcopo nulla differencia discerni, cum multi presbiteri instructi in lege Domini vivunt sancte, et multi episcopi ignari legis Dei vivunt contrarie. Ideo necesse est esse differenciam sacerdotum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 312.1: It is objected that orders would be done away with.
- 312.8: This we deny.
- 312.23: It is not proved that Joan's acts as pope were invalid,
- 313.9: The sacraments would remain if there were no pope.
- 313.19: It would be good to get rid of the many bishops of Nowhere.
- 313.26: Sham priests and bishops.
- 314.14: Ordination by a simple priest may be sufficient.
- 315.1: In apostolic times there were only two orders: priests and deacons.
- 315.9: A good chrtstian has all orders.
- 315.28: Friars get bishopries with bad results.
- 316.16: Jerome's witness that bishop and priest were the same.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 312: *Hic* [R3]
  - 312: *Et* (20 is the line number) [R3]
  - 313: *intencione* [NW]
  - 314: *prelato* [R3]
  - 314: *∅* (by is the English side note (Ordination by a simple priest)) [R3]
  - 314: *Et* [R4]
  - 315: *esse* (25 is the line number) [R3]
  - 315: *videatur* [R4]
  - 316: *claustrale* [R5]
  - 313: *eis,* (LEFT-odd: print = printed; side-note word adjacent) [OVERRIDE-SCARPLATE]
  - 315: *specialiter* (LEFT-odd: box misplaced on variare; word is speci-|aliter with folio bar) [OVERRIDE-SCARPLATE]
  - 315: *doctrinata* (LEFT-nw: hyphenated doctri-|nata) [OVERRIDE-SCARPLATE]
  - 316: *Herius* (W2: capital H, italic) [OVERRIDE-SCARPLATE]
  - 316: *Herius* (LEFT-nw: capital H) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 312:
1. A in marg. : Tercio arguitur; ib. A in marg. : l, 2. 8. Codd. in
marg. : Omnes sancti christiani sunt sacerdotes. 23. Codd. in marg. :
Femina sacerdos papa.
ii. De Civit. Dei, lib. XX, cap. X, Opp. tom. VII, pag. 588.
20. I. Petr. II, q. 2i. Opp. tom. VI, 856.

p. 313:
29. Codd. in marg. : Nota hic. 3i. B in marg.: Vadentes curtam
Romanam pro sacerdocio. 32. A in marg. : Cave.
2. pag. 706 seqq.

p. 314:
4. A in marg. : Cave foveam. 34. B in marg. : Ordines clericorum
quinque.

p. 315:
18. A in marg. : Nota et tene.
18. Aeriani ab Aerio etc. Aug. Opp. tom. VIII, 18.

p. 316:
Codd. : clanstrare. 16. qni; B: quia. 25. Codd.: in marg. :
Papa cesarius si deest ecclesia sancta melius staret.
14. Decreti Prima Pars, Dist. XCV, cap. V.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 312: Sederunt sacerdotes Dei et Christi et regnabunt cum ipso mille annis; non utique de solis episcopis et presbiteris dictum est, | qui proprie iam vocantur in ecclesia sacerdotes, sed sicut omnes christianos dicimus propter misticum carisma, sic omues sacerdotes, quoniam membra sunt unius sacerdotis, de quibus apostolus Petrus ait: Plebs sancta, regale sacerdocium.
p. 313: continuatos corpori Christi dicit esse christianos;
p. 314: Cave foveam. quinque.
p. 315: Herio quodam sunt dicti, qui y cum esset presbiter y doluit | fortiter quod episcopus non potuit ordinari, et in Arrianorum heresim lapsus propria queque doctrinata addidisse, nonnulla dicens offerri pro dormientibus non oportere, nec statuta soltempniter celebranda esse ieiunia, sed cum quibus voluerit | esse ieiunandumj ne videatur esse sub lege. Dicebat eciam presbiternm ab episcopo nulla differencia debere discerni.
p. 316: Heritis doluit, quod episcopus non potuit ordinari, | olim idem fuit episcopus et sacerdos,
```
