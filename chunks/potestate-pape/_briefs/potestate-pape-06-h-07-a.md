# Translation brief: potestate-pape 06-h–07-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-06-h.md chunks/potestate-pape/wyc-potestate-pape-06-i.md chunks/potestate-pape/wyc-potestate-pape-07-a.md` once and fix what it reports.
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

## Glossary (the 234 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
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
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| dotacio | endowment | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
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
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 06-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "129.32–133.25"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 8 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "787 words; 766 unanimous or majority-real; 15 settled by vote (R2 6, R3a 7, R5a 2); 6 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n190–n194 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 8: [TITLE]

## ¶1 · 129.32–131.34

> [p. 129] Et istam sentenciam approbat tota Trinitas cum tota ecclesia triumphante, tota natura bestiarum [p. 130] cum condicione status innocencie et saniores monachi, qui propter perfeccionem decreverunt statum illum eligere. Et patet probabilitas cronice, quam narrat Cestrensis libro IV, cap. LXXXVI quomodo tempore dotacionis ecclesie audita est angelica vox in aere, dicens quod hodie effusum est venenum in ecclesia sancta Dei. Nam quomodocumque hoc fuerit, hoc est verum, cum clerus a statu perfecciori decidit sine equivalente recompensa, ut eventus patulus rei probat. Unde manifestum signum foret Pseudochristi dampnantis ut hereticum quod genus illorum qui sic maculaverunt matrem nostram possunt eam purgare de macula quam ex eorum stulticia sic contraxit. Unde capitalis defendens pertinaciter istam sentenciam contra perfeccionem membrorum Christi et sancte matris ecclesie, heresiarcha racionaliter potest dici. ed dubitatur si homo sit simul in multis statibus. Et videtur planum quod sic de statibus tam corporis quam anime compossibilibus, sicut homo habet simul denominaciones multorum actuum, ut puta qualitatum. Similiter differendum est utrique preposito peccanti propter dignitatem status, ut patet LXXXII distinccione cap. Presbiter et sepe alibi; et cum hoc valet efficaciter testimonium Augustini in multis locis, ut ubi docet quod in Pharaone, in Nabuchodonosor propter statum et dignitatem regalem ad regimen populi subiecti Deus inspiraverat propheciam, et propter sacerdotalem [p. 131] dignitatem Deus dedit Cayphe propheciam, ut dicit Augustinus in de Questionibus veteris et nove legis XXXV, et hinc David rite pepercit Sauli, ut patet I Reg. XXIV. Similiter, aliter nullius status celsitudo gravaret peccatum, quod est contra illud Sapiencie VI, 6 Durissimum iudicium hiis qui presunt, fiet, ymo aliter cuiuscumque prepositi status extingueretur, antequam quicquam boni vel mali faceret, que contradicunt scripture, cum ecclesie legibus, communi modo loquendi et sanctis doctoribus. Supposita igitur constancia statuum et facta limitacione ad statum quem preter nudos ritus humanos Deus ordinat, est dubium quomodo status variatur propter actus statui dissonos vel peccatum. Videtur enim quod status cum sit accidens tam parve constancie quod sit inalterabilis et per idem immobilis, cum manet eius dignitas cum peccato; aliter enim status sacerdotalis posset per alteracionem subiecti equiparari statui laycali et quilibet status cuilibet. Similiter, cum dignitas status hominis sit impertinens suis moribus, videtur quod stat eundem esse simul quantumcumque dignum et indignum et propter multiplicitatem statuum foret impertinens discernere per statum de hominis dignitate, nec sufficit homo cognoscere statum totalem aggregatum, tum quia infinitus est statuum numerus, tum quia aliquem statum proximi oportet viatorem quomodolibet ignorare. Similiter, cum status denigrari et debilitari poterit et alias serenari, videtur quod omne mortale statum quem invenit inficit, cum secundum Augustinum facit hominem esse nichil.

[ENGLISH]

## ¶2 · 132.1–133.25

> [p. 132] Ex quo videtur quod sicut homo dubitat de proximo si sit in mortali vel prescitus, sic dubitaret de excellencia cuiuscumque status viantis. Sic enim fuit status exproprietarie vivendi Scariothis vilissimus, ymo cum status sit successivus et dubitatur de fine qui est status beatitudinis secundum Boecium III de Consolatione philosophie videtur, quod quilibet foret de totali statu fratris sui ambiguus. Hic oportet supponere descripcionem et distinccionem supradictas de statibus. Et secundo oportet notare quomodo dupliciter aliquid dicitur transmutari, vel subiective vel gracia concomitancie. Subiective ut sola substancia transmutatur; gracia concomitante omnis status vel res alia inexistens homini melioratur vel peioratur propter concomitanciam virtutis aut vicii. Et sic res in natura sua continue nunc est melior et nunc peior, et sic fides et spes possunt nunc formari caritate et nunc remanere informes, cum ipsa non permittit secum crimen ut suprema virtus et simplex. Et patet, quod triplex primum argumentum roborat veritatem. Quantum ad primum trium argumentorum sequencium patet ex distinccione iam posita, quomodo status non alteratur subiective sed con- comitative. Et quandoque per peccatum extinguitur, quod pertinet ad eum cognoscere, qui nobis incomprehensibiliter ordinat cunctos status; quamvis autem materia de statibus sit valde ampli ambitus, ut medicus tractat de statu corporis, ut precedit ad felicitatem vie sive miseriam, politicus [p. 133] autem considerat de statu partis populi, secundum quem respicit pacem reipublice, tamen theologus et curatus, qui debet esse animarum medicus, considerat de statu hominis secundum virtutes vel vicia, ut respicit statum beatitudinis; et de tali statu est nobis sermo. Ipse autem infinitum excedit status alios, eciam status vivendi sive officii, qui dicuntur racione concomitancie virtutis vel vicii alterari; et patet ad primum obiectum. Ad secundum dicitur quod status temporalis est impertinens moribus quantum ad naturam status pertinet, vel in se simpliciter quod solum considerantes naturas universalium et reduplicativas concipiunt, verumtamen quantum ad denominacionem respectivam concomitancie status, tales valde pertinenter respiciunt virtutes et vicia; et hinc voco eos status disposicionis et alios virtutis; et sic concedo quod stat eundem esse dignum et indignum equivoce quoad dignitates morum et status, ideo pertinet specificare de qua hominis dignitate loquimur, quando ex statu dignitatem hominis arbitramur, et ultra conceditur quod non sufficimus hic cognoscere nisi imperfecte de statu totali hominis, quia ignoramus de exitu.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 130.19: A man may be in several states at once.
- 130.24: The higher a man's state, the worse his sin.
- 131.17: A man's state is not changed by his sin.
- 132.1: We cannot judge of the spiritual state of others.
- 132.11: Change may be in substance or in concomitant good or evil.
- 132.24: It is in the latter way that state is altered,
- 133.1: As doctors treat of the state of the body, so priests should of the soul.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 130: *illum* [R3]
  - 130: *∅* (English side-note word) [R3]
  - 131: *hiis* [R4]
  - 131: *fiet* [R3]
  - 132: *non* [R3]
  - 132: *con-* (hyphenated con-comitative; main token holds first half, 25 is the line number) [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 129:
4. AB in marg.: Status diversi secundum gradus. 12. B: et tantum.
26. B in marg. : Perfecciones in aniversali non augentur sed in singulari.
32. AB in marg. : Status exproprietarius approbatur a tota Trinitate.
De Potestate Pape. 9

p. 130:
2. monachi. Codd. : monses. 7. AB in marg. : Vox hodie effusum
est venenum. 19. AB in marg. : Status multos si tenet homo.
4. Cestrensis, i. e. Radulphus de Higden in Polychronico.
Non est cap. LXXXVI sed XXVI, tom. V, i3o. 26. Decreti
Prima pars, dist. LXXXII, cap. V.

p. 131:
5. A in marg. : /. 22. A in marg. : 2.
3. Opp. tom. III, App. p. 53.

p. 132:
1. A in marg. : 3. 4. A in marg.: Nota optime.' 5. B: Vilissimis.
7. Codd.: de questione. 11. AB in marg. : Mutari dicilur aliguid dupli-
citer. 19. Codd.: caritatem. 23. B in marg. : Ad primum. 3o. AB
in marg.: Diversitas statuum. Dignum et indignum slat eundem esse ho-
minem. 3i. B: policitus.
7. Opp. (ed. Migne t. LXIII), pag. 720.

p. 133:
io. AB in marg. : Ad 2. 26. AB in marg. : Ad tercinm. 27. so-
lummodo ; cod.: sodo. 3o. AB in marg. : Corripere potest subditus pre-
positum.
32. Decr. Greg. IX, Lib. V, tit. XXXII, cap. 2.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 130: hodie effusum est venenum in ecclesia sancta Dei.
p. 131: Durissimum iudicium hiis } qui prestint, fiet,
p. 133: Cum ex iniuncto
```

---

## Chunk 06-i: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-i.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-i
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "133.26–135.11"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 9 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "346 words; 332 unanimous or majority-real; 10 settled by vote (DEL 1, R2 3, R3a 2, R5a 3, R6a 1); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n194–n196 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 9: [TITLE]

## ¶1 · 133.26–135.11

> [p. 133] Ad tercium patet quod status denigratur vel serenatur solummodo concomitanter, ethoc quoad Deum, quomodo omne mortale denigrat, et super isto currunt multe leges hominum propter quas pusillanimes timent sibi nedum corripere sed peccata publice predicare, ut V decretalium De Hereticis cap. Cum ex iniuncto in fine prohibetur quod inferior publice corripiat patrem suum; et [p. 134] multe sunt leges huiusmodi, que omnes intelliguntur quod nemo debet illegitime fratrem suum corripere; non enim subiacet ordinacioni humane correpcionem fraternam quam Christus precipit Matth. XVIII cap. prohibere. Nec debet quis attemptare corripere suum prepositum, nisi propter defectum notorium, quem dicere debet ecclesie, quando prepositus notorie excidit a racione patris et pastoris. Quando scilicet nec gignit nec fovet subditum verbo Dei, tunc enim est tam expers racionis patris quam expers est quilibet a quocumque patris opere alienus; unde peccant qui mendaciter tales patres nominant vel pastores. Sed ut procedam minus intricabiliter et remocius a verbis scandali, securius servo me m verbis generalibus et condicionalibus, que ad auditorium et personam rei debent faciliter applicari efficaciter ad errantem, ut nullus papa nisi forte sibi conscius imponeret sibi raciones declaratas superius convenire autonomatice pseudopape. Unde non evidencius posset quis scandalizare se ipsum, quam sibi applicare sine pluri data evidencia verbum huiusmodi generale. Sic enim exierunt incipiendo a senioribus adulteram accusantes Joh. VIII. Sic et sacerdotes et Pharisei cognoverunt quod Christus de ipsis diceret in suis parabolis, Matth. XXI. Quod si probabiliter cognovero, quod predicans applicat ad me verbum huiusmodi generale, examinabo primo veritatem sentencie, secundo utrum in hoc sum conscius michi ipsi. Et tercio festinanter instar me ipsum corrigere et reddendo Deo gracias verba generalia nitar equaliter tollerare, quia nimis ostendunt suam stulticiam, qui ex talibus verbis communibus [p. 135] convincunt illegitimam correpcionem vel scandalum, verumtamen sciens peccatum quantumcumque alti prepositi esse notorium et periculosum ecclesie, debet ex fervore spiritus peccatorem quem credit aliunde non corrigi publice arguere cum Johanne, ut patet Mar. VI de Herode; oportet tamen in talibus quod homo a se ipso correpcionem incipiat et pura intencione procedat et utrobique sensui legis Domini innitatur, pro cuius exposicione nullus fidelium offendetur, ut patet de Paulo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 133.26: Duty of reproving superiors.
- 134.15: Our attack on the pseudopope is not personal except to any who feels that it fits him.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 133: *concomitanter* [NW]
  - 134: *corripere* [R3]
  - 134: *condicionalibus* [NW]
  - 134: *efficaciter* (W1: efncaciter -> efficaciter (scans: efncaciter | eincaciter | efficaciter | efncaciter)) [OVERRIDE-SCAR]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Causes ot Peter's primacy. (135.13).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 133:
io. AB in marg. : Ad 2. 26. AB in marg. : Ad tercinm. 27. so-
lummodo ; cod.: sodo. 3o. AB in marg. : Corripere potest subditus pre-
positum.
32. Decr. Greg. IX, Lib. V, tit. XXXII, cap. 2.

p. 134:
i3. B: patres deest. i6. B: et decst. 17. B: et rei. 16. Codd.

p. 135:
10. pro cuius. Codd.: procius. 22. A in marg. : 2. 26. A in
marg. : 3. 29. B : infantes qui magis deest.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 133: Cum ex iniuncto
p. 135: Ouimaior est vestrum, fiat ut minor.
```

---

## Chunk 07-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "135.13–138.31"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "789 words; 724 unanimous or majority-real; 52 settled by vote (R2 35, R3a 10, R5a 7); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n196–n199 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 1: [TITLE]

## ¶1 · 135.13–135.21

> [p. 135] Sed ulterius transcurrendum est per argumenta capta ex fide evangelii, ut sciatur quam sentenciam reportant in testimonium veritatis. Ex primo itaque argumento capto a diffinicione Christi Luce XXII elicitur, quod preeminencia Petri in alios non stat in honore, in dominatu vel gloria seculari sed in omnino oppositis. Patet primo ex hoc quod stat in fidei sinceritate et humilitate et in servitute, ut patet ex dictis.

[ENGLISH]

## ¶2 · 135.22–135.24

> [p. 135] Similiter primatus Petri stat in preeminencia sequendi Christum in moribus; Christus autem omnia predicta abnuit et condiciones oppositas acceptavit.

[ENGLISH]

## ¶3 · 135.25–136.14

> [p. 135] Similiter, Luce XXII; 26 sic loquitur: Qui maior est vestrum, fiat ut minor. Constat autem ex doctrina prima Petri II quod maiores in ecclesia debent esse quasi modo geniti infantes, qui magis alienati sunt ab honore, a dominatu vel gloria seculari; debet autem primas post Christum esse minor, ad serviendum flexibilior, ut dicitur [p. 136] Matth. XX. Sic enim Christus fuit omnium hominum servus necessarior ac mitior, ut docet Ambrosius epistola, et Augustinus De Verbis Domini sermone VIII: hominem coaptatum unam fecit Deus cum servo personam. Voluit inquam regnum suum conquirere per humilem pacienciam iniurie, et cetera arma virtutum et non per gentilem dominatum, quem apostolis suis prohibuit, sed reverti voluit ad iudicium in celesti Dominio glorioso. Unde infidelior, horribilior et stulcior non posset fieri argucia quam ex vicaria primatus Petri et Christi eius magistri, arguere vel fundare in eorum vicariis triplicitatem predictam mundanam, cum omnino contrarium inferatur.

[ENGLISH]

## ¶4 · 136.16–137.31

> [p. 136] Pro declaracione vero istius materie adduxi alia multa testimonia de Christo et unum de beato Bernhardo oportet repetere. Nam libro secundo ad Eugenium ita scribit: Quid dimisit tibi sanctus apostolus, quod habeo, hoc tibi do. Quid illud? Unum scio: non est aurum neque argentum, cum ipse dicat: argentum et aurum non est michi. Si habere contingat, utere non pro libitu sed pro tempore. Sic eris utens illis quasi non utens. Ipsa quidem ad animi bonum non spectant, cuiusmodi sunt divicie, nec sunt per se bona nec mala, usus autem horum bonus, abusio mala, sollicitudo peior, questus turpior. Esto ut alia racione hec tibi vendices sed non apostolico iure. Nec enim ille tibi dare potuit quod non habuit; quod habuit hoc dedit, sollicitudinem ut dixi super ecclesias. Numquid dominacionem? [p. 137] Audi ipsum: non dominantes, ait, in clero, sed forma facti gregis. Et ne dictum sola humilitate putes non eciam veritate, vox Domini est in evangelio: Reges gencium dominantur eorum etc. Et infert: vos autem non sic. Planum est, apostolis interdicitur dominatus. Et igitur tu tibi usurpare audes aut dominans apostolatum aut apostolicus dominatum. Planum est, ab utroque prohiberis. Si utrumque simul habere voles, perdes utrumque. Alioquin non te exceptum de illorum numero putes, de quibus Deus sic conqueritur: Ipsi regnaverunt et non ex me, principes extiterunt et non cognovi eos. Iam si regnare sine Deo iuvat, habes gloriam sed non apud Deum, at si interdictum tenemus audiamus edictum, id est qui maior est vestrum, fiat sicut minor et qui precessor est sicut qui ministrat, forma apostolica hec est, dominacio interdicitur, indicitur ministracio, que et commendatur exemplo ipsius legislatoris, qui secutus adiungit, ego autem in medio vestrum sum tamquam qui ministrat. Ecce quam breviter iste sanctus et quam plane dilucidat sentenciam sepedictam tamquam sequentem formaliter ex scriptura, et revera dampnare, hereticare vel impugnare sentenciam tam sancti, tam devoti, tam profundi atque subtilis theologi sicut fuit beatus Bernhardus ab ecclesia canonizatus et in celo cum angelis gloriosus propter istam sentenciam quam verbo docuit et exemplo, videretur nimis ceca presumpcio et specialiter in materia fidei quam dictavit tam lex Christi quam lex naturalis.

[ENGLISH]

## ¶5 · 137.32–138.22

> [p. 137] Constat quidem ex dictis sanctorum et testatur canon XXIV q. Ill cap. Heresis, quod qui aliter [p. 138] intelligit scripturam sacram, quam Spiritus Sanctus flagitat, adiuncta pertinacia, est expresse hereticus. Iste autem sanctus intellexit et expressit tam opere quam sermone quod non licet sacerdoti Christi, specialiter Romano pontifici, seculariter vel civiliter dominari, in tantum quod papatus et vera secularis dominacio qualis est licita in laycis formaliter contradicunt. Et virtute huius precepti vixerunt apostoli, sancti monachi et mendicantes exproprietarie, usque hodie dicentes tam vita quam verbo quod Dominus suis sacerdotibus hoc precipit; aliquos tamen voluit habere usum temporalium largius et alios striccius ex titulo elemosine secularium dominorum subducto seculari dominio. Unde credo beatum Bernhardum habuisse noticiam de toxico dominandi in Romano pontifice; et ideo dicit libro III ad Eugenium: Nullum tibi venenum, nullum gladium plus formido, quam libidinem dominandi; non enim sequitur ex primo testimonio scripture Luce XX, quo docetur Petrum super alios preeminere sed eius oppositum.

[ENGLISH]

## ¶6 · 138.23–138.31

> [p. 138] Et ideo libro II declarans pape officium: Si hec facis, inquit, honorificas ministerium tuum, non mediocris est iste principatus. Hoc enim est extirpare malas bestias a terminis tuis, quo greges tui securi in pascua educantur. Domabis lupos sed ovibus non dominaberis. Pascendas utique non premendas suscepisti. Timebat enim iste sanctus ex dominacione illius sedis subversionem vocate ecclesie.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 135.13: Causes of Peter's primacy.
- 135.22: Humility.
- 135.25: Mildness.
- 138.3: He taught that the Pope should not exercise secular rule.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 135: *CAPITULUM SEPTIMUM.* [HEAD]
  - 135: *acceptavit* (print has line 25 acceptavit, missing from main scan; print has v) [INS?]
  - 135: *26* [R3]
  - 135: *sic loquitur* (one token covers two printed words) [R3]
  - 135: *Qui maior* (one token covers two printed words) [R5]
  - 136: *habeo* [R4]
  - 136: *illis* [R3]
  - 136: *divicie* (print has v) [R3]
  - 137: *Deus* [R3]
  - 137: *audiamus* (15 is the line number) [R4]
  - 137: *hereticare* [NW]
  - 138: *scripturam* [THIN]
  - 138: *quam* [THIN]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Causes ot Peter's primacy. (135.13).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 135:
10. pro cuius. Codd.: procius. 22. A in marg. : 2. 26. A in
marg. : 3. 29. B : infantes qui magis deest.

p. 136:
7. Codd.: veritatum. 18. A in marg. : Nota. Nota beatwn Bernar-
dum contra dominacionem cleri sed non contra temporalium possessionem
et appropriacionem evangelicam; B in marg. : Quid dimisit Petrus suis
successoribus. 23. utere. Codd.: vere. 24. Codd. : malicia temporis.
3. St. Augustini Opp. tom. V, p. 373. 19. Cap. VI. Opp.
(Migne) I, 748.

p. 137:
7—8. Codd. : aut dominus .... aut apostolatus dominium. 18. Codd. :
que et commendatur deest. 19. Codd. : adiungi.

p. 138:
18. Cap. I, p. 769. 24. Cap. VI, p. 749. Recte: ministerium
tuum et ministerium te.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 135: Ouimaior est vestrum, fiat ut minor.
p. 136: Qitid dimisit tibi sanctus apostolus, quod hdbeo, hoc tibi do. | Quid illud? i\ Unum scio: non est aurum neque argentum, cum ipse dicat: argentum et aurum non est michi. Si habere contingat, utere non pro libitu sed pro tempore. Sic eris utens iliis quasi non utens. Ipsa quidem ad animi bonum non spectant, cuiusmodi^ sunt divicie, nec sunt per se bona nec mala, usus autem horum bonus, abusio mala, sotlicitudo peior, questus turpior. Esto ut alia racione hec tibi vendices sed non apostolico iure. Nec enim ille tibi dare potuit quod non habuit; quod habuit hoc dedit, sotli- | citudinem ut dixi super ecclesias. Numquid domina-
p. 137: cionem? Audi ipsum: non dominantes, ait, in clero, sed forma facti gregis. Et ne dictum sola humilitate ptites non eciam veritate, vox Domini est in evangelio: Reges gencium dominantur eorum etc. | Et infert: vos autem non sic. Planum est, apostolis interdicitur dominatus. Et igitur tu tibi usurpare audes aut dominans apostolatum aut apostolicus dominatum. Planum est, ab utroque prohiberis. Si utrumque simul habere voles, perdes utrumque. loAIioquin non te exceptum de illorum numero putes, de qttibus Deus sic conqueritur: Ipsi regnaverunt et non ex me, principes extiterunt et non cognovi eos. Iam si regnare sine Deo iuvat, habes gloriam sed non apud Deum, at si interdictum tenemus | audiamus edictum, id est qui maior est vestrum, fiat sicut minor et qui precessor est sicut qui ministrat, forma apostolica hec est, dominacio interdicitur, indicitur ministracio, que et commendatur exemplo ipsius legislatoris, qui secutus adiungit, | ego autem in medio vestrum sum tamquam qui \ | qui aliter
p. 138: intelligit scripttiram sacram, qtiam Spiritus Sanctus flagitat, | Nullum tibi venenum, nullum gladium plus formido, quam libidinem dominandi; | Si hec faciSf | honorificas ministerium tuum, non mediocris est iste principatus. Hoc enim est ex- | tirpare malas bestias a terminis tttis, quo greges tui securi in pascua educantur. Domabis lupos } sed ovibus non dominaberis. Pascendas utique non premendas suscepisti.
```
