# Translation brief: potestate-pape 05-b–05-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-05-b.md chunks/potestate-pape/wyc-potestate-pape-05-c.md chunks/potestate-pape/wyc-potestate-pape-05-d.md` once and fix what it reports.
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

## Glossary (the 248 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
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
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
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
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
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
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| demereri | to demerit | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 05-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-05-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-05-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "83.28–86.17"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 80.23); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "597 words; 573 unanimous or majority-real; 17 settled by vote (INS 1, R2 11, R3a 5); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n144–n147 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 5, part 2: [TITLE]

## ¶1 · 83.28–86.17

> [p. 83] Ex istis quarto colligitur, cum quilibet ex lege caritatis debet appetere maius bonum, sed maius bonum foret tam clero quam laicis, quod laici occuparent totam civilitatem secularis dominii, videtur quod clerici ex caritatis regulis hoc optarent. Ipsi enim forent exinde exonerandi et layci forent circa laycum officium in temporalibus meritorie occupati, quomodo igitur non dictaret [p. 84] caritas, que non querit que sua sunt, quod tota civilitas foret contenta in manibus laycorum. Nam nulli dubium quin secularia iudicia, contenciones, pugne et alia laboriosa manualia sunt laycis plus pertinencia, illud igitur magis bonum debet clerus appetere. Et quantum ad arbitrium cleri variantis in perfeccione ac utilitate bonorum seculi, standum est plus Christi et apostolorum arbitrio et non arbitrio nostrorum spiritualiter infirmorum. Et patet horrenda dampnacio istius sentencie tamquam heretice, quod seculares iuvent clericos exonerando eos a temporalibus, quibus nimis onerati sunt ex stultis dotacionibus dominorum. Et quantum ad obiectum quod per idem, cum layci conversi tempore apostolorum vixerunt exproprietarie, clerici debent ex habundanciori caritate auferre bona a laycis, constat quod pauci layci perfecte conversi per apostolos reliquerunt omnia temporalia sua et devenerunt clerici illiterati; et sic apostoli titulo elemosine auferebant illa relinquentes imperfectum, scilicet proprietatem civilem ut eis inconsonum. Et utinam nostri episcopi recolerent quomodo apostoli quorum officio funguntur taliter converterint laycos ad perfeccionem regule christiane, relinquendo quendo laycis coaccionem civilem. Perfecti enim debent niti assimilare inferiores ad suam perfeccionem et non per media illicita inducendo in eorum imperfeccionem. Papa igitur qui debet esse proximus vicarius Christi ducendo christianum exercitum ad eius sanctitatem debet ista principaliter facere tam opere quam sermone. Item, secundum principia philosophorum melius est [p. 85] philosophari quam ditari, sed quam bonum est philosophari tam bonum est amare sapienciam incarnatam, igitur melius estipsam diligere quam ditari. Sed de quanto christianus diligit legem suorum consiliorum sequendo ipsum in moribus, de tanto diligit ipsum, igitur hoc est melius quam ditari, cum stat hominem esse peccato miserrimum cum quantumlibet mundi multis diviciis. Ideo (ut sepe dixi) paupertas evangelica non stat in non habere temporalia, sed in moderate habere quoad modum habendi et multitudinem habiti propter amorem Christi, si quod quantumcumque temporalia iuverint ad faciendum opus viatoris officii, tantum precise Deus vult ut habeat. Unde cum in statu innocencie et statu patrie deficiet talis civilitas, videtur quod ipsa sapit imperfeccionem et est officio cleri dissonum; nec enim est necessarium ad humiliacionem nec evangelisacionem nec aliam sacerdotalem ministracionem sed ad vite ministracionem ad quam pauca ex promissione Dei sufficiunt. Ideo sapiens Proverb. XXX, 8 petit a Domino: Divicias et mendicitatem ne dederis michi, sed tantum viciui meo prebe necessaria. Consideremus igitur equalitatem iusticie, si aliquid habemus preter necessarium ad nostrum officium, et indubie senciemus quod superfluit nobis quodcumque civile dominium, cum multi clerici vivunt operosius sine tali; quare igitur non nos qui debemus scire quod Dei filius naturalis venit in mundum ob amorem nostrum in artissima paupertate, et hoc ad exemplandum nobis de sorte sua, ut ob eius amorem ac nostrum immensum commodum conversemur conformiter. Nec dubium quin sic multiplicaretur clerus ut olym, cum [p. 86] talis non foret familia secularibus onerosa nec in sustentacione subducto globo monstruose multitudinis sumptuosa. Si enim private elemosine, quando mundus fuit irreligiosior et clerus necessarior, suffecerunt ad sustentandum totum clerum Christi, quanto magis hodie superaddite oblaciones et decime. Subducamus itaque in clero avariciam, fastum et officio suo impertinens ac superfluum, et non dubium quin satis sufficerent et commodum spirituale ex hinc in secularibus et clericis circumcrescens infinitum excederet prosperitatem et gloriam mundanam ex opposito contingentem. Affecciones itaque personales caritati contrarie faciunt quod ordinacio Christi contempnitur et tot scripturarum ac sanctorum testimonia vel sunt sinistre glossata vel a clero infideliter parvipensa.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 83.28: who should desire all civil rule to be in the laity.
- 84.23: Would that our bishops like the apostles set an example of perfection and drew others to it.
- 85.8: Evangelical poverty does not consist in having no wealth, but in the spirit in which wealth is held,
- 85.25: For our work as priests we need no civil dominion.
- 86.3: Alms sufficed for the priests when Christians were fewer and there were no tithes.
- 86.14: Christ's ordinances are explained away or disregarded.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 83: *caritatis* [R3]
  - 84: *elemosine* (20 is the line number) [R4]
  - 84: *illa* [R3]
  - 84: *relinquendo* (hyphenated relin-/quendo; main token covers whole word) [R4]
  - 85: *∅* (1ᵈ is part of the folio mark 181ᵈ) [R4]
  - 85: *ministracionem* [R4]
  - 85: *prebe* (zoomed: b with closed bowl) [NW]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 1. I. Cor. XIII, 5. (84.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 83:
3. Decreti Secunda pars. causa XIV, q. V. cap. X.

p. 84:
28 Codd.: induendo.

p. 85:
4. Codd ; ditare, 8. B in marg.; Paupertas evangelica in quo stat.

p. 86:
17. A in marg. : Papa ornatus seculariter.
27. Cap. II (Migne) Opp. I, p. 776. Cf. Hussii Opp. 2i2b.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 83: Denique si 1 non potest
p. 84: non qnerit que sua sunt,
p. 85: Divicias et mendicitatem ne dederis michi, sed tantum viciui meo prele necessaria. | multi venient in nomine | suo, dicentes se esse Christus, et multos seducent, | ante diem iudicii oportety quod veniat dissensio primum et reveletur homo peccati, qui extollitur super omne quod | dicitur Deus. | Ecce hic Avinione est Christus | nolite credere, | ita et. | Discessio in Vulgate.
p. 86: Interhec tu pastor procedis deauraitts, tam multa circumdatus varietate. Oves quid capiunt? Si auderem dicere, demonum magis quam ovium pascua hec^o sunt. Non sic factitabat Petrus vel Pautus ludebat. | Pastorem te populo aut nega aut exhibe; non negabis, ne cuius sedem tenes \ te neges | heredem; Petrus hic est, qui nescitur processisse | Ideo videtur securum. | sr sr | cnm me ^ us f ore t ecclesie, quod nullus foret huiusmodi, quod vivamus ut ante dotacionem, quando ecctesia communiter regutabatur per socios, | Antichristi Iria signa ponit Augustinus.
```

---

## Chunk 05-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-05-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-05-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "86.18–89.20"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 80.23); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "707 words; 667 unanimous or majority-real; 24 settled by vote (R2 16, R3a 4, R5a 3, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n147–n150 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 5, part 3: [TITLE]

## ¶1 · 86.18–89.20

> [p. 86] Sed contra illud arguitur, primo de papa quomodo non sufficeret dignitati sui officii nisi haberet regna et copiosa dominia pro se et suis officiariis limitata. Et idem est iudicium de nostris episcopis atque abbatibus. Sed ad istud sepe dictum est quod officiariorum superfluitas et apparatuum sumptuositas est in causa. Unde correspondenter ad istorum crementum decrescit religiositas et edificatoria officiositas. Unde Bernhardus libro IV ad Eugenium: Inter hec tu pastor procedis deauratus, tam multa circumdatus varietate. Oves quid capiunt? Si auderem dicere, demonum magis quam ovium pascua hec sunt. Non sic factitabat Petrus vel Paulus ludebat. Et sequitur: Pastorem te populo aut nega aut exhibe; non negabis, ne cuius sedem tenes te neges heredem; Petrus hic est, qui nescitur processisse [p. 87] vel gemmis ornatus vel sericis, non teclus auro vel vectus equo albo nec stipatus milite nec circumstrepentibus ministris; absque hiis tamen credidit satis posse impleri salutare mandatum. Si amas me, pasce oves meas. In hiis successisti non Petro sed Constantino. Inconsequens igitur foret quod sequitur quod in prelatis mundi gloria sit sepulta vita edificatoria instar Christi et apostolorum in ipso abscondita et undique conversacio consona ac lucrifactiva in clero et laycis copulata. Sed donemus autori isti iniuriam. Non querat igitur prelatus mundanam excellenciam sed iuxta regulam Christi inferioritatem ministerii et pacienciam contemptus mundani et iniurie, si contingat propter fervorem anhelandi celestia et totum reputatum mundo inconveniens erit dulce; et loco momenti mundane glorie accrescet nomen vite et operum sanctitate et quod est maius gaudium eterna inscripcio libro vite. Unde racio quare non insequimur istam sentenciam est infidelitas, qua non credimus scriptis sanctorum et iudicio sapientum. Ad tantum enim pulvis mundi et suorum sensibilium nos cecat et diutina delectacio innaturalis in illis sopita palatum animi discrasiavit, quod ad magnum Ve nobis iuxta vaticinium Ysaie V, 20 dicimus bonum malum; et sic de illorum contrariis perversum est nostrum iudicium maniace in contrarium iudicium racionis, et tam multi ac magni inciderunt in istam rabiem, quod maior pars mundi arguet docentes et servantes istam sentenciam ut insanos, sic quod generalior, accusacior et perseverancior est persecucio in paucos docentes licet remisse [p. 88] istam sentenciam quam olim fuerat in prophetas. Cuius causa est quia superiores ecclesie qui videntur esse aliquid perseveranter dogmatizant oppositum, cum summe odiunt recedere a mundi deliciis, quibus ex declinacione a Christi vestigiis tam diu subdole sunt sopiti. Quomodo igitur non duceretur currus in precipicium cuius veredus et auriga ducit tam fervide ad deorsum? Secundo obicitur per hoc quod multi sancti dotacionem huiusmodi approbarunt; cum igitur in secularibus sit licita, foret in clericis magis sancta; quamvis igitur quibusdam expediat vivere exproprietarie, tamen decorat totum corpus cleri quod docetur ut regina celi sit circumdata varietate. Ad illud sepe dictum est quod tales argucie non procedunt, ideo cum sanctus sanctorum docet verbo et opere quod clerus suus debet omnem secularem modum habendi relinquere, patet quod sibi debemus in isto plene credere. Nam iuxta dicta non debemus credere vel imitari alium sanctum ecclesie, nisi de quanto in ipso sua sentencia est fundata. Specialiter autem debemus credere et exemplum capere ab illis sanctis, qui primicias spiritus habuerunt, modo autem ordine nimis prepostero fundamus nos in sanctis infimis et postremis, qui magis declinarunt ad seculum, supponentes infideliter si ipsi sic fecerant igitur bene, nam apostoli multa culpabiliter fecerunt de quibus posterius sunt purgati; et multo evidencius posteriores confessores commiserunt multa crimina, de quibus finaliter penitebant. Magna itaque cecitas in nostris arguere: ipsi sic fecerant, igitur bene. Quis igitur color, si isti per magnam partem vite sue appropriaverint [p. 89] dotacionem ecclesie, tunc non fuit illicita. Secunda stulticia est; qua plus credimus portentis quomodocumque factis, ut imponimus virtuti corporum mortuorum, quam signis vivacibus sanctorum evangelizancium, peccatores plurimos convertendo, in tantum quod si portentum tale sancto nostro ascribimus, cece arguimus quod quicquid fecerat non pecavit. Sed tercia stulticia est qua arguimus, si illi meritorie susceperunt elemosinas donatas ecclesie sub condicione, quam oportet intelligi, quod tunc nec licet ipsas auferre nostris, nec phas est negare, quin licet nobis ipsas expendere quomodolibet consumendo. Notaremus igitur formam, condicionem et usum sanctorum et equaremus ista in nobis, antequam concluderemus per locum a simili. Nec est color, si cerimonia sit in laycis meritoria, quod foret in clericis magis sancta. Sicut patet de homicidiis, de connubiis et multiplici meritorio ritu in laycis, qui foret in clericis venenosus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 87.11: Let prelates devote themselves to Christ's service and welcome the contempt of the world.
- 87.20: We are so blinded that we persecute those who teach Christ's doctrine.
- 88.9: It is urged that many saints have approved of endowment.
- 88.22: All saints are not to be followed in all things; even the apostles committed faults.
- 89.1: Another folly is the weight laid on portents as a proof of saintliness.
- 89.8: A third folly is to argue that if alms were rightly received they must not be withdrawn, even though the conditions of the gift are disregarded.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 86: *Inter hec* (one token covers two printed words) [R5]
  - 86: *tenes* (zoomed: t with crossbar) [R4]
  - 87: *teclus* (leaf 148 zoomed: 4th letter tall, no crossbar, unlike the short crossed t of vectus below = l (misprint)) [THIN]
  - 87: *auro* [THIN]
  - 87: *stipatus* [THIN]
  - 87: *hiis* [THIN]
  - 87: *Petro* [R4]
  - 87: *iniurie* [R3]
  - 87: *iudicium* [R3]
  - 88: *odiunt* [NW]
  - 88: *∅* (English side-note word) [R6]
  - 89: *∅* (quo-/modocumque is one word, already whole at pos 13 (quomodocumque)) [INS?]
  - 89: *nostris* [THIN]
  - 89: *nec* [THIN]
  - 89: *phas* [THIN]
  - 86: *correspondenter* (LEFT-odd: box covers only a speck/tick before ad; no word [coordinator: the box was the junk glued to the word; the word stands]) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 86:
17. A in marg. : Papa ornatus seculariter.
27. Cap. II (Migne) Opp. I, p. 776. Cf. Hussii Opp. 2i2b.

p. 87:
4. Cod.: implere. 21. Codd.: scripti.
4. Joh. XXI, l5.

p. 88:
9. A inmarg.: Secunda obieccio pro dotacione. 10. B: huius ; modi
deest. 32. Codd.: ipsis. 34 an : approbaverint (?)

p. 89:
3. Godd.: virtute. 21. A in marg. : Divicie quomodo venenant eccle-
siam. 23. A in marg ; Nota quomodo clerus potest cum Deo habere
omnia bona que habet et quomodo ea sancti habuerunt.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 86: Interhec tu pastor procedis deauraitts, tam multa circumdatus varietate. Oves quid capiunt? Si auderem dicere, demonum magis quam ovium pascua hec^o sunt. Non sic factitabat Petrus vel Pautus ludebat. | Pastorem te populo aut nega aut exhibe; non negabis, ne cuius sedem tenes \ te neges | heredem; Petrus hic est, qui nescitur processisse | Ideo videtur securum. | sr sr | cnm me ^ us f ore t ecclesie, quod nullus foret huiusmodi, quod vivamus ut ante dotacionem, quando ecctesia communiter regutabatur per socios, | Antichristi Iria signa ponit Augustinus.
p. 87: vel gemmis ornatus vel sericis, non teclus anro vel vectus equo albo nec stipatns milite nec circumstrepentibus ministris; absque Jtiis tamen credidit satis posse impleri salutare mandatum. Si amas | me, pasce oves meas. In hiis successisti non Petro sed Constantino. | bonum malum; | Ignorantes Dei iusticiam et | suam volentes constituere, iusticie Dei non sunt subiecti. | est aliud ignorare Dei iusticiam et snam veile constituere nisi dicere, ego iosanctifico, ego iustifico, quod ego dedero sanctum est, dimitte Deo quod Dei est, agnosce, homo, quod hominis est; ignoras Dei iusticiam et tuam vis constituere, iustificare me vis, sufficit tibi ut mecum iustificeris. | Ego veni in nomine patris mei et non accepistis me, Si alius venerit in nomine suo, illum accipietis. | De Antichristo dictum est, et omnes sic inteltigunt: Ego veni in nomine patris mei et non suscepistis me, si alius venerit in nomine suo, hunc suscipietis. Sed audiamus Johannem: Audistis, quia Antichristus venit, et nunc Antichristi multi facti sunt. Quid | f autem expavescimus in Antichristo, nisi \ quia nomen suum honoraturus est et nomen domini contempturus. Quid aliud facit, qui dicit: Ego iustifico? respondet eis subditus, ego ad Christum veni | ego sanctifico, ego sancttfico.
p. 88: non pedibus sed corde; ubi evangelium audivi, ibi credidi, et ille: Non es mundus. Ouare? quia non fui ibi. | Scrutamini scripturas, quia putatis in illis habere vitam eternam, et ilie sunt que testimonium perhibent de me. | Anten, amen dico vobis,^ non potest Jilius a se ipso facere quicqnam, nisi quod viderit patrem facientem. | cium meum iustum est, quia non quero voluntatem | meam sed voluntatem eius, qui misit me, patris.
p. 89: testimonium maius Johanne, opera enim que dedit michi pater ut perficiam; ipsa opera que ego facio testimouium perhibent de me. | Si boni sumus, | facite quod scriptum est: Imitatores mei estote, sicut et ego Christi. Si autem mali sumus, | sic nec deserti estis nec sine Consilio remaitsistis; audite dicentem: Que dicunt facite, toque autem faciunt nolite facere. Sed prelati contra hec: Nisi boni fuerimus, peristis. Sed hic est alius, qui veniet in nomine Christi. | fundamentum atiud 2o nemo potest ponere nisi Christum, | applica de.
```

---

## Chunk 05-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-05-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-05-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "89.21–93.30"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 80.23); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "958 words; 915 unanimous or majority-real; 28 settled by vote (R2 15, R3a 8, R5a 4, R6a 1); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n150–n154 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 5, part 4: [TITLE]

## ¶1 · 89.21–93.30

> [p. 89] Notandum tamen quod temporalia non occasione ab eis data sed male accepta venenant ecclesiam. Si enim totus clerus diceret effectualiter quod omnia temporalia que habemus ut clerici forent pure elemosine secularium et bona communia pauperum, secundo effectualiter et indifferenter ministraremus de illis magis egentibus et tercio consumeremus precise de illis quantum est necessarium ad nostrum clericale officium, possemus proprietate usus et ministerii occupare licite omnia temporalia que habemus. Et sic occuparunt omnes sancti episcopi ex mundi diviciis commendandi. Quod si blasfemamus quod nude materia [p. 90] successionis Christi et apostolorum qui dominati sunt seculariter omnibus mundi diviciis habemus hec omnia, et secundo consumimus illa differenter seculariter et proprietarie, et tercio dimittimus vel remittimus exinde debitum officium clericale, manifestum est quod irreligiose, iniuste et proditorie consumimus bona Dei; et hoc totum inportaret in clerico monstruosa civilitas. Sed dubitatur supposito usu legitimo, quis modus vivendi foret perfeccior; nec dubium quin modus vivendi parcior et exproprietarius, quia est securior et vite Christi ac innocencie utrique conformior. Vix enim reperies mundi divitem quin vel nimis afficiatur et occupetur circa eius divicias vel inique ipsas distribuat vel tercio voluptuose atque superflue ipsas consumat, in tantum quod de divite j evadente ista pericula scribitur Eccli. XXXI, 9: Quis est hic et laudabimus eum? fecit enim mirabilia in vita sua. Et hec fuit racio quare sapiencia Dei patris ob amorem nostri sic vixit exproprietarie et docuit suos cariores sic vivere. Ex quo invincibiliter colligitur quod status cuiuscumque cleri vel episcopi foret subducta appropriacione dotantis perfeccior, licet aliqui sancti in hoc evadant periculum, quia indubie predicta triplex occupacio temporalium foret ad onus cuiuscumque clerici qui intenderet perficere officium clericale; nam multitudo familie et mundani honoris nimis distraherent. Distribucio vero corporalis elemosine pertinet ad ministerium laycale, clerico intento ad distribuendum spirituales elemosinas pociores. Et sic ex dotacione sparguntur in clero macule, que ultra varietatem, quam Christus instituit, non pulcrificant matrem [p. 91] nostram. Et si dicatur quod alicui clerico foret melius sic dotari, revera hoc est valde remotum ad inferendum quod status dotati cleri sit statu exproprietarie viventis perfeccior. Sic enim expediret alicui clerico quod foret laycus, ymo ut dicit Christus Math. XVIII: Expedit scandalizanti ut suspendatur mola asinaria circa collum eius et demergatur in profundum maris. Hoc est secundum beatum Gregorium in De Cura Pastorali II expediret prelato] prescito quod ob errorem laycalis officii sit dampnatus. Non igitur sequitur: Utilius foret Petro esse in statu tali; igitur status ille est alio statu perfeccior. Nam iuxta istam vesaniam quilibet gradus turpis status foret statu honesto perfeccior, quia status perfeccior, quem statuatus deturpat, facit per accidens quod deturpatori peius eveniat, sicut inferioritas status potest cum gracia Dei esse causa per accidens unde homo amplius mereatur: ymo necesse est ut status dyaboli ac membrorum suorum prosit per accidens ecclesie, sicut status peccandi Petri et aliorum sanctorum secundum Augustinum fuit multum expediens. Numquid propterea servabimus talem statum? Notato igitur illo clerico; quem decorat imperatoris dotacio, patet quod ipse posset eque perficere opus predicandi; orandi et contemplandi sine tanta copia terrenorum; cum omne quod per se superaddit sonat in mundi gloriam et retardat ab officio clericali, quomodo igitur non foret status signancius ex dotacione imperfeccio? Et idem est argumentum de quocumque clerico signato; ex quo colligitur quod si status tocius cleri dotati foret alteratus [p. 92] in statum exproprietarium similis statui apostolorum vel rectorum m communi vivencium pure de oblacionibus, decimis et privatis elemosinis, uniformitas faceret ad decorem ecclesie, quia pulchrius pulchriori additum, facit totum aggregatum pulchrius quam totum minus pulcrum additum minus pulchro. Unde igitur auctoritas membris ecclesie sic strangulare contra exemplum vel autoritatem Domini clerum suum, cum in veteri testamento non licuit] arare in bove et asino nec indui vestimento ex lana et lino, ut patet Numeri XII et Deutronomii XXII. Si igitur levite et sacerdotes legis veteris et Christi discipuli vixerunt conformiter, quare non sic viveret clerus sequens? quam uniformitatem Christi vicarius debet incipere, ut coraula; Christus enim fuit homo pauperrimus sic quod nemo potuit esse pauperior; ut hic supponitur, quomodo igitur non eius sequax in terris simillimus, cum paupertas illa sonat perfeccionem virtutis viancium. Sicut igitur oportuitPetrum in fide, in humilitate; in caritate evidencius sequi Christum ex dictis in fine tercii capituli, sic oportet Petri vicarium sequi ipsum. Sed que fides est regulam perfeccionis, quam Christus instituit, tam cito propter mundum deserere? Vel que humilitas est sine auctoritate Christi supra alios mortales, eciam supra elemosinantem seculariter se extollere? Nam libro IV dicit Bernhardus ad papam Eugenium, ut recitavi superius: In hiis, inquit, successisti Constantino non Petro. Et beatus Jeronimus, ut recitatum est XCII distinccione Olim, et XCV distinccione Absit, dicit quod tale sacramentum [p. 93] superioritas non est a Deo et tunc indubie est a dyabolo. Si igitur papa viveret recte exproprietarie cum ceteris paribus sicut Petrus, quomodo non omnes eius subditi conversarentur conformiter? Et istam doctrinam dat Petrus I Pet. IV precipiens quod seniores et prepositi non sint dominantes in clero sed forma gregis. Et illud verbum notaret Petri vicarius propter reverenciam dignitatis. Quantum ad caritatem non video quin repugnat perfectissime caritati viantis quod in Petri vicario sit tam dominativa et copiosa possessio, quia cum caritas non querit proprietatem huiusmodi, ut dicit apostolus I. Corint. XIII, patet quod si Petri vicarius ex fervore caritatis omnia illa propter amorem Christi relinqueret, sicut fecerunt apostoli, quod cum paribus foret in eo caritas intensior et foret Petro similior, qui Actuum III, 6 confitetur: Argentum, inquit, et aurum non est michi. Et tunc liberalis dominus donaret sibi meliorem possessionem, scilicet virtutem faciendi miracula, sic quod curatus dicere possit cum Petro: Quod autem habeo, hoc tibi do, scilicet sanitatem; qui enim habet virtutem sanandi, habet eius fructum, licet non formaliter. Cum igitur iste gradus caritatis foret vicario Petri possibilis et ab illo deficit in magnum dampnum ecclesie, videtur quod propter dissimilitudinem non sit Petri vicarius et per consequens neque heres.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 89.21: Endowments would be quite other if we recognized that they are the common property of the poor.
- 90.1: We claim wealth as Christ's heritage but use it as worldly property.
- 90.13: Danger of riches.
- 91.11: It may be best for a given man to be in a state that is not the best.
- 91.20: Even the devils profit the church accidentally.
- 92.1: All priests should live alike and only on alms.
- 92.16: The pope should set the example.
- 93.10: That the pope should have so much wealth is against charity,
- 93.18: If like Peter, he had not gold or silver, God might give him the power of healing.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 90: *illa* [R3]
  - 90: *hic* [R4]
  - 91: *ut* [R3]
  - 91: *ille* [R3]
  - 92: *exproprietarium* [THIN]
  - 92: *similis* [THIN]
  - 92: *levite* (print has v) [NW]
  - 92: *coraula* [NW]
  - 92: *fuit* [R3]
  - 92: *illa* [R3]
  - 92: *hiis* [R4]
  - 92: *et XCV* (one token covers two printed words) [THIN]
  - 93: *dyabolo* [R4]
  - 93: *illa* [R3]
  - 93: *sanandi* (hyphenated sa-/nandi; main token covers whole word) [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Danger ot (90.13).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 89:
3. Godd.: virtute. 21. A in marg. : Divicie quomodo venenant eccle-
siam. 23. A in marg ; Nota quomodo clerus potest cum Deo habere
omnia bona que habet et quomodo ea sancti habuerunt.

p. 90:
8. A in marg. : Nota quod perfeccior modus est vivere clero expro-
prietarie, id est, nihil horum sibi appropriando vel ecc/esie.

p. 91:
10. B: Clerico prescito. 20. suorum ; codd. : ecclesie.
St. Gregorii De Cura Past. I pars, cap. II. Looselv quoted.

p. 92:
5. Codd.: pulcrus. %. Codd.: stragulare. 2h. Cod.: eliantem.
?o. Cap. III. V. p. 87. 32. Olim = Disi. XCV, cap. V. In
distinccione Abstt quae supra memorantur non inveniuntur.

p. 93:
io. quin; codd. : quando. i3, 14. B: modi deest. 23. Godd.: do
6. I. Petr. V, 3. 10. Cf. Hussii Opp. 2i2b.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 89: testimonium maius Johanne, opera enim que dedit michi pater ut perficiam; ipsa opera que ego facio testimouium perhibent de me. | Si boni sumus, | facite quod scriptum est: Imitatores mei estote, sicut et ego Christi. Si autem mali sumus, | sic nec deserti estis nec sine Consilio remaitsistis; audite dicentem: Que dicunt facite, toque autem faciunt nolite facere. Sed prelati contra hec: Nisi boni fuerimus, peristis. Sed hic est alius, qui veniet in nomine Christi. | fundamentum atiud 2o nemo potest ponere nisi Christum, | applica de.
p. 90: Quis est kic et laudabimus eum? fecit enim mirabilia in vita sua. | Unaui Sanctam | per visnm ter | iucrepavit, et quarto | in capite percussit, quo dolore vexatus pauio post obiit. | ad papam Innocencium misit Robertus Lynconiensis episfolam invectivam satis et tonantem, pro eo quod ecclesias Anglie indebitis exaccionibus vexare videretur; hac de causa ad curiam vocatusio est, et cum ibi moiestaretur, appeJlavit constanter a curia Innocencii ad fribunat Christi; uude contigit, quod Roberto in Aitgiia obeunte audita est vox in curia pape: Veni miser ad \ iudicium; reper- | tusque est in crastino papa exauimis, quasi cuspidezb baculi in Jatere percussus. Qni licet perspicacius effutserit miraculis, transferri tamen in sanctorum catJiaJogo a curia novi est permissus. | Obediencia pape nota bene. | Greporins sanctus papa occidit siinm successorem. | Appellavit Lincolniensis ad tribunal Christi. 3.
p. 91: Expedit scandalizanfi ut suspendatur mola asinaria circa collum eius et demergatur iu profundnm maris. | Nunc autem divina, | consilio congregato Confessus quod fecerat et in se tidit sentenciam deposicionis, et | veuiens coram Dyocleciano, confessus est se esse christianum | Omnia que- 20 cumque dixerint vobis, facite. | tibi fecit ecclesia ut eam veiis quodammodo decoltare? qui, | sic decoiiare 6 | Marcellinus papa ydolatravit. | in secidari. | Caput ecclesie,
p. 92: In hiis, | successisti Constantino non Petvo. | tale sacra-
p. 93: mentum superioritas non est a Deo et tunc indubie est a dyabolo. | seniores et prepositi non sint dominantes in clero sed forma gregis. | loaurum non est michi. | Ouod autem habeo, hoc tibi do,
```
