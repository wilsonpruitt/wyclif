# Translation brief: potestate-pape 06-e–06-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-06-e.md chunks/potestate-pape/wyc-potestate-pape-06-f.md chunks/potestate-pape/wyc-potestate-pape-06-g.md` once and fix what it reports.
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

## Glossary (the 271 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |

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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| castra caynitica | Caim's castles | The friars' houses; the Wycliffite English name (CAIM = the four mendicant orders' initials). Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| metaphisica | metaphysics | *Inter omnes metaphisicas* → "among all the metaphysics": he counts the doctrine of the church as one (T. p. 368). Pilot. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| idiota | unlearned man | Not "idiot". Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| brocardicum / brogardicum | brocard | The schoolmen's stock maxim. Ruled 2026-10-02 (*Eccl.* 16, 360.9). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| exequie | exequies | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| negociatores | dealers | Kept apart from *mercantes* "traders" (*Eccl.*); the servants of the talents parable (Matt. 25). Ruled 2026-10-07 (*Pot. pape* 101.7). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 06-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "118.6–122.29"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 5 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1026 words; 978 unanimous or majority-real; 29 settled by vote (R2 16, R3a 4, R5a 8, R6a 1); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n179–n183 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 5: [TITLE]

## ¶1 · 118.6–119.6

> [p. 118] Octava sentencia est: Romano pontifice vel quocumque alio fingente se gerere primatum vicarie potestatis Christi in terris, ab eius semita declinante secundum sensum scripture nullus plenius vel periculosius gerit de facto nomen et opera Antichristi. Pro declaracione istius sentencie notandum est primo secundum modum loquendi scripture: Quod quicumque est Christo vel legi sue contrarius, dicitur Antichristus, et concordat literalis composicio, cum Antichristus dicitur ab anti, quod est contra, et Christus quasi contra Christum. Et isto modo loquitur Evangelista in prima epistola sua canonica II cap. 18: Et sicut audistis, inquit, quia Antichristus venit, nunc Antichristi multi facti sunt. Et illos vocat Christus Matth. XXIV cap. Pseudochristos a pseudo quod latine dicitur falsus vel decipiens, et sic quilibet dyabolus vel membrum eius est realiter antichristus. Unde videtur michi illos esse culpandos qui preter auctoritatem scripture sompniant quod de tribu Dan in illo loco cum equis et curru igneis et ceteris ficticiis dominabitur Antichristus. Doctores autem qui sic loquuntur vel ad modum loquendi propheticum loquuntur mistice vel videntur ad modum concionatoris fingere. Certum est itaque quod persona prescitorum aggregata, est unus Antichristus, sicut quotlibet membrum eius, et illius erit unus capitalis in malicia plus [p. 119] accensus; ymo videtur predestinatum, dum crimine fuerit Christo contrarius, dici posse realiter Antichristum, modo quo ille qui dixit et facta sunt Mat. XVI propter adversacionem nominat Petrum sathanam. Est igitur christiano necessarium cognoscere Antichristum.

[ENGLISH]

## ¶2 · 119.7–119.30

> [p. 119] Secundo notandum, quod de clero necesse est Antichristum trahere suam originem; cum enim non omnes sacerdotes confirmati sunt, necesse est quod aliqui propter status excellenciam cadant profundius. Sic magnus Antichristus fuit Lucifer cum suis complicibus, sic magnus Antichristus fuit Scarioth cum avaris suis sequentibus, et ita de generacione nequam, que processit Cayn usque ad novissimum reprobandum, unde beatus Evangelista II epistola canonica concedit, quod multi seductores exierunt in mundum, qui non confitentur Jhesum Christum venisse in carne; hic est seductor et antichristus, unde prima epistola IV, cap.: Multi pseudoprophete exierunt in mundum; et sequitur eorum descripcio Omnis spiritus qui solverit Jhesum ex Deo non est, et hic est Antichristus de quo audistis quoniam venit, et declarat quod ille Antichristus sit mundo deditus et de clero prodiit. Cui conformiter loquitur Christus Matth. XXIV, 5: Multi, inquit, venient in nomine meo, dicentes quia ego sum Christus, et multos seducent, et illos nominat posterius Pseudochristos. Ex quibus videtur quod surgent de clero.

[ENGLISH]

## ¶3 · 119.31–121.9

> [p. 119] Et concordat racio cum antichristus peccato gravissimo et magis subdolo erit Christo contrarius. Sed illud peccatum oportet esse traditoriam [p. 120] ypocrisim, quia illam scit dyabolus magis efficere, et simplices propter velamentum eam minus percipere. Et ad istum sensum vadunt verba Apostoli II epistola ad Thym., II Petri epistola, et epistola Jude cum aliis dictis propheticis, quia indubie talis est apcius instrumentum dyaboli ad simplices seducendum. Quando enim dyabolus videt constantem dileccionem Christi in laycis et cum pietate ceca ignoranciam legis Christi, ex alioque latere avariciam Scariothis in clero, non est sibi placencius crimen propter ingratitudinis et duplicitatis gravedinem, quam seducere christianos in propriis instrumentis; sic enim victus est a Christo. Unde sine assercione ymaginor tercio quod sit unus nominetenus papa pseudonomine, cui iste XI condiciones insint ex instinctu patris mendacii. Primo quod ubi est Christus veritas Joh. XIV, Pseudo ubique innititur mendacio, quod notum est esse contrarium veritati, innititur, inquam, mendacio in verbis, in scriptis et vita, dicendo se propinquissime sequi Christum tamquam eius ndelem vicarium, dum tamen sit ab eo in moribus maxime elongatus, aliter enim non palliaret seducendo populum, quomodo veniret in nomine crucifixi, ut Christus prophetavit Matth. XXIV et Joh. XV. Secundo, ubi Christus regularissime tenuit summam pauperiem, iste Pseudo irregulariter summe seculo innititur; aliter enim non esset de mundo, sed ex Deo, qui per pauperiem vicit mundum, ut prophetatum est I Joh. II et Joh. [p. 121] XVII, cum enim sibi desunt miracula et vite sanctitas; aliter valde pauci suo disciplinatui iungerentur. Modo autem ex instinctu dyaboli totus mundus est mundo deditus, sic ubi Christus renuit oblacione dyaboli omnia regna mundi, ut dicitur Matth. IV, iste Pseudo dicit maniace quod dominetur capitaliter super tota habitabili et per eius licenciam et pacienciam singuli reges regnant.

[ENGLISH]

## ¶4 · 121.10–121.28

> [p. 121] Tercio, ubi Christus anathemate gravi prohibuit quod non adderetur aliquid impertinens legi sue, ut patet Gal. primo et sepe alibi, iste Pseudo fabricat leges novas, que nusquam reperiuntur in scriptura sacra; in qua secundum Augustinum est omnis veritas, sed sunt legi Christi latenter contrarie. Nec mirum quia sacerdos et propheta paulative declinantes a lege Domini preposituram talis legiferi meruerunt, ut prophetatum est Psalmo IX, 21. Ubi propheta de Antichristo loquens secundum exposicionem sanctorum: Constitue, inquit, legislatorem super eos. Et istam legis translacionem oportet sequi extraneum sacerdotem, quia Heb. VII, 12 dicit Apostolus, quod translato sacerdocio necesse est ut legis translacio fiat. Et iste triplex funiculus, scilicet commentum mendacii, commentum favoris seculi et commentum tradicionis inique sunt basis tocius retis dyaboli.

[ENGLISH]

## ¶5 · 121.29–122.3

> [p. 121] Quarto, ubi Christus elegit discipulos simplices idiotas, mundo pauperes et introitu ad suam religionem fecit plus pauperes, ut patet Matth. XIX; iste Pseudo eligit sibi plus inclitos, callidos et astutos, et prius mundo abiectos elevat m falsos dominos urbis et orbis. Aliter enim foret discipulus magistro nimis dissimilis et ex contrarietate [p. 122] foret societas desoluta, quia Ecclesiastici XIII, 3 scribitur: Quid communicabit cacabus ad ollam? quando enim se colliserint confringetur.

[ENGLISH]

## ¶6 · 122.4–122.16

> [p. 122] Quinto, ubi Christus precepit suis discipulis ire in mundum universum et predicare indifferenter evangelium docereque omnes gentes servare quecumque eis mandaverat, ut patet Matth. ultimo, iste Pseudo docet et care conducit suos discipulos modo contrario servare oppositum, cum ipse residens in sumptuoso palacio constructo de bonis pauperum, ut alter Cosdroe, nulli predicat et discipulos tales optat, qui in castris conquestis mutescendo resideant nisi forte superbe, blasfeme, eciam scandalose in verba de potestate sua proruperint. Et istarum scolarum promulgata contrarietas confundit seculum.

[ENGLISH]

## ¶7 · 122.18–122.29

> [p. 122] Sexto, ubi docuit Christus suos discipulos possidere et servare vitas suas quietas atque perpetuas in paciendo tribulaciones atque iniurias, ut patet Matth. V et Luce XXI, iste Pseudo docet verbo et opere suos discipulos ex immensitate sue dignitatis quoscumque eis contrarios debellare, quia aliter paulative periret ab eis dominium; et sic sunt in capitulo impiorum, de quibus Sapiencie II, 1 scribitur: Dixerunt impii cogitantes apud se non recte: Exiguum et cum tedio est tempus vite nostre, non est refrigerium in fine hominis, et cetera que sequuntur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 118.6: A pontiff who claims to be Christ's Vicar while leaving his way is the worst of Antichrists.
- 118.29: The whole body of the reprobate are Antichrist; so is each of its members.
- 119.7: Antichrist must originate from the clergy.
- 119.31: The special sin of Antichrist is hypocrisy.
- 120.13: A man may be a pope in name, yet have the conditions of Antichrist.
- 120.21: 1. He says he is a follower of Christ, yet goes and leads others astray.
- 120.27: 2. He does not imitate Christ in his poverty,
- 121.1: but claims rule over the whole world.
- 121.10: 3. Against Christ's prohibition he makes new laws not founded in Scripture.
- 121.29: Christ chose poor simple men for his disciples; the pope chooses such as are illustrious or astute.
- 122.4: 5. Christ bade his disciples to go out through the world preaching; the false pope dwells in a rich palace and does not preach.
- 122.18: 6. Christ taught his disciples to submit to persecution; the pope teaches his to fight for dominion.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 118: *literalis* [NW]
  - 118: *18* [R3]
  - 119: *carne* [R3]
  - 119: *traditoriam* (hyphenated tradi-toriam; main token covers whole word) [R5]
  - 120: *placencius* [NW]
  - 120: *vicarium* (print has v; 190d is the folio mark) [R3]
  - 120: *∅* (English side-note word) [R6]
  - 121: *21* [R3]
  - 121: *12* (print has Heb. VII, 12 before dicit) [INS?]
  - 121: *iste Pseudo* (one token covers two printed words) [THIN]
  - 121: *eligit* [THIN]
  - 121: *discipulus* (35 is the line number) [R4]
  - 122: *cacabus* [NW]
  - 122: *de* (25 is the line number) [R3]
  - 122: *1* (old-style 1, x-height) [R3]
  - 122: *recte* [R3]
  - 122: *vite* (print has v) [R4]
  - 122: *refrigerium* [R4]
  - 120: *nominetenus* (W1: nommetenus -> nominetenus (scans: nommetenus | nommetenus | nominetenus | nommetenus)) [OVERRIDE-SCAR]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 118:
6. AB in marg. : Antichristus quis est secundum scripturam. 16. B
inmarg. : Anti valet contra. 24. Ainmarg. : De Antichristo. 27. AB
in marg. : De Antichrislo.

p. 119:
1. A in marg. : Nota contradicit sibi de ecclesia. 7. A in marg.:
Antichristus ex clero.
7. Cf. Wyclif, De Antichristo = Op. Ev. III, 6.

p. 120:
16. AB in marg. : Antichristi condiciones. 17. AB in marg. : 1.
18 et 20. Codd.: innitatur. il.tamen; A : tantum. 27. AB in marg.: 2.
16. De Condicionibus Antichristi in plurimis operibus Johannis
Wyclif tractatur. Conferas e. g. Opus evangelicum III, IV, 106,
1 35/6. De Christo et suo adversario Antichristo cap. XI. Pol.
Works II. 680. Sed sunt ibi duodecim condiciones.

p. 121:
G. Codd.: dicat. 10. AB in marg.: j. 20. Codd.: supositum.

p. 122:
3. Codd.: colliderint; ib. 13: refringentur ; A: confringentur. 4. AB
in marg. : 5. 11. B: Cosdree. i5. Codd. : proi -umperint. 18. AB in
marg. : 6. 3o. A in marg. : 7.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 121: legislatorem super eos. | translato \ sacerdocio necesse est ut legis translacio fiat. | ^ rT Sr
p. 122: Qnid communicabit cacdbus ad ollam? quando enim se colliserint confringetur. | Dixerunt impii cogitantes apud se non recte: Exiguum et cum tedio est tempus vite nostre, non est refrigerium in fine kominis,
```

---

## Chunk 06-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "122.30–125.31"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 6 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "683 words; 645 unanimous or majority-real; 29 settled by vote (DEL 1, R2 16, R3a 11, R5a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n183–n186 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 6: [TITLE]

## ¶1 · 122.30–123.8

> [p. 122] Septimo, ubi Christus prohibet suis ferire cum gladio sed pati ut ipse, cum potuit hostes suos faciliter superare; ut patet Joh. XVIII, iste Pseudo docet et conducit milites de bonis pauperum [p. 123] ad cumulandum sibi superfluitates stercorum et discipulos suos, qui severius exequuntur illud officium, plus commendat et promovet ad seculi dignitatem, sic quod Christo conversante nobiscum non foret suis cum illis societas vel amicicia nisi inter homines prope pares, Et secundum Apostolum II Cor. VI, 15 non est communicacio Christi ad Belial, ut tangebam superius.

[ENGLISH]

## ¶2 · 123.9–123.20

> [p. 123] Octavo, ubi Christus prohibuit cariores eius discipulos Jacobum et Johannem inprecari ignem de celo descendere instar Helye, IV Reg primo ad vindicandum de Samaritanis negantibus eis necessaria, cibum et tegumina, ut patetLuce IX, 56, iste Pseudo deficiente materiali gladio fingit fulmen anathematis in eos, qui nolunt sue tyrannidi obedire, sic quod ubi Christus dicit suos discipulos esse spirituales nulli obnoxios, cum ipse non venit animas perdere sed salvare, ut ibi dicitur, iste Pseudo pro nichilo perdit utramque vitam multiplicium animarum.

[ENGLISH]

## ¶3 · 123.21–124.7

> [p. 123] Nono, ubi Christus dicit in suo Apostolo prima Cor. VI, 7 quod omnino est delictum in gentibus, quod iudicia secularia sic exercent, cum ipse renuit tale iudicium, ut patet Luce XII, iste Pseudo hortatur viis et modis scolares suos contendere, dicens quod condidit multiplices leges sacras ecclesie et ordinavit satrapas ad complementum talis iusticie; ideo sicut excomunicantur qui impediunt pugiles ecclesie, qui volunt exequi eius iura, sic excomunicantur iniuriati in paciendo iniurias, cum ob torporem eorum leges et possessiones ecclesie sunt extincte. Unde Apostolus dicens: Quare non magis iniuriam patimini? per [p. 124] antiphrasim locutus est yronice, sicut quando dicit quod talia debent per contemptibiles ecclesie iudicari, et sic ubi Christus cum sua familia suspensus fuit a talibus intendens pure saluti anime, iste Pseudo cum sua familia trahit sibi omnia secularia negocia, gracia congregandi pecunie.

[ENGLISH]

## ¶4 · 124.8–124.34

> [p. 124] Decimo, ubi Christus ostendit humiliter suam inferioritatem celans sub testa humanitatis suam divinitatem, ut patet Joh. XIV et alibi sepe in evangelio, iste Pseudo proclamat pompatice et blasfeme quod est Deus mixtus vel Deus in terris, quem nemo debet corripere, cum habens omnes leges in scrinio pectoris, debet ad votum scripturam autorizare, exponere vel quantum libuerit abrogare, et sic propter iniustam pene gravedinem periculosius est in mandatum suum quam in mandatum Christi offendere, cum potest declarare quoscumque sibi contradicentes, licet pure asserentes fidem scripture, esse hereticos, cum pure ex bullis suis ad votum habilitat et inhabilitat quemcumque voluerit, ymo eo ipso quo pretendit se quovis modo solvere vel ligare, eo ipso sic solvit vel ligat. Et ipse supra Christum habet plenam potestatem civiliter dominandi, et sic de infinitis blasfemiis, ex quibus infertur prophecia Apostoli II. Tess. II, 3 de Antichristo dicta quem hominem peccati nominant, ita ut in templo Dei sedeat, ostendens se tamquam sit Deus, ymo ut dicit Apostolus, extollitur super omne quod dicitur Deus. Deus enim non potest taliter dominari nec nude per bullas sine interiori illapsu quemquam habilitare, nec potestatem preter Dei licenciam ab imperatore capere.

[ENGLISH]

## ¶5 · 125.1–125.31

> [p. 125] Undecimo et ultimo patet quod Christus abnuit omnem sentenciam, in qua necesse foret facere alicui iniuriam, ideo Luce XII, 14 dicit cuidam petenti eius iudicium: Quis me constituit iudicem aut diuisorem super vos? Unde et eius apostoli abalienati sunt a divisione cuiuscumque prepositure, que lucrum temporale sapiunt, quia didicerant a magistro Matth. X, 8: Gratis accepistis gratis date. Iste autem Pseudo cum discipulis suis palliat, quod ad eum solum spectat in solidum, omnes preposituras sapientes pinguedinem temporalem tribuere; nec potest propter plenitudinem potestatis symoniam committere, sed propter plenitudinem dominii oportet quemcumque secundum pinguedinem sui beneficii de thesauro Pseudo afferre; et de plenitudine potestatis facit reservaciones mentales absconditas, et virtute earum plus offerens preponetur, cum potest anteriorare vel posteriorare tempus ad libitum, ymo non obstante quod Christus sit cum suis apostolis omnibus diebus usque ad consumacionem seculi, ut dicit Matth. ultimo, iste tamen Pseudo potest dispensando tempus redimere et mutare, sic quod quando est maxime necessarium Christo et sue ecclesie consilia Christi servare, liceat sibi consilia ipsa suspendere, privilegia quecumque propter questum concedere, et quantumcumque Christo inhabiles tamquam habiles approbare, et quicquid fecerit debet tota militans ecclesia, quam oportet esse sub dicione ut legem Christi ratum credere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 122.30: 7. Christ forbade his disciples to take the sword;
- 123.1: the pope uses the spoils of the poor to hire soldiers,
- 123.9: Christ would not call down fire on the Samaritans; the pope curses all who do not obey him.
- 123.21: 9. Christ refused to be a judge; the pope is always grasping at jurisdiction.
- 124.8: 10. Christ humbly hid his deity under cover of his manhood; the pope claims to be God in earth,
- 124.28: and fulfils St. Paul's prophecy of the man of sin.
- 125.1: Christ's disciples made no money by prelacies, the pope makes all appointments a matter of gain.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 124: *inferioritatem* [THIN]
  - 124: *celans* [THIN]
  - 124: *Joh* [R4]
  - 124: *pene* [R3]
  - 125: *∅* (box is the folio bar before nec (192a)) [R4]
  - 125: *ecclesia* (30 is the line number) [R4]
  - 123: *inter homines* (W-split: interhomines -> inter homines (two words run together)) [OVERRIDE-SCAR]
  - 125: *spectat in* (W-split: spectatin -> spectat in (two words run together)) [OVERRIDE-SCAR]
  - 123: *fulmen* (LEFT-nw: 15 is the line number) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 33.1. Cor. VI, 7. (123.33); reference 28. II. Thess. II, 4. (124.34); reference 22. Matth. V, 20. (125.34).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 122:
3. Codd.: colliderint; ib. 13: refringentur ; A: confringentur. 4. AB
in marg. : 5. 11. B: Cosdree. i5. Codd. : proi -umperint. 18. AB in
marg. : 6. 3o. A in marg. : 7.

p. 123:
5. sui in codd. 9. AB in marg. : 8. 21. AB in marg. : 9.

p. 124:
(none)

p. 125:
I. AB in marg. : 11. 32. Multe; codd. : materie.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 122: Qnid communicabit cacdbus ad ollam? quando enim se colliserint confringetur. | Dixerunt impii cogitantes apud se non recte: Exiguum et cum tedio est tempus vite nostre, non est refrigerium in fine kominis,
p. 123: non est communicado Christi ad Belial, | ipse non venit animas perdere sed salvare, | omnino est delictum | iudicia \ secularia sic exercent, | Quare non magis iniuriam patimini?
p. 124: hominem peccati | in templo Dei sedeat, ostendens se tamquam sit Deus, | extollitur super | omne quod dicitur Deus.
p. 125: Quis me constituit iudicem | aut diuisorem super vos? | Gratis accepistis gratis date. | Christus sit cum suis apostolis omnibus diebus usque ad consumacionem seculi,
```

---

## Chunk 06-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "125.32–129.31"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 7 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "874 words; 820 unanimous or majority-real; 43 settled by vote (DEL 1, R2 31, R3a 10, R5a 1); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n186–n190 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 7: [TITLE]

## ¶1 · 125.32–127.31

> [p. 125] Multe sunt versucie velate sub istis XI, in quibus falluntur simplices versuciis Pseudochristi, et indubie quicumque fuerit talis Pseudo vel ei [p. 126] consenciens est secundum quod plus vel minus istis condicionibus participat Antichristus. Ideo docet beatus Evangelista epistola sua canonica; postquam Antichristum descripserit: Nolite, inquit, eum recipere in domum vestram, nec ave ei dixeritis; quod oportet intelligi nec in persona sua propria nec in membris, qui, inquit; dixerit illi ave, communicabit operibus eius malignis, et iste si est talis est heresiarcha solvens Christum infideliter in naturis persone, in Christi legibus et in membris, cuius scolam oportet cordatos theologos affeccione donorum suorum et timore suorum supplicacionum postpositis animose detegere. Et ipsum describunt omnes libri sapienciales vel prophetici alterius testamenti; et propter nostrorum vecordiam et membrorum suorum crescenciam in brevi tempore magis invaluit. Nec dubium quin sit infidelis Christo, qui aliquo quinque modorum consentit homini contra Christum. Sunt autem multa sophistica quibus homo iste illudit simplicibus christianis; dicitur enim primo quod status cleri sui est infinitum perfeccior quam status aliquis laycalis, ideo non pertinet ipsos de statu cleri cognoscere. Dicit secundo palpatus in metaphisica quod omnis status hominis est realiter ipse homo. Contra utrumque istorum invexi sepius: contra primum est decretum Crysostomi Imperfecto Omelia 26; ubi docet; quod homo debet iudicare de operibus manifestis, quia aliter precluderet lex Christi naturale iudicium et foret sibi ipsi contraria, [p. 127] cum ipsemet docet Matth. VII, 15 attendere a falsis prophetis ex fructibus cognoscendis, aliter enim necessario cecaret laycos ad elemosinas suas Antichristi discipulis improvide parciendum. Contra secundum patet quodrepugnat priori, cum tunc omnis clericus foret infinitum perfeccior quam laycus; quod soli Christo potest competere; iterum omnis homo vel angelus maneret continue in eodem statu, sicut manet constanter in eadem humanitate, et sic nullus status posset maius aut minus suscipere. Et iterum periret status et christianorum distinccio, ymo propter casum Luciferi non foret status angelorum deterior, nisi forte dicatur quod status sit qualitas anime vel peccatum. Ideo certum est quod status iuxta methaphisicam scripture verissimam est denominacio, qua natura racionalis dicitur formaliter stare respectu finis ultimi, et sic in homine aliquis est status corporis, aliquis status anime et aliquis mixtum; aliquis eciam est status quoad mores et aliquis quoad ritus vel religionem, aliquis totalis et aliquis parcialis. Unde de statu corporali et statu mentali racionali vel integra individua potest intelligi illud Yob. XIII quod homo miserabilior lapsus nunquam in eodem statu permanet continue, nam secundum statum integrum variatur, ut patet de etate, de morum varietate et de circumstanciis statum integrantibus, que communiter variantur; manet tamen idem status communis et individuis successivis intercisus vel continuus.

[ENGLISH]

## ¶2 · 127.32–129.3

> [p. 127] Ex istis logici sollicitant se quod continuum componitur ex non quantis, cum status continuus sicut etas per indivisibile vel duo aut quotlibet [p. 128] indivisibilia excedit aliud, nam P. superstes, qui incepit cum Paulo nunc desinente est per instans antiquior quam fuit Paulus vel ipse; nec est possibile unum continuum per indivisibile excedere aliud nisi indivisibile faciens ad maioritatem eius sit pars talis maioris, ut est in numeris. Et sic potest argui de statu sanitatis vel infirmitatis, de quo quis meritorie continue elicit actum caritatis, gaudendo et laudando Deum de statu; et patet quod actus terminatur exclusive ad instans ut sanitas vel infirmitas, et (ut videtur) est continue novus actus, sicut continue novum obiectum, ad quod actus essencialiter terminatur. Et ita videtur quod captis duobus predestinatis, quorum primi meritum terminetur exclusive ad septimum gradum, et secundi totale meritum terminetur inclusive ad eundem gradum, status primum in patria correspondenter se habebunt; nec negabitur antecedens, cum stat de duobus predestinatis unum exclusive et alium inclusive incipere mereri ab eodem instanti. Postquam originaliter peccando continue antefuerant in mortali et continue equaliter merendo pro eodem instanti decedant. Constat quidem quod actuum merendi aliquis est successivus, cuius incepcio est per remocionem de presenti, et aliquis per posicionem de presenti. Sic enim Christus potuit incipere purgasse Baptistam ab originali pro primo instanti sui esse, et alium communem sibi et aliunde undique parem creasse in gracia et beatificasse eos correspondenter ad merita, et sic de mille casibus possibilibus et de facto in quibus implicatur unum quantum excedere aliud per indivisibile. Ex quibus oportet concedere aliquam esse maximam partem quantitativam, [p. 129] eius parem excesso, et adiectum cum facit quantitative totum maius, oportet esse partem quantitativam maiorati per ipsum.

[ENGLISH]

## ¶3 · 129.4–129.31

> [p. 129] Istam materiam diffuse prosecutus sum alibi cum alus dubiis annexis, ideo transeo dictum repetens superius, quod status exproprietarie vivendi est quocumque statu civili perfeccior, sicut status virginitatis est quocumque statu coniugati perfeccior, natura angelica est naturaliter natura humana superior, vita contemplativa est vita activa perfeccior et sexus femineus est sexu masculino fragilior; et tamen constat quod multi coniugati sunt multis virginibus meliores, multi homines superiores dyabolis gracia non natura, multi activi sunt multis contemplativis sancciores, et multe femine virgines in iuvenili etate multis viris eciam decrepitis plus constantes, ut sepe meminit Augustinus in scriptis istius materie. Ideo necesse est volentem istam materiam intelligere considerare perfeccionem quam habet homo in quantum exproprietarie vivit, et perfeccionem quam habet in quantum civilis proprietarius, et illarum perfeccionum quas voco perfecciones simpliciter supra perfecciones individuas, primam inveniet plus perfectam. Ille autem perfecciones more universalium non possunt augmentari vel minui, sed perfecciones vel status individui secundum quod illis alia commoda sunt adiecta, et sic, ut sepe repecii, status exproprietarie vivendi propter excellenciam perfeccionis, congruit clero Christi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 126.21: The pope says that the clerical state is more perfect than the lay and that the laity have no right to judge the clergy. He says too that the man and his state are one.
- 126.28: A man may and must judge of deeds open and visible.
- 127.5: If the man and his state are one every cleric is infinitely more perfect than any layman. Moreover the state of every man and angel would be unchangeable.
- 129.4: The state of being without property is, as a State, better than that of a civil owner.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 126: *∅* (English side-note word) [R4]
  - 127: *VII* [R5]
  - 127: *attendere* [R3]
  - 127: *cum* (English side-note glued) [R4]
  - 127: *in* [R3]
  - 127: *minus* [R4]
  - 127: *Et* [R3]
  - 127: *corporali* [R4]
  - 128: *incepcio* (25 is the line number) [R4]
  - 127: *methaphisicam* (LEFT-nw: metha- | phisicam across lines; whole word per main-scan token) [OVERRIDE-SCARPLATE]
  - 129: *exproprietarie* (S-split: one word, no split) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 22. Matth. V, 20. (125.34).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 125:
I. AB in marg. : 11. 32. Multe; codd. : materie.

p. 126:
8. Codd.: ille. 18. 13: infideles. 25. AB in marg. : Judicare de
prelatis.
4. 2. Joh. 10. 3o. Opp. tom. VI, 743 (?) Cf. In Matth. Hom.
XXIII Opp. tom. VII, 3o7.

p. 127:
5. Codd.^ tercium. 11. Godd.: statns christianorum. i5. AB in
marg. : Status hominis quid est. 3o. intricisus in codd. 32. B in

p. 128:
I. II. codd. 6. numeris. Cod.: m'us. 7. B in marg. : Casus notabilis.

p. 129:
4. AB in marg.: Status diversi secundum gradus. 12. B: et tantum.
26. B in marg. : Perfecciones in aniversali non augentur sed in singulari.
32. AB in marg. : Status exproprietarius approbatur a tota Trinitate.
De Potestate Pape. 9
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 125: Quis me constituit iudicem | aut diuisorem super vos? | Gratis accepistis gratis date. | Christus sit cum suis apostolis omnibus diebus usque ad consumacionem seculi,
p. 126: eum recipere in domum vestram, nec ave | ei dixeritis; | dixerit illi ave, communicabit \ operibus eius malignis, | homo debet iudicare | de operibus manifestis, quia aliter precluderet lex Christi naturale iudicium et foret sibi ipsi con-
p. 127: a falsis prophetis ex fructibus cognosccndis,
```
