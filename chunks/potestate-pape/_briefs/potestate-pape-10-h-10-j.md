# Translation brief: potestate-pape 10-h–10-j

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-10-h.md chunks/potestate-pape/wyc-potestate-pape-10-i.md chunks/potestate-pape/wyc-potestate-pape-10-j.md` once and fix what it reports.
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

## Glossary (the 279 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
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
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
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
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
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
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio | boast; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 10-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "246.22–250.21"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 8 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "896 words; 842 unanimous or majority-real; 38 settled by vote (R2 25, R3a 11, R5a 2); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n307–n311 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 8: [TITLE]

## ¶1 · 246.22–247.3

> [p. 246] Feci autem ad hoc raciones multiplices ex sufficiencia legis Christi et ex vertibilitate Romani pontificis; ymo patet ex dictis quomodo corpus Christi militaret securius atque perfeccius subducto tali ordine cesareo; nam vivendo omnino exproprietarie, sicut ante dotacionem tempore quo crevit ecclesia, quando pure regulabatur per legem Christi et regebatur per sacerdotes socios sine preeminencia humanitus instituta, melius et perfeccius vixit quam modo. Nec est racio quin per idem hodie viaret sic perfeccius quam nunc viat, igitur cum hoc sit possibile, patet conclusio. Tolle igitur dotacionem et tradiciones humanas, quibus preter scripturam [p. 247] sacram occupatur ecclesia et oriretur ecclesie prior status, qui foret indubie similior et disposicior ad ecclesiam triumphantem.

[ENGLISH]

## ¶2 · 247.4–247.7

> [p. 247] Sed obicitur contra illud tripliciter, primo quod tunc perirent iuramenta et lige tam personarum quam ordinum quibus obediencie pape et Romane curie obligantur.

[ENGLISH]

## ¶3 · 247.8–248.5

> [p. 247] Sed constat quod lige tales forent infidelissime, nisi subintelligantur condicionaliter, de quanto sedes illa et persone compensant in facto imitando Christum similius et tenendo religionem suam perfeccius, ut verbaliter profitentur. Aliter quidem contingeret quod persone et ordines obligate forent tenere cum Antichristo et eius discipulis contra Christum, nam (ut patet ex dictis) est magna disposicio, ut ista comitiva sit realiter Antichristus. Unde ad tantum dicitur hodie perplexa ecclesia, quod fratres necessitantur Parisius iurare Roberto obedienciam tamquam capiti, quod sciunt vel credunt firmiter verum papam; in Anglia autem necessitantur iurare Urbano nostro forma consimili, licet illi sint directe contrarii, ubi oportet quod altera pars infideliter incurrat periurium sive perfidiam. Et cum ex famosis principiis legistarum oportet facere sub pena peccati mortalis quicquid papa mandaverit, oportet credere ut fidem, quicquid in excomunicacione et infidelitate papa decreverit. Et sic de iudicio pape ad propositum. Manifeste sequitur cum paribus quod oportet utramque partem imponere infidelitatem secte Antichristi alteri et relinquere comunicacionem cum reliqua tamquam excomunicata, heretica et omni possessione ac iure indigna; et sic de infinitis inconvenientibus, [p. 248] que ad nimis magnam equivocacionem fidei sequerentur. Ideo tam prelati qui onerarunt homines sic iurare quam illi qui sic sollempnizarunt hanc obedienciam, discuterent et declararent suam sentenciam pro instruccione ecclesie.

[ENGLISH]

## ¶4 · 248.6–249.12

> [p. 248] Sentencia autem catholica quam sepe repecii stat in isto quod nec est credendum nec obediendum pape, episcopo, abbati vel cuicumque spirituali preposito, nisi de quanto dixerit vel mandaverit legem Christi, et per consequens nec Urbano nec Roberto tenetur fidelis credere, nisi de quanto fidem scripture dixerit; nec est de substancia fidei explicite credere alterum eorum esse papam. Benedictus Deus veritatis, qui ordinavit istam dissensionem, ut veritas huius fidei elucescat. Nam ego fidelis philosophus extra utramque istarum parcium sic opinancium, unam istarum parcium hec negantem de reliqua sic arguo; nec credo quod evadet iuxta sua principia: Dicit enim quod subditus tenetur sub pena mortalis obedire papa suo in quibuscumque neutris que ipse mandaverit. Cum igitur iuxta sua principia omnis verus papa habens iurisdicionem super totam ecclesiam precipit vel debet precipere cuilibet membro eius, ut declinet reliquum ut excomunicandum Antichristum, patet quod utraque secta tenetur credere consequenter de reliqua, quod sit a fide Christi scis matica. Dicit enim utraque secta quod omnis subiectus pape sub pena peccati mortalis debet facere omne possibile sibi quod papa suus virtute sacre obediencie sibi mandaverit, et per consequens ipso mandante ut veniat sibi, ut det sibi medietatem [p. 249] sue substancie, et sic de neutris similibus tenetur sub pena mortalis illud perficere; et sic uno precipiente suis quod non veniant ad concilium generale, et alio precipiente suis quod veniant, diu foret antequam esset utrumque concilium congregatum. Unde medium empericum foret ad temptandum religiosos qui sic magnificant suam obedienciam, si loquuntur ex animo, quod papa suus precipiat ista neutra. Et revera ego verecundarer in Oxonia caput erigere, si istam sentenciam de obediencia in scolis publice seminassem.

[ENGLISH]

## ¶5 · 249.13–249.35

> [p. 249] Est igitur tractatus istius articuli cuicumque fideli necessarius et specialiter isti opinioni, cum dicit se esse membrum dyaboli et nisi resipiscat dampnandum, nisi adhereat vero pape; et revera pro querendo minori bono quam est regnum celorum, et profugiendo minori malo quam est dampnacio gehenne, daret operam ad scrutinium veritatis, ymo antequam scandalizaret tantum numerum de exercitu christiano, tum oportet eos dicere, quod maior pars vel quasi medietas christianismi relicta sit per unum Antichristum perdita. Noticiam igitur veri pape discuterent et post noticiam verum papam eligerent ac pro salvacione sui et populi veritatem catholicam publice predicarent; ideo vel sunt segnes infidelibus nequiores vel credunt sentenciam suam de obediencia esse ficticiam. Ego autem credo ex necessitate divina sentenciam quam dixi superius esse fidelibus instancius detegendam, ut si Deus voluerit, fideles moveantur dotacionem destruere, que est radix istius magne versucie vel saltem primatum cesareum minus attendere.

[ENGLISH]

## ¶6 · 249.36–250.6

> [p. 249] Oportet igitur studere, ex quo signo debemus cognoscere verum papam, cum eleccio, opinio [p. 250] aut reprobacio humana sit huic impertinens. Ista enim non auctoritative constituunt vel faciunt verum papam, quia tunc recurreretur ad hoc fundamentum fidei, ut salus exinde consequens habeatur, sed omittendo vel incurrimus notam infidelitatis vel subsannamus istam ficticiam.

[ENGLISH]

## ¶7 · 250.7–250.21

> [p. 250] Secundo replicatur per decretum beati Jeronymi positum XXIV distinccione prima, ubi sic scribitur: Hec est fides, papa beatissime, quam in ecclesia catholica didicimus quamque semper tenuimus, in qua si quid minus perite aut parum caute aliquid positum est, emendari cupimus a te, qui Petri sedem tenes et fidem. Si autem hec nostra confessio apostolatus tui iudicio comprobatur, quicumque me culpare voluerit, ss imperitum aut malivolum vel eciam non catholicum sed hereticum comprobabit. Et sequitur: Sancta Romana ecclesia, que semper immaculata permansit, Domino concedente et beato Petro apostolo opem ferente in futuro manebit sine ulla hereticorum insultacione firmaque et immobilis persistet omni tempore.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 246.22: The Church would be better without such prelates and without endowments.
- 247.4: It is objected that disendowment would destroy the oaths and services by which men are bound to the pope.
- 247.15: Such bonds must be conditional or men would find themselves bound to Antichrist e. g. in swearing to Robert or Urban.
- 248.6: We should obey the pope and prelates only so far as they accord with Christ.
- 248.17: Christ has ordained the Schism to make this clear,
- 249.6: I should be ashamed to shew miself at Oxford, if I had upheld such obedience in the schools.
- 249.18: Half Christendom would be lost eternally.
- 250.10: St. Jerome's reliance on the Roman Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 246: *pontificis* [R3]
  - 247: *lige* [NW]
  - 247: *lige* [NW]
  - 247: *illa* [R3]
  - 247: *legistarum* [NW]
  - 248: *stat* (main "preiates" is the side-note word prelates; the print line opens "stat in isto") [R4]
  - 248: *in* [R3]
  - 248: *isto* [R4]
  - 248: *credo* [R3]
  - 248: *quod* [R3]
  - 248: *matica* (word split by the folio bar (scis | matica, 223b); this is the printed second part) [NW]
  - 249: *publice* [R3]
  - 250: *parum* [R3]
  - 250: *hereticum* [R3]
  - 250: *ulla* [R3]
  - 248: *istarum* (LEFT-odd: print = istarum) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 246:
2. Codd. in marg. : Sine papa potest homo salvari.

p. 247:
4. Codd. in marg. : Obiciiur. 26. B: quicquam papa tnandaverat.

p. 248:
1. An : enervacionem. 18. Codd. : unam-opinantium twice. 19. Codd.
in marg. : Obediencia in neutris. 27. Codd.: excommunicativum.

p. 249:
(none)

p. 250:
7. A in marg. : 20; B in marg. : Replicacio notabilis. 8. A in marg. :
Nota argumentum optimum pro papam esseetpro eius regimine, sed cave
extortam evasionem istius.
9. Decreti Secunda Pars, Causa XXIV, qu. I, cap. XIV.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 246: idem ftiit sacerdos et episcopus,
p. 248: ego fidelis philosophus
p. 250: Hec est fides, papa beatissime, qttam in | ecciesia catliolica didicimns qitamqne semper tenui- | mus, in qua si qitid minus perite aut parum caute aiiquid positum est, emendari cupimus a te, qui Petri sedem tenes et fidem. Si autem hec nostra confessio apostolatus tui iudicio comprobatur, quicumque me cutpare voiuerit, se imperitum aut | malivolum vel eciam non cathoticum sed hereticitm comprobabit. | Sancta Romana ecciesia, que semper immacutata permansit, Domino concedente et beato Petro apostoio opem ferente } in futuro manebit sine ulta hereticorum insuttacione | firmaque et immobilis persistet omni tempore.
```

---

## Chunk 10-i: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-i.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-i
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "250.22–253.27"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 9 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "690 words; 630 unanimous or majority-real; 42 settled by vote (INS 1, R2 26, R3a 10, R5a 5); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n311–n314 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 9: [TITLE]

## ¶1 · 250.22–253.27

> [p. 250] Multe sunt et leges et sanctorum sentencie de preeminencia Romane ecclesie. Sed ad intelligendum ista decreta sanctorum doctorum theologie oportet postponere glossas Johannis de Deo, Johannis Andree, Johannis Monachi et eis similium, qui logice, methaphisice, theologice sanctorum sentencie sunt ignari. Oportet (inquam) notare iuxta dicta quod beatus Jeronymus loquitur de genere predestinatorum fidelium, qui principium sumpserant a Romanis. Paulus enim fuit Romanus ex genere, ut patet Act. XVI et [p. 251] XXII, et Petrus ex occisione. Illam autem predestinatorum generacionem, cuius racio est insensibilis, oportet necessario semper stare fidelem ubicumque migraverit; nec oportet nunc aliquam eius partem Romam vel Avinonam incolere vel esse presbiterum, nisi forte necessitate ex supposicione, quod est nobis ambiguum; et de tali Romana ecclesia intelligit decretum Jeronymi, quia certum est ex VIII. capitulo quod pape plurimi Romani et Avinonici erant manifesti heretici et signantissimi Antichristi. Istam autem generacionem simpliciter et concrete intelligendo non est possibile peccare dampnabiliter, quia cum sit predestinata, necessario salvabitur, et quomodocumque peccaverit, habebit veniam. Sed de tali privilegio non est pompa, cum ignoramus, qui sunt de illa ecclesia. Beatus autem Jeronymus reputative locutus est et credibiliter ex fide quam sumpsit ex apostolicis operibus huius pape, sicut sancti reputative loquuntur, quando vident prelatos declinantes a Christi vestigiis, dicentes quod sunt dampnandi vel membra dyaboli. Utrum autem beatus Jeronymus habuit revelacionem de predestinacione huius pape et iusticia suorum operum, ignoratur. Subtilitas autem huius sensus est valde remota a noticia legistarum. Et patet quomodo intelligenda est condicionalis Jeronymi quod si illa sua confessio confirmatur illius pape iudicio, quicumque impugnare voluerit foret hereticus; reputative enim vel ex revelacione asseruit, quod ille papa non confirmaret aliud nisi verum. Sed dementis foret credere quod hoc debet trahi in consequenciam de quocumque Romano pontifice, quia certum est, quod multi eorum, quantum in eisfuit, ratificarunt multas hereses propter lucrum, [p. 252] ut Gregorius, qui excessit decalogum, vel saltem pseudocardinales, qui sunt hodie cum Roberto, dicuntur dampnasse tamquam valde hereticum quod domini temporales possunt auferre temporalia ab ecclesia delinquente; et tamen Urbanus noster succedens mercede conduxit temporales dominos ad practizandum illam catholicam veritatem; sicut prior ecclesia commendavit et privilegiavit imperatorem ex hoc, quod pseudopapas deposuit et tam temporalia quam insignia pape ab illis abstulit nec non papas quos ipse instituit, approbavit, ut patet XXIII distinccione: In nomine Domini, ubi textus narrat, quomodo papa conqueritur quod crebris tunsionibus symoniace heresis sedes illa sepius est percussa, ideo volendo providere de remedio in futurum decrevit, quod mortuo papa cardinales, religiosi, clerici et layci conveniant ad eligendum unum papam idoneum de illius ecclesie gremio vel alterius, ubi magis fuerit idoneus, salvo semper privilegio imperatoris Henrici, quod in eleccione pape habeat cum suis heredibus interesse. Electus autem tamquam verus papa habebit ante consecracionem suam instar beati Gregorii potestatem disponendi papaliter de bonis ecclesie, et quemcumque qui ordinem eligendi impedierit anathematizat tamquam pessimum antichristum. Glossa autem ordinaria dicit, quod hic tangitur latenter quod legitur in cronicis, quomodo Benedictus qui successit Stephano eiectus est de pontificatu et Johannes Sabinensis episcopus factus est papa pro pecunia; cui impositum est nomen [p. 253] Silvester. Sed iste deiectus est et restitutus Benedictus, qui iterum est eiectus; et datus est papatus Johanni archipresbitero ante portam Latinam, cui impositum est nomen Gregorius; et hic ab Henrico imperatore est deiectus et ultra montes translatus; et hoc totum uno anno factum est. Et propter hoc datum fuit hoc privilegium Henrico. Hec glossa decreti. Considerarent itaque clerici nostri imponentes heresim detegentibus has leges ecclesie, quomodo ipsi ex scandalo sunt econtra heretici. Sicut secta Roberti imponit nobis quod sumus heretici, nos econtra. Si enim iuxta illud decretum Jeronymi ille est hereticus, qui impugnat acrius, quod verus papa fecerit in se ipso, et sic secte iste dicunt altrinsecus se esse hereticos, ita quod ab origine mundi, ut credo, non fuit crebrior imposicio heretice pravitatis. Sicut enim sacerdotes imposuerunt Christo blasfemiam, que est peior pars heresis, sic ignari Antichristi discipuli imponunt heresim tamquam inimicis ecclesie eis qui plus zelant pro eius privilegiis que Christus concesserat conservandis, in tantum quod quidam doctor ignarus quia adeptus est dotacionem pontificis j declamat acucius in locis plus publicis, quod talis est hereticus et hostis ecclesie. Nullus enim peior est apostata, quam qui post altiorem statum ecclesie ad mundum excidit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 250.28: We must note how Jerome speaks of the predestinate.
- 251.1: Their faith sprang from Rome, but is not restricted to Rome or any place.
- 251.15: We know not who are of this true church.
- 251.25: Jerome may have had a revelation as to the Pope to whom he submitted.
- 252.6: Contradictory utterances of various popes.
- 253.12: Mutual charges of heresy.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 251: *Sed* (the box also takes in the side-note "We who") [R3]
  - 251: *illa* [R3]
  - 251: *legistarum* [NW]
  - 251: *illa* [R3]
  - 252: *nomine* [R3]
  - 252: *illa* [R3]
  - 252: *suis* [R4]
  - 252: *tangitur* [R4]
  - 253: *et restitutus* (one main token covers two printed words) [THIN]
  - 253: *iterum* [THIN]
  - 253: *eiectus* [THIN]
  - 253: *Johanni* [THIN]
  - 253: *archipresbitero* [THIN]
  - 253: *Latinam* [R5]
  - 253: *montes* [R4]
  - 253: *translatus* [R4]
  - 253: *uno* [R3]
  - 253: *imponunt* (LEFT-nw: line number 20 glued; print = imponunt) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 250:
7. A in marg. : 20; B in marg. : Replicacio notabilis. 8. A in marg. :
Nota argumentum optimum pro papam esseetpro eius regimine, sed cave
extortam evasionem istius.
9. Decreti Secunda Pars, Causa XXIV, qu. I, cap. XIV.

p. 251:
12. B.: simpliciter conecte. 33. Consequenciam; cod.: conam.

p. 252:
l. Codd. in marg. : Auferre bona temporalia dampnatum est.
12. Codd. in marg. : Simonia sedis Romane. 21. B: habeant.
27. Codd. in marg.: Deposicio paparum.
1. i. e. Gregorius Xf. 12. Decret. Prima pars, Dist. XXIII,
cap. [. Est decretum Nicolai papae de electione Romani pontificis.
27. Glossa ordinaria fed. Ven. i5o,5) I, 97-

p. 253:
1. Glossa ordinaria: Benediclus X. 8, 9. Codci.: impotentes.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 250: Hec est fides, papa beatissime, qttam in | ecciesia catliolica didicimns qitamqne semper tenui- | mus, in qua si qitid minus perite aut parum caute aiiquid positum est, emendari cupimus a te, qui Petri sedem tenes et fidem. Si autem hec nostra confessio apostolatus tui iudicio comprobatur, quicumque me cutpare voiuerit, se imperitum aut | malivolum vel eciam non cathoticum sed hereticitm comprobabit. | Sancta Romana ecciesia, que semper immacutata permansit, Domino concedente et beato Petro apostoio opem ferente } in futuro manebit sine ulta hereticorum insuttacione | firmaque et immobilis persistet omni tempore.
p. 252: In uomine Domini, | crebris tunsionibus symoniace heresis sedcs illa sepius est percussa, | mortuo papa cardinales, religiosi, clerici et layci conveniant ad eligendtim unum papam idoneum de illius ecclesie gremio vel alterius, ubi magis fuerit idoneus, salvo semper privilegio imperatoris | Henrici, quod iu eleccione pape habeat cum suis heredibus interesse. Electus autem tamquam verus papa habebit ante consecracionem suam instar \ beati | Gregorii potestatem disponendi papaliter de bonis ecclesie, et quemcumque qui ordinem eligendi im- | pedierit anathematizat tamquam pessimum antichristum. | quod hic iangilur latenter quod legitur in cronicis, quomodo Benedictus qui successit Stephano eiectus est de pontiftcatu et Johannes Sabinensis episcopus factus | est papa pro pecunia; cui impositum est nomen l.
p. 253: Silvester. Sed iste deiectus est etrestitutns Benedictus, qui iferum est eiectus; et datus est papatus Johauui archipresHtero ante portam Latinam, cui impositum est nomen Gregorius; et hic ab Henrico | imperatore est deiecins et ultra montes translatus; et hoc totum uno anno factum est. Et propter hoc datum fnit hoc privilegium Henrico. | Si patremfamilias Belzebub vocaverunt, quanto magis domesticos eiusP
```

---

## Chunk 10-j: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-j.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-j
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "253.28–257.32"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 10 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "920 words; 843 unanimous or majority-real; 51 settled by vote (DEL 1, R2 29, R3a 16, R5a 5); 26 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n314–n318 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 10: [TITLE]

## ¶1 · 253.28–255.20

> [p. 253] Consolacio autem a Christo est in operando in causa ista fideliter et constanter, cum Matth. X, 25 dicat: Si patremfamilias Belzebub vocaverunt, quanto magis domesticos eius? Ideo ibant apostoli gaudentes quod digni habiti sunt pro nomine Jhesu contumeliam pati. Sed et consolacio quedam mundana exoritur, quodadtantum insane prorumpunt satrape in suis sermonibus, quod imponunt [p. 254] principalem heresim regi suo. Rex, inquiunt, care conduxit stipendiarios contra sanctam ecclesiam; ex quo patenter implicant quod rex eorum sit heresiarcha non obstante ignorancia puerili. Apostolus enim non fuit excusatus a blasfemia, non obstante quod per ignoranciam stulte fecit, ut prima Timothei primo. Videtur itaque nimis magna presumpcio sic imponere heresim toti consilio tanti regni; predicarent enim iuxta suam opinionem atque scienciam de periculosiori heresi adversancium pape suo, et si umquam valet sciencia decretiste, valet ad cerciorandum ecclesiam in hac parte. Dicit enim quod ad illos singulariter pertinet cognoscere disposicionem veri pape et rectitudinem sue consuetudinis cum aliis annexis difficultatibus, sicut ad eos pertinet cognoscere quiditatem heresis et penam sui subditi. Doceant igitur in istis populum de fraude, quia (ut inquiunt) sine fide istius articuli non est salus; ostendant igitur artem suam in isto fideliter, quia maior et famosior est multitudo decretistarum eis contraria in hac parte et specialiter cuneus pseudocardinalium, quibus videbatur regi ecclesie tempore Gregorii excedentis decalogum. Ipsi enim in tradicionibus humanis periti, qui melius noverunt qualitatem eleccionis quam ipsimet celebrarunt, testantur nobis cartis et nunciis, quod eleccio eorum non fuit legitima, et sic (ut inquiunt) noster Urbanus, quem colimus infideliter, non est papa. Nostri autem theologi dicunt primo, quod licet eleccio eorum, ut vere creditur, fuerit maledicta, eleccio tamen passiva Urbani nostri ex eleccione activa Dei est valida, dum tamen fiat ab ipso electo in veris factis papalibus [p. 255] recompensa. Dicunt secundo quod nedum catholice sed melius quam modo conversaretur fidelis ecclesia quocumque papa cesareo subducto, quia Act. IV, 12 dicitur, quod non est aliud nomen sub celo, in quo oportet nos salvos fieri preter nomen domini Jhesu Christi. Et dicunt tercio quod pensando virtutum insignia probabiliter reputant Urbanum nostrum verum papam, cum omnes sancti episcopi erant pape, et Robertum non reputant explicite papam vel membrum sancte ecclesie, quia in De Verbis Domini sermone LIII sic scribitur: Caput humile et membrum superbum absit; non vult esse de corpore capitis Christi, quia amat superbiam. Unde cum secundum eundem Augustinum sermone L Christus vere loquens de quibuscumque pastoribus, cum in se habet omnes pastores bonos vere dicit: Ego sum unus, mecum omnes in unitate unum sunt. Prescitus autem cum sit membrum dyaboli, non compaginatur ordinate huic capiti.

[ENGLISH]

## ¶2 · 255.21–256.2

> [p. 255] Istam autem negativam dico opinando, sicut secta altera possit catholice dicere conformiter de Urbano. Ideo oportet, quod opera iusta dent fidem papatus, cum nichil sit fallacius quam humana eleccio et tradicio phariseica cum suo iudicio. Nam easdem tradiciones habet secta Roberti et nostra, et tamen in iudicio quo maxime servirent ecclesie sunt directe opposite, et indubie neutra pars noscit evidenciam vie sue; theologus autem neutram sectam dampnat, sedinstar libertatis christianorum primeve ecclesie dicit quod utraque pars potest viare satis catholice, et sive uter eorum credat explicite, et quicumque [p. 256] theologus dixerit huius contrarium, a facultate sua degenerat.

[ENGLISH]

## ¶3 · 256.3–257.10

> [p. 256] Tercio replicatur ex dicto Lynconiensis Epistola XXXVI, ubi sic loquitur: Sicut super mundi cardines mundus innititur eorumque fulcimine supportatur, sic super sancte Romane ecclesie cardinales orbis terrarum qui non commovebitur, id est universalis ecclesia que nullis commocionibus a stabilitate fidei deicitur, fixe innititur et ab eisdem forte et firmiter sustinetur. Ipsi enim sunt quos vocat psalmista fundamenta orbis terrarum, ipsi sunt de quibus in Yob scribitur: Sub quo curvantur qui portant orbem; dum enim curas ecclesie oneraque cunctorum tolerant, quasi sibi superimpositum orbem portant. Et sicut in mundo visibili sol iste conspicuus suo preeminenti lumine mundi tenebras purgat singulariterque mundum illustrat motuque suo ordinatissimo ceteros motus corporales naturales ordinat et regulat, sic in orbem ecclesie summus pontifex vicem solis obtinet precellenti luce doctrine et eximiorum operum, mundum purgans ab errorum tenebris, ad veritatis cognicionem singulari prerogativa eundem illuminans, omnes eciam motus accionum in universali ecclesia disposicione sua ordinans, regulans et gubernans. Quemadmodum igitur mundi status, decor et ordo post mundi conditorem angelicosque spiritus ad conditoris nutum administratorios debent subesse soli visibili mundique cardinibus, sic ut veraciter senciunt qui que sursum sunt sapiunt, post mundi conditorem et redemptorem curiamque celestem ex spiritibus beatis angelorum et sanctorum [p. 257] adunatam, status, decor et ordo universalis ecclesie debet subesse suo soli suisque cardinibus, hoc est, summo pontifici sibique assistentibus cardinalibus. Ideoque sancte Romane ecclesie debetur ab universis ecclesie filiis devotissima obediencia, honoratissima reverencia, id est, ferventissimus amor, subiectissi mus timor. Hec et hiis similia ab eis debentur obligacius et forcius, qui pro sublimitate gradus ecclesiastici fastigio ecclesie, id est, summo pontifici et cardinalibus adherent proximius.

[ENGLISH]

## ¶4 · 257.11–257.13

> [p. 257] Talia sunt multa dicta Lyncolniensis et aliorum doctorum, que ex defectu intelligencie inferiores infatuant et superiores faciunt insanire.

[ENGLISH]

## ¶5 · 257.14–257.18

> [p. 257] Unde pro intentu dictorum huius sancti notandum, primo quod describitur in dictis qualis debet esse summus pontifex cum cardinalibus, cum, ut dicit in sermone suo ad papam, ipse gerit in militante ecclesia vicem Christi.

[ENGLISH]

## ¶6 · 257.19–257.21

> [p. 257] Ex quo patet quod oportet verum papam conversari Christo similius et aliter est ex mendacio dolosissimus Antichristus.

[ENGLISH]

## ¶7 · 257.22–257.32

> [p. 257] Secundo notandum quod iste sanctus intelligit predicta re putative vel condicionaliter, et non assertive competere pape secum viventi, quia aliter foret nimis sompniferus contradictorius sibi ipsi. Ipse enim obedienter pape tamquam Antichristo restitit ad tribunal Christi ab eius iudicio appellando et post mortem eundem usque ad mortem quasi cuspide baculi vulneravit, ut dixi VIII capitulo. Et patet quod nichil insanius quam credere quod eo ipso quo quis fungitur vice pape iste condiciones sibi conveniunt.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 254.1: Prelates go so far as to charge the king with heresy.
- 254.28: The cardinals elected Urban and then declared that his election was not lawful.
- 255.6: We think Urban is probably a true pope, and that Robert is not even a member of the Church.
- 255.21: Others may think the Opposite.
- 257.14: Grosseteste's claims for the pope are conditional on his being what he ought to be.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 253: *X* [R5]
  - 253: *Belzebub* [R4]
  - 254: *ex* (print "ex quo patenter"; the main scan lost ex) [INS?]
  - 254: *dicunt* (print "theologi dicunt 30 primo"; the main scan lost dicunt (30 is the line number)) [INS?]
  - 255: *preter* [R3]
  - 255: *eundem* (15 is the line number) [R4]
  - 256: *non* [R3]
  - 256: *fidei* [THIN]
  - 256: *deicitur* [THIN]
  - 256: *fixe* [THIN]
  - 256: *innititur* [THIN]
  - 256: *suo* [R3]
  - 256: *motuque* [R3]
  - 256: *ordinat* [R4]
  - 256: *administratorios* [R4]
  - 256: *redemptorem* [THIN]
  - 256: *celestem* (hyphenated ce-|lestem; main token holds the whole word) [THIN]
  - 256: *spiritibus* [THIN]
  - 257: *adunatam* [THIN]
  - 257: *ferventissimus* [THIN]
  - 257: *amor* [THIN]
  - 257: *subiectissi* (hyphenated subiectissi-|mus; main token subiectissi111 holds the first half plus the m, the rest (us) is at pos 38) [THIN]
  - 257: *mus* (second half of subiectissi-|mus; main split it as ...111 + us) [THIN]
  - 257: *timor* [THIN]
  - 257: *hiis* [R4]
  - 256: *preeminenti* (S-split: one word) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 253:
1. Glossa ordinaria: Benediclus X. 8, 9. Codci.: impotentes.

p. 254:
12. Codd. : circiorandum. 23. Cuneus ; cod.: timens; ib. Codd.
pseudocarnalium (B: carnalia). 25. B: de tradicionibus.

p. 255:
12. A in marg. : Prescitus non esi membrum.
11. Opp. tom. V, i375. 15. Ibid. pag. 671.-

p. 256:
3. Codd. in marg. : Argumentum pro papa. 4, 5. B: sicut supc'r
viundi dccst. 6. Codd. in marg. : Cardinalium laus per Lincolniensem.
28, 29. Recte: debent se so/i.
4. Robertus Grosseste Epistolae ed. Luard p. 12?. 10. Ps.
XVII, 16. 11. Job. IX, 1?.

p. 257:
2. Recte: debet se soli suo. 14. Codd. in marg. : Papa qualis debet
esse. 22. A in marg. : Cave.
De Potestate Pape. 17
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 253: Silvester. Sed iste deiectus est etrestitutns Benedictus, qui iferum est eiectus; et datus est papatus Johauui archipresHtero ante portam Latinam, cui impositum est nomen Gregorius; et hic ab Henrico | imperatore est deiecins et ultra montes translatus; et hoc totum uno anno factum est. Et propter hoc datum fnit hoc privilegium Henrico. | Si patremfamilias Belzebub vocaverunt, quanto magis domesticos eiusP
p. 255: non est aliud nomen | sub celo y in quo oportet nos salvos fieri preter nomen domini Jhesu Christi. | Caput hnmile et membrum superbum absit; non vult esse de corpore capitis Christi, quia amat superbiam. | Ego sum unus, mecum omnes in unitate unum sunt.
p. 256: Sicut super mundi cardines mundus innitiiur eorumque fidci- | mine supportatur, sic super sancte Romane ecclesie cardinales orbis terrarum qui non commovebitur, id est universalis ecclesia que nullis commocionibus a stabilitate fidei deicitur, fixe innititur et ab eisdem forte et firmiter sustinetur. Ipsi enim sunt quos | vocat psalmista fundamenta orbis terrarum, ipsi sunt de quibus in Yob scribitur: Sub quo curvantur qui portant orbem; dum enim curas ecclesie oneraque cunctorum tolerant, quasi sibi superimpositum orbem portant. Et sicut in muudo vtsibili | sol iste conspicuus suo preemincnti lumine mundi tenebras purgat singulariterque mundum illustrat moluque suo ordinatissimo ceteros motus corporales naturales ordinat et regulat, sic in orbeni ecclesie summus pontifex vicem solis obtinet precel- | lenti luce doctrine et eximiorum operum, mundum purgans | ab errorum tenebris, ad veritatis cogni- 22} h cionem singulari prerogativa eundem iUuminans, omnes eciam motns accionum in universali ecctesia disposicione sua ordinans, regutans et gubernans.2? Ouemadmodum igitur mnndi stafus, decor et ordo post mundi conditorem augeJicosque spiritus ad conditoris uutum administratorios } debent subesse soli visibiii mundique cardinibus, sic ut veraciter senciunt qui que sursum sunt sapiunt, post | mundi conditorem et redemptovcm curiamque ce- Jestem ex spiritibtis beatis angelorum et sanctorum 3.
p. 257: adunatant, status, decor et ordo universalis ecclesie debet subesse stio soli suisque cardinibus, hoc est, summo pontifici sibique assistentibus cardinalibus. Ideoque sancte Romane ecclesie debetur ab universis | ecclesie filiis devotissima obediencia, honoratissima reverencia, id est, ferventissimus anwr, subiectissi- 111 us timor. Hec et hiis similia ab eis debentur obligacius et forcius, qui pro subtimitate gradus ecclesiastici fastigio ecclesie, id est, summo pontifici | et cardinalibus adherent proximius.
```
