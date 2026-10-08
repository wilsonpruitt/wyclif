# Translation brief: potestate-pape 10-e–10-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-10-e.md chunks/potestate-pape/wyc-potestate-pape-10-f.md chunks/potestate-pape/wyc-potestate-pape-10-g.md` once and fix what it reports.
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

## Glossary (the 301 rows these chunks use; the full file is GLOSSARY.md)

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
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
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
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia; prevaricacio | transgressor; transgression; transgression | Ruled 2026-09-28 (*prevaricacio* 2026-10-08, *Pot. pape* 155.10). *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| oculata fide | with our own eyes | Ruled 2026-10-02 (*Eccl.* 15, 352.27). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| acephala; incapitata | acephalous; unheaded | *Incapitata* pairs with *capitatus*. Ruled 2026-10-02 (*Eccl.* 18, 435.20–23). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
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
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 10-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "236.1–237.27"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 5 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "397 words; 375 unanimous or majority-real; 14 settled by vote (DEL 1, R2 6, R3a 3, R5a 4); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n297–n298 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 5: [TITLE]

## ¶1 · 236.1–237.14

> [p. 236] De indulgenciis vero quas ipsi distribuebant per bullas non recolo, sed committebant illas sine bullis divino iudicio. Nec credo quod omnes falsigraphi fundabunt oppositum. Arguitur igitur communiter: quod Deus posset concessisse Petro et cuicumque Romano pontifici, ut communitas credit, preeminenciam potestatis, nec probari poterit quod non fecit; igitur cum ista fides multum intererat devocionis fidelium, videtur quod theologus debet ipsam defendere et non infundabiliter impugnare. Ista argucia est plena mendacio, nam communitas credit multa impossibilia et heretica de potestate vicaria, ut puta quod quilibet papa habet tantam potestatem sicut Christus habebat humanitus, quod quilibet Romanus pontifex in quantum talis habet infinitum maiorem potestatem quam habet alius in concedendo indulgencias, cum terminum potestatis ponunt in aliis non in illo, sic quod eo ipso quo pretendit se quovismodo solvere vel ligare, eo ipso sic solvit vel ligat; et sic de infinitis summe impossibilibus atque hereticis. De veritatibus autem, quas credere debet communitas de pape preeminencia, non dubium quin probari potest ex scripture testistimonio vel ex sensu. Loquendo autem de excessu ficte potestatis, patet quod minor est falsa. Sed si loquamur de gradu potestatis possibili, patet quod non est color in hoc concludere quod debemus illum concedere, quia sic concederemus in papa et quocumque presbitero omnem potestatem sibi possibilem. Ex ista blasfema evidencia potest habere istam potenciam, igitur habet. Sed quis tunc resisteret Antichristo, cum iuxta hoc debemus mendaciter credere falsissimam extollenciam [p. 237] potestatis? Est igitur argumentum sufficiens, si quis extollit se de preeminencia potestatis ecclesiastice, ultra quod scitur fundari ex scriptura verbo vel opere fecisse sanctos apostolos, tunc non debemus credere huiusmodi potestatem. Et sic aliquam potestatem vendicatam debemus non credere, ut ego non credo, non obstante concessione Cesaris quod quilibet papa habet potestatem iurisdicionis sive regiminis super totam Yndiam, Yudeam et alias naciones, ymo credo quod non habet, sicut nec credo quod Petrus superstes habuit tam ample singulariter tantam potenciam, quia tunc nimis graviter ex negligencia peccavisset.

[ENGLISH]

## ¶2 · 237.15–237.27

> [p. 237] Tercio replicatur contra dicta per hoc quod multi sancti pape et episcopi, multi beati seculares domini et populi dotacionem ecclesie approbarunt, ymo aliter non haberemus papam vel ordinem episcoporum, et per consequens nec causarum ecclesiasticarum decisiones nec privilegiaciones nec sacramentorum aut ministrorum ecclesiasticorum ministraciones, quod est contra racionem naturalem, ut ecclesia sit ita acephala. Sicut igitur oportet esse principes seculares ita et principes spirituales, sicut exemplatum est in veteri testamento; nimis magna itaqueforet presumpcio cessare dotaciones, elecciones et leges ecclesie super istis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 236.1: Some argue that the powers ascribed to the pope tend to piety, though they cannot be proved,
- 236.27: Then we should credit every priest with every possible power and admit the pretensions of Antichrist.
- 237.1: It is said that withdrawing endowment would ruin the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 236: *indulgenciis* (the bar after it is a folio mark) [THIN]
  - 236: *ipsi* [THIN]
  - 236: *in* (15 is the line number) [THIN]
  - 236: *quantum talis* (one main token covers two printed words) [THIN]
  - 236: *Ex* [R4]
  - 236: *∅* (the inserted i is the folio bar before falsissimam) [INS?]
  - 237: *sufficiens* [R4]
  - 237: *preeminencia* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 236:
4. Codd. in marg.: Pape potestas infiniia. 9. Codd. : interterat.
22—23. Codd.: quas de papa credere debet commioiitas de pape preemi-

p. 237:
1. Codd.: excellenciam. 4. Codd.: vel nostro opere vel fecisse. Cf.
p. 283, 1. 3. i5. A in marg. : Tercio arguitur. Codd. in marg. : Pape
necessitas, nota bene. 3i. Codd. in marg. : Dotacionem approbantes
sancti peccaverunt.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 236: quas de papa credere debet commioiitas de pape preeminencia.
p. 237: Si solus Christtts,
```

---

## Chunk 10-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "237.28–241.33"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 6 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "904 words; 864 unanimous or majority-real; 22 settled by vote (R2 10, R3a 6, R5a 5, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n298–n302 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 6: [TITLE]

## ¶1 · 237.28–241.3

> [p. 237] Quantum ad istud sunt multa dicenda: primo quod argumentum non valet, cum omnes peccaverunt et egent gracia Dei, ideo docet decretum distinccione VIII: Si solus Christus, quod debemus solum sequi Christum, qui errare non potuit [p. 238] vel alios de quanto sequamur ipsum, ipse autem summus medicus non autorizavit dotacionem huiusmodi, sed verbo et opere reprobavit; et sic videtur michi quod omnes approbantes dotacionem illam peccaverant in hoc mortaliter vel venialiter plus vel minus; nec feramus hoc graviter de beatis, quia beatus Evangelista, qui detestatus est approbacionem huiusmodi fuit sanccior omnibus illis, et tamen ipse dicit: Si dicimus quia peccatum non habemus, nos ipsos seducimus et veritas in nobis non est I. Joh. I, 8. Nec est color si multa ecclesie utilia ex hoc processerant, ideo non fuit in illa peccatum; nam multa mala ex illa processerant, cum ex hoc deiecta est ecclesia cleri a statu perfecciori ad statum minus perfectum sine equivalencia recompense. Secundo seminavit discordiam in ecclesia, ut homines plus appetant preposituram propter fastum et questum quam propter meritum, ut patet superius VIII capitulo. Et tercio facit errores in eleccionibus, in legibus et omnino in officii cleri execucionibus. Aliter enim non est facile fingere, quare indigni tam frontose, tam impetuose et tam ociose ultra quam ante dotacionem aspirant ad pinguiores ecclesiasticas prelacias. Unde vellem eos qui sompniant quod quicquid mali regno contigerit est propter parcitatem vel subtraccionem dotacionis aut privilegiacionis cesaree discere et docere clare suas causales, et quare post dotacionem circa papatus tales magis contenditur quam perante; cuius causa experiencia doceri poterit, si subtracta dotacione cessaret aspiracio ad huiusmodi dignitates. Causa enim secundum philosophos est qua posita vel subtracta correspondenter [p. 239] effectus, posicio vel subtraccio consequetur. Cum igitur ante dotacionem non fuit talis divisio nec adhuc est, ubi non est ecclesia sic dotata, evidentissimum est, quod litura temporalium et voluptas honoris mundani est causa. Cum igitur omnia ista pericula evacuantur per expropriacionem et observanciam status quem Christus instituit, manifestum est (ut sepe repecii) quod elemosina foret expergefacere illum statum. Unde magna infidelitas est qua Antichristi discipuli excecant laycos, quod instar phariseorum Matth. V predicant esse sacrilegium auferre bona consecrata ecclesie, et sic sollempnizant facta que layci cecati stulte et superbe donaverant, sed decretum Christi non curant; et tamen luce clarius patet quod seculares debent postposito excommunicacionis timore in hoc errata corrigere, quia ut docet glossa ordinaria super decreto XXIV questio I cap. I: Sacerdos hereticus vel excommunicatus non excommunicat nisi se ipsum, et indubie omnis excommunicans propter restitucionem istius perfeccionis status sancte matris ecclesie est ut sic excommunicatus. Ideo non obstante malediccione sua bonum ecclesie est constanter et celeriter consummandum, ymo (ut patet alibi) sive excommunicatus sive insons maledixerit homini, non est timendum sibi, nisi de quanto declinaverit a Christi consiliis vel preceptis. Ideo (ut dicit glossa) non obstante excommunicacione tali homo debet saltem abscondite celebrare et facere quecumque bona de genere inturbate. Quod si pars Antichristi ad tantum prevaleat, quod sit Christiano plurior, christianus debet publice reclamare, quia talis foret gloriosa causa [p. 240] martyrii. Quod si queratur de gravedine peccati sanctorum episcoporum primitive ecclesie qui dotacionem receperant, certum est quod peccarunt graviter sed venialiter ex ingrata negligencia et consensu, ut patet ex decreto beati Jeronymi posito in De Consecracione, distinccione V: Non mediocriter. Et ista sciunt modo Silvestri, Augustini, Gregorii et consimiles, qui in hoc graviter peccaverunt. Sed secundo notanda est cecitas, quam sepe repecii, quod per locum ab insufficientissima similitudine cadimus paulative a statu apostolico, qui fuit status viantis perfectissimus, usque ad statum cleri cesareum qui est status cleri abiectissimus; capimus enim illud quod consonat peccatum in gestis sanctorum patrum, et illud extendimus, sed illud quod sonat virtutem omittimus. Ut sophistice arguitur, si dicti sancti receperunt temporalia supereffluenter ex pura secularium elemosina et totum residuum pauperibus erogarunt, igitur per idem licet nobis quantumcumque ample extorquere dominia tamquam sine elemosina secularium primo nobis debita, et dimisso eorum usu eis abuti quantumcumque voluptuose et seculariter conversando. Sic enim concludimus in effectu et, amplificando culpam ac dimittendo perfeccionem laudabilem, augemur nimirum difformiter ambobus partibus in voraginem viciorum. Ideo perfeccius atque securius foret nobis tenere limites quos Deus instituit, vivendo de decimis, oblacionibus et privatis elemosinis, quia transgrediendo terminos quos Christus instituit damus nobis et posteris evidenciam corruendi. Et hec fuit causa quare [p. 241] beatus Gregorius percussit iam mortuus successorem suum usque ad mortem, ut recitatum est VIII cap.

[ENGLISH]

## ¶2 · 241.4–241.6

> [p. 241] Sed instatur quod dicti sancti non penitebant de istis peccatis finaliter nec revocarunt errorem, sed pocius tamquam meritoriam auxerunt dotacionem.

[ENGLISH]

## ¶3 · 241.8–241.33

> [p. 241] Hic dicitur quod false assumitur nec umquam probabitur, ymo sancti ut remisse perceperunt errorem sic remisse laborarunt ad eius extinccionem, ut beatus Possidonius narrat de beato Augustino, quomodo rogavit cives suos, ut caperent possessiones quas sibi et sociis suis contulerunt, ut possint pure vivere de sorte Domini, tamquam clerici, sicut vixerunt in veteri testamento. Et sic videtur michi quod clerici et religiosi possessionati in ista appropriacione et proposito decedentes sine fructuosa penitencia sunt damnandi; et hanc reor racionem, quare Christus Matth. XXIV. 21- dicit: hoc tempus esse tantum horribile, non propter tribulacionem corporis sed anime infinitum maiorem, unde Apostolus II Thym. III, 1, 2 dicens, quod instabunt tempora periculosa, annectit tamquam signum et causam precipuam: Erunt, inquit, homines se ipsos amantes. Dyabolus enim ex cupiditate temporalium trahit plurimos ad infernum. Sancti igitur percipientes saltem confuse huius peccati maliciam, saltem confuse finaliter penitebant. Nos autem qui oculata fide percipimus huius avaricie invalescentis gravedinem, oportet penitere distinccius de tali avaricia et omnino de consensu et correpcionis negligencia, si volumus esse salvi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 237.28: Answer. 1. It is forbidden by God.
- 238.16: 2. Endowment has spread discord in the Church.
- 238.21: 3. It is a constant source of error and contention.
- 239.16: Laymen should not fear excommunication for withdrawing endowments.
- 240.6: The saints who approved endowment now know that they erred.
- 241.8: We must believe that the saints who approved endowment repented.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 237: *peccaverunt* (hyphenated pecca-|verunt; main token holds the whole word) [R4]
  - 238: *peccatum* [R4]
  - 238: *habemus* [R4]
  - 238: *Joh* [R3]
  - 238: *I* (italic capital I (I. Joh. I, 8)) [R3]
  - 238: *illa* [R3]
  - 238: *illa* [R3]
  - 238: *recompense* [NW]
  - 238: *qui* (25 is the line number) [R3]
  - 238: *∅* (the inserted i is the folio bar before est) [INS?]
  - 239: *illum* [R3]
  - 241: *II Thym* (one token covers two printed words (II. Thym.)) [R5]
  - 241: *III* [R5]
  - 241: *1* (old-style arabic 1, x-height (III, 1, 2)) [R4]
  - 238: *legibus* (LEFT-nw: print = printed) [OVERRIDE-SCARPLATE]
  - 240: *insufficientissima* (LEFT-nw: hyphenated insuffi-|cientissima) [OVERRIDE-SCARPLATE]
  - 241: *21-* (LEFT-odd: box on Matth.; token is verse number 21 followed by dash before dicit) [OVERRIDE-SCARPLATE]
  - 241: *huius* (LEFT-odd: box in blank gap after huius) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 22. Codd.: Tim. II. (241.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 237:
1. Codd.: excellenciam. 4. Codd.: vel nostro opere vel fecisse. Cf.
p. 283, 1. 3. i5. A in marg. : Tercio arguitur. Codd. in marg. : Pape
necessitas, nota bene. 3i. Codd. in marg. : Dotacionem approbantes
sancti peccaverunt.

p. 238:
11. Codd. in marg. : Dotacio quomodo prodest nocet. 21. Codd.:
exequencionibus. 27, 28. B: dotaciottes.

p. 239:
i5. Codd.: non curant postponere. 4. litura i. e. macnla.
19. Gf. Glossam ord. (ed. Venet. 1 5g5) I, p. 1295.

p. 240:
7. modo; Codd.: modi. 9. Codd. in marg. : Dotationem recipientes
sancti quomodo peccaverunt. 27. augemur. Ita codd.
6, Cap. XXIV.

p. 241:
4. Codd. in marg. : Dotacionis argumentum. 11. Recte: Possidius.
11. Cf. De Givili Dominio III, 225.
De Potestate Pape. 16
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 237: Si solus Christtts,
p. 238: Si dicimiis quia peccatum non habewius, nos ipsos seducimus | et veritas iu nobis non est I. Joh. 1, 8.
p. 239: Sacerdos hereticus | vel excommunicatus non excommnnicat nisi se ipsum,
p. 241: instabunt tempora periculosa, | homines se ipsos amantes. | Tim. II.
```

---

## Chunk 10-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "242.1–246.21"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 7 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1009 words; 951 unanimous or majority-real; 44 settled by vote (R2 27, R3a 11, R5a 6); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n303–n307 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 7: [TITLE]

## ¶1 · 242.1–242.5

> [p. 242] Consideraremus itaqae, quantum sancti eciam posteriores et peiores apostolis ab isto peccato cupidinis se servarunt et ipsum in scriptis ac verbis vivacibus reprobarunt, ut specialiter patet in scriptis et decretis beati Gregorii.

[ENGLISH]

## ¶2 · 242.6–242.30

> [p. 242] Sed adhuc replicatur, quomodo melius foret corrigere cleri cupidinem quam devote collata auferre? cum ista possunt meritorie possideri et securitas ac copia temporalium confortat et auget clericos, ymo habent hoc, cum sit meritorium et iuste petitum ex titulo doni Dei; grave itaque foret cum tanta subtraccione perturbare ecclesiam. Hic videtur michi quod evidencia non procedit, cum melius foret clericos conversari ut clericos generaliter quoad quoscumque dotatos; optimum itaque foret radicitus corrigere cleri cupidinem, auferendo venenosam occasionem, sic quod clerus reductus ad perfeccionem status primevi allidat parvulos reatus ad petram iusticie. Ista itaque foret correccio cupiditatis cleri fructuosior, permanencior et complecior, quam blasfema extorsio humanitus palliata. Qui enim sanaret vulnus vel morbum hominis, destrueret radicalem causam; qua dimissa remaneret patens occasio frutices cupidinis producendi; oportet tamen prudenter auferre radicem istam pestiferam, quando ex peccato notorio datur occasio auferendi, specialiter incipiendo a fonte cupidinis producendi, quia non cessabunt cupiditatum litigia nisi ipse fuerit exsiccatus.

[ENGLISH]

## ¶3 · 242.31–246.21

> [p. 242] Sunt autem mille occasiones sanandi ecclesiam, sed cautela dyaboli sparsi sunt favores et pax, quam Christus venit dissolvere, et sic dona mamone [p. 243] sunt inter legistas et clericos eciam exproprietarios et dominos seminata. Sed oportet quod Deus gladio vindicte quem venit mittere modo sibi abscondito, ut pestilencia, guerra vel alia pena racionali dissipet istas fraudes; tunc enim foret clerus proporcionatus in numero et virtute, ubi iam nocivus est undique vivis et mortuis: vivis non faciendo clericale officium peccati populi destructivum, et mortuis non mitigando penam defunctorum quam ex stultis donariis paciuntur. Et ista argucia: Hoc bene potest fieri, igitur non debet corrigi, multos cecat; securitas autem debet confidenter exspectari a Deo non seculo, et in hoc debet sperari tam nobis quam laycis vera securitas, et ideo precipit nobis Apostolus Hebre, ultimo, quod sumus contenti presentibus, ita quod confidenter dicamus: Dominus michi adiutor et non timebo, quid faciat michi homo. Et hinc petimus in oracione dominica: panem nostrum cotidianum da nobis hodie. Sed et nos sacerdotes innitentes ritibus legis veteris confidenter annuatim sine thaurizacione diutina porcionem Domini scilicet oblaciones et decimas expectamus. Quantum ad dacionem Domini, patet quod in penam peccati dat indignis, quod eis obedit, ut dicit Augustinus in De Verbis Domini Sermone LIII: Deus, inquit, iratus dat creature ad eius voluntatem et alias placidus dat creature ad eius utilitatem, eciam quod non appetit habere. Triplex autem ponitur exemplum primi, nam [p. 244] Yob primo legitur quomodo Deus dedit dyabolo potestatem ad temptandum beatum Yob in sui confusionem et sancti probacionem, sic eciam demones exauditi sunt petendo se mitti in porcos Mar. V, et sic Israhelite exauditi sunt secundum suum desiderium, scilicit confusionem in escis carnalibus, ut patet Psalmus LXXVII, 30: Adhuc esce eorum erant in ore ipsorum et ira Dei ascendit super eos. Sed Apostolus exauditus est in contrario illius, quod peciit. Nam II. Cor. XII, 8 ita dicit: Ter Dominum rogavi, ut discederet a me angelus sathane, et dixit mihi: Sufficit tibi gracia mea, nam virtus in infirmitate perficitur. Sunt enim nonnulli qui ex carencia temptacionis superbiunt, et sunt nonnulli qui ex fortitudine temptacionis senciunt de se ipsis humilius et gloriosius coronantur; et ideo preter beatitudinem et alia Per se bona debemus condicionaliter petere moderate, ut petendo temporalia debemus modum attendere; et condicionaliter petere, si et quatenus nobis prosunt. Et hec racio, quare petimus sub forma panis cottidiani temporalia necessaria hodie nobis dari, que Apostolus vocat presencia. Et constat, quod nimis levis est evidencia, Deus concedit eciam sanctis copiam temporalium et gloriam mundanam, igitur eis expedit vel est licitum sic habere, quamvis sint aliunde apud Deum laudabiles, verumtamen non in illo. Unde videtur quod nostri episcopi sunt Christo ingratiores quam Scarioth et legis veteris sacerdotes; ipsi enim tenuerunt se superficietenus, quoad possessiones in limitibus legis Dei, sed [p. 245] adulterati sunt abscondite in adulacione voti aut elemosine, ut patet Matth. XV; et ideo re mansit penes eos palliata clavis sciencie; unde et Christus Joh. V, 39 dicit eos putare vitam eternam habere in scripturis. Et Matth. XXIII, 3: Omnia quecumque dixerint vobis, facite, quod non diceret hodie de nostris episcopis propter ingratiorem defectum sentencie, ideo videtur quod sunt plus debriati avaricia et ingratitudine ignorancie, sapiencie prime opposite, quam irreligiositas Scariothis. Melius utique foret semel ad sanitatem perfectam perturbare ecclesiam quam quod remaneat continue periculosius, irreligiosius et lacius perturbata. Ulterius notandum est tercio, quod necesse est paparum et episcoporum ordinem esse in ecclesia militante. Sed duplicem ordinem talium ministrorum considera, scilicet cesareum et divinum. Quamvis autem oporteat ex malicia ordinem cesareum quem Christus approbat secundum totum bonum virtutis in eo bonum utile vel nature, necesse tamen est in eo esse malum culpe quod Deus reprobat, et sic dat Deus tyrannis et blasfemis bona que occupant sine eorum vero dominio. Alium autem ordinem divinum oportet esse integre secundum ordinacionem divinam, cum non per se sapit peccatum ut prior. Ipse autem ex institucione humana capit gradus suos, secundum quod variantur gradatim mundi divicie vel honores. Alius autem ordo hec respuens respicit pure et mundo abscondite ordinacionem divinamad plus vel minus prodessendum ecclesie; quando autem ordinacio humana concordat in persona quam Deus ad gradum talem elegerit, [p. 246] sapit minus peccatum et aliter colitur Antichristus. Unde nichil maius hereticum quam quod tam necessarius est iste ordo cesareus, ut nemo posset sine papa istius ordinis esse salvus, primo quod multis pseudopapis non existentibus, ut patet ex dictis, sancta duravit predestinatorum ecclesia, secundo quia trecentis annis et amplius, quibus sine dotacione crevit ecclesia, regulabatur sine tali primatu cesareo communi consilio sacerdotum. Pro quo tempore idem fuit sacerdos et episcopus, ut patet ex dictis. Tercio quod totus ordo talis fuit, institutus a cesare preter Christum, ut patet ex dictis VIII cap. Et nichil infidelius quam quod nemo potest modo salvari sine suo decreto tam extraordinario preter fidem. Sicut igitur conversi in Yndia et Grecia et aliis locis, ubi papatus noster non colitur, sunt christiani salvandi, eciam qui religiosius nobis vivunt: sic in Europa stat esse perfectos christianos secundum fidem Christi, etsi non cognoscant preeminenciam pontificis Constantini.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 242.6: It is said we should correct the clergy instead of taking away endowments.
- 242.13: The best way to correct is to take away the occasion of evil,
- 243.1: Mammon sows his gifts among the clergy, inviting God's vengeance.
- 244.17: Except for spiritual blessings We should be moderate in our prayers and submissive to God's will.
- 245.1: The priests of the Old Law were less corrupt than ours.
- 245.15: There must be popes and bishops, but they must be such as God has chosen.
- 246.2: Popes of human appointment not necessary to salvation.
- 246.10: For 300 years
- 246.11: bishops and priests were the same.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 242: *itaqae* (misprint kept: zoomed leaf clearly reads itaqae) [NW]
  - 242: *Sed* [R3]
  - 242: *auferre* [R3]
  - 243: *legistas* [R5]
  - 243: *faciat* [R4]
  - 243: *LIII* [R4]
  - 244: *ut* [R3]
  - 245: *∅* (elemosine already stands at pos 7 (the vote replaced the folio mark 222b there); this is a duplicate) [R6]
  - 245: *in* (5 is the line number) [NW]
  - 245: *quecumque* (hyphenated que-|cumque; main token holds the whole word) [R4]
  - 245: *facite* [R3]
  - 246: *fuit* [R4]
  - 246: *fuit* (main "same" is the English side-note word; the print has fuit here (line opens "fuit institutus") and the main scan lost it; institutus follows at pos 79) [R3]
  - 246: *institutus* (LEFT-odd: print = institutus) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 242:
5. Codd. in marg. : Dotacionis argumentum. 8. Codd. in marg. :
Ablacio temporaliam.
18, 19. Psalm CXXXVI, 9.

p. 243:
8. Codd.inmarg: Clerus quomodo nocetvivis etmortuis. 9. Codd.:
destruclum. 17. Codd. in marg. : Dat Deus indignis ad penam peccati.
34. dacionem; B: dotacionem. 3o. Codd. in marg. : Exaudiuntur mali
a Deo sibi in penam.
16. Hebr. XIII, 5, 6. 20. Lucae XI, 3. 27. Opp. tom. V,
1378: Aliquando Deus iratus dat quod petis et Deus propitius
negat quod petis.

p. 244:
7. Codd.: Psalm. LXXIX. i3. Codd.: in firntitate. 32. B: Dei
5__7. Matth. VIII, 32; Num. XI, 33; Psalm. LXXVII, 3o.
Eadem cxempla in Serm. St. Augustini 1. c.

p. 245:
17. Codd. in marg. : Ordo duplex sacerdotum. 21. Hic verbum
decsse vidctur.

p. 246:
2. Codd. in marg. : Sine papa potest homo salvari.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 242: allidat parvulos | ad petram
p. 243: sumus contenti presentibus, ita quod confidenter dicamus: Dominus michi adiutor et non timebo, quid faciat michi homo. | panem nostrum cotidiamim da nobis hodie. | iratus dat creature ad eius voluntatem et alias placidus dat creature ad eius utilitatem, eciam quod non appetit habere.
p. 244: Adhuc esce eorum erant in ore ipsornm et ira Dei ascendit super eos. | Ter Dominnm rogavi, nt discederet a me angelus sathane, et dixit mihi: Sufficit tibi gracia mea, nam virtus in infirmitate perficitur.
p. 245: vitam eternam habere bin scripturis. | Omnia quectimque dixerint vobis, facite,
p. 246: idem ftiit sacerdos et episcopus,
```
