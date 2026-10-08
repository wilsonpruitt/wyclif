# Translation brief: potestate-pape 10-k–11-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-10-k.md chunks/potestate-pape/wyc-potestate-pape-10-l.md chunks/potestate-pape/wyc-potestate-pape-11-a.md` once and fix what it reports.
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

## Glossary (the 287 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| symbolum | creed | *Utrumque simbolum* = both creeds, Apostles' and Nicene (T. p. 368). |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
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
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
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
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
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
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| brocardicum / brogardicum | brocard | The schoolmen's stock maxim. Ruled 2026-10-02 (*Eccl.* 16, 360.9). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
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
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio; pompa | boast; boasting; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 10-k: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-k.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-k
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "257.33–261.7"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 11 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "719 words; 682 unanimous or majority-real; 30 settled by vote (R2 22, R3a 6, R5a 2); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n318–n322 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 11: [TITLE]

## ¶1 · 257.33–258.18

> [p. 257] Notandum est tercio quod iste doctor videtur prudenter innuere quod nullus episcopus cesareus [p. 258] assumeret illud papale officium, quia obligat se ut sic quod sit in terris proximus sequax Christi, quod forte statui quem accipit est incompossibile. Ideo dicit Crysostomus Omelia XXVIII Operis Imperfecti: Quicumque, inquit, Domino? humilitati studente iactancie studet, non est imago Christi, et qui Domino paupertatem amante diviciarum amator est in hoc seculo, repellit a se Christi similitudinem nec est vere discipulus qui non imitatur magistrum. Studeat igitur Romanus pontifex, si imitatur simillime vias Christi. Ideo dicit Epistola XLIII: Scio, inquit, domini pape et sancte sedis hanc esse potestatem, ut de omnibus beneficiis ecclesiasticis posset libere ordinare, scio quoque quod quisquis abutitur hac potestate edificat ad gehennam. Ideo (ut videtur multis) descripcio quam ponit de papa non convenit apostolis, sed solummodo pape summo.

[ENGLISH]

## ¶2 · 258.19–259.8

> [p. 258] Unde propter talia verba quidam ad tantum insaniunt, quod dicunt neminem posse salvari nisi credat istum articulum fidei, quod quilibet papa sit per se causa tocius profectus spiritualis ecclesie. Unde Lyncolniensis Epistola XXXV: Ex generali debito subieccionis, quo non solum populus christianus sed totum humanum genus obligatur et sine cuius solucione nullus salutem consequitur, debitor sum sanctissime paternitati vestre excellentissimeque dominacioni plenitudinis, obediencie et reverencie, honoris et timoris. Et forte ex talibus verbis declamatoriis fuit iste doctor punitus a Domino per eum quem verbis floridis [p. 259] sic palpavit Si enim iste sit tam necessarius articulus fidei, cum apostoli et omnes christiani ante dotacionem non crediderunt istum articulum, videtur quod absit quod eorum quilibet sit dampnandus. Sed dicti beati possunt de sic errantibus dicere irridendo: Novi recentesque articuli fidei per constitucionem imperatoris venerunt quos non coluerunt patres eorum.

[ENGLISH]

## ¶3 · 259.9–259.23

> [p. 259] Item (ut patet ex decretis et cronicis tactis VIII capitulo) licencia et auctoritate cesaris factum vel fictum est quod generaliter suus episcopus sit caput ecclesie. Sed ille imperator non habet plus potestatem condendi novos articulos fidei quam quilibet alius christianus; sic enim posset condere novam legem Christi et legem conditam abrogare; non enim licet vel angelo de celo onerare sanctam ecclesiam novis articulis vel ritibus extra scripturam sacram a Spiritu Sancto doctam, ut patet in materia De Cessacione Legalium. Magna (inquam) libertas et privilegium fuit facilitas in qua Christus posuit suam ecclesiam, ut patet Gal. II; et hoc privilegium debent cuncti christiani defendere.

[ENGLISH]

## ¶4 · 259.24–259.32

> [p. 259] Item, non est possibile quod fidei orthodoxe sit falsitas substrata; sed sepe contingit quod Romanus pontifex non est papa, ymo posito quod sit; non est tantum necessarium ad salutem cuiuslibet christiani hoc credere, quod sine hoc non posset salvari, nam papa mortuo vel perverso non ex hoc titubat fides in quolibet christiano; et illud testarentur conversi per apostolos nostram nimirum demenciam deridendo.

[ENGLISH]

## ¶5 · 259.33–260.20

> [p. 259] Assumptum patet ex hoc quod aliter Deus necessitaret hominem ad menciendum et per consequens ad peccandum, et unus alius ymo sic [p. 260] illusus pie crederet eius contradiccionem, sicut christianus credit implicite esse verum; et sic oportet utramque sectam Urbani et Roberti dicere quod reliqua sit heretica, quia articuli fidei non limitantur sic ad loca, ut in ista villa teneantur credi et in proxima villa discredi. Nec valent sophismata quibus putantes subtiliare referunt quod papa potest facere novos articulos fidei et per consequens facere antiquos cessare, ymo facere christianos teneri credere falsitati, quia si quelibet veritas sit articulus fidei, tunc sacramenta potest facere, novos articulos ymo musca; sed et illum articulum sollempnizatum, quod iste sit papa, potest nedum imperator facere vel electores, sed quodcumque animatum vel inanimatum fuerit ad hoc movens. Sed evidencius foret, quod quis rogando Deum et perficiens papale officium, faciat se ipsum et plus timeat quod venenum peccati quam quod venenum corporis corrumpat istum christiane fidei articulum.

[ENGLISH]

## ¶6 · 260.21–260.32

> [p. 260] In ista materia dixi alias quomodo quedam est credulitas explicita vel distincta, et quedam est implicita vel confusa; et isto modo tenetur omnis christianus credere singulas veritates, quia tenetur credere Deum esse, quod est omnis veritas. Hoc autem omnis fidelis tenetur pro aliquo tempore vie distincte credere, et sic quicumque in Deum finaliter crediderit salvabitur, etsi non plus de grano synapis habuerit. Alios autem oportet plus et alios minus de fide distincte credere secundum quod plus vel minus de gracia ad hoc obligante habuerit.

[ENGLISH]

## ¶7 · 261.1–261.7

> [p. 261] Unde quidam vocant solum illas veritates catholicas quas oportet viatorem distincte credere articulos fidei, cuiusmodi sunt veritates expresse in symbolo; alii autem quamlibet veritatem catholicam articulum fidei, quia partem parvulam totalis fidei. Et illa concedit conclusiones sequentes, que equivocantibus videntur mirabiles.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 258.19: Some even say it is a matter of faith that the pope is the source of spiritual profit.
- 259.1: If so, all the apostles and primitive christians were damned.
- 259.9: The pope owed his position to being the emperor's bishop.
- 259.24: Faith is not dependent on the pope.
- 260.21: Explicit and implicit belief.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 258: *seculo* [NW]
  - 258: *non* [R3]
  - 258: *nisi* [R4]
  - 258: *credat* [R3]
  - 258: *totum* [R3]
  - 260: *illum* [R3]
  - 261: *illa* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 257:
2. Recte: debet se soli suo. 14. Codd. in marg. : Papa qualis debet
esse. 22. A in marg. : Cave.
De Potestate Pape. 17

p. 258:
4. Codd. in marg. : Papam dicunt esse necessarium ad salutem.
24. Codd. in marg. : Lincolniensis de papa nota bene. 27. B-.vestre et.
4. Opp. tom. VI, pag. 771. 12. Est Epistola XLIX Roberti
Grosseteste vid. Epp. pag. 145. 24. Roberti Grosseteste, Epi-
stolae, No. XXXV, pag. 123.

p. 259:
7. B: per constitulionem imperatoris deest 19. Codd.: a deest.

p. 260:
6. 13: sic teneantur. 8. Codd. in marg. : Articuli novi fidei a papa.
i3. Musca; hic aliquot vcrba exciderunt. 21. Codd. in marg. : Credu-
litas duplex.
21. E. g. Trial. p. 413.

p. 261:
3. Codd. in marg.: Articuli Jidei. 5. B: pervulgam. 9. Codd.
loquatur Jidelis. 28. A: et sic non.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 257: adunatant, status, decor et ordo universalis ecclesie debet subesse stio soli suisque cardinibus, hoc est, summo pontifici sibique assistentibus cardinalibus. Ideoque sancte Romane ecclesie debetur ab universis | ecclesie filiis devotissima obediencia, honoratissima reverencia, id est, ferventissimus anwr, subiectissi- 111 us timor. Hec et hiis similia ab eis debentur obligacius et forcius, qui pro subtimitate gradus ecclesiastici fastigio ecclesie, id est, summo pontifici | et cardinalibus adherent proximius.
p. 258: Domino? humilitati studente iactancie studet, non est imago Christi, et qui Domino paupertatem amante diviciarum amator est in hoc secnlo, repellit a se Christi similitudinem nec est vere disciputus qui 11011 imitatur magistrum. | domini pape et sancte sedis hanc esse potestatem, ut de omnibus beneficiis ecclesiasticis posset libere ordinare, scio quoque quod quisquis abutitur hac potestate edificat | ad gehennam. | Ex generali debito subieccionis, quo non solum | populus christianus sed totum humanum genus ob- | ligatur et sine cuius solucione nullus salutem consequitur, debitor sttm sanctissime paternitati vestre excellentissimeque dominacioni ptenitudinis, obediencie et reverencie, honoris et timoris.
```

---

## Chunk 10-l: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-l.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-l
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "261.8–265.16"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 12 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "937 words; 889 unanimous or majority-real; 28 settled by vote (DEL 1, R2 15, R3a 8, R5a 4); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n322–n326 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 12: [TITLE]

## ¶1 · 261.8–263.5

> [p. 261] Sed quomodocumque loquatur, fideli nichil insanius quam credere quod omnis fidelis debet credere quod omnis episcopus Romanus sit papa vel quod omnis subditus tenetur facere quicquid preceperit aut quod auctoritate et declaracione illius tenetur omnis christianus credere cuicumque scripture quam ipse limitat; nam mille sunt fideles, qui habent immediate a Deo fidem scripture independenter ab illo, eciam plus quam ipse; verumtamen cum multi pape sunt gloriosi post dotacionem ecclesie, quilibet christianus tenetur saltem confuse credere quod multi Romani episcopi sunt veri pape, et illi qui non fecerunt exaccionem talis fidei Antichristi; sed hoc non est generaliter ad laudem Romani pontificis, quia sic tenentur credere quod multi Romani pontifices non sunt pape, quia multi sunt dampnati, non membra sancte ecclesie, et sic de omni veritate tenetur omnis christianus credere quia est, etsi non sonat in pompam pape, quod omnis christianus tenetur ipsum credere esse papam, sicut non sonat in pompam cuiuscumque predestinati quod omnis homo tenetur credere ipsum esse salvandum, sicut omnem prescitum tenetur credere esse dampnandum, cum oportet Deum distincte illud cognoscere; ymo est michi evidens quod tam subtilis logicus atque theologus, sicut fuitRobertus Lyncolniensis [p. 262] non induceret hunc errorem fidei ad onus ecclesie, quod quemlibet Romanum pontificem tenetur credere esse papam, vel quod alius non habens ad hoc revelacionem de se ipso vel quocumque alio conversante secum tenetur expresse credere quod sit predestinatus vel apud Deum acceptus; de se ipso tamen tenetur hoc sperare et de aliis si moveat evidencia operis reputare. Nam ante dotacionem fuit privilegium et libertas ecclesie quod non tenebatur sic credere. Ideo non obstante dotacione debent ecclesie filii defendere pristinam libertatem; et sic intelliguntur multa dicta Roberti Grostest, que dicit condicionaliter aut reputative, quia aliter contradiceret sibi ipsi. Unde Epistola XXXVII. ut recitavi in fine secundi cap. libri V, dicit Lynconiensis quod iniustarum possessionum quas occupat ecclesia abscisio non est ecclesiarum imminucio, sed pocius earum pulcrificacio vel plurificacio. Et sic secundum eum et alios sanctos, qui iniuste occupat locum papalem, non sequendo Christum in moribus, non est papa vel clericus, sed unus dyabolicus an tipapa. Ex istis patet consideranti quantum malum et onus irreligiosum ecclesie induxit dotacio; ad tantum enim insaniunt pape cesarei, quod tenent cum suis satrapis quod papa non debet corripi ab aliquo viatore. Quod probant tripliciter: primo per hoc gentile principium: par in parem non habet imperium, cum igitur papa excedit omnem personam viantem, videtur quod non interest alicuius viantis papam corripere. Sed quantum ad illud patet, quod tam deficit [p. 263] in forma quam in materia; in forma, quia necesse est antecedens esse verum, cum necessario pater in Spiritum Sanctum non habet imperium sed missionem et tamen necessario sunt pares.

[ENGLISH]

## ¶2 · 263.6–263.10

> [p. 263] Iterum, necessario imperium habet pater in filium secundum humanitatem assumptam, et tamen absolute necessario sunt pares; ideo si nullus par in parem habet imperium, periret fides catholica.

[ENGLISH]

## ¶3 · 263.11–263.16

> [p. 263] Et iterum quoddam est imperium vicarium, cuiusmodi est omne humanum imperium, quomodo loquitur Apostolus prima Thym. VI, 17: Divitibus huius seculi precipe non sublime sapere. Quoddam autem imperium est per se vel originaliter autenticum super quamlibet creaturam.

[ENGLISH]

## ¶4 · 263.17–264.11

> [p. 263] Et patet quam nuda sit ista argucia quoad materiam et formam. Intelligit enim per hoc principium quod par non habet imperium autoritativum in suum parem, sub racione qua par est taliter imperanti. Sed quid obest huic quod excellencior virtute corripiat inferiorem in moribus, licet sit superior quoad statum. Aliter enim periret lex Christi, que ordinat quemcumque christianum prelatum peccabilem, et cum peccaverit; ab alio corrigendum, ut patetMatth. XVIII, in tantum quod si per impossibile Christus peccaverit, foret ab ecclesia corrigendus; cum enim sit frater noster Hebre. II. 12 et lex sua dicit universaliter: si peccaverit in te frater tuus, corripe eum, patet quod omnis viator peccando debet corripi a confratre. Aliter enim deficeret lex [p. 264] Christi ordinando remedium contra maculam sponse sue, cui Paulus contradicit Gal. II. cum pro levi culpa in facie restitit Petro pape; ideo nichil infidelius quam negare quod statu superior et inferior quoad mores potest corripi a subiecto. Ideo secundo arguitur per hoc quod papa gerit in terris vicem domini Ihesu Christi, sed ipsum non licuit alicui corripere, ut patet Matth. XVI, 23 ubi propter correpcionem Christi Petrus vocatur sathanas, igitur nec eius vicem gerentem licet corripere.

[ENGLISH]

## ¶5 · 264.12–264.16

> [p. 264] Sed ista argucia nimis claudicat, cum oporteret dicere quod omnis Christi vicarius sit impeccabilis sicut Christus: et sic vere concluditur quod nec papa nec alius debet corripi vel corrigi, in quantum sequitur caput Christum.

[ENGLISH]

## ¶6 · 264.17–264.21

> [p. 264] Sed tercio arguitur ex lege XXI distinccione Nunc autem divina, ubi dicitur, quod nullus sanctorum episcoporum ausus est in Marcellinum papam inferre sentenciam, sed dixerunt: tuo ore iudica causam tuam, non nostro iudicio subiacebis.

[ENGLISH]

## ¶7 · 264.22–265.5

> [p. 264] Sed constat quod illud verbum episcoporum non potest tollere legem Dei, qua in archiepiscopo Paulo corripuit papam Petrum, ut patet Gal. II. Ideo idem foret dicere quod non licet papam corripere et dicere quod est personaliter impeccabilis dominus Ihesus Christus vel ipseLucifer, qui per correpcionem fraternam non potest corrigi. Unde cum papa racione multiplici sit pronior et periculosior in peccando, oportet de correpcione et correccione sua prudencius precavere; et ad hoc ordinantur leges ecclesie, ut patet distinccione [p. 265] XL: Si papa, et distinccione LXXIX: Si quis pecunia; et aliter forent omnia facta in deposicione paparum iniusta et per consequens deponentes forent heretici, sicut et ecclesia approbans eius correpcionem et pape novi intronizacionem.

[ENGLISH]

## ¶8 · 265.7–265.16

> [p. 265] Et quantum ad dictum episcoporum de correpcione Marcellini, dicitur quod valde superfluum foret eos ipsum in tali casu corripere, quia perceperunt ex eius contricione quod fuit plene correptus a Domino, Ideo nimis levis evidencia foret ex isto facto concludere quod nullus papa debet in aliquo casu a fratribus reprehendi, ut patet ex libro beati Bernhardi ad papam Eugenium. Mille autem sunt blasfemie cum nonnulla intronizacione pape cesarei introducte.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 261.8: We are not bound to believe that every Roman bishop is pope.
- 262.20: If he does not follow Christ he is a devil and antipope.
- 262.28: Popes even declare that no one may reprove them.
- 263.2: It is said falsely that between equals there is no authority.
- 264.24: Such a claim implies that the pope is impeccable.
- 265.7: Case of Marcellinus.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 261: *nam* (15 is the line number) [R3]
  - 262: *secundi* (hyphenated se-|cundi; main token holds the whole word) [R3]
  - 262: *∅* (second half of se-|cundi, which the main scan already holds whole at pos 104) [INS?]
  - 263: *in* [THIN]
  - 263: *in* [THIN]
  - 263: *materia* [THIN]
  - 263: *in* [THIN]
  - 263: *noster* [R4]
  - 263: *universaliter* (30 is the line number) [R4]
  - 263: *peccaverit* [R4]
  - 263: *te* [R3]
  - 263: *frater* [R4]
  - 264: *Marcellinum* [R5]
  - 264: *papam* [R3]
  - 264: *nostro* [R3]
  - 264: *legem Dei* (one token covers two printed words) [R5]
  - 264: *qua in* (one token covers two printed words (qua in archiepiscopo)) [NW]
  - 265: *Marcellini* [R5]
  - 264: *licet* (W1: hcet -> licet (scans: hcet | hcet | licet | hcet)) [OVERRIDE-SCAR]
  - 261: *Romanus* (LEFT-nw: capital R) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 3o. Matth. XVIII, 2 5. (263.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 261:
3. Codd. in marg.: Articuli Jidei. 5. B: pervulgam. 9. Codd.
loquatur Jidelis. 28. A: et sic non.

p. 262:
2. Romanum ; B: christianum. i5. Godd. in marg. : Papa malus si
estpapa. 19. B : vel plurificacio in marg. 23. B : Ex isto. 25. Codd.
in mar£. : Papa non debel corripi, probat tripliciter. 26. B in marg. :
Moderni pontijices Romani sunt diabolici antipape. Rec. man.
16. De Civili Dominio III, p. 3o, Rob. Linc. Epp. pag. 226.

p. 263:
1. B: quam in matevia in forma deest. 2. B in marg.: Pulchritm
per totum. 6. B in marg. : Nota. 11. B in marg. : Nota. i5. Codd.
in marg. : Imperium duplex par habet imperium in parem.

p. 264:
25. Codd. in marg. : Correpcio patris necessaria. 27. Codd. in
marg.: Correpcio pape licita.
18. Decreti Prima Pars, Dist. XXI, cap. VII.

p. 265:
2, 3. B: iri posicione. 17. A: Cap. XI deest. 23. Sic ; B: si.
1. Dist. XL, cap. VI et dist. LXXIX, caP. IX.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 262: iniustarum possessionum quas occupat ecclesia abscisio non est ecclesiarum imminucio, sed pocius earum pulcrificacio vel plurificacio.
p. 263: Divitibus huius seculi precipe non snblime sapere. | frater noster | si peccaverit in te frater tnns, corripe eum,
p. 264: Nunc autem divina, | nullus sanctorum episcoporum ausus est in Marcellinum papam inferre seutenciam, sed dixerunt: tuo ore | iudica causam tuam, non uostro iudicio subiacebis.
p. 265: Si papa, | Si quis pecunia; | posuit quamlibet universitatem suam in mensura, J^ldl | numero et pondere, | Vestem autem sanctam qua utitur Aaron habebunt filii eius post eum, ut ungantur in ea et consecrentur ■\ Q manus eorum.
```

---

## Chunk 11-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "265.18–268.27"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 1 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "721 words; 597 unanimous or majority-real; 71 settled by vote (DEL 1, R2 38, R3a 30, R5a 2); 53 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n326–n329 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 1: [TITLE]

## ¶1 · 265.18–266.3

> [p. 265] Contra dicta arguitur per hoc quod Deus posuit quamlibet universitatem suam in mensura, numero et pondere, ut dicitur Sapiens XI, 31 et per consequens oportet esse ordinem in sacerdotali potestate sacramenta et sacramentalia ministrandi. Sic enim in lege veteri fuit unicus summus sacerdos, cui erant excellenciora officia limitata, in cuius signum Deus ordinavit unicam vestem sacerdotalem pro Aaron, ut patet Exod. XXVIII, 4; unde et consequenter dicitur: Vestem autem sanctam qua utitur Aaron habebunt filii eius post eum, ut ungantur in ea et consecrentur manus eorum. Summo autem sacerdoti appropriata sunt multa officia, ut patet Exod. XXIX, [p. 266] XXX et Levitici VIII, multo magis igitur in novo testamento, ubi debet esse in perfecciori ordine maior distinccio.

[ENGLISH]

## ¶2 · 266.4–266.8

> [p. 266] Hic dicitur quod prima conclusio est concedenda. Omne enim quod erit contingenter oportet esse necessitate ex supposicione, cum Deus necessario eternaliter noscit illud et ordinat vel ipsum vel de ipso bonum.

[ENGLISH]

## ¶3 · 266.9–268.27

> [p. 266] Sed pro materia argumenti notandum quod aliquis pretenditur esse ordo, in quo propter defectum ordinis homo peccat et aliquis ordo est, circa quem propter defectum preponderancie homo peccat. Pretenditur autem esse ordo, quod papa sit mundo ditissimus, et tamen est abusus ordinis abiectissimus, cum Christus cuius ordini strictissime obligatur fuit mundo pauperrimus; potest tamen titulo elemosine accipere benediccionem ab homine, sic quod nec sit exinde fastu vel avaricia soporatus nec a papali officio plus abstractus. Quod si elemosinacio perversa est in dominacionem, sancta predicacio in litis secularis defensionem et affeccio spiritualis lucri ecclesie in mundialium affeccionem, tunc est plena abhominacio desolacionis Dan. IX et Matth. XXIV capitulis prophetata. Et talem vocant quidam papam cesareum et alium condicionis opposite papam Christi. Unde beatus Bernhardus ad Eugenium destruit multas hereses istius materie, nam in fine libri IV loquitur contra dominium ecclesie sub hiis verbis: Consideres ante omnia sanctam Romanam ecclesiam, cui Deo autore prees, [p. 267] ecclesiarum matrem esse non dominam: te vero non dominum esse episcoporum sed unum ex ipsis, qualem de cetero oportet te esse. Considera formam iusticie, sanctimonie speculum, pietatis exemplar, assertorem veritatis, fidei defensorem, doctorem gencium, christianorum ducem, amicum sponsi, sponse paranimfum, cleri ordinatorem, pastorem plebium, magistrum insipiencium refugium oppressorum, pauperum advocatum, miserorum spem, tutorem pupillorum, iudicem viduarum, oculum cecorum, linguam mutorum, baculum senum, ultorem scelerum, malorum metum, bonorum gloriam, virgam potentum, malleum criminosorum, regum patrem, legum moderatorem, canonum dispensatore sal terre orbis lumen, sacerdotem altissimi, vicarium Christi, christum Domini postremo Deum Pharaonis. Talis debet esse papa: quod si in istis triginta quatuor deficiat induens vestem lupi oppositam, nullum est in ecclesia horribilius monstrum, ut docet in fine III libri et libro II: Nunc avdi canticum meum minus suave sed salutare. Monstruosa res gradus summus et: animus infimus, sedes prima et vita yma, lingua magniloqua et manus ociosa, sermo multus et: fructus nullus, vultus gravis et actus levis, ingens auctoritas et nutans subtilitas. Unde II in principio libri III declarat et modificat: potestatem, quam papa debet habere si vitam novam inculpabiliter recompensat et incipiens ab apostolis. a quibus oportet exemplari papalem potenciam Occumbebant. inquit, fortissimi bellatores: et:::: non succumbebant triumphabant eciam mortui; nimis confortatus est principatus eorum; constituti svr [p. 268] principes super omnem terram; eis tu successisti in hereditatem; ita tu heres et orbis hereditas, ac quamvis hec porcio te contingat, id sobria consideracione pensandum; non enim reor per omnem modum, sed sane quodamtenus; dispensacio, inquit, super illum tibi credita est, non data possessio. Et post detegit heresim, qua Antichristus extollit se super omne quod dicitur Deus. Si quis, inquit, usurpat hanc potestatem, contradicit illi, qui dicit: Meus est orbis terre et plenitudo eius. Non tu ille, de quo propheta: Et erit omnis terra possessio eius. Christus hic est, qui possessionem sibi vendicat et iure creacionis et merito redemcionis et dono Patris. Cui enim alteri dictum est: Postula a me et dabo tibi gentes, hereditatem tuam et possessionem tuam, terminos terre, possessionem et dominium, cede huic, tu curam illius habe, pars tua hec, ultra ne extendas manum. Et post obicit per hoc quod idem est preesse et dominari, sed hoc negat, cum bene preest, qui preest in sollicitudine, villa eciam subiecta est villico et dominus parvulus pedagogo. Ita et tu, inquit, presis, ut provideas, ut consulas, ut procures et serves, presis ut prosis, presis ut fidelis servus et prudens, ut des subiectis escam in tempore, hoc est, ut dispenses, non ut imperes; hoc fac et dominari te non affectes hominum homo, ut non dominetur tui iniusticia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 265.18: It is argued that God has made all things in order, which we are bound to keep.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 265: *suam* [R3]
  - 266: *VIII* (p. 266 strip from tractatusdepotes00wycl:327) [R5]
  - 266: *preponderancie* [R5]
  - 266: *Dan* [R5]
  - 266: *materie* [R3]
  - 266: *hiis* [R5]
  - 266: *sanctam* (p. 266 strip from tractatusdepotes00wycl:327) [THIN]
  - 266: *autore* (p. 266 strip from tractatusdepotes00wycl:327) [THIN]
  - 267: *matrem* [THIN]
  - 267: *cetero* [R4]
  - 267: *assertorem* (5 is the line number (main b)) [R4]
  - 267: *paranimfum* [R5]
  - 267: *ordinatorem* [R5]
  - 267: *tutorem* (10 is the line number) [THIN]
  - 267: *pupillorum* (main split the one printed word pupillorum into puri + rum; the whole word goes here) [THIN]
  - 267: *∅* (second piece of pupillorum, which main split (puri + rum); the whole word is at pos 54) [THIN]
  - 267: *ultorem* (hyphenated ul-|torem; main token holds the whole word) [R3]
  - 267: *terre orbis* (one token covers two printed words (terre, orbis)) [R3]
  - 267: *Domini* (main split Domini into do + miui; the whole word goes here) [THIN]
  - 267: *∅* (second piece of Domini (main do + miui); the whole word is at pos 88) [THIN]
  - 267: *postremo* [THIN]
  - 267: *III* [R5]
  - 267: *et* [R3]
  - 267: *infimus* [R3]
  - 267: *vita* [R3]
  - 267: *et* [R3]
  - 267: *et* [R3]
  - 267: *III* [R5]
  - 267: *modificat* [R3]
  - 267: *potenciam* (blurred line: main split potenciam into pc + er + iara (pos 190-192); the whole word goes at the first piece) [THIN]
  - 267: *∅* (piece of potenciam (main pc + er + iara); whole word at pos 190) [THIN]
  - 267: *∅* (piece of potenciam (box ciam.); whole word at pos 190) [THIN]
  - 267: *Occumbebant* (hyphenated Occum-|bebant; main token rbebant holds the m- and bebant, Occu is lost in the garbage of pos 192; whole word here) [THIN]
  - 267: *fortissimi* [THIN]
  - 267: *bellatores* (main split bellatores into beiiai + res) [THIN]
  - 267: *∅* (piece of bellatores (main beiiai + res); whole word at pos 196) [THIN]
  - 267: *et* [THIN]
  - 267: *non* (print "et non succum-|bebant": the main scan lost non and split succumbebant into 5 + u + bebant (pos 199-201); words reassigned in print order) [THIN]
  - 267: *succumbebant* (hyphenated succum-|bebant; see pos 199 (non) and 201 (∅)) [THIN]
  - 267: *∅* (bebant, the second half of succum-|bebant, given whole at pos 200) [THIN]
  - 267: *confortatus* (hyphenated con-|fortatus; main token holds the whole word) [R4]
  - 267: *constituti* [THIN]
  - 268: *tu* [THIN]
  - 268: *et* [R3]
  - 268: *quodamtenus* [R4]
  - 268: *illum* [R3]
  - 268: *est* [R3]
  - 268: *Deus* [R3]
  - 268: *Meus* [R3]
  - 268: *iure* [R3]
  - 268: *et* [R3]
  - 268: *eciam* [R3]
  - 268: *ut* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 265:
2, 3. B: iri posicione. 17. A: Cap. XI deest. 23. Sic ; B: si.
1. Dist. XL, cap. VI et dist. LXXIX, caP. IX.

p. 266:
(none)

p. 267:
2. unitm ex ipszs; codd.: mrnatnm. *at Codd. in. mirg. : Mon-

p. 268:
8. Codd. in marg. : Dominacio pape iJilerdicilar universali*.
12, i3. et iure ; codd.: opere creationis metiio, i3 Patris ; codd.: po-
testatis. 28. B. in marg. : Omnes pape post dotacionem e. v. dicuntur
cesarei sacerdoles. Rec. inan.
lo. Ps. XLIX, 11. 11. Ps. CIII, 27. 14. Ps. II, 8.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 265: Si papa, | Si quis pecunia; | posuit quamlibet universitatem suam in mensura, J^ldl | numero et pondere, | Vestem autem sanctam qua utitur Aaron habebunt filii eius post eum, ut ungantur in ea et consecrentur ■\ Q manus eorum.
p. 267: ecclesiarum mafrem esse non dominam: te vero non dominum esse episcoporum sed unnm ex ipsis, quaJem de ceiero oportet te esse. Considera formam iusticie. sanctimonie speculunij pietatis exemplar. bassertorem veritatis, Jidei defensorem, doctorem f gencium, christianorum ducem. | amicum sponsi. sponse paranimfum, cleri ordinaiorem. pastorem plebium, magistrum insipiencium^ refugium oppressorum, panpernm advocatum, miserornm spem, lotuiorem puri'.'. :rum. iudicem '.iduarum. ::uium cecorum, linguam mutornm, bacuJum senum. nliorem scelerum, maljrum meium. roncrum gisriam. virgam potentum, maUeum criminosorum, regum patrem, legum moderatorem, canonum dispensailtoretn. sal terre T orbis lumen, sacerdotem altzssimi, vicarium Christi, christum Domiui, posiremc Deum Pharaouis. | Xunc av.di canticum meum miuus suai: sed salutare. Monsiruosa res sradv.s summus e: ardmus infimus. sedes prima et vi:a yma. liuaua maxniloqua ei manus ociosa. serm: mvdius e: &u:::.s | nuJJus, vuJtus gravis et acins Jevis, ingens auctoritas et nutans subtiJitas. | fsriissimi beiiai:res e: '■:::: 5 u :::>::■:bebant, triumphabant eciam mortui; nimis confortatus est principatus eorum; comstUmH svr 2. unitm ex ipszs; | mirg.: Monstruosa r?s
p. 268: principes super omnem terram; eis tu successisti in hereditatem; ita tn heres et orbis hereditas, ac quamvis hec porcio te contingat, id sobria consideracione pensandum; non enim reor per omnem modum, sed sane quodamtemts; dispensacio, | super illum tibi credita est, non data possessio. | extollit se super omne quod dicitur Deus. Si quis, | usurpat hanc potestatem, contradicit illi, qui dicit: Meus est orbis terre et pleuitndo eius. Kon tu ille. de quo propheta: Et erit omnis terra possessio eius. Christus hic est, qui possessionem sibi veudicat et iure creacionis et merito redemciouis et dono Pairis. Cui enim alteri dictum est: Postula a me et dabo tibi gentes, hereditatem tuam etpossessionem tuam, terminos terre, possessionem et dominium, cede huic, tu curam illius habe, pars tua hec, ultra ue exteudas manum. | idem est preesse et dominari, | cum bene preest, qui preest in sollicitudine, villa eciam subiecta est villico et dominus parvulus pedagogo. Ita et tu f iuquit, presis, ut provideas, ut consulas, ut procures et serves, presis ut prosis, presis ut fidelis servus et prudens, ut des subiectis escam in tempore, hoc est, ut dispenses, uon ut imperes; hoc fac et dominari te nou affectes homiuum homo, ut uon domiuetur tui iniusticia.
```
