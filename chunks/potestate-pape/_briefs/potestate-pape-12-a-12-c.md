# Translation brief: potestate-pape 12-a–12-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-12-a.md chunks/potestate-pape/wyc-potestate-pape-12-b.md chunks/potestate-pape/wyc-potestate-pape-12-c.md` once and fix what it reports.
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

## Glossary (the 300 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| calumpnia (ponere / capere) | challenge (to lay a challenge against / to be open to challenge) | The disputant's formal objection to a premiss. Ruled 2026-10-02 (*Eccl.* 16, 363.18, 363.24, 367.11). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
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
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
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
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| influencia (celestis) | (celestial) influence | Astrological sense. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 172.1). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio; pompa | boast; boasting; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| locus a simili | the topic from likeness | Dialectical topic. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 240.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |

---

## Chunk 12-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "316.25–320.21"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 1 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "824 words; 788 unanimous or majority-real; 26 settled by vote (DEL 1, R2 13, R3a 6, R5a 5, R6a 1); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n377–n381 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 1: [TITLE]

## ¶1 · 316.25–317.3

> [p. 316] Adhuc restat dubitandum quomodo posset de-? esse papa cesareus, cum necesse sit esse unum caput ad causas ecclesiasticas terminandum, ad beneficia ecclesiastica parciendum et ad privilegia concedendum; unde ad tantum cecati sunt seculares valde subtiles in ista argucia, quod [p. 317] putant cum clero infatuante dominos, quod non staret sine ordine huius cleri cesarei dominium seculare.

[ENGLISH]

## ¶2 · 317.4–317.16

> [p. 317] Sed ambos istos simul convinco tripliciter, primo in hoc quod perfecte stetit ecclesia cum seculari dominio trecentis annis post ascensionem Christi et amplius, quando non fuit talis ceca et venenosa dotacio. Si igitur tunc crevit utrumque istorum membrorum ecclesie, et post decrevit, eciam quousque utrumque istorum capitum reliquum destruxerit ad non gradum, quomodo non est evidens, quod utramque istarum parcium foret viare plus prospere quoad Deum et homines reducta ad ordinem ecclesie quem Christus instituit, quam sit irreligiose commixta in ritibus ex auctoritate cesarea.

[ENGLISH]

## ¶3 · 317.17–317.22

> [p. 317] Quod potest confirmari ex lege Dei, ex lege ecclesie et lege cesarea. Ex lege Dei, quia tunc viveret clerus uterque lege Dei placencius, sibi utilius, Christo ac apostolis suis conformius. Quomodo igitur non haberet Deum exinde magis propicium?

[ENGLISH]

## ¶4 · 317.23–317.34

> [p. 317] Ex lege ecclesie patet idem cum distinccione XCV: Olim ex decreto Jeronymi docentur quomodo ecclesia regulabatur ante dotacionem, eciam in tempore apostolorum communi consilio sacerdotum, et postmodum instigacione dyaboli facta est divisio constituendo capitaneos secundum dignitatem mundanam, captam fallaciter ex preeminencia apostolorum, a quibus instrumentaliter sunt conversi, ut tangit Apostolus prima Cor. I et III. Quare igitur non foret perfeccius stare in statu primevo, quem Christus instituit quam in statu extraneo qui instinctu dyaboli inolevit?

[ENGLISH]

## ¶5 · 318.1–318.26

> [p. 318] Et quantum ad legem civilem, patet quod imperator sicut et quilibet civilis dominus tenetur defendere suum dominium seculare vel mutare in melius, sed in solucione ordinis cleri Christo deterioratur utraque pars saltem in spiritualibus quoad Deum, igitur repugnat principiis legis humane talis prepositi spiritualis mundana dotacio. Item, prius tempore et natura est secularis dominacio quam talis cleri dotacio, ut docet Crysostomus In Imperfecto Omelia XXXIV, sed omne sic prius potest esse tali posteriori subducto, igitur possibile est ecclesiam viare prospere sine tali capitaneo. Mirum itaque foret, quod ita fuit de facto ex ordinacione divina, et cum modo non potest sic esse propter ordinacionem cesaream, sic quod ordinacionem Christi licet extinguere, sed ordinacio cesaris non potest deficere stante prosperitate ecclesie. Inconsequenter igitur loquuntur qui dicunt quod ecclesia potest prospere procedere sine Romano imperio adiuvante, ut patuit in primitiva ecclesia, et patet hodie de multis christianis, exemtis ab illo imperio infirmato, sed non potest stare sine suo episcopo vel ab eo collato privilegio. Numquid? fumus est maioris constancie quam ignis?

[ENGLISH]

## ¶6 · 318.27–318.30

> [p. 318] Nec valet ficticia qua dicitur, quod ordinacio pape processit immediate a Christo, ut patet de Petro, ordinacio autem imperatoris processit ab homine.

[ENGLISH]

## ¶7 · 318.31–319.34

> [p. 318] In ista autem materia necesse foret utramque partem cognoscere conclusiones ad confutandum cautelas dyaboli. Necesse est secundo distinguere inter papam, vel episcopum cesareum et ministrum [p. 319] simplicem christianum; nam iuxta dicta talis cesareus innititur privilegiis humanis tamquam principiis per se constituentibus servum talem. Minister autem pure christianus irridet hec privilegia ut superflua vel nociva. Et patet tercio defectus argucie, quando sic arguitur: Ordinacio pape immediate processit a Christo, ut patet de Petro, igitur ordinacio pape cesarei sic processit ex ordinacione Christi. Per papam Petrum et suos socios adiutores regebatur ecclesia, ergo per idem ex ordinacione Constantini oportet quod per gradus prelatorum cesareos regatur ecclesia; Christus indubie docens Matth. XX et Luce XXII maioritatem, quam sui debent attendere, negat istam arguciam. Si igitur Christus per se constituit capitaneum tocius militantis ecclesie, nec Petrus vel alius apostolus audebat talem capitaneum constituere vel se ipsum huiusmodi vendicare, sed constituerunt per loca episcopos, quanta irreligiosa presumpcio in cesare statuere, quod generaliter suus episcopus foret caput tocius ecclesie aut quod maioritatem civilem sub pallio privilegii contra decretum Christi in ecclesiam suam induceret? Ordinacio autem regis longe ante hec tempora processit a Deo, ut patet II De Civitate Dei XII, sic quod, licet Christus tempore legis veteris approbavit dominium seculare divinitus, et tempore legis nove approbavit multipliciter imperatorem, regem et dominum secularem humanitus, tamen nedum layci sed professores scripture verecunde proclamant, quando deficiunt argumenta, quod per idem vel forcius deficeret in ecclesia quodcumque dominium seculare.

[ENGLISH]

## ¶8 · 320.1–320.21

> [p. 320] Sed ista deduccio non habet fundamentum, nisi ut ironice loquar, quod autor scripture crebro ponit secularem primatum et sacerdotalem primatum cesareum interdicit. Et ideo dicit Crysostomus ut supra, quod in acceptando primatum ecclesiasticum neque est racio neque utilitas, quia tempore suo saltem in gente sua non fuit adiuncta primatui ecclesiastico, ut modo, pinguedo commodi temporalis. Si igitur signetur quicumque papa, cuius ordinacio immediate processit a Christo, videtur michi quod hoc docto totus populus debet eum venerabiliter amplecti. Sed nimis aliena est ab ista doctrina humana eleccio vel institucio. Ideo oportet quod illud doceatur ex vite et operum sanctitate; non ex aspiracione ad seculi commodum vel honorem. Nec ex fulminacione ficte censure ad ostendendum dominacionem nec ex tonsione gregis subiecti per fraudulentam temporalium subtraccionem, sed per condiciones apostolorum istis oppositas; et talis papa non foret alicui fidelium onerosus sed procurans undique pro lucro anime et profectu.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 316.25: Extravagant notions as to the need for an endowed pope.
- 317.1: It is said that without one secular sovernment would fall,
- 317.11: Both church and state, would be the better,
- 317.17: and more conformed to the law of God,
- 317.25: of the Church.
- 318.2: and civil law.
- 318.9: Civil rule existed before the popes were endowed,
- 318.31: We must distinguish between Caesarean prelates
- 319.1: and simple christian ministers.
- 319.16: Neither Peter nor any of the apostles claimed such rule over the Church and it was presumptuons of the Emperor to appoint precedence in his bishop.
- 320.9: Any pope ordained by Christ should by gladly received, but such would be marked out by holiness not by human election.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 316: *posset de-* (one main token covers two printed words; de- is the first half of de-|esse (next line), 25 is the line number) [THIN]
  - 316: *∅* (an is the English side note (the need for an endowed pope)) [THIN]
  - 316: *esse* (second half of de-|esse) [THIN]
  - 316: *privilegia* (hyphenated privi-|legia; main token holds the whole word) [R4]
  - 317: *placencius* [NW]
  - 317: *∅* (folio bar before Christo (240ᵇ in margin) read as i) [INS?]
  - 318: *Numquid* (25 is the line number) [R4]
  - 319: *∅* (30 is the line number) [R4]
  - 320: *Si* [R3]
  - 320: *humana* [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Neither Peter (319.16).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 316:
Codd. : clanstrare. 16. qni; B: quia. 25. Codd.: in marg. :
Papa cesarius si deest ecclesia sancta melius staret.
14. Decreti Prima Pars, Dist. XCV, cap. V.

p. 317:
3o. AB: in sacramentaliter.
24. See above p. 3 16. Decr. prima pars, dist. XGV, cap. V.

p. 318:
7. Codd. : humanis. 27. A in marg. : Argumentum pro papa.

p. 319:
17. nec; B: et. 3o. nedum ; B: negandum.

p. 320:
(none)
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 316: Heritis doluit, quod episcopus non potuit ordinari, | olim idem fuit episcopus et sacerdos,
```

---

## Chunk 12-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "320.23–324.6"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 2 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "834 words; 797 unanimous or majority-real; 27 settled by vote (DEL 2, R2 20, R3a 3, R5a 2); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n381–n385 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 2: [TITLE]

## ¶1 · 320.23–321.10

> [p. 320] Item, magnificantes necessitatem huius sacramenti cesarei oportet docere ipsam ex testimonio scripture vel per racionem ostendere necessarium influxum papalis preeminencie, quia aliter fingi posset novella religio servatis eisdem nominibus vel mutatis omnino contraria ordini christiano. Constat autem, quod primum deest in toto corpore scripture. Et quantum ad secundum, patet quod oporteret illum influxum vel adiutorium esse spirituale, quia sine corporali preter adiutorium quod ecclesia habet de seculari brachio posset stare. Si autem sit spirituale vel est actus anime vel habitus. Cum autem actus anime sint nobis notissimi, perceptibilis foret tam talis actus quam eius absencia in morte, in divisione vel [p. 321] omissione pape et in eius operacione apostolica; quando magis copiose et attente influeret? Sed nedum abest a nobis talis experimentalis noticia, sed propinquiores huic fonti sunt magis a Dei instinctibus alieni, ymo cum papa sit crebro infidelis vel expers donorum Dei quam eius subditi magis sancti, videtur quod non oportet regulariter hunc solem eclipsabilem sic in quoscumque lucidiores eciam plus tenebrosum in- fluere.

[ENGLISH]

## ¶2 · 321.11–321.25

> [p. 321] Nec valet dicere quod papa dat habitum, quia sic extolleretur super omne quod dicitur Deus, dans quantumcumque distanter eciam personis Deo indignis spiritualia dona Dei, quia quid blasphemius vel infidelius quam quod oportet Deum cum omni tali concurrere complendo quicquid promiserit. Unde si habitus vel donum spirituale Dei quiescat, sic quod ex influxu pape in animam subiecti quemque inclinaret ad opus, quod non experitur ecclesia, sed eius contrarium, tunc enim deesset Petro et aliis apostolis influencia illa cesarea, et cesare excedente Christum et eius vicarium correspondenter ad dotacionem vel ritus cesareos, cresceret vel decresceret potestas taliter influendi.

[ENGLISH]

## ¶3 · 321.26–322.17

> [p. 321] Ex mille evidenciis patet quod nichil est infidelius isto porismate, quod post do tacionem ecclesia non potest rite procedere sine tali papa cesareo. Nichil enim plus accusaret dotacionem vel caput huiusmodi de condicionibus Antichristi, quod foret abhominacio desolacionis, stans in loco sancto, ut expositum est in fine noni capituli et concordat Crysostomus Omelia ultima Operis Imperfecti. Pro cuius sensus declaracione repeto, [p. 322] quod Christus propheta summus prediceret pericula maiora ecclesie, quibus non est maius vel blasfemius quam cum vita yma, ut declarant Gregorius et Bernhardus, vendicare pompatice statum Christi. Cum igitur hoc sepe contingit de papa, ut patet ex cronicis allegatis, videtur quod Christus debuit periculum illud predicere. Sed ubi expressius, quam Matth. XXIV, 15 dicens: Cum videritis abhominacionem desolacionis, que dicta est a Daniele propheta stante in loco sancto, qui legit, intelligat. Daret autem fidelis operam ad intelligendum hunc textum propter tria, primo quia est textus viri desideriorum, ut patet Daniel IX, secundo quia est textus evangelicus a summa sapiencia repetitus, et tercio quia Christus ex magna causa precipit quod hoc legens ipsum intelligat.

[ENGLISH]

## ¶4 · 322.18–323.21

> [p. 322] Expositores autem verificant illud de Antichristo concorditer. Sed alii verificant hoc de Adriano imperatore vel alio, qui posuit statuam imaginis sue in templo Domini. Et alii fingunt sensus extraneos. Michi autem videtur quod nichil plus concordat cum litera vel ebdomalibus Danielis quam exponendo hoc de pseudopapa, qui est potissimus Antichristus. In hoc enim est abhominacio desolacionis, ut supra exposui. Nam communitas abhominaretur sentire unum fingentem personam Christi in interludio estivo et super hec extra formam ludi facientem turpidinem vel loquentem, quanto magis, quando quis pretendit vivaciter tamquam spectaculum toti ecclesie, quod gerit personam Christi, et tamen committendo peccata turpissima vivit Christo summe contrarie. Hec, inquam, nedum est abhominacio ut in ludo sed desolacio, deficiente [p. 323] capitali suffragio hoste Christi subdole introducto. Communis autem modus loquendi concordat, quod, papa stante in loco Petri vel papatu, per tantum aut tantum temporis ille locus debet esse sanctissimus, cum papa pretendit se stare in loco sancti sanctorum, in cuius signum consentit quod vocetur pater sanctissimus. Studeat igitur calumpniator huius sentencie de qua persona ecclesie pertinencius verificaretur dictum Christi ad literam, et cum de multis pseudopapis sit verum, quod sint abhominacio desolacionis stans in loco sancto, quid obest scripturam sacram gravidari ista sentencia, aut quid derogat profecie Christi, quod ipse predixit nobis illud periculum? Non enim videtur quod Christus locutus est de loco materiali, ut templo Jerusalem vel alio, quia nulla vel modica sanctitas nisi equivoce est in illo, sed loquitur de loco spirituali, qui est status sanctus, in quo succedit unus post alium et abhominacionem in tali loco necesse est fundari in clero.

[ENGLISH]

## ¶5 · 323.22–324.6

> [p. 323] Sed contra illud arguitur per hoc, quod Apostolus II. Tessal., II, 4 de Antichristo loquens prophetat quod in templo Dei sedeat, non igitur stat in loco sancto, et per consequens Christus ibi non loquitur de Antichristo. Primo tollo instanciam detegens fallaciam, nam et stabit et sedebit. Stabit ad erigendum et magnificandum suam potenciam tamquam paratus ad temporalia rapiendum, nam sicut Stephanus vidit Ihesum stantem a dextris virtutis Dei Act. VII, paratum ad membra sua certancia relevandum, et sic utrobique loquitur scriptura de stacione spirituali, quia (ut creditur) Stephanus non vidit stacionem corporalem ad tantam distanciam oculo corporali, [p. 324] ut notat Augustinus in De Cognicione Vere Vite prope finem. Nec phas est imponere in hoc militi Christi mendacium. Et ista maledicta stacio Antichristi implicat ipsum sedere, quia a ministerio Christi ad quod excellenter sed false se obligat ociantem. Et ista est mala sessio spiritualis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 320.23: The defenders of the Pope should prove his authority from Scripture or the value of his influence — over the Church.
- 321.11: Nor can he establish a relation between God and man.
- 321.26: The endowed pope is Antichrist.
- 322.18: The pseudopope is the abomination of desolation.
- 323.22: It is argued that Antichrist sits in the temple and so cannot stand.
- 323.31: 'There is no contradiction.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 320: *Constat* [R4]
  - 320: *∅* (main scan already holds Constat whole at pos 180) [INS?]
  - 320: *illum* [R3]
  - 321: *in-* (hyphenated in-|fluere; main token holds the first half, fluere follows) [R4]
  - 321: *blasphemius* [NW]
  - 321: *illa* [R3]
  - 321: *infidelius* (hyphenated in-|fidelius; main token holds the whole word) [R4]
  - 321: *tacionem* (do | tacionem split by folio bar (241ᵇ in margin), not a hyphen; this part only) [NW]
  - 322: *blasfemius* [NW]
  - 321: *dicitur* (LEFT-nw: print = dicitur) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustine's exposition. . . (324.8).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 320:
(none)

p. 321:
3. Codd. in marg. : Fons papa. 7. Codd. in marg. : Sol. 3i. Codd.
in marg. : Abhominacio desolacionis. 32. B: et exposiium est.
De Potestate Pape. 2 1

p. 322:
(none)

p. 323:
3. Cod. : stat. 22. Codd. in marg. : Antichristus quomodo ostenditur.

p. 324:
9. Codd.: Dei deest. i5. A in marg.: Antichristus quomodo osten-
1. Opp. tom. VI, App. VI, 182/3. 8. Opp. tom. VII, 687
Non est De Civitate Dei II, sed XX. i5. II. Tess. II, 2.
3o. II. Thess. II, 5— 1 1.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 321: extolleretur super omne quod dtcitur Deus, | abhominacio desolacionis, stans in loco sancto,
p. 322: Cum videritis abhominacionem desolacionis, que dicta est a Daniele propheta stante in loco sancto, | qui legit, intelligat.
p. 323: pater sanctissinuts. | abhominacio desolacionis stans in loco sanctOy | tn teniplo Dei sedeat,
p. 324: Non terreamini, quasi instet dies Domini, | nisi venerit dissensio primum, et revelatus fuerit homo peccati } filius perdicionis, qui adversatur et extollitur super omne quod dicitur Deus, aut qnod colitur, ita ut in templo Dei sedeat y ostendens se tamquam ipse sit Deus, | nulli dubium est, | eum de Antichristo isto dixisse, | Non retinetis, qnod cum apudZo vos essem, hec dicebam vobis, et nunc quid detineat } | Antichristus quomodo ostenditur.
```

---

## Chunk 12-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "324.8–328.20"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 3 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "973 words; 913 unanimous or majority-real; 37 settled by vote (R2 22, R3a 9, R5a 4, R6a 2); 23 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n385–n389 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 3: [TITLE]

## ¶1 · 324.8–326.3

> [p. 324] Secundo notandum quod Augustinus II De Civitate Dei quasi per totum exponens scripturam de Antichristo, specialiter Apokalipsim Iohannis et propheciam Danielis inter cetera capitulo II exponit textum predictum apostoli de Antichristo. Textus autem Apostoli, quem Augustinus dicit nullomodo pretereundum, in nostris codicibus ita iacet: Non terreamini, quasi instet dies Domini, quoniam, inquit, nisi venerit dissensio primum, et revelatus fuerit homo peccati filius perdicionis, qui adversatur et extollitur super omne quod dicitur Deus, aut quod colitur, ita ut in templo Dei sedeat, ostendens se tamquam ipse sit Deus, supple nisi talis Antichristus prius venerit, non veniet dies iudicii; nulli dubium est, inquit Augustinus, eum de Antichristo isto dixisse, unde Apostolus videns abhominacionem desolacionis, pro dolore loquitur interrupte, sicut Christus videns peccatum Jerusalem flevit dicens, quia si cognovisses et tu; supple peccatum tuum et penam exinde tibi infligendam; tu fleres, ut ego te defleo. Unde Apostolus consequenter declarat Antichristi versucias in hec verba: Non retinetis, quod cum apud vos essem, hec dicebam vobis, et nunc quid detineat [p. 325] scitis, ut reveletur in suo tempore; nam misterium iam operatur iniquitatis, tantum ut qui tenet nunc teneat, donec de medio fiat. Et tunc revelabitur ille iniquus, quem dominus Ihesus interficiet spiritu oris sui et destruet illustracione adventus sui eum, cuius est adventus secundum operacionem sathane in omni virtute et signis et prodigiis mendacibus et in omni seduccione iniquitatis hiis, qui pereunt, eo quod caritatem veritatis non receperunt, ut salvi fierent; ideo mittet illis Deus operacionem erroris, ut credant mendacio, ut iudicentur omnes, qui non crediderunt veritati, sed consenserunt iniquitati. Istum autem textum exposuit Augustinus secundum partem ex certa sciencia et secundum aliam partem tamquam sensum probabilem; certus est enim quod Apostolus hic loquens de Antichristo vocat eum hominem peccati et filium perdicionis, qui extollitur super omne, quod dicitur Deus. Est iterum Augustinus sicut et pius theologus de hoc certus, quod cuicumque viatori iste condiciones conveniunt hic est Antichristus. Et est tercio iste sanctus certus quod Christus non veniet ad diem finalis iudicii, quem Apostolus vocat diem Domini, iudicaturus vivos et mortuos nisi prius venerit ad seducendum in anima mortuos eius adversarius Antichristus. Primo quod iste sit sensus textus Apostoli, quod Antichristus, quem vocat refugam, sedebit in templo Dei, hoc est in ecclesia, non, inquit, templum alicuius ydoli vel demonis templum Dei vocat apostolus intelligens per Antichristum non solum ipsum principem, sed multitudinem impiorum hominum qui sunt quodammodo corpus eius. Unde in greco dicitur, tamquam in templum [p. 326] Dei sedeat, tamquam ipse sit templum Dei, quod est ecclesia. Sicut dicimus Petrum sedere in amicum id est velut amicus.

[ENGLISH]

## ¶2 · 326.4–326.27

> [p. 326] Secundo vero exponit sequencia: Sed nunc quid detineat scitis, ne adhuc veniat ille magnus Antichristus, quia oportet ecclesiam parum profundari in fide, nec ad coronam eius Antichristus reveletur in suo tempore. Iam enim misterium iniquitatis operatur Antichristus tacite in suis membris, ut dicit evangelista, ut fidelis christianus habens iudicia sui exercitus, qui tenet fidem ecclesie, nunc teneat in principio illam fidem, donec fiat revelacio de medio sue malicie. Victoria enim in belli inicio confundit adversarios et animat expugnantes; in medio enim illius concertacionis veniet unus capitalis malignus, licet post et antea erunt mali eciam usque ad diem iudicii, ut patet Daniel IX. Unde quia sensus Apostoli est multum absconditus, non confunditur iste sanctus dicere: Ego prorsus quid dixerit me fateor ignorare. Et recitando tres opiniones dicit prima, quod Neronem vocavit Apostolus tacite Antichristum, secunda quam Augustinus approbat, dicit hunc esse sensum Apostoli, qui tenet imperium, teneat donec tollatur de medio, quia post dotacionem ecclesie revelabitur Antichristus. Et tercia sentencia est supradicta.

[ENGLISH]

## ¶3 · 326.28–327.15

> [p. 326] Tercio vero prosequitur, quomodo Antichristus seducet virtute dyaboli tam m causa temporali, quam spirituali, in qua pretendet se habere virtutem m signis et prodigiis mendacibus, per que quidam intelligunt bullas atque epistolas de plenitudine potestatis papalis, plenas mendacio, ut verificant de indulgenciis et prefeccione inhabilium, quos menciuntur per eos esse habiles, [p. 327] cum divinum iudicium sit in multis contrarium. In temporalibus vero fingunt se super omnes seculares dominos dominari civiliter, et sic notato dicto Augustini, quod oportet Antichristum esse de Romano imperio, quod extinguet, ut dicit XXIV cap. et dicto beati Johannis quod Antichristi prenuncii magni Antichristi prodierunt ex apostolis et per consequens de clero, cum factis paparum Christo contrariis eliciunt quidam probabiliter quod ipsi perversi sunt pessimiAn-. tichristi; Deus autem secundum Apostolum mittet tales contra suos apostolos vel seductos in operacionem erroris, ut credant mendacio in penampeccati. Quod ego credo ydolatriam in colendo signa ut Deum, sicut specialiter patet in ostia consecrata.

[ENGLISH]

## ¶4 · 327.16–327.25

> [p. 327] Recolligendo igitur dicta superius, videtur michi quod aliqua sunt ex fide simpliciter concedenda, alia vero ut omnia scripture sacre contraria simpliciter sunt neganda. In tercio vero gradu sunt quedam probabiliter asserenda ut illa que probabiliter creduntur esse in scriptura sacra implicita. In quarto vero gradu sunt aliqua credenda probabiliter esse falsa ut illa de quibus habemus probabiliter evidenciam quod sunt scripture sacre contraria.

[ENGLISH]

## ¶5 · 327.26–328.6

> [p. 327] In primis vero et secundo contrariis iacet fides expellens formidinem. In mediis vero cadit formido cum prestanciori via ad credendum, ut m gradu tercio aut cum prestanciori evidencia ad discredendum ut in gradu ultimo. Et ista quatuor apud theologum sunt notanda; tunc dico me credere in primo gradu quod Antichristus est in predictis scripturis descriptus. [p. 328] is Secundo quod licet omnes presciti sint unus magnus Antichristus, oportet tamen esse unum principalem et maximum Antichristum. Tercio vero sive papa sive cesar sive quicumque alius fuerit maximus adversarius legis Christi, ipse est potissimus Antichristus.

[ENGLISH]

## ¶6 · 328.7–328.13

> [p. 328] Quarto credo quod dictus Antichristus cum omnibus suis complicibus damnabitur ex mendacio in die iudicii fugatis peccatorum tenebris et illucescente lumine veritatis. Ulterius dico tamquam michi probabile in gradu tercio quod papa sit ille Antichristus qui describitur in scriptura.

[ENGLISH]

## ¶7 · 328.14–328.20

> [p. 328] In istis autem mediis paratus sum cuicumque parti ad quam concepero quod evidencia est pocior consentire. Et sic dividitur diccio mea in fidem et opinionem. In fidem, concedendo vel negando, in opinionem, remisse credendo vel discredendo illa, quorum pura credulitas est mihi preternecessaria ad salutem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 324.8: Augustine's exposition.
- 325.26: The temple of God prophesied of is the Church.
- 326.28: How Antichrist is to lead men astray in temporal as in spiritual matters e. g. indulgences,
- 327.2: and claims to civil rule.
- 327.10: Antichrist is tocome from the clergy.
- 327.16: Degrees of belief and disbelief,
- 327.26: Wyclif fully believes that Antichrist is described in the scriptures quoted;
- 328.1: that there is one Chiefantichrist, who is the chief opponent of God's law and who will be damned.
- 328.11: He thinks it likely the pope is that Antichrist.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 324: *scripturam* [NW]
  - 324: *filius* [R4]
  - 324: *apud* (30 is the line number) [R4]
  - 326: *Petrum* [R5]
  - 326: *Iam* [NW]
  - 326: *concertacionis* (hyphenated con-|certacionis (15 line number); main token holds the whole word) [R3]
  - 326: *∅* (main scan already holds concertacionis whole at pos 102) [INS?]
  - 326: *est multum* (one main token covers two printed words) [R5]
  - 326: *post* (print "quia post" ends the line above dotacionem (25 line number); the main scan lost post) [INS?]
  - 326: *spirituali* [NW]
  - 326: *prodigiis* [NW]
  - 327: *seductos in* (one main token covers two printed words) [R5]
  - 327: *illa* [R3]
  - 327: *illa* [R3]
  - 327: *prestanciori* [NW]
  - 328: *Antichristum* [THIN]
  - 328: *∅* (will is the English side note (and who will be damned)) [THIN]
  - 328: *Tercio* (main splits Tercio into 1 + ercio; whole word given here, next token ∅) [THIN]
  - 328: *∅* (rest of Tercio, given whole at pos 19) [THIN]
  - 328: *illa* [R3]
  - 325: *aliam partem* (W-split: aliampartem -> aliam partem (two words run together)) [OVERRIDE-SCAR]
  - 327: *tichristi;* (LEFT-nw: second half of An-|tichristi) [OVERRIDE-SCARPLATE]
  - 328: *gradu* (LEFT-nw: print = gradu) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustine's exposition. . . (324.8).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 324:
9. Codd.: Dei deest. i5. A in marg.: Antichristus quomodo osten-
1. Opp. tom. VI, App. VI, 182/3. 8. Opp. tom. VII, 687
Non est De Civitate Dei II, sed XX. i5. II. Tess. II, 2.
3o. II. Thess. II, 5— 1 1.

p. 325:
24. B: diem die. 27. Codd.: primo quod after aposloli.
29. pag. 597.

p. 326:
17. 13: eciam deest. 24. B: apostolicum.

p. 327:
16. Codd. in marg. : Concedenda simpliciter neganda simpliciter.
20. Odd. in marg. : Asserenda probatur. 32. Codd. in marg. : Anti-
christus quis est.

p. 328:
16. Codd. in marg. : ^^.^.^^distinguitur. 3o. Codd. in marg.
Canoni\acionem nota.
3o. Gf. De Ecclesia p. 44 — 46.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 324: Non terreamini, quasi instet dies Domini, | nisi venerit dissensio primum, et revelatus fuerit homo peccati } filius perdicionis, qui adversatur et extollitur super omne quod dicitur Deus, aut qnod colitur, ita ut in templo Dei sedeat y ostendens se tamquam ipse sit Deus, | nulli dubium est, | eum de Antichristo isto dixisse, | Non retinetis, qnod cum apudZo vos essem, hec dicebam vobis, et nunc quid detineat } | Antichristus quomodo ostenditur.
p. 325: scitis, ut reveletur in suo tempore; nam misterium iam operatur iniquitatis, tantum ut qui tenet nunc teneat, donec de medio fiat. Et tunc revelabitur ille iniquus, quem dominus Ihesus interficiet spiritu oris | sui et destruet illustracione adventus sui eum, cuius est adventus secundum operacionem sathane in omni virtute et signis et prodigiis mendacibus et in omni seduccione iniquitatis hiis, qui pereunt, eo quod caritatem veritatis non receperunt, ut salvi | fierent; ideo mittet illis Deus operacionem erroris, ut credant mendacio, ut iudicentur omnes, qui non crediderunt veritati, sed consenserunt iniquitati. | templum alicuius ydoli vel demonis templum Dei vocat apostotus, | Unde in greco dicitur, tamquam in templum
p. 326: Dei sedeat, tamquam ipse sit templum Dei, quod est ecclesia. Sicut dicimus Petrum sedere in amicum id est velut amicus. | Sed nunc quid detineat scitis, | lam enim misterium iniquitatis operatur | Ego prorsus quid dixerit \ me | fateor ignorare. | qui tenet imperium, teueat, donec tollatur de medio,
p. 328: In istis autem mediis paratus sum cuicumque parti ad quam concepero quod evidencia est pocior
```
