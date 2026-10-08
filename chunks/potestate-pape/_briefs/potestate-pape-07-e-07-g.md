# Translation brief: potestate-pape 07-e–07-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-07-e.md chunks/potestate-pape/wyc-potestate-pape-07-f.md chunks/potestate-pape/wyc-potestate-pape-07-g.md` once and fix what it reports.
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

## Glossary (the 275 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
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
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
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
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
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
| redarguere | to refute | T. p. 365. |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
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
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
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
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| demereri | to demerit | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 07-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "147.27–152.9"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "972 words; 913 unanimous or majority-real; 47 settled by vote (R2 30, R3a 6, R5a 10, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n208–n213 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 5: [TITLE]

## ¶1 · 147.27–152.9

> [p. 147] Ad quintum patet ex illo Mar. XIV quod P. et quilibet eius vicarius debet cum Christo vigilare attencius in custodia gregis sui, quia Psalmo CXX, 4 dicitur quod non dormitabit neque dormiet, qui custodit Ysrahel, quod si no mine [p. 148] tenus papa dormierit sompno spirituali letifero, nullus dampnabilius se ipsum condempnat et ad officium illud inhabilitat, cum sibi ipsi in vita et nomine contradicit. Nec debet communitas fidelium sequi talem; habet enim ex mendacio signum potissimum Antichristi, ut declarat Crysostomus Omelia VIII, exponens illud II. Thim. III, 1 In novissimis diebus instabunt tempora periculosa, ubi declarat processisse hereticos a mundi principio, dyabolo contra plantacionem Dei mendacium seminante. Et correspondenter de membris istorum causatum ut Caym contra Abel, filii Dei contra filios hominum, Abraham et Pharao, Yacob et Esau, Moyses et magi, prophete et pseudoprophete, apostoli et pseudoapostoli, Christus et Antichristus continue repugnarunt et continue opponebatur mendacium veritati. Dyabolus, inquit, et membra sua operibus nichil monstrant, sed verbis magna false promittunt, ut patet Genes. ubi dicit dyabolus: Nequaquam moriemini, sed eritis sicut dii. Quod si de maioritate potestatis pompose contendimus et in vita ac sanctis operibus sumus steriles, absolucionem a pena et a culpa pro pecunia promittentes et tamen in vivendo Christo conformiter subditos non iuvantes, sumus indubie Antichristi. Quod si torpemus in declaracione talium, Spiritus Sanctus necessario dissipabit consilium Achitofel, dividens membra Antichristi ab invicem fidelibus precipiens ne sequantur. Nam Matth. XXIV, 5 dicitur: Multi venient in nomine meo, dicentes quia ego sum Christus et multos seducent, quod cum necesse sit esse verum ad literam, patet quod oportet hoc verificari de pretendentibus se esse Christi [p. 149] vicarios, unde quia sofisticacione dyaboli nimis seducitur populus, non credens signo abhominacionis stanti in loco sancto Dan. IX cap. prophetato, abbreviabit Deus dies propter electos faciendo divisionem inter apostatas, ut vel sic noscatur veritas. Et statim de cavendo periculo divisionis subiungit, tunc si quis dixerit vobis: Ecce hic est Christus aut illic, nolite credere. Surgent enim pseudochristi et pseudoprophete, et dabunt signa magna. Ecce, inquit, predixi vobis. Istam propheciam Christi omnis catholicus tenetur credere. Et videtur michi ipsam posse exponi de istis dicentibus hodie se esse papas; uterque enim dicit se esse Christum Deum, et maioris vel pluris potestatis quam Ihesus noster; in cuius nomine tamquam eius summos vicarios referunt se venire; et certum est quod ista divisio est ad instruccionem ecclesie. Ideo videtur salubris doctrina Christi, quod neque nudis verbis dicencium, quod nunc papa sit Rome, nunc quod papa sit Avinione, debemus credere, sed ipsis operibus Christo conformibus, ut docet Joh. X, 38 de seipso; quia certum est, quod nuda verborum promulgacio nec fallax et subdola satraparum eleccio facit fidem de Christi vicario, sed ut dicit beatus Crysostomus: Nudis foliis verborum ut signis generacionis adultere innititur Antichristus, quia hoc est magis contrarium verbo Dei. Unde uterque istorum, ut michi videtur, debet contentari de isto regnorum responso: ex quo non claret eis ex eleccione vel opere quis est papa, quiescuntin fide filii Dei, quousque ecclesia plene doceatur, quis eorum fuerit verus papa, et supponentes [p. 150] utrumque eorum esse bonum sacerdotem atque catholicum, parati sunt obedire utrique secundum formam, qua Apostolus obedivit debite beato Petro. Et quicumque extorserit maiorem obedienciam est suspectus. Petrus enim non peciit obedienciam maiorem a populo nisi quod credatur fides Christi et efficaciter opere compleatur. Non enim peciit dominacionem seculi, pecuniam vel vectigal. Nec subest alteri eorum auctoritas plus querendi, et specialiter de regnis, populis vel personis exigendo pecunias vel pinguium beneficiorum collaciones, nisi fundare sciverit ex racione vel scriptura quod Christus vel Petrus obedienciam huiusmodi vendicavit vel debuit vendicare. Si autem alter eorum regno vel populo fidem Christi predicare voluerit vel fidem susceptam instar Petri confirmare miraculis; videtur michi quod populus gratanter debeat obedire, dominacionem autem ut venenum debet expellere, gracias agens Deo, qui abbreviavit et detexit venenosam tyrannidem Antichristi. Nec moveat quod tempora ista sunt prospera, Christus autem dicit; quod est tribulacio magna, qualis nunquam fuit. Loquitur autem de miserabili tribulacione anime maxima que iam instat, quia dormicio Symonis et Yude vigilia in cautelis faciunt litargire quod multi sompno letifero insensibiliter moriantur. Paratus sum autem revocare istam sentenciam, docto quod sit contraria fidei christiane. Sed videtur michi indubie quod non amplius quam ostensum est; debet catholicus talem ducem sequi vel ei ut Christi vicario obedire; et nichil [p. 151] infidelius quam quod oportet de necessitate salutis christianum exercitum tali capite regulari. Et patet quod in isto quinto argumento facto pro papa debet ipse diligenter attendere quod non sit ad instar Petri reprobati fumo fastus vel avaricie soporatus; de quo sompno dictum est alibi. Nam habere solum nomen Petri vicarii vel pastoris est ex mendaci ypocrisi magis dampnabile quam si foret homo huius prepositure, cum Gregorius beatus primo libro De cura Pastorali II cap. exponendo illud Matth. XVIII, 6 Qui scandalizaverit unum de pusillis istis minimis, qui in me credunt, expedit ei ut suspendatur mola asinaria circa collum eius et demergatur in profundum maris: Pastores, inquit, perversi in moribus quod verbis predicant, moribus impugnant; unde fit, ut cum pastor per abrupta graditur, ad precipicium grex sequatur; quia cum layci dicta prelatorum cognoverint, per opera pervertuntur. Hinc scribitur per prophetam: Causa sunt ruine populi sacerdotes mali, de quibus dicit Dominus per prophetam: Facti sunt domui Ysrahel in offendiculum iniquitatis. Nemo quippe amplius in ecclesia nocet, quam qui perverse agens habet nomen vel ordinem sanctitatis, delinquentem autem hunc redarguere nullus audet; et in exemplum culpa vehementer extenditur, quando peccator pro reverencia ordinis honoratur. Indigni namque, tanti ponderis pericula fugerent, si Veritatis sentenciam sollicite cogitarent, qui scandalizaverit etc. Per molam quippe asinariam secularis vite circuitus [p. 152] ac labor exprimitur et per profundum maris extrema dampnacio designatur. Qui igitur ad sanctitatis speciem deductus vel verbo ceteros destruit vel exemplo, melius profecto fuerat, ut hunc ad mortem sub seculari habitu terrena acta constringerent, quam quod sacra officia in culpa ceteris imitabilem demonstrarent, quia nimirum si solus caderet hunc utrumque pena inferni tollerabilior cruciaret.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 147.27: The vicar of Peter must be a watchful guardian of the flock.
- 148.5: If not, the faithful should not follow him.
- 148.29: Christ's prophecy of Antichrist.
- 149.10: It may refer to those who now claim to be popes.
- 149.28: They should Walt patiently for a decision and meanwhile serve the Church as true priests.
- 150.9: They have no authority to claim tribute and the nations should not allow their lordship.
- 150.28: Wyclif will recant if taught better.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 148: *sequi talem* (one token covers two printed words) [R5]
  - 148: *1* (old-style 1, x-height) [R3]
  - 148: *sed* (20 is the line number) [R3]
  - 149: *responso* [R3]
  - 150: *tempora* [R3]
  - 151: *fit* [R3]
  - 152: *labor* [THIN]
  - 152: *exprimitur* [THIN]
  - 152: *verbo* (print has v) [R3]
  - 152: *terrena* [R4]
  - 148: *Antichristi,* (W1: Antichnsti, -> Antichristi, (scans: antichristi | antichnsti | antichnsti | antichnsti)) [OVERRIDE-SCAR]
  - 148: *instabunt* (LEFT-nw: print = instabunt) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 147:
4. Codd.: vadantes. 12. sperificantibus. B: ad modum spere se ro-
tantibus ; additur et in A in marg. 25. tamen; A: tantum. 27. B in
marg. : Ad 5. 3i. AB in marg. : Papa non est verus vicarius Christi,
dum Christum non imitatur.
3. In Ep. II ad Timoth. cap. II Hom. V, Opp. tom. XI, 628.
19. pag. 628.

p. 148:
12. Causatum. Codd. : catum. 21. AB in marg.: Antichristi qui sunt.
7. Opp. tom. XI, p. 643. 17. Loosely quoted.

p. 149:
i3. Codd.: se hodie esse. 16. Codd.: summos vicarius. 3o. /)e
isto regnorum responso i. e. que regna eis respondere debeant.
7. Matth. XXIV, 23, 24, 25.

p. 150:
5. AB in marg.; Obedire pape.
23. Matth. XXIV, 21. 28. In Protestationibus J. W. (ed.
HCfler, Anna v. I.uxemburg in Denkschriften der Wiener Aka-
demie 1870/71, p. 147) haec protestacio deest.

p. 151:
2. B: regulare. 9. Codd. : foret sihomo. 9— 10. In codd. hic locus
corruptus est. Legitur in A: prepositure tam Gregorius beatus, Gregorius
primo libro De Cura . . . B : tam Gregorius beatus quam Gregorius primo
libro ... 10. AB in marg: Nocent in ecclesia maxime mali sacerdotes.
Sacerdotum perversitas causat mala. 17. B: ut deest. 3o. Binmarg. :
Mola asinaria quid signet.
10. De Gura Pastor. 1. c. Cf. Hussii Opp. fol. CCXXIV*.

p. 152:
4. Codd.: suaverat ut hunc. b, 6. B: constringerentur. 14. A in
marg. : Ad 6. 28. Codd.: Linconiense.
10. Hussii De Eccl. fol. CCXXIV*. 24. De Civili Domi
nio III, 485 seqq. 29. Epistola Roberti Grosseteste directa
domino Hugoni de Pateshillis ed. Luard p. 99.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 147: Videres tunc, | animam pallidam trementem, loverecundantem, velatam, agoniam habeutem, se ipsam miserabiliter contempnentem. | non dormitabit neque | dormiet, qui custodit Ysrahel,
p. 148: In novissimis diebus instdbunt tempora periculosa, | et membra sua operibus nichil monstrant, sed verbis magna false promittunt, ut patet Genes. 111,5 ubi dicit dyabolus: Nequaquam moriemini, sedi° eritis sicut dii. | Multi 3o venient in nomine meo, diceiites quia ego sum Christus \ et multos seducent,
p. 149: si quis dixerit vobis: Ecce hic est Christus aut illic, nolite credere. Surgent enim pseudochristi et pseudoprophete, et dabunt ^signa magna. Ecce, | predixi vobis. | Nudis foliis verbortim ut signis generacionis adultere innititur Antichristtis,
p. 150: est tribulacio magna, qualis nunquam fuit. | Paratus sum autem revocare istam | sentenciam, docto quod sit contraria fidei christiane.
p. 151: Qui scandalizaverit unum de pusillis istis minimis, qui in me credunt, expedit ei ut suspendatur mola asinaria circa collum eius et demergatur in pro- | fundum maris: Pastores, | perversi in moribus quod verbis predicant, moribus impugnant; unde fit, ut cum pastor per abrupta graditur, ad precipicium grex sequatur; quia } cum layci dicta prelatorum cognoverint, per opera pervertuntur. | Hinc scribitur per prophetam: Causa sunt ruine populi sacerdotes mali, de quibus dicit Dominus per prophetam: Facti sunt domui Ysrahel in offendiculum iniquitatis. Nemo quippe ampiius in ecclesia nocet, quam qui perverse agens habet nomen vel | ordinem sanctitatis, delinquentem autem hunc redarguere nullus audet; et in exemplum culpa vehementer extenditur, quando peccator pro reve- | rencia ordinis \ honoratur. Indigni namque, tanti ponderis pericula fugerent, si Veritatis sentenciam losotlicite cogitarent, qui scandalizaverit etc. Per molam quippe asinariam secularis vite circuitus 2.
p. 152: ac Idbor exprimitnr et per profundum maris extrema dampnacio designatur. Qui igitur ad sanctitatis speciem deductus vel verbo ceteros destruit vel exemplo, melius profecto fuerat, ut hunc ad mortem sub seculari habitu terrena acta constrin- | gerent, quam quod sacra officia in culpa ceteris imitabilem demonstrarent, quia nimirum si solus caderet hunc utrumque pena inferni tollerabilior cruciaret. | Dispensacione beneficiorum quisquis abutitur, qui ad alium finem quam ad fidei et caritatis augmenta- | cionem eadem utitur.
```

---

## Chunk 07-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "152.10–156.25"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "962 words; 890 unanimous or majority-real; 56 settled by vote (DEL 1, R2 26, R3a 17, R5a 12); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n213–n217 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 6: [TITLE]

## ¶1 · 152.10–154.15

> [p. 152] Iste sanctus papa novit condiciones et pericula adiacencia perverso preposito et specialiter Romano pontifici, cum peccatum commissionis vel omissionis in ipso foret scandalum toti gregi. per hoc patet responsio ad sextam racionem, in qua ex secunda piscacione Petri notatur in ipso preeminencia sepedicta. Ex quo notaret papa ex preeminencia dignitatis periculum, sciens quod vocatus ad tale officium ex corpore vel negligencia gravius est dampnandus, ymo acceptans illud officium plus propter piscacionem fastus aut questus, quam propter piscacionem animarum trahendarum ad litus soliditatis perpetue in retibus regis Christi, ut sic peccat mortaliter, ut patet XXIII cap. quinti libri, et per consequens quamdiu duraverit talis declinans intencio in occupacione vocati beneficii ecclesiastici vel dignitatis crimen amplius continue invalescit, dicente Lyncolniensi in quadam epistola: Dispensacione beneficiorum quisquis abutitur, qui ad alium finem quam ad fidei et caritatis augmentacionem eadem utitur. Quomodo igitur excusatur distribuens bona ecclesie propter carnem vel favorem [p. 153] mundi lucrificacione Christi postposita. Recole quomodo Petro dabatur titulus beatitudinis, quia caro et sanguis non revelavit sibi, et per consequens ex equo opposito acquirit titulum dampnacionis qui propter carnem vel sanguinem sic accipit vel distribuit bona Dei. Consule, inquit, conscienciam tuam, utrum plura ecclesiastica queris beneficia, ut caritas augeatur in ovibus aut tu augearis ex ovium operibus, ut tu pascas oves verbo, exemplo et oracione aut tu pascaris ex ovium lacte, vide utrum Deo dicere possis cum Augustino in De Verbis Domini Sermone XLIX: Domine, tu scis quia dixi scis quia non tacui scis quo animo dixi, scis quia flevi, cum dicerem et non audirer; ipsa puto integra racio est nostra. In ista materia convincere potest pius theologus, attendens ad conversacionem pontificum ydolorum, quod peccatum Symonis est tam publice induratum, ut nisi pastor summus trahat clerum ad vitam pauperem per subtraccionem elemosinarum secularium tam grex quam pastores vadent in precipicium. Stupor enim huius veneni mortiferi ex diutina consuetudine ad tantum invaluit, quod verba quantumlibet acuta et ex fide desiderabilia non movent clerum possessionibus soporatum. Ideo non restat nisi denudare stertentem litargicum, subtrahendo velamentum sompniferum; olim enim verificatum est illud Apostoli Hebre. V; 4: Nemo sibi sumit honorem, sed qui vocatur a Deo, ymo hodie debet esse, si non essemus peccatis cecati occultatis periculis, quod nemo sumeret sibi dignitatem huiusmodi per procuratoria media sumptuosa, subdola et laboriosa, quin pocius necessitatus apostolo, propter vite sanctitatem [p. 154] coactus susciperet onus tam arduum cum intencione faciendi opus evangeliste, subducta affeccione prosperitatis terrene et per consequens cum timore. Inde distinccione XL sub auctoritate Jeronimi dicit canon: Non est facile stare in loco Petri et Petri tenere cathedram, quia non sanctorum filii sunt qui tenent loca sanctorum sed qui exercent opera eorum. Attendamus igitur ad opera pastorum primitive ecclesie et non ad temporalia preter ordinacionem primevam ex pia ignorancia conglobata, et videbimus ex decreto (ut sepe repecii) quod nimis multi mendaciter sunt prelati. Ideo dicit Spiritus Apoc. III, 9 quomodo illi de synagoga sathane dicunt se esse ludeos et non sunt sed menciuntur.

[ENGLISH]

## ¶2 · 154.16–156.25

> [p. 154] Redeundo igitur ad exposicionem scripture videamus secundum mellifluum sub cortice verborum centum qninquaginta trium magnorum piscium. Nam, ut inquit Augustinus, De Verbis Domini Sermone XIV: Quando possumus de divinis operibus, que leguntur, intellectum alicuius mistice significacionis exculpere quasi de abstrusis favorum cellis mella producimus. Vel Christi discipulos imitantes spicas manibus confricamus, ut ad grana vitalia in eis latencia contingamus. Exponit autem Augustinus LXXXIII questionum questione LVII illum numerum seriose notans, primo quatuor gradus status ecclesie; primo enim a quaternario resultat denarius sub quo ecclesia ymo tota universitas continetur. Dicit enim Apostolus prima Cor. XI, 3 quod mulieris caput est vir sed viri caput est Christus, caput autem Christi est Deus, in quo gradu quadruplici patet quod [p. 155] Deo correspondet unitas, Christo binarius propter duplicitatem naturarum, cum humanitas in potencia fuit sibi semper adaptata, trinarius vero correspondet homini, cum sit memoria, racio et voluntas, quaternarius autem correspondet carni vel corpori quod dicitur ex quatuor principiis scilicet punctali, lineari, superficiali et profundali vel quatuor electis, colligendo autem unum duo tria quatuor constituunt decem. Sed natura humana egrediens denarium ex prevaricacione decalogi (ut dicitur cap. XXIII, V huius) indiguit reformante, ideo mediator Dei et hominum, sponsus et formator ecclesie, corpus suum quod est quaternarius duxit in dictum denarium et passione sua redemit ecclesiam. Et hec racio quare ieiunavit quadraginta diebus. Sed quia quadragenarius resultans ex ductu quaternarii in denarium habet septem partes aliquotas, ut XX, X; VIII, V, IV, II, I, que integrant quinquaginta, iam post resureccionem quadraginta diebus exspectavit ascensionem et post decem dies reformatam ecclesiam confirmavit, mittendo consolantem Spiritum dono septemplici. Sed quarto dictus cesar semper augustus augmentando semper progrediens dictam ecclesiam, consumavit, quando dictum quinquagenarium triplicavit, quod constituit centum quinquaginta et in eternitate extra illum numerum beatificavit; quod fit, cum fides, spes et caritas tocius ecclesie quoad miliciam consumatur. Pisces igitur captos a spiritu predestinante ministerio hortancium ad bona gracie Petrus trahit in terram vivencium, quando usque ad [p. 156] finem oves diligens corroborat verbo et opere finalem docens perseveranciam in virtute. Qui igitur voluerit esse Christi vel Petri vicarius; oportet ut ad instar eorum ex animo faciat similiter cum vita imitatoria et non nudum nomen vel eleccio in facie ecclesie facit papam. Predicet igitur cum apostolo, ubi nominatus est Christus, donec in vasis capacibus formetur Christus et tunc ex quaternario evangeliorum format ecclesiam. Secundo lapsis conversis suis det animam complens quadragesimam penitencie pro ovibus reformandis, tercio implorando eis Spiritum Sanctum imponat eis manus operatrices, oves morbidas confirmando, recolens illud Luce XXII cap. 32 dictum Petro: Et tu aliquando conversus confirma fratres tuos. Unde Act. VIII, 17 legitur quod Petrus confirmando imposuit eis manus. Et quarto reducat oves ad stabilimentum cubi supra petram firmam quomodolibet proiecti, stantis sine vituperio anguli. Quod si quatuor virtutibus cardinalibus tamquam quatuor equis superficialibus lateralibus substrata sit equa operacio et supposita virtutum continuacio secundum similitudinem captam ex operibus presidentis, tunc enim vendicare potest ex debito locum Petri.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 152.14: Danger of accepting the office of Pope from wrong motives.
- 153.16: Prevalence of simony.
- 154.16: The mystical meaning of the 153 fishes.
- 155.2: Various significations to be drawn from the number 153.
- 155.29: The fishes are the elect.
- 156.3: The vicar of St. Peter should preach to bring men to Christ, should help the fallen and confirm the sickly.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 152: *∅* (English side-note word) [R6]
  - 153: *opposito* [R3]
  - 153: *ut* [R3]
  - 153: *ut* [R3]
  - 153: *tacui* [R3]
  - 154: *qninquaginta* (misprint: second letter has arched top = n (turned u), zoomed leaf 215) [NW]
  - 154: *illum* [R3]
  - 154: *∅* (folio bar (199c) read as i; not text) [INS?]
  - 155: *carni* [R3]
  - 155: *punctali* [NW]
  - 155: *illum* [R3]
  - 156: *animo* [R5]
  - 156: *tu* [R3]
  - 156: *17* (print has 17; main token holds the 1 only) [R3]
  - 156: *quatuor* (20 is the line number) [R4]
  - 153: *dixi* (S-split: one word, italic; comma not carried) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 6.-7. Cf. Rom. XV, 20. (156.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 152:
4. Codd.: suaverat ut hunc. b, 6. B: constringerentur. 14. A in
marg. : Ad 6. 28. Codd.: Linconiense.
10. Hussii De Eccl. fol. CCXXIV*. 24. De Civili Domi
nio III, 485 seqq. 29. Epistola Roberti Grosseteste directa
domino Hugoni de Pateshillis ed. Luard p. 99.

p. 153:
17. AB in marg. : Prelatus verus (B: bonus) non est qui vita bona
caret. 29. AB m marg. : Dignitates ecclesiasticas quomodo usurpant.

p. 154:
25. AB in marg. : Pisces 153 quid signant.
5. Cap. II. 20. Opp. tom. V, App. p. i3i/32. 26. tom. VI,
p. 25 De centum quinquaginta tribus piscibus.

p. 155:
2. naturarum. B in marg. : vel anime. 7. punctali. Codd.: peccali.
Aug. 1. c quod progressio a puncto ad longitudinem, a longitudine
ad latitudinem ... 20. 21. B: quadraginta — ascensionem deest.
11. De Civili Dominio III, 485.

p. 156:
2. AB in marg.: Vicarius Christi verus qualis est. 26. A in rnarg.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 152: ac Idbor exprimitnr et per profundum maris extrema dampnacio designatur. Qui igitur ad sanctitatis speciem deductus vel verbo ceteros destruit vel exemplo, melius profecto fuerat, ut hunc ad mortem sub seculari habitu terrena acta constrin- | gerent, quam quod sacra officia in culpa ceteris imitabilem demonstrarent, quia nimirum si solus caderet hunc utrumque pena inferni tollerabilior cruciaret. | Dispensacione beneficiorum quisquis abutitur, qui ad alium finem quam ad fidei et caritatis augmenta- | cionem eadem utitur.
p. 153: caro et sanguis non revelavit sibi, | conscienciam tuam, utrum plura ecclesiastica queris beneficia, ut caritas augeatur in ovibus aut tu augearis ex ovium operibus, ut tu pascas oves verbo, | exempto et oracione aut tu pascaris ex ovium lacte, vide utrum Deo dicere possis cum Augustino in De Verbis Domini Sermone XLIX: Domine, tu scis quia dixiy scis quia non tacui y scis quo animo dixi, scis quia flevi, cum dicerem et non audirer; ipsa | puto integra racio est nostra. | Nemo sibi sumit honorem, sed qui vocatur
p. 154: Non est facile stare in$ loco Petri et Petri tenere cathedram, quia non sanctornm filii sunt qui tenent loca sanctorum sed qui exercent opera eorum. | de synagoga sathane dicunt se esse ludeos et non sunt sed menciuntur. | centum qninquaginta trium magnorum piscium. | Quando possumus de di- | vinis operibus, que leguntur, intellectum alicuius mistice significacionis exculpere quasi de abstrusis favorum cellis mella producimus. Vel Christi discipulos imitantes spicas manibus confricamus, ut ad grana vitalia in eis latencia contingamus. | mulieris caput est | virj sed viri caput est Christus, caput autem Christi est Deus,
p. 156: Et tu aliquando con- | versus confirma fratres tuos. | imposuit eis manus.
```

---

## Chunk 07-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "156.26–160.4"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "795 words; 758 unanimous or majority-real; 32 settled by vote (R2 17, R3a 9, R5a 5, R6a 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n217–n221 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 7: [TITLE]

## ¶1 · 156.26–160.4

> [p. 156] Per hec patet responsio ad septimum, in quo probatur preeminencia Petri per illud Act. XV, quod Petrus humiliter se pretulit ad laborem. Non fuit tunc inter apostolos de prepositura contencio, sed octuplex vera humilitas necessitavit Petrum respondere pre aliis. Et utinam papa modernus vellet exercere illam clavem sciencie fidei instar Petri, tunc enim non temptaret imponere [p. 157] fidelibus graves cerimonias eciam ultra ritus iudaycos, sed sine illis vel obediencia exacta a Petro diffiniret libertatem eorum stare in isto, quod eis et gentibus suffecit ad salutem gracia domini Ihesu Christi. Et post hec Jacobus socialiter et domestice alloquitur populum in hec verba: Viri fratres, audite me, Symon narravit quomodo Deus visitavit sumere ex gentibus populum nomini suo; propter quod ego iudico non inquietari eos, qui ex gentibus convertuntur. Ubi notum est quod Spiritus Sanctus non scribit eum beatissimum papam Petrum, sed vocat eum Symonem ex humilitate socium, et Jacobum non ex auctoritate Petri, sed Domini sic locutum, et ideo singulariter dixisse, ego iudico, quod verbum foret hodie graviter ut rusticum et inconsonum reprobatum. Nec valet allegare contra modernos episcopos Jacobi sanctitatem, quia tantum distat papa a sanctitate Petri, qui nec in hoc reprobavit Jacobum nec vendicavit quod ex sua auctoritate Jacobus sic loquatur. Sicut igitur episcopi longe sunt a sanctitate Jacobi, sic pape nimis distant a sanctitate Petri. Unde igitur pape auctoritas ad vendicandum de episcopis quod non est exemplatum in iurisdicione Petri super alios sanctos apostolos vel conversos? Petrus autem nullam dominacionem vendicavit super alios fratres suos, sed apostolo reprehendenti ipsum humiliter obedivit. Recolat igitur papa quomodo nemo debet sibi obedire, nisi de quanto ut Dei organum dixerit legem suam, nec tenetur sibi credere, nisi de quanto tenetur credere quod Deus in ipso loquitur; et hoc movebit eum ad allegandam legem Domini, in qua est omnis [p. 158] veritas et ad innitendum preeminencie sanctitatis, quia aliter est ut Antichristus maxime discredendus et a comitiva fidelium precipue fugiendus. Et tercio recolat quod Roboam ex dominacione pompatica, quam didicit ex consilio iuvenum dixit false, quod minimus digitus suus fuit potencior dorso patris, et per hoc divisum est regnum, ut patet III. Reg. XII, 10 et notat Crysostomus Omelia prima Operis Imperfecti. Et applicet ad hoc verba sua et opera, si implicat se extollere super omne quod dicitur Deus, exigens dominacionem quam Christus non potest exigere, et videbit quod racione huius precipue christianismus dividitur, nam fideles ab eo recesserant propter fetens eius dominium, et hinc impeditur utrimque conversio infidelium ad legem Domini; tam extranea, inquam, videtur conversacio eius a Christo quod longe plus variatur ab eo quam conversacio sacerdotum veteris legis a Moyse, qui sensu, verbis et doctrina remanserant, sed vita et opere recesserunt. Iste autem papa videtur extraneus a Christo, qui tam vita quam doctrina ab eo discordat, nam Matth. XXIV, 11 Christus dicit quod predicabitur hoc evangelium de pseudochristo in universo mundo in testimonium omnibus gentibus, pseudo autem nedum est interpositus, ut sit testis Christo in terris, sed persequitur illos, qui hoc evangelium attestantur; unde videtur quod non de illis Christus tantum confidit, ut de sacerdotibus legis veteris, cum Matth. XXIII, 3 suis precipit: Omnia quecumque dixerint vobis facite, secundum opera eorum nolite facere, dicunt enim et non faciunt. Dicitur autem quod nostri prelati ex maiori elongacione a Christo per superinductam dotacionem cesaream nec dicunt nec faciunt. [p. 159] Nam ubi beatus Gregorius ex animo iter arripuit ad Anglicos convertendum, papa modernus ut legem sibi limitat quod non predicet ne cadat in heresim, propter quam est solummodo deponendus, ut videtur exXL distinccione: Si papa. Sed scandalosa sunt ista, primo quia papa sciret cavere sibi de heresi antequam acciperet huiusmodi dignitatem, secundo quia papa; qui dicitur habere tantam potestatis plenitudinem, diffiniret quod non foret heresis quicquid dixerit, vel saltem protestaretur, quod non habet animum a lege Domini declinandi. Tercio heresis periculosior est in vite discordia, ymo per idem nullus prepositus predicaret, cum pro heresi et specialiter reali sit dignus deponi, et papa propter causam multiplicem cicius aufugeret illud periculum. Ideo non est nisi antichristiana et accusatoria excusacio in peccatis. Accusatoria dico, quia ut sic patenter iudicat, quod sit alienus a vicario Christi, et in aliis dicitur comuniter quod peccare non poterit. Et sic notaret Petri vicarius illud septimo replicatum, quomodo Matth. XVIII propter primatum fuit dictum singulariter Petro, quod fratrem suum corriperet, ubi sunt tria Petri vicario annotanda, primo cum debet fratrem suum corripere, debet primo omnium irreprehensibilem se servare, nam caritas debet incipere a se ipsa. Secundo notandum est quod Petri vicarius debet esse in modo corripiendi prudens, assiduus et intentus, quod non excomunicet ante finem correpcionis tercie in quo viderit fratrem suum non esse apcius corrigendum. Tercio debet notare, quod sit socius et minister ecclesie; aliter enim [p. 160] non adhiberet sibi multitudinis testimonio, et quarto diceret ecclesie ut maiori, sic enim missus est a parva apostolorum ecclesia, ut patet Act. VIII.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 156.26: Peter's behaviour at the council of Jerusalem.
- 158.19: Our prelates preach another gospel than Christ's.
- 159.1: A scandalous reason is given why the Pope should not preach.
- 159.21: How Christ's vicar should correct others.
- 159.25: 1. He should keep himself clear of fault. 2. He must correct wisely.
- 159.31: 3. He must remember that he is a servant of the Church.
- 160.1: 4. That the Church is greater than he.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 158: *10* (old-style 10) [R4]
  - 158: *universo* (print has v) [R3]
  - 159: *et* (20 is the line number) [R4]
  - 160: *adhiberet* [THIN]
  - 160: *∅* (page-opening slip repeating end of p. 159; main scan already holds it) [INS?]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 6.-7. Cf. Rom. XV, 20. (156.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 156:
2. AB in marg.: Vicarius Christi verus qualis est. 26. A in rnarg.

p. 157:
(none)

p. 158:
(none)

p. 159:
5. AB in marg. : Papa quare non predicat. 21. AB in marg.: Vi-
carius Petri debet notare dicta Petro. 24. ubi; B: ut.

p. 160:
5. A in raarg.: Ad 8. i5. sic. Codd.: si credere.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 156: Et tu aliquando con- | versus confirma fratres tuos. | imposuit eis manus.
p. 157: Viri fratres, audite me, Symon narravit quomodo Deus visitavit sumere ex gentibus populum nomini sno; propter quod ego iudico non inquietari 10 eos, qui ex gentibus convertuntur. | ego iudico,
p. 158: minimus digitus suus fuit potencior dorso patris, | super omne quod dicitur Deus, | predicabitur hoc evangelium | in universo mundo in testimonium omnibus gentibus, | Omnia quecumque dixerint vobis facite, secundum opera eorum nolite facere, dicunt enim et non faciunt.
p. 159: Si papa.
```
