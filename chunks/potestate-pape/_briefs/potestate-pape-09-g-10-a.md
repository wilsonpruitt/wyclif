# Translation brief: potestate-pape 09-g–10-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-09-g.md chunks/potestate-pape/wyc-potestate-pape-09-h.md chunks/potestate-pape/wyc-potestate-pape-10-a.md` once and fix what it reports.
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

## Glossary (the 270 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate / suppliant | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. Of one who prays to God himself (*devotus Dei orator*, *Pot. pape* 68.17) "suppliant", with a **C** note; ruled 2026-10-07. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| fantasticus | imaginary | Cf. *fantasia* "imagination". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 203.4). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 09-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "214.3–218.24"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "995 words; 921 unanimous or majority-real; 52 settled by vote (DEL 1, R2 28, R3a 13, R5a 10); 22 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n275–n279 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 7: [TITLE]

## ¶1 · 214.3–215.17

> [p. 214] Et quantum ad implicatum de eleccione humana patet ex sepe dictis, quod confirmatur ex lege triplici; primo docetur LXXIX distinccione: Si quis pecunia vel gracia humana vel tumultu populari sine canonica eleccione fuerit intronizatus, non apostolicus sed apostaticus habeatur. Cum igitur sit maior error in eleccione activa, quando eligentes coacti sunt a dyabolo eligere personam quam Deus reprobat, quod patule patet ex opere et omissione papalis officii, multo magis vel a pari sequitur, quod electus talis non apostolicus sed apostaticus est habendus. Non enim licet humanitus reprobare, ut ex fide supponitur, nisi ut Deus ex lege sua docuerit reprobandum; nec valet vel deficit humana eleccio nisi de quanto eleccioni divine consentit vel discrepat. Ex quo patet, cum stat electores cogi humanitus ad eligendum aput Deum ydoneum, quod dicta lex debet intelligi, quando militaris vel popularis tumultus cogit ad eligendum inhabilem, quare igitur non, si dyabolus vel peccatum collegii electorum et observatis humanis ritibus cogit ad eligendum tam inhabilem, eque non apostolicus sed apostaticus habendus est? Nec est probacio legis humane tam valida, sicut sensibilis probacio docta ex vita prepositi: nam maior capta ex lege Domini et minor capta ad sensum ex vita prepositi, concludunt cercius, quam evidencie palliate ex humanis legibus. Secundo docetur eadem sentencia ex lege Jeronymi distinccione [p. 215] XL sic loquentis: Non est facile stare in loco Petri et Pauli et tenere cathedram, quia non sanctorum filii sunt, qui tenent loca sanctorum, sed qui exercent opera eorum. Ex quo patet quod nemo sit papa, nisi sit Christi et Petri filius, imitando eos in moribus, sed sicut non subiacet potestati eleccionis humane hoc facere, sic nec subiacet potestati humane papam constituere. Si autem vocetur papa quicumque quem occidentalis ecclesia acceptat ad capitaliter decidendum causas ecclesie, ad precipiendum fidelibus infundabiliter et blasfeme pro congregandis pecuniis et mundanis honoribus, abusio est termini infundabilis, iuxta quam oportet in casu concedere, quod maximus hereticus et antichristus sit papa, sed et rudissimus laycus vel femella; et periret fides vel religio capiti ecclesie adhibenda.

[ENGLISH]

## ¶2 · 215.19–217.13

> [p. 215] Unde notaremus cronicas predictas, quomodo inolevit papalis dignitas. Et narrat dominus Ardmacanus libro VII cap. XXIV de questionibus Armenorum, quomodo imperator Constantinus circa annum domini trecentesimum primum hoc censuit et precepit, quod suus episcopus ab omnibus papa vocaretur. Et Foca imperator circa annum domini sexcentesimum hoc idem ex cleri instancia confirmavit, ut legitur in suis annalibus, quomodo igitur saltaret in summum sacramentum ecclesie, quod imperator terrenus tam irreligiose instituit, ymo ut inquit: Si imperator Thartarie ecclesiam de Cambalek aut de Cathay conversus ad [p. 216] christianismum caput omnium aliarum ecclesiarum constitueret, cederet ceteris paribus capitalitas Romane ecclesie. Horribile itaque atque necessario defectibile fundamentum ecclesie a seculari principe ita inductum. Numquid credimus quod humana eleccio plus iuris per se tribuit quam Christi eleccio? Christi autem eleccio non est per se sufficiens ad constituendum quamcumque partem ecclesie, cum requiritur eterna predestinacio cum gracia consumante. Et hinc credo quod ille qui nichil facit ex indifferencia reliquit nobis exemplum ad consenciendum isti sentencie per hoc quod ipsemet elegit dyabolum. Joh. VI, 71 dicitur: Nonne duodecim vos elegi et unus ex vobis dyabolus est? Tercio docetur eadem sentencia ex decreto beati Jeronymi posito XXIV questio I: Quoniam vetus oriens, ubi dicens mistice multa commendabilia de Romana ecclesia subiungit condicionem, quam oportet de ipsa subintelligi: Fatiscat, inquit, invidia Romani culminis, recedat ambicio; cum successore piscatoris et discipulo Christi loquor: Et concludit in fine. Quicumque tecum non colligit, spergit, hoc est qui Christi est, Antichristi est. In qua lege sunt tria notanda, primo quod Romana ecclesia est ubicumque habitaverit universitas fidelium viatorum, sic quod si iam non esset alius Romanus christianus, adhuc fideles conversi a quocumque apostolo, quia sunt discipuli Petri et Pauli, qui fuerunt Romani, possunt dici Romana ecclesia; tanta namque fuit Christi et omnium apostolorum concors [p. 217] amicicia, quod christiano sequente unum eorum in moribus, sequitur eorum quemlibet cuiuslibet eorum in gradu suo discipulus. Satis est, cum et omnino oportet quod christianus sit Christi discipulus, et sic nitetur explanacio beati Jeronymi in fine addita, quando dicitur: Quicumque non colligit cum Romano pontifice spargit, hoc est, inquit, qui Christi non est, Antichristi est, non tamen quod Romana ecclesia sepe sumitur pro qualicumque papa et suis cardinalibus, ubicumque habitaverint, quomodolibet conversando, sed ista significacio seculariter et infundabiliter est extorta, et ideo nimirum intricat ecclesiam.

[ENGLISH]

## ¶3 · 217.14–218.6

> [p. 217] Secundo notandum ex dicto beati Jeronymi quod quicumque diviserit contra Christum est Antichristus, cuiusmodi sunt superbi et specialiter sacerdotes cesarei legi Christi contrarii. Nam secundum beatum Gregorium nullus in ecclesia magis nocet, ut allegatum est ex secundo cap. primi De Cura Pastorali, et per consequens nullus est nequior Antichristus. Et isto modo loquitur decretum de Antichristo sub autoritate Gregorii, XVI questio VII: Pervenit ad nos, ubi dicitur, quod quidam episcopi consumunt bona pauperum tribus modis: primo in militibus et aliis laycis, qui ipsos fovent et protegunt in gloria seculari, secundo in monstruosa familia et tercio quod est gravius in consanguineis. Et ex diffinicione sancti talis episcopus inter maximos here: oticos et antichristos non minimus habeatur, et forte si omnes episcopi hodie in Anglia cum religiosis et secularibus eis consentaneis essent signati in fronte signo bestie, pateret quod longe [p. 218] plures quam sunt catholici ex parte Christi forent infideles, quia heretici et realiter antichristi. Sic autem loquuntur tot sancti doctores de antichristis et hereticis cum lege ecclesie et scriptura. Alias autem significaciones somniant ut heretici et antichristi absconsius delitescant.

[ENGLISH]

## ¶4 · 218.7–218.24

> [p. 218] Tercio notandum quod omnes leges que loquntur de papatu et obediencia fienda Romane ecclesie subintelligende sunt cum condicione, quod illa ecclesia correspondenter ad nomen excellencie in ministerio faciat recompensam. Aliter enim beatus Petrus non foret capitaneus inter apostolos, ut patet ex dictis; et aliter beatus Jeronymus distinccione XL allegata cum archidiacono contradiceret sibi ipsi, cum aliter racione loci et nudi nominis consenciendum foret in casu pessimo antichristo. Sicut enim Deus non potest facere hominem album sine albedine, sic non potest hominem facere papam vel membrum ecclesie sine inducta debita qualitate, ad quod locus vel eleccio humana est impertinens, nisi de quanto consentanea est dominio ipsum vere notificans populo, quod si false promulgat, est error in ianuis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 214.3: False election makes an apostate, not apostolic.
- 215.4: A pope is not truly such unless he follows Christ and Peter.
- 215.19: The papal dignity is founded on a grant of the emperor who had no right to make such.
- 216.11: Even Christ s election is not enough without predestination as Judas shews,
- 216.25: The Roman Church is wherever the mass of the faithful are.
- 217.14: Proud and Cesarian priests are Antichrists.
- 217.28: Such are more numerous in England than true priests.
- 218.7: Obedience is not due to the Roman Church unless it ministers truly in return.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 214: *Nec* [R4]
  - 216: *caput omnium* (one main token covers two printed words) [THIN]
  - 216: *aliarum* [THIN]
  - 216: *constitueret* [THIN]
  - 216: *paribus* [THIN]
  - 216: *capitalitas* [THIN]
  - 216: *Romane* (hyphenated Ro-|mane; main token holds the whole word) [THIN]
  - 216: *ecclesie* [THIN]
  - 216: *seculari* [R4]
  - 216: *∅* (s is the end of the English side-note "Christ's") [R6]
  - 216: *predestinacio* (hyphenated predesti-|nacio; main token predestinobis is the whole word garbled. NB main scan has lost the following lines (nacio cum gracia ... ) with no GAP flagged) [THIN]
  - 216: *Quoniam* (zoomed leaf: Q with tail) [R4]
  - 216: *non* [R3]
  - 217: *non* [R3]
  - 217: *non* [R3]
  - 217: *ista* [R3]
  - 217: *tribus* [R4]
  - 217: *in* [R3]
  - 218: *heretici* [R4]
  - 218: *fienda* [NW]
  - 218: *illa* [R3]
  - 217: *Jeronymi* (S-split: one word; initial is J, not T) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 214:
5. Codd. in marg. : Papa apostaticus. <>. Codd.: vel deest.
ayut : B: caput. 24. Codd.: electori. 29— 32. lege — lege twice.
6. Decr. Prima pars, dist LXXVIIII, cap. IX.

p. 215:
2. Codd.: Petri et Petri tenere. 20. B in marg. : Papa. 25. Codd.
in marg. : Papam vocari qnis institnit.
1. Decr. Prima Pars dist. XL, cap. II. 2 5. Sic et in Poly-
chronico V, 416; Hic impetravit ab Augusto Phoca, ut ecclesia
beati Petri Romae caput foret omnium ecclesiarum in orbe.

p. 216:
7. Codd. in marg. : Eieccio huihana non est efficax ad facienchtm
dignum prelatum. 19. V,-. de ipsa docst. 20. B: fatiscat /.cesset;
A: cesset superscriptum. 24. Codd.: leges. 3o. Codd. in marfj : Ro-
mana ecclesia quid est.

p. 217:
9. B: qnod deest; ib. A: per. 22. Codd. : Antichristo..
20. Gregorii, De Cura Past. 1. c. 23. Cap. III loosely
quoted. 28. Cap. II Non est facile.

p. 218:
7. Codd. in marg. : Obediencia ecclesie Romane. o. 15: sub con-
dicione. 27. Codd. in marg. : Sedes quatnor Romana, Alexandrina,
Anthiocena, Constantinopolitana.
27. Cap. II.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 214: Si quis pecunia vci gracia humana vel tumuttu poputari sine canonica eleccione fuerit intronizaius, non apostoticus sed apostaficus habeatur.
p. 215: Non est facile stare in loco Pelri et Patili et tenere cathedram, qnia non sanctomm filii snnt, qui tenent loca sanctomm, sed qni exercent opera eomm. | Si imperator Thartarie ecclesiam de Cambalek ant de Cathay conversus ad
p. 216: christianismum caputomnium aliarnm ecclesiarum constittieret, cederet ceteris paribtis capitalitas Romane ecctesie. | Nonne dtiodecim vos eJegi et unus ex vobis dyabolus est? | Ouoniam vetus oriens, | invidia Romani cuJminis, recedat | ambicio; cum successore piscatoris et discipuJo Cliristi Joquor: | Ouicumque tecum 11011 coJJigit, spergit, hoc est qui Christi 11012 est, Autichristi est.
p. 217: Quicumque non colligit cum Romano pontifice spargit, hoc esty | qui Christi non cst, Antichristi est, | Pervenit acl nos, | quod quidam episcopi consumunt bona pauperuni tribtis modis: primo in militibus et aiiis laycis, qui ipsos fovent et protegunt in gloria secularij secundo in monstruosa familia et tcrcio quod est gravius iu consanguineis.
p. 218: Romana ecclesia non ab apostolis, sed a Domino primatum obtinuit, ct post iJlam primam sedem secunda sedes est apud AJexandriam, a beato | Marco et evangelista Petri discipulo consecrata; tercia sedes est apud Antliiochiam, ubi Petrus ante-
```

---

## Chunk 09-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "218.25–222.18"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "819 words; 744 unanimous or majority-real; 56 settled by vote (DEL 2, R2 36, R3a 13, R5a 5); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n279–n283 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 8: [TITLE]

## ¶1 · 218.25–221.16

> [p. 218] Et patet ad quem sensum valent leges de eleccionibus et de locorum particularium dignitate, ut XXII distinccione: Sacrosancta dicitur, quod Romana ecclesia non ab apostolis, sed a Domino primatum obtinuit, et post illam primam sedem secunda sedes est apud Alexandriam, a beato Marco et evangelista Petri discipulo consecrata; tercia sedes est apud Anthiochiam, ubi Petrus antequam [p. 219] Romam venerat, sedit episcopus et Ignacium episcopum constituit, ubi primum christianorum nomen exortum est et post synodus decrevit Constantinopolitanam ecclesiam tenere secundum sedem post Romam, propter hoc quod sit quodammodo nova Roma; frivola forent ista, nisi sedes dicta factis compensent. Ideo dicit Gregorius ibidem: Cum culpa non exigit, omnes secundum racionem humilitatis equales sumus. Et confirmacio est quod iste tres sedes a nostris tamquam scismatice sunt abiecte, et ipsi econtra censent nostros scismaticos, et Asyani et alii fideles reputant utrosque deliros maniacos, constituentes in suis ecclesiis sedes alias, asserentes vere, cum non locus sed virtus gentem sanctificat, quecumque ecclesia est maior, que humilius sequitur Ihesum Christum. Et ista est vera sentencia, cum Joh. IV. 20 dicit Veritas mulieri Samaritane opposite Christo: patres nostri in monte hoc adoraverunt, et vos dicitis quia Jerusolimis est locus in quo adorare oportet; venit, inquit, hora et nunc est, quando veri adoratores adorabunt patrem in spiritu et veritate. Cum enim spiritus sit Deus, quemlibet locum replens, patet quod nec oportet m montem altum ascendere, ut Deus melius audiat preces nostras, ut Samaritani ex gestis patriarcharum crediderant, nec oportet in templum Salamonis cum Yudeis ascendere sed adorare in spiritu et montuose aspirando ad celestia secundum memorativam potenciam anime, scilicet intelligenciam, et cum anima sit, ubi afficitur, iuxta illud Apostoli ad Phil. III. 20 nostra [p. 220] conversacio in celis est, patet, quod sic orans mons altus efficitur per Deum sibi ipsi, et ideo Veritas docens nos patrem orare Matth. VI. 9, docet consideracionem nostram incipere ab altitudine adorati: Pater noster, qui es in celis etc. quantum ad templum Yudeorum Jerusalem, oportet adorare in veritate, sic quod vita non discordet mendaciter a peticione et animo adorantis, et tunc fit templum infinitum domino prestancius quam basilica Yudeorum, quia I. Cor. III. 16 dicit Apostolus: templum Domini est, quod estis vos. Quando enim est veritas in conversacione et veritas in peticione, que quidem veritas est adequacio ad intellectum divinum, tunc ex plena conformitate voluntati divine, orans sic mente et spiritu constituitur templum Dei, et tunc sicut dicit digne primam peticionem oracionis dominice Deo patri propter intellectus sublimitatem, sic potest digne dicere duas peticiones sequentes ad secundas personas alias, cum taliter difformem oportet trahi ad regnum, ubi erit perfecte voluntatis increate et create conformitas. Ideo oramus, quod sicut in celo est plena conformitas sic in terra sit proporcionaliter conformitas voluntatum. Et patet ex ista duplici racione orandi, quomodo verificantur decreta distinccione XL: Non est facile cum duobus capitulis sequentibus et capitulo: Multi sunt sacerdotes cum eis similibus. In quibus plane docetur quod locus quicumque sicut et sacramentum vel ritus sensibilis est adoracioni isti et preeminencie persone apud [p. 221] Deum impertinens, nisi forte per accidens excitaverit sanctitatem, unde signum est, quod adoramus samaritane sive yudaice tamquam irracionale animal, reptans depresso capite mentis nostre, quod tantum loca et cerimonias observamus. Christus autem ad hoc ascendit in celum, ut parvipendentes hec temporalia ascendamus per scalam virtutum ab istis sublunaribus in quibus infigimur ad spiritualia bona celestia finaliter affectanda. Unde Veritas cerrespondenter ad fidem mulieris, qua vere credidit Christum esse prophetam, ipsam alloquitur: Mulier, crede michi, quasi diceret propter imperfeccionem fidei es longe a sponsa, sed cum salus ex Yudeis est, oportet quod infundamento scale orandi statuens tibi substanciam fidei credas michi.

[ENGLISH]

## ¶2 · 221.17–222.18

> [p. 221] In istis igitur ymaginibus et fantasticis post dotacionem et affeccionis subversionem delusa est ecclesia in penam peccati et specialiter in constituendo sibi principem tamquam Christum. Et sic cum protestacione predicta intelligo illud Matth. XXIV, 15: Cum igitur videritis abhominacionem desolacionis, que dicta est a Daniele propheta, stantem in loco sancto, qui legit intelligat. Locus autem sanctus videtur michi esse status sanctus, quem papa vendicat, ideo dicitur stantem et Mar. XIII. 14 dicitur stantem, ubi non debet. Revera, quod auctoritate et imperio cesaris vel falsa eleccione cardinalium constituatur summus Christi vicarius, est abhominacio in abstracto, et si fideles anime viderent clare utrobique statum spiritualem ecclesie, quomodo solebat in ea presidere unus paterfamilias, qui graciose acceptaret invitando, pasceret refovendo atque defenderet [p. 222] adiuvando quoscumque suos domesticos. Modo autem invenirent in eadem domo ecclesie presidere unum blasfemum ypocritam, omnino condicionis opposite, non mirum si plurimi desolentur, ut si itinerans solebat hospitari cum uno patrefamilias magnifice largitatis et post inveniat monstruosam beluam, que in hospites famelice, subdole et proditorie tyrannizet, intrans domum: videndo talem sedere in cathedra pii patrisfamilias desolaretur non modicum in aspectu. Sic igitur ego intelligo abhominacionem desolacionis prophetatam et evangelizatam quam Christus precipit parti intellectuali ecclesie intelligere ex effectu. Nec mirum si posteriores docti ab experiencia noscant hunc sensum particularius quam sancti priores quibus non est ex effectu vel prophetice revelatus. Non enim generaliter noticia sensus scripture et sanctitas correspondent.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 218.25: Place is of little importance.
- 219.8: Of the four chief sees three are now schismatic.
- 219.23: We gain nothing by going up a mountain, like the Samaritans, or into Salomon's temple, like the Jews.
- 221.17: The popedom is the abomination of desolation spoken of by Daniel and Christ.
- 222.1: A blasphemous hypocrite usurps Christ's place.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 218: *Et* [R4]
  - 218: *apud* [R4]
  - 218: *Anthiochiam* [THIN]
  - 218: *Petrus* [THIN]
  - 219: *venerat* [THIN]
  - 219: *Ignacium* [THIN]
  - 219: *episcopum* [THIN]
  - 219: *ubi* [THIN]
  - 219: *christianorum* [THIN]
  - 219: *exortum* [THIN]
  - 219: *est* [THIN]
  - 219: *humilitatis* [R4]
  - 219: *Et* [R4]
  - 219: *veri* [R3]
  - 219: *III* [THIN]
  - 220: *∅* (box is on the English side-note (temple / adoring); no Latin word there) [R4]
  - 221: *loco* (print "stantem in loco sancto"; the main scan lost loco) [INS?]
  - 222: *Nec* [R4]
  - 220: *difformem* (LEFT-nw: print = printed; line number 20 follows) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 218:
7. Codd. in marg. : Obediencia ecclesie Romane. o. 15: sub con-
dicione. 27. Codd. in marg. : Sedes quatnor Romana, Alexandrina,
Anthiocena, Constantinopolitana.
27. Cap. II.

p. 219:
7. Codd. in marg: Dignitas ecclesie. 12. Codd. in marg.: Locus
oracionis non sanctificat hominem. 16. B : quemcunque. iq. opposite
(sic) Codd.: oppositi. 20. B: adorabunt deest.
5. Decreti Prima Pars, dist. XXII. eap. III. 8. Ibid. cap. IV,

p. 220:
6. Codd. in marg.: Ternplum Dei anima sancta. 23—24. s,c 1,1
terra sit proporcionaiiter couformitas decst. 2S. Codd. in marg. : Ho-
minis sanctitati locus est impertinens.
26. Cap. II, cap. III Kos qui presumns et W Kon loca.
28. Cap. XII.

p. 221:
11. B: a fide; ib. B: creditur, 14. Codd.: est. 22. Codd. in
marg. : Locus sanctus, in quo stat abhominacio dcsolacionis. 33. Codd.
in marg. : Paterfamilias verus.

p. 222:
7. Codd. in marg. : Exemplwn bonum; B in marg.: Noia. zi. A in
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 218: Romana ecclesia non ab apostolis, sed a Domino primatum obtinuit, ct post iJlam primam sedem secunda sedes est apud AJexandriam, a beato | Marco et evangelista Petri discipulo consecrata; tercia sedes est apud Antliiochiam, ubi Petrus ante-
p. 219: quam Romam vencrat, sedit episcopus et Ignacium episcopnm constituit. nbi primum christiauorum nomen exortnm est y | propter hoc \ quod sit quodammodo nova Roma; | Cum cutpa non exigit, omnes se- | cundum raaouem humititatis equales sumus. ht | patres nostri in monte hoc adoraverunt, et vos dicitis quia Jerusolimis est locus in quo adorare oportet; venit, | hora et nunc est. quando veri adoratores adorabunt patrem in spiritu et veritate.
p. 220: conversacio in celis est, | Pater nosfcr, qui es iu celis | templum Domini esf, quod esfis vos. | sicut in celo | sic iu ferra | esf facile | Multi sunf sacerdotes
p. 221: Mnlier, crede michtj | P°ff* om | Cum igitur videritis abhominacionem desolacionis, qne dicta est a Daniele propheta, stantem intoco sancto, qni legit inteiligat. | siantem, nbi non debet.
```

---

## Chunk 10-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "222.20–223.12"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 1 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "159 words; 145 unanimous or majority-real; 11 settled by vote (R2 9, R3a 2); 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n283–n284 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 1: [TITLE]

## ¶1 · 222.20–222.28

> [p. 222] Contra dicta arguitur per multa media tam raciones quam testimonia, et primo per deducens ad inconsequens probatur quod oportet papam esse dominum terre potissimum, quia aliter non sufficeret pro illo ministerio, sed subditi, eciam clerici, forent sibi inproporcionales quoad mundanam potenciam; ymo in possessione mundana vel securitate eius est occasio virtutis non vicii, et per consequens est racionabiliter appetenda.

[ENGLISH]

## ¶2 · 222.29–223.12

> [p. 222] In isto oportet ex fide credere summo medico Ihesu Christo, cuius est palatum oris mentis sanissimum, omnes autem infecti febribus, et [p. 223] cum alio genere morborum spiritualium, patimur discrasiam. Ideo sibi debemus credere, postposito nostro iudicio. Ipse autem verbis docuit et facto ac vita exposuit quod in diviciarum mundi affluencia est periculum et in earum parcitate ac remocione a seculo medicina, ideo reservavit illud regimen carioribus eius discipulis, ut patet Luce XVII et testatur Augustinus in De Ecclesiasticis Dogmatibus: Bonum est facultates cum dispensacione erogare pauperibus, sed melius est pro intencione sequendi Dominum semel donare, et absolutum sollicitudine egere cum Christo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 222.20: It is argued that the pope's secular greatness is needed for the protection of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 222: *CAPITULUM DECIMUM.* [HEAD]
  - 222: *ad* [R3]
  - 222: *arguitur* (LEFT-odd: box sits on Contra; word with junk is arguitur, line number 20 at line end; print clean) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 222:
7. Codd. in marg. : Exemplwn bonum; B in marg.: Noia. zi. A in

p. 223:
23. A in marg. : Nota. 29. A in marg.: Pape postulacio pvo sub-
9. Opp. tom. VIII, App. pag. 79, cap. XXXVIII. 22. Flores
Historiarum ed. by H. R. Luard vol. II, 184.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 223: Bomim est facultates cum | dispensacione erogare pauperibus, sed melius est pro intencione seqnendi Dominum semel douare, et absohitum sollicitudine egere cum Christo. | Avarus nou im- 20plebitur pecunia, et qui amat divicias fructus non capiet ex eis. | Otho nunccius domini pape | ostendit literas domini pape cousilio regui nostn | apud Westmonasteritim, in quibus papa allegavit scandalum Romane ecclesie et obprobrium vetustissimum, notam scilicet cupiditatis que radix esi omnium malorum, iu lioc precipue, quod nullus potest aliquod negocium iu Romaua curia expedire, 3onisi effusa magna summa pecunie et donorum exhibicione. Sed quoniam scandali huius et infamie Romana paupertas est causa, deberent matris in- | Pape postulacio pvo subsidio.
```
