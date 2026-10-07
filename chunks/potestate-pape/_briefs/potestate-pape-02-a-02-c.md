# Translation brief: potestate-pape 02-a–02-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-02-a.md chunks/potestate-pape/wyc-potestate-pape-02-b.md chunks/potestate-pape/wyc-potestate-pape-02-c.md` once and fix what it reports.
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

## Glossary (the 243 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| metaphisica | metaphysics | *Inter omnes metaphisicas* → "among all the metaphysics": he counts the doctrine of the church as one (T. p. 368). Pilot. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
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
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| globus | band | Derogatory collective (*globus reprobus*, *globos claustralium*). Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of things (*globus temporalium*): "mass", untagged with a note (2026-10-02). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| preconium | commendation | Ruled 2026-10-02 (*Eccl.* 20, 488.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| caracter in actu | character in act | Ruled 2026-10-02 (*Eccl.* 21, 513.18). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | sovereignty | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.27). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 02-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-02-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-02-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "22.2–26.8"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 22.1); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "922 words; 888 unanimous or majority-real; 23 settled by vote (R2 5, R3a 12, R5a 6); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n83–n87 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 2, part 1: [TITLE]

## ¶1 · 22.2–22.7

> [p. 22] has Sed adhuc videtur, cum omnis potestas sit a Deo, quod nemo habet potestatem ad faciendum aliquid, nisi quod Deus intendit ut faciat. Ex quo videtur quod sacerdotes ociantes excusantur, cum non habent potestatem ad faciendam aliquid quod omittunt.

[ENGLISH]

## ¶2 · 22.8–22.11

> [p. 22] Hic videtur mihi quod questio prima illata concedi debeat, nam Deus omnisciens non dat homini aliquid nisi propter finem, quem plenissime et distinccione intendit, quia aliter frustra daret.

[ENGLISH]

## ¶3 · 22.12–22.16

> [p. 22] Item, nemo habet potestatem ad aliquid faciendum, nisi liceat sibi illud facere, cum a Deo non sit potestas nisi legitima, et per consequens Deus obligat eum sub pena peccati vel amissionis premii ut illud faciat, sicut Deus intendit.

[ENGLISH]

## ¶4 · 22.17–22.21

> [p. 22] Item; recipiens talem potestatem a Deo est ut sic obligacior, sed oportet Deum cognoscere excessum obligacionis, et per consequens, quid adequate potentatus debet facere ex illa potestate, et sic Deus intendit ut illud faciat.

[ENGLISH]

## ¶5 · 22.22–23.3

> [p. 22] Sed notandum est, quod sicut aliud est Deum velle quod Petrus sit salvus et aliud Deum velle quod ipse est salvus, sic aliud est Deum intendere, quod Petrus faciat hoc et aliud Deum intendere quod ipse facit hoc; quia eo ipso quo Deus obligat Petrum sub obtentu premii vel incursu pene quod Petrus faciat hoc; Deus intendit quod faciat hoc; et sic utrobique solum intendit et vult veritatem, cum veritas est quod [p. 23] Petrus debet facere hoc; licet non sit verum, quod hoc facit, et per consequens non intentum vel volitum a Deo.

[ENGLISH]

## ¶6 · 23.4–23.11

> [p. 23] Et patet quod non excusatur sed accusatur ocium sacerdotum dicente Apostolo: Hortamur vos ne in vacuum graciam Dei recipiatis. Quicunque enim aliquam potestatem a Deo receperit, per quam liceat sibi opus Dei facere et ex negligencia pretermittit, in vanum graciam Dei recipit. Et in hoc imitamur eos, qui ex omissione instanter operando bonum peccaverunt continue.

[ENGLISH]

## ¶7 · 23.12–23.23

> [p. 23] In hoc tamen est duplex culpa. prima est negligencia potentatus, et secunda maior, crebrior et periculosior est vetacio sathane, qua adversans impedit ne potentatus exerceat potestatem; et hoc contingit per mille meandros tradicionis humane, et specialiter per ficta de iurisdiccione. Quando autem non stat per illum qui immediate habet potestatem sed per alium irracionabiliter restringentem, tunc non sibi sed alii est debitum imputandum; sed hoc raro contingit, cum causa martirii foret hominem se exponere pro distribucione prudenti thesauri Domini.

[ENGLISH]

## ¶8 · 23.24–23.33

> [p. 23] Unde videtur multis, quod Deus non intendit ut potens faciat tale opus; nec habet potestatem ad hoc; sed habet potestatem ut mereatur ex hoc quod nititur ad sic agendum. Alii autem dicunt quod habet potestatem remotam ad sic faciendum, hoc est, potestatem mediate; qua potest sic facere, et tamen Deus non intendit simpliciter quod ita faciet, et sic habet potestatem sic faciendi, sed non ad finem ut sic faciat.

[ENGLISH]

## ¶9 · 24.1–24.29

> [p. 24] Sed dimissa ista dissensione logica, videtur quod omnis potestas secularis diminuetur usque ad non gradum, quia solum durat pro tempore vie, ut docet Apostolus prima Corinth. XV, 24: Deinde, inquit, finis, cum tradiderit regnum Deo et Patri cum evacuaverit omnem principatum et potestatem et virtutem. Ymo videtur, cum Christus Limitat omni sacerdoti suo formam et numerum obiectorum, quod hodie sunt prepositi potestatis minoris quam erant in primitiva ecclesia, et sic usque ad non gradum. Et id considerarent qui stulte et nescie suam magnificant potestatem. Videtur enim quod proporcionabiliter ut plus meritorie nituntur ad edificandum ecclesiam, sic habent amplius potestatis, cum secundum illam mensuram Deus dat potestatem hominibus; quilibet autem clericus vel laicus habet potestatem sufficientem edificandi ecclesiam, si voluerit esse Dei adiutor, faciens quod Deus destinavit eum ad taliter faciendum. Noverunt, inquam, logici quod est in libera potestate hominis facere quod Deus destinavit eum vel ordinavit eum ad fines huiusmodi. Sed aliter loquuntur qui ponunt globum potestatis quam Deus ubilibet potest per se ponere. Secundo principaliter arguitur I de potestate faciendi miracula, de potestate dandi Spiritum Sanctum vel graciam, de potestate ampla absolvendi vel dispensandi alia sacramenta.

[ENGLISH]

## ¶10 · 24.30–26.8

> [p. 24] Quantum ad primum videtur mihi quod miraculum potest dici factum vel faccio quam Deus appropriate facit, et sic solus Deus agit miracula et longe crebrius quam putamus, quia quicunque creat licet solita, quia non miramur ea non [p. 25] vocamus miracula, ut declarat Augustinus super Joh. Omel., et sic quelibet creatura, sicut quilibet actus creandi potest dici miraculum, sic et quelibet faccio que Deo est propria. Unde idem esset creaturam vendicare potestatem miraculose agere, et vendicare quod sit alter Deus; quod Deus non potest creature concedere. Creare autem non potest Deus communicare creature, nec annichilare potest alicui competere, ut dictum est in materia de universalibus. Et patet quomodo debemus iudicare intellectu et fide miracula. Periculosum autem est instante tempore Antichristi magnificare signa sensibilia, cum Antichristi discipuli extollunt se super omne quod dicitur Deus, de principatu, de potestate, et virtute, quas Apostolus dicit evacuandos per Christum, Deus autem ad meritum hominis tam vivi quam mortui sepe facit miracula. Ad quem sensum dicitur corpora mortuorum facere miracula, ymo truncos lapides et multa putrida finguntur facere miracula propter lucrum. Sic autem equivocando in faccione miraculi, videtur quod omne membrum sancte matris ecclesie, de quanto sic meretur ut Deus operetur miraculose, facit miraculum, et pauci mortui qui sunt in statu merendi beati in patria. Illi autem qui dicunt quod lapis, herba et alia natura corporea habet virtutem faciendi miracula, videntur michi nimis confuse loqui, quia sic omnia forent miracula, cum nemo posset facere nisi miraculum quoad Deum. Alii autem dicunt quod oportet [p. 26] esse opus mirabile, et sic sunt illis quibus sunt mira insolita opera nature miracula, aliis autem non forent miracula, et sic de multis ficticiis infundabiliter adinventis. Vel ergo dicamus quod solus Deus habet potestatem faciendi miracula vel equivoce concedamus quod omnis homo promerens aput Deum, ut faciat ad preces suas miracula, facit quodammodo ipsa miracula.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 22.2: No one has power to do anything but what God wills,
- 22.8: This is made an excuse by idle priests.
- 22.22: But we must note the difference between what God wills we should do and his will that we do it,
- 23.4: Idleness of priests condemned by St. Paul.
- 23.12: The fault is double; I. negligence of those who have power.
- 23.18: 2. Hindrances of jurisdiction.
- 24.8: Prelates have less power now than in the primitive Church.
- 24.26: Miracles are works done by God alone and all his works are miracles,
- 25.12: Danger of too much attention to wonders.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 22: *CAPITULUM SECUNDUM.* [HEAD]
  - 22: *illa* [R3]
  - 22: *∅* (in-/tendere is one word, already whole at pos 174 (intendere)) [INS?]
  - 22: *∅* (the inserted i is the folio bar before obligat) [INS?]
  - 23: *volitum* (print has v) [NW]
  - 23: *Hortamur* [R3]
  - 23: *periculosior* [NW]
  - 23: *illum* [R3]
  - 24: *∅* (English side-note word) [R6]
  - 24: *ea* [THIN]
  - 24: *Limitat* (W1: Hmitat -> Limitat (scans: hmitat | hmitat | limitat | hmitat)) [OVERRIDE-SCAR]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 5. II. Cor. VI, 1. (23.33); reference Danger of too (25.12).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 22:
i. A: Capitulum 2*». De potestate. 3. A in marg. : Potestatem habere
ad aliqnid faciendum ; B: Potestatem habere. 2, 3. A : faciendum aliud
nisi. 8. A in marg. : /. 12. A in marg. : 2. 16. Codd. : et sic
Dcits. 17. A in marg. : 3.

p. 23:
10. B: et deest. 11. Rectius: operandi.

p. 24:
2. Codd.: diminuelur dne'1. 21. Codd.: liberlate. 3o. AB in
marg. : Miraculum.

p. 25:
4. A in marg. : nota. 7. A in marg. : Creare. 11. Codd.: in-
lellectum. 21, 22. B: Si autem.
1. Cf. St. Augustini Serm. LXXX De verbis Evangelii Joann. VI.
Cf. et Sermonem CXXVI. 14. II. Thess. II, 4. 16. II. Cor.
III, 7.

p. 26:
i, 2. A: sunt miracula. 7. B: promerent. 9. A in marg : Dare
Sptritum Sanctum. 26. Codd.: Sed quod.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 23: Hortamur vos ne in vacuum graciam Dei recipiatis.
p. 24: finis, cum tradiderit regnum Deo | et Patri } cum evacuaverit omnem principatum et potestatem et virtutem. | non miramur ea y non
p. 25: vocamus miracula, | extollunt se super omne quod | lodicitur Deus, | evacuandos per Chrisium.
p. 26: ut acciperent Spiritum Sanctum. | in omni motu movens et motum sunt simul,
```

---

## Chunk 02-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-02-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-02-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "26.9–32.8"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 22.1); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1304 words; 1229 unanimous or majority-real; 62 settled by vote (DEL 2, R2 31, R3a 12, R5a 17); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n87–n93 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 2, part 2: [TITLE]

## ¶1 · 26.9–32.8

> [p. 26] Quantum ad potestatem dandi Spiritum Sanctum vel graciam, videtur dicendum conformiter quod foret nimis magna presumpcio dicere quod homo peccator dat Spiritum Sanctum, quia Christo super quem specialiter descendit columba appropriatur baptizacio ista, ut patet Joh. primo, Ymo nullus talis habet potestatem servandi sibi Spiritum Sanctum, quomodo igitur ad dandum alteri, cum ignorat utrum pertineat ad columbam? Ymo apostoli, ad quorum ministerium dabatur Spiritus Sanctus, non presumpserunt asserere quod dederunt, sed, ut patet Act. VIII, 15, oraverunt pro illis ut acciperent Spiritum Sanctum. Ideo vel solus Deus habet potestatem dandi Spiritum Sanctum, vel quilibet laycus baptizando vel promerendo habet potestatem dandi Spiritum Sanctum; differenter tamen episcopus, secundum quod autoritative det donum tale, nimis multum excederet vicariam potestatem. Quis igitur concederet, quod habet potestatem super Deum vel eius graciam, et quomodocunque locuti fuerimus, maximum foret quod unus meretur alteri primam graciam, quia, cum in omni motu movens et motum sunt simul, nimis scandalosum foret quod Romanus episcopus tam distanter, tam generaliter et tam improporcionaliter ad [p. 27] Deum, alteraret homines, dando graciam, cum multorum talium spiritus, in quibus subiectaretur talis potestas, sunt miserabiliter damnandi non sufficientes iuvare se ipsos. Et si dicatur quod solum limitatur potestas eorum habilibus, cum solum talibus Deus potest dare graciam, revera habiles haberent a Deo graciam non eo plus vel minus, licet tales non sic menciantur se dare graciam Sicut igitur non habent potestatem faciendi filios Dei, dando graciam predestinacionis, sic nec aliquam graciam, qua Christianus foret gratus Deo. Nec est color si habent potestatem super antecedens, quod habent potestatem super omne consequens vel convertibile, eo quod sic essent potentatus pares Deo, et cum Psalmo LXXXIX, 10 dicitur: Si in potentatibus octoginta anni, et amplius eorum, labor et dolor. Et revera minus videtur errorem sapere quod sanitas corporalis subsit hominis potestati, quam quod gracia vel Spiritus Sanctus subsit, nam cum nichil est in potestate hominis dare, nisi quod subiacet sue potestati, nimis magnum foret christianum habere potestatem dandi Spiritum Sanctum; hoc enim est singulare donum sui principii, cum christianus non potest ipsum vendere. Et conformis est consideracio de absolucione; quondam enim reputabatur Deo proprium tollere peccata tam aput fideles quam aput infideles; unde singulariter dixit Baptista de Christo, ut legitur Joh. I, 29: Ecce agnus Dei, ecce qui tollit peccata mundi. Super quo dicit August. Omel. IV: Nemo sibi arroget et dicat, quod ipse aufert peccata [p. 28] mundi. Iam attendite contra quos superbos intendebat digitum Ioannes. Nondum erant nati heretici et iam ostendebantur, contra illos clamabat a fluvio. Unde sepe imposuerunt Judei Christo blasfemiam ex hoc quod peccata dimisit simpliciter, quia non dimittitur peccatum simpliciter nisi ex hoc, quod offensa in Deum laxatur, sed quis dimittit iniuriam, nisi vel factam sibi vel suo subdito? Deus enim dando homini potestatem huiusmodi, prius dimitteret suam iniuriam antequam vicarius suus dimitteret. Et ista videtur sentencia multorum doctorum, ut XXIII, q. V ex decreto beati Ambrosii sic habetur: Remittuntur, inquit, peccata per Dei filium, cuius levita interpres et quidam excusator est, quia, ut dicitur XV, q. I: Nec is: Levita minister remissionis est. Unde super illo decreto Archidiaconus ita scribit: Prelati quando ligant vel solvunt indignos, mirum est si tunc ligantur vel solvuntur in celis, sed intelligitur de illis, quorum merita ligari vel solvi postulant. Et illud notat XXIV, q. I Ubi sana et Quicunque. Nec dubium de ista sentencia, ne blasfemetur quod prelati nostri prevalent contra Deum; Deus enim non potest quemquam absolvere, nisi prius ipsum habilitet; cum igitur christianus nullum habilitat, nisi forsan orando vel merendo, patet quod oportet Deum habilitare hominem secundum meritum eius. Et de isto debet christianus confidere non autem in pseudochristi blasfemia, [p. 29] qua sompniat et facit ignaros credere de sua insensibili et infundabili potestate; unde non sinit quod scrutinium sue blasphemie in luce clareat, et licet sit tantum errabilis, blasfemat profundius quod Deus est necessitatus complere omnia sua iudicia. Sicut igitur sacerdotes legis veteris non fecerunt hominem sanum vel leprosum sed notificabant, ut patet IV Sentenciarum dist. XVIII et recitatur inferius, sic presbyteri legis nove. In cuius signum Christus suscitavit Lazarum et fecit Apostolos ipsum solvere, ut patet X, XI: et decem leprosi, dum ipsi irent, mundati sunt, ut dicitur Luce XVII, 12, 14 et Psalmus XXXI, 5: Dixi confitebor adversum me, et tu remisisti. Verum tamen amplius habent sacerdotes Christi quam sacerdotes legis veteris, quia plus est iudicare de macula spiritus quam de macula corporali, plus eciam est dignum et humile habere graciam et meritum ex subieccione ecclesie quam corporaliter infirmum esse notificatum in populo esse sanum; et sic licet in multis excellenciis sacerdocium legis veteris superat sacerdocium legis nove, ad sacerdocium tamen Christi non potest attingere, sed generaliter fallit, quando non sequitur arbitrium interni iudicis, ut patet XI, q. Ill Ad hoc vera est. Ista autem blasfema gentilitas, qua sacerdotes debiliores usurpant sibi opus, quod est Deo proprium, maculat matrem ecclesiam, ideo necesse foret eos cognoscere, quomodo quidam tantum a veritate degeneraverant quod negarunt accionem aliquam competere creature (ut patet IX Metaphysice Comment. [p. 30] VII). Alii autem magis blasfeme concesserant quod Deus omnem accionem illis ad extra communicat tamquam eius vicariis, et hii tamquam alter Nabuchodonosor. de quo Dan. IV. et alter Senacherib, de quo II. Paralip. XXXII vendicant se esse socios Trinitatis. Considerarent autem dictum Augustini II De Mirabilibus Scripture Sacre cap. IV quomodo sol et luna steterunt contra Gabaon, non humani imperii auctoritate sed Domini imperantis. Nil, inquit, propter iubentis hominis verbum creature faciunt, sed quod Dominus servi sui oracioni obediens precipit, et cap. XXIV dicit quod lepra Naaman sanata est in sermone imperantis Dei, et non in re aliqua sacramentum virtutis continebatur, et hinc Elizeus accipere munera recusavit. Et sic attribuerent sibi quod servo est proprium, promulgando, operando et promerendo, quod Deus dignatur per illos facere continue, sumendo ut servi humiliter de se ipsis. Ubi autem dubitant de suo opere, debent vere, religiose et secure totam accionem Deo ascribere, cum oportet eum facere omnem accionem creature. Sive utatur igitur in tali accione creatura sua ut organo sive non, sibi laus est operis tribuenda, laudem autem creature de quanto meretur oportet esse aput Deum absconditam, unde magnificantes suam potenciam notarent formam utendi et ascribendi potestatem in sanctis apostolis, et nimis magnum foret, quod nostri illos excederent. set Ipsi autem sepe confitentur, quod non habent potestatem nisi ad edificacionem ecclesie, ut patet [p. 31] II. Corinth. X. et iterum confitentur quod ve illis nisi edificatorie usi fuerint potestate, ut patet I. Corinth. IX, 16: Ve mihi, si non evangelizavero, et tercio confitentur se non audere de se ipsis loqui vel aliis nisi quod Christus in eis loquitur. Nam Rom. XV, 18 ait Apostolus: Non, inquit, audeo aliquid loqui eorum, que per me non effecit Christus. Stulticia igitur foret, episcopum cecum infundabilia et inopinabilia de se ipso presumere. Quantumcunque itaque fuerit magnus Christi episcopus, non potest quemquam absolvere nisi de quanto contritus prius et absolutus fuerit apud Deum; et tunc videtur multis quod de tanto quilibet simplex sacerdos posset absolvere, ymo quasi contritus secure absolvitur, etsi humana absolucio non sequatur, dimittere autem suam iniuriam sicut peccatum in ipsum potest quilibet christianus eque plene ut papa, sicut ponit Matth. VI et XVIII. Quomodo igitur auderet aliquis dicere quod ipse habet singulariter potestatem absolvendi quemcumque peccatorem a pena et a culpa? Revera foret nimis damnabilis, qui ad detrimentum ecclesie tantum incarcerat huiusmodi potestatem. Et conformiter dicitur de potestate excommunicandi vel puniendi subiectos. Nemo enim habet ut membrum Christi potestatem puniendi aliquem, nisi de quanto Deus prius punierit, quod si excedit, punit ut tortor dyaboli. Et hinc dicit Augustinus in De Mirabilibus Scripture cap. XVII quod Isaac benedixit non Esau quem voluit, sed [p. 32] Jacob quem noluit benedicere, ut in benediccione non hominis ostenderet beneficium sed Dei benedicentis. Denique dictum est in Numeris ad Moysen et Aaron sacerdotes: Vos ponite nomen meum super filios Israhel, ego Dominus benedicam vos. Nec voluntas sacerdotis obesse aut prodesse possit ultra meritum benediccionem poscentis. Nec dubium fideli de ista sentencia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 26.9: Man cannot give the Holy Spirit.
- 26.24: A bishop has a spiritual power but he cannot grant the Spirit at his will.
- 27.1: Nor can the pope; indeed many popes have themselves lacked it.
- 27.27: The power of absolution: Only God takes away sin.
- 28.21: God himself cannot give absolution save to one whom he has fitted to receive it.
- 29.6: The priests in the old law did not cure the leper but declared his state; so it is as to absolution in the new law.
- 29.26: How bad priests usurp the office of God,
- 30.17: They should attribute to themselves the office of a servant and ascribe all power to God.
- 30.31: Example set by the apostles.
- 31.10: A simple priest can declare absolution to the contrite as well as the Pope.
- 31.25: So as to excommunication, no man has the power of punishing thus unless God has already punished.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 28: *mundi* [THIN]
  - 28: *intendebat* (hyphenated inten-/debat; main token covers whole word) [R4]
  - 28: *erant* [R3]
  - 28: *levita* (print has v) [NW]
  - 28: *Levita* (print has capital L, v) [R5]
  - 28: *ligantur* [R4]
  - 28: *Deus* [R4]
  - 29: *tu* [R3]
  - 29: *tamen amplius* (one token covers two printed words) [R5]
  - 29: *graciam* [R4]
  - 30: *precipit* [R4]
  - 28: *fluvio* (LEFT-nw: italic, v as printed; stop after not carried) [OVERRIDE-SCARPLATE]
  - 31: *Augustinus* (LEFT-nw: Augu- | stinus split by line break; whole word per main-scan token; 30 is line number) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 5 Num. VI, 27. (32.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 26:
i, 2. A: sunt miracula. 7. B: promerent. 9. A in marg : Dare
Sptritum Sanctum. 26. Codd.: Sed quod.

p. 27:
27. A in marg. : Peccata tollit solus Christus.
32. St. Augustini In Joannis evangel. cap. I, tract. IV, Opp.
tom. III, p. 3 16.

p. 28:
4. A in marg. : Nota bene. 14 Rectius: per Dei verbum. i5. Codd.:
XVI, q. I. Correxi. 21. Codd.: XXIV, q. I versus sua (sic) et quod-
cunque ; B in marg. : Absolutio. 22. A: nec blasphemetur. 24. A in
marg. : absolvere.
12. Decreti secunda pars, causa XXIII, quaest. V, cap. XLIX.
i5. Decreti secunda pars, causa XV, q. I, cap. XI. Archid. 1. c.
21. Decreti secunda pars, causa XXIV, q. I, capp. XXVII et
XXIX.

p. 29:
24, 25. B: qaantam non sequitur.
8. Petr. Lombard. ed. Lugd. p. 41^. 26. Cap. Decretalis
Ad hoc vera est non extat. Sed est Causa XI, q. III Tunc

p. 30:
7, 8. Codd.: III De Mirabilibiis .... cap. 3. Correxi. 12. Codd.:
Cap. 22. Correxi. 14. Codd.: non in aqua. Correxi. 19. Codd.:
continue sumando ut supera.
7. St. Augustini Opp. III, 2, 1000.

p. 31:
2. A in marg. : Potestatem apostnlt quam se dicunt habere. 10. B:
ita fuerit. 20. A: similiter potestatem ; ABinmarg. : Dimittere peccata.
3i. Rectius Quaestiones ex veteri testamento. Quaestio XI
Opp. tom. III, 2, io'3o.

p. 32:
26. B: dicit quod; AB in marg. : Aposioli quando facti sunt sacer
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 26: ut acciperent Spiritum Sanctum. | in omni motu movens et motum sunt simul,
p. 27: Si in potentatibus octoginta anni, et amplius eorum, labor et dolor. | Ecce agnus Dei, ecce qui tollit peccata mundi. | Nemo sibi arroget et dicat, quod ipse aufert peccata
p. 28: mnndi. Iam attendite contra quos superbos iniendebat digitum Ioannes. Nondum erant nati heretici et iam ostendebantur, contra illos clamabat a ftuvio. | peccata per Dei filium, cuius levita interpres et quidam excusator est, | Nec is: 1 | Levita minister remissionis est. | Prelati quando ligant vel solvunt indignos, mirum est si tunc ligantur vel solvuntur in celis, sed intettigitur de illis, quorum merita ligari vel solvi postulant. | Ubi sana
p. 29: et decem leprosi, dum ipsi irent, mundati sunt, | Dixi conjitebor adversum me, et iu remisisti. | 2d non sequitur arbitrium interni iudicis, | Tunc ve a est.
p. 30: non humani imperii auctoritate sed Domini imperantis. Nil, | propter iubentis | hominis verbum creature faciunt, sed quod Dominus servi sui oracioni obediens precipit, | in sermone imperantis Dei, et non in re aliqua sacramentum virtutis continebatur, et hinc Elizeus accipere munera recusavit.
p. 31: Ulis nisi edificatorie usi \ fuerint potestate, | Ve mihi, si non evangelizavero, | audeo aliquid loqni eorum, que per me non ejfecit Christus. | Isaac benedixit non Esau quem voluit, sed 2. | Ex hinc.
p. 32: Jacob quem noluit benedicere, ut in benediccione non hominis ostenderet beneficium sed Dei benedicentis. Denique dictum est in Numeris ad Moysen et Aaron sacerdotes: Vos ponite nomen meum super filios Israhely ego Dominus benedicam vos. Nec, voluntas sacerdotis obesse aut prodesse possit ultra meritum benediccionem poscentis. | Quodcunque ligaveritis super terram erit ligatum et in celis, | hoc facite in meam com~ memoracionem, | Accipite Spiritum Sanctum, quorum remiseritis peccata, remittentur eis, | Aposioli quando facti sunt sacer dotes.
```

---

## Chunk 02-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-02-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-02-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "32.9–36.27"
divisions: "cap. 2 (heading 'CAPITULUM SECUNDUM.' at 22.1); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "948 words; 896 unanimous or majority-real; 36 settled by vote (DEL 1, R2 17, R3a 10, R5a 8); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n93–n97 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 2, part 3: [TITLE]

## ¶1 · 32.9–33.5

> [p. 32] Sed tercio principaliter arguitur de modo committendi potestates nec non de ordine et perdicione potestatum ecclesie; et que potestas sit alia prestancior? Quantum ad primum patet, cum Deus dat omnem potestatem vicariam, qualem solum Deus communicat creature, non refert sive in signo sensibili, sive inspiracione interna Deus potestatem talem communicaverit creature quia oportet omnino quod insensibiliter communicet sive sacramentum sensibile affuerit sive non. Unde vana est concencio, quando et quomodo apostoli facti fuerant sacerdotes, ut Ardmacanus libro II De Questionibus Armenorum recitat septem opiniones in ista materia. Prima dicit quod, quando Christus dixit eis Math. XVIII, 18: Quodcunque ligaveritis super terram erit ligatum et in celis, secunda dicit, quando in cena dixit apostolis de confeccione eukaristie, hoc facite in meam commemoracionem, de quo Luce XXII, 19; tercia opinio dicit quod, quando Christus inflavit in eos dicens: Accipite Spiritum Sanctum, quorum remiseritis peccata, remittentur eis, Joh. XX, 22, 23. Quarta opinio dicit quod die Penthecostes, quando Spiritus Sanctus apparuit eis in linguis [p. 33] igneis Act. II; quinta opinio dicit quod in ascensione, quando dixit: Ite, docete omnes gentes, baptizantes eos Matth, ult.; sexta opinio dicit quod, quando primo misit apostolos ad predicandum Matth. X, 8 dicit: Infirmos curate.

[ENGLISH]

## ¶2 · 33.6–33.14

> [p. 33] Sed doctor reprobat omnes istas sex opiniones per hoc quod, quando fecit eos apostolos dedit eis potestatem sui officii, que est potestas sacerdocii; nec sequitur quod primo, quando precipit eis hec facere. habuerunt huiusmodi potestatem. Nam Joh. IV, legitur quod vivente Baptista apostoli baptizarunt et sic predicarunt et multa sacerdotis officia ante mortem Christi exercuerant, cum Yudas fuit episcopus, ut dicitur Actuum primo.

[ENGLISH]

## ¶3 · 33.15–34.6

> [p. 33] In ista materia videntur mihi tria dicenda: Primo quod sentencia ista doctoris sit satis probabilis, secundo videtur mihi vanum nimis discutere quando apostoli baptizabantur, ordinabantur in sacerdotes vel sacramenta alia ministraverant sive receperant ultraquod est in evangelio expressatum. Scivit enim Christus quod infideles christiani signa querentes ad sacramentalia sensibilia, dimissa re sacramenti, attenderent; ideo de ministerio sacramentorum huiusmodi facit modicam mencionem, sed ut ego credo insensibiliter sine sacramento sensibili, tamquam primus magister ordinavit suos apostolos sacerdotes. Sic enim insensibiliter ordinavit Moysen in veteri testamento; ipse autem fuit sacerdos, licet non Aaronita sensibiliter ordinatus; et ita ignoramus locum; tempus et formam, quibus apostoli ordinati fuerant sacerdotes; debemus tamen credere quod si fuisset plus necessarium ad fidem [p. 34] ecclesie, Spiritus Sanctus in evangelio expressisset. Unde vana curiositas videtur, plus quam evidenter ex scriptura elicitur, tractare huiusmodi questiones, sed ignoranciam nostram confitendo humiliter debemus gracias agere Deo; qui noticiam nostram sic salubriter moderavit.

[ENGLISH]

## ¶4 · 34.7–34.11

> [p. 34] Sed tercio videtur doctorem arguere ex inconveniencia quod oportuit simul et plene fieri sacerdotes. quia aliter (ut inquit) sacramentum sacerdocii foret partibile et non indivisibile ut reliqua sacramenta.

[ENGLISH]

## ¶5 · 34.12–35.16

> [p. 34] Sed hic videtur mihi iuxta dicta de potestate ordinis quod, quotquot sunt genera officiorum presbyteri, tot sunt genera potestatum, ymo respectu cuiuscunque actus quem debet facere ex potestate huiusmodi est dare unam insensibilem; et omnes ille tamquam partes integrales vel aggregata eidem subiecto unam potestatem constituunt. Nec videtur illud insensibile sed signum sensibile quod facit ordinans esse ecclesiasticum sacramentum. Nec est inconveniens sed veritati consonum quod quotlibet parcialia constituunt unum sacramentum, licet sint disparium specierum, nam per se notum videtur fidelibus quod Deus posset dare homini potestatem ad unum et subtrahere potestatem ad aliud. Ex quibus sequitur cum dictis de quiditate potestatis, quod oportet dare particulares potestates secundum numerum obiectorum terminancium, quia diceretur aliter quod preter liberum arbitrium nemo acquireret vel perderet potestatem. Ulterius videtur incertum quantam potestatem oporteret viantem habere, ad hoc quod sit sacerdos, vel si omnes sacerdotes sunt paris [p. 35] potestatis ordinis, quia certum est quod Deus dat vel non dat, ut sibi placuerit, ordinis potestatem. Unde caracterem sacerdotalis ordinis supponimus communiter consequi par officium sacerdotis. In qua materia vellem nostros solempnizantes constituciones humanas ad fidem scripture et puram racionem attendere et non amplius fingere ad onus ecclesie, nisi quod exinde scirent clare deducere, quia potissimum in talibus quod summus sacerdos potest facere, est mereri vel preconizare quod tale sit Dei iudicium, a quo sensu sepe exorbitat; ideo sepe creditur quod absolvit vel excommunicat, et tamen totum contrarium evenit aput Deum, et dum nos viantes sumus ecclesie triumphanti contrarii, necesse est quod sit controversia in universali ecclesia.

[ENGLISH]

## ¶6 · 35.17–36.27

> [p. 35] Quantum ad tercium, scilicet ordinem potestatum, dicitur communiter quod sicut sunt novem ordines angelorum, sic sunt novem ordines potestatum; et hoc elicitur ex Apostolo I. Corinth. XII, 6 ubi declarans unitatem corporis ecclesie ostendit, primo quod divisio graciarum, ministracionum et operacionum procedit ab uno spirituali Domino, qui operatur in omnibus; oportet enim graciam precedere, que sit principium ministrandi in clericis et operandi in laycis. Spiritus autem dat graciam, Dominus recipit ministracionem, Deus exigit ministracionem. Alii, inquit, per Spiritum datur sermo sapiencie, alii vero sermo sciencie secundum eundem Spiritum. Alteri fides in eodem Spiritu, alii gracia sanitatum in uno Spiritu, alii [p. 36] operacio virtutum, alii prophecia, alii discrecio Spirituum, alii genera linguarum, alii interpretacio sermonum. Et hec novem videtur Apostolus consequenter ordine suo in subiectis suis exprimere. Quosdam, inquit, Deus posuit in ecclesia, primo apostolos, secundo prophetas, tercio doctores, demum virtutes, exinde gracias curacionum, opitulacioues, gubernaciones, genera linguarum, interpretaciones sermonum. Que novem videntur aptanda novem prioribus. Apostoli autem sunt primi post Christum, quorum officium est preeminenter secundum sapienciam et missionem capitis ministrare, et eorum officium gerunt episcopi, sicut dicitur papam gerere vicem Christi. Nec oportet contendere circa gradum disposicionis requisite ad esse apostoli, quia certum est quod est latitudo supereminentis disposicionis ad statum apostolicum requisita, qua deficiente non est apostolus sive episcopus; nec requiritur quod Christus viando ipsum elegerit, ut patet de Paulo, Barnaba, Luca, Marco et Matthia; nec obest quod habeat multa officia, cum debeat propinquius sequi Christum assumentem summe ministratorie officium septem ordinum, ut patet libro IV capitulo VIII. Ideo officia cleri debent esse supereminenter in apostolis aggregata, sicut sapiencia excedit alia bona.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 32.9: How the power of orders is conferred.
- 32.13: God grants it by his inspiration, and outward signs are unimportant.
- 33.15: In such matters we may be content with what Scripture tells us.
- 33.23: Christ probably oppointed them without any sensible sacrament.
- 34.7: Fitzralph argues that they must have been made priests at once and completely, or the sacraments would be divisible.
- 34.17: There is no real objection to such division.
- 34.27: We must allow that powers are given according the need of each case,
- 34.32: We do not know what powers are necessary to a priest.
- 35.5: Our legislators should not burden the Church beyond what. Scripture clearly bids.
- 35.12: The Pope often errs in absolving or or excommunicating).
- 35.21: St. Paul tells us that our Lord grants various graces,
- 36.3: which he enumerates,
- 36.10: 1. Apostles.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 32: *∅* (English side-note word (it)) [R4]
  - 32: *18* [R3]
  - 32: *facite* [R3]
  - 32: *∅* (re-/miseritis is one word, already whole at pos 192 (remiseritis)) [INS?]
  - 32: *Quarta* [R4]
  - 33: *Primo* [R3]
  - 33: *probabilis* (hyphenated pro-/babilis; main token covers whole word) [NW]
  - 33: *Aaronita* (30 is the line number) [R4]
  - 34: *hic* [R4]
  - 35: *datur* [R4]
  - 36: *prophecia* [THIN]
  - 36: *primo* [R3]
  - 36: *opitulacioues* (print has open-topped u for n (misprint), zoomed on leaf 97) [NW]
  - 36: *debent* (25 is the line number glued on) [NW]
  - 32: *communicaverit creature quia* (S-split: three words; comma after creature not carried) [OVERRIDE-SCARPLATE]
  - 35: *attendere* (S-split: one word, print = attendere) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 5 Num. VI, 27. (32.33); reference 3. Matth. XXVIII, 19. (33.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 32:
26. B: dicit quod; AB in marg. : Aposioli quando facti sunt sacer

p. 33:
28. AB in marg. : Moises fuit sacerdos, non Aaronita.
De Potestate Pape.

p. 34:
7. B in marg. : de unitate sacerdotalis ordinis. 27. B: ex quiditate.
3o. B: quoniam preter. 33. A: oportet.

p. 35:
17. B in marg. : Novem genera potestatum ; A in marg: Ordines po-
testatem (sic) in sacerdolibus novem sunt. 23, 24. B: spiritu alio do-
minio. 27. B: recepit.
24. I. Gor. XII, 5 Divisiones gratiavum sunt, idem autem
spiritus. 28. Ibidem 8 — 10.

p. 36:
14. AR in marg. : Prima ierarehia; A: primus gradus. lerarchie quo-
modo in ecclesia sunt posite. 22. Godd.: habeant. 28. A in marg.:
5. Ibidem 28. 25. In libro IV (De Civili Dominio II) hic
locus non extat.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 32: Jacob quem noluit benedicere, ut in benediccione non hominis ostenderet beneficium sed Dei benedicentis. Denique dictum est in Numeris ad Moysen et Aaron sacerdotes: Vos ponite nomen meum super filios Israhely ego Dominus benedicam vos. Nec, voluntas sacerdotis obesse aut prodesse possit ultra meritum benediccionem poscentis. | Quodcunque ligaveritis super terram erit ligatum et in celis, | hoc facite in meam com~ memoracionem, | Accipite Spiritum Sanctum, quorum remiseritis peccata, remittentur eis, | Aposioli quando facti sunt sacer dotes.
p. 33: Ite, docete omnes gentes, baptizantes eos | Infirmos curate.
p. 34: sacerdocii joret partwile et non indivisibile ut | rehqua sacramenta.
p. 35: qui operatur in omnibus; | per Spiritum datur sermo sapiencie, alii vero sermo sciencie secundum eundem Spiritum. Alteri fides in eodem Spiritu, alii gracia sanitatum in uno Spiritu, alii
p. 36: operacio virtutum, alii propkecia, alii discrecio Spirituum, alii genera linguarum, alii interpretacio | Deus posuit in ecclesia, prinio | apostolos, secundo prophetas, tercio doctores, demum virtutes, exinde gracias curacionum, opitulacioues, gubemaciones, genera lingttarum, interpretaciones sermonum.
```
