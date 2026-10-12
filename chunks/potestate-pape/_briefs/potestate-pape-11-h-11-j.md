# Translation brief: potestate-pape 11-h–11-j

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-11-h.md chunks/potestate-pape/wyc-potestate-pape-11-i.md chunks/potestate-pape/wyc-potestate-pape-11-j.md` once and fix what it reports.
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

## Glossary (the 329 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
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
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
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
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| idiota | unlearned man | Not "idiot". Ruled 2026-09-28 (coordinator, delegated). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| affidacio | affiance | Betrothal by plighted trust; keeps the play on *confidit*. Ruled 2026-10-02 (*Eccl.* 20, 475.22). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
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
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 11-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "290.28–294.2"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 8 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "694 words; 671 unanimous or majority-real; 14 settled by vote (DEL 1, R2 4, R3a 7, R5a 2); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n351–n355 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 8: [TITLE]

## ¶1 · 290.28–291.32

> [p. 290] Et sic sentitur de cruce, per quam sequela Christi in passione saltem carnis crucifixionis notatur, prepositis cesareis auream crucem habentibus, laucius, sumptuosius et studiosius carne pastis. Preciositas vero anuli aurei ingemmata non signat vere desponsacionem prelati cum sponso ecclesie aut Christi ovibus, sed affidacionem cum [p. 291] seculo et lana ac funo balancium. Nec sandalia, que in missis prelatus induit, signant precellenter preparacionem affeccionum in evangelium pacis, ut grex ordinatus sequatur eum faciendo similiter. Sed propter linicionem cesaream sopitur affeccio, quo ad illud officium et duabus viis in volucione serpentina titubando proceditur. Mitra vero gemmata non signat vere utriusque testamenti secundum duos semicirculos perfectam noticiam pastoralem, sed mundanam prudenciam, que est terrena, animalis et dyabolica ad fraudandum tam priores, preteritos quam sequentes. Cyrotece vero que signarent operacionis mundiciam signant potestatis velacionem et sanguinosa opera prelatorum. Pallium vero archiepiscopo novello adiectum, non signat plenitudinem fortitudinis et potestatis cum sciencia, cum vite asperitate atque prudencia ad regendum, sed econtra fortitudinem humane prudencie, ad tribulaciones pro temporalibus sufferendum et ut cingulum equinum ad onus equi et mulicum prudencia seculi supportandum. Et utinam decretales I epistole, de quibus primo decretalium: De autoritate et usu pallii. Ex tenore cum locis similibus rectificarent usum spiritualis pallii, dimisso venali pallio corporali. Sic enim pervertuntur mendaciter signa generacionis adultere, quod minus accusabile nobis foret tantum committere et omittere de signato sine accusacione mendacii, quam quod tantum mendacii sit in signis. Est enim perversio prelatorum simpliciter signis contraria, ut contingit in isto metrico:

[ENGLISH]

## ¶2 · 292.1–292.1

> [p. 292] Sacramentum pingue dabo

[ENGLISH]

## ¶3 · 292.2–292.2

> [p. 292] Non macrum sacrificabo.

[ENGLISH]

## ¶4 · 292.3–292.28

> [p. 292] Cum autem signa ista non sint nisi gracia signatorum, signata per se sufficiunt sine signis, sed signa sine signatorum correspondencia sunt venenum; nec morarer circa hec signa in novo testamento ad onus ecclesie introducta nisi ad detegendum sensum misticum ornamentorum sacerdotalium legis veteris, quibus omnia in figura contigerant ad ostendendum sensum, quem nos utentes talibus signis debemus preponderanter attendere et ad convincendum mendacium philosophice signa ista gerencium. Ad tantum enim quidam in istis vane subtiliant, quod totum officium misse et sacerdotalis officii cum signis suis ac eciam partes basilice cum suis accidentibus mistice moralizant, ut ventilogium in summitate campanilis ecclesie dicunt signare curatum illius ecclesie, qui debet esse in conversacione superior, contemplacione celesti ecclesie triumphanti propinquior et contra omnes ventos temptacionum ecclesie tamquam gallus ad predicandum paracior. Sed Antichristus cum magistro suoLucifero habet sensum contrarium in hiis signis, ut quod prelatus in fastu sit alcior, ad omnem ventum temptacionis vertibilior et tamquam canis mutus non valens latrare, ymo ut nuda galli statua ad fallendum subiectos mendacior.

[ENGLISH]

## ¶5 · 292.29–293.11

> [p. 292] Tercio principaliter arguitur per hoc quod nisi papa haberet plenitudinem potestatis et alii episcopi gradatim, ut in ecclesia ordinantur, periret ordo COnfessionis et timor committendi peccata, ymo per idem non observaretur ritus vel usus alicuius ecclesie, nisi qui foret expresse fundabilis [p. 293] in scriptura, et per consequens nemo observaret aliquem modum in serviendo Deo, sed longe evidencius tolleretur ordo secularium dominorum, sic quod non oportet esse cesarem, cum necessarius foret quod esset dignitas et distinccio clericalis. Ad hec igitur oportet elecciones procedere, sicut dictant leges et usus ecclesie. Non igitur sequitur: Christus et apostoli sic sequuntur, ergo non licet nobis sequentibus facere contrarium, cum pro variacione loci et temporis diversimode est agendum.

[ENGLISH]

## ¶6 · 293.12–294.2

> [p. 293] Quantum ad illud patet quod est expediens quod sit papa, sed ad aggravandum difficultatem loquamur limitate de papa cesareo. Et tunc videtur michi quod multum officit esse talem, ut patet inferius. Diceret autem logicus quod quilibet apostolus et quilibet sacerdos apostolorum vicarius habet in gradu suo plenitudinem potestatis. Sed decretiste videntur intelligere quod quilibet papa habet in infinitum maiorem potestatem iurisdicionis sive regiminis quam aliquis alius episcopus non Romanus, quia (ut sepe dictum est) cum sit infundabile mendacium in materia fidei est nimis hereticum. Petrus enim non habuit tantum aut talem excessum super alios apostolos sibi consocios; nec imperatoris est talem potestatem concedere. Quomodo igitur foret utile tale mendax et monstruosum ydolum ducem tocius corporis Christi fingere? Nec periret ex defectu talis monstri ordo confitendi, ordo regiminis vel alterius boni ecclesie, quia sicut in primitiva ecclesia regulabatur sine tali graduacione dominii in clero ex communi sacerdotum officio, qui omnes erant episcopi, quod exemplatum est [p. 294] in ecclesia apostolica, et tunc crevit ecclesia, sic posset esse hodie ad maiorem utilitatem ecclesie.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 290.28: The Cross.
- 290.32: The Ring.
- 291.1: The Sandals.
- 291.7: The Mitre.
- 291.12: The Gloves.
- 291.15: The Pall.
- 291.23: Since we neglect the thing signified we should be better without the sign.
- 292.13: Absurd and fanciful symbolizing.
- 292.29: 3rd argument: But for the powers of pope and prelates order would perish.
- 293.12: Answer. It may be well to have a pope but not such as we moderns have.
- 293.24: Peter claimed no such authority over his followers.
- 293.29: Why pretend that this monster is the head of Christ's body.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 290: *carne* [R3]
  - 290: *ingemmata* (print has double m) [NW]
  - 291: *funo* (print has n (funo), kept as printed) [NW]
  - 291: *novello* [R4]
  - 292: *omnia in* (one main token covers two printed words) [R5]
  - 292: *ordo* [R4]
  - 293: *Quantum* [R3]
  - 293: *talis* (30 is the line number) [R4]
  - 291: *quibus primo* (S-split: two words) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 290:
12. Codd.: comunam. 20. A in marg. : Bacuhts. 2S. Codd. in
marg.: Crux episcopomm. 32. Codd. in marg. : Atiulus.

p. 291:
1. Hic locus corruptus esse videtur. Codd. in marg. : Mitra.
12. Codd. in marg.: Cyrotece. i5. Codd. in marg : Palium.
24. I, 8 Cap. V; sed est cap. Ex tuarum.

p. 292:
23. Codd. in marg. : Gallus supra pinaculum campanilis positus quii
signat. 3i. Codd. in marg. : Potestatis plenitudo tn papa.

p. 293:
l3. B: fit. 29. Codd. in marg. : Ordo ecclesie non periret non
existcnte cesareo papa.

p. 294:
15. Codd. in marg. : Consuetudinum laudabilium fundamentum.
2(j. sacrum; ita cod.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 291: Ex tenore
p. 292: Sacramentum pingne dabo Non macrum sacrificabo. | canis \ mutus non valens
p. 294: Omnia honeste et secundum ordinem fiant.
```

---

## Chunk 11-i: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-i.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-i
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "294.3–299.5"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 9 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1144 words; 1089 unanimous or majority-real; 44 settled by vote (DEL 1, R2 28, R3a 14, R5a 1); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n355–n360 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 9: [TITLE]

## ¶1 · 294.3–299.5

> [p. 294] Conceditur tamen, quod ex illo, sicut ex quolibet malo quedam propria utilitas succedit ecclesie. Sed (ut utar verbis Apostoli) absit ut illa mala sint propterea facienda. Ulterius conceditur quod observanda est laudabilis consuetudo ecclesie, licet non sit explicita sed implicita in scriptura, quia minus diffusa et onerosa foret lex Christi, si omnes tales ritus, usus vel consuetudines forent in ea expresse. Ideo credendum est quod Spiritus Sanctus necessariora ecclesie expressit, et leviora sub quodam confuso involucro simul texit, ut patet prima Cor. XIV 40; dicit spiritus per suum Apostolum: Omnia honeste et secundum ordinem fiant. In quo includuntur omnes usus ecclesie in dicendo servicium, omnes ritus ordinum privatorum, et breviter omnis consuetudo clericalis vel laycalis laudabilis. Et in isto puncto surrepit maior irreligiositas populi christiani, quod postponendo preponderanciora expressa in lege Domini, preponderantur tradiciones et adinvenciones humane, quedam heretice et quedam in suo ordine observande. Sicut enim scriptura docet nos ista preponderanter cognoscere, sic minimum expressum in lege Domini observare sub incursu maioris pene quam aliquid quod est expressum singulariter in usu sacrum vel ritus aliquos eciam ordinate in religiosis vel laicis preter fidem Christi expressam noviter introductos. Et in isto cecatur ac oneratur ecclesia ultra modum, quia vel introducuntur irracionalia vel racionalia suntnimium ponderata. Unde decretum XII distinccione sub [p. 295] auctoritate Augustini ad inquisiciones Januarii sic loquitur (ut sepe repecii): Omnia talia que neque scripturarum sanctarum auctoritatibus continentur nec in consiliis episcoporum statuta inveniuntur nec consuetudine universalis ecclesie roborata sunt, sed diversorum locorum diversis moribus innumerabiliter variantur, ita ut vix aut nunquam inveniri possunt cause, quas in eis constituendis homines secuti sunt, ubi facultas tribuitur sine aliqua dubitacione resecanda estimo. Quamvis enim hoc non inveniri possit, quomodo contra fidem sint, ipsam tamen religionem quam paucissimis et manifestissimis celebracionum sacramentis misericordia Domini voluit esse liberam, servilibus oneribus adeo premunt, ut tollerabilior sit condicio Iudeorum, qui etsi tempus libertatis non cogno verunt, legalibus tamen sacramentis, non humanis presumcionibus subiciuntur. Ex istis videtur, primo quod infidelius nostri pharisei premunt ecclesiam tradicionibus, sectis et exaccionibus quam fecerant pharisei legis veteris. Ipsi enim undique parcius onerarunt; moralia legis preponderarunt et veniente figurato viderunt quod figure cessarunt. Nostri autem pontifices, scribe et pharisei magnificant infideles tradiciones hominum, eciam ultra tradiciones quas Deus instituit, cum illas dicunt oportere cessare, si onus sapiunt et nonlucrum; tradiciones vero suas, que honorem vel lucrum temporalem sapiunt, dicunt non posse cessare, licet sint tradicionibus et vite Christi contrarie; cum per illas consecrantur res, a qua consecracione non licet recedere; deminuere autem libertatem, que est verum privilegium ecclesie, per [p. 296] falsos dico non clericos sed idiotas, vocem propriam ignorantes, foret nota infidelitatis discipulo Antichristi. Quando enim queritur ab eis racio facti, vel balbuciunt, dicentes machometice quod non debet dari vel disputari racio sue tradicionis, cum per se sufficit voluntas capitis, vel arguunt ex insufficienti similitudine de lege veteri, vel allegant infundabiliter leges hominis, ut quod iurisconsultus vel satrapa sic diffinit, nec licet (ut inquiunt) racionem querere ut in lege Dei sed ad ipsos ut primum principium est sistendum. Seculares autem provident quod leges eorum consonent legi Dei, quia utilitati et racioni, cum profitentur catholice quod omnis lex vel ritus hominis que non habet ab ipsa principium est heretica et fugibilis ut venenum. Ex quo patet quod lex Dei debet primo disci a quocumque catholico. Quid inquam fideli de lege alia? Unde lex Dei cum tradicionibus humanis sophistice est commixta; scilicet ut tradicio pallietur et coloracius observetur. Observet igitur fidelis iusticiam legis et paret se ad sufferendum iniurias et penas pro omissione legum hominum. Hoc enim directe accelerat viatorem ad terminum et oppositum deviat vel retardat. Conceditur igitur quod ritus et leges honeste ex lege Dommi eliquate sunt in suo ordine observande. Sed caveat christianus de nimietate studii eorum et observancie; suspensus itaque in lege Dei sine ulteriori sollicitudine sit contentus de flatu spiritus sine istis extravagantibus dirigentis. Quid queso fideli de gentili ritu vel phariseico nisi de quanto modeste facilitat ad observanciam legis Dei? Unde graviter peccarunt, qui introduxerunt [p. 297] sectas et distincciones legum ecclesie, per quas diminuitur meditacio legis Dei, cum melius esset quod pure observaretur vita apostolica, et dimissa difformitate tenderetur ad uniformitatem status innocencie, licet graduacio in seculari dominio sit licita ac necessaria peccato supposito. Unde nichil infidelius quam ex graduacione secularis dominii concludere graduacionem dominacionis et honoris secularis in clericis. Cum enim status ille sit alcior, statui Christi et sanctorum conformior, oportet quod tendat ad maiorem unitatem, regulans statum laycalem et non sit a statu tam difformi quem regulat exemplatus. Conceditur tamen quod sunt gradus in illo statu apostolico; sed contrarie ad statum secularem; nam hic maior est pauperior, servitivior et ad currendum per peregrinacionem cum paucioribus temporalibus sufficiencior. Unde omnes presbiteri debent esse socii, ut docet Apostolus cum decreto de ipso et Petro, verumtamen servus ex maiori humilitate fit alcior. Unde (ut sepe dixi) pars laycalis dividitur in popularem et partem secularem illi prepositam quarum prior est bona et secunda melior. Sed pars clericalis propter socialem uniformitatem remanet indivisa et optima, quam elegit Maria; unde periculose balbuciunt, qui dicunt quod reges non sunt domini regnorum, sednudi defensores, velaliter (ut inquiunt) oportet dare in clericis gradus talis dominii. Scrutentur isti scripturas et videre possunt, quam spissim autor scripture tam verbo quam opere concedit illis de medio statu dominium, cum ipse obedienter dedit tributum cesari, a se ipso autem ac suis apostolis et eorum successoribus [p. 298] exclusit dominium, ut patet superius. Iudicent igitur inter evidencias; Deus interdicit sacerdoti Christi dominium et dat seculari dominium, igitur sic debet esse. Et cesar vel lex papalis negat seculari adesse dominium et dicit quod pape ac episcopis debet adesse quodcumque seculare dominium, igitur verum. Et sic de istis locis a simili: Christus exclusit se et suos apostolos a seculari dominio, igitur per idem hoc debet a suis vicariis observari, et seculares domini ac prelati vendicant sibi dominacionem civilem, primi legittime et secundi falsa usurpacione, igitur per idem omnes clerici debent taliter dominari. In tales argucias arundineas prorumpunt qui siciunt seculare dominium; et necesse est ut multiplicetur in clero Christi, sicut in parte multiplicabatur in clero legis veteris, talis confusio, quousque Antichristus destruxerat membra sua. Ideo cum secundum variacionem loci et temporis agendum est; ut congruit, patet quod regnante cupiditatis malicia sequenda est nobis via Christi sollercius, nam imminente maiori periculo debet periclitans magis inniti suffragio. Sic enim fecit sacerdos Christus veniens in summo gradu expropriacionis, quando summe regnavit cupiditas sacerdotum. Et hec est causa apostoli, ut prius exposui. Redimentes, inquit, tempus, quoniam dies mali sunt, unde nimis blasfemant degeneres qui dicunt quod tam utile et tam conveniens est statui cleri modo ditari amplius quam necessaria fuit potestas faciendi miracula in ecclesia primitiva. Revera tunc nec clerus possessionatus nec laycus daret corporalem elemosinam mendicanti, sicut apostoli non diminuerent de potestate faciendi [p. 299] miracula, ymo potestas, quam Evangelista habuit ad mutandum littoria saxorum fragmenta in gemmas et silvestres frondes in aurum, foret mundo utilior quam quantacumque temporalis possessio, sicut testaretur eciam Symon magus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 294.7: It is well to keep good customs, but those are of most importance which are expressly enjoined in Scripture.
- 295.18: How our pharisees oppress the Church,
- 296.5: and give no good reasons for their traditions.
- 296.24: We should pay little attention to them and depend on the law of God.
- 297.7: The government of the Church should not be modelled on thet of the State.
- 297.30: Scripture authorizes seculari rule.
- 298.5: False claims set up by the papal law.
- 298.29: Some say: Endowment replaces the power of working miracles.
- 299.1: Miracles like St. John's would please them.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 294: *illa* [R3]
  - 295: *in* [R3]
  - 295: *tribuitur* (italic t) [NW]
  - 295: *verunt* (cogno | verunt split by folio bar (234ᵈ in margin), not a hyphen; this line's part) [NW]
  - 296: *et* (20 is the line number) [R3]
  - 296: *eliquate* [NW]
  - 297: *unitatem* [R4]
  - 297: *socialem* (hyphenated socia-|lem (25 line number); main token holds the whole word) [R4]
  - 298: *mali* [R3]
  - 295: *oneribus* (LEFT-nw: hyphenated one-|ribus) [OVERRIDE-SCARPLATE]
  - 295: *licet* (S-split: line number 30 glued (read as so)) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 294:
15. Codd. in marg. : Consuetudinum laudabilium fundamentum.
2(j. sacrum; ita cod.

p. 295:
1. Codd. : Augustini 2. 2. Codd. in marg. : Ritus gravantes ecclesiam.

p. 296:
3. Codd. in marg. : Rituum, tradiciomim et consuetudinum defensio.
16. Codd. in marg.: Lex Dei maxime est sludenda.

p. 297:
7. Codd. in marg. : Gradus dignitatis in secularibus non concludit esse
tales inclericis. i3. A in marg. : Vide qualiter admittit gradus in clero.

p. 298:
27. Eph. V, 10.

p. 299:
2. De Ecclesia pag. 189 and 81 supra.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 294: Omnia honeste et secundum ordinem fiant.
p. 295: Omnia talia que neque scripturarum sanctarum auctoritatibus continentur nec iu consiliis episcoporum stattita inveniuntur | nec consuetudine universalis ecclesie roborata sunt, sed diversorum locorum diversis moribus innumerabiliter variantur, ita ut vix aut nunquam inveniri possunt cause, quas iu eis constituendis homines secuti sunt, ubi facultas iribuitur sine | aliqua dubitacione resecanda estimo. Ouamvis euim hoc non inveniri possit, quomodo contra fidem sint, ipsam tamen religionem quam paucissimis et manifestissimis celebracionum sacrameutis misericordia Domini voluit esse liberam, servilibus oneibribus adeo premunt, ut tollerabilior sit condicio Iudeorum, qui etsi tempus libertatis non cogno \ | verunt, legalibus tamen sacramentis, non humanis presumcionibus subiciuntur.
p. 298: Redimentes, inquit, tempus, quoniam dies mali sunt,
p. 299: ad mutandum littoria saxorum fragmenta | in gemmas et silvestres frondes in aurum, | Si vis perfectus esse y vade et vende omnia que habcs, et da pauperibus, et veni, sequere me.
```

---

## Chunk 11-j: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-j.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-j
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "299.6–302.33"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 10 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "832 words; 775 unanimous or majority-real; 44 settled by vote (R2 34, R3a 9, R5a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n360–n363 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 10: [TITLE]

## ¶1 · 299.6–300.26

> [p. 299] Ista autem sentencia placeret quibusdam episcopis qui, licet debeant habere omnia cum fratribus in communi, tamen stante ista sentencia pro conservandis suis privilegiis non tribuerent eis temporalia plus vel minus. Et multo evidencius nec aliquis secularis. Dignitas itaque clericalis est dignitate seculari necessarior, sed oportet quod sit illa dignitas paupertatis et moris quam Christus instituit, quia secularis dignitas cleri utramque partem matris nostre intoxicat. Christus enim in cunabulis satis pauperibus adoratus fuit a regibus, ut patet Matth. II. Sed indutus vestem purpuream fuit flagellatus a militibus, ut patet Mar. XV. Unde premittit exoneracionem et excussionem festuce fedantis ecclesiam, et sic tamquam formam ultimam vie inducit apostolicam dignitatem, ut patet Matth. XIX. Et ibidem dicitur: Si vis perfectus esse, vade et vende omnia que habes, et da pauperibus, et veni, sequere me. Christus enim noluit suos apostolos occupari circa tam contemptibile officium, cuiusmodi est civilis distribucio elemosine corporalis; hoc enim est laycale officium, quod sacerdotes debent postponere. Tercium vero exemplum periculi est quod Apostolo ferenti benediccionem vel elemosinam sanctis Jerusalem opposite fuerunt insidie, ut innuitur Act. XX. Non obstante autem multiplici evidencia fideli, nonnulli, qui gustaverunt altissime paupertatis dulcedinem, habent ex religione omnia [p. 300] in communi, apostatant plus quam Ananyas et Saphira, palliantes dignitatem episcopalem et bona pauperum non cum fratribus, sed nimis seculariter et proprietarie consumentes; unde videtur ut supra, quod fratres sui qui multipliciter apostasie tam gravi consenciunt, carerent benediccione populi dicentis quod capiant de bonis suis, quibus habundant populo copiosius in se et suo episcopo. Nec dubium fideli quin fratres qui propter personale commodum vel honorem ordinis vel aliunde omittendo talem corripere culpe sue consenciunt, et sic indignificant se ad recipiendum elemosinam pauperum laycorum. Nam debet esse per se notum fidelibus quod propter peccatum personale est communitas punienda, ut propter peccatum primi hominis totum genus humanum patitur, ut propter errorem archiprepositi inferiores prepositi et tota communitas paciuntur. Ideo (ut dixi alias) ad destruendum errorem paparum totus christianismus et specialiter episcopi debent consurgere. Blasfemant enim inDeum, dicentesquod ipsi habent infinitum maiorem potestatem quam aliquis episcopus citra ipsos, quia infinitum ampliores indulgencias, dispensaciones et cetera privilegia possunt concedere quam aliquis episcopus citra ipsos.

[ENGLISH]

## ¶2 · 300.27–302.22

> [p. 300] Et hoc indubie sonat in scandalum toti ecclesie propter multa: primo quia blasfemia facta in Christum caput, qua innuitur quod papa sit maioris potestatis date a cesare quam Christus habuit, facit subtraccionem capitalis suffragii; secundo quia papa habente solum finitam potestatem quilibet illorum prelatorum non haberet potestatem sub aliquo gradu signabili, et tercio quia propter subtraccionem minoris boni quam [p. 301] foret subsidium, quod papa subtrahit populus licite et laboriose prosequitur. Quare igitur non prosequitur contra papam correptibilem fratrem nostrum? Et ista videtur sentencia beati Gregorii posita XCIX distinccione: Ecce, ubi precepit Eulogio patriarche Alexandrino quod non vocet eum amplius papam universalem: Vobis, inquit, subtrahitur quod alteri plus quam racio exigit prebetur, ego vero non verbis quero prosperari sed moribus, nec honorem esse deputo in quo fratres nostros honorem suum perdere Cognosco. Meus namque est honor universalis ecclesie, meus honor est fratrum meorum solidus vigor; tunc ego honoratus sum, cum singulis quibusque honor debitus non negatur. Si me enim universalem papam vestra sanctitas dicit, negat se esse hoc, quod me fatetur, universum, sed absit hoc, recedant verba, que unitatem inflant et caritatem vulnerant. Unde Pellagius papa: Nullus patriarcharum universalitatis vocabulo umquam utatur, quia si unus eorum universalis dicitur, patriarcharum nomen ceteris derogatur. Sed absit a fidelibus hoc sibi quempiam nomen velle arripere, unde honorem fratrum suorum ex quantidacumque parte minuere videatur; quapropter caritas vestra neminem umquam in suis epistolis universalem nominet, ne sibi debitum subtrahat, dum alteri honorem offert indebitum. Ideo ex generali concilio decretum est, quod prime sedis episcopus non appelletur princeps sacerdotum aut summus sacerdos aut aliquid huiusmodi, sed tantum prime sedis episcopus. Universalis autem nec eciam romanus pontifex appelletur. [p. 302] Licet enim possent hec nomina sane intelligi, mirum est tamen quomodo posteriores, peiores prioribus, tale nomen singulariter sibi vendicant sine fructu; etenim onus nimium, licet omnes tales episcopi comportent et regulent ecclesiam communi concilio sicut olim. Et patet, quod nuda est ista argucia, Gregorius vel alius sanctus Romanus episcopus fuit precellens pre aliis, igitur per idem et quilibet Romanus pontifex. Variatur enim stulta affeccio dignitatis. Stultum quidem est assumere nomen Christi, ut Bernhardus, Lyncolniensis et Jeronymus describunt sine possibili correspondencia dignitatis. Idem enim est hoc facere et symeam ad summum repere ut profundius et gravius preceps ruat. Sed contra ista arguitur per hoc, quod totus iste ordo cesareus videtur esse ad honorem et utilitatem ecclesie matris sancte, non igitur destruendum est tam utile et tantum faciens ad honorem ecclesie, potissime cum nescitur quibus prodesset eius destruccio, et nulla persona ecclesie est improvide punienda.

[ENGLISH]

## ¶3 · 302.23–302.33

> [p. 302] Assumptum videtur ex hoc quod, etsi omnes dotati forent dampnandi ex dotacione, adhuc dotacio foret ad honorem et utilitatem ecclesie, igitur multo magis multis personis hinc altrinsecus merentibus et salvatis. Assumptum patet ex hoc, quod totus prescitorum numerus sicut et omnis culpa proderit per accidens et honorabit numerum salvandorum, nam dampnati exercitabunt predestinatos, glorificabunt eorum victorias et cedent eis ad augmentum et racionem beatitudinis ut hic supponitur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 299.12: The dignity of the clergy consists in poverty and Christlike life.
- 300.19: Christendom should unite to destroy the errors of the popes.
- 301.5: Example of St. Gregory, who would not be called universal pope.
- 302.1: Danger of using such titles.
- 302.16: It is said that the hierarchy is to the honour of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 299: *illa* [R3]
  - 299: *habes* (italic e with a faint, broken eye (not c); damaged letter) [NW]
  - 300: *∅* (folio bar before sub (236ᵇ in margin) read as i) [INS?]
  - 300: *tercio* (236ᵇ is the folio mark) [R4]
  - 301: *nec* [THIN]
  - 301: *honorem* [THIN]
  - 301: *meus* [R3]
  - 301: *recedant* [R4]
  - 301: *∅* (25 is the line number) [R4]
  - 301: *∅* (folio bar before sed (236ᶜ in margin) read as i) [INS?]
  - 302: *∅* (that is the English side note (It is said that ...)) [R6]
  - 302: *utilitatem* [NW]
  - 301: *Eulogio* (LEFT-odd: print = Eulogio) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Danger of using sucli . . tities. (302.1).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 299:
2. De Ecclesia pag. 189 and 81 supra.

p. 300:
21. Codd. in marg. : Potestas pape injinita supra alio* episcopos.

p. 301:
5. Codcl. in marg. : Universalis papa noluit vncari Gregorius
G. Codd. : Eulogie.
5. Cap. V. 19. Decreti Prima Pars. Dist. XCIX, cap. IV.
29. Decreti Prima Pars, Dist. XCIX, cap. III.

p. 302:
4. 15: sive fructum. 16. Codd. in marg. : Argumentum forte pro
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 299: ad mutandum littoria saxorum fragmenta | in gemmas et silvestres frondes in aurum, | Si vis perfectus esse y vade et vende omnia que habcs, et da pauperibus, et veni, sequere me.
p. 301: papam universalem: Vobis, | subtrahitur quod alteri plus quam racio exigit prebetur, ego vero non verbis quero prospe- | rari sed moribus, nec honorem esse deputo in quo fratres nostros honorem suum perdere Cognosco. Meus namque est honor universalis ecclesie, meus honor est fratrum meorum solidus vigor; tunc ego houoratus sum, cum singnlis quibusque honor deibbitus non negatur. Si me enim universalem papani vestra sanctitas dicit, negat se esse hoc, quod nie fatetur, universum, sed absit hoc, recedant verba, que unitatem inflant et caritatem vulnerant. | Nullus patriarcharum universali- | tatis vocabulo umquam utatur, quia si unus eorum uuiversalis dicitur, patriarcharum nomen ceteris derogatur. Sed absit a fidelibus hoc sibi quempiam nomen velle arripere, unde honorem fratrum suorum ex quantidacumque parte minuere videatur; | quapropter caritas veslra neminem umquam in suis epistolis universalem nominet, ne sibi debituui subtrahatj dum alteri honorem offert indebitum. | prime sedis episcopus non appelletur princeps sacer- | dotum aut summus sacerdos aut aliquid huius- | sed tantum prime sedis episcopus. Universalis autem nec eciam romanus pontifex appelletur.
p. 302: Argumentum forte pro dotacione.
```
