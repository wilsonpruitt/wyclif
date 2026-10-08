# Translation brief: potestate-pape 08-c–08-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-08-c.md chunks/potestate-pape/wyc-potestate-pape-08-d.md chunks/potestate-pape/wyc-potestate-pape-08-e.md` once and fix what it reports.
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

## Glossary (the 245 rows these chunks use; the full file is GLOSSARY.md)

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
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| franchisia | franchise | Ruled 2026-10-02 (*Eccl.* 239.22). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| laureola | aureole | The theologians' special crown (of virgins, martyrs, doctors). Ruled 2026-10-02. |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| exequie | exequies | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| coraula | choir-leader | Ruled 2026-10-07 (*Pot. pape* 92.17). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 08-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "173.33–176.4"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "490 words; 459 unanimous or majority-real; 28 settled by vote (DEL 1, R2 12, R3a 5, R5a 10); 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n234–n237 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 3: [TITLE]

## ¶1 · 173.33–174.11

> [p. 173] Item, quicumque superstes dat alteri potestatem solum dat sibi potestatem vicariam et non parem, [p. 174] igitur ex hoc quod Petrus instituit Clementem Rome pontificem, non sequitur successorem suum fuisse summum pontificem sicut Petrus. Nec valet ficticia, qua dicitur quod Petrus Rome obiit, ideo successor suus ibidem debuit esse papa. Nam Christus papa summus obiit Jerusolimis et tamen Jacobus Alphei tenens ibidem episcopatum a Christo datum et ibi obiens non propterea fuit papa. Que igitur liga Petri ad Clementem pocius quam Christus ad Jacobum, ut episcopus succedens loco quo obiit foret papa?

[ENGLISH]

## ¶2 · 174.12–176.4

> [p. 174] Item, non subiacet humane potestati sed solum divine constituere quemquam summum pontificem, igitur non debet supponi in Petro tanta presumpcio, ut eligat hominem de quo non fuit sibi ad hoc facta revelacio in summum pontificem et immediatum Christi vicarium super terram, specialiter cum super ista fatuitate, non relinquitur nobis scriptum autenticum, sed in eleccione Mathie reliquit hoc divine iudicio, ut patet Actuum primo; quanto plus in eleccione maioris. Quis, inquam, crederet quod Petrus diffiniret beatum Clementem sequi Christum similius quam Evangelistam, qui diu vixit post Petrum, vel beatum Evangelistam debere Clementi ut maiori? vel capiti necessario regulandi obedienciam et reverenciam, qualem pape iam exigunt a subiectis. vel quod Christus aut alius apostolus talem maioritatem instituit, vel policiam in sua ecclesia approbavit? Voluit enim omnes apostolos esse socios sibi invicem obedientes et servientes sine dominio vel magisterio alicuius capitanei preter Christum. Et ex istis infirmatur tercia ficticia quod per viam eleccionis et institucionis humane ponitur [p. 175] quis Romanus et summus pontifex. Et quamvis ista sentencia sit maxime propinqua facto, tamen nimis elongatur a religione fideli et stabili fundamento. Cum enim aliquem stat esse Romanum pontificem et non papam et econtra, ut patet in Christo et Petro, patet quod oportet istas duas elecciones esse racionis disparis et nature ordine separatas. Stat enim aliquem esse Romanum pontificem et pessimum Antichristum, sicut econtra stat aliquem esse summum pontificem, cum hoc quod sit loco illi indifferens, ut patet ex dictis. Unde dominus Ardmacanus libro VII, cap. XVIII De Questionibus Armenorum dicit quod sunt duo pontificatus naturaliter differentes, et oportet quodsint eciam apud Deum due elecciones. Sed videtur michi quod eleccio qua quis eligeretur in papam vel summum pontificem non subiacet potestati vel eleccioni humane. Nam idem est hominem eligere in papam vel summum pontificem et eligere ipsum in apostolicum maxime propinque per graciam sequentem Christi vestigia; sed hoc non subiacet ordinacioni vel eleccioni humane, igitur nec aliud sive idem; sic enim eligeret quis hominem in predestinatum vel quocumque aliter graciosum. Et confirmatur ex factis et verbis apostolorum Act. I in eleccione Mathie apostoli, quod est minus quam eligere summum pontificem, ubi ipsi non eligunt sed rogant Deum; ut ostendat ipse quem elegerit. Sicut igitur electores non eligunt summum pontificem in eligendo alterum Scarioth vel Antichristum; sic casualiter eligendo eum quem Deus elegerit non [p. 176] eligunt talem in summum pontificem, sed in fungentem tali officio, quod non dicit excellenciam gracie vel alia carismata, que sunt propria dona Dei.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 174.2: Nor does Clement's succession to the bishopric carry the papacy.
- 174.8: Why Clement rather than James?
- 174.12: Peter would not presume to choose Christ's vicar without a revelation,
- 174.24: Was John the Evangelist subject to Clement?
- 174.33: That the pope is such
- 175.1: by human election is true to fact but lacks religious sanction.
- 175.15: Man cannot choose a pope truly,
- 175.21: since it depends on grace which man cannot judge.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 174: *∅* (folio bar (204c) read as i; not text) [INS?]
  - 174: *beatum* [R4]
  - 175: *propinqua* [NW]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Peter would (174.12).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 173:
7. AB in marg. : Dotacionem et loci appropriacionem qitare apostoli
fugiemnt. 20. Codd.: apostoli. 21. Codd.: ficticium.

p. 174:
6, 7. A -. et tantum 22. A in marg.: Nota tempore apostolorum et
evangelistarum Clemens a Petro eligitur, ergo non secundum sanctitatem

p. 175:
4. AB in marg. : Romanum poyitijicem stat esse et Jion esse papam.
12. Cod.: Cap. XIX. AB in marg. : Eleccio pon'(ficis summi non subiacet
eleccioni humane. 29. AB in marg. : Eleccio pontificis secundum repu-
tacionem hominum.
i3. Loosely quoted.

p. 176:
2. dicit. Rectius: dat. 14. B: fit iuste. 28 AB in marg.: Aliud
est eligere hominem in papam et aliud eligere papam.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 08-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "176.5–180.32"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1067 words; 993 unanimous or majority-real; 61 settled by vote (DEL 3, INS 1, R2 29, R3a 11, R5a 15, R6a 2); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n237–n241 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 4: [TITLE]

## ¶1 · 176.5–178.16

> [p. 176] Unde post dotacionem sunt elecciones hominum introducte et cadunt super officio, dignitate vel dominacione humanitus instituta et non super carismata Deo propria. Ut communitas eligit hominem in pontificem cesareum vel nuncupative dictum, et sic cadit eleccio humana super episcopum, ut dicit communiter episcopum secundum reputacionem vel approbacionem humanam, quod fit sepius cum errore, vel secundum autorizacionem divinam, quod semper sit iuste, unde quando contingit quod eleccio humana concordat cum eleccione divina, tunc homo eligit verum episcopum et summum pontificem, sicut sepe contigit de Romanis pontificibus veris papis. Et quando discordat ab eleccione divina, tunc eligit false reputatum summum pontificem et non summum pontificem, licet errando illud crediderit. Unde cum iste terminus papa et summum dicunt summitatem in moribus, quam mirabilitatem solius Dei est facere, videtur quod solus Deus eligit hominem in papam vel summum pontificem, quia non videtur fundabile quod isti termini extendantur ad false nuncupatum huius, quia sic dyabolus foret summus pontifex. Episcopus autem secundum apostolum est nomen officii et sic aliud est eligere papam et aliud eligere hominem in papam, quia secunda proposicio implicat quod cadat eleccio in papatum, sed prima proposicio verificaretur de eleccione persone ad quodcumque officium vel preposituram, ut populus eligit [p. 177] papam, quando instituit vel acceptat personam ad officium vel dignitatem humanam, quam personam Deus eligit ad preeminenciam sanctitatis, unde, cum scriptura Deutro. XXVI, 17 signanter dicit: Dominum elegisti hodie, patet quod quedam eleccio est institucio vel quedam faccio, et quedam eleccio est acceptacio; et per consequens oportet preter eleccionem instituencium esse eleccionem equivocam, que sit approbacio subditorum. Sic enim populus eligit dominum, quando effectualiter acceptat, quod ille sit dominus suus et spondet fideliter se esse sibi ut domino serviturum. Unde quando successione hereditaria vadit dominium, adhuc est alia eleccio subditorum; ad quod oportet movere vitam et mores in spirituali preposito, et aliter est intrusoris monstruosa extorsio. Et patet quod debet esse pape duplex eleccio, una humana in Romanum episcopum et alia pure divina in papam vel summum pontificem; qua deficiente Romanus pontifex non est papa sed unus alius mundo absconditus. Sed cum tres ficciones non sufficiunt, remanet dubium, quomodo dicta duo nomina sunt connexa. In qua materia credendum est cronicis. Narrat enim Cestrensis libro IV, cap. XXXVI, quomodo excellencia Romani imperii adinvenit papatum sui pontificis super alios: Nycena, inquit, synodus hoc contulit privilegium Romano pontifici, ut sicut Augustus pre ceteris regibus, ita Romanus pre ceteris pontifex haberetur episcopis et papa velut principalis pater vocaretur. Origo autem istius nominis et excellencie fuit in dotacione ecclesie, [p. 178] ut specificat Decretum XLVI distinccione Constantinus. Ideo superfluum et labor inutilis foret fingere mendacia, quod sic oportuit esse ex racionibus ad hoc urgentibus vel scriptura. Unde quia ista videtur levis fundacio et ecclesia Romana tunc sibi cadere a papatu, narrat idem Cestrensis libro V cap. X, quomodo Bonifacius IV impetravit a Foca cesare, ut ecclesia beati Petri Rome Caput esset ecclesiarum, quia caput ecclesie Constantinopolitane se scripsit papam. Quotlibet tales fideles cronice et decreta testantur primatum Romani pontificis fuisse humanitus adinventum. Nam si papa fieret vagus ut olim et nulli loco affixus sed in mari mortuo vel deserto, et sic post eum papa secundus, et sic ad finem viacionis ecclesie, patet quod non obstante isto vere foret papa.

[ENGLISH]

## ¶2 · 178.17–179.7

> [p. 178] Ideo oportet quod aliqua sit racio pape ante notacionem loci huius qualiscumque. Ideo vere dicit dominus Ardmacanus j libro VII cap. XXI De Questionibus Armenorum: Quod Petrus ideo fuit Christi vicarius, quia fuit sibi similior in virtute. Et foret inanis ficticia quod, ubicumque fuerit talis electus humanis ritibus, consequitur quod sit Roma; non enim est racio, quare pocius fieret ibi Roma quam Anthiochia, Jerusalem vel Constantinopolis. Tales enim locorum illorum metropolitani dixerunt se esse papas propter disparem racionem: Anthiochia, quia ibi vocati sunt primo discipuli christiani, ut patet Act. XI, et beatus Petrus ibi resedit episcopus multis annis, et tercio quia prius recepit fidem Christi quam Roma. Episcopus autem Jerosolimitanus [p. 179] vendicat papatum propter Christum, propter primitatem fidei, propter mortem Jacobi, qui ibi primo secutus est mortem Domini. Constantinopolis vero propter nomen cesaris, qui dotando tantum decoravit ecclesiam. Et Roma, quia ibi sancti apostoli sunt occisi et realiter, quia impetrarunt a cesare hoc privilegium.

[ENGLISH]

## ¶3 · 179.8–180.20

> [p. 179] Et revera omnes et singulas istarum causarum propter impertinenciam ad papatum est turpe fingere, sed turpissimum quod papa aliquis impetrat privilegium illud concedere vel donare, quam potest concedere, quod datus episcopus vivat Christo similius. Sed sicut sophista vel maniacus concedit quod Deus regnat in angelis et tamen non sequitur propter suum concedere sive imperium plus vel minus, ita est de concessione privilegii pape vel cesaris, ut quis sequatur Christum similius in virtute. Sed cum locus sit huic dignitati impertinens, oportet rogare trinitatem obnixius, implorare suffragium ecclesie utriusque humilius et attendere devote bonis operibus, ut Deus eligat quem voluerit, et ostendat I oraculis vel sanctis operibus, que precedant eleccionem humanam, quia eleccio humana est istis impertinens. Concedo igitur cum domino Ardmacano historiam de beato Petro quomodo timore cesaris proposuit sub colore Christi consilii a Roma aufugere, et quomodo obvianti Christo in porta civitatis et querenti: Domine, quo vadis, responsum est ab eo venio Romam iterum crucifigi. Per quod Petrus expectans concepit, quod dominus crucifigendus fuit ibi in ipso, quia iuxta rectam logicam Christi Matth. XXV [p. 180] Christo faciunt vel non faciunt homines quicquid fecerint vel non fecerint membris suis, et sic nedum fuit ex divina ordinacione, quod Petrus et Paulus inibi morerentur, sed omne quod fit in mundo fit ex ordinacione divina accessoria vel directa. Accessoria in viciosis operibus, de quibus bonum ordinat, et directa in virtuosis operibus vel operibus naturalibus. Causam autem quare Christus ordinavit gloriosos apostolos ibi pati martyrium est exemplar et speculum aliis martyribus, quod ordinavit postmodum ibi pati, cum aliis bonis exemplum sequentibus. Sed credo quod nullus fidelis tantum insaniet, quod fingat dominum ordinasse ibi illorum martyrium, ut doceat fore papam quemcumque Romanum episcopum successurum, quia (ut dictum est) nomen tale inolevit ex institucione humana et sepe opinioni hominum in istis falsitas est substrata; locus enim ille est impertinens, ut eius episcopus sit precipuus sequax Christi.

[ENGLISH]

## ¶4 · 180.21–180.32

> [p. 180] Unde videtur non esse de substancia fidei, quod Clemens, Linus, Cletus vel alius post Petrum Romanus episcopus fuit papa, intelligendo papam, ut dicit primitatem alienum excludentem. Intelligendo autem papam communiter, modo quo Ambrosius, Augustinus et ceteri sancti episcopi erant pape, manifestum est quod Paulus, Clemens et ceteri sancti martyres et confessores Romani episcopi erant pape simul cum aliis, quod si aliquis eorum in regimine ovium Christi omnes conversantes secum excesserat, tunc fuit iste papa ad sensum superius limitatum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 176.5: Man's election does not make a pope unless God too has chosen him.
- 177.5: An election requires acceptance by the subjects.
- 177.21: The true origin of the name 'Pope'.
- 178.7: The right to be sole pope was first granted by the Emperor Phocas.
- 178.17: Local claims as strong in other cities as in Rome.
- 179.8: All these claims are groundless and wrong; the worst is a privilege begged from the Emperor.
- 180.21: It is not a matter of faith that Clement and others were popes in the modern use.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 177: *intrusoris* [NW]
  - 177: *sicut* [R3]
  - 178: *beati Petri* (one token covers two printed words) [THIN]
  - 178: *Rome* (hyphenated Ro-me; main token covers whole word) [THIN]
  - 178: *papa fieret* (one token covers two printed words) [THIN]
  - 178: *vagus ut olim* (one token covers three printed words) [THIN]
  - 178: *nulli loco* (one token covers two printed words) [R4]
  - 178: *Christi* [R3]
  - 179: *impertinenciam* [NW]
  - 179: *sit huic* (one token covers two printed words) [R5]
  - 179: *istis* (25 is the line number) [R4]
  - 180: *et speculum* (one token covers two printed words) [R5]
  - 180: *quod* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 176:
2. dicit. Rectius: dat. 14. B: fit iuste. 28 AB in marg.: Aliud
est eligere hominem in papam et aliud eligere papam.

p. 177:
6. AB in marg : Eleccio duplex est. 14. Codd.: estalis (sic).
24. AB in marg. : Papa illud nomen unde habet ortum. 25. Codd.:
cap. XIV. Correxi. 29, 3o Codd.: Romanus pontifex pre ceteris deest.
2 5.Polychronicon Ranulphi Higden V, 140. Hussii Opp. CCXXb.
33. Cap. XIV.
De Potestate Pape. I 2

p. 178:
3. esse ; B: se. fj. iunc ; adde: videbatur. 7. Codd. : Cap. LVIl.
18. AB in marg. : Vicarius Christi quare dicitur Petrus. 22. Codd. :
insanis. 27. Codd.: metropoli. 28. A in marg.: Papa Antiochie.
32. A in marg. : Papa Jerosolimitanus.
6. Polychron. V, 417.

p. 179:
3. A in marg.: Papa Constantinopnlitanus. 5. A in marg. : Papa
Romanus. i5. suum: Hic aliquot verba desunt. 20 Codd.: obnixns.
25. AB in marg. : Fuga Petri de Roma.
33. Matth. XXV, 34 seqq.

p. 180:
6. AB in marg.: Ordinario divina est duplex. 12. AB in marg. :
Roma est impertinens i:t eins episcopus sit precipuus sequax Chrisli.
16. Codd.: nomine. 25. AB in tnarg. : Papa dicitur dupliciter.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 177: Dominum elegisti hodie, | synodns hoc contulit privilegium Romano pontifici, ut sicut Augustus pre ceteris regibus, ita Romauus pre ceteris pontifex haberetur episcopis et papa velut principalis pater vocaretur.
p. 178: Bonifacius IV | impetravit a Foca cesare, ut ecclesia beatiPetri Ro- | me C aput esset ecclesiarum, quia caput ecclesie Constantinopolitane se scripsit papam. | Onod Petrus ideo fitit Chrisii vicarius, quia fuit sibi simitior in virtute.
p. 179: Domine, ?oquo vadiSy | venio Romam iterum cruciflgi.
```

---

## Chunk 08-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "180.33–184.33"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "804 words; 723 unanimous or majority-real; 60 settled by vote (DEL 1, R2 37, R3a 9, R5a 11, R6a 2); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n241–n245 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 5: [TITLE]

## ¶1 · 180.33–181.15

> [p. 180] Abusio autem termini infundabilis videtur michi vocare quemcumque pseudopapam nudo nomine [p. 181] papam vel caput ecclesie. Unde gentilitas et primatus affeccio docuerunt quod quicumque Romanus pontifex censeatur papa et gerat primatum huiusmodi super singulos alios sacerdotes; unde patet quod Deus non ordinasset apostolorum martyrium Rome propter hunc finem, nisi verus papatus regulariter sequeretur. Sed frequenter post dotacionem ecclesie separatus est papatus a Romano pontifice, igitur Deus non intenderat per illud martyrium illum finem; tunc enim Deus frustratus a suo proposito improvide ordinasset et negligenter omisisset m suo testamento tam necessarium primatum ad regimen sue ecclesie. Ideo certum est quod invencio humana fabricavit institucionem istam de papa.

[ENGLISH]

## ¶2 · 181.16–181.32

> [p. 181] In cronicis autem Cestrensis narravi alias quomodo multi Romani pontifices de papatu defecerant, et repeto illa que scripta sunt in cronica aurea Radulphi de Dyceto decani sancti Pauli, cui Anglici darent fidem. Narrat enim libro I cap. II, quomodo anno domini CCCCXX presidebat in Roma Boni facius papa et contra hunc ordinato Eulalio, ac pro hoc dissidente ecclesia ambo iussu Honorii Augusti urbe egrediuntur, et sic reprobato Eulalio iussu Augusti Bonifacius, quia prior ordinatus fuerat, sedi apostolice restituitur. Nondum enim tunc tantum sopitum fuit dominium Romani imperii nec ad tantum invaluit usurpacio Romani pontificis quod fuit reputatum hereticum, quod domini temporales possunt auferre temporalia, ymo dignitates atque officia ab ecclesia delinquente.

[ENGLISH]

## ¶3 · 182.1–182.2

> [p. 182] Secundo, anno domini CCCCXCIII contra Symachum papam ordinatur Laurencius per contencionem.

[ENGLISH]

## ¶4 · 182.4–182.7

> [p. 182] Tercio, anno domini DCCLXVIII Constantino papa scismatico oculis privato Stephanus papa constituitur; hic synodum Rome congregat et ordinatos a Constantino scismatico reordinat.

[ENGLISH]

## ¶5 · 182.8–182.9

> [p. 182] Quarto, anno domini DCCCLIII adversus Benedictum papam Anastasius presulatum invadit.

[ENGLISH]

## ¶6 · 182.10–182.11

> [p. 182] Quinto, anno domini DCCCCVII presidet Leo papa, contra quem Chrystoforus surgit.

[ENGLISH]

## ¶7 · 182.12–182.30

> [p. 182] Sexto, anno domini DCCCCLXVIII collecta a tota Ytalia episcoporum synodo Johannes papa de nephariis causis infamatur, qui dum se excusaturum venire cunctatur, Leo adhuc laycus eleccione omnium et consensu imperatoris papa substituitur. Sic Leo fecit ordinaciones et alia, que erant apostolica. Nec longum Romani alterata fide apud imperatorem papam recipiunt Johannem. Ille autem synodo collecta Leonem deposuit et eius gesta cassavit. Statutumque est synodum a Leone non nominandam synodum sed prostibulum favens adulteris. Quicumque igitur eo ordinante erant dampnati iussi suam ipsorum proscripsionem presentare in cartha hec continente: Pater meus nichil sibi habuit, nichil michi dedit, et sic depositi manserunt in illis gradibus, quos habuerant nondum a Leone ordinati. Iste Johannes papa cum uxore cuiusdam oblectans a dyabolo in tempore coitus percutitur et sine viatico dominico obiit.

[ENGLISH]

## ¶8 · 183.1–183.7

> [p. 183] Septimo contigit Romanos contra iuramentum, quod imperatori fecerant, scilicet quod nunquam eligerent papam sine eius et sine filii eius Othonis consensu, Benedictum papam constituunt, sed imbperator Roma obsessa adeo Romanos affflixit, ut Leonem papam se recepturos promitterent et sic Benedictus renuitur.

[ENGLISH]

## ¶9 · 183.8–183.13

> [p. 183] Octavo, anno domini MXLV Benedictus, qui symoniace papatum invaserat, cum esset rudis literarum, alterum ad vices ecclesiastici officii exequendas secum papam Silvestrum consecrari fecit; quod cum multis non placeret, tercius superinducitur Gregorius, qui solus vices duorum impleret.

[ENGLISH]

## ¶10 · 183.14–184.4

> [p. 183] Nono, anno domini MXLVl Rome uno contra duos et duobus contra unum de papatu altercantibus rtx Henricus contra eos Romam vadit et eis canonica et imperiali censura depositis, Clemens presidet, et ab eo rex Henricus in imperatorem benedicitur, iurantibus Romanis se sine eius consensu nunquam papam electuros. Tunc enim practizata fuit lex sepe tacta, que ponitur III. Reg. II, 35 quod instar Salomonis rex debet in casu deponere summum pontificem. Tunc eciam accepit rex ab eo humiliter benediccionem, quod post infidelitatem vocatum est necessarium sacramentum et confirmacio sine qua non fit aliquis imperator. Sed ista ficta mendacia extra fidem scripture ex gestis et factis preteritis cum racionibus professorum scripture relicta sunt a domino convincenda. Tercio patet quod antequam introducta est novella et infundabilis secta cardinalium; papa fuit electus a populo Romanorum, [p. 184] Decimo, anno domini MLXVIII Rome duobus de papatu contendentibus Alexander cum suam purgasset innocenciam de symonia recipitur, Cadalus Parmensis episcopus reprobatur, unde dictum est

[ENGLISH]

## ¶11 · 184.5–184.5

> [p. 184] Cadalus in Parma Parme fuit arcus et arma.

[ENGLISH]

## ¶12 · 184.6–184.6

> [p. 184] Cadalus occubuit, Parma ruina fuit.

[ENGLISH]

## ¶13 · 184.7–184.10

> [p. 184] Undecimo, anno domini MLXXXIII Henricus urbem Rome infregit et Wybertum in sede apostolica constituit, Hildebrandus vero Beneventum adiit, ubi usque ad obitum suum deguit.

[ENGLISH]

## ¶14 · 184.11–184.13

> [p. 184] Duodecimo, anno domini MLXXXVII Desiderius, qui et Victor, papa contra Clementem est factus.

[ENGLISH]

## ¶15 · 184.14–184.23

> [p. 184] Decimo tercio, anno domini MXCI fertur fuisse duos, qui dicebantur Romani pontifices a se invicem discordantes et ecclesiam Dei inter se divisam trahentes, Urbanus scilicet, qui primum fuerat episcopus Ostiensis, et Clemens qui Wybertus archiepiscopus Ravenensis. Que res per plures annos ecclesiam Anglie in tantum occupavit, quod ex quo Gregorius, qui et Hildebrandus, defunctusfuit, nulli loco pape usque ad hoc tempus subdi et obedire voluerit.

[ENGLISH]

## ¶16 · 184.24–184.28

> [p. 184] Decimo quarto, anno domini MCXXX Innocencio papa regente intrusus est Petrus Leonis et dictus est Anacletus, qui regem Rogerum Sycilie consecravit, sed Innocencius papa transivit in Franciam, unde dicitur:

[ENGLISH]

## ¶17 · 184.29–184.29

> [p. 184] Romam Petrus habet, totum Gregorius orbem.

[ENGLISH]

## ¶18 · 184.30–184.33

> [p. 184] Decimo quinto, anno domini MCLIX rexit Alexander papa, contra quem Octavianus intruditur, sed in scismate moritur, et sic Guido Cremensis sed Johannes intrusus reconciliatur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 181.11: Such modern popedom is of man's invention.
- 181.20: The history of Boniface and Eulalius shews how great was the power of the lay ruler.
- 182.1: Other instances of rival popes as related by Ralph de Diceto.
- 183.20: The emperor Henry IV (like Solomon) deposed the chief pontiff.
- 184.7: More instances of rival popes.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 181: *illum* [R3]
  - 181: *illa* [R3]
  - 181: *I* (print has libro I, at line end before cap. II; main scan lacks it) [INS?]
  - 181: *facius* (Boni | facius split by folio bar (206b), no hyphen) [R4]
  - 181: *hunc* [R3]
  - 182: *CCCCXCIII* [THIN]
  - 182: *Symachum* (hyphenated Sy-machum; main token covers whole word) [THIN]
  - 182: *papam* [THIN]
  - 182: *ordinatur* [THIN]
  - 182: *per* [THIN]
  - 182: *contencionem* (hyphenated con-tencionem; main token covers whole word) [R5]
  - 182: *DCCLXVIII* [R5]
  - 182: *meus* [R3]
  - 182: *dominico* [THIN]
  - 183: *et* [R3]
  - 183: *impleret* [R3]
  - 183: *Romanorum* (plate: main token spans pages; Decimo belongs at the head of p. 184 (restored there by tokenfix after the re-vote)) [THIN]
  - 184: *papatu* [R4]
  - 184: *occubuit* [R4]
  - 184: *factus* [R3]
  - 183: *filii* (W2: italic f (long-s-like f); print = filii) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 180:
6. AB in marg.: Ordinario divina est duplex. 12. AB in marg. :
Roma est impertinens i:t eins episcopus sit precipuus sequax Chrisli.
16. Codd.: nomine. 25. AB in tnarg. : Papa dicitur dupliciter.

p. 181:
3. B: gerit. 4. modi deest in codd. 20. ABinmarg. : Deposicio
paparum. 23. Codd.: per. 24. Codd.: urbem. 26. quia ; codd.:qui.
20. Radulphus de Diceto, 11 83 decanus Londoniensis S. Pauli
(f 22. Nov. 1202 vel i2o3) ed. Stubbs I, 83. Hussii Opp. 23oa.

p. 182:
i3. B: synode. 14. Recte: excusatum. 20, 21. B: Cessavil.
21, 22. Codd. : nominanda synodus. 25. Codd. : Pater nimis.
20. Codd. : mansuerunt; recte : remanserunt.
1. Radulfi de Diceto p. 89. 4. Ibid. p. 124. 8. Ibid. p. 137.
Recte: 855. 10. Ibid. pag. 142. Recte: co3. 12. Ibid. pag. i5i.
Recte: q63. Huss 23o\

p. 183:
14. AB in marg. : Juramentum imperatoris dicitur necessarium sacra-
1. lbid. p. 1 1 . 8. Radulfi de Diceto pag. 187. Huss 23oa.
14. Ibid.

p. 184:
19. Cod. : populares annos.
1. Radulfi de Diceto p. 200. 7. Ibid. p. 211. 11. Ibid.
p. 21G. 24. Ibid. p. 246. 3o. Ibid. p. 3o3. Huss, 23ob.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 181: anno domini CCCCXX presi- | debat in Roma Boni \facius papa et contra hunc | ordinato Eulalio, ac pro hoc dissidente ecclesia ambo iussu Honorii Augusti urbe egrediuntur, 2d et sic reprobato Eulalio iussu Augusti Bonifacius, quia prior ordinatus fiierat y sedi apostolice restituitur.
p. 182: Secundo, anno domini CCCCXCIII contra Sy- | machum pavam ordtnatur Laurencius ver con- | tenctonem. Tercio, anno domini DCCLXVIII Constantino papa scismatico oculis privato Stephanus papa | constituitur; hic synodum Rome congregat et ordinatos a Constantino scismatico reordinat. Quarto, anno domini DCCCLIII adversus Benedictum papam Anastasius presulatum invadit. Quinto, anno domini DCCCCVII presidet Leo | papa, contra quem Chrystoforus surgit. Sexto, anno domini DCCCCLXVIII collecta a tota Ytalia episcoporum synodo Johannes papa de nephariis causis infamatur, qui dnm se excusaturum venire cunctatur, Leo adhuc laycus eleccione omnium 1 | et consensu imperatoris papa substituitur. Sic Leo fecit ordinaciones et alia, que erant apostolica. Nec longum Romani alterata fide apud imperatorem papam recipiunt Johannem. Ille autem synodo collecta Leonem deposuit et eius gesta cassa- 20 vit. Statutunique est synodum a Leone non nominandam synodum sed prostibulum favens adulteris. Quicumque igitur eo ordinante erant dampnati iussi suam ipsorum proscripsionem \ presentare in | cartha hec continente: Pater meus nichil sibi habuit, | nichil michi dedit, et sic depositi manseruut in illis gradibus, quos habuerant nondum a Leone ordinati. Iste Johannes papa cum uxore cuiusdam oblectans a dyabolo in tempore coitus percutitur et sine viatico domimco obiit.
p. 183: Septimo contigit Romanos contra inramentum, quod imperatori fecerant, scilicet quod nunquam eligerent papam sine eius et sine Jilii eitts Othonis consensu, Benedictunt papam constitiaint, sed imbperator Ronta obsessa adeo Romanos affftixit, ut Leonem papam se recepturos promitterent et sic Benedictus renuitur. Octavo, anno domini MXLV Benedictus y qui symoniace papatum invaserat, cum esset rudis li- \oterarum, alterum ad vices ecclesiastici officii exeqnendas secum papam Silvestrum consecrari fecii; quod cum multis non placeret, tercius superinducitur Gregorhts, qui soltts vices duorum impleret, Nono, anno domini MXLVl Rome uno contra ibduos et duobus contra unum de papatu altercantibus rtx Henricus contra eos Romam vadit et eis canonica et imperiali censura depositis, Clemens presidet, et ab eo rex Henricus in imperatorent beuedicittir, iurantibus Romanis se sine eius con- | sensu nunquam papam electuros. | Juramentum imperatoris dicitur necessarium sacramenlum.
p. 184: Deciino, anno domini MLXVIII Rome duobus de papatu contendentibus Alexander cum suam purgasset innocenciam de symonia recipitur, Cadalus Parmensis episcopus reprobatur, unde dictum est Cadalus in Parma Parme fuit arcus et arma. | Cadaius occubuit, Parma ruina fuit. | Undecimo, anno domini MLXXXIII Henricus urbem Rome infregit et Wybertum in sede apostolica constituit, Hildebrandus vero Beneventum adiit, ubi usque ad obitum suum deguit. | Duodecimo, anno domini MLXXXVII Desiderius, qui et Victor, papa contra Clementem est factus. Decimo tercio, anno domini MXCI fertur fuisse duos, qui dicebantur Romani pontifices a se in- | vicem discordantes et ecclesiam Dei inter se divisam trahentes, Urbanus scilicet, qui primum fuerat episcopus Ostiensis, et Clemens qtii Wybertus archiepiscopus Ravenensis. Que res per plures annos ecclesiam Anglie in tantum occupavit, quod ex quo 20 Gregorius, qui et Hildebrandus, defunctusfuit, nulli loco pape usque ad hoc tempus subdi et obedire voluerit. Decimo quarto, anno domini MCXXX Innocencio papa regente intrusus est Petrus Leonis et dictus | est Anacletus, qui regem Rogerum Sycilie consecravit, sed Innocencius papa transivit in Franciam, unde dicitur: Romam Petrus habet, totum Gregorius orbem. Decimo quinto, anno domini MCLIX rexit Ale- | xander papa, contra quem Octavianus intruditur, sed in scismate moritur, et sic Guido Cremensis \ sed Johannes intrusus reconciliatur.
```
