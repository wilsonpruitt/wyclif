# Translation brief: potestate-pape 05-e–06-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-05-e.md chunks/potestate-pape/wyc-potestate-pape-05-f.md chunks/potestate-pape/wyc-potestate-pape-06-a.md` once and fix what it reports.
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

## Glossary (the 264 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
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
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

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
| sumitur pro | is taken for | Supposition language. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| ociatores | men of leisure | Ruled 2026-10-02 (201.27). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
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
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
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
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| exequie | exequies | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 05-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-05-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-05-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "93.31–97.12"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 80.23); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "763 words; 725 unanimous or majority-real; 26 settled by vote (R2 12, R3a 3, R5a 10, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n154–n158 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 5, part 5: [TITLE]

## ¶1 · 93.31–96.20

> [p. 93] Et quantum ad beatos Silvestrem, Gregorium et similes dicitur quod cum pena habuerunt tantum tumultum temporalium exproprietarie per [p. 94] medias personas distribuendo bona ecclesie, ipsi autem servabant vitam humilem et pauperem in se ipsis, quod si scivissent peccatores sequentes sic obtinuisse illas divicias, firmiter credo quod ipsas pro se et posteris reliquissent. Et stultus est qui sompniat et defendit quod non in hoc venialiter peccaverunt. Non enim repugnat quod remisse in gracia occuparunt illud officium sicut meritorie, sed defectu veniali occuparunt temporalia et in posteris propter profundiorem maliciam in occupacionem mortalem et simpliciter Deo odibilem est perversa. Periculum igitur foret trahere in exemplum vel consequenciam modum agendi venialiter culpabilem, quia sic ex pietate doceremus cum Petro gentes iudaizare, propter quod fuit a Paulo, ut patet capitulo II ad Gal., reprehensus. Et credo quod longe maius peccatum fuit in dotatis episcopis ex hoc quod dotacionem huiusmodi admiserunt, Caveamus igitur exempla capere sanctorum ab operibus eorum mixtim laudabilibus et venialiter culpabilibus secundum disparem racionem, quia nescimus si in nobis sit predestinacionis gracia vel excusandi racio a mortali. Ideo debemus sequi secure sanctum sanctorum et virtutes in membris suis, nec non in operibus sic mixtis debemus colare racionem laudabilem et illi inniti racione alia separata. Et credo quod ignorancia huius sentencie fecit multos a via Domini declinare. Noverunt sophiste quomodo eadem res est simul laudabilis et culpabilis secundum disparem racionem, ut Petrus et operacio sua est laudabilis, quia sub aliquo gradu bona moraliter, et est cum hoc culpabilis et reprobabilis propter defectum habundancie [p. 95] virtutis et fervorum amoris. Sic enim sumus omnes in vita continue increpandi; et talis tepiditas, ut dicitur Apocalipsis III, 16 causat vomitum, quia indubie inducit plurimos in mor tercio arguitur contra dicta per hoc quod iuxta sepe et publice dicta a me alia est potestas iurisdicionis et alia ordinis; sicut declarat dominus Ardmacanus libro VII De Questionibus Armenorum VI capitulo, ubi dicitur, quod potestates ordinis in omnibus sacerdotibus sunt equales. Sed potestates regiminis variantur, cum Petro et suis successoribus qui soli habent universalem potestatem regiminis data est sic potestas super universalem ecclesiam; et consonat factum ecclesie cum multis legibus de regimine vel iurisdicione loquentibus; oportet igitur docere quod officium Petro conveniat et quid sit ab eo vetitum. Quantum ad illud non discucio, quid fiat de facto, sed quid auctoritate scripture vel racione debet fieri. Unde Deum contestor, nec ex scriptura nec ex sanctis doctoribus fundari video istius iurisdicionis extensionem tam vanam, sed ex ritu gentilium sicut institucionem pape et cardinalium introductam. Concedo igitur distinccionem predictam. Pro quo notandum quod multi sacerdotes et episcopi habent dispares potestates. Sed potestas ordinis, que est par in quolibet sacerdote, est potestas quam clericus habet in quantum est Christi sacerdos, quam oportet esse communem et quodlibet eius iudicium est potestas sic remissa, qua sacerdos non potest carere manente suo sacerdocio; et illa potestas non potest maius et [p. 96] minus suscipere. Et preter illam est dare aliam maneriem potestatis iurisdicionis sive regiminis, que fuit dispar in diversis apostolis et continue est dispar in diversis episcopis. Sed illa non attenditur penes institucionem humanam, sed Penes hoc quod Deus ordinavit episcopum intensius vel remissius debere regere maiorem partem ecclesie vel minorem. Et non attenditur in isto ad humanum primatum sed ad quantitatem potestatis quam Deus attribuit ad edificandum suam ecclesiam, et (ut dictum est) omnes habuerunt commixtam potenciam super eodem populo sine repugnancia, Petrus primatum non propter amplitudinem iurisdiccionis sed propter fervorem dileccionis Christi et sue ecclesie. Nam ut credo ceteri extensius laborarunt, ita quod tur pissime et inevidentissime arguitur quod, si Petrus habuit primatum inter apostolos, tunc ille habuit iurisdiccionem universalem tocius ecclesie, et alii particularem a Petro et eius vicariis limitatam.

[ENGLISH]

## ¶2 · 96.21–96.24

> [p. 96] Tres tamen evidencias innuit dominus Ardmacanus ad roborandum istam arguciam, primo quod oportet aliquem capitaliter sic regere ex auctoritate domini, sed ille potissime foret Petrus.

[ENGLISH]

## ¶3 · 96.25–97.5

> [p. 96] Ad illud dicitur et in futurum declarabitur quod hodierna gentilis iurisdiccio fuit preter autoritatem Domini ex superbia introducta, quia iuxta decretum beati Jeronimi XCV distinccione: Olim ecclesia regulabatur in principio communi sacerdotum consilio, sicut fuit tempore apostolorum subducta dominacione. Et ad docendum nos istam sentenciam credo Spiritum Sanctum ordinasse, quod in lege Christi preponeretur quandoque [p. 97] ante Petrum alius Christi apostolus, ut Gal. II Paulus preponit Jacobum fratrem Domini et Act. VIII miserunt apostoli Petrum et Johannem Samariam. Et Act. II docetur eleccionem Matthie ex communi apostolorum consilio processisse.

[ENGLISH]

## ¶4 · 97.6–97.12

> [p. 97] Secundo arguitur per hoc quod Petro singulariter dicta sunt et concessa multa a Dommo; oportet igitur quod illa dicant m Petro quandam preeminenciam, sed nullam pertinencius quam regimen universale predictum; et illud multum notatur, quod soli Petro dictum est Math. XVI, 19: Tibi dabo claves regni celorum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 93.31: Examples of Silvester and Gregory.
- 94.9: They sinned venially.
- 94.24: Let us follow the Holiest and the virtues shown in his members,
- 95.5: I am said to have admitted the distinction between powers given by orders and powers of government; and the pope is said to have the latter over the whole Church.
- 95.19: I do not dispute the fact, but deny the authority.
- 95.27: Every priest of Christ has the same power by his orders.
- 96.3: There is a varying power of government. but in thus Gods ordinance should be followed.
- 96.21: Fitzralph argues that there must be a head to rule the Church.
- 97.6: It is said that special powers were given by Christ to Peter,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 94: *sed* [R3]
  - 94: *habundancie* (hyphenated habun-/dancie; main token covers whole word) [THIN]
  - 95: *alia* [R3]
  - 95: *sacerdotibus* [R4]
  - 95: *illa* [R3]
  - 96: *que* [R3]
  - 96: *fuit* [R4]
  - 96: *est* [R3]
  - 96: *illa* [R3]
  - 96: *tur* (print: tur | pissime, turpissime split by the folio bar (184ᵈ); main token holds the first part) [NW]
  - 97: *illa* [R3]
  - 95: *mor* (S-split: mor- | tale at line end; hyphen not carried, other half tale on next line) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 93:
io. quin; codd. : quando. i3, 14. B: modi deest. 23. Godd.: do
6. I. Petr. V, 3. 10. Cf. Hussii Opp. 2i2b.

p. 94:
3 Codd. : scissent. 7. A in marg. : Sancti suscipiendo dotacionem
venialiter peccaverunt. 3i. B: et culpabilis deest.

p. 95:
3. Codd.: 30 causat. 8. A in marg. : Nota de duplici potestate
scilicet iurisdiccionis et ordinis. 9. B: Archidmanus. 27. AB in
marg: Potestas dispar in episcopis et sacerdotibus.

p. 96:
6. B: quod Deus est. i3. AB in marg. : Petrus quomodo primatum
habuit inter apostolos. 21. A in marg. : 1.
28. Vide supra pag. 92.

p. 97:
6. A in marg. : 2. i5, 16. A : Jiunt humilior. 20. A: ethincfuit.
23. A in marg. : Petrus habuit primatum saper apostolos.
23. St. Augustini Opp. tom. II, 85.
De Pote6tate Pape. 7
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 93: mentum superioritas non est a Deo et tunc indubie est a dyabolo. | seniores et prepositi non sint dominantes in clero sed forma gregis. | loaurum non est michi. | Ouod autem habeo, hoc tibi do,
p. 94: merl ^ orle ^ | scissent. venialiter peccaverunt.
p. 95: states orchnts tn omntbns saceraotwus sunt equalcs.
p. 96: Olim ecclesia regutdbatur in principio communi sacerdotum consilio,
p. 97: Tibi dabo claves regni celorum. | Tibi dabo claves regni celornm,
```

---

## Chunk 05-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-05-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-05-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "97.13–102.24"
divisions: "cap. 5 (heading 'CAPITULUM QUINTUM.' at 80.23); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1166 words; 1076 unanimous or majority-real; 68 settled by vote (R2 45, R3a 13, R5a 8, R6a 2); 22 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n158–n163 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 5, part 6: [TITLE]

## ¶1 · 97.13–98.26

> [p. 97] Quantum ad illud, patet quod turpiter petitur quod probaretur, quia, ut patet in parte ex dictis, propter spiritualem primatum, quo ceteris fuit humilior, servicior et ecclesie Christi amancior, et non propter aliquam dignitatem mundanam Deus dedit sibi primatum ecclesie, et sic fuit ad laborem et sollicitudinem suam, quod habuit illam preeminenciam, et hoc fuit obligare obedire minoribus. Et hinc sumitur racio, quare sic meruit paciendo humiliter reprobacionem Apostoli, de qua Gal. II, ut declarat Augustinus Epistola IX. Quilibet igitur apostolus habuit regimen quodammodo universale viantis ecclesie, sedPaulus Petro extensius. Et quantum ad illud dictum Petro Mar. XVI Tibi dabo claves regni celorum, patet quod fuit dictum in persona ecclesie sacerdotum, quod aliter nos non gauderemus hoc privilegio virtute horum verborum Domini; unde miror quod aliquis habens fidem scripture retorqueret ex isto verbo singulare privilegium Romani pontificis in solvendo. Hoc enim fuit singulariter [p. 98] dictum Petro tamquam generali procuratori ecclesie sacerdotum et non tamquam singulari recipienti pro se solum hoc privilegium, sed limitatum et diffinitum fuit a Christo preter ordinacionem humanam quomodo sacerdotes sibi habiles privilegio isti participent. Et ista est sentencia Augustini super X, Omelia CXXIV: Petrus, inquit, apostolus propter apostolatus sui primatum gerebat figurata generalitate personam ecclesie; quod enim ad ipsum proprie pertinet, natura unus homo erat gracia christianus, habundanciori gracia unus idemque primus apostolus. Sed quando ei dictum est: Tibi dabo claves regni celorum, et quodcumque ligaveris super terram, erit ligatum et in celis, et quodcumque solveris super terram, erit solutum et in celis, universam signat ecclesiam, que in hoc seculo diversis temptacionibus ut ymbribus et tempestatibus quatitur, et non cadit, quoniam fundatur super petram; unde Petrus nomen accepit, que fundatur in Christo. Horrenda itaque et infidelis seduccio simplicium laycorum foret ex isto textu evangelii episcopum irracionabiliter reservare sibi potenciam ad ligandum et cecare populum cum laxacione potestatis proprie et suspensione potestatis alterius, ut patet in materia de sacramento penitencie.

[ENGLISH]

## ¶2 · 98.28–99.34

> [p. 98] Sed tercio nimis leviter sollempnisatur quod Paulus accepit autoritatem et licenciam a Petro ad predicandum in gentibus ex textu Gal. II, 9: Cum cognovissent) inquit, graciam que data est [p. 99] michi, Jacobus et Cephas et Johannes, qui videbantur esse columpne, dexteras dederunt michi et Barnabe societatis, ut nos in gentes, ipsi vero in circumcisionem. Sed notet rogo arguens ex isto textu, quomodo Paulus triennio ante illud tempus Sine eorum auctoritate predicavit in gentibus, de quo non cepit penitenciam vel reprobacionem a Petro, quia Paulus cicius illud insereret quam reprehensionem Petri. Notet secundo quomodo communi consilio et auctoritate Christi, ut dicit Jeronimus, locuti sunt apostoli in ecclesia primitiva. Petrus autem ex decreto cetus apostolici fuit paracior ad laborem, ut patet Act. VIII, 14 ubi dicitur, quod apostoli, qui erant Jerusolimis, miserunt Petrum et Johannem in Samariam ad confirmandum populum, qui prius receperat verbum Dei; ubi non notatur Petro humana dignitas, quod apostoli eum miserunt ad illud officium, sicut papa non acceptaret sibi dignitatem et honorem, quod cardinales mitterent eum et unum episcopum socium ad convertendum unam gentem. Et patet quod minus inevidenter eliceretur ex isto textu quod Petrus et Johannes cepissent autoritatem ab apostolis qui residebant Jerusolimis; non enim est magna auctoritas cursorem mitti ad operam. Sed tercio notet falsarius verba textus Apostoli et videat si sequatur: Jacobus, Petrus et Johannes dederunt Paulo et Barnabe dextram societatis, igitur dederunt eis autoritatem sive licenciam; dederunt, inquam, eis bonam societatem, gaudentes quod dedit eis Deus graciam predicandi gentibus, sicut Petro Judeis, ymmo precepit separare sibi Paulum et Barnabam ad illud officium.

[ENGLISH]

## ¶3 · 100.1–100.22

> [p. 100] Unde nimis magna stulticia foret apostolos presumere dare illis vasis licenciam, postquam cognoverunt quod Deus prius dedit ad hoc licenciam et preceptum. Maniaca, inquam, foret stulticia, nos dare licenciam angelis ad exequendum suum officium, quod Deus preceperit. Sufficit igitur Christi auctoritas sive licencia, qua cognita licet rogare ethortari ad illam sedule exequendum. Unde oportet notare pro intellectu istius historie apostolice benedicte, quomodo Apostolus incipit calculare a conversione sua; de quaAct...: tunc enim segregatus fuit ex utero matris sue synagoge, pro cuius defensione infideliter laboravit; et hinc vocat se ipsum abortivum prima Cor. XV, 8: Novissime, inquit, tamquam abortivo Christus visus est michi, quia de matre sua synagoga prodiit ipsa ocasione illius exitus pereunte, quia, ut dicitur Act. IX, 10: Mansit cum discipulis diebus aliquot; quos absit credere fuisse apostolos, et continue invalescebat confundens Judeos propter amorem indubie, quo dilexerat matrem suam.

[ENGLISH]

## ¶4 · 100.23–101.12

> [p. 100] Ex istis colligitur, quod sicut omnes apostoli preter Scarioth erant socii sibi obedientes, honore invicem prevenientes et superiores invicem arbitrantes, qui inmediate a Deo potestatem et licenciam ad evangelizandum acceperunt; sic debet esse de sacerdotibus et episcopis ecclesie iam instantis, ita quod disparitas ditacionis societatem et amiciciam evangelicam non dissolvet, quia per idem Christus per possibile reconversans nobiscum, observans scolam suam ex integro sicut olim, non haberet papam vel dotatos episcopos socios vel amicos sed dominos, quibus solveret tributum sicut olim fecit cesari. Non enim consonat [p. 101] scole sapientis habere familiam tam discordem a capite quod monstruose et contra policiam humanam servicium ab eis exigeret, et in propria familia doctrine capitis repugnaret, quod si veniens in mundum illum non invenerit episcopos in conversacione sibi consentaneos et amicos, quomodo laudaret eos ut fideles vicarios, nec ut fideles negociatores in die iudicii beatitudine premiandos; a multis creditur quod nullos vel paucos inveniet, in quibus scintilla sue conversacionis sit propter antichristianam declinacionem ad seculum exemplata.

[ENGLISH]

## ¶5 · 101.13–101.22

> [p. 101] Si autem queritur quid nos sacerdotes debemus facere, dicitur indubie quod debemus in conversacione sequi ipsum quantum sufficimus. Sic quod primo abraderemus quantum sufficimus omnem occupacionem mentis aut corporis, que fuerit inpertinens aut contraria officio sacerdotis. Secundo vero poneremus omnem sacerdotalem potestatem quantum sufficeremus efficaciter in effectum, et omnium istorum exemplar et specula debet esse dominus Jhesus Christus.

[ENGLISH]

## ¶6 · 101.23–102.24

> [p. 101] Ex istis sequerentur tres conclusiones graciose ecclesie, primo quod papa non intromitteret se iudicando de negocio seculari, quia est alienum a sacerdotali officio iuxta illud II Thim. II, 4: Nemo militans Deo implicat se negociis secularibus, Secundo quod renueret omnem dotacionem cesaream, cum ex facto Christi et Petri patet quod foret impertinens papali officio; et per consequens omnes alii episcopi ut sit conformitas ad caput, et revera necessarior foret conformitas paparum sequencium in ista pauperie ad Christum, sicut [p. 102] Petrus et alii sub quibus crevit ecclesia se Domino conformarunt. Tercio quod papa et omnes alii episcopi debent evangelizacione, oracione et sancte vite exemplacione assidue pascere oves Christi; patet ex officio ter limitato Petro Johannis ultimo. Unde Augustinus Epistola CXLI ad Paulinum notat, quomodo in textu Apostoli Ephe. IV, ii officium pastoris et doctoris iunguntur: Pastores, inquit, et doctores quos maxime discernere voluisti eosdem puto esse et non alios pastores et alios doctores intelligamus; et ideo cum predixisset pastores, subiunxit doctores, ut pastores intelligerent ad officium suum pertinere doctrinam. Ideo vero non ait: quosdam vero pastores et quosdam doctores, ut superiori locucionis genere, sed quosdam pastores et doctores, tamquam unum aliquid duobus nominibus amplexus est, quosdam, inquit, pastores et doctores. Et sic spoliatis superfluis, pateret quis episcopus remaneret habilis ex thesauro Domini et quis remaneret vacuus prescisso organo et officio laycali; et forte reperirentur plures pastores cesarei quam fideles vicarii domini Jhesu Christi. Et utinam talis discernendi monstracio foret facta.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 97.13: Such primacy was given only because he was more loving and humble than the rest.
- 97.26: The power of the keys was given to him as representing the priesthood and confers no privilege on the Roman pontiff.
- 98.28: Paul did not accept authority or licence from Peter.
- 99.4: He had preached three years before he met Peter.
- 99.15: Peter was sent to Samaria by the apostles.
- 100.1: The apostles would not have given licence to one who had already received it of God.
- 100.23: The apostles consorted on terms of mutual service and honour.
- 100.30: So should our priests and bishops do.
- 101.1: If Christ were to revisit the earth, he would find few faithful servants.
- 101.13: We priests ought to devote ourselves entirely to priestly duties.
- 101.23: The pope should not judge in secular business.
- 101.29: He should give up all cesarean endowments.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 97: *celorum* [R4]
  - 98: *figurata* [R4]
  - 98: *quodcumque* [NW]
  - 98: *in* [R3]
  - 98: *quodcumque* [R4]
  - 98: *Sed* [R3]
  - 99: *Jacobus* [THIN]
  - 99: *in* [R3]
  - 99: *miserunt* (15 is the line number) [R4]
  - 100: *abortivum* (print has v) [NW]
  - 100: *10* (old-style 10) [R4]
  - 100: *∅* (English side-note word) [R6]
  - 101: *policiam* [NW]
  - 101: *illum* [R3]
  - 101: *in* [R3]
  - 101: *iudicando* (25 is the line number) [R4]
  - 101: *implicat* [R3]
  - 102: *se Domino* (one token covers two printed words) [R4]
  - 102: *ut* [R3]
  - 102: *ut* [R4]
  - 102: *inquit* [R3]
  - 97: *virtute* (LEFT-nw: 30 is the line number) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference met Peter. . . (99.5).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 97:
6. A in marg. : 2. i5, 16. A : Jiunt humilior. 20. A: ethincfuit.
23. A in marg. : Petrus habuit primatum saper apostolos.
23. St. Augustini Opp. tom. II, 85.
De Pote6tate Pape. 7

p. 98:
4. B: diffinitum fuerit modo preter. 7. Codd. : super 10 omelie.
12. B: apostolus deest. 19. B: qui fundatur. 24. B: populum deest.
7. Augustini Enarr. in Psalm. CVIIT, tom. \\\ r 2 1 5, tom. \r,
702, 706. 20. Cf. Hussii Opp. 210".

p. 99:
(none)

p. 100:
(none)

p. 101:
i3. B in marg. : Sacerdotes quid debent facere. 23. graciose ;
Codd. : gloriose ; A in marg.: prima conclusio. 26. B: // before Tim.
deest. 28. B in marg.: Secundo.

p. 102:
2. B in marg.: 3. 6. AB in marg.: Pjstores debent esse doctores
ptebem exemplo et verbo docentes. n. intetligamus deest in codd. Addidi.
14. ait; B: agit. 2 5. A in marg. : C. VI. 26. B: facta deest.
6. St. Augustini E. ad Paulinum, Ep. CXLIX. Opp. tom. II,
pag. 5o8.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 97: Tibi dabo claves regni celorum. | Tibi dabo claves regni celornm,
p. 98: apostolus propter apostolatus sui primatum gerebat figurata generalitate personam ecclesie; | Tibi dabo claves regni celorum, et qnodcumque ligaveris super terram, erit ligatum et iu celis, et quodcunuque solveris | super terram, erit solutum et in celis, | Cum cognovissent) | graciam que data est
p. 99: michi, Jacobns et Cephas et Johannes, qui videbautnr esse columpne, dexteras dederunt michi et Barnabe societatis, ut nos in gentes, ipsi vero iu circumcisionem. | apostoli, qui erant Jerusoliuiis, | miserunt Petrum et Johannem in Samariam
p. 100: tamquam abortivo | Christus visus est michi, | Mansit cnm discipulis diebus aliquot;
p. 101: Nemo militans Deo implicat se negociis sectilaribus.
p. 102: et doctores qnos maxime discernere voluisti eosdetn ptito esse et non alios pastores | et alios doctores intelligamtis: et ideo cum predixisset pastores, subiunxit doctores, tit pastores ittteUigerent ad offcium suum pertittere doctrinam. Ideo vero non ait: qtwsdam vero pastores et quosdam doctores, tit superiori locticionis genere, sed qttos- | dam pastores et doctores, tamqttam untim aliquid dtiobtts nominibtis amplextis est, qtiosdam, inquii, pastores et doctores.
```

---

## Chunk 06-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "102.26–106.28"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 1 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "898 words; 861 unanimous or majority-real; 29 settled by vote (INS 1, R2 12, R3a 12, R5a 4); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n163–n167 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 1: [TITLE]

## ¶1 · 102.26–103.7

> [p. 102] Septima facta sentencia premittenda est hec: Sicut nullus apostolorum habuit tantam potestatem quantam habuit Christus humanitus, sic nec omnes [p. 103] pape habent tantam potestatem quantam habuit beatus Petrus vel alius Christi apostolus. Prima pars patet ex primogenitura Christi, que non potest communicari alicui eius vicario, cum tunc foret Deus et homo; cum igitur Christus habuit illam potestatem primogeniture humanitus, sequitur probandum.

[ENGLISH]

## ¶2 · 103.8–104.8

> [p. 103] Item, Christus habuit potestatem ponendi animam suam et iterum sumendi eam, ut patet johan. X, et sic non potuit aliquis eius vicarius, ut declarat Augustinus Omelia XLVII, ergo conclusio. Si enim Petrus haberet potestatem iterum sumendi animam suam prius positam, oporteret Petrum esse naturam terciam a corpore et anima cui inesset potestas resumendi animam sic positam, quod soli Deo potest competere, quia oportet dare subiectum cui competeret sic assumere, corpus vero exanime, non habet huiusmodi potestatem nec anima potest se ipsam assumere. Item, Christus habet per se potestatem ad redimendum genus humanum et ad principiandum graciam cuilibet alteri de suo genere, sed sic non habet aliquis eius vicarius, ergo conclusio. Antecedens patet per illud Johan. I, 14: Vidimus gloriam eius quasi unigeniti a patre plenum gracie et veritatis; de cuius plenitudine nos omnes accipimus, graciam pro Gracia. Sic igitur nullus alius potest mutari in Deum et hominem, ut sit per se fons gracie, a quo oportet omnem graciam datam ecclesie derivari, quia sic nec potest alius homo vel angelus Jhesu nostro in potencia, in plenitudine gracie vel preeminencia coequari. [p. 104] Nec hoc verti debet fideli in dubium, qui credit, quod nullus alius potest idemptificari personaliter Jhesu nostro, et quod natura divina ac humana idemptificantur in persona filii, licet ille nature infinite distinguantur, quodammodo necesse est divinitatem Christi in humanitatem eius ex vi unionis supereminenter incomunicabiliter aliis personis influere.

[ENGLISH]

## ¶3 · 104.9–106.10

> [p. 104] Nec sunt obiectus, quos ignari obiciunt digni memoria. Arguunt enim quidam: cum gracia et potestas date Christo humanitus sint tantum finite, derogaretur infinite divine potencie nisi posset eandem vel tantam ponere in quocumque. Et confirmacio est quod Christus sicut est eiusdem speciei nobiscum sic et quelibet gracia vel potestas quam habet humanitus. Stat igitur Deum ex omnipotencia sua augere potestatem vel graciam in Petro, quousque parificata fuerit qualitati in Christo. Tercio confirmatur per hoc quod omnem qualitatem, potest per se ponere et per consequens in quocumque subiecto voluerit et cum anima Petri sit tante capacitatis, ut anima Christi, Deus potest facere qualitates tales positas in aliis spiritibus informare. Sed et istud arguunt ex hoc quod verbum Dei potest quamcumque naturam humanam seorsum vel simul assumere; quo facto inessent sibi tanta gracia et potestas sicut Christus habet humanitus, igitur non posita illa unione Deus potest faciliter facere qualitates huiusmodi informare hominem non assumptum. Sed benedictus dominus qui nos liberavit de istis arguciis. Dictum est autem in materia de [p. 105] incarnacione, quod Christus non potuit aliam humanitatem assumere, verumtamen potuit facillime si voluisset, dictum est eciam quod ipse tam secundum corpus quam animam est eiusdem speciei cum quolibet alio fratre suo. Et dictum est tercio quod ex vi unionis ipostatice gracia, potestas et pulchritudo vel speciositas in Christo est alterius speciei quam aliqua qualitas consimilis nominis in alio homine potest esse. Et ideo incarnacio Christi perfecit totam universitatem creatam tam secundum individua quam universalia, cum multa talia aliter non fuissent. Sicut igitur individuum unius speciei licet infinitum creverit, non potest in toto parificari individuo alterius speciei, sic est de gracia Christi, de potestate, speciositate sue humanitatis. Qualitates autem multe, sicut patet de corporali pulchritudine, principiantur a relacione, ideo idem esset querere istas qualitates in alio homine et querere alium hominem qui simul sit Deus et homo. Ideo errant, qui nude arguunt idemptitatem specificam qualitatum ex idemptitate specifica subiectorum. Oportet enim principia rerum tendere ad maiorem unitatem quam sit in suis effectibus, cum summa unitas sit in primo principio et summa diversitas in sua universitate creata. Nec est michi sermo de qualitate que potest per se esse, quia certum est quod est dare unam naturam qualitatis, que non potest esse nisi informet substanciam, cum non sit nisi substanciam accidentaliter esse qualem. Et qui sompniant aliam ex vanitate subtilitatis circa sacramentum eukaristie, ultra hoc quod sciunt fundare in scriptura sacra, in antiquis sanctis doctoribus vel racionis efficacia, debilitant scolam Christi. Paratus sum tamen eis annuere si illud probaverint et non ante. Et credo quod scola possit aliunde occupari [p. 106] circa fidem scripture ut olim usque ad tubam novissimam, antequam rima ad fundandum illud in scriptura sacra in qua est omnis veritas sit reperta; et tamen, si foret utile, autor scripture non omississet illud inserere nec quatuor sancti doctores illud detegere neglexissent; unde oportet ecclesiam cavere ab huiusmodi novitate. Et colligi potest solucio ad tres predictas argucias; quomodo vel peccant in materia vel in forma. Et patet prima pars predicte sentencie.

[ENGLISH]

## ¶4 · 106.11–106.13

> [p. 106] Et secunda pars patet ex potestate faciendi miracula et ex potestate auctonzandi scripturam sacram et ex potestate edificandi ecclesiam.

[ENGLISH]

## ¶5 · 106.14–106.28

> [p. 106] Quantum ad miracula, patet quod cessant hodie in nostris episcopis, cum satis est post fidem in evangelio divulgatam ipsam impressam sanctis exhortacionibus confirmare. Cum igitur Deus non dat quicquam superflue, sequitur quod Deus non dat I nostris prepositis, ut olim dedit discipulis, potestatem faciendi miracula; et per consequens nunc non habent; hec autem fuit racio; quare Apostolus non miraculose sed per viam naturalis medicine sanavit Thimoteum, bonum regimen iniungendo. Utere, inquit; modico vino propter stomachum tuum et frequentes tuas infirmitates prima Thim. V. Sed communicando cum infidelibus convertendis per miracula exercuit illam potestatem; ut patet Actuum ultimo copiose.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 102.26: No apostle had all Christ's human powers, nor has every pope all the
- 103.1: powers of an apostle.
- 103.8: Christ could lay down his life and take it again, which only God can do,
- 103.20: Christ had power to redeem the human race.
- 104.1: This power was due to the two natures in Christ.
- 104.9: Some argue that God can give toa man the grace and power given to Christ's humanity.
- 105.1: In treating of the Incarnation we have said that Christ was of the same species with his brothers but by the hypostatic union his power and beauty were other than man's,
- 105.27: A quality cannot exist without a subject and those who fancy it may do so in the Host injure the Church.
- 106.11: The popes have not all the powers of the apostles.
- 106.14: Our prelates cannot work miracles, which are not needed now.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 102: *CAPITULUM SEXTUM.* [HEAD]
  - 102: *Christus* [R5]
  - 104: *idemptificari* [R4]
  - 104: *parificata* [NW]
  - 104: *illa* [R3]
  - 105: *parificari* [NW]
  - 106: *prima Thim* (one token covers two printed words) [R5]
  - 106: *V* [R5]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 24. I. Tim. V, 23. (106.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 102:
2. B in marg.: 3. 6. AB in marg.: Pjstores debent esse doctores
ptebem exemplo et verbo docentes. n. intetligamus deest in codd. Addidi.
14. ait; B: agit. 2 5. A in marg. : C. VI. 26. B: facta deest.
6. St. Augustini E. ad Paulinum, Ep. CXLIX. Opp. tom. II,
pag. 5o8.

p. 103:
1. B in marg. : Potestatem Christas habuit hamanitus quantam nullus
habuit apostolus. 14. lerciam ; sic in codd.; separatam. 27. Codd.:
accipimus.

p. 104:
2. B: et personaliter. 9. A in marg.: /. 12. Codd.: infiniti.
14. A in marg. : 2. 19. A in marg. : 3.
32. Cf. De Benedicta Incarnacione cap. XI, pag. 1 89 (?)

p. 105:
(none)

p. 106:
11. AR in marg. : Secunda pars. 24. A: utere inquam ; B m marg. :
inquit.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 102: et doctores qnos maxime discernere voluisti eosdetn ptito esse et non alios pastores | et alios doctores intelligamtis: et ideo cum predixisset pastores, subiunxit doctores, tit pastores ittteUigerent ad offcium suum pertittere doctrinam. Ideo vero non ait: qtwsdam vero pastores et quosdam doctores, tit superiori locticionis genere, sed qttos- | dam pastores et doctores, tamqttam untim aliquid dtiobtts nominibtis amplextis est, qtiosdam, inquii, pastores et doctores.
p. 103: gloriam eitis quasi unigeniti a patre \ plennm gracie et veritatis; de cuius plenitudine nos omnes accipimus, graciam pro Gracia.
p. 106: modico vino propter stomachum tnum et frequentes tuas infirmitates
```
