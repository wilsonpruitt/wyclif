# Translation brief: potestate-pape 12-p–12-r

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-12-p.md chunks/potestate-pape/wyc-potestate-pape-12-q.md chunks/potestate-pape/wyc-potestate-pape-12-r.md` once and fix what it reports.
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

## Glossary (the 355 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
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
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
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
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
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
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| claustrales | cloisterers | Ruled 2026-09-28 (20 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| bigamia | bigamy | Canon-law sense: a second marriage (successive, or to a widow), a bar to orders; a **C** note at the first occurrence in each chunk says so. Ruled 2026-10-01 (3 sites; first *Eccl.* 11.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| digestio | digestion | The recurring figure of the four digestions (Rom. 8:30). Ruled 2026-10-02 (60.29 ff.). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| inobedienciarius | disobedient man | The negative of *obedienciarius*. Ruled 2026-10-02 (146.11). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia; prevaricacio | transgressor; transgression; transgression | Ruled 2026-09-28 (*prevaricacio* 2026-10-08, *Pot. pape* 155.10). *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
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
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| negociatores | dealers | Kept apart from *mercantes* "traders" (*Eccl.*); the servants of the talents parable (Matt. 25). Ruled 2026-10-07 (*Pot. pape* 101.7). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| irregularitas | irregularity | Canonical impediment to orders or office. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 190.30). |
| negociacio | dealing | Pairs with *negociatores* "dealers". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 194.5). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| archiprepositus | arch-superior | Formed on *prepositi* "superiors". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 300.17). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| pseudopontifices | false pontiffs | Cf. *pseudoclerici*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 335.1). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| pagina (of a law) | page | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.13). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| decimacio | tithing | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.26). |
| decimantes | tithe-payers | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.24). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |

---

## Chunk 12-p: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-p.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-p
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "373.29–377.23"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 16 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "865 words; 780 unanimous or majority-real; 60 settled by vote (R2 47, R3a 11, R6a 2); 25 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n434–n438 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 16: [TITLE]

## ¶1 · 373.29–377.23

> [p. 373] Ex istis colligitur talis racio ex lege primi mandati secunde tabule, omnis homo debet honorare sanctam matrem ecclesiam, sed honor eius precipuus foret auferre ab ea turpitudinis maculam, servando m ea statum tam dignum et nobilem et tuendo pristinam libertatem, igitur omnis homo et specialiter secularis dominus ac [p. 374] superior clericus hoc tenetur. Si igitur homo sit excommunicatus atquegravis sacrilegus qui spoliat ecclesiam bonis fortune et sacris ecclesie ornamentis, quanto magis qui extinguit in ecclesia vel aufert ab ea iocale preciosius et infinitum? quodammodo magis sacrum, cuiusmodi sunt status, privilegium et libertas, que Christus dedit ecclesie cleri sui. Et hec excommunicacio sacrilega perturbat nimirum totam ecclesiam militantem; nam tam auferentes quam consencientes sunt heretici a Deo maledicti, et eo gravius quo sic honorare matrem suam foret facilius. Nam via Domini est consolativa, plana et facilis, sed via dyaboli est litigativa, sumptuosa atque difficilis. Et istum scrupulum detegeret clerus mundi principibus, quia illorum est extirpare hos nidos hereticos. Melius enim foret et plus ad pacem nostram, quod non foret in Anglia domus vel prepositus sic possessionatus, quam quod sic duraret in ipsa hoc excomunicatum et hereticum sacrilegium antiquatum. Licet enim sit tam contrarium profectui populi et possessioni secularium dominorum induratum et tam diutine vix potest nisi per miraculum semoveri, et illi quos rex conduxit carius ad instruendum eum in hac fide proditorie plus resistunt. Et idem est iudicium de fratrum collegiis, que in magna parte fovent hoc facinus vel defendunt. Sicut enim Machomed habuit duos complices, scilicet Hebreum peritum in legeveteri, et Sergium monachum subdolum christianum, ita dicitur hodie prelatos cesareos habere ex uno latere peritos in lege cesarea et ex alio latere ypocritam exproprietarium, vocatum sacre pagine [p. 375] professorem; foret (inquam) copia cleri purgati, ut in vitis patrum priorum, clero Christi secundum eius privilegia, libertates Christi et regulas conservante. Nichil enim utile, iustum atque legitimum est alicui statui ecclesie vel legi, quem Christus instituit, contrarium, dampniferum vel nocivum, quia sic Christus foret in membris et legibus sibi ipsi contrarius. Dotacio igitur cleri non foret plus hodie quam tempore Christi contraria dominio seculari; et multo evidencius non foret contenciosa contraria sibi ipsi. Regum itaque est ad pacificacionem regni sui tales sectas et ritus novellos extinguere. Vel ahter quomodo stabit regnum? Domus enim supra domum cadet, tam in contencionibus quam pugnis spiritualibus aut corporalibus; tam inter religiosos quam laycos ac mixtim, cum forent sibi ipsis contrarii ex consensu peccati, quod omnino facit subiectum contrarium sibi ipsi. Nec dissonat sed consonat istis dictum Augustini in deDuodecim Gradibus Abusionum nono capitulo ubi dicit, quod regem non iniquum sed correctorem iniquorum esse oportet. Inde in semet ipso dignitatem sui nominis custodiret, nomen enim regis intellectualiter retinet, ut subiectis omnibus rectoris officium procuret. Ex isto plane sequitur: Si totus clerus regni habet aliquem regem suum, debet subesse eius regimini; ut patet super Jeronymum Omelia XI. Consequenter ponit iste sanctus viginti duas proprietates, que debent regibus convenire. Qualiter, inquit, alios corrigere poterit, qui proprios mores, ne iniqui sint, non corrigit, quoniam iusticia regis exaltatur solium [p. 376] et in veritate solidantur gubernacula populorum. Iusticia vero regis est neminem iniuste per potenciam opprimere, sine personarum accepcione inter virum et proximum suum iuste iudicare, advenis, pupillis et viduis defensorem esse, cohibere furta, adulteria punire, iniquos non exaltare, impudicos et histriones non nutrire, impios de terra perdere, patricidas et prave viventes vivere non sinere, ecclesias defendere, pauperes elemosinis alere, iustos super regni negocia constituere, senes sapientes et sobrios consiliarios habere, magorum, ariolorum, phitonissarum supersticionibus non contendere, iracundiam differre, patriam fortiter et iuste contra adversarios defendere, per omnia in Deo confidere, prosperitatibus animam non elevare, cuncta adversa pacienter tollerare, filios suos non sinere impie agere, certis horis oracionibus insistere, ante horas congruas non gustare cibum. Ve enim terre, cuius rex puer est et cuius principes mane comedunt. Hec regni prosperitatem in presenti faciunt et regem ad celestia regna meliora perducunt. Et post narrat iste sanctus duodecim condiciones, que ex opposito consequuntur: Qui, inquit, regnum non secundum legem hanc dispensat, multas nimirum adversitates in imperio tollerabit. Idcirco enim pax sepe ipsorum rumpitur, offendicula eciam de regno suscitantur, terrarum fructus diminuuntur, servicia populorum prepediuntur, multi et varii dolores prosperitatem regni inficiunt, carorum et liberorum mors tristiciam confert, hostium incursus et provincias undique vastant, bestie armentorum et pecorum greges dilacerant, tempestas aeris et hyemis turbata rerum fecunditatem et maris ministeria [p. 377] prohibent et aliquando fulminum ictus segetes, arborum flores et pampinos exurunt. Super omnia vero regis iniusticia non solum prosperitatem presentis imperii fuscat, sed eciam filios suos et nepotes, ne post se hereditatem teneant, obscurat. Propter piaculum enim regis Salomonis domus Israhel Dominus de manibus filiorum Israhel dispersit et propter iusticiam regis David lucernam de semine eius in Jerusalem semper reliquit. Ecce quantum iusticia regis seculo valet, in tuentibus perspicue patet. Est enim pax populorum tutamentum patrie, immunitas plebis, munimentum gentis, cura languorum, gaudium hominum, temperies aeris, serenitas maris, terre fecunditas, solacium pauperum, hereditas filiorum et sibimet ipsi spes future beatitudinis. Attamen sciat rex: sicut in throno hominum primus constitutus est, sic et in penis, si iusticiam non fecerit, primatum habiturus est, omnes namque quoscumque peccatores in presenti sub se habuerit, supra se modo plagali in pena futura habebit. Et ista bona duodecim cum pena decima tercia moverent regem et populum altrinsecus se iuvare.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 373.29: The fifth commandment teaches us to honour our mother the church and remove all. blots from her.
- 374.21: Those who should advise the king mislead him.
- 374.26: Prelates maintain false counsellors, lawyers and theologians.
- 375.11: It is the duty of kings to put down new sects and ceremonies.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 374: *iocale* (5 is the line number on that line) [NW]
  - 374: *∅* (folio bar after tam (254ᵃ in margin) read as i) [INS?]
  - 374: *dominorum* [NW]
  - 374: *induratum* (hyphenated in-|duratum; main token holds the whole word) [NW]
  - 374: *facinus* [R3]
  - 374: *defendunt* [R3]
  - 375: *Regum* [R4]
  - 375: *extinguere* [NW]
  - 375: *Inde* [R4]
  - 375: *semet* [R3]
  - 375: *ut* [R3]
  - 375: *subiectis* [NW]
  - 375: *convenire* (30 is the line number) [THIN]
  - 375: *Qualiter* [THIN]
  - 375: *iusticia* [R3]
  - 376: *iudicare* [R3]
  - 376: *regem* (20 is the line number) [R3]
  - 376: *multi* [R3]
  - 376: *hostium* [R4]
  - 377: *piaculum* [R4]
  - 377: *filiorum* [NW]
  - 377: *populorum* [THIN]
  - 377: *tutamentum* (hyphenated tutamen-|tum; main token holds the whole word) [THIN]
  - 375: *regibus* (LEFT-odd: line number 30 glued) [OVERRIDE-SCARPLATE]
  - 376: *ariolorum,* (LEFT-odd: folio bar after comma, not text) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 373:
23. faciant; ita codd. 29. Codd. in marg. : Auferre bona tempo-
ralia. argumentum bonum.

p. 374:
3. A in marg.: Omamenta sacra ecclesie. 5. B: aiifer. 28. B in
marg.: Machomet habuit duos complices.
'M>. De Sergio monacho vide Oe Ecclesia p. 290, 333, 5ii.

p. 375:
uj. Codd. iu marg. : Regi subesse debet c/erus. 20. Codd.:
abusionis. 24. Codd. in marg. : Regis condiciones 22.
20. Opp. tom. VI, App. p. 214. 3o. Nonus abusionis gradus

p. 376:
i5. Rectius: antmo non elevaru 3o. Recte: mortps . . . conferunt
ib. Codd.: cursns. 33. Godd. : fecunditate et moris.
19. Eccl. X, 16.

p. 377:
11. Codd.: Est enim deest. 12. Codd.: immunimentum.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 375: regem non iniqmim sed correctorem iniquorum esse oportet. Inde in semet ipso dignitatem sui nominis custodiret, nomen enim regis inteUectualiter retinet, ut subiectis omnibus 2 5 rectoris officinm procuret. | alios corrigere poterit, qui proprios mores, ne iniqui sint, non corrigit, quoniam iusticia regis exaltatur solium uj.
p. 376: et in veritate solidantur gubernacula populorum. Iusticia vero regis est neminem iniuste per potenciam opprimere, sine personarum accepcione inter virum et proximum suum iuste iudicare, adveuis, pupitlis et viduis defensorem esse, cohibere furta, | aduiteria punire, iniquos non exaltare, impudicos et histriones non nutrire, impios de terra perdere, patricidas et prave viventes vivere non sinere, ecciesias defendere, pauperes eiemosinis alere, iustos super regni negocia constituere, senes sapientes et | sobrios consiliarios kabere, magorum, ariotorum, \ phitonissarum supersticionibus non contendere, ira- | cundiani differre, patriam fortiter et iuste contra adversarios defendere, per omnia in Deo confidere, prosperitatibus animam non elevare, cuucta adversa | pacienter tollerare, fiiios suos non sinere impie agere, certis horis oracionibus iusistere, ante horas congruas non gustare cibum. Ve enim terre, cuius rex puer est et cuius principes mane comedunt. Hec regni prosperitatem in presenti faciunt et regem | ad celestia regna meliora perducunt. | regnum nou secundum legeui hanc dispensat, multas nimirum adversitates in imperio tollerabit. Idcirco enimib pax sepe ipsorum rnmpitur, offendicuta eciam de regno suscitantur, terrarum fructus dimiuuuntur, servicia populoruni prepediuutur, mutti et varii doiores prosperitatem regui iuficiunt, carorum et liberorum mors tristiciam confert, hostiuiu incursusSo et provincias uudique vastant, bestie armentorum et pecorum greges ditaceraut, tempestas aeris et hyemis turbata rerum fecunditatem et maris mini-
p. 377: steria prohibent et aliquando fulminum ictus segetes, arborum flores et pampinos exurunt. Super omnia vero regis iniusticia non solum prosperitatem preseutis imperii fuscat, sed eciam jilios suos et | nepoteSy ne post se hereditatem teneant, obscurat. Propter piacuhim enim regis Satomouis domus Israhel Domiuus de mauibus jiliorum Israhet dispersit et propter iusticiam regis David lucernam de semine ems iu Jerusalem sempcr reliquit. Ecce quantum iusticia regis seculo valet, in \ tuentibus perspicue patet. Est enim pax popuiorum tutamentum patrie, immunitas plebis, munimentum gentis, cura languorum, gaudium hominum. temperies aeris, serenitas maris, terre fecunditas, solacium | pauperum, hereditas filiorum et sibimet ipsi spes future bcatitudinis. Attamen sciat rex: sicut in throuo hominnm primus constitutus est, sic ct in penis, si iusticiam non feccrit, primatum habiturus est, omnes namque quoscumque peccatores in pre- | senti sub se habuerit, supra se modo plagali in pena futura habebit.
```

---

## Chunk 12-q: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-q.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-q
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "377.24–381.2"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 17 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "758 words; 710 unanimous or majority-real; 31 settled by vote (R2 18, R3a 9, R5a 4); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n438–n442 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 17: [TITLE]

## ¶1 · 377.24–378.32

> [p. 377] Et ex istis primo patet quod rex Anglie primo et principaliter daret operam ad regulandum clerum suum et specialiter episcopos ut vivant similius legi Christi; totum enim regnum est unum corpus, quod tueri atque mederi spectat ad regis officium, ut dicit iste sanctus. Ideo oportet se- cundum beatum Crysostomum Omelia XXXI Operis Imperfecti incipere a clero, cum sit pars principalis et stomachus corporis, per quem cibi digestio et sanitas sunt ad cetera membra corporis derivanda. Oportet enim regem ab illis incipere [p. 378] secundum leges ordinis naturalis. Unde quantum ad illas viginti duas condiciones regis, omnes sonant implicite quod rex debet ad regimen cleri sui magis attendere; tunc enim defendit ecclesiam, regnum, viduas et pupillos. Quod si exaltat et fovet indignos episcopos, heresiarcha et autor sui facinoris est censendus. Secundo patet quod sive Romanus pontifex sive quicumque alius ex presumcione infundabili impedierit hoc sacrum regis officium, habet j racionem heretici et pessimi Antichristi. Patet ex hoc quod talis est capitalis in heresi talis regis, nam nec Petrus nec Paulus nec eciam dominus Ihesus Christus habet potestatem ad dampnificandum, sed meliorandum ecclesiam; ideo hoc temptans contra reges, qui sunt Dei vicarii, temptat sacrilege contra sanctam ecclesiam et per consequens contra Deum; eciam sic potest sinistre intelligi maledicta glossa ordinaria super XXV questione Sunt quidam, ubi dicit quod papa habet potestatem nedum dispensandi contra Apostolum sed eciam contra Christum, et tunc indubie est Christo contrarius et pessimus Antichristus. Non enim fingi potest quomodo haberet a Deo potenciam ad tollendum vel impediendum potestatem regum, qua edificaretur ecclesia; si enim non liceret regi regere suum clerum, cum ille potest totum residuum regni inficere, ymo residuum populi superare, alias non foret rex regni integri. Et sic, ut dicit Augustinus De Antichristo XX De Civitate Dei, XXIV capitulo, ipse destrueret quartum regnum.

[ENGLISH]

## ¶2 · 379.1–379.23

> [p. 379] Tercio patet ex verbis sancti doctoris, quod pax regnorum est precipue per cleri maculas perturbata, non propter regis culpam in regendo subiectos; primo enim, ut dicit, pax populorum dissolvitur. Sed defectus illius regiminis a defectu regiminis cleri exoritur; ibidem enim primo pax cum Deo destruitur, et per consequens oportet destrui pacem cum homine, quiaYob IX 4 scribitur: Quis sibi restitit et pacem habuit? Patet igitur quod venenato clero, qui mediaret inter Deum et homines, necesse est pacem in populo perturbari; in cuius signum, ubi clerus insolencius et nequius conversatur, est maior tranquillitatis distancia. Et ut notat quidam I intuens successus seculi in diocesi Dunelmiensi, est maior turbacio et minor episcoporum et cleri religio. Ideo gaudent quidam de iusto Dei iudicio, quod ibidem ponuntur pestilencie, fames et unius gentis in alteram insultacio. Surgant itaque et pacificent, qui facto et consensu sextuplici tam cupide et irregulariter ecclesiam Christi turbaverant. Melius enim est pugnare contra hostes extrinsecos quam contra iustos domesticos.

[ENGLISH]

## ¶3 · 379.24–380.29

> [p. 379] Sed certum est quod nunquam tolletur regnorum dissensio, antequam rex clerum rexerit in statu quem Christus instituit, ut patet Daniel II Omne enim tale peccatum Deus regi imputat ex consensu. Expergiscat igitur rex prudencia et non permittat maniacos per privilegia consumere bona sua et bona pauperum regni sui, nam reducere ad statum primevum ecclesiam regi principaliter spectat ad suum officium. Non autem potest fundari in lege Domini tale privilegium et specialiter emptum cum gravi consumpcione bonorum pauperum. Ideo bona illa ne sic depopulentur, [p. 380] ad regem pertinet sequestrare. In scriptura siquidem legitur de duplici tali privilegio sacerdotis et cetera. Ieremias enim ex mandato Domini appendit ad collum cathenam ligneam, ut patet Jeremie XXVII. et post fracturam illius cathene per pseudoprophetam Ananiam accepit cathenam ferream, ut patet XXVIII capitulo. Sedechias vero pseudopropheta cesareus libro III Regum XXII et II Paralipomenon XVIII fecisse sibi ornamentum ex parte dyaboli concessum ad fingendum mendacium. Fecit, inquit, sibi Sedechias filius Canaan cornua ferrea, et ait: Hec dicit Dominus Deus: Hiis ventilabis Syriam, donec deleas eam. Et revera sicut contra Micheam erant multi pseudoprophete, false ferentes signa mendacii, sic contra paucos sacerdotes Christi sunt multi cesarei longe falsius ferentes ornamenta cesarea, quibus de victoria contra dyabolum se et suos decipiunt. Cum igitur cessarunt in nobis legalia legis veteris, debemus ad moralia virtutum figurata attendere et videre quid in Christo et suis discipulis invenitur secundum legem suam induere. Nam Psal. CXXXI, 9 per prophetam dicitur: Sacerdotes eius induantur iusticiam. De ornamentis autem corporalibus non legi Christum vel suos apostolos legem particulariter tradidisse, sed sine dissensione vel scandalo nunc unum ornamentum nunc aliud leviter acceptasse, docendo nos ut faciamus similiter.

[ENGLISH]

## ¶4 · 380.30–381.2

> [p. 380] Quantum igitur ad privilegia ornamentorum debet christianus ipsa attendere quasi neutra et nullo modo preponderare illa suis signatis. scilicet virtutibus [p. 381] datis a Domino, licet tamen eis uti pro tempore, ut patet de Apostolo Act. XXI.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 377.24: The king of England should enforce a right life in his prelates and clergy.
- 378.8: The pope or any other who hinders this action is Antichrist.
- 378.20: Accursed error in the Gloss.
- 379.1: It is the sin of the clergy that most disturbs peace.
- 379.14: Durham is an evidence oft this,
- 379.24: Dissensions will not cease till the king brings the clergy back to the state ordained by Christ.
- 380.1: The ornaments of the clergy are of small importance.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 377: *se-* (hyphenated se-|cundum; main token holds the first half) [NW]
  - 377: *cundum* (second half of se-|cundum (30 line number)) [NW]
  - 377: *Imperfecti* [R4]
  - 378: *∅* (or is the English side note (The pope or any other who hinders this)) [R6]
  - 378: *XXV questione* (one main token covers two printed words) [THIN]
  - 378: *Sunt* [THIN]
  - 378: *quidam* [THIN]
  - 379: *Quis* [R3]
  - 379: *diocesi* [NW]
  - 379: *turbacio* [R4]
  - 379: *II* (print "Daniel II." ends the line above Omne; the main scan lost II) [INS?]
  - 379: *illa* (35 is the line number on that line) [R3]
  - 380: *regem* [THIN]
  - 380: *Ieremias* [R3]
  - 380: *∅* (main scan already holds figurata whole (figu-|rata) at pos 132) [INS?]
  - 380: *illa* [R3]
  - 377: *legi Christi;* (S-split: two words) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 377:
11. Codd.: Est enim deest. 12. Codd.: immunimentum.

p. 378:
20. Causa XXV, Quaest. I, Cap. VI. Glossa ord. I, p. 1347
(ed. Ven. i5g5): Papa utrum possit contra Apostolum dispensare.
3o. Aug. Opp. tom. VII, 606.

p. 379:
i5, Cf. De Ecclesia p. 2 1 y.

p. 380:
23. Codd. in marg.: Ornamenta clericorum. 32. Codd. in mar-g.:
Dispensacio ad clericatum.

p. 381:
(none)
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 377: steria prohibent et aliquando fulminum ictus segetes, arborum flores et pampinos exurunt. Super omnia vero regis iniusticia non solum prosperitatem preseutis imperii fuscat, sed eciam jilios suos et | nepoteSy ne post se hereditatem teneant, obscurat. Propter piacuhim enim regis Satomouis domus Israhel Domiuus de mauibus jiliorum Israhet dispersit et propter iusticiam regis David lucernam de semine ems iu Jerusalem sempcr reliquit. Ecce quantum iusticia regis seculo valet, in \ tuentibus perspicue patet. Est enim pax popuiorum tutamentum patrie, immunitas plebis, munimentum gentis, cura languorum, gaudium hominum. temperies aeris, serenitas maris, terre fecunditas, solacium | pauperum, hereditas filiorum et sibimet ipsi spes future bcatitudinis. Attamen sciat rex: sicut in throuo hominnm primus constitutus est, sic ct in penis, si iusticiam non feccrit, primatum habiturus est, omnes namque quoscumque peccatores in pre- | senti sub se habuerit, supra se modo plagali in pena futura habebit.
p. 378: Suut quidam, | Regis qfjicium tmpedtens peccat.
p. 379: Quis sibi restitit et pacem habuit?
p. 380: sibi Sedechias filius Canaan cornua ferrea, et ait: Hec dicit Dominus Deus: Hiis vcntilabis Syriam, donec deleas eam. | Sacerdotes eius induaniur insticiam.
p. 381: ^Sbout^ticense
```

---

## Chunk 12-r: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-r.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-r
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "381.3–385.31"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 18 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1069 words; 1027 unanimous or majority-real; 30 settled by vote (R2 13, R3a 11, R5a 6); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n442–n446 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 18: [TITLE]

## ¶1 · 381.3–383.1

> [p. 381] Et quantum ad alia privilegia, ut licenciam varie celebrandi dispensacionem cum irregularibus, bigamis et coniugatis ad sacerdocium vel matrimonium cum infinitis huiusmodi adinventis, videtur michi quod Deus sepe dispensat cum talibus. Sed hoc ex fide capio quod non licet pape vel homini dispensare in quocumque cum aliquo, nisi Deus dispenset ante ea in eodem, sic quod vicarius Christi dispensans in talibus est nudus divine sentencie promulgator, quia cum non dependent sacramentaliter a suo officio, non restat sibi medium dispensandi nisi per modum meriti vel discrecionis promulgandi non esse periculum. Unde quia solet esse in papa maior sanctitas atque discrecio, ideo solet laycus in talibus ad papam recurrere, et modo reputatum est ut sacramentum divinissimum quod ad eum spectat singulariter ista concedere; videtur enim quod ista primo discerneret, si sint racionabilia et edificativa ecclesie, quia stante contrario non obstante sua concessione, tam ipse quam privilegiatus deceptorie est in culpa. Quod si sint racionabilia et edificatoria, quicumque promulgaverit eorum licenciam, ymo sola racione movente est licitum secundum illa procedere, cum Deus per se faciat hec licere, nec potest fundari ex humanis tradicionibus adinventis quod oportet capere generaliter sic a prelatis licenciam; vel quod licet eis sic restringendo potestatem populi vel presbiteri in neutris vel licitis ex fide scripture; servare sibi licenciam ad procedendum in talibus singulariter vel quod aliter obedienciam istam non faciens; eciam plus quam propter prevaricacionem decalogi puniatur; quia cuiuslibet christiani et specialiter prelati est ampliare atque defendere [p. 382] privilegia et libertates, quas Christus concessit ecclesie, ut patet Act. XV, sic quod peccatum antichristianum foret libertatem illam tollere vel limites in altero extremo excedere. Ideo oportet fidelem videre secundum legem scripture, exprimendo vel tacendo sic licitum, et procedere secundum doctrinam huius exemplaris generaliter et licenter. Unde pene et dispensacionum reservaciones sive licencie nimis excecant populum, sicut dicam, si Deus voluerit, in materia de sacramentis. Dicitur enim quod sacerdos benedicens in secundis nupciis nedum suspenditur, sed eo ipso irregularitatem incurrit, sed faciendo mille enormitates Deo odibiles nedum reputatur immunis, sed pro pecunia collaudatur; et fundamentum in hiis omnibus est ficta obediencia, sic quod non foret tam grave benedicendo implorare super prius nuptis divinam graciam, nisi quia leges papales precipiunt quod non fiat. Inobediencia, inquiunt, facta statutis papalibus, est gravissime punienda, et sic Christus cum lege sua postponitur. Sic enim papa posset in tollendo vel difficultando legem Christi decernere quod nullus christianus licite faciat aliquod opus neutrum, nisi quod ipse posterius approbando ratificat, et consequenter ordinare satrapas suos ad citandum quoscumque comparere responsuros in suo iudicio, cum legem consimilem ordinat Ihesus noster, ut dicunt parificatur Christo humanitus; sic enim possent ad votum vexare et mulctare populum, ut faciunt in absolucionibus, in reservacionibus et in dispensacionibus, et, ut creditur, practizarent hec amplius, nisi quia timent sibi [p. 383] quod populus percipiens suam versuciam rebellaret.

[ENGLISH]

## ¶2 · 383.3–384.14

> [p. 383] Unde logici multiplicant in ista materia argumenta, ut posito quod papa vel alius prelatus iniungat cuicumque clerico sibi subiecto virtute sacre obediencie et sub obtentu absolucionis a pena et culpa vel alterius suffragii spiritualis quod obviet primo plene pape obedienti et iniungat cuicumque layco sub forma consimili, quod obviet primo pape inobedienti, et fiat ista iniunccio sub gravissimo anathemate, et posito cum hoc quod omnis clericus vel laycus pape isti subiectus fuit primo plene sibi obediens, et quod omnis clericus obviet primo singulariter layco et econtra, et videtur sequi contradiccio. Quia da quod non, de Petro clerico et de Paulo layco sibi primo obviantibus, et quero utrum Petrus pro instanti obvie sit pape obediens; si sic, tunc in casu oportet dicere quod Paulus pro illo instanti sit pape inobediens, quia cum primo obviat Petro, qui est plene pape obediens, et iniunctum est sibi quod primo obviet pape inobedienti, sequitur quod Paulus incurrit notam inobediencie et sic Petrus, si in casu isto Petrus sit pro instanti obvie pape inobediens, tunc oportet concedere Paulum esse obedientem et consequenter Petrum, quia ante obviam fuit uterque obediens, et Petrus ex obvia non fit inobediens, sed confirmatur eius obediencia iuxta dicta. Nec valet negare casum propter tria: primo quia solum neutrum vel possibile est preceptum, secundo [p. 384] quia prelatus potest precipere simpliciter impossibile et omnino irracionale, igitur per idem vel a maiori potest istud precipere, ideo non restat responsio nisi veritas quod propter suum precipere nec magis nec minus incurrit clerus vel laycus penam vel premium, quia oportet preceptum cui obedietur esse prius racionabile apud Deum: et tunc fieret, licet nemo sub obediencia humana illud preciperet, cum aliter foret homo inobediens racioni. Et patet quod sicut in isto casu non restat expectare plenam remissionem vel anathema, sic generaliter in papali iudicio, nisi de quanto quis meruerit apud Deum; oportet enim quod obiectus sophisticus sit solutus.

[ENGLISH]

## ¶3 · 384.15–384.27

> [p. 384] Quotlibet sunt tales casus longe coloraciores quam obligaciones obediencie humanitus adinvente, ut posito quodPetrus prior habeat duas duodenas claustrales, omnes sibi obedientes, et precipiat stabiliori duodene, quod non colloquatur cum reliqua, nisi forte inobediente Petro ad obedienciam reducendum; et quod secunda duodena non colloquatur cum reliqua, nisi obediente Petro ad obedienciam confirmandum, et incipiat Paulus prioris duodene loqui cum Lino secunde duodene, utroque prestante in hoc obedienciam observare, sic quod continue ante illud colloquium uterque fuit rite Petro obediens.

[ENGLISH]

## ¶4 · 384.28–385.31

> [p. 384] Ulterius quantum ad dispensacionem affinitatis vel consangumeitatis patet quod fabricatur ut plurimum zophistarum illusio, nam si contractus sit racionalis et consentaneus legi Dei, non obstante [p. 385] prohibicione papali est validus; nec licet pape illum dissolvere, quia Matth. XIV, 6 dicitur: Quos Deus coniunxit, homo non separet. Si autem huiusmodi coniugium foret dissolutivum legi Dei.; papalis dispensacio utramque partem seduceret. Videtur itaque mihi quod coniugium parentis ad prolem proximam contrariaretur legi nature et sic Dei, quia honor et subieccio debetur parentibus. sed coniugibus amicicia socialis. Fratres autem et sorores oportuit in principio mundi contrahere, ut patet de patriarchis; quibus limitatum est de cognacione propria coniugari; tempore autem legis gracie toto genere gencium converso ad Dominum, racionaliter ordinatum est quod extra cognacionem matrimonium contrahatur, ut liga federis cognacionis habeat aliam ligam affinitatis ex desponsacione carnali, et sic forcius atque extensius sit triplex vinculum pro humani generis federe colligando, et sic dimissa liga fraternitatis spiritualis in Domino multiplicantur tradiciones hominum de gradu contractus liciti et alias revocantur; et dispensacio pro pecunia et de cognacione potencie incurrit. Certum est tamen quod non valet dispensacio papalis nisi subsit racio scripture, sed ad tantum valet diffinicio papalis, de quanto ipse racionem prudenter dilucidat et non ultra. Mille conclusiones ex istis sequuntur, quas omnes oportet concedere; unde stulticia facit quod homines plus appreciantur tradiciones hominum de coniugio cognatorum quam mandata decalogi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 381.3: Dispensations as to ordination or matrimony are lawful only when they express the will of God.
- 381.25: We may do what is reasonable and edifying without license of prelates.
- 382.14: Obedience to papal law is falsely made the test of righteousness.
- 382.30: Rapacity of the popes.
- 383.3: Logical difficulty.
- 384.5: Orders of pope or prelate cannot affect reward or punishment, which depends on God's judgment.
- 384.28: Dispensation as to prohibited degrees useless.
- 385.6: Reason for the gradual extension of such prohibitions.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 381: *bigamis* (5 is the line number) [R4]
  - 381: *vel* (15 is the line number) [R4]
  - 381: *illa* [R3]
  - 382: *parificatur* [NW]
  - 382: *mulctare* (30 is the line number) [NW]
  - 384: *illud* [R4]
  - 385: *illum* [R3]
  - 385: *coniunxit* [R4]
  - 385: *ligam* [NW]
  - 381: *coniugatis* (LEFT-nw: print = coniugatis) [OVERRIDE-SCARPLATE]
  - 384: *ad* (LEFT-odd: small stray mark before ad; kept as ad) [OVERRIDE-SCARPLATE]
  - 385: *proximam* (LEFT-odd: box in blank gap after proximam) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 381:
(none)

p. 382:
27. Gitacio auctoris alluditur.

p. 383:
2. A n marg. : Nota casum pulchrum. 3. Codd. in marg.: Casus.
4. Codd. in marg. : Spohat clerus populum suummirabiliter. 11. posito ;
B: post. 23. B in marg. : Obediencia pape in neutris.
4. Quae supra narrantur: ut posito usque pag. 384 1. 14 sit
sohitus inJohannis Hus De Ecclesia capit. XXI verbotenus babes.

p. 384:
17. Codd. in marg. : Sota casum. 28. Codd. in marg. : Dispemacio
n afjinitate et consanguineitate.
17. Quae supra explicantur videas in Opere Joh. Hus De
EccL L c. p. 246*. incipiendo a: quod Petrus prior usque ad
vocem obediens.

p. 385:
2. Cod.: Matth. XIX. 9. B: amiciciam. 11. contrakere; Adde:
matrimonia. 32. Codd. in marg. : Hereses decidere ad quem spectat.
De Poteatate Pape. 2:
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 381: ^Sbout^ticense
p. 385: Quos Deus couiunxit, honw nou separet.
```
