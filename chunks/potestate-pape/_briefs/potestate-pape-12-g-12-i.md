# Translation brief: potestate-pape 12-g–12-i

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-12-g.md chunks/potestate-pape/wyc-potestate-pape-12-h.md chunks/potestate-pape/wyc-potestate-pape-12-i.md` once and fix what it reports.
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

## Glossary (the 280 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
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
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| ociatores | men of leisure | Ruled 2026-10-02 (201.27). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| brocardicum / brogardicum | brocard | The schoolmen's stock maxim. Ruled 2026-10-02 (*Eccl.* 16, 360.9). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
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
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| exequie | exequies | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
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
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| patronus (a saint) | patron | A second sense beside the benefice row; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.17–19). |

---

## Chunk 12-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "338.9–342.18"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 7 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "951 words; 923 unanimous or majority-real; 18 settled by vote (R2 9, R3a 9); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n399–n403 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 7: [TITLE]

## ¶1 · 338.9–339.25

> [p. 338] Ideo talis evangelizans predicaret vitam et doctrinam Christi, in qua non est periculum. Secundo exponeret quomodo sanctus, cui innititur non in lege quam Christus instituit, declinavit, tercio consideraret si modum ita laudabilem sicut fecerunt patroni, quibus innitimur, observamus, quia cum Deus remunerator est adverbiorum, modus est maxime attendendus; quarto vero consideraremus in vitis patrum, si patres nostri ordinis spissius vixerunt et sanccius, quando viventes exproprietarie et nobis contrarie secuti sunt facilius et similius salvatorem. Modicus enim error, qui est insensibilis ex pravitate peccati, est ex continuo incremento sensibile et intoUerabile peccatum, a tota ecclesia destruendum, sicut specialiter patet in dotacione ecclesie, que a nuda elemosina crevit in venenosum dominium. Sic igitur duplex illud morale principium, practizatum in via morum, retrocedere est illicitum et de duobus bonis est pocius et facilius eligendum, rectificaret totam ecclesiam; ideo sine excusacione debemus omnes effectualiter illud attendere. Sed redeundo quantum ad secundam sentenciam de necessitate legum ecclesie, patet ex sepe dictis, quod melius regeretur ecclesia pura [p. 339] lege Domini quam per se vel cum adiectis legi domini legibus hominum adinventis. Patet ex hoc quod primo modo honori Dei conformius, ad serviendum sibi direccius et inducendum pacem ecclesie copiosius, regularetur ecclesia. Unde antichristiana heresis videtur quod lex Dei non est per se sufficiens nec eque sufficiens ut leges hominum extinguere iniurias in ecclesia germinantes, nam ad confundendum tales infidelitates de Antichristo dicitur Psalmo IX, 21: Constitue Domine legislatorem super eos, ut sciant gentes, quoniam homines sunt ad imaginem Dei, quibus creavit legem in reputacione sua completam condere; ideo debent secundum illam conversari ut homines et non ut bruta. Deus enim ex summa sapiencia legem condidit et dedit ecclesie ad hunc finem. Ideo si lex humana foret ad hoc lege Dei complecior, Antichristus in potencia, in sapiencia, et in providencia excederet Jhesum Christum; et tunc vera foret discipulorum eius sentencia, quod expedicius foret ecclesie quod legerentur in missis epistole decretales quam epistole apostolorum vel evangelium; nam secundum quod lex est necessarior et expedicior est magis venerabilis et plus meritorie commendanda.

[ENGLISH]

## ¶2 · 339.27–340.14

> [p. 339] Item, lex Christi plus pacificat cum Deo et plus disponit ad salutem anime, quam tradicio humana, sed in quantum lex hec fecerit, est honorabilior ac necessarior, igitur lex Christi excellit proporcionabiliter tradicionem humanam. Et cum pax quam habet homo cum Deo infinitum excedit pacem aliam, sicut salus anime et spiritualis prosperitas infinitum excedunt bona alia, que [p. 340] per leges hominum acquiruntur, patet quod lex Dei infinitum excedit leges hominum; et ex eodem sequitur quod sit infinitum prestancior ad placendum Deo et paciendum cum populo, nam per observanciam illius legis et non aliter placeretur, et per consequens pacificaretur homo cum Deo; sed nacta pace cum Deo, acquiritur pax cum qualibet creatura. Quomodo rogo, non obediret et proficeret quelibet creatura homini, cui videret Deum suum amicabiliter obedire, igitur etsi membra dyaboli tribulant amicos Christi, tamen prosunt illis, ut obedienciarii et amici; sic enim Scarioth fuit amicus Christo, Joh. XVIII, et procuravit licet invite serviens pacem Christi.

[ENGLISH]

## ¶3 · 340.15–340.26

> [p. 340] Item, lex Christi per se gigneret copiosius? caritatem in populo quam leges hominum per se vel commixte legi Domini. Et patet conclusio corollaria. Assumptum patet ex hoc, quod lex Domini precipit quoad bona nature prebere per cucienti maxillam sinistram Matth. V 39, 40, quoad bona fortune volenti auferre tunicam dare et pallium, ymo volenti tecum in iudicio contendere et tunicam tollere dare debitum; unde Luce VI, 30 dicitur: Qui aufert que tua sunt ne repetas. Et ista triplex paciencia per se induceret plenam pacem, extinguendo discordias.

[ENGLISH]

## ¶4 · 340.27–340.35

> [p. 340] Nec valet infidelis obiectus, quo dicitur quod tunc extingueretur complementum iusticie, quia Deus foret necessitatus ad providendum sue ecclesie ex hinc ad melius, ymo sic accederet ad statum exproprietarium plus perfectum. Ideo idem foret sic dicere et blasfeme imponere Deo inpotenciam, negligenciam sive invidiam, et per consequens quod legifer nonnullus extollitur super omne, quod dicitur Deus.

[ENGLISH]

## ¶5 · 341.1–342.7

> [p. 341] Unde consequenter profundantur in heresim, qui dicunt quod status dotacionis sit perfeccior quam status expropriacionis, et per consequens lex papalis qua stabilitur dotacio est perfeccior quam lex Christi, qua suadetur expropriacio; nam ut inquiunt iste due leges et isti duo status convertibiliter se sequuntur, quia aliter omnino superflueret lex humana et venenose pasceret populum postposito verbo vite. Oportet enim populum illum regi magis intendere, cuius legem preponderat; quia lex et status quem stabilit, se invicem consequuntur. Unde videtur michi nota infidelitatis et dolosa calliditas Antichristi, quod domini temporales statuunt sibi tales pastores et prophetas, qui et artem pascendi ignorent et preparent vel inordinate vel toxice cibum mentis. Constat autem ex fide scripture quod anima pascitur verbo Dei: verba autem alia sunt venenum anime; cum autem non sic ordinant pro coco et cibo corporis, et secundum Crysostomum prelati debent esse stomachus corporis ecclesie et cocus membrorum eius, patet quanta infidelitate laborant mundi principes, qui plus appreciantur atque preponderant cocum corporis coco mentis. Illi autem, quorum Deus venter est, non sunt filii pacis, cum pax prima cum Deo dissolvitur. Et in isto notabiliter deficit doctor fidei christiane. Oportet enim primo rectificare in ecclesia apostolos et prophetas et consequenter residuum corporis ecclesie erit sanum. Illi autem stabilirent hoc necessarium principium fidei modo discreditum propter excecacionem pulveris temporalium, quod quilibet christianus [p. 342] debet infinitum plus amare virtutes quamhonorem, voluptatem vel commodum temporale, sicut debet infinitum plus odire peccatum eciam veniale quam penam aliquam corporalem, et idem principium fidei per hoc quod, ut aliquid est peius vel melius, est ipsum fugiendum proporcionabiliter vel amandum.

[ENGLISH]

## ¶6 · 342.8–342.18

> [p. 342] Ex quibus sequitur quod lex Christi eciam secundum consilia sit generaliter servanda et lex hominum postponenda. Exhinc enim accrescit bonum anime infinitum preciosius quam lucrum aliquod temporale. Et hec racio moveret eciam infidelem, nam melius, facilius et brevius foret observare Christi consilia et precepta, igitur non debemus inniti suis contrariis prestancius omittendo. Peccamus igitur graviter, dum facimus nobis inexpediens, et honorem Dei diminuens, utilitatem ecclesie subtrahendo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 338.9: What preaching should be.
- 338.31: No laws but Christ's needed.
- 339.27: Christ's law makes us at peace with God.
- 340.15: Christ's law would breed more charity,
- 340.27: and God would provide for justice.
- 341.1: To advocate endowment Is a heresy.
- 341.18: God's word is the food of the soul.
- 342.8: Christ's law should be followed even as to its counsels.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 338: *Sed* (the main token read the English side note "but"; this slot is the only one for the printed Sed) [R4]
  - 339: *tradicio* [R4]
  - 340: *copiosius* (15 is the line number) [R4]
  - 340: *accederet* (30 is the line number) [R4]
  - 341: *illum* [R3]
  - 341: *preponderat* [R3]
  - 341: *toxice* [NW]
  - 342: *Ex* [R4]
  - 340: *per* (LEFT-odd: first half of per-|cucienti; box misplaced on Domini) [OVERRIDE-SCARPLATE]
  - 340: *V 39,* (LEFT-odd: print has V and 39, separated by a space; box misplaced) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 338:
1. B: obligant. 9. Codd. in marg. : Predicacionis modus de sanctis.
n. A in marg. : Nota. 12. lege ; cod.: hoc; cf. p. 33y 1. 16.
32. Codd. in marg. : Lege Dei sine humanis legibus ecclesia optime
regeretur.

p. 339:
5. R: et regularetur. n. Codd. : sed ut. 17. Codd. in marg. :
Lege Dei impossibile est esse meliorem.

p. 340:
a3. B: tunicam contendere.

p. 341:
10. B: legi. 11. B: preponderant. 20. Codd. in marg. : Cocuni
corporis preponderantes coco mentis peccant graviter. 27. B: de-
fecit.

p. 342:
1. Codd. in marg. : Amare debet christianus virtutem plus infinitum
auam voluptatem etc. 3. Codd. in marg. : Odire debet homo plus pec-
catum eciam veniale quam penam.
24. Cap. XII. 29. Ep. LXXVII. Sed est ad Oceanum.
Opp. ad Migne Ser. Lat. XXII, 691.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 339: Constitue Domine legislatorem super eos, ut sciant gentes, quoniam homines sunt
p. 340: prebere per~ cucienti maxillam sinistram } | auferre tunicam dare et pallium, | volenii tecum in iudicio contendere et tunicam tollere | Qui anfert que tua sunt ne repetas. | extollitur super ornne, quod dicitur Deus.
p. 341: prelati debent esse stomachus corporis ecclesie et cocus membrorum eius,
p. 342: Quicquid viris iubetur, hoc cousequenter redundat ad | feminas, neque enim adultera uxor dimittenda est
```

---

## Chunk 12-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "342.19–345.21"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 8 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "663 words; 598 unanimous or majority-real; 49 settled by vote (R2 33, R3a 15, R5a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n403–n406 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 8: [TITLE]

## ¶1 · 342.19–343.31

> [p. 342] Et de ista subtraccione a libertate legis Christi post multiplicitatem legum Antichristi conquesti sunt sancti; quod patet in exemplo triplici, primo ex decreto beati Augustini ad inquisiciones Januarii superius recitato et ponitur in decretis XII distinccione: Omnia; secundo ex dicto beati Jeronymi epistola CXVIII ad Domicianum de morte Fabiole, ubi exponens illud evangelium Matth. XIX, 9, ubi dominus precepit viris uxorem non debere dimittere, excepta causa fornicacionis, et dimissam manere innuptam sic loquitur: Quicquid viris iubetur, hoc consequenter redundat ad feminas, neque enim adultera uxor dimittenda est [p. 343] et vir mechus tenendus. Si quis meretrici coniungitur unum corpus efficitur, igitur que scortatori impuroque sociatur, unum cum eo corpus efficitur. Alie, inquit, sunt leges cesarum, alie Ihesu Christi, aliud Papinianus, aliud Paulus noster precipit. Apud illos viris inpudicicie frena laxantur, et solo stupro atque adulterio condempnaio, passim per lupanaria atque ancillulas libido permittitur, quasi culpam dignitas faciat, non voluptas; apud nos quod non licet feminis, eque non licet viris. Igitur in lege Christi oportet fidelem quiescere, et alias leges, nisi de quanto consonant legi Christi, contempnere, quod sepe oportet de vocata lege ecclesie. Unde beatus Bernhardus libro primo ad Eugenium sic effatur: Quid servilius indigniusque presertim summo pontifici, quem non dico omni die, sed pene omni hora insudare talibus rebus et pro talibus. Deinde quando oramus, quando docemus populos, quando edificamus ecclesiam, quando meditamur in lege? Et quidem cottidie perstrepunt in pallacio leges, sed lustiniani non Domini. Si iustum istud, tu videris, nam certe lex Domini immaculata convertens animas. Hec autem non tam leges quam lites sunt et cavillaciones subvertentes iudicium. Tu igitur pastor et episcopus animarum, qua mente obsecro sustines coram te, semper silere illam, garrire istas? Fallor, si non movet tibi scrupulum perversitas hec, puto quod interdum compellat te clamor ad Dominum cum propheta: Narraverunt michi iniqui fabulaciones, sed non ut lex tua.

[ENGLISH]

## ¶2 · 344.1–344.25

> [p. 344] Ista autem secundum fidem scripture sunt a papa et quolibet episcopo meditanda, et postpositis cunctis legibus extraneis effectualiter exequenda. In extraneis enim legibus iacet a lege Christi et per consequens a Deo distraccio, utriusque testamenti offensio et periculosa ac latens iniuriacio. Quis (queso) dubitat, quin occupacio circa leges hominum, que omnes sunt conclusio ad viacionem superflue, de tanto distrahunt pusillam capacitatem anime a lege Domini? Quis insuper hesitat de legislatore Christo, quem oportet omnem salvandum sequi? Psalmus primo, 2 scribitur: In lege eius meditabitur die ac nocte, ymo Deutronomio VIII, i dicitur: Omne mandatum quod ego precipio tibi hodie, cave diligenter ut facias. Et quia ad hoc requiritur mandatorum noticia;] ideo Deutronomio VI, 6; precipitur post precepcionem observancie omnium mandatorum erunt verba hec, que ego precipio tibi hodie, in corde tuo, et narrabis ea filiis tuis et meditaberis sedens in domo tua et ambulans in itinere, dormiens atque consurgens. Et Joh XIV, ab equo dicitur: Si quis diligit me, sermonem meum servabit. Nichil enim attencius mandatur a Domino, quam iugis meditacio legis Dei.

[ENGLISH]

## ¶3 · 344.26–345.10

> [p. 344] Et quantum ad tercium patet, quod in legibus humanis est fraudis et iniurie plenitudo. Patet hoc de principiis vel maximis legum ecclesie, et multo magis de conclusionibus ex illis sequentibus. Nam libro VI de constitucionibus datur pro regula, quod duobus super eadem provisione litteras a papa habentibus una die, is, cui papa [p. 345] canonicatum contulit preferendus est ei cui non dedit canonicatum, ignorante executore quis prius impetraverit. Si autem sint pares in gracia, quoad formam stili papalis, is qui prius presentavit erit pocior in prebenda. Et tercio si equales fuerint in hiis tribus, tunc canonici, quibus spectat collacio, vel maior pars eorum tenetur eligere reliquo carente fructu gracie nisi ex tenore papalium litterarum expresse appareat, quod papa utrique illorum voluerit providere.

[ENGLISH]

## ¶4 · 345.11–345.18

> [p. 345] Ista autem trimembris maxima videtur in toto esse principium contra Christum, quia supposito sicut in maiori parte contingit, quod prepositus in canonicatu vel tempore, in presentacione vel ostensione gracie, vel tercio in capitali eleccione sit reliquo quantumlibet indignior quoad Deum, tunc ex ista maxima Antichristi debet iudicari contra Christi iudicium.

[ENGLISH]

## ¶5 · 345.19–345.21

> [p. 345] Ex quo manifeste sequitur quod hoc Antichristi porisma sit iniquum contra iusticiam et per consequens contra Christum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 344.7: Attention to human law distracts us from God and his law.
- 344.26: Fraud and injustice in human law.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 343: *et* [R3]
  - 343: *ancillulas* [R4]
  - 343: *dignitas* [THIN]
  - 343: *faciat* [THIN]
  - 343: *∅* (folio bar after ad (246ᶜ in margin) read as i) [INS?]
  - 343: *Deinde* [R3]
  - 343: *pallacio* [NW]
  - 343: *iudicium* [R3]
  - 344: *Quis* [R3]
  - 344: *diligenter* (hyphenated dili-|genter (15 line number); main token holds the whole word) [R3]
  - 344: *Joh XIV* (one main token covers two printed words (Joh. XIV,); 15 is the line number) [R4]
  - 345: *canonicatum* [THIN]
  - 345: *canonicatum* [R5]
  - 345: *hiis* [R4]
  - 343: *Papinianus,* (W1: Papiniauus, -> Papinianus, (scans: papiniauus | papinianus | papiuianns | papiniauus)) [OVERRIDE-SCAR]
  - 343: *leges* (LEFT-odd: specks above e in leges (print: leges)) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 342:
1. Codd. in marg. : Amare debet christianus virtutem plus infinitum
auam voluptatem etc. 3. Codd. in marg. : Odire debet homo plus pec-
catum eciam veniale quam penam.
24. Cap. XII. 29. Ep. LXXVII. Sed est ad Oceanum.
Opp. ad Migne Ser. Lat. XXII, 691.

p. 343:
1. A in marg. : De meretricio ; B in marg. : Meretricacio. 2. B:
igitur deest. 2, 3. Codd.: scortatori imponitur sociatur. 6. Codd.:
in viris pudicicie. 12. B: consonant deest. i5. B in marg. : Leges
humane supra legem Christi garriunt ante papam. 18. B: et deest.
14. Cap. IV. Opp. I, 732.

p. 344:
11. Codd.: hesitat quin. 14. Codd. in marg.: Lex Dei debet diligen-
tissime studeri. 25. quam. B: quod. 3o. Codd. in marg. : Lex papalis
patitur instanciam.
i3. Psalm. CXVIII, 85. 3o. Liber Sextus, tit. II. Sed est
titulus III De Rescriptis, cap. XIV Duobus.

p. 345:
i. ei. Codd.: eo. 3. B: impetravit. 16. B: fit.
28. Esse videntur titt. III— VI.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 342: Quicquid viris iubetur, hoc cousequenter redundat ad | feminas, neque enim adultera uxor dimittenda est
p. 343: et vir mechus tenendus. Si quis meretrici coniungitur, unum corpus efficitur, igitur que scortatori impuroque sociatur, unum cum eo corpus efficitur. Alie, | sunt lege^s cesarum, alie Ihesu Christi, | aliud Papiniauus, aliud Paulus noster precipit. Apud illos viris inptidicicie frena laxantur, et solo stupro atque adulterio condempnato, passim per lupanaria atque aucillulas libido permittitur, quasi culpam dignitas faciat, non voluptas; apud nos ^quod non Hcet feminis, eque non licet viris. | Quid servilius indigniusque presertim summo pontifici, quem non dico omni die, sed pene omni hora insudare talibus rebus et pro talibus. Deinde quando oramus, quando docemus populos, quando edificamus ecclesiam, zoquaudo meditamur in lege? Et quidem cottidie perstrepunt in pallacio leges, sed lustiniani non Domini. Si iustum istud, tu videris, nam certe lex Domini immaculata convertens animas. Hec atitem non tam leges quam lites sunt et cavillaciones subibvertentes iudicium. Tu igitur pastor et episcopus animarum, qua mente obsecro sustines coram te, semper silere illam, garrire istas? Fallor, si nou movet tibi scrupuhim perversitas hec, puto quod interdum compellat te clamor ad Dominum cum Zopropheta: Narraverunt michi iniqui fabulaciones, sed non ut lex tua.
p. 344: In lege eius meditabitur die ac nocte, | Omne mandatum quod ego precipio tibi hodie, cave dili- | genter ut facias. | erunt verba hec, que ego precipio tibi hodie, in corde tuo, et narrabis ea filiis tuis et | meditaberis sedens in domo tua et ambulans in itinere, dormiens atque consurgens. | Si quis diligit me, sermonem meum servabit. | duobus super eadem provisione Utteras a papa habentibus una die, is, cui papa
p. 345: cauonicatum contulit preferendus est ei cui non dedit canonicatum, ignorante executore quis prius impetraverit. Si autem sint pares in gracia, quoad formam stili papalis, is qni prius presentavit | erit pocior in prebenda. Et tercio si equales fuerint in hiis tribus, tunc canonici, quibus spectat collacio, vel maior pars eorum tenetur eligere } reliquo carente fructu gracie nisi ex tenore papalium litterarum expresse appareat, qnod papa utrique | illorum voluerit providere.
```

---

## Chunk 12-i: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-i.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-i
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "345.22–349.26"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 9 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "907 words; 874 unanimous or majority-real; 20 settled by vote (R2 6, R3a 8, R5a 6); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n406–n410 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 9: [TITLE]

## ¶1 · 345.22–347.25

> [p. 345] Ex quo patet ulterius, quod sit a fidelibus tamquam hereticum abrogandum, et per consequens papa non debet pro toto mundo secundum ipsum generaliter causas ecclesiasticas terminare. Et idem est argumentum de generalibus legum paparum principiis, et specialiter de maximis Bonifacii VIII in Sexto, que manifeste obviant legi Dei. Non enim preferunt nec sciunt preferre quem Deus preelegit, sed communiter preeligunt maximum Antichristum, quia cum Judas non dormit avaricia debriatus sepe contingit quod membrum dyaboli preferatur; calliditas [p. 346] enim vulpina sepe preficit minus dignos. Unde apostoli non audebant nec potuerunt sicut nec Christus talem legem statuere. Ideo ista vocata lex est Antichristi, qui extollitur super omne quod dicitur Deus. Christus enim non potest ex nuda prelacione momenti temporis, ex callida presentacione priori collacionis papalis nec ex iterata eleccione sepe frivola capituli acceptantis, ineptum virtute preponere, sed oportet omnino, quod ille quem Christus vel lex sua preeligit, sit quoad Deum virtute prestancior. Et hinc apostoli non presumpserunt vel legem eleccionis statuere vel Mathiam eligere, sed commiserunt hec divino iudicio, ut patet Act. I. Sic autem faceret papa, cum pro toto mundo non statueret legem iniustam vei committeret peccatum eciam veniale. Est autem maior blasfemia constanter asserrere quod eo ipso quo Papa hoc sta tuit eciam contra decretum Domini, tunc est iustum, vel quod oportet quod Deus condescendat pape et legem quamcumque pape iustificet. Vel tercio quod levem iniuriam homo debet committere propter maius commodum inde sequens. Cum igitur quoad omnes causas terminandas per se sufficit lex scripture, quomodo presumeret Christi vicarius legem assumere tam iniquam quoad iniurias, commoveatur utraque pars pati iniurias et propter periculum tempus sibi redimere. Hoc autem ex fide est melius quam iudicium quod sentenciat lex humana, quod si neutra pars voluerit decreto Domini in talibus humiliter consentire, compromittant ponendo se in arbitrio boni viri vel ad minimum iudicentur secundum leges civiles intra ecclesiam, vel si omnia ista renuerint, fugiantur tamquam ethnici et publicani [p. 347] et discipuli Antichristi. Et nullomodo trahat Christi vicarius huiusmodi causas sibi, sed effugiat ut venenum iuxtaexemplaria legum civilium condere novas leges, sedabnuentem finaliter hancviam triplicem, excommunicet ut membrum dyaboli. Excommunicanten im quandoque simplices; quia dissentire renuunt legi. Et patet quomodo preter papam oportet esse, sicut fuit in primitiva ecclesia, unum caput ad causas ecclesiasticas terminandum. Quoad secundum patet quod oportet esse unum caput ad beneficia ecclesiastica parciendum, nam lex Christi est ad illud sufficiens, et persona populi, cui preficeretur talis prepositus, foret optimus iudex ad discernendum talem prepositum episcopo presentandum. Sic enim fuit in primitiva ecclesia; nec cessat racio, quare non sic foret hodie. Nam illa persona tenerrime provideret de mediis ad salutem anime necessariis cuiusmodi est pastor discretus; si enim providet de mediis corporis nutritivis, fides necessitat quod infinitum plus provideat de mediis anime nutritivis. Ideo Ecclesiastici XXX, 24 dicitur: Miserere anime tue placens Deo. Istam igitur providenciam non est Christi et per consequens nullius creature vetare.

[ENGLISH]

## ¶2 · 347.26–347.31

> [p. 347] Quantum ad legem, patet quod sola lex Christi perfecte docet pastoris officium, quomodo introducendus est, quomodo nutriendus et quomodo castigandus; illam igitur legem oportet communitatem christianorum defendere et tradiciones contrarias impugnare.

[ENGLISH]

## ¶3 · 347.32–348.26

> [p. 347] Sunt igitur tam ex parte electorum quam electi pericula. Ex parte electoris in hoc, quod posset blasfeme presumere quod sufficit voluntas [p. 348] sua; cum signo ab eo accepto ad rite constituendum prelatum ecclesie; et sic foret personaliter Ihesus Christus. Oportet enim Deum prius eligendo et habilitando constituere, cuius ordinacioni concordans sagax instrumentum Dei potest esse nudus promulgator divine sentencie, et ignorando divinam sentenciam reticeret, sicut fecerunt apostoli in eleccione Matthie. Si enim contrariatur divine sentencie, tunc peccat; nec debet sibi in hoc credi nec a fidelibus consentiri, quia aliter posset papa esse cum sibi adherentibus, infra modicum tempus maximus Antichristus, quia proditorie contra Christum dissipans oves suas; hoc autem est signum potissimum Antichristi. Item; est valde possibile quod papa ignoret vel negligat personam ydoneam gregi fideli postponere, sed nimis periculosum et stultum foret cum hoc preficere prelatum ecclesie, igitur in illo officio adiacet pape magnum periculum. Cum igitur in omni tali pars securior est tenenda videtur quod securius et optacius foret illud dimittere et per consequens papa peccaret in eligendo partem tam periculosam atque ambiguam. Nam iuxta legem pape in De Consecracione distinccione V: Non mediocriter peccat, qui bono postposito eligit minus bonum.

[ENGLISH]

## ¶4 · 348.27–349.6

> [p. 348] Assumptum patet in facto de distancia personarum inexpertarum quas ex nudo verbo testium eorum sepe preficit, et ex hoc quod ipse ac examinatores sui ignorant communiter mores persone extranee, et quoad scienciam sepe preponderant artem litigandi civiliter arti curandi animas; quod est condicio Antichristi. Recoleret [p. 349] igitur quomodo omni facinori perversi prepositi quem stulte sic preficit est non solum consenciens sed ipsum capitaliter auctorizans; pape igitur sanctissimi istam dominativam formam preficiendi prepositos non temptarunt. Que igitur prudencia, quod infirmiores pape hoc facerent?

[ENGLISH]

## ¶5 · 349.7–349.26

> [p. 349] Item, grave peccatum est propositis e duabus partibus minus bona eligere, sed hoc sepe contingit in preposituris papalibus, igitur sepius sunt inique. Quis ergo color excommunicandi omnes, qui resistunt pagine tam inique. Iste itaque error sepe devolvit profundius quod excommunicetur persona, quia facit ut debet conformiter legi Dei. Assumptum patet ex hoc; quod Deus vult et precipit quod homo eligat pociora, quia aliter excusaretur stulticia, ne sapiat peccatum et liceret voluntati Dei quamlibet deformari. Principium igitur nature est, quod homo eligat sibi utilius, ideo plane sequitur ex primo principio quod homo debet sic facere. Et hec racio quare fides scripture docet orare et petere condicionaliter media, de quibus ignoratur utrum sint magis utilia. Nec dubium quin Deo bono sit beneplacitum; quod homo laboret continue circa sibi utilius, quia aliter foret invidus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 345.27: Godless laws of Boniface VIII.
- 346.18: It is blasphemy to say that God confirms all laws made by the pope.
- 347.10: How appointment to benefices should be made.
- 347.32: Dangers attending choice.
- 348.27: The Pope often appoints persons of whom he knows nothing,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 345: *preferre* (30 is the line number) [R4]
  - 346: *asserrere* (print has double r (asserrere), kept as printed) [THIN]
  - 346: *quod* [THIN]
  - 346: *eo* [THIN]
  - 346: *quo* [R4]
  - 346: *sta* (sta | tuit split by folio bar (247ᵇ in margin), not a hyphen; this part only) [THIN]
  - 346: *tuit* (second part of sta | tuit (folio bar); 247ᵇ is the folio mark) [THIN]
  - 346: *eciam* [THIN]
  - 346: *vel* (20 is the line number on that line) [R4]
  - 347: *illa* [R3]
  - 348: *inexpertarum* [NW]
  - 349: *preficiendi* [NW]
  - 349: *ideo* (20 is the line number) [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Dangers choice. ^ (347.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 345:
i. ei. Codd.: eo. 3. B: impetravit. 16. B: fit.
28. Esse videntur titt. III— VI.

p. 346:
(none)

p. 347:
2. modi deest. 10. Codd. in raarg.: Capnt nnum oportet esse ad
distribuendum benejicia. 32. Codd. in marg. : Eleccio prelati habet
pericula.

p. 348:
3. B: Christus deest. 25. peccat. Recte: errant. 29. Codd.: tes-
than florum.
24. De Consecr. Cap. XXIV.

p. 349:
i5. Codd. in marg. : Distribucio beneficiorum quid confert pape.
3i. Codd. in marg. : Eligere pociora homo vult Deus.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 345: cauonicatum contulit preferendus est ei cui non dedit canonicatum, ignorante executore quis prius impetraverit. Si autem sint pares in gracia, quoad formam stili papalis, is qni prius presentavit | erit pocior in prebenda. Et tercio si equales fuerint in hiis tribus, tunc canonici, quibus spectat collacio, vel maior pars eorum tenetur eligere } reliquo carente fructu gracie nisi ex tenore papalium litterarum expresse appareat, qnod papa utrique | illorum voluerit providere.
p. 346: extollitur super omne quod dicitur Deus.
p. 347: Miserere anime tue placens Deo.
p. 348: Non mediocriter peccat, quimaiori 25 bono postposito eligit minus bonum.
```
