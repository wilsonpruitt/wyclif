# Translation brief: potestate-pape 09-a–09-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-09-a.md chunks/potestate-pape/wyc-potestate-pape-09-b.md chunks/potestate-pape/wyc-potestate-pape-09-c.md` once and fix what it reports.
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

## Glossary (the 263 rows these chunks use; the full file is GLOSSARY.md)

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
| presciencia | foreknowledge | |
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| laureola | aureole | The theologians' special crown (of virgins, martyrs, doctors). Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia; prevaricacio | transgressor; transgression; transgression | Ruled 2026-09-28 (*prevaricacio* 2026-10-08, *Pot. pape* 155.10). *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
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
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| preconium | commendation | Ruled 2026-10-02 (*Eccl.* 20, 488.20). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| preco (Dei) | herald (of God) | Ruled 2026-10-07 (*Pot. pape* 06-b, 06-d). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 09-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "194.8–197.27"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "789 words; 736 unanimous or majority-real; 39 settled by vote (R2 24, R3a 10, R5a 4, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n255–n258 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 1: [TITLE]

## ¶1 · 194.8–195.6

> [p. 194] Cum autem necesse est papam continue in ecclesia esse militante, nec est papa vians nobiscum nisi limites Petri servaverit, necessarium videtur de limitibus istis et potestate pape cognoscere. Arguunt autem multi per raciones naturales et alii testimoniis scriptis quod continue oportet aliquem esse papam; quod est concedendum, nam necesse est Christum, qui solus est caput universalis ecclesie esse usque ad finem seculi cum ecclesia militante, ut patet Matth. ultimo; et preter hec necesse est esse confuse aliquem predestinatum viantem, quem Deus propter excessum edificacionis ecclesie sue plus approbat; quem oportet ex eleccione Domini esse papam; et illam eleccionem non potest frustrare humana eleccio. Et sic intelligo decretum VII questione prima, ubi beatus Gregorius ita scribit: In apibus princeps unus est, grues unam sequuntur ordine limitato. Imperator unus, iudex unus provincie. Roma autem condita duos fratres reges simul habere non potuit, sed fratricidio dedicatur. In Rebecce utero Esau et Yacob bella gesserunt. Sic [p. 195] singuli ecclesiarum episcopi, singuli archipresbiteri, singuli archidiaconi et omnis ordo ecclesiasticus suis rectoribus innititur. Oportet igitur unam militantem ecclesiam habere conversantem unum prepositum, cum secundum philosophos omnis multitudo ad unitatem reducitur.

[ENGLISH]

## ¶2 · 195.7–197.2

> [p. 195] Data igitur tota ista sentencia patet ex dictis quod alienum est ex istis inferre quod talis prepositus sit Romanus pontifex vel humanis ritibus institutus. Sed sicut in brutis dux ostenditur a natura, ut patet ex decreto predicto, sic dux christiani exercitus debet ostendi revelacione divina, quia nichil falsius; quam quod humana eleccio facit papam nam solus Deus iustificat hominem. Omnis qui facit papam vel membrum sancte matris ecclesie, facit iustum, igitur solus Dominus facit papam. Maior patet per Augustinum in De Verbis Domini sermone XLV cum locis similibus, ubi reputat oppositum nimis hereticum. Et minor patet ex hoc quod papa (in quantum huiusmodi) est pater sanctissimus atque iustissimus, cum notum sit quod cardinales eligendo membrum non eligunt papam, nec proficit sed officit talem in ecclesia presidere. Ideo Act. primo legitur, quomodo dominus non apostoli Matthiam in apostolum elegerunt. Et certum est quod cardinales ex ficticia introducti non habent efficaciorem auctoritatem quam habuerunt dicti apostoli. Unde videtur multis quod ritus hodiernus eligendi papam inductus sit ecclesie scan dalozus, primo quia est infundabilis ex scriptura. Christus enim cuius potestati humane non possunt equiparari apostoli, elegit sibi apostolos et unum [p. 196] capitaneum inter illos. Petrus autem et omnes alii apostoli non presumpserunt nec audebant eligere unum apostolum, ut patet Act. primo cap. de Matthia, igitur multo magis cardinales infundabiliter introducti non habent potestatem ad eligendum caput universalis ecclesie quod excederet omnes apostolos preter Petrum. Dico autem illos infundabiliter introductos, quia in utroque testamento, si non fallor, fundari non potest eorum institucio sive nomen. Unde quidam dicit quod cardinalis dicitur a cardine, quia in illis porte inferi sunt rotate; sunt, inquit, altera filia sanguisuge, de qua Proverb. XXX, 15: Sanguisuge due sunt filie, dicentes: Affer, after: non enim gerunt vicem apostolorum, cum omnes apostoli erant episcopi. Multi autem eorum non sunt presbiteri. Isti autem videntur inferiores illo de quo Marci IX, 3: Magister, vidimus quendam in nomine tuo eiicere demonia, qui non sequitur nos, quia ut patet ex responsione Christi, ipse fuit non Christo contrarius, ideo fuit ex evangelio minus istis cardinalibus improbatus. Non enim videntur venire in nomine Christi eos mittentis, cum tamquam alter Geysy beneficia ecclesiastica congregant et cumulant et pro eorum vendicione nummos per se vel suos acceptant et sic bona pauperum voluptuose et superbe devorant. Sed nec faciunt miracula nec predicant neque orant, sic quod notando quantitatem ypocrisis et operis, nec Geysy nec Symon dignus est dici eorum minister in servicio Antichristi, quod si est ita: ve illis, ve eorum autoribus et ve omnibus, qui facinori eorum consenciunt. Nec supplent tales vicem dyaconorum, quos constituerunt apostoli, [p. 197] ut patet Act. VI, quia nec faciunt eorum officia nec vivunt eorum vita.

[ENGLISH]

## ¶3 · 197.3–197.20

> [p. 197] Nec valet indagare ex ritibus veteris testamenti, quia nec subest causa neque licencia; ymo quando doctores residebant Jerusalem, ut dicitur fuisse tempore Christi, tunc maxime dissipaverant legem Dei. Ideo nisi dominus dissipaverit consilium Achitophel, possent talia monstra crescere in ecclesia, in specie, in numero et in spoliacione sine fine. Unde igitur talibus monstris innominatis in scriptura potestas ad constituendum caput ecclesie, cum non sit opus hominis facere aliquod membrum ecclesie. Principem autem super eos quantumcumque indignum possunt eligere, eum papam instar sui nominare extranee, sed non possunt constituere caput ecclesie; quod si Deus elegerit et ipsi instinctu Dei in talem consenserint, possunt illum populo intimare. Sed unde talibus ultra apostolos a Deo auctoritas ad eligendum caput ecclesie?

[ENGLISH]

## ¶4 · 197.21–197.27

> [p. 197] Secundo principaliter arguitur ad idem per hoc, quod non licet ecclesie recedere ab observanciis apostolicis quas Christus docuit, sed ante dotacionem ecclesie sacerdotes Christi sine dominio erant socii et communi consilio secundum legem Dei rexerunt ecclesiam, ut patet ex dictis; igitur non licet a limitibus illis ad ritus gentiles recedere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 194.8: There must be a pope, but he must be of Christ's appointing.
- 195.7: Only God can make a pope,
- 195.20: The cardinals' election is of no effect.
- 195.30: The modern form of election is as scandal,
- 196.1: The apostles would not elect an apostle,
- 196.7: The cardinals have been introduced without authority.
- 196.14: They do not take the place of the apostles who were all bishops.
- 196.24: They heap up benefices and devour the goods of the poor.
- 196.27: They surpass Gehazi and Simon.
- 196.30: They do not even supply the place of deacons,
- 197.3: What claim have there 'monsters' to appoint a head of the Church,
- 197.21: It is not lawful tor the Church to abandon the observances of the apostles.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 194: *CAPITULUM NONUM.* [HEAD]
  - 194: *unus* [R3]
  - 194: *Roma autem* (one token covers two printed words) [THIN]
  - 194: *reges simul* (one token covers two printed words) [R3]
  - 194: *Rebecce* [R5]
  - 195: *archipresbiteri* [THIN]
  - 195: *alienum* [R3]
  - 195: *istis* [R3]
  - 195: *scan* (scan | dalozus split by folio bar (209d), no hyphen) [NW]
  - 196: *after* [R3]
  - 197: *instar* (15 is the line number) [R4]
  - 197: *illum* [R3]
  - 194: *duos fratres* (S-split: two words, italic, tightly spaced) [OVERRIDE-SCARPLATE]
  - 197: *observanciis* (LEFT-nw: print = observanciis) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 194:
7. A in marg. : Capitulum Q. 12. A in marg.: Caput ecclesie ne-
cesse est esse Chrialum. Nola Gregorii pro papa JienJo, pro archieph-
copis, pro archipresbyteris et archidiaconis. 26. In Dccr. : literato.

p. 195:
17. AB in marg. : Facere tnembrum ecclesie. 3o. AB in marg. :

p. 196:
11. Codd.: dicunt. i3. AB in marg.: Cardinales quid faciunt.
2 5. Codd.: commutant.

p. 197:
(none)
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 194: In apibus princeps unus est, grues unam sequuntur | ordine \ limitato. Imperator unus, iudex unus pro- | vincie. Romaautem condita duosfratres regessimnl habere uou potuit, sed fratricidio dedicatur. In Rebecce utero Esau et Yacob bella gesserunt. Sic
p. 195: singuli ecclesiarum episcopi, singuli archipresbiteri, singuli archidiaconi et omnis ordo ecclesiasticus suis rectoribus innititur. | Facere tnembrum ecclesie. Eleccio pape.
p. 196: guisuge due sunt fitie, dicentes: Affer, affer: | ° ° J JJ ) JJ > | Magister, vidimus quendam in nomine tuo eiicere demonia, quj non sequitur nos,
```

---

## Chunk 09-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "197.29–200.29"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "686 words; 621 unanimous or majority-real; 53 settled by vote (DEL 1, R2 31, R3a 12, R5a 9); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n258–n261 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 2: [TITLE]

## ¶1 · 197.29–200.12

> [p. 197] Maior patet ex hoc, quod ritus humani servantur ut evangelium, igitur longe evidencius ritus Dei. Non enim licuit sine gravi offensa filiis Ysrahel petere sibi regem, sed rege dato eis a Domino propter offensam graviter sunt puniti, ut patet I. Reg. VIII et infra; multo magis christiani sine licencia Domini, qui contra evangelium sibi constituunt plus quam regem quem papam nominant. Unde decrementum ecclesie; quod [p. 198] continue plus invaluit, et cronice istius materie confirmant eandem sentenciam: Narrat enim Cestrensis libro 86 cap. quomodo ex tunc ecclesia Romana quanto plus cepit ditari, facta est magis instabilis, adepta plus sollicitudinis et subieccionis, quam spiritualia devocionis, plus exterioris assecuta pompositatis quam interioris ut creditur felicitatis. Proinde et hostis antiquus facta per Constantinum hac publica largicione ecclesiis legitur publice in aere proclamasse hodie infusum est venenum in ecclesia Unde Jeronimus scripsit in vitis patrum, ecclesia ex quo crevit in possessionibus: decrevit in virtutibus. Nec moveat, quod videtur dyabolum patrem mendacii sic clamasse, quia certum est quod oportet demones, qui letantur cum male fecerint, ministrare Deo et esse nuncios veritatis; et decet Deum per mamonam preconizare plebi periculum. Alia autem pericula ex hoc, quod sequuntur post correpcionem ecclesie; scimus stultissime applicare ad subtraccionem voluptatum ecclesie, sed vindictas prevaricacionem sequentes quas est evidens ex scriptura et sanctis doctoribus ex hinc sequi abnuimus inde sequi. Ex hinc enim oportet debilitari ecclesiam atque imperium, ut prophetatum est? Daniel II. Ex hinc eciam debilitati sunt episcopi in virtute et populus consequenter, nam, ut patet ex cronicis predictis, tunc debilitati sunt Romani episcopi in tantum; quod instar magcrum Pharaonis, qui in tercio signo defecerant, magnus hereticus fuit papa tercius post Silvestrum. Narrat [p. 199] enim Cestrensis libro suo IV quomodo post Silvestrum successit Marcus, cui successit Julius, qui passus est exilium decennale, et post hunc successit Liberius, de quo cap. 91 lib. IV Cestrensis dicit, quod iussu Constantini exulat tribus annis, quia Arrianis favere noluit. De cuius consilio clerus Romanus ordinavit interim Felicem papam. Qui celebrato consilio duos presbiteros Arrianos condempnans eiecit. Hoc audito Liberius ab exilio revocatur, qui exilii diuturnitate devictus et papatus resuscepcione exhilaratus, ad hereticam pravitatem consensit et Felice deiecto ecclesiam Petri et Pauli et Laurencii tenuit violenter, ita ut clerici et sacerdotes Felici faventes Liberio non prohibente in ecclesia cruciarentur, Felix vero martyrizatur. Iste autem maledictus Liberius non foret plus de papatu exilaratus et cadens in heresim pocius quam pape ante dotacionem nisi propter innaturalem papatus pinguedinem. Et patet probabiliter maior secundi argumenti. Minor autem ex hoc evidet, quod ante dotacionem ecclesie non fuerunt nomina cleri taliter baptizata et per consequens nec dignitatum officia. Idem enim fuit ante dotacionem ecclesie presbiter, episcopus et sacerdos, ut dominus Ardmacanus ostendit libro XI De Questionibus Armenorum V cap. ex scriptura multiplici, primo ex illo ad Tytum I, 5, Reliqui te Crete, ut ea que desunt corrigas, et constituas per civitates presbiteros, si quis sine crimine est, unius uxoris vir, filios habens fideles, non in accusacione luxurie aut non subditos. Et subdit causam condicionis presbiteri. Oportet. [p. 200] inquit, episcopum sine crimine esse, sicut Dei dispensatorem. Ecce quod eundem quem prius vocat presbiterum, id est seniorem, vocat secundo episcopum; id est superintendentem. Item, Act. XX. 27— 28 legitur, quod Apostolus vocans ad se maiores natu ecclesie Ephesiorum, dicit eis: Non subterfugi quominus nunciarem consilium Dei vobis. Attendite vobis et universo gregi, in quo Spiritus Sanctus posuit vos episcopos regere ecclesiam Dei, quam aquisivit sanguine suo. Ecce quod omnes maiores natu id est seniores vel presbiteros vocat episcopos.

[ENGLISH]

## ¶2 · 200.13–200.29

> [p. 200] Item, eidem consonat dictum Apostoli prima Thym. Ill, 1: Si quis episcopatum desiderat, bonum opus desiderat, quasi diceret episcopatus non dicit supra presbiteratum nisi opus superintendencie, unde V cap. specificat dicens: Qui bene presunt presbiteri, duplici honore digni habeantur, maxime quo laborant in verbo et doctrina Dei. Et sequitur: Adversus presbiterum accusacionem noli recipere nisi sub duobus vel tribus testibus. Presbiteros dicit episcopos; quia aliter non diceret IV cap. 14, quod gracia data est sibi cum imposicione manuum presbiteri. Cum igitur ad solos episcopos pertinet manus imponere, ut patet Act. VIII, patet quod Apostolus exprimit indifferenter sacerdotes nomine episcopi et nomine presbiteri; tunc enim non erat coactiva iurisdiccio vel temporalium dotacio que faceret diversitatem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 197.29: The Israelites sinned in wanting a king; we worse in appointing a pope.
- 198.8: The poison of endowment in the Church proclaimed by the Devil.
- 198.27: Heresy soon followed on endowment.
- 199.15: Endowment led Liberius astray.
- 199.20: Before endowment there was no distinction between elders, bishops and priests.
- 200.5: Evidence from Scripture,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 197: *a* (print has dato eis a at line end before Domino) [INS?]
  - 198: *magcrum* (letter after g is open on the right with no join = c (or a broken o); zoomed leaf 259, kept as printed) [NW]
  - 199: *cui* [R4]
  - 199: *lib* [NW]
  - 199: *papatus* [R4]
  - 199: *nomina* [NW]
  - 200: *sicut* [R3]
  - 200: *1* (old-style 1, x-height) [R3]
  - 200: *bonum* [R4]
  - 200: *tribus* [R3]
  - 200: *quod gracia* (one token covers two printed words) [R4]
  - 200: *27—* (LEFT-odd: box on the dash of 27—28) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 197:
(none)

p. 198:
2. AH in marg.: Ecclesia Romana a lempore dotacionis facta est in-
stabilis. 3. Recte: libro IV, cap. XX VI. 5. Codd. : adepla temporalia
sollicitudinis. Correxi. 6. A: contra spiritualia. 12. AB in marg. :
Ecclesia crescens in possessinnibus decrescit in virlutibus. Vnx : venenum
infusum est in ecctesiam Dei. 19, 20. cnrrepcionem ; in corrupcinnem?
?. Polychronicon Ranulphi Higden V/ i3o. (Rr(£f £u>Lu

p. 199:
2. AB in marg.: Depositio pape heretici. 4. Nunc cap. XXVII.
26. AB in marg. : Episcopus presbiter et sacerdos olim fuit idem.
29. B: per civitates deest.
1. V, 146, 148, 1 58. 2?. Cf. Trialogum 276.

p. 200:
24. Codd.: ad dee^t, 28. B: erant.
17. I. Tim. V, 17. 20. V, IQ. 22. I. Tim. 11T. 7 — 8.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 198: ex tunc ecclesia Romana quanto plus cepit ditari, facta est magis instabilis, adepta plus sollicitudinis et subieccionis, | quam spiritualia devocionis, plus exterioris assecuta pompositatis quam interioris ut creditur feli- | citatis. Proinde et hostis antiquus facta per Con- | stantinum hac publica largicione ecclesiis legitur | publice in aere proclamasse 'hodie infusum est | venenum in ecclesia\ Unde Jeronimus scripsit iu vitis patrum, ecclesia ex quo crevit in possessionibus : decrevit in virtutibus.
p. 199: post Silvestrum successit Marcus, cui successit Julius, qui passus est exilium decennale, et post hunc successit Liberius, de quo | exulat tribus annis, quia Arrianis favere noluit. De cuius consilio clerus Romanus ordinavit interim Felicem papam. Qui celebrato consilio duos presbiteros Arrianos condempnans eiecit. Hoc audito Liberius ab exilio | revocatur, qui exilii diuturnitate devictus et papatus resuscepcione exhilaratus, ad hereticam pravitatem consensit et Felice deiecto ecclesiam Petri et Pauli et Laurencii tenuit violenter, ita ut clerici et sacerdotes Felici faventes Liberio non prohibente in ec- | clesia cruciarentur, Felix vero martyrizatur. | Reliqui te Crete, ut ea que desunt corrigas, et constituas per civitates presbiteros, si loquis sine crimine est, unius uxoris vir, fitios habens fideles, non iu accusacione luxurie aut non subditos.
p. 200: episcopum sine crimine esse, sicut Dei dispensatorem. | N011 subterfugi quominus nunciarem consilium Dei vobis. Attendite vobis et universo gregi, in quo Spiritus Sanctus posuit vos episcopos regere ecclesiam Dei, quam aquisivit sanguine suo. | Si quis episcopatum desiderat, bonunt opus desiderat, | Qui bene presuut presbiteri, duplici honore digni habeantur, maxime quo laborant in verbo et doctrina Dei. | Adversus presbiterum accusacioncm uoli recipere | nisi sub duobus vel tribus testibus. | quodgracia data est sibi cum imposicione manuum presbiteri. | episcopum esse irreprehensibilem, unius uxoris virum. | dyaconos autem pudicos, non bilingues, \ non multo
```

---

## Chunk 09-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "200.30–204.29"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "896 words; 813 unanimous or majority-real; 59 settled by vote (R2 40, R3a 16, R5a 3); 24 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n261–n265 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 3: [TITLE]

## ¶1 · 200.30–202.2

> [p. 200] Item, prima Thym. Ill, 2 scribit sibi Apostolus quales condiciones debet habere episcopus: Oportet, inquit, episcopum esse irreprehensibilem unius uxoris virum. Et immediate subiungit: dyaconos autem pudicos, non bilingues, non multo [p. 201] vino deditos, 11011 turpe lucrum sectantes. Si. inquam, inter ordinem episcopalem et ordinem dyaconatus foret ordo medius, iste magnus doctor gencium, qui complete et inmediate evangelium suum didicit a Domino Ihesu Christo, ut patet Gal. primo, distinccionem et regulas illius ordinis non pretermisisset; ymo nusquam in epistola aliqua ponit distinccionem illorum ordinum, sed concludit presbiteros, sacerdotes et episcopos sub nomine apostoli, quem gradum ecclesie inter novem nominat primum tamquam dignissimum, ut patet I. Cor. XII. Et idem dicit Ephes. IV. Unde et illud testantur alii sancti doctores, ut patet in decretis, distinccione XCIII Legimus sub auctoritate Jeronimi, ubi allegantur dicta testimonia Apostoli ad hunc sensum. Et adducitur duplex aliud testimonium, primum illud Apostoli Phil. primo: Paulus et Thymotheus, servus Jhesu Christi, omnibus Sanctis qui sunt Philippis cum episcopis et dyaconibus. Secundum exemplum est dictum Petri I. Pet. V, 1, 2: Seniores igitur, qui in vobis sunt obsecro, consenior et testis Christi passionum, pascite qui in vobis est gregem Dei. Per seniores intelligit iste sanctus cum decreto presbiteros, quibus interdicitur dominatus. Et distinccione XCV Olym sub auctoritate Jeronymi sic recitatur expressius: Olym idem presbiter qui et episcopus, et antequam instinctu dyaboli studia in religione fierent et diceretur in populis: Ego sum Pauli, ego sum Apollo, ego sum Cephe, communi consilio presbiterorum ecclesie gubernabantur. Sicut, inquit, presbiteri sciunt se esse ex ecclesie consuetudine ei, qui sibi prepositus fuerit, esse subiectos, ita episcopi noverint se magis consuetudine quam [p. 202] dispensacionis dominice veritate presbiteris esse maiores et in communi debere ecclesiam regere.

[ENGLISH]

## ¶2 · 202.3–202.8

> [p. 202] Tercio principaliter arguitur ad idem per hoc, quod precipuum officium pastoris suspenditur per elecciones novellas, sed suspenso tali officio non est pastor nisi equivoce, igitur expedicius foret ecclesie quod non foret ad talem dignitatem humana eleccio.

[ENGLISH]

## ¶3 · 202.9–202.31

> [p. 202] Assumptum patet de pastu populi verbo Dei, ad quam ydoneitatem non attenditur, sed omnino postponitur in eleccione huiusmodi. Et constat quod per se ab illo pastu pastor ecclesie trahit nomen, non autem a pastu corporali, cum hoc sit officium laycale, ut pulchre declarat Augustinus in De Verbis Domini Sermone XLIX, exponens textum Joh. X de pastore mercenario et lupo. Mercenarius, inquit, videns aliquem loqui peccata aut sentire secundum perniciem anime sue vel aliquid facere sceleratum, et tamen quia videtur habere alicuius momenti personam in ecclesia, unde si sperat commodum, obmutescit. Videt, inquit, hominem perire in peccato, videt ilium sequi lupum id est dyabolum, videt illius guttur morsu trahi ad supplicium, et tamen non illi dicit: Peccas, uec illum obiurgat, ne perdat commoda sua; talis mentaliter videt lupum venientem et fugit. Sed bonus pastor usque ad mortem facit contrarium. In quo secundum Augustinum est integra racio pastoralis officii. Securos, inquit, nos fecit Spiritus Sanctus per Ezechielem XXXIII. 7, quia limitavit nobis speculatoris officium.

[ENGLISH]

## ¶4 · 202.32–204.29

> [p. 202] Et mundum in testem invoco, quod ista papalis eleccio et sua beneficiorum distribucio seminat [p. 203] in ecclesia mercenarios nimis late, ex parte vero paparum dat occasionem nimis extollendi vicariam potestatem, nimis appreciandi seculi dignitatem et nimis affectandi fantasticam sanctitatem. Illi autem doctores, qui expectant remuneracionem temporalem a papa, dicunt quod est incomprehensibilis potestatis, quia potest omnia que Christus potuit humanitus et multa ultra, que concernunt regimen ecclesie activorum. Nec est aliqua opinio Antichristi magis heretica vel blasfema, quia certum est ex fide quod non habet aliquam potestatem nisi quam Deus dat sibi ad edificandum ecclesiam conformiter legi sue. Quod si habet tantam potestatem, adhuc reddit nimis se dampnabilem, quod non exponit scintillam eius ad regimen presentis ecclesie adeo vacillantis, ymo ut declarat Lumbardus IV sentenciarum distinccione XVIII cap. II et infra ex testimoniis sanctorum Augustini, Ambrosii. Jeronymi, divisus ab ecclesia, ut prescitus non habet potestatem huiusmodi; et quantumcumque verus sacerdos christianus non habet potestatem absolvendi, nisi ad promulgandum divinam sentenciam vel arbitrandum penitenciam aut acceptandum vel refutandum personam secundum quod digna fuerit aut indigna; quod si quis abutitur clavibus discordans ab ecclesia triumphante ostendit se expertem a clavibus sancte ecclesie; et creditur quod supercilium phariseicum ad tantum vibravit claves contra semitas immobiles ecclesie triumphantis, quod perit evidencia et surrepit diffidencia in opere clavium pretendencium se superiorem primatum gerere in ecclesia militante. Sed benedictus Yerarcha tocius ecclesie, quod [p. 204] satis est fidei in ipsum credere. Unde Jeronymus exponens illud Matth. XVI. 29: Tibi dabo claves regni celorum, hunc inquit, locum aliqui non intelligentes, sumunt aliquid de supercilio phariseorum, ut dampnare innoxios vel solvere se putent noxios, cum apud Deum non sentencia sacerdotum sed vita reorum queratur. Sed sicut Levit. XIV ostendere se sacerdotibus iubentur leprosi, quos illi mundos vel leprosos non faciunt, sed discernunt, ita et hic Unde non video de quo prelatus sic Posset pompare inanius quam de huiusmodi potestate, quia ignorat si habeat aliquam huiusmodi potestatem. Ignorat si exercens potestatem reddit se dampnabilem ex errore mendaci ab ecclesia triumphante. Ignorat tercio, si simplex subiectus suus habet eo quantumlibet amplius potestatis. Ideo indubie sacerdotalis potestatis pompacio fetet coram Deo et homine. Coram Deo, quia illi quorum potestas a Deo suspenditur per peccatum vel ex inhabilitate nunquam acceperant potestatem, inmiscent in Christum pompose blasfemias, dicentes se posse ultra hoc quod poterunt apostoli vel eciam Ihesus noster. Addunt eciam in palliacionem sue versucie horrendam heresim, quod Deus pepigit cum eis, quod ipsis? assisteret quicquid pretenderent se solvere vel ligare, eo quod quicquid apostoli rite secundum claves ecclesie sic solverint vel ligaverint, Dei assistencia confirmabat.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 200.30: The only other order was of deacons.
- 201.26: Jerome's authority.
- 202.3: These elections prevent preaching, which is a priest's first duty.
- 202.32: Papal election multiplies hirelings,
- 203.5: Doctors flatter the pope in hope of reward.
- 203.21: Even a true priest has not the power they claim.
- 203.30: The keys have been flourished till they are discredited.
- 204.10: The priest cannot, know what powers he has,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 201: *Paulus* [R4]
  - 201: *1* (old-style 1, x-height) [R3]
  - 201: *Seniores* [R3]
  - 201: *expressius* [NW]
  - 201: *antequam* [NW]
  - 201: *Pauli* (30 is the line number) [R5]
  - 201: *Apollo* [R5]
  - 202: *peccata* (short ascender at t-height (same as t of et), crossbar not inked = broken t; zoomed leaf 263) [R4]
  - 202: *et* [R3]
  - 202: *tamen* (short ascender at t-height (same as t of et), crossbar not inked = broken t; zoomed leaf 263) [R3]
  - 202: *videtur* (print has v) [R4]
  - 202: *uec* (misprint: first letter is u (open top), not n; zoomed leaf 263) [NW]
  - 202: *illum* [R3]
  - 202: *seminat* [THIN]
  - 203: *∅* (second half of incomprehen-sibilis; main scan already holds whole word) [INS?]
  - 203: *diffidencia* (hyphenated diffi-dencia; main token covers whole word) [NW]
  - 204: *intelligentes* (hyphenated in-telligentes; main token covers whole word) [THIN]
  - 204: *sumunt* [THIN]
  - 204: *aliquid* [THIN]
  - 204: *ut* (5 is the line number) [R3]
  - 204: *discernunt* [R4]
  - 204: *ita* [R3]
  - 204: *hic* [R4]
  - 200: *bilingues,* (LEFT-odd: box on a folio bar before non; no word [coordinator: the box was the junk glued to the word; the word stands]) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Jerome's authoritv. (201.26).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 200:
24. Codd.: ad dee^t, 28. B: erant.
17. I. Tim. V, 17. 20. V, IQ. 22. I. Tim. 11T. 7 — 8.

p. 201:
27. Cap. V.

p. 202:
2. Codd.: et deest. S. Codd. : humanam. 9. AB in marg. :
Pastor dicitur a pastu. 17. AB in marg. : Mercenavius. 26. AB in
marg. : Beneficiorum distribucio papalis. 3o. Codd.: XXXI V.
14. Opp. tom. V, 669 (Serm. CXXXVII).

p. 203:
3. ABinmarg.; Potestas pape magna. 3i. \\: perit evideneia deest.
17. Opp. ed. Migne CXGU, 1106.

p. 204:
to. AB in marg. : Clavium abusio et pampa. 19. Codd.r ille.
2. Hier. Gommcnt. in Ev. Matth. Lib. III, cap. XVI, v. 19.
Mignc XXVI, 118. 3i. Magistcr, i. c. Pctrus I.ombard. 1. c.
pag. 887.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 200: episcopum sine crimine esse, sicut Dei dispensatorem. | N011 subterfugi quominus nunciarem consilium Dei vobis. Attendite vobis et universo gregi, in quo Spiritus Sanctus posuit vos episcopos regere ecclesiam Dei, quam aquisivit sanguine suo. | Si quis episcopatum desiderat, bonunt opus desiderat, | Qui bene presuut presbiteri, duplici honore digni habeantur, maxime quo laborant in verbo et doctrina Dei. | Adversus presbiterum accusacioncm uoli recipere | nisi sub duobus vel tribus testibus. | quodgracia data est sibi cum imposicione manuum presbiteri. | episcopum esse irreprehensibilem, unius uxoris virum. | dyaconos autem pudicos, non bilingues, \ non multo
p. 201: vino deditos, 11011 turpe lucrum sectantes. | Panhis et Thymotheus, servus Jhesu Christi, omnibus sanciis qui sunt Philippis cum | episcopis et dyaconihus. | Seuiores igitur, qui in vohis sunt obsecro, consenior et testis Christi passionum, pascite qui iu vohis est gregem Dei. | Olym idem preshiter qin et episcopus, et autequam instinctu dyaholi studia in religione fierent et diceretur in populis: Ego sum SoPauli, ego sum Apollo, ego sum Cephe, communi consilio preshiterorum ecclesie guhcrnahantur. Sicut, | preshiteri sciunt se esse ex ecctesie consue- | ei, qui sihi prepositus fuerit, esse suhiectos, ita episcopi noverint se magis consuetudine quam
p. 202: dispensacionis dominice veritate presbiteris esse maiores et in commnni debere ecclesiam regere. | videns aliquem loqni peccata aut sentire secundnm perniciem anime sne vel aliquid facere sceleratum, et iamen quia videtur habere alicnius momenti personam in eccle- | sia, unde si sperat commodum, obmutescit. Videt, | hominem perire in peccato, videt iUum sequi Iupum, id est dyabolum, videt illius guttur morsu trahi ad supplicium, et tamen non illi dicit: Peccas, uec illum obiurgat, ne perdat commoda sua; talis* mentaliter videt lupum venientem et fugit. | nos fecit Spiritus Sanctus per Ezechielem
p. 204: Tibi dabo claves regni celorum, hunc } | locuni aliqni non intelligentes, sumunt aliquid de superciliophariseorum, ut dampnare innoxios vel solvere se putent noxios, | cum apud Beum non sentencia sacerdotum sed vita reorum queratur. Sed sicut Levit. XIV ostendere se sacerdotibus iubentur leprosi, quos illi muudos vel leprosos non faciuut, sed discernuuf, | Quodcumque ligaveris super terram etc. hoc est ego Deus
```
