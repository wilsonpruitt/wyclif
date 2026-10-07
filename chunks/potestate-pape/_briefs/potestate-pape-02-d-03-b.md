# Translation brief: potestate-pape 02-d–03-b

You translate these 4 chunk(s) of Wyclif's *Tractatus de potestate pape* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-02-d.md chunks/potestate-pape/wyc-potestate-pape-02-e.md chunks/potestate-pape/wyc-potestate-pape-03-a.md chunks/potestate-pape/wyc-potestate-pape-03-b.md` once and fix what it reports.
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

## Glossary (the 262 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
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
| magnates | magnates | Ruled 2026-09-28. |
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
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
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
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
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
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| illabi | to flow into | Ruled 2026-09-28. |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
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
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
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
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
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
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 02-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-02-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-02-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "36.28–40.30"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 22.1); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "874 words; 846 unanimous or majority-real; 20 settled by vote (DEL 1, R2 9, R3a 7, R5a 3); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n97–n101 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 2, part 4: [TITLE]

## ¶1 · 36.28–37.11

> [p. 36] In secundo gradu ponuntur prophete, qui possunt intelligi secundum scienciam evangelizantes prophecias de preterito et futuro; predicatores quidem debent procul fari vulgo abscondita, et secundum scienciam aptare auditorio [p. 37] sermonem; et sic habuerunt apostoli alciorem propheciam, vivaciorem et magis fructiferam quam prophete veteris testamenti, ut patet II. Petri I; et illud credo esse supremum officium apostolorum ad extra post sapiencialem contemplacionem ad intra, ideo Christus et eius apostoli instanter exercuerunt illud officium, ut patet Marc. ult. et I. Corinth. I. Et ad istum sensum intelligunt quidam illud Matth. XXIII, 34: Ecce ego mitto ad vos prophetas, sapientes et scribas et apostolos et evangelistas.

[ENGLISH]

## ¶2 · 37.12–37.18

> [p. 37] In tercio autem gradu sunt doctores qui seorsum ad partem sive scolastice sive private docent evangelizatum vel prophetizatum publice. Et illis correspondet donum fidei, cum debent constanter docere rudes instar Christi, qui domi docebat suas predicatas parabolas, ut patet Marc. IV.

[ENGLISH]

## ¶3 · 37.19–38.20

> [p. 37] Habito itaque pastu triplici secundum primam yerarchiam recipientem a Deo sibi tres gradus exemplariter ad primam yerarchiam celestem, consequenter ponit quomodo suffragatur virtus inferior. Et omnia ista manifestant quomodo Deus qui est spiritus rutilat varie in hominibus donis suis. Sicut enim fumus indicat ignem a quo efficitur, sic quelibet creatura habens variabiliter lumen virtutis sicut radius dicit lucem. Ideo Apostolus vocat hec dona manifestacionem spiritus. Alii autem habent virtutem ut Deus faciat per eos mirabilia; per hoc enim spiritus pascitur et virtus anime roboratur, sed hoc est modicum in comparacione ad priora, sicut modicum sit quod Spiritus Sanctus apparuit apostolis in linguis igneis, nisi eos illustrasset interius; [p. 38] talem autem virtutem habuerunt patres in primitiva ecclesia plus vel minus. Sed non ascribebant sibi virtutes nisi ut organis ex humilitate magis capacibus. jn secundo vero gradu secunde yerarchie est gracia curandi corporaliter infirmos, et sic duo sensus extremi, scilicet visus et tactus, in ordine ad animam erant pasti. Unus autem sensus quoad ordinem dignitatis et propinquitatem ad spiritum est prior, sed alius sensus genere, generalitate et carnis propinquitate preponitur. Sed alie due habent virtutem opitulandi egentibus, pascendi medios cunctos sensus; et hoc fit firmitate fidei, qua auditur, adoratur et gustatur Christus in membris. Apostolus enim corporalis elemosyne pascit tres sensus medios quo auditur vox Christi Matth. XXV, 40: Quamdiu uni de minimis meis fecistis, mihi fecistis, tunc enim Christi bonus odor sumus Deo, si gustamus internam Christi dulcedinem.

[ENGLISH]

## ¶4 · 38.21–39.5

> [p. 38] Sed quoad terciam yerarchiam, qua populus a prepositis regulatur, Deus dedit quibusdam gubernaciones sicut prepositis utriusque membrorum ecclesie; ad quod requiritur discrecio donorum spiritualium et per consequens spirituum movencium ad illud officium, ponendo; servando et protegendo quemlibet in illo gradu, ad quem Deus per dona sua disposuit; hoc enim maxime pertinet ad officium prelatorum. Et quia homo est naturaliter animal communicativum in sermonibus et civile, ideo oportet secundo quod talis prepositure curatus habeat genera linguarum, [p. 39] quibus communicabit cum subditis, quia aliter foret eis barbarus. Nec hoc sufficit, cum avis posset voces formare, ideo requiritur ultimo interpretacio sermonum, nam viva vox habet ex cooperacione spiritus multum latentis energie.

[ENGLISH]

## ¶5 · 39.6–39.23

> [p. 39] Et aptantur hec novem dona spiritualia ad membra humani corporis, ita quod trinarius prime yerarchie correspondeat cerebro, in quo sunt tres ventriculi vasa lucidorum spirituum, et quinque sensuum interiorum, quibus sapiencia, id est Dei noticia, tamquam sol vel dies ad intra percipitur. Sed organa quinque spirituum situatorum in capite figurant secundum spiritum dicentem scienciam mundanorum, collum vero quod est organum vociferandi signat donum fidei ex auditu, sed in regione pectoralium cor, stomachus et pulmo ex proprietate correspondent secundo trinario. In regione vero nutritivorum splen et intestina correspondent tercie yerarchie, ymo sicut Apostolus factus est omnia omnibus, ut omnia lucrifaceret; sic non est membrum ecclesie, quin pertinenter possit cuicunque membro corporis cooperari.

[ENGLISH]

## ¶6 · 39.24–40.17

> [p. 39] Triplex tamen conveniencia et triplex differencia est notanda. Sicut enim membra constituunt unum corpus cui anima copulatur, et iterum sicut omne membrum est cuicunque necessarium, cum iuvant se reciproce in suis officiis, sic est de membris ecclesie ex vi communionis et vinculo caritatis. Tercio vero sicut membra se habent in suo regimine, sic et membra ecclesie, cum secundum Crist. Omel. XXII Operis Imperfecti homo sit liber quidam, cui tota religio christiana [p. 40] inscribitur. Sicut igitur est affinitas capitis ad pedes, sic racio et affeccio connectuntur, sicut eciam omne membrum nobile vel ignobile sine contencione servit spiritui, sic omne membrum ecclesie sine contencione minoritatis et obediencie servit Christo, et sicut membra preeminencia non de sua nobilitate superbiunt, sed faciunt suum officium secundum regimen anime ad suffragium singulorum, sic debet esse de membris ecclesie; oculi quidem et facies carent tali tegimine, ne velatum deturpent et preparent ad ruinam: sic Christus et apostoli ex fervore caritatis et alienacione a fervore cupiditatis non erant temporalibus seculariter involuti. Sed membra minus nobilia ut pudenda sunt absconsius, multiplicius et tenerius cooperta, et sic est de contemptibilibus per quos feces ecclesie expurgantur.

[ENGLISH]

## ¶7 · 40.18–40.30

> [p. 40] Alii autem dividunt membra ecclesie in spiritualia vel dextera sicut clerum et membra corporalia vel sinistra ut laycos, et prima pars que debet esse ut tectum domus ecclesie, eo quod non capit in se incisionem dominii, remanet indivisa. Sed secunda pars dividitur in prepositos et operarios ut parietes et fundamentum ecclesie, et sic habemus tres yerarchias ecclesie cum suis subdivisionibus, in partem infimam, mediam et supremam. Alii autem ex textu apostoli trahunt novem partes ecclesie ad novem partes simplices et spermaticas in humano corpore et alii aptant ipsas ad organa propter conveniencias naturales.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 36.28: 2. Prophets.
- 37.12: 3. Doctors.
- 37.19: A second hierarchy. 1. Lower members of the Church who manifest the Spirit by various virtues.
- 38.5: 2, Those who heal the sick,
- 38.12: 3. Who aid the poor.
- 38.21: Third hierarchy. Prelates who need 1. discernment of Spirits, 2. tongnes, 3. and their interpretation.
- 39.5: These gifts correspond to the members of the body.
- 39.24: Interdependence of all members;
- 40.4: all are bound, to serve Christ, each in his own way.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 36: *preterito* [R3]
  - 37: *ego* (print: Ecce ego mitto; missing from main scan) [INS?]
  - 37: *ad* (print: exemplariter ad primam; missing from main scan) [INS?]
  - 37: *∅* (25 is the line number) [R4]
  - 37: *linguis* [R3]
  - 38: *∅* (English side-note word) [R6]
  - 38: *mihi* (h ascender clear, zoomed) [R4]
  - 40: *inscribitur* [THIN]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 17. II. Cor. II, i5. (38.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 36:
14. AR in marg. : Prima ierarehia; A: primus gradus. lerarchie quo-
modo in ecclesia sunt posite. 22. Godd.: habeant. 28. A in marg.:
5. Ibidem 28. 25. In libro IV (De Civili Dominio II) hic
locus non extat.

p. 37:
10. B: prophecias. 12. A in marg. : tercius ; ib. B: doctoxes deest.
25. A: sic enim. 29. AB in marg. : lerarchia secunda.

p. 38:
18. B: tunc deest; AB in marg. : Tertia ierarchia ; A in marg. sup.:
Membra ecclesie quam habent similitadinem ad membra corporis humani.
19. Codd.: Christus.

p. 39:
23. Coequari? 3o. B in marg. : Membrum.
33. Chrysostomi Opp, (Ed. Migne) tom VI, jdi.

p. 40:
1. A in marg. : /. 4. A in marg. : 2. 6. A in marg. : 3. 3i. B
in marg. : Diversitas in membris corporis organisi et ecclesie.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 36: operacio virtutum, alii propkecia, alii discrecio Spirituum, alii genera linguarum, alii interpretacio | Deus posuit in ecclesia, prinio | apostolos, secundo prophetas, tercio doctores, demum virtutes, exinde gracias curacionum, opitulacioues, gubemaciones, genera lingttarum, interpretaciones sermonum.
p. 37: xoEcceego mitto ad vos prophetas, sapientes et scribas et apostolos et evangelistas.
p. 38: Qttatndiu uni de minimis meis fecistis, miki fecistis, tunc enim Christi bonus odor sumus JDeo,
p. 39: factus est omnia omnibus, | homo sit liber quidam, cui tota religio christiana
```

---

## Chunk 02-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-02-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-02-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "40.31–43.9"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 22.1); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "521 words; 482 unanimous or majority-real; 25 settled by vote (R2 18, R3a 3, R5a 4); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n101–n104 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 2, part 5: [TITLE]

## ¶1 · 40.31–42.5

> [p. 40] Sed quomodocunque loquimur, est notanda diversitas inter membra istorum corporum. Prima, cum partes ecclesie continuantur per graciam, non respiciunt posicionem vel ubicacionem situs [p. 41] corporei ut membra hominis; secunda cum membra sint mistica, non repugnat sed convenit quod unum membrum habeat diversorum generum officia; homo enim est quasi universitas, ideo sibi convenit instanter agere quantum potest. Tercia diversitas est, licet membra ecclesie habeant virtutes influxas a Christo, sicut membra corporis habent virtutes influxas ab anima, a quibus ponuntur in esse membrorum, tamen influencia prior et membrorum operacio est voluntaria et graciosa et meritoria, et secundo influencia anime et membrorum operacio sunt naturales et permanencius perdurantes; licet enim membrum ecclesie posset facillime mutari ex sua vertibilitate ab uno membro in aliud vel ex variacione operis desinere esse membrum vivum, hoc tamen non potest contingere ex differencia spiritus influentis, unde quia tota materia ista est insensibilis, est plena illusione zophistica. Sed quantum ad ultimum scilicet perdicionem potencie, videtur, cum potestas illa sit licencia operandi, quod generaliter perditur per mortale, cum sit illicitum tali aliquid operari. Et ista videtur sentencia beati Gregorii posita in decretis XI, q. III: Ipse, inquit, ligandi atque solvendi potestate se privat, qui hanc pro suis voluntatibus et non subditorum moribus exercet. Et sequitur: Indicare digne de subditis nequeunt, qui in subditorum causis sua vel odio vel gracia sequuntur. Tunc, inquit vera est absolucio presidentis, cum interni sequitur arbitrium iudicis, quod bene quadriduani mortui resuscitacio ilia signat, quia prius Dominus mortuum suscitavit [p. 42] et vivificavit dicens: Lazare, veni foras et postmodum is, qui vivus fuerat, egressus a discipulis est solutus. Et patet cum cursu ecclesie quomodo maior pars ecclesie tam in foro penitencie quam iuris caret potestate iudicii.

[ENGLISH]

## ¶2 · 42.6–42.16

> [p. 42] Confirmatur secundo ex hoc quod potestas talis cum dativo a Deo ad tam excellens ministerium, est quoddam singulare privilegium. Sed secundum beatum Gregorium ibidem: privilegium omnino meretur amittere qui permissa sibi abutitur potestate. Cum igitur quilibet potentatus abutitur sua potestate, dum illam exercuerit in mortali, videtur quod meretur potestatem talem amittere, et cum Deus qui dat insensibiliter potestatem non defert meritum sive dignum, videtur quod eo ipso Deus aufert ab homine potestatem.

[ENGLISH]

## ¶3 · 42.17–42.33

> [p. 42] Item, Deus potest auferre licenciam vel potestatem ab homine pro delicto, sed quando auferret graciosus dominus si non quando se ipsum dampnificat per abusum ad quod non habet licenciam? ideo cum nemo potest abuti tali licencia nec virtute, videtur quod Gregorius equivocat vocando potestatem, posse vel potenciam aut liberum arbitrium, et alias vocat potestatem amissam ipsam licenciam. Et idem videtur ex decreto beati Augustini posito XXIV, q. prima, ubi dicit omnes hereticos, id est, peccato mortali ab ecclesia divisos, non habere aliquid potestatis. Sed notandum est; ut alias declaravi, quod opus heretici vertitur dignis ad commodum, sicut Deus per se supplet, quando prepositi excommunicati a Deo subditis suis deficiunt.

[ENGLISH]

## ¶4 · 43.1–43.9

> [p. 43] Et ex istis videtur quod potestas predestinacionis (de qua Joh. primo et sepe alibi) est maxima potestas, quam Deus communicat viatori. Potestas autem, quam Deus dat beato ad plene fruendum dominio, et in ipso qualis creatura est potestas hominis consumata, de qua quidam intelligunt illud Matth. ult: Data est mihi omnis potestas in celo et in terra, beati enim habent fructum cuiuslibet potestatis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 40.31: Difference between membership of the body and of the Church.
- 41.20: Members who tall into mortal sin lose their power.
- 42.26: Although the wicked lose power, the righteous may profit by their ministrations,
- 43.1: The greatest power God grants is that of predestination.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 40: *∅* (English side-note word) [R4]
  - 41: *illa* [R3]
  - 41: *subditis* [THIN]
  - 41: *nequeunt* [THIN]
  - 41: *qui* [THIN]
  - 41: *in* [THIN]
  - 41: *subditorum* [THIN]
  - 41: *causis* [THIN]
  - 41: *sua* [THIN]
  - 42: *Lazare* [R5]
  - 42: *∅* (English side-note word) [R6]
  - 42: *prepositi* [R3]
  - 43: *Joh* (abbreviation point dropped per no-trailing-punctuation rule) [R3]
  - 41: *sequuntur* (LEFT-odd: italic; stop after not carried) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 40:
1. A in marg. : /. 4. A in marg. : 2. 6. A in marg. : 3. 3i. B
in marg. : Diversitas in membris corporis organisi et ecclesie.

p. 41:
20. B in marg. : Perdere potestatem; A in marg. : Potestatem homo
perdit per peccatum mortale.
25. Decreti secunda pars, Causa XI, q. III, cap. LX — LXIL

p. 42:
(none)

p. 43:
1. B in marg.: Potestas (predestin)acionis maxima ; A in marg. : Po-
testas predestinacionis est maxima potestas viatoris. 5. Codd.: domino.
6. B in marg.: Consummata potestas. 10. A: Cm. tercium. 21. A in
marg. : Petrus si ut caput ecclesie primatum tenuit.
7. Matth. XXVIII, 18.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 41: ligandi atqtie solvendi potestate se privat, qni hanc pro snis volnntatibns et non snbditornm moribns exercet. | Indicare digne de snbditis nequetmt, | iu snbditornm cansis sna vel odio vel gracia ■ o seqnnntnr. Tunc, | vera est absolucio presidentis, cum interni sequitur arbitrium iudicis, quod bene quadriduani mortui resuscitacio ilia signat, quia prius Dominus mortuum suscitavit
p. 42: et vivificavit dicens: Lazare, veni foras et postmodum is, qui vivus fuerat, egressus a discipidis est solutus. | privilegium omnino meretur amittere qui permissa sibi abutitur po- | omnes hereticos, | id est, peccato mortali ab ecclesia divisos, non habere aliquid potestatis.
p. 43: Data est mihi oninis potestas in celo et in terra, | ut qni maior est eornm fiat nt minor;
```

---

## Chunk 03-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-03-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-03-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "43.11–47.26"
divisions: "cap. 3 (heading 'CAPITULUM TERCIUM.' at 43.10); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "958 words; 885 unanimous or majority-real; 53 settled by vote (R2 19, R3a 5, R5a 28, R6a 1); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n104–n108 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 3, part 1: [TITLE]

## ¶1 · 43.11–45.12

> [p. 43] Habito generali sermone de potestate membrorum ecclesie cum suis subditis et eorum singulis superest videre de potestate summi sacerdotis, quem alii vocant papam et alii Romanum pontificem. Et quia tota moderna ecclesia exemplata est ab ecclesia peregrinante pro tempore Christi, ideo restat videre in isto explicari, quis apostolorum post ascensionem Christi primatum tenuit; et arguit dominus Ardmacanus VII libro De Questionibus Armenorum viginti racionibus quod Petrus inter omnes habuit preeminenciam capitalem, primo per illud Math. XX, quando facta est contencio inter discipulos Jesu, quis illorum videtur esse maior, in determinando questionem docet ut qui maior est eorum fiat ut minor; quod dictum implicat aliquem esse inter eos maiorem ceteris. Unde postquam ostenderit quod maioritas, quam ipse definitive diligit [p. 44] attenter penes maioritatem mitis et humilis ministerii vertitur verbum ad Symonem: Ecce, inquit, sathanas expetivit vos, ut cribraret sicut triticum, ego autem rogavi pro te, ut non deficiat fides tua, et tu aliquando conversus confirma fratres tuos. Ecce post generalem I solucionem facta est particularis applicacio preminencie ad Petrum, cum non aliter pertinenter magister optimus decideret questionem sedando brigam et instruendo eos in regulis religionis sue, quas in posterum observaverunt; unde relinquens exemplum suis; ne superbiant de prepositura ecclesiastica, sed pocius timeant propter annexum periculum, sub quodam velamine includente periculum adiutorium atque officium insinuat Petro primatum. Per cribrum intelligunt doctores ad sensum misticum naturam lapsam corpoream. Ipsa enim est quasi caminus temptacionis, in qua spiritus humanus colliditur, sicut in cribro triticum ventilatur. Curvitas ligni signat declinacionem hominis a rectitudine originalis iusticie per peccatum. Tegule dicto ligno infixe que se intersecant ex adverso sunt versucie diaboli et fraus mundi, quibus sensualitati infixis spiritus temptacionibus periculosis concutitur, et eo timorosius quo gradus prepositure est alcior; foramina vero spatulis intercepta sunt genera virtutum, quibus temptatus cognoscit humiliter vitam suam esse ventum aut vacuum. Per istas siquidem rimas patet temptati subterfugium, ut ex gracia et gravedine humilitatis evadat collisionis hostilis periculum, si fuerit horreandus in terra vivencium, quia aliter ventus superbie exsufflat [p. 45] ipsum ab area virtutum comburendum ut paleam vel bestiis civitatis dyaboli devorandum. Expetivit igitur sathanas ut post percussionem pastoris posset eos temptando concutere vento superbie, perplexitate diffidencie et aliis collusionibus spiritualibus, non ad expurgacionem predestinatorum, licet hoc sciverit, sed ad dampnificandum prescitos relictos ut palea, quod obtinuit in Juda. Et sic licencia concessa a Deo sathane ad temptandum apostolos preter eius propositum sicut in beato Job cessit eis ad commodum, cum erant cribrati sicut triticum.

[ENGLISH]

## ¶2 · 45.13–47.8

> [p. 45] Sed secundo, ut cognoscat ecclesiam non a se hoc habere, sed a fide et gracia domini Jesu Christi, ut vel sic postposita superbia celebret eius laudem, statim subiungit: Ego autem rogavi pro te, ut non deficiat fides tua in quo videtur innuere primatum Petri in hoc quod nomine suo exprimit totam ecclesiam militantem; semper enim manet fides ecclesie in una persona vel in alia, sicut in sancto sabbato, quando defecit in Petro; servata fuerat in Maria. Ista igitur negacio accomoda, verificans dictum Christi, docet quod nomine suo tamquam capitanei expressit ecclesiam. Sed tercio (ut exposui in capitulo V huius) limitat prelacie officium, cum subinfert: Et tu aliquando conversus confirma fratres tuos quod officium post Joh. XXI, 17 exponit expressius, cum sibi singulariter iniungit tribus vicibus pascere oves suas; unde Joh. XX, 1 9 dicitur quod apostoli audito a Magdalena sublatum esse corpus Domini Petrus et Johannes, in quibus fides remissius est extincta, cucurrerunt, ut haberent experienciam [p. 46] rei gestae. Et quamvis Johannes, virgo et sterilis, synagogam singnificans, precucurrit citius I Petro, tamen Petrus ex fervore amoris m effectu posito introivit et ab experiencia cum inspiracione interna edoctus resurreccionem credidit, et sic Johannem qui fuit post eum precipuus confirmavit. Unde sequitur in textu: Tunc inquit, introivit et ille discipulus, qui venerat primus ad monumentum, et vidit et credidit; nondum enim sciebant scripturam, quia oportuit eum a mortuis resurgere. Quamvis enim Johannes quoad devocionem amoris contemplantis fervencius Petro Christum dilexerit, tamen Petrus quantum ad amorem practicum plus ceteris apostolis diligebat. In cuius signum Johannes, tamquam speculativus ad percipiendum archana Dei magis dispositus; de Jesu stante in littore ad signandum cursum mundane viacionis sibi transactum, prius percepit quam Petrus, quia dominus est, ut dicitur Joh. ultimo, verumtamen Petrus, audito quia dominus est, misit se fervencius in mare. Et propter magnitudinem istius amoris practici et experienciam fragilitatis humane, cum ipsemet ter negavit Christum Math. XXVI, fuit racioni consonum, ut ipse preficeretur caput ecclesie, Johannes autem virgo et contemplativus a mundo abstractus habuit custodiam matris et virginis que fuit locale sponsi preciosissimum. Et sic habuit signum preeminencie amoris in hoc, quod de tam prope quietus factus est celestis coniugii paranymphus, et preter hec habuit cum ceteris apostolis generalem custodiam matris ecclesie; sed quadam prerogativa Petrus. Et sic secundum unam racionem amandi videtur catholicum quod Johannes plus Petro dilexit celeste coniugium [p. 47] et sine huiusmodi repugnancia quoad aliam racionem amandi Petrus plus hiis diligens plus dilexit Christum atque ecclesiam quam Johannes; et proporcionaliter erant a sponso ecclesie readamati; racione cuius Johannes tam crebro dicit, non quod Jesus eum maxime diligebat; ut patet Joh. XIX, XX et XXI, sed quod eum quodam amoris privilegio precipue diligebat.

[ENGLISH]

## ¶3 · 47.9–47.26

> [p. 47] Ex ista ranga potest pius theologus tamquam fundamento colligere quod Petrus habuit quendam primatum apostolice dignitatis; secundo confirmatur idem ex serie verborum sacre scripture et prerogativa pre ceteris data Petro. Nam Math. X, 2 sic dicitur: Duodecim apostolorum nomina sunt hec Primus Symon, qui dicitur Petrus, et Andreas frater eius. Cum autem nec ordo verborum nec sillaba in scriptura ponatur, quin sit omissa sentencia, quid pertinencius daretur intelligi; quod Petrus dicitur primus apostolorum, nisi quod ipse singulariter tenet primatum apostolice dignitatis; cum vocacione Andreas Petrum precesserit, ut patet Joh. I. Non igitur ex indifferencia preposuit Christus Petrum in vocacione; tercio; ut patet Math. X et Luce VI, ymo communiter connumerando apostolos Petrus preponitur ab eo, qui dixit et facta sunt.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 43.11: The power of the Pope.
- 43.16: We must first decide which of the apostles held the primacy,
- 43.22: Fitzralph's proofs of Peters preeminence.
- 44.6: Explanation of the 'sifting'.
- 45.13: Christ suggests the primacy of Peter in addressing him as if he were the Church.
- 46.2: Behaviour of Peter and John at the Sepulchre,
- 46.12: John more fervent in contemplative, Peter in practical love.
- 47.9: Peters primacy confirmed from other parts of Scripture.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 43: *CAPITULUM TERCIUM.* [HEAD]
  - 43: *facta* [R3]
  - 43: *ut* [R4]
  - 43: *ut* [R3]
  - 44: *sicut* [R3]
  - 44: *tua* [R3]
  - 44: *tu* [R3]
  - 44: *confirma* (5 is the line number) [THIN]
  - 44: *∅* (English side-note word) [THIN]
  - 44: *subterfugium* [NW]
  - 45: *1* (old-style arabic 1, x-height, zoomed) [R3]
  - 46: *effectu* [R3]
  - 46: *dilexerit* [R4]
  - 46: *archana* [NW]
  - 46: *∅* (the inserted i is the folio bar before quadam) [INS?]
  - 46: *coniugium* (35 is the line number) [THIN]
  - 47: *hec Primus* (one token covers two printed words) [R5]
  - 46: *Christum* (W1: Chnstum -> Christum (scans: christum | chnstum | chnstum | chnstum)) [OVERRIDE-SCAR]
  - 45: *suas* (LEFT-odd: italic; 30 is line number; semicolon not carried) [OVERRIDE-SCARPLATE]
  - 46: *singnificans* (LEFT-odd: ink shows -gn- spelling as in main scans; kept as printed; comma not carried) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Peter in (45.14).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 43:
1. B in marg.: Potestas (predestin)acionis maxima ; A in marg. : Po-
testas predestinacionis est maxima potestas viatoris. 5. Codd.: domino.
6. B in marg.: Consummata potestas. 10. A: Cm. tercium. 21. A in
marg. : Petrus si ut caput ecclesie primatum tenuit.
7. Matth. XXVIII, 18.

p. 44:
16. B in marg.: Per cribrum intelligitur ; A: Cribrum tnistice quid
signet? 3o. B: ruinas.

p. 45:
5. B: perplexitate. 20, 21. A: vel alia. 21. B: dejicit.
22, 23. Codd.: negacio accomoda aconda (sic). 26. B: tu deest.

p. 46:
17. Joh. XXI, 4.

p. 47:
9. ran^a; cf. De Veritate S. Scripturae p. 124 1. 4. It seems to be
taken from English range or rank (Matthew). 24. Cod.: tevcia 27. A
in marg. : Petra C/irislus, non retrus.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 43: Data est mihi oninis potestas in celo et in terra, | ut qni maior est eornm fiat nt minor;
p. 44: sathanas expetivit vos, ut cribraret sicut triticum, ego autem rogavi pro te, ut non deficiat fides tua, et tu aliquando conversus confirma | fratres tuos.
p. 45: Ego autem rogavi | pro te, ut non deficiat fides tua } | Et tu aliquando conversus confirma fratres tuos } | pascere oves 'iosuas; | sublatum esse corpus Domini | Joh. XX.
p. 46: precucurrit citius | introivit et ille discipulus, qui venerat primtis ad monumentum, et vidit et credidit; nonduni enim sciebant scripturam, quia oportuit eum a mortuis | Jesu stante in littore
p. 47: Duodecim apostolorum | nomina sunt hec:Primus Symon, qui dicitur Petrus, et Andreas frater eius. | dixit et facta sunt. | Et ego dico tibi quia tu es Petrus, et super hanc petram edificabo ecclesiam meam et porte inferi non prevalebunt adversus eam, et tibi dabo claves regni celorum, et quod- | cunque ligaveris super terram \ erit ligatum et in
```

---

## Chunk 03-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-03-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-03-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "47.27–51.10"
divisions: "cap. 3 (heading 'CAPITULUM TERCIUM.' at 43.10); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "824 words; 757 unanimous or majority-real; 59 settled by vote (DEL 1, R2 18, R3a 16, R5a 24); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n108–n112 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 3, part 2: [TITLE]

## ¶1 · 47.27–49.31

> [p. 47] Quantum ad privilegia dignitatis ecclesie Math. XVI; 18— 19 post confessionem Petri de filiacione Christi naturali, respondit Christus, quasi pro arris mercedis fidei: Et ego dico tibi quia tu es Petrus, et super hanc petram edificabo ecclesiam meam et porte inferi non prevalebunt adversus eam, et tibi dabo claves regni celorum, et quodcunque ligaveris super terram erit ligatum et in [p. 48] celis, et quodcunque solveris super terram, erit solutum et in celis. Sed post Math. XVIII et Joh. XX dat apostolis communiter potestatem. Sed nusquam legitur in scriptura quod alteri quam Petro dedit dominus claves celi; per hoc igitur quod Petrus ex approbacione Christi respondit pro omnibus in precipua materia fidei, que est fundamentum spirituali preposito, et per hoc quod Christus mutato nomine a Symone in Petrum quod nomen contraxit a se ipso, qui est Petra et fundamentum ecclesie, ut patet I. Corinth. X et I. Corinth. Ill, videtur concedere Petro quandam prerogativam super ceteros apostolos ad regendam suam ecclesiam, ac si diceret secundum exposicionem Augustini De Verbis Domini sermone XIII: Ego sum petra, (quia Christus) a qua tu es Petrus, id est christianus in fide firmus, inmediatus mei vicarius, super quam petram, quam confessus es, per te ut proximum eius capitaneum fundabo ecclesiam meam. Ideo, dicit Augustinus, a petra petrus non a petro petra, sicut a Christo Christianus, non a Christiano Christus. Ideo super me edificabo ecclesiam meam, non super te, nam volentes edificare super homines dicebant: Ego quidem sum Pauli, ego quidem Apollo, ego vero Cephe, sed apostolus dicit se esse lapidis, qui est Christus. Cum igitur Christus nominat Petrum primo nomine suo; videtur concedere primitatem, ideo dicit Augustinus quod apostolatus tenuit principatum in signum cuius possessionis et preeminencie subditChristus: Dabo tibi post mortem meam claves ecclesie, quam fortificabo [p. 49] super ecclesiam malignancium, dando tibi potestatem ligandi atque solvendi; ut non superflue occupes claves ecclesie, quas dedi tibi racione confessionis meritorie humanitatis et deitatis qua a Spiritu Sancto edoctus dixisti, tu es Christus et per consequens verus homo filius Dei vivi; quod non fuisset pertinenter additum, nisi intelligeretur de filio naturali. Et ista confessio est maxime pertinens christiano preposito, ut patet Joh. IV; eo quod maxime obviat Antichristo, cumipse negabit divinitatem et infatuabit; quantum in ipso erit, Christi pauperiem et voluntariam passionem. Ubi enim nos christiani docemur a Christo et ecclesia expetere constanciam, prospera mundi despicere et nulla eius adversa formidare, Antichristus econtra cum multis suis docet homines ad mundi prospera aspirare et penalitates contempnere, unde Petrus, quia dixit Christo; absit hoc a te Domine ut vadas Jerusalem crucifigi, vocatus est ab eo Sathanas paulo post hoc privilegium singulare, ut patet Math. XVI; 23, ad denotandum quod ipse est potissime Christo adversans tamquam alter Antichristus, qui in paupertate et penalitate abnuit sequi Christum. Unde isto scuto fidei armatus est Petrus postmodum, cum pro Christo reliquit uxorem et omnia, sequendo ipsum Math. XIX, 27, pro Christo promisit se mori percuciendo servum pontificis Joh. XVIII, 10; pro Christo exposuit se in aquam Math. XIV et Joh. ultimo et demum in capite mundi Roma pro Christo pertulit mortem acerbam.

[ENGLISH]

## ¶2 · 49.32–50.27

> [p. 49] Quid igitur datur intelligi, quod solus Petrus videbatur a domino Math. XIV venire ad ipsum supra mare, nisi quod presens seculum per mare [p. 50] signatum ipse a Deo adiutus, singulariter presidens navicule significanti ecclesiam Christi, subiceret servituti; etistum sensumponit Augustinus Sermone IV. Quid autem per secundam in mari missionem, de qua Johannis ultimo, aliis discipulis navigio ad Christum venientibus, j ipse solus tunica succinctus audacter misit se in mare, daretur nobis intelligi vere quod omnes alii Christi discipuli ducatu Petri tunica virtutum et zona potencie ligandi ornati fuerant in via tendendi ad terminum regulandi? Hoc eciam figuratur per hoc, quod soli tempore passionis Salvator dixerit Marc. XIV, 37: Simon dormis? Non potuisti una hora vigilare mecum? per hoc innuens quod ipse solus pre ceteris et pro ceteris haberet capitaliter in cura pastoralis officii vigilare. Et hoc idem figuratur per hoc, quod ipse solus in secunda piscacione traxit ad litus rete plenum centum quinquaginta tribus magnis piscibus, ut dicitur Joh. ult; per hoc enim figuratur quod ipse solus inter apostolos trahit capitaliter sponsam Christi ad terram vivencium in retibus legisDei. Magnum itaque privilegium vicarii, qui potest trahere animas ad beatitudinem, cum ista secunda piscacio significat capcionem hominum ad ecclesiam triumphantem, sicut prima piscacio signat capcionem hominum ad ecclesiam militantem.

[ENGLISH]

## ¶3 · 50.28–51.10

> [p. 50] Idem eciam figuratur per hoc quod Christus doctrinam correpcionis, quam voluit tradi cunctis fidelibus, per Petrum voluit in alios derivari. Nam Math. XVIII, 15 legitur: Aspiciens Ihesus in discipulos suos dixit Simoni Petro: Si peccaverit in te frater tuus, vade et corripe eum inter te et [p. 51] ipsum solum, ut exposui VIII capitulo IV huius et XXIV cap. V libri. Idem figuratum est Joh. ultimo. ubi in conventu duodecim discipulorum universitatem fidelium Christi signancium post triplicem examinacionem amoris ipse singulariter recepit a pastore summo curam et pastum simpliciter I tam ovium quam agnorum; ut sicut ter Christum negaverat; sic ostendat eius amorem in pascendo magnates, vulgus et clericos verbo; opere et exemplo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 48.4: Only to Peter Were given the keys of heaven.
- 49.8: Peter's confession a check to Antichrist.
- 49.32: Peter's Walking on the water.
- 50.4: His plunging into the sea.
- 50.12: Christ's address to him in Gethsemane.
- 50.17: His dragging the net to land.
- 51.6: Christ's charge to him to feed the sheep.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 48: *et* [R3]
  - 48: *dominus* [R3]
  - 49: *absit* [R4]
  - 49: *10* (old-style arabic 10) [R3]
  - 50: *Simon* [R4]
  - 50: *Non* [R3]
  - 50: *potuisti* [R4]
  - 47: *18—* (LEFT-odd: box on the dash of 18—19; print has 19 after it) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 47:
9. ran^a; cf. De Veritate S. Scripturae p. 124 1. 4. It seems to be
taken from English range or rank (Matthew). 24. Cod.: tevcia 27. A
in marg. : Petra C/irislus, non retrus.

p. 48:
19. per te ; B: peter. 28. B: Petrum deest.
i5. St. Augustini episcopi Sermo LXXVI de verbio evangelii
Matth. XIV, Opp. tom. V, 41 5. Cf. Hussii Opp. 2ioa. 3o. St.
Augustini Sermo LXXVI ubi p. 416.

p. 49:
14. Codd.: ecclesiam. 17. B: aspirare deest.
19. Matth. XVI, 23.
De Potestate Pape. 4

p. 50:
II, Codd.: ad dominum. i3. Codd.: MarciXXVl.
3. St. Augustini ubi supra p. 320.

p. 51:
2. B: 34; A in marg. alia manu: Nota quod sensus figuraliler equi-
valet literali. i3. Codd.: tamen sic. 19. Codd.: dicetur.
U De Civili Dominio II, 62 et III, 5 19.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 47: Duodecim apostolorum | nomina sunt hec:Primus Symon, qui dicitur Petrus, et Andreas frater eius. | dixit et facta sunt. | Et ego dico tibi quia tu es Petrus, et super hanc petram edificabo ecclesiam meam et porte inferi non prevalebunt adversus eam, et tibi dabo claves regni celorum, et quod- | cunque ligaveris super terram \ erit ligatum et in
p. 48: celis, et quodcunque solveris super terram, erit solutum et in celis. | a petra petrus non a petro petra, sicut a Christo Christianus, non a Christiano Christus. Ideo super me edificabo ecclesiam meam, non super te, nam volentes edificare super homines dicebant: Ego quidem sum Pauli, ego quidem | Apolio, ego vero Cephe, sed apostolus dicit se esse lapidis, qui est Christus. | apostolatus tenuit principatum | Dabo tibi | ciaves ecclesie,
p. 49: dbsit hoc a te Domhie | uxorem et omnia, | percuciendo servum pontificis
p. 50: aliis discipulis | navigio ad Christum venientibus, | Simon dormis? Non potuisti una hora vigilare mecum? | plenum centum quinquaginta tribus magnis piscibus, | Si peccaverit in te frater tuus, vade et corripe eum inter te et
p. 51: ipsum solum,
```
