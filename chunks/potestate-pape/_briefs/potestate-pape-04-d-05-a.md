# Translation brief: potestate-pape 04-d–05-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-04-d.md chunks/potestate-pape/wyc-potestate-pape-04-e.md chunks/potestate-pape/wyc-potestate-pape-05-a.md` once and fix what it reports.
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
| pars peregrinans; peregrinari | the pilgrim part; to be a pilgrim | Augustine's *peregrinatio* (Ench. 56). Pilot. |
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 04-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-04-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-04-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "72.16–76.11"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 62.9); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "840 words; 782 unanimous or majority-real; 44 settled by vote (INS 1, R2 19, R3a 9, R5a 15); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n133–n137 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 4, part 4: [TITLE]

## ¶1 · 72.16–74.11

> [p. 72] Sed triplex ponitur causa quare tempore legis gracie sacerdocium non sic vadit iure hereditario. Prima quia sacerdotes nostri et specialiter summi pontifices debent caste vivere instar Christi et per consequens non relinquere sue carnali soboli ius ad quicquam. Secunda causa est quia Christus noluit eius vicarios habere seculare dominium vel honorem sed omnino specie hereditatis celestis, que solum datur patrissantibus in moribus spiritualibus filiis adoptivis. Tercia causa est ut nos tempore legis gracie spiritualius procedentes, discamus eligere meliores et amare duplicem virginitatem, et quod spiritualis prepositura vel dignitas sacerdotis non sit carnalis sed spiritualis ex filiacione in moribus; cum hereditas illa sit cuicumque promerenti indifferens. Necesse est igitur quod summus sacerdos noster sit in se totus collectus circa edificacionem ecclesie et non [p. 73] divisus ad placendum uxori sue; ut loquitur Apostolus I. Cor. VII. Et hec racio quare oportuit legem illam cessare et novam introduci, ut dicitur Heb. VII. Sed illud calliditate dyaboli est frustratum, cum episcopi nostri gravius fornicantur cum seculo. Sed quarto obicitur per hoc quod iuxta dictam sentenciam contingit duos episcopos super eodem populo legittime ordinari; quod concedo; cum Christus animarum necessario est episcopus cuiuslibet populi christiani et habet multos episcopos vicarios super eodem populo adiutores. Ipse tamen excellenter et differenter est episcopus ecclesie triumphantis et tocius ecclesie militantis. Similiter, eedem persone, quas Petrus, Paulus et ceteri apostoli ordinarunt episcopos, non excluserunt eos a superintendencia populi sed iuverunt, ut beatus Clemens quem beatus Petrus ordinavit prudenter ut oportet dicere episcopum Romanorum fuit episcopatui Petri nedum conpossibilis, sed adiutor, nam in quadam epistola beati Clementis directa Jacobo Jerusalimitano sic scribitur: Beatus Petrus morte sibi appropinquante in collegio fratrum positus ipsum Clementem per manum accipiens dixit, hunc Clementem episcopum vobis ordino, qui ab inicio mecum fuit. Nec dubium quin tanti capitis ordinacio quam oportuit ex Spiritu Sancto procedere non instituisset Clementem episcopum, nisi de facto foret episcopus; ymo videtur quod sicut actus episcopales non repugnant tam simul quam paulative super eodem populo, sic nec [p. 74] pontificum dignitates, sicut videtur de Christo et Petro, cum simul cum eo fuit summus pontifex. Sic enim beatus Johannes fuit episcopus continue ecclesie Asyane et tamen habuitseptem episcopos adiutores. Actus ergo spirituales non repugnant et per consequens potestates vel habitus respectu eiusdem populi. Sed tota repugnancia videtur civilitas et dominium, quod haberent in populo. Hec enim fuit racio quare Abraham et Loth scilicet propter proprietates possessionum non potuerunt habitare simul, ut Gen. XIII.

[ENGLISH]

## ¶2 · 74.12–76.11

> [p. 74] Tercio confirmatur de rectoribus et suis episcopis, qui sunt simul episcopi eiusdem parrochie, et Deus scit quis quoad Deum est suo adiutore superior, quia certum est quod ille qui magis spiritualiter prodest parrochie est episcopus superior I quoad Deum; et certum est quod profectus suus est extensior. Nec valet dicere quod sacerdos talis non est episcopus, quia iuxta decretum Jeronimi positum 95 distinccione Olim; Olim, inquit, erat idem presbiter, qui et episcopus, et antequam dyaboli instinctu studia in religione fierent et diceretur in populis, ego sum Pauli, ego Apollo, ego sum Cephe, communi presbiterorum consilio ecclesie gubernabantur. Postquam autem unusquisque eos quos baptizaverat suos esse putabat, non Christi, decretum est ut unus de presbiteris superponeretur et scismatum semina tollerentur. Nec est fingendum quod propter adinventas preposituras secundum dignitates reputacionis humane fit novus ordo supra sacerdotum, sed manent septem ordines antiqui humanitus alterati. Non enim princeps secularis per viam dotacionis et maioritatis reputacionis mundane [p. 75] instituit novum ecclesiasticum sacramentum. Multi igitur sunt episcopi super eodem populo se iuvantes, quia aliter non liceret habere episcopum suffraganeum, cum ille sit episcopus non Nullatensis, sed illius loci quem incolit et illius populi, cui superintendit. Et idem est iudicium de Petro et Paulo qui simul erant Romani episcopi. Paulus enim erat episcopus sicut Scarioth et omnes apostoli, sed cuius populi si non gentium quas tantum edificando superintendit predicacionibus, miraculorum faccionibus et scriptura, et hec consumavit excellenter et finaliter cum Romanis. Ideo non beatus Petrus sed ipse fuit precipue episcopus Romanorum. Sic igitur non repugnat sed consonat multos angelos deputari ad unius custodiam, sed fides scripture testatur Deum, Paulum et ceteros apostolos habere in eodem officio spirituali plurimos adiutores; sic est de spirituali episcopatus officio senciendum; sed oportet illum excellere qui spiritualiter magis servit. Nec est credendum institucionibus civilibus vel ficticiis de repugnancia iurisdicionum, nisi de quanto fundata fuerint in scriptura, quomodo preeminencia Petri super ceteros apostolos stat in universali iurisdiccione super totam militantem ecclesiam, aut quod certa potestas iurisdicionalis debet esse in alios apostolos, per illam potestatem ad locum et populum limitata. Nam ceteri apostoli edificarunt ecclesiam in regionibus variis, non petita licencia a Petro, Paulus vero universalius quam Petrus convertit gentes, eciam antequam vidit Petrum, ut patet Actuum IX et infra, Galat. [p. 76] primo et infra; Joh. in Asya minori diu post Petri martirium. Nec oportuit vel decuit illum, qui tam crebras revelaciones Spiritus Sancti habuit; quomodo agendum fuerit, querere instruccionem a suo conservo et consocio Petro vel eius vicario qui instruccione eiusdem magistri indiguit. Et idem est iudicium de sancto Thoma, quando Christus in foro venalium precepit sibi, quod transiret in Yndiam, et sic de ceteris apostolis, ut patet ex fideli eorum cronica quam legit et sollempnizat ecclesia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 72.16: Reasons against its present use.
- 73.7: There may be more than one bishop in a diocese if all work together usefully.
- 74.12: No essential distinction between priests and bishops.
- 75.8: Peter and Paul were Roman bishops at the same time.
- 75.21: We need not concern ourselves about clash of jurisdictions.
- 76.2: The apostles preached and suffered without asking authority from Peter.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 72: *hereditario* [NW]
  - 72: *illa* [R3]
  - 73: *necessario* [R3]
  - 73: *∅* (178ᵈ is the folio mark) [R4]
  - 74: *qui* [R3]
  - 74: *Olim* [R3]
  - 74: *fierent* [NW]
  - 74: *ecclesie* [R3]
  - 75: *episcopatus* (hyphenated episco-/patus; main token covers whole word) [R4]
  - 75: *illum* [R3]
  - 76: *Petri* [R4]
  - 76: *illum* [R3]
  - 76: *tam* [R3]
  - 76: *habuit* [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Peter and Pau] (75.8).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 72:
8. Ainmarg. : Summi pontificis institucio iure hereditario. 16. B in
marg.: Tempore legis gracie sacerdocium non currit iure hereditario
triplici causa.

p. 73:
9. A in marg. : Episcopos duos stat esse super eodem populo. 3o. 15
in marg. : Plures episcopos super eodem populo contingit le^itime ordinari.
23. Clementis I. Rom. pont. Opp. dubia. Epist. decret. Migne,
Pat. curs. compl. Ser. Graeca I, 464.

p. 74:
20. H in marg. : Nota. 28. Codd.: supponeretur. Correxi.
20. Decreti prima pars, dist. XGV, cap. V.

p. 75:
b. A in marg. : Pau/us aposlolus fuit gencium ct Romanorum episcopus.
1 3. Codd. : non deest.
5. Nullatensis Cf. De Ecclesia p. 583. Serm. II, 65.

p. 76:
i5. B in marg. : Natalicia apostolorum ; A: Apostolorum mortes.
27. A in marg.: Apostoli non habuerunt recursum ad Petrum.
8. In foro venalium. The lesson in the Sarum Rreviary says :
Apparuit ei Dominus in visu noctis. (Matthew). 1 2. .lanuen-
sis Catholicon, Cf. De Civili Dominio III, 425.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 72: Jerusalem que occidis prophetas et lapidas eos | qui ad te missi sunt, | Manasses effudit sanguinem innoxium et implevit Jerusalem cruore innocencium, et ob hanc rem noluit dominus propiciari. | Jerusalem locus sanccior Roma.
p. 73: Beatns Petrus morte sibi appropinquante in collegio fratrum po- | situs ipsum Clementem per manum accipiens dixit, hunc Clementem episcopum vobis ordino, qui ab inicio mecum fnit. | Non habemus hic manentem civitatem sed futuram iuquirtmus, | Dotacionem et loci appropriacionem qitare apostoli fugiemnt.
p. 74: Olimc^o Otim, | erat idem presbiter, qui et episcopus, et antequam dyaboli instinctu studia in religione jierent et diceretur in populis, ego sum Pauii, ego Apollo, ego sum Cephe, communi presbiterorum consilio ecclcsie gubernabantur. Postquam autem | unusquisque eos quos baptizaverat suos esse pntabat, non Christi, decretum est ut unus de presbiteris superponeretur et scismatum semina toilerentur. | et tantum | Nota tempore apostolorum et evangelistarum Clemens a Petro eligitur, ergo non secundum sanctitatem
p. 76: apostoli per orbem post ascensionem Domini sunt dispersi: Petrus Romam venit, Andreas | Achaiam et uterqne ibi crucifigitur, Johannes Ephesum vivus intrat sepnicrum, Jacobus maior Jerusolimis decotlatur, Thomas in Yndia iancea transfigitur, Philippus in Frigia crucifigitur, Jacobus minor partica futlonis Jerusolimis occiditur, Bar- | tolomeus in maiori Yndia excoriatur et decollatur, Matheus iu Ethiopia in altari lancea perforatur, Symon et Yudas iu Persyde a pontificibus ydotorum tumuitu populi interimuntur, Mathias in Yndia pro Christo patitur, Lucas in Bythinia, obiit, Marcus^b Atexandrie martirium complevit, Barnabas iu Salamia occisus est.
```

---

## Chunk 04-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-04-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-04-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "76.12–80.22"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 62.9); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "932 words; 842 unanimous or majority-real; 70 settled by vote (R2 35, R3a 20, R5a 14, R6a 1); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n137–n141 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 4, part 5: [TITLE]

## ¶1 · 76.12–78.3

> [p. 76] Unde Januensis in suo Katholicon narrat ex quadam cronica conformiter ad cantum ecclesie, quomodo apostoli per orbem post ascensionem Domini sunt dispersi: Petrus Romam venit, Andreas Achaiam et uterque ibi crucifigitur, Johannes Ephesum vivus intrat sepulcrum, Jacobus maior Jerusolimis decollatur, Thomas in Yndia lancea transfigitur, Philippus in Frigia crucifigitur, Jacobus minor partica fullonis Jerusolimis occiditur, Bartolomeus in maiori Yndia excoriatur et decollatur, Matheus in Ethiopia in altari lancea perforatur, Symon et Yudas in Persyde a pontificibus ydolorum tumultu populi interimuntur, Mathias in Yndia pro Christo patitur, Lucas in Bythinia, obiit, Marcus Alexandrie martirium complevit, Barnabas in Salamia occisus est. Stultum autem et infidele mendacium foret fingere quod omnes alii apostoli habuerunt recursum ad Petrum vel eius vicarium; et ex eorum precepto ac auctoritate fecerunt quicquid fecerant, primo quia habuerunt magistrum omnium eis continue assistentem; iuxta [p. 77] promissum suum Math, ultimo: Ecce ego vobiscum sum, omnibus diebus usque ad consumacionem seculi. Quomodo igitur foret necessarium tam ambigue querere auctoritatem sive consilium, quando tanta copia fontis sapiencie continue fuit presens. Secundo quia Paulus testatur Gal. I, 17 quod post conversionem suam non venit statim Jerusolimam ad apostolos sed continuo predicavit in Arabya. Deinde post annos tres venit Jerusalem videre Petrum et mansit cum eo diebus quindecim, quia (ut dicit in principio) non fuit factus apostolus ab hominibus neque per hominem, eleccione vel instrumentali institucione, sed per Ihesum Christum secundum deitatem, per cuius revelacionem evangelium suum didicerat, deinde (ut narrat cap. II, I, 2 post annos quatuordecim iterum ascendit per revelacionem in Jerusalem cum Barnaba et Tito contulitque cum precipuis apostolis. Michi, inquit, qui videbantur esse aliquid nichil contulerunt, sed e contra cum vidissent, quod creditum est michi evangelium prepucii, sicut Petro circumcisionis, cum cognovissent graciam Dei, que data est michi, Jacobus et Cefas et Johannes, qui videbantur esse columpne, dextras dederunt michi et Barnabe societatis. Cum, inquit, venisset Cephas Antiochiam, in faciem ei restiti, quia reprehensibilis erat, Numquid credimus vas eleccionis et scribam Spiritus Sancti qui vidit quanta mala futura erant in ecclesia pro primatu usus fuit falsitate vel levitate in verbis fidei? quin pocius ad destruendum hereses quas sciverat postmodum pullulare premittens Jacobum dicit quod omnes illi tres [p. 78] nichil sibi contulerant? Cuius sensus repugnaret isti quod Paulus necessitatus fuit accipere autoritativam potestatem a Petro.

[ENGLISH]

## ¶2 · 78.4–80.22

> [p. 78] Et ad idem vadit secundum verbum quod illi apostoli gaudebant quod habuerunt tales socios in dextero brachio sancte ecclesie, ista (inquam) apostolorum societas excluderet eosdem esse subditos a paritate potestatis non auctoritative vel iurisdicionalis super consocios. Et idem patet per hoc quod Paulus reprobavit Petrum in sua parrochia; ideo absit fidelem crederehoc dePetro, cum ipse apostolorum humillimus fecit cuncta sua opera post ascensionem auctoritate et nomine Ihesu nichil auctoritati sue attribuens, quia aliter tota scriptura illud obmittens foret nimium defectiva. Tercio confirmatur de iurisdiccione data comuniter cunctis apostolis Matth. ultimo tam quoad locum quam populum. Data est, inquit, michi potestas in celo et in terra, euntes igitur docete omnes gentes servare omnia quecunque mandavi vobis. Et Mar, ultimo limitatur iurisdicionis locus: Euntes, inquit, in mundum universum, predicate evangelium omni creature; ubi patet primo quod alloquitur omnes apostolos pro se et suis vicariis. Apostoli enim iverunt in? Asyam. Africam et Europam: et per omnem terram habitabilem exivit virtus sermonis eorum, quia (ut patet ex sepedictis) non est aliqua pars terre vel mundi, quin spiritualiter aleretur ex predicacione evangelii per potestatem datam Christo. Et sic docuerunt mediate vel immediate omnia genera gentium: Grecos. Latinos et barbaros. [p. 79] Et patet secundo quomodo Christus tempore quo apostoli magis recolerent; dedit eis preponderantem sentenciam; quomodo fideliter docerent populum ex integro servare mandata et consilia sua que ad hoc eos docuit. Omnis enim gens debet servare ipsa in una parte vel alia. Quidam tamen apostolorum peragrarunt plures regiones et quidam pauciores, ut Paulus; qui plus omnibus laboravit, visitavit corporaliter et convertit plures provincias. Et breviter cuilibet apostolo vel eius vicario fuit nedum licitum, sed debitum tantum de populo vel terra convertere vel confirmare in fide Christi quantum sufficeret, et non fuit restriccio iurisdicionis nisi ex insufficiencia. Non enim dicit singulariter Petro: vade tu et singulariter predica toti mundo limitaque ceteros apostolos quantum sub iurisdicione sua de terra vel populo subiacebit, quin pocius Spiritus Sanctus dixit Paulo quod predicaret lacius inter gentes; Petro vero quod striccius iret in Judeos, uterque tamen sicut omnes apostoli et eorum vicarii sunt debitores omni homini, ut sibi prosint meliori modo quo poterint. Absit quin rector vel episcopus debeat proficere populo de alia parrochia sive dyocesi, et in casu quo crederet plus prodesse ecclesie et placere Christo, debet parochiam suam dimittere, et aliis in quibus magis proficeret se gratis adiungere. Sed heu ista religiosa regula primeva temporalium cupiditate disrumpitur; et nostri satrape vertunt evangelizacionem in pecunie colleccionem et propter questum circa limites iurisdicionis contenditur, cuius civilitatis origo dicitur cepisse a capite Romane ecclesie. Dicitur enim in nobis [p. 80] occiduis, quod Romanus pontifex vendicat infideliter quod nemo salvabitur nisi subiaceat taxis suis; sed nichil plus horribile vel blasfemum; cum sine personarum accepcione, quecunque persona vel populus de Yndia, Ethiopia, Grecia vel quantumcunque remota insula crediderit in dominum Ihesum Christum salvabitur, per quemcunque apostolum vel Christi discipulum conversa fuerit nisi finaliter ad infidelitatem redierit; ideo omnes tales fideles, ubicunque terrarum fuerint, sunt imitatores Petri, Pauli, et cuiuscunque apostoli quod sufficiat diligere caput Christum, cum diligendo ipsum universitas diligitur ordinate. Nec valet alterius obediencia vel subieccio, nisi de quanto docuerit legem et dileccionem Christi servare, in tantum quod sive dyabolus sive paganus sive inmediate Christus ipsam anuncciaverit subducto quocumque apostolo vel eius vicario sufficit ad salutem, cum amor Christi sit per se sufficiens. Et ista est concors apostolorum sentencia qui se ipsos parvipenderant et magnificaverant nomen Ihesu.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 77.1: They acted on Christ's command given with promise.
- 77.9: Paul's rejection of human authority,
- 78.16: Christ's commission to the apostles extended to the whole world.
- 79.14: He gave no charge to Peter to control the other apostles.
- 79.28: Our prelates quarrel over limits of jurisdiction for the sake of gain.
- 80.1: It is said that none can be saved who do not pay the Papal dues.
- 80.12: He who loves Christ, and only he, will be saved.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 76: *sepulcrum* [R4]
  - 77: *17* [R3]
  - 77: *non* [R3]
  - 77: *tres* [R3]
  - 77: *non* [THIN]
  - 77: *fuit* [THIN]
  - 77: *factus* [THIN]
  - 77: *2* (print: cap. II, 1, 2) post; main has the 1 only) [INS?]
  - 77: *levitate* (30 is the line number) [R4]
  - 78: *docete* [R4]
  - 78: *evangelium* [NW]
  - 79: *∅* (page-opening slip: end of p.78 (sic docuerunt … barbaros) re-matched; nothing between Et and patet) [INS?]
  - 79: *omnibus* [R4]
  - 79: *laboravit* [R4]
  - 79: *dyocesi* [NW]
  - 79: *primeva* [NW]
  - 80: *quod* [THIN]
  - 80: *apostoli* (hyphenated apo-/stoli; main token (aposto^, next token quod) stands for the whole word) [THIN]
  - 80: *quod* [THIN]
  - 77: *annos* (LEFT-nw: italic; print = annos) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 76:
i5. B in marg. : Natalicia apostolorum ; A: Apostolorum mortes.
27. A in marg.: Apostoli non habuerunt recursum ad Petrum.
8. In foro venalium. The lesson in the Sarum Rreviary says :
Apparuit ei Dominus in visu noctis. (Matthew). 1 2. .lanuen-
sis Catholicon, Cf. De Civili Dominio III, 425.

p. 77:
i5. B: narravit. 19. B in marg. : Paulo niliil contulcrunt columne
1. Matth. XXVIII, 19. 11. Gal. I, 1. 16. Gal. II, 6—8.
25. Gal. II, 11.

p. 78:
12. Codd. : humilius. 22. A in marg. : Potestas iurisdiccionis data
18. Matth. XXVIII, 18—20. 22. Marc. XV, i5.

p. 79:
1. B : tempnre deest ; A in marg.: Apostoli habuerunt recursutn aci
totum orbem. 19. A in marg. : Paulus habuit iurisdiccionern latam.

p. 80:
12. ita quod. B: quod si. 17. ipsam. B: iam; A in marg. : Romano
pontifici subesse non est de necessitate salutis. 23. A in marg.: Cap. V.
27. A in marg : Exproprietarie vivere debet vicarius Christi.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 76: apostoli per orbem post ascensionem Domini sunt dispersi: Petrus Romam venit, Andreas | Achaiam et uterqne ibi crucifigitur, Johannes Ephesum vivus intrat sepnicrum, Jacobus maior Jerusolimis decotlatur, Thomas in Yndia iancea transfigitur, Philippus in Frigia crucifigitur, Jacobus minor partica futlonis Jerusolimis occiditur, Bar- | tolomeus in maiori Yndia excoriatur et decollatur, Matheus iu Ethiopia in altari lancea perforatur, Symon et Yudas iu Persyde a pontificibus ydotorum tumuitu populi interimuntur, Mathias in Yndia pro Christo patitur, Lucas in Bythinia, obiit, Marcus^b Atexandrie martirium complevit, Barnabas iu Salamia occisus est.
p. 77: Ecce ego vobiscum | sum, omnibus diebus usquc ad consumacionem | non venit statim Jerusolimam ad apostolos sed continuo predicavit | in Arabya. Deinde post\ annos tres venit Jerusalem | mvidere Petrum et mansit cum eo diebus quindecim, | non fuil factus apostolus ab hominibus neqne per hominem, | sedper Ihesum Christum | post auuos quatuordecim itcrum ascendit per revelacionem in Jerusalem cum Baruaba et Tito contulitqne cum precipuis apostolis. Michiy | qui videbantur esse aliquid nichil 20 contulerunty scd e coutra cum vidissent, quod creditum est michi evangelium prepucii, sicut Petro circumcisiouis, cum cognovissent graciam Dei, que data est michi, Jacobus et Cefas et Johannes, qui videbantur esse columpne, dextras dederunt michi 2? et Barnabe societatis. Cum, | venisset Cephas Antiochiam, in faciem ei rcstiti, quia reprehensibilis erqt. | Paulo niliil contulcrunt columne ecclesie.
p. 78: Data est, | michi potestas in celo et in terra, euntes igitur docete omnes gcntes servare omnia qnecunqne | mandavi vobis. | in mundum uuivcrsum, predicate evangelinm omni creaturc; | Potestas iurisdiccionis data est omnibus.
p. 79: qui plns omnibns laboravit,
```

---

## Chunk 05-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-05-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-05-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "80.24–83.27"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 80.23); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "659 words; 629 unanimous or majority-real; 18 settled by vote (R2 7, R3a 5, R5a 6); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n141–n144 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 5, part 1: [TITLE]

## ¶1 · 80.24–83.27

> [p. 80] Supersunt alie tres sentencie premittende: prima sive Romanus pontifex sive quicumque alius fuerit Christi archivicarius, debet vivere maxime exproprietarie et esse a mundo maxime elongatus; patet ex hoc, quod debet esse inter viantes maxime virtuosus et in conversacione Christo similior. Ipse autem sic vixit, ut ex fide [p. 81] scripture sepe declarata supponitur; quomodo igitur non oportet eius proximum vicarium conversari conformiter. Hoc enim movebat Petrum, Johannem et ceteros apostolos, qui potuerunt facillime, copiosissime et splendidissime fuisse dotati j et tamen ex religione et debito imitandi magistrum illud omiserant. Johannes autem, qui post ascensionem Domini septuaginta annis et amplius in maiori parte vixit fixe in pace, potuit dotasse suam ecclesiam, si fuisset expediens, cum silvestres frondes mutavit in aurum et fragmina saxorum in gemmas, sed in detestacionem amoris pecunie. Et revera ista sentencia de verbis et factis apostolorum daret fidem fidelibus, quod proximi Christi et Petri vicarii debent exire de mundo et conversari similiter et quod conversacio illa perficeret statum cleri. Christus enim ipsam elegerat in se et suis apostolis: quod omnipotens et omnisciens non faceret, nisi quia scivit quod perficeret statum suorum militum. Et idem confirmatur ex decretali ecclesie, quam papa Nicolaus tercius in sexto incorporat, Exiit qui seminat, ubi declarat quod status fratrum Minorum est ideo celestis et perfectissimus, quia statui Christi et apostolorum simillimus. Et ex istis credo quod ecclesia Romana, decretisteet fratres, sed specialiterfratres Minores, defenderent istam sentenciam. Aliter enim non crederetur alicui decretali, cum illam que evidencius fundatur ex scriptura ipsimet parvipendunt. Et conformiter dicitur ad obiectum quo dicitur Johannem XXII ordinasse decretales multas [p. 82] contra istam sentenciam. Quis, inquam, crederet talibus prepositis, quorum unus sine fundacione alteri contradicit? Scolares igitur legis papalis detenderent decretalem predictam, quia aliter non crederetur alicui ipsorum textui, sed eo ipso quo textus eorum sic asserit foret sentencia minus credibilis et de mendacio plus suspecta; nec dat fidem quod papa subsequens approbat hoc vel illud, quia sequentes sunt communiter minus religiosi et plus ignari; ideo debet eis minor fides in talibus adhiberi. Et istam sentenciam credo fratres et specialiter Minores velle defendere, quia aliter indubie ipsi tamquam mendaces ypocrite multipliciter perturbarent et molestarent ecclesiam. Item, quantum ad scolasticos in fide ecclesie credo quod ipsi consentirent eidem sentencie; nam bonum quod afferunt seculares divicie, non est nisi mundi prosperitas. Sed illam tam sancti doctores quam oraciones ecclesie docent despicere, igitur cum pauperies affert bonum spirituale, videtur quod superhabundans dotacio magis imperficeret clerum Christi. Confirmatur primo per hoc quod, cum imperatores sint pontifices, ut patet distinccione De Capitulis, videtur quod ante dotacionem ecclesie ipsi erant summi pontifices, quia tunc episcopi exproprietarie viventes erant miseri et egeni, cum caruerunt perfeccione quam modo ecclesia habet ex mundi diviciis. Illam autem perfeccionem diviciarum pertinencius tunc habuerunt cesares, igitur undequaque ipsi erant perfecciores pontifices, et sic summi dupliciter tam quoad seculum quam ad Deum. Et ex isto videtur dotacionis imperfeccio quod recipientes illam inperfecerant dominos qui dotarunt.. Sed dominium [p. 83] Christi, quia spirituale fuit, nulli perfeccioni incompossibile, fuit perfeccius. Cum igitur secundum legem ecclesie XIV q. V Denique si non potest sacerdos non debet illi officio vel arti intendere, per quam sequitur deterioracio proximi, videtur quod non debent intendere proprietati civili. Si enim renunciacio temporalium per viam elemosine sit perfecta in laico, multo magis in clerico. Illi igitur qui tantum imperfecerunt laicos, remitterent illis sua dominia ex causa multiplici. Omnis enim, qui se regem facit, per quod diminueretur imperium, contradicit cesari. Oportet igitur quod temporale dominium ponat plus imperfeccionis quam perfeccionis in clerico. Similiter, ultra vite necessaria non est perfeccio in mundi diviciis, nisi ad eas debite regulandum, sed hoc officium est alienum clerico, igitur et superhabundans possessio, sicut docet Apostolus Thim. VI. Regimen enim spirituale et regimen corporale, sicut et occupacio eorum, mutuo se retardant. Et hinc dicunt sancti quod divicie sunt pondus anime. Et quantum ad securitatem habendam et clerum multiplicandum, patet quod illa mundi insecuritas est meritoria et pertinens Christi discipulo, ut patet Math. VI. Mundi autem securitas est fallax et irreligiosa et solum affectabilis imperfectis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 80.26: Christ's chief-vicar should be free from all worldly cares.
- 81.5: The apostles did not endow churches, though St. John could easily have done so.
- 81.19: Christ chose a poor lite for himself and his apostles. Nicholas III. praised the Minorites for their poverty.
- 82.1: The utmost we can infer from the contradiction of John XXII is that neither pope speaks with authority.
- 82.24: The emperors are pontiffs and if endowment of pontiffs is good, they should keep it for themselves,
- 83.4: The clergy should not accept a gift which injures the giver.
- 83.15: There is no perfection in wealth save in ordering it properly, but this is not the duty of the clergy

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 80: *CAPITULUM QUINTUM.* [HEAD]
  - 80: *quicumque* (25 is the line number) [R4]
  - 81: *illa* [R3]
  - 81: *scivit* [R4]
  - 82: *Capitulis* [R4]
  - 83: *deterioracio* [R4]
  - 83: *∅* (15 is the line number) [R4]
  - 83: *clerico* [THIN]
  - 83: *igitur* [THIN]
  - 83: *illa* [R3]
  - 80: *exproprietarie* (LEFT-nw: one word; print = exproprietarie) [OVERRIDE-SCARPLATE]
  - 82: *exproprietarie* (S-split: one word, no split in print) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 80:
12. ita quod. B: quod si. 17. ipsam. B: iam; A in marg. : Romano
pontifici subesse non est de necessitate salutis. 23. A in marg.: Cap. V.
27. A in marg : Exproprietarie vivere debet vicarius Christi.

p. 81:
3i. A in marg. : Decrelales invicem contradicunt scilicet Nicolai 111 et
Johannis XXII.
ii. Sarum Missal First lesson for S. John's day. Gf. De
Ecclesia pag. 189. 23. De Verborum Signif. V, 12, 3.
De Potestate Pape. 6

p. 82:
23. Dist. ,X. cap. IX: Leges imperatorum cuslodiri oportet.

p. 83:
3. Decreti Secunda pars. causa XIV, q. V. cap. X.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 81: Exitt qui seminat,
p. 82: De Ccipitulis,
p. 83: Denique si 1 non potest
```
