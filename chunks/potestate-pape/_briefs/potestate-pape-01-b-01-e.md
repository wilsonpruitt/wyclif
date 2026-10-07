# Translation brief: potestate-pape 01-b–01-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-01-b.md chunks/potestate-pape/wyc-potestate-pape-01-c.md chunks/potestate-pape/wyc-potestate-pape-01-d.md chunks/potestate-pape/wyc-potestate-pape-01-e.md` once and fix what it reports.
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

## Glossary (the 250 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
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
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
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
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| famosior | best-known [sense] | Pilot. |
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
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| metaphisica | metaphysics | *Inter omnes metaphisicas* → "among all the metaphysics": he counts the doctrine of the church as one (T. p. 368). Pilot. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| subautenticus | sub-authentic | Beside *autenticus*. Ruled 2026-10-02 (*Eccl.* 15, 345.15). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| calumpnia (ponere / capere) | challenge (to lay a challenge against / to be open to challenge) | The disputant's formal objection to a premiss. Ruled 2026-10-02 (*Eccl.* 16, 363.18, 363.24, 367.11). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
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
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| laxare | loose | Kept apart from *relaxare* "relax". Ruled 2026-10-02 (*Eccl.* 23, 571.29). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
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

## Chunk 01-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-01-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-01-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "5.22–9.10"
divisions: "cap. 1 (unheaded in print); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "783 words; 730 unanimous or majority-real; 37 settled by vote (R2 22, R3a 8, R5a 7); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n66–n70 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 1, part 2: [TITLE]

## ¶1 · 5.22–8.2

> [p. 5] Quamvis autem nesciam fundare efficaciter ex scriptura, quod aliqua sit potestas nisi racionalis potencia, tamen quia videtur Aristotelem et doctores nostros loqui extensius, et nomen est vox sensitiva ad placitum, satis possunt admitti omnes significaciones termini supradicte, nam beatus Johannes intelligit in primo libro prophetico homines bestialiter conversantes. In cuius signum Apocal. IX describit bestias descripcionibus, quales non possunt corporaliter competere animali. Ut patet de locustis, quas dicit habere caudas similes scorpionum, et aculei erant in caudis earum. [p. 6] Et sic intelligitur de potestate equorum, qui post tubacionem sexti angeli exierunt, et conformiter intelligitur capitulo XIII, 4 de potestate, quam draco dedit bestie. Unde propter defectum auctoris non audeo dicere quod Deus habet potestatem producendi quicquam ad intra sed solum ad extra, licet habeat potenciam ad omnia producibilia sui intrinseca producendum, nec personam aut actum in Deo sue dicimus subici potestati. Omnes tamen actus nostri liberi arbitrii, sicut opera extrinseca per hos facta, dicuntur nostre subici potestati, ut patet I. Retractacionum XXXII, III De libero arbitrio et in De spiritu et anima XXVI. Unde non sequitur: si unum convertibilium non sit in potestate nostra, tunc nec reliquum vel e contra; antecedens non est in potestate nostra, igitur nec consequens vel e contra. Et sic argumentando affirmative ex opposito: in potestate, inquit Augustinus, nostra non est, nisi quod nostram sequitur voluntatem. Sequitur enim: Deus predestinavit me igitur habeo virtutem finalis perseverancie et e contra. Sequitur eciam: placet mihi de hoc quod digero alimentum, igitur sic digero; antecedens est in potestate mea et consequens non, quia ex II. Ethicorum propter illa que non sunt in potestate nostra non sumus laudandi moraliter nec culpandi. Supposito igitur, quod fiat restriccio potestatis a racionalem potenciam liberam accidentalem homini, patet quod tales potestates habent subdivisionem [p. 7] multiplicem et terminos magistrales, ut aha est potestas ordinis, alia regiminis vel iurisdiccionis, alia potestas autentica, et alia vicaria vel commissa. Et breviter secundum distinccionem operum est distinccio potestatum. Famosior autem distinccio potestatis pertinens huic proposito est illa quam tangit Hugo II De Sacramentis, parte II capitulo IV, dicens quod sicut duplex est vita hominis; vita terrena corporalis vel naturalis, alia celestis spiritualis vel supernaturalis, sic duplex est potestas. Prima vita corpus vivit ex anima, secunda vero vita anima vivit ex Deo illapso per graciam, et utraque vita suum bonum habet quo vegetatur et nutritur, ut possit subsistere; ut autem in utraque vita iusticia servetur, est dare secundum duos populos, scilicet clerum et laicos, duplicem potestatem, scilicet spiritualem et secularem; et in utraque diversi sunt gradus et ordines potestatum, sub uno tamen capite ecclesie utrimque distributi, et quasi ab uno principio deducti et ad unum relati. Terrena potestas caput habet regem in terris, sicut spiritualis potestas summum pontificem, Sed difficultas scolastica est quomodo iste potestates due describi debeant; et videtur Hugonem innuere quod spiritualis potestas sit potestas clerici ad dirigendum ecclesiam, ut bene vivat vita spirituali. Potestas autem secularis vel terrena sit potestas laici ad dirigendum ecclesiam, ut bene vivat vita naturali. Et habent iste potestates suas leges ac bona sua, de quibus principaliter intromittunt, ut laicus [p. 8] bona nature et fortune, sed clericus bona gracie et virtutis.

[ENGLISH]

## ¶2 · 8.3–8.17

> [p. 8] Iste autem descripciones videntur perplexe, cum clerici nostri videntur habere potestatem secularem concessam eis a regibus. Sicut ad reges pertinet subditos suos in virtute instruere, specialiter cum per se finis vite naturalis sit ut ornetur virtutibus, nec aliter est regnum vel populus, nec aliter vivit legaliter. Cum igitur quicquid potestas potest inferior, potest superior, non e contra, potestas autem spiritualis excedit aliam ut anima corpus, patet secundum doctorem quod potestas spiritualis habet aliam instruere, et quando deviat iudicare; spiritualis, inquit, potestas a solo Deo debet iudicari iuxta illud I. Corinth. II, 15: Spiritualis iudicat omnia, et ipse a nemine iudicatur.

[ENGLISH]

## ¶3 · 8.18–8.28

> [p. 8] Unde spiritualis potestas excedit aliam in antiquitate in dignitate et in utilitate. In antiquitate, quia prius iubente Deo sacerdocium institutum est, ut patet Exod. XXVIII, postea per sacerdocium iubente Deo instituta est regalis potestas, ut patet Deuter. XVIII et I. Regum XII. Ex quo videtur quod ista potestas excedit aliam in dignitate, quia, cum secundum Apostolum Heb. VII: Maior est qui benedicit, et minor qui benedicitur, videtur quod potestas consecrandi et instituendi regem excedit regiam potestatem.

[ENGLISH]

## ¶4 · 8.29–9.5

> [p. 8] Utilitas maioritatis eius ex hoc evidet, quod Potestas spiritualis per se sufficit ad regimen populi, ut patet de Israhele usque ad tempora Saul sine potestate regia salubriter regulato. [p. 9] Potestas! igitur spiritualis cum sit de bonis optimis et per se sufficientibus, excedit potestatem terrenam, cum illa nichil valet sine potestate spirituali principaliter regulante. Sed e contra ista per se sufficit sine illa.

[ENGLISH]

## ¶5 · 9.6–9.10

> [p. 9] In ista utique materia tenendum est pro constanti quod potestas spiritualis quoad dignitatem excedit aliam, ut testatur doctor et quotlibet leges hominum fundate racionibus et scripturis, ut patet capitulo V huius.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 5.22: All these meanings must be allowed since they are in common use.
- 6.29: Even restricting the word to a free rational power exercised by man;
- 7.1: it is of many kinds.
- 7.18: There are powers spiritual and secular of which the heads are respectively pope and king.
- 8.18: The spiritual power is said to be superior 10 the secular in antiquity, dignity and usefulness.
- 8.29: Usefulness: The Jews were governed only by this till the time of Saul.
- 9.6: Dignity: This is self evident.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 6: *illa* [R3]
  - 6: *∅* (English side-note word) [R6]
  - 7: *multiplicem* [THIN]
  - 7: *terminos* [THIN]
  - 7: *magistrales* [THIN]
  - 7: *illa* [R3]
  - 7: *deducti* [R4]
  - 7: *relati* [R4]
  - 8: *antiquitate* (hyphenated antiqui-tate; main token covers whole word) [R4]
  - 8: *in* [R4]
  - 8: *dignitate* [R3]
  - 8: *prius* [R4]
  - 9: *illa* [R3]
  - 9: *illa* [R3]
  - 7: *possit* (LEFT-nw: italic; print = possit) [OVERRIDE-SCARPLATE]
  - 8: *Maior* (LEFT-nw: italic, capital M) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 5:
16. AB in marg. : Potestas pretensa. 28. primo; rectius : in illo — in io-
11— 19. Quae de potestate hoc loco memorantur in Johannis
Hus De Ecclesia fol. 2i7b verbotenus legimus. 32. Apoc. IX, 10.

p. 6:
29. AB in marg.: Potestas multiplex libera.
2. Apoc. IX, 17. 12. Retract. 1. c. sponte homo in Ubero
arbitrio cadere potuit. De lib. arbitrio 1. c. De spiritu et anima 1. c.
19. Aug. Retractationum lib. II, cap. II, III. 26. Aristoteles,
Ethic. Nicom. II, 9 (?) 31. Hussii Opp. 2131'.

p. 7:
9. AB in marg. : Vita hominis duplex, naturalis et spiritualis.
11. AB in marg.: Potestas duplex.
1 — 4. Hussii Opp. 1. c. 7. Hugo de S. Victore, Patrol.
curs. compl. t. 176, p. 418. Loosely quoted.

p. 8:
4. B: videntur deest. 5. B: concessa. 10. B: quidquid inferior
potestas potest. 14. B: et deest. 22. Codd.: Deo deest. Addidi e
textu Hugonis.
12. Quae sequuntur ex Hugone excerpta sunt. 18 — 32. Cf.

p. 9:
6. AB in marg. : Potestas spiritualis est dignior potestate regia.
i — 5. Hussii Opp. 2i3b. 14. De Civili Dominio III, p. 425
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 5: sub nullius redigi potestate, | coniuges non habent sui corporis po~ testatem, | Omnis anima potestatibus sublimioribus subdita sit. | Hec est hora vestra et potestas tenebrarum. | de locustis, | habere caudas similes scorpionum, et actilei erant in caudis earum.
p. 6: de potestate, quam draco dedit bestie. | in potestate, | nostra non est, nisi quod nostram sequitur voluntatem. | propter illa que non sunt in potestate nostra non sumus laudandi moraliter nec culpandi. | sic videt.
p. 7: sicut duplex est vita hominis; vita terrena corporalis vel naturalis, alia celestis spiritualis vel supernaturalis, sic duplex est potestas. Prima vita corpus vivit ex anima, secunda vero vita anima vivit ex Deo illapso per graciam, et utraque vita suum bonum habet quo vegetatur et nutritur, ut possit subsistere; ut autem in utraque vita iusticia servetur, est dare secundum duos populos, scilicet clerum et laicos, duplicem potestatem, scilicet spiritualem et secularem; et in utraque diversi sunt | gradus et ordines potestatum, sub uno tamen cavite | ecclesie utrimque distributi, et quasi ab uno prin- | cipio deducti et ad unum relati. Terrena potestas caput habet regem in terris, sicut spiritualis potestas summuni poiitificem. | autem eos qui credtderint, hec sequenfur: ln nomtne | meo demonia eiicient, Unguis loquentur novis, serpentes tollent, et si mortiferum quid biberint non eis nocebit. | dtvisiones graciarum sunt, | esse GreciSy Lahnis et barbaris debitorem,
p. 8: potestas autem spiritualis excedit aliam ut anima corpus, | potestas a solo Deo debet iudicari iuxta illud I. Corinth. II, 15: Spiritualis iudicat omnia, et ipse a nemine iudicatur. | Unde spiritualis potestas excedit aliam in antiqui- | iaie > * n dignitate et in utilitate. In antiquitate, quia | P r ius iubente Deo sacerdocium institutum est, | per sacerdociitm iubente Deo instituta est regalis potestas, | Maior est qui benedicit, et minor qui benedicitur, | apostoli et evangeliste qui scripserunt libros canonicos erant eorum autores, Iicet solus Deus fuerit autor summus. | Et sicut audistis, | quia Antichristus venit, nunc Autichristi multi facti sunt. | Antichristus quis est secundum scripturam. | Anti valet contra. | De Antichristo. | De Antichrislo.
p. 9: de veritate et auctoritate scripture. | Spiritus Sanctus discipline effugiet fictum, | Est et Non, | sepe fallit et fallitur, | Auctoritas sacre scripture excellit omnes alias scripturas. | dixit et facta sunt | Multi pseudoprophete exierunt in tnundum; | Omnis spiritus qui solverit Jhesum ex Deo non est, et hic est Antichristus de quo audistis quoniam venit, | venient in nomine meo, dicentes quia ego sum Christus, et multos seducent, | Nota contradicit sibi de ecclesia. | Antichristus ex clero.
```

---

## Chunk 01-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-01-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-01-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "9.11–11.32"
divisions: "cap. 1 (unheaded in print); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "560 words; 543 unanimous or majority-real; 13 settled by vote (R2 6, R3a 3, R5a 4); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n70–n72 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 1, part 3: [TITLE]

## ¶1 · 9.11–10.24

> [p. 9] Quantum ad antiquitatem, patet quod sacerdocium gentile vel naturale precessit sacerdocium leviticum. Et correspondenter de potestate dicitur, ut tangitur XXI capitulo V libri. Unde illo modo creditur Adam et Cayn eius progenitum ante peccatum fuisse quodammodo naturaliter sacerdotes. et sic potestas spiritualis benedicendi et consecrandi, videtur dignitate, tempore et utilitate precedere potestatem civiliter coactivam, ymmo potestas sacerdotalis levitica videtur potestatem regiam Israheliticam antiquitate precedere; non autem potestatem regiam gentilem, cum tempore Abrahe legitur novem reges fuisse in valle congregatos. Dignitate autem et utilitate videtur sacerdotalis potestas levitica esse prior. In Deo autem videtur racio potestatis regie increate precedere potestatem sacerdotalem; sicut secunda persona origine precedit terciam. et opus sustentacionis; opus confirmacionis. que correspondent istis officiis, et per consequens sacerdos eternus primos parentes matrimonio copulavit, licet spirituale matrimonium Christi et ecclesie ipsum precesserit. [p. 10] Redeundo igitur ad descripciones potestatum predictas, videtur quod capiunt multas calumpnias; primo quia eidem persone insunt ambe potestates simul; que persona fuit layca in veteri testamento, ut patet de rege Salem Melchisedech Genes. XIV, de Moyse et aliis iudicibus qui non erant sacerdotes levitici, in tantum quod videtur multis ipsos fuisse populares vel laicos. Secundo quia in novo testamento videtur multis quod clerici habeant simul utramque potestatem, cum habent secularem dominacionem; ut fingitur. Et tercio quia reges temporales habent spiritualem ad destruendum vicia et plantandum ac augendum virtutes in se et in aliis, quotquot autem receperunt Christum per fidem, dedit eis potestatem racione filiacionis spiritualis, ad impendendum opera spiritualia misericordie que indubie est potestas spiritualis; quia potestas data divinitus immediate ad vitam spiritualem gignendam et alendam. Nec potest christianus sine hac potestate sanctificare sabbatum; quam potestatem auferre a quolibet Christiano foret contradicere legi Dei; ut patet Exod. XX. Omnis enim potestas qua homo sanctificiat se vel tempus est potestas spiritualis.

[ENGLISH]

## ¶2 · 10.25–11.16

> [p. 10] Et patet impugnacio descripcionis supradicte. Ideo ut descripcio dictarum potestatum sit nocior et ecclesie consentaneor, potest dici quod potestas spiritualis est potestas spiritus per se immediate ordinata, ut creatura racionalis secundum bona gracie dirigatur, et sic individuatur tam a subiecto quam obiecto. Est autem omnis homo spiritus, cum sit duarum naturarum utraque, ut loquitur scriptura Luce IX; 55: Nescitis cuius [p. 11] spiritus estis, et I. Joh. IV, 3: Omnis spiritus, qui solvit Jhesum, ex Deo nou est, spiritus ibi est subtilis hereticus. Et sic sive analogizetur potestas ad Deum et creaturas racionales, sive restringatur ad potestates hominum et angelorum verum est, quod omnis potestas spiritualis est potestas spiritus. Et quamvis homo non det graciam, ministrat tamen sacramenta, ut subditus secundum bona gracie dirigatur. Potestas autem corporalis, quamvis sit gracia bonorum gracie; tamen immediate est; ut creatura Dei ordinetur secundum bona naturalia vel fortune. Et ita videtur omnis homo habere duplicem potestatem, cum omnis homo debet habere potestatem super actus membrorum, et preterea habet potestatem viandi in gracia.

[ENGLISH]

## ¶3 · 11.17–11.32

> [p. 11] Ideo potestas spiritualis capit subdivisionem multiplicem, cum aliqua sit ordinis, et aliqua sit communis. Potestas ordinis vocatur potestas spiritualis quam habet clericus ad ministrandum ecclesie sacramenta, ut spiritualiter prosit sibi et laicis, ut est potestas conficiendi, absolvendi et sacramenta ministrandi. Nam potestas conficiendi ordinatur per se et immediate, ut sacerdos conficiat, sicut habitus virtutis moralis ordinantur propter actus habitibus meliores; et cum sacerdos, ut digne conficiat, dirigitur secundum bona gracie; ideo patet in isto et sibi similibus descripcio supradicta. Potestas autem spiritualis communis, quam habet quilibet christianus, in exercendo opera spiritualia misericordie in se et in aliis; de quibus meminit iste versus:

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 9.11: Antiquity: It is believed that Adam and Cain had a sort of priesthood.
- 9.26: In God however the kingly power has priority.
- 10.1: Objections to accepting Hugo's description. 1. Both powers were united in one person e. g. Melchizedek. 2. A similar union of powers in clerics, 3. and in kings, since it belongs to them to increase virtue.
- 10.25: Spiritual power is a power of the Spirit to direct a rational creature according to the gifts of grace.
- 11.10: Corporal power is the ordering of the creature according to gifts of nature or fortune.
- 11.17: Different kinds of spiritual power; the power given in orders and that which is common to all christians.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 9: *Et* [R3]
  - 10: *insunt* [R5]
  - 11: *nou* (print has open-topped u (misprint), zoomed) [R3]
  - 11: *angelorum* [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Corporai ^ower of the creanlrf (11.10).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 9:
6. AB in marg. : Potestas spiritualis est dignior potestate regia.
i — 5. Hussii Opp. 2i3b. 14. De Civili Dominio III, p. 425

p. 10:
21. B: quam deest. 27. B in marg. : Potestas spiritualis; A in
marg. : Potestas spiriiualis quid est?
14. Joh. I, 12. 27 et seqq. v. Hussii Opp. 2i3a.

p. 11:
10. AB in marg. : Potestas corporalis. 18. A: alia. 18, 19. B-.Jit
communis. 19. A in marg. : Potestas ordinis, 21. Codd.: sacramen-
talia. 29. B in marg. : Potestas communis christianis.
1—32. V. Hussii Opp. 2i3ab
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 9: de veritate et auctoritate scripture. | Spiritus Sanctus discipline effugiet fictum, | Est et Non, | sepe fallit et fallitur, | Auctoritas sacre scripture excellit omnes alias scripturas. | dixit et facta sunt | Multi pseudoprophete exierunt in tnundum; | Omnis spiritus qui solverit Jhesum ex Deo non est, et hic est Antichristus de quo audistis quoniam venit, | venient in nomine meo, dicentes quia ego sum Christus, et multos seducent, | Nota contradicit sibi de ecclesia. | Antichristus ex clero.
p. 10: quotqnot autem recepenmt Christum per fidem, dedit eis potestatem | Nescitis cuius | onus-siium esse leve, | non venit solvere legem 2? sed implere, | in dileccione Dei et proximi lex pendei et prophete. | lerem. Christi sufficientissnna est.
p. 11: Omnis spiritus, qui solvit Jhesum, ex Deo nou est y
```

---

## Chunk 01-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-01-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-01-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "12.1–16.21"
divisions: "cap. 1 (unheaded in print); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "994 words; 978 unanimous or majority-real; 12 settled by vote (R2 8, R3a 1, R5a 2, R6a 1); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n73–n77 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 1, part 4: [TITLE]

## ¶1 · 12.1–14.10

> [p. 12] Docy consul, castiga, solare, remitte, fer. ora, quia (ut dictum est) quotquot receperunt Christum fide formata, dedit eis potestatem sic filios Dei fieri, ut liceat eis dirigere se et fratres suos in via patris sui Christi, eciam corripiendo, sicut patet Matth. XVIII. Unde correspondenter ad potestatem spiritualem potestas secularis est duplex, scilicet civilis et communis. Civilis autoritativa solum domino I civili competit, sed civilis vicaria convenit ballivis vel aliis gerentibus vicem secularium dominorum. Potestas autem communis secularis est qua quilibet potest secundum bona nature et fortune dirigere se et suos. Et ita sicut homo non potest esse sine anima et corpore, nec filius Dei adoptivus sine bonis nature et gracie, sic non stat viatorem esse nisi habeat tam secularem quam spiritualem potestatem communem, quamvis in infantibus et morionibus sit ligata. Spiritualis autem potestas est utrobique perfeccior, sed et sacerdotalis potestas spiritualis superaddit spiritualem communem. Quod autem limitatur potestas clericis super bonis suis temporalibus, seclusa potestate secularium, videtur esse presumpcio et avaricia sacerdotum. Et sic sunt quotlibet divisiones magistrales potestatum, quas curiositas ecclesie adinvenit, ut archidiaconus et electus dicuntur habere potestatem iurisdiccionis, eciam ad absolvendum et excommunicandum, licet non habeant ad hec potestatem ordinis, et talem potestatem in foro contencioso dicitur laycos habere ex commissionibus prelatorum. Contra dicta de multiplicitate potestatis humane arguitur. Videtur enim quod Deus non potest [p. 13] ordinare medium multiplicius pro fine qui eque perfecte fieret per medium brevius, cum omnis talis ordinacio foret frustra; sed omnis finis pro quo ordinaretur potestas tam multiplex eque perfecte si non perfeccius fieret per unicam simplicem potestatem, que est liberum arbitrium, sicud per quotlibet potestates superadditas, igitur superfluit ponere tam multas. Minor probatur ex hoc, quod omnis potestas creata est propter opus perfeccionis universi secundum ecclesiam vel aliam eius partem, sed in omne tale opus sufficit liberum arbitrium sine potestate accidentali, nam in statu innocencie foret solum talis potestas, sicut post statum innocencie illi qui vixerunt religiosius caruerunt huiusmodi potestate, quid (queso) sufficit homo ordinare vel facere, quod non sufficit ex puro libero arbitrio? Videtur enim quod palliata potestas superaddita pocius perturbat ecclesiam. Item, eadem potestas in numero potest nunc laxari et nun restringi, ut patet de potestate ordinis pari in quolibet sacerdote, licet in prelatis suscipiat in laxacione et restriccione gradus multiplices; igitur per idem naturalis potestas potest nunc laxari et nunc restringi quantum oportet pro regimine ecclesie, igitur cum in tali laxacione non acquiritur nova potestas, nec in restriccione deperditur, sequitur quod non oportet superaddere novam huiusmodi potestatem. Minor patet, tum quia potestas non componitur ex suis partibus intensivis, tum eciam quia aliter non foret eadem potestas restricta vel laxata sed omnino vel antiqua perdita vel nova genita. Et illud evidencius movet quod non oportet in sacerdote ponere distinccionem specificam inter [p. 14] potestatem ordinis et iurisdiccionis, sed dans potestatem ordinis dat ut sic potestatem iurisdiccionis, quia aliter foret nuda potestas ordinis nimis superflua, quia insufficiens ut sit in materiam quantumcunque exercita. Christus autem quando dedit discipulis potestatem predicandi dixit Math. ultimo generaliter: Euntes igitur docete omnes gentes, baptizantes eos; quando igitur conceditur principale, conceditur accessorium sine quo ipsum non posset proficere.

[ENGLISH]

## ¶2 · 14.11–14.22

> [p. 14] Item, nulla pura creatura cooperatur cum Deo in producendo quantitatem mentis indivisibilem omnis huiusmodi potestas est qualitas mentis indivisibilis, ergo nulla pura creatura cooperatur cum Deo in producendo huiusmodi potestatem, et per consequens preter potestatem quam Deus creat in anima non est dare aliam datam ab homine. Assumptum patet ex hoc quod nullum materiale agit in immateriale, ut dicit Augustinus XII Sup. Gen. ad litteram: Omnis potentatus est substancia materialis, igitur non imprimit in animam spiritualem huiusmodi potestatem.

[ENGLISH]

## ¶3 · 14.23–14.29

> [p. 14] Similiter, nulla pure creatura cooperatur cum Deo nisi ut eius organum, sed Deus non requirit creaturam ut organum in produccione subdita huius indivisibilis qualitatis pocius quam in produccione gracie, cum hoc superflueret, igitur creatura non comproducit cum Deo huiusmodi qualitatem.

[ENGLISH]

## ¶4 · 14.30–16.21

> [p. 14] Similiter, posito quod dominus papa committat potestatem per bullas m Angliam Petro archiepiscopo ad absolvendum Paulum criminosum in [p. 15] casibus curie reservatis, et pono quod dominus papa ante adventum bullarum in Angliam moriatur, tunc dominus papa nec pro instanti propositi sui conferendi Petro potestatem huiusmodi imprimit in Petro subito huiusmodi potestatem nec pro aliquo posteriori signando. Et idem iudicium de qualibet creatura, que daret alteri potestatem, igitur non est aliqua potestas huiusmodi nisi ficta; non enim potest Christi vicarius ad votum imprimere tam distanter qualitatem in animam, quia tunc foret superfluum auctorizare potestatem huiusmodi per bullas, et continue post foret accio pape impertinens, sicut foret ipso mortuo pro instanti noticie bullarum. Et per idem sequitur, quod non subiacet potestati sue revocare potestatem a Deo datam nec laxare potestatem prius ligatam, sicut non subest potestati sue quod quandocumque pretendit se dare potestatem huiusmodi quod Deus concurrat prebens principaliter potestatem. Et aliter certum est quod non datur potestas talis ab homine; sicut igitur non datur potestas inhabili vel invito, sic nec potentatus dat potestatem alteri si pretendit, aliter enim possent homines in sepotestatum commercia experiri, et generalis volicio qua omnis papa vult quod omnes sacerdotes Christi habiles et solum tales habeant potestatem causaret longe aliter quam reputat ecclesia potestatem. In ista materia videtur mihi quod potestas dicit nunc absolute potenciam ad regulandum, et nunc dicit aggregative potenciam talem cum notificacione aut promulgacione autentica, et cum [p. 16] sensus sint eque noti, patet quod non repugnat non esse potestatem nisi a Deo; et tamen aliud a Deo dare potestatem, hoc est promulgacionem autenticam in facie ecclesie, quod persona creata habeat a Deo huiusmodi potestatem; tale quidem aggregatum secundum partem datur ab homine, sed nonnisiDeus principaliter auctorizet, ut patet inferius. Ad primum conceditur consequencia cum assumpto, sed negatur minor, cum post lapsum necesse est habere potestatem secundum timorem servilem promulgatam ab homine ad cohercendum rebelles sicut non oportuit in statu innocencie nec in regimine pie obediencium, quia lex talis propter transgressores posita est, quam non timebit humilis Christianus. Et conceditur quod potentatus male accipiunt occasionem ad perturbandum ecclesiam ex ficticia potestatis; oportet tamen Deum dare potestates spirituales ad ministrandum sacramenta, ad cohercendum seculariter rebelles ecclesie, preter liberum arbitrium, ut patet ex scriptura multiplici.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 12.6: So secular power may be civil, of the ruler, or common, by which the individual directs his private affairs.
- 12.16: Every man must have common power both spiritual and secular.
- 12.22: Wrongful claims of the clergy as to juridiction.
- 12.33: Objections to the multiplication of human powers.
- 13.20: Power the same in kind may be enlarged or restricted.
- 14.11: All spiritual power is the direct gift of God,
- 14.30: The pope cannot confer authority on others,
- 15.15: or revoke or increase power given by God.
- 15.30: Yet be may have the right of authentic promulgation of what God has ordained.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 12: *Quod* [R4]
  - 12: *∅* (English side-note word) [R6]
  - 14: *producendo* [R4]
  - 15: *concurrat* (20 is the line number) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 12:
7. B in marg. : Potestas secularis. 33. B in marg. : Obieccio.
1. Joh. I, 12. 1 — 20. V. Hussii Opp. 2i3\

p. 13:
10. universi; B-. verwn se. 20. B: eadem deest; B in marg. : 2.
28. B : ne deperditur.

p. 14:
11. B in marg. : 3. 12— 15. AB : quaniitatem — producendo dcest.
In cod. A in marg. alia manu additur. 21. B: inprimerit. 23. B in
marg. : 4. 25. A: subita. 3o. B in marg. : 5.
7. Matth. XXVIII, 19. 20. St. Augustini Opp. tom. III, 1. p.

p. 15:
2—3. AB: ante — papa deest. In cod. A in marg. alia manu additum.
3o. AB in marg. : Potestas ; B: Responsio ad obiectum.
3o— 33. Hussii Opp. 2i3b.

p. 16:
8. AB in marg. : ad i. 22. B in marg. : ad 21*.
1— 7. HussiiOpp.2i3b. 22 — 33.ib. 2131' — 214". 28.Decreti
secunda pars, causa XXIV, qu. I, cap. XXXVH.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 12: Doc.y consul, castiga, solare, remitte, fer. ora, | quotquot receperunt Christum fide formata, dedit eis potestatem sic filios Dei fieri,
p. 14: Euntes igitur docete | omnes gentes y baptizantes eos; | Omnis potentatns est | snbstancia materialis, | Obiectus de auctoritalis maioritate;
p. 15: Auctoritas potestatis vel iurisdiccionis.
p. 16: Miramur: Alhid, | est potestas officii, aliud execucio, et ut plurimum in monachis et aliis retinetur potestas officii, velud in suspensis, quibus ministracio interdicitur, potencia non aufertur.
```

---

## Chunk 01-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-01-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-01-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "16.22–21.31"
divisions: "cap. 1 (unheaded in print); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1117 words; 1052 unanimous or majority-real; 53 settled by vote (INS 1, R2 29, R3a 13, R5a 10); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n77–n82 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 1, part 5: [TITLE]

## ¶1 · 16.22–17.17

> [p. 16] Ad secundum dicitur quod talis potestas non laxatur vel restringitur, augmentatur vel diminuitur quoad suam essenciam, sed quoad execucionem operis quod ab ipsa procederet, quod licet facere, sed non nisi affuerit causa rationalis, quoad Deum. Et illum sensum exponit XXIV canon, quest. prima, Miramur: Aliud, inquit, est potestas officii, aliud execucio, et ut plurimum in monachis et aliis retinetur potestas officii, velud in suspensis, quibus ministracio interdicitur, potencia non aufertur. Et ad conformem sensum conceditur quod naturalis potestas que est [p. 17] liberum arbitrium potest nunc laxari per graciam et nunc restringi, et sic per equivocacionem solvuntur apparentes discordie doctorum, quorum aliqui (ut Anshelmus) dicunt quod non potest perdi, augmentari vel minui liberum arbitrium. Alii autem (ut Augustinus Encheridion) dicunt quod perdi potest liberum arbitrium per peccatum et augeri per graciam. Intelligunt autem sufficienciam propinquam ad operam. quam oportet post primum peccatum dari ex gracia. sicut et ordinis potestatem, preter liberum arbitrium naturale. et sic potestas naturalis augetur vel restringitur per adventum potestatis adventicie et illa consistens in successione, potest instar etatis nunc esse amplior et nunc minor, licet sit indivisibilis quo ad molem. De potestate vero ordinis et iurisdictionis dicetur inferius.

[ENGLISH]

## ¶2 · 17.18–18.9

> [p. 17] Ad tercium dicitur quod assumptum et consequencia illata videntur michi vera; quamvis enim creatura cooperatur cum Deo, faciendo signa sacramentalia et sic quodammodo faciendo, quia facit occasionaliter quod Deus dat graciam, imprimit karacterem. vel producit huiusmodi qualitatem supernaturalem, non tamen producit cumDeo huiusmodi qualitatem, ut dicetur proximo capitulo; sed Deus nunc antecedenter nunc consequenter et nunc concomitanter ad signum sensibile per se facit opus supernaturale, et potestas ordinis est quodammodo causa; quare Deus sic agit, cum statuit se concurrere cum quolibet sacerdote rite ministrante huiusmodi sacramenta. Sicut natura dat animam post disposicionem [p. 18] materie per qualitates elementares et virtutes corporales. quibus non est pars produccionis anime tribuenda sed disposicionis previe, ideo dicuntur coefficere animam quoad animacionem non nude quoad essenciam spiritus, quia tunc crearent; et sic homo non alterat spiritum imprimendo in ipso aliquod absolutum, sed subautentice facit nosci in signo sensibili, quod Deus dat huiusmodi potestatem.

[ENGLISH]

## ¶3 · 18.10–18.29

> [p. 18] Unde inter omnes locuciones blasfemas quibus christianismus illuditur, maximus cathaclismus mendacii est de collacione. subtraccione vel restriccione huiusmodi potestatum. Quando enim Deus et racio cogunt ad utilitatem ecclesie, ut sic fiat per hominem, tunc et aliter non Deus dat huiusmodi potestatem. Ideo in primitiva ecclesia non usi sunt apostoli tali locucione civili, quia tunc foret potestas symoniaca vendibilis et emibilis sicut officium, ideo propter bullas papales non attribuitur potestas subdito plus vel minus, cum Deus dat potestatem habilibus ad edificacionem ecclesie independenter a tali sacramento sensibili introducto, et rectitudo operis est evidencius signum talis potestatis quam littera vel sacramenta prelati; nec ex hoc infertur quod liceret civiliter assumere sibi potestatem ad taliter operandum; quia nemo assumeret potestatem sibi ipsi, sed acciperet ab alio quando Deus necessitat.

[ENGLISH]

## ¶4 · 18.30–20.19

> [p. 18] Unde Symon Magus non presumpsit sibi assumere potestatem apostolicam, quia timeret tunc sibi, ne effectualis efficacia operis sequeretur. [p. 19] ideo voluit emisse potestatem pecunia, ut patet Actuum VIII. Sed nostri prepositi quietati in cortice signorum, solum querentes honorem et lucrum seculi, sunt odibilius Deo symoniaci; et sic conceditur, ut tangitur in confirmacione tercia, quod nimis multe sophisticaciones volant in ista materia, quia omnes que non sunt fundabiles in scriptura, cum ipsa contineat singulas veritates. Potestatem autem secularem regendi civiliter, videtur Apostolum fundare Rom. XIII 1 quando vocat temporales dominos potestates; et dicit, quod non sine causa portant gladium, id est potestatem civiliter coactivam, dicens quod ibidem foret resistere Deo et illis quoad execucionem huiusmodi potestatis, quia (ut inquit) non est potestas nisi a Deo; quod oportet omnino intelligere quod solus Deus dat huiusmodi potestatem, vel quod non datur a racionali creatura, nisi Deus prius ipsam dederit, ita quod hoc signum nisi sumatur pro si non, ad modum loquendi scripture. Et istum sensum dixit Christus Joh. XIX, 10 11 ubi legitur Christo tacente Pilatus dixisse: Nescis quia potestatem habeo crucifigere te et potestatem habeo dimittere te? Cui Jesus: Non haberes potestatem adversum me ullam, nisi tibi datum esset desuper. Super quo Augustinus Omelia CXVI notat, primo quomodo Dominus sepe tacuit et sepe respondit. Tacuit coram Pilato, coram sacerdotibus et Herode propter tria, primo ut impleretur scriptum Isaie LIII, 7: Sicut agnus coram tondente sine voce, sic non aperuit os suum; secundo [p. 20] ut ostendatur eius miticia Math. XII, 19 recitata: Neque aliquis in plateis audiet vocem eius, et tercio ut doceat quomodo verbalis contencio est sepe inutilis; et ideo quando expedit est silendum. Ideo ad tollendum instancias de huiusmodi negativis dicit Augustinus quod generaliter non sicut reus vel dolosus obmutuit, sed sicut agnus, hoc est simplex et innocens, non aperuit os suum. Nunquam enim loquebatur excusando se de suo crimine, sicut nunquam tacuit pro suo reatu; et sic utrobique tam eius silencium quam eius responsio propter latens misterium est notandum; ubi inquit, non respondit sicut ovis silebat, et ubi respondit sicut pastor docebat. Discamus ergo quatuor veritates; quas pastor in responsione sua docuerit, primo docet dicendo, quod non haberet potestatem nisi datum esset sibi desuper, quod per Apostolum suum docuit; quod non est potestas nisi a Deo.

[ENGLISH]

## ¶5 · 20.20–20.24

> [p. 20] Secundo docet quod plus peccat qui potestati innocentem occidendum livore tradit quam potestas ipsa, cum eum timore alterius maioris potestatis occidit; propterea, inquit; qui tradidit me tibi maius peccatum habet.

[ENGLISH]

## ¶6 · 20.25–20.27

> [p. 20] Et patet tercio, quomodo vanum est excusare Pilatum a crimine sed magis est vanum excusare maioritatem peccati in sacerdote.

[ENGLISH]

## ¶7 · 20.28–21.13

> [p. 20] Quarto vero innuitur quomodo quis est sub alterius potestate; et quod potentatus superior non est eo ipso culpandus quo inferior excedit [p. 21] limites potestatis talis: Talem, inquit, Deus Pilato dederat potestatem, ut esset eciam sub cesaris potestate. Unde quidam intelligunt Christum non solum intelligere dacionem potestatis Pilati desuper non solum a Deo sed cesare, quia cesarem plus timuit ut autorem potestatis sue quam occidere regem gentis aliene. Sed timor ille fuit servilis, cum postposita regula potestatis divine, non timuit occidere innocentem; excusacionem autem non habuit, cum excessit potestatem quam habebat a cesare, qui potuit pretendere se dare potestatem adversum Dominum, sed non Deus.

[ENGLISH]

## ¶8 · 21.14–21.31

> [p. 21] Et videtur mihi quinto quod magister docet misterium metaphysice per hoc, quod dicit nisi datum esset tibi desuper, non solum quod cesar non dat nisi Deus prius dederit, verum eciam quod potestas non est quid absolutum, quod posset per se existere, sed potestas dicitur dari ab autore, quando datum est a Deo creature, ut ministro Dei, quod sic aut sic sufficiat facere ad populum in Dei nomine regulandum, et credere quod hoc sit res que posset per se esse foret nimis magna stulticia; et sic per hoc participium neutrum datum convenienter exprimitur res verbi exprimenda per complexum, ut concessum est creature, quod legittime possit in nomine Domini regulare, et illa licencia est potestas, quam Deus nunc dat immediate per se, et nunc per sacramentale ministerium ad notificandum populo Dei licenciam.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 16.22: Power given by God cannot be enlarged or diminished, but the acts orising from it may be controlled.
- 17.2: In what sense Free will may be augmented or diminished.
- 17.18: In the sacraments man's cooperation is but secondary; God gives the grace.
- 18.10: Concerning nothing is there such a flood of lies as about the grant, withdrawal and restriction of spiritual powers.
- 18.23: Righteousness in the chief sign of power.
- 19.10: God alone gives civil power,
- 19.23: as Christ declared to Pilate.
- 20.14: Four lessons from Christ's words.
- 21.12: Power is not a self existent thing, but a grant to a creature to act in God's name.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 16: *illum* [R3]
  - 17: *illa* [R3]
  - 17: *concomitanter* [NW]
  - 19: *1* (old-style arabic 1, x-height like the 2) [R3]
  - 19: *11* (print: Joh. XIX, 10—11, ubi; main has 10 only, the 11 is the inserted token) [INS?]
  - 19: *aperuit os* (one token covers two printed words) [R5]
  - 20: *ubi* [R4]
  - 21: *Talem* [R4]
  - 21: *Deus* [R3]
  - 21: *ut* [R3]
  - 21: *illa* [R3]
  - 21: *nisi* (LEFT-nw: italic; print = nisi) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 16:
8. AB in marg. : ad i. 22. B in marg. : ad 21*.
1— 7. HussiiOpp.2i3b. 22 — 33.ib. 2131' — 214". 28.Decreti
secunda pars, causa XXIV, qu. I, cap. XXXVH.

p. 17:
12. Cod.: stringUur. 18. AB in marg.: ad jm
1—8. Hussii Opp. fol. 2i4a. 4. De Libero Arbitrio 121.
6. Enchiridion ad Laurentium: Libero arbitrio male utens homo
et se pcrdit et ipsuw.
De Pote-tate Pape. 2

p. 18:
10. AB in marg. : Poteaiatem subtraccio { ; B: katafclislijca ;
(kathdclismus). 18. B in marg. : Nota
10 — 14. Cf. Hussii Opp. I. c. 214".

p. 19:
4. B: odibiles. 10. B: secularem deest. n. B in marg. : Funda-
mentwn potestatis civilis. 29. AB in marg.: Christus sepe tacuil
3o. A in marg.: /. 32. A in marg. : 2.
2. Act. VIII, 1 8 — 2 1 . 27. Augustinus in Ev. Joannis cap. XIX,
tract. CXVII.

p. 20:
2 A in marg. : 3. 14. B in marg. : Qualuor verilatcs. 16. B in
marg. : /. 19. B in marg. : 2, 21. Codd.: cum enim; ib. potestatis
deest in codd. Addidi e textu St. Augustini. 24. B in marg. : 3.
3o. AB in marg. : Pilatus habuil potestatem et peccavit.
13. lbid. 19- Rom. XIII, 1. 24. Joh. XIX, 1 1. 30. Au-
gustinus ut suora.

p. 21:
7. AB in marg. : Potesias quomodo dicitur dari.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 16: Miramur: Alhid, | est potestas officii, aliud execucio, et ut plurimum in monachis et aliis retinetur potestas officii, velud in suspensis, quibus ministracio interdicitur, potencia non aufertur.
p. 17: non potest perdi, 5 augmentari vel minui liberum arbitrium. | perdi potest liberum arbitrium per peccatum et augeri per graciam.
p. 18: Poteaiatem (kathdclismus). | Nota {collacio | katafclislijca; restriccio >
p. 19: non sine cansa portant gladium, | ibidem foret resistereDeo et illis | non est potestas nisi a Deo; | si non, | Nescis quia potestatem habeo crucifigere te et potestatem | habeo dimittere te? Cui Jesus: Non haberes potestatem adversum me ullam, nisi tibi datum esset desuper. | Sicut agnus coram tondente sinevoce y sic non aperuitos suum;
p. 20: Neque aliquis in plateis audiet vocem eius, | non sicut reus vel dolosus obmutuit, sed sicut agnus, hoc est simplex et innocens, non aperuit os suum. | non respondit sicut ovis silebat, et ubi | respondit sicut pastor docebat. Discamus ergo | quod non haberet potestatem nisi datum esset sibi desuper, | quod \ non est potestas | nisi a Deo. | plus peccat qui potestati | innocentem occidendum Jivore tradit quam potestas ipsa, cum eum timore alterius maioris potestatis occidit; propterea, | qui tvadidit me tibi maius peccatum habet.
p. 21: Dens Pilato dederat potestatem, ut esset eciam sub cesaris potestate. | msi datum esset tibi desuper,
```
