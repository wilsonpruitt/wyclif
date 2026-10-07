# Translation brief: potestate-pape 04-a–04-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-04-a.md chunks/potestate-pape/wyc-potestate-pape-04-b.md chunks/potestate-pape/wyc-potestate-pape-04-c.md` once and fix what it reports.
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

## Glossary (the 212 rows these chunks use; the full file is GLOSSARY.md)

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
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
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
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
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
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| inobedienciarius | disobedient man | The negative of *obedienciarius*. Ruled 2026-10-02 (146.11). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| preconium | commendation | Ruled 2026-10-02 (*Eccl.* 20, 488.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
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
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 04-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-04-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-04-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "62.10–66.18"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 62.9); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "905 words; 856 unanimous or majority-real; 39 settled by vote (R2 14, R3a 15, R5a 10); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n123–n127 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 4, part 1: [TITLE]

## ¶1 · 62.10–63.8

> [p. 62] Supposito quod beatus Petrus habuit primatum inter apostolos ad regendum, arbitror quod non solum accepit primatum pro se ipso sed pro eius vicariis succedentibus in ecclesia militante. Cum enim Christus non potest ecclesiam suam deserere et oporteat ipsam militantem post Christum exemplari ab ecclesia apostolica, mandatum est quod, sicut Christus fuit capitaneus cetus apostolici et post ipsum Petrus, sic oportet continue esse capitaneum in ecclesia militante. Sed antequam discuciatur utrum oporteat ipsum esse Romanum pontificem necessarium, arbitror precognoscere aliquas sentencias premittendas. Et primo, qualem oportet esse beati Petri archivicarium et per quid constituitur Petri vicarius. Nec debet fideli verti in dubium quin sicut Petrus ex hinc per se fuit Christi vicarius; quod magistrum suum quoad actus et mores secutus fuit similius, sic oportet Petri vicarium similius sequendo Petrum de corpore ecclesie derivari. [p. 63] Vicarius enim in quantum huiusmodi gerit vicem superioris a quo capit vicariam potestatem. Si igitur in principio quod debet regulare sequencia Petrus non fuisset sic Christi vicarius nisi quia secutus fuit eum propinquius, per locum a sufficienti similitudine oportet quod Petri archivicarius de propinquiori sequatur Christum et per consequens Petrum in moribus.

[ENGLISH]

## ¶2 · 63.9–63.26

> [p. 63] Item, illius est homo vicarius cuius vicem gerit et a quo procuratoriam potestatem legitime accepit, sed nemo gerit vicem Christi vel Petri nisi sequatur eum in moribus, cum nulla alia se quela sit pertinens nec aliter recipit a Deo procuratoriam potestatem, igitur ad illud officium vicarium requiritur et morum conformitas et instituentis auctoritas. Cum enim Deus necessario agit omnem accionem creature, patet quod impossibile est habere quemquam talem vicariam potestatem nisi Deus ipsam dederit, sicut dicit Apostolus Rom. XIII, ymo cum illa potestas sit tam excellens dominium supernaturale, videtur quod oportet ipsum singulariter et supernaturaliter dari a Deo. Deus autem non daret provide potestatem huiusmodi illi quem sciret esse proditurum suam ecclesiam, sicut nec dat graciam predestinacionis illi quem scit finaliter periturum.

[ENGLISH]

## ¶3 · 63.27–65.7

> [p. 63] Ex quibus patet quod humana eleccio nichil valet in eligendo talem prepositum; nisi forte de quanto promulgaverit conformiter ad divinum iudicium. Et ista est secunda sentencia supponenda. Item suppono quod electores devient eligendo unum inhabilem propter affeccionem persone, pecunie vel in penam peccati populi, non concordando divine sentencie, tunc cum Deus non approbat nec confirmat quod peccator [p. 64] quem eligunt sit eius vicarius, patet quod eorum activa eleccio non dat electo iusticiam quoad Deum. Sic enim possent electores perverti quod eligunt in Christi vicarium pessimum Antichristum. Et hinc credo quod ritus ecclesie religiose nominant talem electum permissione divina episcopum; non presumunt dicere approbacione vel gracia divina; quod sepius mentiretur. Si dicatur quod eo ipso quis eligitur aput Deum autorizantem eleccionem, quo in eum maior pars consenserit electorum, eo ipso subditi debent sequi eum quomodocumque viaverit, patet quod nichil infidelius, quia non solum membra dyaboli cogerent Deum ad malum; sed fides consequentis subverteret statum ecclesie, ideo absit a fidelibus hoc porisma; tunc enim posset currus Dei ex principiis fidei duci in precipicium, descendendo per latitudinem itineris Antichristi. Ideo debet esse maxima fideli quod precise de tanto debet subditus sequi suum privatum prepositum vel sibi aut sue prepositure legitime consentire, de quanto imitatus est Christum vel docuerit legem suam, aut conversacione et opere ostendit signum vivum sui officii. Patet ex decreto sancti pape Cypriani distinccione VIII Si solus Christus, et docet apostolus primaCor. XI, 1: Estote imitatores mei sicut ego Christi. Ecce quam breviter forma exprimitur imitandi. Et hec racio quare apostoli, ne eclipsarent, sed declararent visionem ad sequendum Christi vestigia, non ediderunt novas leges sed legem quam a Christo acceperant sedule docuerunt; dixerunt se esse vacuos et dyasones quasi nichil, ut patet prima Cor. XIII, 2, [p. 65] et Christum non se vigilancius predicabant, ut patet II. Cor. IV. Nichil enim periculosius in ecclesia quam obumbrare viam sequendi Christi vestigia, ducendo populum ab eius semita, quia error talis secundum imaginacionem Aristotelis primo De Celo et Mundo cresceret in declinacionem maximam Antichristi.

[ENGLISH]

## ¶4 · 65.8–65.27

> [p. 65] Et ex isto quarto colligitur quod, sive electores bene vel male elegerint, operibus bonis debemus credere et quicumque modus perficiendi prepositum fuerit iudicio Christi conformior est eo melior. Nam ex dictis secundo capitulo de potestate eo ipso quo quis copiosius operatur meritorie habet a Deo ad hoc copiosius potestatem. Et hinc dicit Christus Joh. X, 38: Operibus credite, et hinc dicit Crisostomus in De laude Pauli: Si, inquit, magisterii atque primatus adipiscendi gracia ad procuranda tanta negocia apostoli prosiluissent, consequenter essent de ambicione culpabiles. Sequitur: Sicut enim, qui princeps fuerit ordinatus, nisi digne sibi impositum ministret officium, meretur eciam maiora supplicia, sic alter etsi non ordinetur, suscipiat tamen et sicut oportet impleat non dico sacerdocium sed solicitudinem curamque multorum, tunc profecto honore est dignissimus. Iste sanctus non ponderavit elecciones nostras sed recta officia.

[ENGLISH]

## ¶5 · 65.28–65.30

> [p. 65] Sed contra illud arguitur per hoc, quod iuxta istam sentenciam perirent de eleccionibus multe leges et multa legum principia.

[ENGLISH]

## ¶6 · 66.1–66.18

> [p. 66] Sed negetur illud, nisi forte vocentur leges hereses, quibus intricatur ecclesia. Nichil enim est magis hereticum quam pertinaciter defendere quod eo ipso quo electores vel maior pars eorum consenserit viva voce secundum ritus hominum in personam aliquam, eo ipso illa persona legittime est electa; oportet enim subducere subduccionem, quia stat in culpatis electoribus quod electus sit pessimus antichristus et stat illos amore vel odio eligere personam in quam Deus non consenserit, sicut stat ipsos male eligere personam cuius eleccionem passivam Deus approbat. Ideo idem hoc foret credere et electores extollere super Deum; quia ratificare per eos eleccionem quoad personam apud Deum inhabilem, quod Trinitas non potest facere. Ideo illi qui religiosius eligunt subducta revelacione solum probabili reputacione pronuncciant pro electo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 62.10: Peter's primacy was continued to his successors.
- 62.21: What is required of Peter's vicar and what makes him such.
- 63.9: We must follow Peter in his way of life, and must have authority from God.
- 63.27: Human choice avails nothing unless it declares God's will.
- 64.20: Rulers are to be obeyed so far as they set forth the life and will of Christ.
- 65.8: The success of an election is to be judged by the good works of the elected.
- 66.1: Laws would not be set aside except so far as they were heretical.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 62: *CAPITULUM QUARTUM.* [HEAD]
  - 63: *∅* (the inserted i is the folio bar before quela) [INS?]
  - 63: *illa* [R3]
  - 64: *1* (old-style arabic 1, x-height) [R3]
  - 64: *mei* [R4]
  - 65: *ministret* [R4]
  - 65: *non* (zoomed: closed-top n) [R3]
  - 65: *honore* (zoomed: closed-top n) [R4]
  - 66: *defendere* (zoomed: f with crossbar and ascender) [R3]
  - 66: *illa persona* (one token covers two printed words) [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Peter's (62.10).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 62:
9. A in marg.: Capitulwn 4»*- 18. post; B: oportet ease. 22. B:
permittendas. -ib- B in marg. : Qjialis debet esse archivicarins Petri;
A in marg.: Vicarius Petri per quid constituatur.
1. Loosely quoted.

p. 63:
i3. B: fit pertinens.

p. 64:
5, 6. Cod.: Nominat. 6, 7. Codd.: talem episcopnm.
25. Decreti Prima pars, dist. VIII. cap. IX.

p. 65:
4. Codd. : et ducendo. 8. A in marg. : Officii explecio debita os-
tendit prelatum habere potestatem. 17. B in marg. : Nota. 20. A in
marg. : Ministrans sollicite ccclesie est honore dignissimus. 28. A in
16. Opp. (ed. Mignc) tom. I, 83o, 931, cf. ct IX, 2o5.
17. Cf. Chrysostom: in ep. ad. Tit. cap. I, Hom. II et
saepe alias.
De Potestate Pape, 5

p. 66:
19. A in marg. : 2. Eleccionis leges quomodo sunt intelligende. Flec-
cionis inodus in prelatum. 28. Codd.: humilitaverit.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 62: quantum ab alio quolibet Christus diligitur scire poterat, qui cor aiterius videre non poterat, et ideo prudenter non dicit Petrus: Domine, Tu scis, quia amo teptus kiis sed asseruit: Domine, inquit, Tu scis, quia amo te; caritatem itaque et alias virtutes Petrus habuit in via secundum aliquam racionem ceteris apostolis plus perfectas. | Status exproprietarius. Status proprietarius. | Privilegium cleri datum a Christo. | Status exproprietarius alcior.
p. 63: Sint mores sine avaricia, contenti presentibus; ipse enim dixit: Non te deseram neque derelinquam Ita ut confidenter dicamus: Dominus michi adiutor, et non timebo quid faciat michi 20 homo. | Si ali- | quid amplius gloriatus fuero de potestate nostra, quam nobis dedit Dominus iu edificacionem et non in destruccionem. | contemptis presentibns. | Si aliquid — destruccionem | et patet;
p. 64: Si solus Christus, | Estote imitatores mei sicut ego Christi. | Et secuti sumus te, | dimissis aviis.
p. 65: magisterii atque primatus adi-piscendi gracia ad procuranda tanta negocia apostoli prosiluissent, consequenter essent de ambicione | Sicut enim, qui princeps fuerit ordinatus, nisi digne sibi impositum miuistret ofjicinm, meretur eciam maiora suppiicia, sic alter etsi non ordinetur, suscipiat iamen et sicut oportet impteat 11011 dico sacerdocinm sed solicitudinem | curamque multorum, tunc profecto honore est dignissimus. | Et vocabitur nomen eius admirabilis, consiliarius, Deus fortis, princeps pacis. | Domino vere sancto et beatissimo pape Augustino Jeronimus salutem. | Libros beatissimi pape Ambrosii credo hdbere sanctiiatem tuam, eos autem | multum desidero quos adversus nonnullos imperitissimos et superbissimos, qui de Platonis Jibris dominum profecisse contendunt, diligentissime ac copiosissime scripsit. | Domino beatissimo | pape Aurelio; | Papa hoc nomen quid signet. | Quod pape vocabantur Jeronymus, Auguslinus, Ambrosius, Aurelius et alii. Nota Augustinus mirabiliter contra Wy.
p. 66: peccandum esse iit bontim eveniat. | Tue sanctitatis epistolam admonitu me terrificantem suscepi; etenim venerabiiis papa: Si thorus ille legitimus pavidos habet accessusy qno debet puniri supplicio qui divinas temerat raciones? | Ora igitur, venerabilis papa, ut talis de inimicis sepe ulcio procedat, | Greci vocant cunctos presbiteros papas; | Papa specialiter quid significel.
```

---

## Chunk 04-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-04-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-04-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "66.19–69.29"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 62.9); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "699 words; 652 unanimous or majority-real; 37 settled by vote (DEL 1, INS 1, R2 18, R3a 7, R5a 9, R6a 1); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n127–n130 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 4, part 2: [TITLE]

## ¶1 · 66.19–68.7

> [p. 66] Sed secundo replicatur per hoc quod oportet pro salvando cursu et statu ecclesie incidere in tales errores absconditos, ne ecclesia destituatur regimine. Sed iste est communior lapsus in heresim, qua dogmatizatur peccandum esse ut bonum eveniat. Constat quidem ex fide quod pro toto mundo non consentiret fidelis mendacio electorum, sicut nec electores contra veritatem eligerent unum inhabilem quem Deus prius non elegerit et habilitaverit. Et patet quod sentencia electivarum legum debet supponere cetera paria et conformia in preeleccione divina, quia aliter est dicta maxima summe impossibilis et fidelium seductiva. Nec aliquis fidelis ad tantum infatuatur, ut credat Deum ex pacto electoribus assistere et suam eleccionem qualiscumque fuerit confirmare; [p. 67] tunc enim forent electores inpeccabiles, cum in eligendo facilius errare potuerunt. Nec tunc convinci poterit error eleccionis nec esset eius confirmacio ab homine expectanda. Ideo nichil fideli nocius quam quod in eleccionibus huiusmodi contingit errare crebrius; quod regulariter contingit, quando electores eligunt personam quam Deus non approbat vel habilitat ad tale officium. Et hec racio quare apostoli elegerunt Mathiam per sortem, ut patet Actuum Ubi sunt notanda misteria, primo quomodo beatus Petrus ex illo Psalmo CVIII; 8 episcopatum eius accipiat alter concludit quod oportet ex hiis viris, qui viderunt conversacionem apostolorum cum Christo; unum institui loco Jude et. quia nondum habuerunt revelacionem de persona; constituerunt duos plus habiles scilicet Barsabam et Mathiam, relinquentes divino iudicio quem illorum voluerit per sortem ostendere electum penes eum; cuius arbitrio oportet in eleccionibus dare fidem. Unde triginta electores sequentes dixerunt verba notabilia sepe dicte sentencie expressiva. Tu Domine, inquiunt, qui nosti corda hominum, ostende quem elegeris ex hiis duobus unum accipere locum ministerii huius, ubi patet quod oportet Deum eligere et secundum alios ritus eligentes valde ecquivoce eleccionem Dei fideliter promulgare ideo dicit, ostende quem elegeris non ad dignitatem sed ministerium. Sed tercio obicitur, cum eleccio nostra debet exemplari et autorizari ab apostolis; a quibus trahimus ritus alios, videtur quod debemus in nostris eleccionibus sequi illos; nam magis autenticam [p. 68] formam eligendi non possumus cogitare; et obiectus eque moverent contra apostolos. Et iterum videtur quod non plus in isto quam in illis que sonant commodum et honorem licet a ritu apostolorum recedere, quia sic pertinenter imponeretur nobis quod deserentes fidem scripture exequimur infideliter ritus gentilium.

[ENGLISH]

## ¶2 · 68.8–68.34

> [p. 68] Quantum ad istam materiam diffuse tractat eam dominus Ardmacanus libro VII De questionibus Armenorum, recitans quatuor vias constituendi pontifices: una via est per sortem, secunda via per episcopi institucionem, tercia via per hereditariam successionem et quarta via per eleccionem: quod variatur secundum diversitatem variam electorum. Nec movet triplex obiectus istius materie. Primo quod sic temptaretur Deus, si non habentibus ad hec revelacionem liceret sortes mittere, quia ista argumenta procederent contra factum apostolorum et contra sortem veteris testamenti. Nec est Dei temptacio, ubi devotus Dei orator ignorat quid sit Dei voluntati conformius; qualis ignorancia communiter est in electoribus. Secundus obiectus est quod apostoli elegerunt duos scilicet Barsabam et Mathiam, ideo nos debemus operari conformiter. Quantum ad illud non contendo si ordinare multitudinem ut Deus de illa digniorem eligat vocetur eleccio, sed scriptura sic loquitur: Statuerunt duos etc. Sed rogo sic arguentem ut consenciat quod utrobique fiat conformiter nisi subsit racio diversitatis; statuant igitur de humilioribus, quantum adest illis certitudo, et de incerto residuo mittant sortem.

[ENGLISH]

## ¶3 · 69.1–69.11

> [p. 69] Et per hoc patet racio ad tercium obiectum, quo arguitur sorte sepe contingeret ineptum eligi; non nominentur, inquam, primo aliqui nisi apti et tunc indubie sors communius indicabit apciorem quem Deus elegerit quam faciunt elecciones hodie celebrate, et preter hoc tradiciones humane de eleccionibus, occupaciones superflue ad illos regulandum et conspiraciones, contenciones nec non deviaciones a divino arbitrio delete multum exonerarent et prosperarent ecclesiam.

[ENGLISH]

## ¶4 · 69.12–69.29

> [p. 69] Secunda via est probabilis subducto errore instituentis, cum Petrus sic instituit Marcum et Clementem Antiochie et Rome, Paulus autem Thimoteum et Tytum. Ceteri vero apostoli ordinarunt episcopos super populos quos evangelizando converterunt, modo autem superadduntur sicut in ordinibus clericorum, de eleccionibus, de presentacionibus, de institucionibus; de induccionibus et confirmacionibus, que pharisei tantum ponderant ut sacramenta ecclesie; et certum est quod totum est tradicio gentilis superflua nisi forte sit medium ducens ad exequendum divinum arbitrium, sic quod rite exequens opus talis officii sine tali cerimonia introducta, sicut dicit Crisostomus, est tam autentice a Deo electus, sicut aliquis cum quotlibet tradicionibus phariseicis quantumlibet sollempniter celebratis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 66.19: It is argued that without elections order would fail in the Church.
- 66.26: This is doing evil that good may come.
- 66.32: (;od has not engaged to confirm any election made.
- 67.4: Electors often err.
- 67.10: The apostles elected Matthias by lot.
- 68.8: Four ways of choice: 1. Lot. 2. Bishop's appointment. 3. Hereditary succession; 4. Election as as now practised.
- 68.24: It may be well to select to the best of our judgement and then cast lots, as did the apostles.
- 69.1: This would prevent the objection that the lot might fall on one quite unfit.
- 69.12: Appointment by bishops might be good, but is now ruined by all kinds of traditions.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 66: *ut* [R3]
  - 66: *bonum* [R4]
  - 67: *duobus* [NW]
  - 67: *unum* (25 is the line number) [R3]
  - 68: *dominus* [R3]
  - 68: *pontifices* [R4]
  - 68: *∅* (English side-note word) [R6]
  - 68: *Quantum* [R3]
  - 68: *illa* [R3]
  - 69: *Petrus* [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 66:
19. A in marg. : 2. Eleccionis leges quomodo sunt intelligende. Flec-
cionis inodus in prelatum. 28. Codd.: humilitaverit.

p. 67:
6, 7. B: irregulariter. 8. Codd. : humilitat. 12. Peirus. Codd.:P.
17. Codd.: humiles. 2?, 24. Recte : corcta omnium. 3o. A in

p. 68:
8. A in marg. : Eleccio pontijicis quatuor modis; B: Quatuor vie eli-
gendi pontifices. 16. Ainmarg.: /. 24. Airtmarg. : 2. 25,26. A:
uos debemus nos.

p. 69:
i. A in marg.: 3. 12. A in marg. : Secunda via. 17. super-
adduniur; deest verbum.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 66: peccandum esse iit bontim eveniat. | Tue sanctitatis epistolam admonitu me terrificantem suscepi; etenim venerabiiis papa: Si thorus ille legitimus pavidos habet accessusy qno debet puniri supplicio qui divinas temerat raciones? | Ora igitur, venerabilis papa, ut talis de inimicis sepe ulcio procedat, | Greci vocant cunctos presbiteros papas; | Papa specialiter quid significel.
p. 67: episcopatum eius accipiat alter | Tu Domine. | qui nosti corda hominum, ostende qnem elegeris ex hiis dnobus ihunum accipere locuni ministerii huius, | ostende quem elegeris | Detis autem rex noster ante secula | operatns est sahitem in medio terre. | Oui non providet | snis et maxime domesticis fidem negat et est infideli deterior,
p. 68: Statuerunt dnos | ut non sohim imperio Magni Canis de Cathay, sed modo insuper imperio Persarum, imperio Usbeckj imperio Soldani et imperio barbarorum sit minor | videtur quod | papatus et pontificatus Romanus non sic | Canis = (Khanj. | Catnay. {Cathay =
p. 69: Predicaverunt episcopi Romani ante dotacionem. | Dotacio imperatoris deduxit et multiplex malum. | finem XV; | VIII, g; XV =
```

---

## Chunk 04-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-04-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-04-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "69.30–72.15"
divisions: "cap. 4 (heading 'CAPITULUM QUARTUM.' at 62.9); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "537 words; 443 unanimous or majority-real; 76 settled by vote (DEL 1, R2 53, R3a 17, R5a 4, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n130–n133 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 4, part 3: [TITLE]

## ¶1 · 69.30–71.27

> [p. 69] Et quantum ad omnes leges que videntur sonare contrarium, omnes intelliguntur de legibus humanis in quantum conferunt ut ordinetur conformiter ad divinum iudicium et de inobedientibus ecclesie triumphanti; ideo ne sit contencio de [p. 70] istis, ordinavit Spiritus Sanctus quod teneremus nos in limitibus legis sue. Unde istam materiam de eleccionibus tangit beatus Crisostomus super I. Thim. V: Dignitas, inquit, magisterii et sacerdocii magna est et mirabilis et vere sentencia Dei indigens ut eum qui dignus est in medium deducat. Nec audivi alios tam insanos, quod dissentirent isti sentencie. Unde quantum ad eleccionem sic loquitur iste sanctus: Ita antiquitus fiebat, ita et modo fit, cum sine passione humana elecciones facimus, cum ad nil vite huius respicimus, non ad amiciciam, non ad odium; et si in discrecione non tanto spiritu participamus, sufficit voluntas bona in Deo ponere intronizacionem, quia neque apostoli spiritu participabant, cum Mathiam elegerant, sed oracioni rem committentes in cathalogo apostolorum Mathiam annumeraverunt neque ad dileccionem humanam aspiciebant. Et ita in omni eleccione fieri oporteret, ubi electores sunt ambigui quis est habilior apud Deum. Videtur michi quod debent instar apostolorum sortes mittere; devote committendo sibi iudicium, sicut dicit iste sanctus, quia nemo diffiniret contra divinam sentenciam nec in materia ambigua, in qua non habuerit racionem naturalem, testimonium scripture vel revelacionem. Nec est factum apostolorum, a Deo tam crebro in lege veteri exemplatum; magis cerimoniale vel reprobandum, quam leges gentiles in ecclesia minori auctoritate vel evidencia introducte. Ideo secundum [p. 71] Crysostomum cum ista via sit secura et magis utilis propter multa et illam despicimus, qualiter Deus abscondita revelabit? Est enim intencio huius sancti quod apostoli in eligendo episcopos habuerunt revelacionem vel propheciam. Que, inquit, opera secundum nil humanum fiebant, a prophecia et spiritu sancto fiebant. Prophecia enim non est solum dicere futura sed presencia, cum Saul secundum propheciam monstratus est in vasis occultatus; Deus enim iustis revelat et prophecia fuit hec dicere: Separate, inquit, michi Paulum et Barnabam; ita et Thimoteus electus est a Paulo, qui multas prophecias habuit, ut quando circumcidit Thimoteum et intronizavit. Et ideo dicit, quod Deus eum elegit, non humanum iudicium, quod intronizatus recoleret custodiendo Dei depositum. Quando igitur electores spiritu ducuntur, alieni a vento calliditatis humane, tunc est simplex institucio vel multorum eleccio legitima; et aliter est infecta. Ideo debent electores postposito omni humano iudicio committere se divino regimini, sicut geromantici in punctuando suspendunt fantasiam propriam et committunt impulsum ad motum influencie celestis corporis. Et patet quod quilibet istorum trium modorum eligendi est laudibilis, quando fit conformiter ad eleccionem divinam.

[ENGLISH]

## ¶2 · 71.28–72.7

> [p. 71] Patet insuper quod eleccio adinventa humanitus est artificiosior sed callidior et postquam avari plus sunt terrenis dediti quam merito et labori officii est periculosior. Eleccio vero per sortem est securior, magis autentica et per consequens [p. 72] nunc eligibilior. Sed cupiditas et fastus obviant; dicitur enim quod nostri electores discernunt melius sicut apostoli; nec tales blasfemias credo cessare antequam status prelatorum sint tantum extenuati a commodo temporali quod officium capiatur propter meritum et non honorem vel commodum temporale.

[ENGLISH]

## ¶3 · 72.8–72.15

> [p. 72] Quantum ad quartum modum instituendi summum sacerdotem iure hereditario patet quod hoc fuit ex ordinacione Dei olim autenticum, quia Exod. XXVIII et XXIX docetur quomodo filii Aaron forent sacerdotes iure perpetuo, et idem patetNumeri XXV de Finees, filio Eleazari, filii Aaron cum genere suo; quod fungeretur sacerdocio iure perpetuo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 70.4: Chrysostom is in favour of lot where choice is doubtful.
- 71.5: The apostles had divine guidance in their choice.
- 72.8: Hereditary succession was allowed in the old law.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 70: *ut* [R3]
  - 70: *fiebat* [R4]
  - 70: *fit* [R3]
  - 71: *et* [THIN]
  - 71: *Deus* [R3]
  - 71: *Que* [R3]
  - 71: *nil* [R3]
  - 71: *fiebant* [R4]
  - 71: *∅* (print has nothing between a and prophecia; main already has prophecia et spiritu sancto fiebant at 40–44) [GAP]
  - 71: *enim* [R4]
  - 71: *cum* [R4]
  - 71: *Saul* [R3]
  - 71: *Deus* [R3]
  - 71: *et* [R3]
  - 71: *Thimoteus* [THIN]
  - 71: *electus* [THIN]
  - 71: *non* [R3]
  - 72: *iure* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 69:
i. A in marg.: 3. 12. A in marg. : Secunda via. 17. super-
adduniur; deest verbum.

p. 70:
7. B in marg. : Nota. n. Codd.: respicienles. i5. B: participant.
17. Codd.: cum Mathiam. 19. Codd.: fieri oporteret deest. Addidi c
textu Chrysostomi.
4. In Epist. I ad Timoth. cap. I, Hom. V (Migne), tom. XI,

p. 71:
[o. Codd.: in istis revelat. 20. B in marg. : Nota.
1. Chrysostomus: Ad nos in extremant ignaviam delapsi,
eciam manifesta abiicimus: si vero manifesta pretermittimus,
quomodo nobis Deus obscura et incerta revelabit?

p. 72:
8. Ainmarg. : Summi pontificis institucio iure hereditario. 16. B in
marg.: Tempore legis gracie sacerdocium non currit iure hereditario
triplici causa.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 69: Predicaverunt episcopi Romani ante dotacionem. | Dotacio imperatoris deduxit et multiplex malum. | finem XV; | VIII, g; XV =
p. 70: magisterii et sacer- | docii magna cst et mirabiiis et vere sentencia Dei ? | indigens itt eum qui diguus est in medium deducat. | Ita antiquitus Jiebat, ita et modo Jit, ciim sine passione humaua elecciones | fucimus, cum ad nil vite huius \ respicimus, non | ad amiciciam, non ad odium; et si in discrecione non tanto spiritu participamus, sufficit voluntas boua in Deo ponere intronizacionem, quia neque apostoli spiritu participabant, cum Mathiam ele- | gerant, sed oracioni rem committentes in cathalogo apostolorum Mathiam annumeraverunt neque ad dileccionem humanam aspiciebant. Et ita in omni eieccione Jieri oporteret, ubi electores sunt ambigui quis est habitior apud Deum. | Ouo inre | Qnid dimistrit pape sanctus apostolus? quod habeo, inquit, hoc tibi do; quid illud? certe non est aurum neque argentum,ib cum ipse dicat: Argentum et aurum non est michi. Si habere contingat, utere non pro libito, sed pro tempore, sic eris utens illis quasi non uteus. Ipsa quidem quantum ad bonum anime spectat, nec bona stmt nec mala, usus tamen horum bomis, | abusio mala, sollicitudo peior, questus turpior. Esto ut alia quacumque \ racione hec tibi venaices | Possessio pape data est a Caesare, non a Christo vel Petro. | libro Ul.
p. 71: cum ista via sit secura et magis utilis propter multa et illam despicimus, qualiter Dens abscondita revelabit? | opera secundum ml numanum | fiebant, a prophecia et spintu sancto fiebant. Prophecia eniui non est solum dicere futura sed presencta, cnm Saul secundum propheciam monstratus 10 est in vasis occultatns; Dens enim iustis revelat ei prophecia fuit iiec dicere: Separate, iuquit, michi Pautuui et Barnabam; ita et Thimoteus electus est | a PaulOj qui multas prophecias \ habuit, ut quando circumcidit Thimoteum et intronizavit. | Deus eum elegit, non humanum iudicium, qnod intronizatus recoleret custodieudo Dei depositum. | sed non apostolico iure; nec enim tibi dare quod 11011 habuit, potuit; quod habuit, lioc dedit, sollicitudinem ut dixi super ecclesias. Numquid dominacionem? Audi ipsum. Non dominanies, ait, in clero | sed forma facti gregis, et ne hoc dictum sola humilitate putes, non eciam veritate, vox domini est in evangelio: Reges gencium dominantur eorum, vos autem non sic. Ptanum est: apostolis interdicitur dominatus. | In hiis successisti non Petro sed Con- | Locus non sanctificat hominem.
p. 72: Jerusalem que occidis prophetas et lapidas eos | qui ad te missi sunt, | Manasses effudit sanguinem innoxium et implevit Jerusalem cruore innocencium, et ob hanc rem noluit dominus propiciari. | Jerusalem locus sanccior Roma.
```
