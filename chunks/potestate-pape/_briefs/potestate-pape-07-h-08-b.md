# Translation brief: potestate-pape 07-h–08-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-07-h.md chunks/potestate-pape/wyc-potestate-pape-08-a.md chunks/potestate-pape/wyc-potestate-pape-08-b.md` once and fix what it reports.
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

## Glossary (the 272 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| gleba | glebe | Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
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
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
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
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
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
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 07-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "160.5–164.32"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1084 words; 1031 unanimous or majority-real; 38 settled by vote (R2 21, R3a 9, R5a 8); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n221–n225 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 8: [TITLE]

## ¶1 · 160.5–161.31

> [p. 160] Ad octavam confirmacionem Johannis ultimo ubi Petrus singulariter recepit pastum ovium propter prerogativam amoris quo Christum et corpus suum dilexerat, vere concluditur primatus Petri predictus; quod si papa fuerit expers predicti amoris?, quid sibi et papatui? Nunquid credimus Christum acceptare personam Romani pontificis propter elecciones aut invenciones humanas, cum hoc quod sit in vita et moribus Christo contrarius? Deliramentum blasfemum foret sic credere. Unde videtur quod papa timens mentiri Domino, servaret se in limitibus paupertatis et apostolice a mundo alienacionis, in quibus Petrum Christus constituit; certum quidem est, quod si mentitur de Christo et Petro, dicens quod virtute successionis vicarie Petri habet ex ordinacione divina tantam excellenciam mundanam super ecclesiam, oportet quod finaliter super verecundo mendacio sit convictus, quia cum peccatum sit mentiri super discolum in materia impertinente fidei; quanto maius peccatum est mentiri super beatos et caput ecclesie in materia fidei, in qua tota ecclesia est seducta? Si igitur papa sit Petri vicarius procuret pro ecclesia instar Petri. Petrus autem procuravit assidue quod clerus Christi poneretur in statu exproprietario plus perfecto, quod si papa viis et modis nitatur degradare se et clerum ab illo statu evangelico ad statum secularem proprietarium, quis dubitat, quin sit infidelissimus proditor, preparans viam dyabolo? Quomodo superabit [p. 161] ecclesiam Christi cum mammona? Ille, inquam, vivit exproprietarie qui ob amorem Dei et securitatem a seculi seduccione relinquit omnem titulum humane securitatis de dotacione vel elemosina perpetua, spe suspensus in Deo, cui in superiori ecclesie officio inturpate et assidue famuletur; qualiter vixerunt prophete legis veteris. Christus cum suis apostolis et multi posteriores docti ab illis. Unde paulative recepit iste status gradus et sophisticabatur mille versuciis; nam tempore apostolorum dividebantur exproprietarii, alii ministrando mensis et alii pure intendentes evangelizacioni et aliis spiritualibus operibus sacerdotis, ut patet Act. VI. Secundo recepit clerus glebam et paulative dotaciones ulteriores ex titulo elemosine sine affeccione vel securitate humana, ymo rapinam et oblacionem talium cum gaudio susceperunt. Et sic fuit tempore Augustini et aliorum sanctorum, qui leviter peccaverunt. Sed cum istis surrepsit venenum dyaboli, quo cum expropriacione de facto propriacionem immiscuit in affectum, ut patet de Scarioth et multis sequentibus; secundo vero subintroducte sunt lacius cautele dyaboli, quibus elemosine occupate a notorie indignis sunt j ut hereditas avidissime vendicata. Et ad defendendum istam cleri avariciam sunt multe leges condite; in tantum quod oblito tali officio summe pro lucro temporali contenditur, et illud venenum est periculosius et extensius: ideo ve illis, qui fovent ipsum propter animum dominandi.

[ENGLISH]

## ¶2 · 161.32–163.8

> [p. 161] Sunt autem multi fuci, quibus discipuli Antichristi perturbant ecclesiam: querunt enim descripcionem vite exproprietarie et arguunt quod [p. 162] omnis homo vivit tam proprietarie quam exproprietarie, et sic inponunt magnam stulticiam pape Nicolao 111. et sanctis doctoribus, ymo nostris religiosis, cum dicunt quod non sit statuum istorum distinccio. Notum est, inquam, ex modo vivendi tam preterito quam presenti quod in alio statu est clerus postquam recepit dotacionem cesaream et in alio antequam fuerit sic dotatus, sicut in alio statu vivunt religiosi possessionati, eciam in alio fratres et alii, quibus non sunt elemosine perpetue humanitus sic affixe. Status igitur exproprietarius cleri est status cleri conversandi sine dotacione et elemosinacione perpetua secularium dominorum. Et status cleri proprietarius est status cleri conversando ex dotacione vel elemosinacione perpetua secularium dominorum, ut contingit personis vel ecclesiis cleri quibus appropriatur ecclesia vel annuus redditus ex pacto elemosinacionis perpetue; que omnia oportet originari ex auctoritate dominorum secularium, licet alii de clero ad hoc adiuverint et autorizare false finxerint. Et patet quod talis appropriacio sapit ingratam diffidenciam deChristo et suis legibus, qua homo superflue exponit se spinis et temptacionibus huius mundi. Status igitur exproprietarius non est non habere temporalia, sed habere ex puro titulo Dei sine autorizacione humana vel sollicitudine preter necessaria ad cleri officium. Nec obest perfeccioni illius status quod sint in illo statu pessimi, quia distinguitur a statu morum. Supposito igitur quod status ille sit alcior atque perfeccior, patet quod ille papa ingrate et infideliter ducit ecclesiam, [p. 163] quia nititur statum illum deprimere et alium exaltare. Non enim licet degradare clerum Christi a statu quem ipse instituit, sed status proprietarius in quo per papam confirmatur ecclesia est inferior statui quem Christus instituit, igitur non licet pape sine auctoritate divina a statu illo deicere clerum Christi. Petrus enim vel Paulus non habuit huiusmodi potestatem.

[ENGLISH]

## ¶3 · 163.9–163.21

> [p. 163] Item, papa tenetur specialiter stare pro privilegiis cleri sui, sed precipuum privilegium per quod distinguuntur cleri a laycis stat in hoc quod cleri serventur in statu exproprietario alciori, igitur hoc privilegium debet papa in se et subditis observare. Sic enim fecit Apostolus in quo locutus est Christus Heb. XIII, 5, 6 quando sic docuit: Sint mores sine avaricia, contenti presentibus; ipse enim dixit: Non te deseram neque derelinquam Ita ut confidenter dicamus: Dominus michi adiutor, et non timebo quid faciat michi homo. Que doctrina videtur expresse facere pro expropriacione contra propriacionem.

[ENGLISH]

## ¶4 · 163.22–164.32

> [p. 163] Item, papa non habet potestatem a Deo ad deteriorandum sed meliorandum ecclesiam, ut dicit Apostolus de se ipso II. Cor. X, 8: Si aliquid amplius gloriatus fuero de potestate nostra, quam nobis dedit Dominus in edificacionem et non in destruccionem. Et patet de racione; nam bonus dominus cesar semper Augustus non dat potestatem homini, ut dampnificet sponsam suam, magna autem dampnificacio foret statum tam altum et securum perdere sine equivalencia recompense; omnis enim mundana ditacio nonpotest attingere illum statum, cum maior ditacio plus abducit. Quomodo igitur autorizabit Christi vicarius [p. 164] ex fastu vel avaricia sic ducere gregem Domini per abrupta; cum posset securius in pascuis quas Christus instituit ducere oves suas? Securius dico propter dietam a morbis putridis preservantem, propter facilitatem tenendi ad pascua semper virencia preparantem, et propter securitatem insultus latronis et male bestie excludentem. Sic enim prudens paterfamilias seminat semen bonum non inter spinas, ne ex earum cremento frugum contrario suffocetur. Scit enim Deus infirmum statum sue familie quomodo prona est ad omnia morborum genera; ideo ut summus medicus iniungit dietam, que licet videatur antichristo Romano contraria, est tamen statui nostro fragili summe consona. Nam iniungit nobis quoad statum exproprietarium relinquere omnia; quod debemus nos curati facere; viventes pure de decimis, oblacionibus et privatis elemosinis laycorum. Et quia cum illo statu exproprietario stat elemosinarum abusio, ideo secundum beatum Jeronimum Petrus adiungit, quod perfectum est scilicet statum morum; dum dicit: Et secuti sumus te, sine hoc enim non potest esse salus fidelium. Sed illius; qui reliquit omnia, est status perfeccior quam remanentis in seculo, quia statui summo propinquior. Istam autem materiam decet cunctos fideles cognoscere, quia caucius cavebunt a lupis qui veniunt in vestimentis ovium; securius sequentur Christi vestigia dimissis viis Antichristi, et prudencius preparabitur ad discredendum suis blasfemiis et ab adhibendo sibi cultus indebitos et consensum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 160.7: It was for his great love that Peter was chosen to feed Christ's sheep,
- 161.9: How the Church gradually fell away from the life of true poverty.
- 162.1: Antichrist's disciples say there is no distinction between the States of poverty and possession.
- 162.14: Endowments make the difference, since they are maintained by secular authority.
- 163.9: The Pope should protect the privilege of the clergy, which is, to live the higher life.
- 163.22: Christ has given authority to no one to make the church worse.
- 164.11: God knows our weakness and enjoins the safer state.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 160: *amoris* [R3]
  - 160: *papatui* [NW]
  - 160: *ex* (20 is the line number) [R3]
  - 161: *elemosina* (hyphenated ele-mosina; main token covers whole word (5 line number glued)) [R4]
  - 162: *omnis* [THIN]
  - 162: *inponunt* [NW]
  - 162: *preterito* [R3]
  - 162: *presenti* [R4]
  - 163: *illum* [R3]
  - 163: *Ita* [R3]
  - 163: *quam* [R3]
  - 163: *recompense* (hyphenated re-compense; main token covers whole word) [NW]
  - 163: *illum* [R3]
  - 164: *pascua semper* (hyphenated pas-cua; main token covers it and the next word) [R5]
  - 161: *expropriacione* (LEFT-nw: print = expropriacione) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 22. Matth. XIX, 27. (164.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 160:
5. A in raarg.: Ad 8. i5. sic. Codd.: si credere.

p. 161:
1. A in marg. : Quid est vivere exproprietarie ; B in marg. : Viverc
exproprietarie.
De Potestate Pape. I 1

p. 162:
12. A in marg. : Nota ; AB in marg. : Status exproprietarius. Status
proprietarius. 25. A: spernis. 26. B: non beforo habere deest.
27. AB in marg. : Privilegium cleri datum a Christo. 3i. AB in marg. :
Status exproprietarius alcior.

p. 163:
16. 17. Codd.: contemptis presentibns. 24— 27. Codd.: Si aliquid —
destruccionem in marg. ; et patet ; B: et dces-t. 2Q. suam ; B: s.

p. 164:
10. suffocetur sc. semen. 14. Codd.: Romani. 29. Codd.: di-
missis aviis. 3o. preparabitur ; adde: via.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 08-a: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-a
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "165.2–169.31"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1023 words; 929 unanimous or majority-real; 77 settled by vote (DEL 1, R2 45, R3a 14, R5a 17); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n226–n230 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 1: [TITLE]

## ¶1 · 165.2–166.25

> [p. 165] Iam restat videre si oporteat regulariter Romanum pontificem esse papam et inmediatum ac proximum vicarium Christi in terris. Sed pro nomine pape, notandum, quod in scriptura sacra, si bene habeo, non exprimitur, sed est ab interieccione pape, quod admiracionem signat, derivatum. Unde eis convenit proprie qui in conversacione sunt admirabiles sanctitate; ad quem sensum Ihesus noster est summus papa possibilis, cum de eo scribitur Ysaias IX, 6: Et vocabitur nomen eius admirabilis, consiliarius, Deus fortis, princeps pacis. Olim autem vocati sunt quicumque sancti episcopi sancti pape. Unde epistola VIII jeronimi ad Augustinum sic loquitur: Domino vere sancto et beatissimo pape Augustino Jeronimus salutem. Item, Augustinus epistola XVIII ad Paulinum sic loquitur: Libros beatissimi pape Ambrosii credo habere sanctitatem tuam, eos autem multum desidero quos adversus nonnullos imperitissimos et superbissimos, qui de Platonis libris dominum profecisse contendunt, diligentissime ac copiosissime scripsit. Item, epistola X ad Aurelium scribunt Alpius et Augustinus: Domino beatissimo pape Aurelio; nec fuit iste Aurelius papa episcopus Romanus, ut patet epistola CXXXIX ad Generosum, in qua enumerat omnes episcopos a beato Petro usque ad Anastasium, qui tunc eandem [p. 166] cathedram rexit, et olim communiter vocabantur episcopi pape. Unde Bonifacius comes epistola CII scribit Augustino: Tue sanctitatis epistolam admonitu me terrificantem suscepi; etenim venerabilis papa: Si thorus ille legitimus pavidos habet accessus quo debet puniri supplicio qui divinas temerat raciones? Et epistola III sic in fine alloquitur idem Bonifacius Augustinum: Ora igitur, venerabilis papa, ut talis de inimicis sepe ulcio procedat, ymo ut recitat Archidiaconus: Greci vocant cunctos presbiteros papas; unde ra- cione dotacionis atque dominii baptizatus fuit terminus ut approprietur Romano pontifici. Sed quia non est vis in servacione termini, suppono quod specialiter significet illum episcopum, qui gerit altissime, simillime et propinquissime vicem Christi, sicut fecit Petrus post ascensionem, et regulariter dicimus quod faciunt Romani pontifices. Sed quia videtur mirabilis saltus et infundabilis a Christo ad totum genus Romanorum pontificum regulariter sic saltare, ideo multi adinveniunt vias varias ad istam ficticiam colorandum. Quidam autem dicunt hoc procedere per viam racionis, quidam per viam Petri successionis, et quidam per viam eleccionis.

[ENGLISH]

## ¶2 · 166.26–166.30

> [p. 166] Quantum ad primum fingit dominus Ardmacanus libro VII De Questionibus Armenorum racionem multiplicem, prima quia Roma est capitalis civitas christianismi, ideo decet quod capitalis episcopus ibi regat.

[ENGLISH]

## ¶3 · 166.31–167.12

> [p. 166] Sed quantum ad istam evidenciam videtur, quod accusat summum pontificem dominum Ihesum Christum, qui elegit Jerusalem passioni, et hoc [p. 167] videtur racionabile, quod ille qui venerat totum genus humanum redimere; in medio terre habitabilis ostenderet medicinam iuxta illud Psalmi LXXIII, 12: Deus autem rex noster ante secula operatus est salutem in medio terre. Secundum cosmimetras Jerusalem ponitur in medio habitabilis, locus autem ille foret convencior summo pontifici quam angulus Europe Roma, quia aliter Christus indubie non taliter elegisset; potissime cum tempore Christi et Augusti Cesaris fuit Roma in medio florum sui dominii; et imperator minus impius quam sequentes tempore apostolorum.

[ENGLISH]

## ¶4 · 167.14–167.31

> [p. 167] Iterum videtur quod racio ista, cum stat continue, accusat papas sequentes, qui m maiori parte Romam non rexerant, sed incrassati quieverunt Avinione; et cum pocior racio nunc subesset, eo quod ille locus imperii dicitur esse de pape dominio; et sic remanet multiplex racio; primo et principaliter regendi hunc populum; cum crescentibus racionibus donorum debet secundum beatum Gregorium crescere racio humilius et promcius ministrandi. Nam secundum Apostolum prima Thym. V; Qui non providet suis et maxime domesticis fidem negat et est infideli deterior, papa igitur provideret specialiter Romanis de bonis spiritualibus; cum fit eorum dominus et curatus. Racione dominii debet eos seculariter defendere et racione patris spiritualis et peculiaris debet eos instar Pauli spiritualiter gignere et fovere.

[ENGLISH]

## ¶5 · 167.32–168.26

> [p. 167] Item; si super ista racione dependet racio papatus Romani pontincis, cum ista racio sit secundum fortunam valde mutabilis, sequitur quod oportet papatum proporcionaliter variari, nam [p. 168] tempore apostolorum et diu post non fuit Roma civitas christianismi, vel plenius civitas synagoge sathane, cum imperator et maior pars populi fuerat infidelis, ymo ut declarat dominus Ardmacanus libro VII, cap. XVI De Questionibus Armenorum, ad tantum restrictum est Romanum imperium, ut non solum imperio Magni Canis de Cathay, sed modo insuper imperio Persarum, imperio Usbeck, imperio Soldani et imperio barbarorum sit minor dominio seculari, ymo secundum relacionem eorum, qui remotas visitarunt contratas, sunt multe civitates, que Romam exuperant. Ideo procul a catholico, ut dicat locum illum vel populum necessitare, ut episcopus suus sit optimus sequax Christi. Et ideo infra dicit dominus Ardmacanus cap. XVIII: Mihi, inquit, videtur quod papatus et pontificatus Romanus non sic connectuntur quin ex causa racionali poterunt separari. Et conformiter tollitur secunda racio, qua fingitur quod in capite mundi, ubi est generalior confluxus populi, reciperet ipse efficacius doctrinam Christi et exemplaretur apcius, quomodo principes Romani forent Christo subiecti, nec non tercio fons cleri assisteret fonti secularis dominii, ut milicia cleri corroboret, et clerusprincipibusconsulat et regat secundum evangelium Ihesu Christi.

[ENGLISH]

## ¶6 · 168.27–169.31

> [p. 168] Ista autem triplex ficticia non est racio, quia in toto continet oppositum. Nam Nero, Dyoclecianus et genus tyrannorum succedencium fuerunt precipua obstacula, quare non currebat in imperio evangelium et lex Christi, sicut patet ex notis cronicis, ymo Constantinus succedens venenando [p. 169] magis diutine dampnificavit ecclesiam; et iterum clerus ex avaricia nimis dampnificavit imperium, et quod plus est dedit principibus perniciosum exemplum de omni genere peccatorum, et quod est infidelissimum, obmutuit incrassatus corripere vel docere. Nam ante dotacionem Petrus, Clemens, Marcellus et alii sancti Romani episcopi usque ad mortem dilexerunt cesarem et eius populum docendo et corripiendo. Sed postquam dotati sunt, laboraverunt vecordia atque blasfemia, vecordia timendo dicere principibus et populis sua vicia, quin pocius lacte adulacionis mollificarunt et dissolverunt suos dominos, ut dando illis temporalia contra regulam Christi dampnificent se et illos. Et tercio prorumpunt in maiores ingratas blasfemias, dicentes quod non habuerunt dotacionem illam a cesare, sed iure successionis Christi et Petri, qui fuerunt summe taliter dominati. Ideo non docet eos visitare principes et eis impertiri aliquid spiritualis doctrine, sed residere ubicumque voluerint, imperatoresque et reges advocare et abiectissima mundana servicia imperialiter ab eis recipere. Non sic fecit Petrus, ideo indubie dissonat scole Christi, cum post multiplicacionem donorum temporalium satagerent visitando donatores, humilius refundere pociora. Sed quis tam ingratus Christo abbati non foret ingratus proximo? Christus enim ob amorem nostri venit summe inops et egenus, ut dicitur II. Cor. VIII ad finem, et ut nos clerici et specialiter Petri vicarii vivamus similiter.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 165.2: „Pope."
- 165.13: Formerly used of other bishops.
- 166.12: It has come to mean the bishop who is nearest to Christ in life and work.
- 166.19: How came it to be assigned to the Roman pontiff:
- 166.26: Armachanus says: Because Rome was the chief city of Christendom.
- 167.14: If so, what of the popes who fatten at Avignon.
- 167.20: Their first duty is to Rome where they claim dominion.
- 167.32: Capitals may be changed.
- 168.13: There are empires greater than the Roman.
- 168.16: The papacy separable from the Roman pontificate.
- 168.22: With this falls the plea that in the capital the clergy had more influence for the good of the Church.
- 169.10: Endowment made the clergy shirk their duty of teaching and reproof.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 165: *CAPITULUM OCTAVUM.* [HEAD]
  - 165: *pontificem* [R4]
  - 165: *Et* [R4]
  - 165: *Deus* [R3]
  - 165: *sanctitatem* [R5]
  - 165: *quos* [R3]
  - 165: *Aurelio* (25 is the line number) [R4]
  - 166: *accessus* (hyphenated ac-cessus; main token covers whole word) [R4]
  - 166: *ra-* (hyphenated ra-cione; main token holds first half) [R3]
  - 166: *illum* [R3]
  - 167: *Deus* [R3]
  - 167: *deterior* [R3]
  - 167: *racio* [R4]
  - 168: *ut* [R3]
  - 168: *Canis* [R4]
  - 168: *contratas* [NW]
  - 168: *illum* [R3]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Rome waTthe (166.27).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 165:
1 A in marg.: c. 8. 4. AB in marg. : Papa hoc nomen quid signet.
14. A in marg. : Quod pape vocabantur Jeronymus, Auguslinus, Ambrosius,
Aurelius et alii. Nota Augustinus mirabiliter contra Wy.
8. Cf. The English Works of Wyclif ed. Matthew p. 471.
See Freeman's William Rufus I, 292. Cf. Huss, 256\ 14. Ep. CXII.
Hier. ad. Aug. Migne Patr. tom. XXII, 916 et Aug. Opp. II, 189.
18. Ep. XXXI al. XXXII Opp. tom. II, 58. 23. Ibid. pag 87.
26. Ep. LIII al. CLXV ib. pag. 120.

p. 166:
10. Codd.: Archidiaconus; seq. lacuna. i3. AB in marg. : Papa
specialiter quid significel.
3. lbid. App. pag. i. 7. Ep. XIV al. CXCIV App. pag. 4.

p. 167:
8. quain; codd.: quia. i5. Codd.: papa.

p. 168:
7. Canis = (Khanj. 8. Codd.: Catnay. {Cathay = regnum Sinese.)
9. Usboth in cod. 18. quin; codd.: quando.
5. Cf. Summa domini Armacani in Questionibus Armeno-
rum VII. 16 fol. XLVIII Paris i5n (R. L. Poole).

p. 169:
6. AB in marg. : Predicaverunt episcopi Romani ante dotacionem.
12. AB in marg. : Dotacio imperatoris deduxit et multiplex malum.
24. Petrus; codd.: P. 27. Codd.: Christi. 3o. finem XV; Rectius:
VIII, g; XV = o.videtur esse: et.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 08-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "169.32–173.32"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "894 words; 805 unanimous or majority-real; 68 settled by vote (R2 38, R3a 16, R5a 13, R6a 1); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n230–n234 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 2: [TITLE]

## ¶1 · 169.32–171.14

> [p. 169] Econtra autem nos pro excusacionibus in peccatis fingimus de eo blasfemum mendacium [p. 170] quod dominatus fuit et apostolos suos dominari docuit summe civiliter. Et virtute istius mendacii coloramus nostrum monstruosum dominium. Non enim decuit regem seculorum assumere sibi ad perfeccionem humanam seculare dominium, nisi hoc faceret ad summum ultra quam alicui alteri bene potest competere Quomodo igitur ipse acciperet tam parce et indigne sessivam in dominio ad quod aspirat, relinquens mendacibus ab eo degenerantibus possessionem gloriosam et plenam super omnia regna mundi. Nonne (ut sepe repecii) leges papales convincunt, illud mendacium, primo XCVI distinccione Constantinus, incorporatur cartha Constantini et pape, testificans formam qua donavit cece partem illam imperii suo episcopo? Nonne secundo ex testimonio magni doctoris Augustini posito distinccione VIII Quo iure docetur expresse, quod clerus non habet proprietatem secularis dominii, nisi ex lege cesaris et dono secularium dominorum? Nonne tercio beatus Bernhardus libro II, III alloquitur Eugenium papam sub hiis verbis, ut recitavi diffuse superius: Quid dimistrit pape sanctus apostolus? quod habeo, inquit, hoc tibi do; quid illud? certe non est aurum neque argentum cum ipse dicat: Argentum et aurum non est michi. Si habere contingat, utere non pro libito, sed pro tempore, sic eris utens illis quasi non utens. Ipsa quidem quantum ad bonum anime spectat, nec bona sunt nec mala, usus tamen horum bonus, abusio mala, sollicitudo peior, questus turpior. Esto ut alia quacumque racione hec tibi venaices [p. 171] sed non apostolico iure; nec enim tibi dare quod non habuit, potuit; quod habuit, hoc dedit, sollicitudinem ut dixi super ecclesias. Numquid dominacionem? Audi ipsum. Non dominanies, ait, in clero sed forma facti gregis, et ne hoc dictum sola humilitate putes, non eciam veritate, vox domini est in evangelio: Reges gencium dominantur eorum, vos autem non sic. Planum est: apostolis interdicitur dominatus. Ecce hoc triplex testimonium manifeste convincit illud mendacium, lex propria, Augustinus, Bernhardus, qui manifeste dicit, quod non iure apostolico papa habet hec temporalia. Ideo dicit libro IV: In hiis successisti non Petro sed Constantino.

[ENGLISH]

## ¶2 · 171.16–171.28

> [p. 171] Et patet quam horribile est fingere talia blasfema mendacia propter dominia temporalia pallianda, Patet eciam, quod nec seculares nec clerici iuvantur per assistenciam talium antichristianorum sed profundius peiorantur, tam quoad bona temporalia quam spiritualia. Quoad temporalia, ut prophetatum est Dan. II et exponitur inferius, hoc fecit scissionem imperii. Et quoad spiritualia, patet quod mutuo se inficiunt ex consensu. Assistencia autem cleri tenentis se in statu primevo decoraret miliciam et econtra, ut patet de beatis Sebastiano, Martino et ceteris sed apostatarum assistencia deturparet.

[ENGLISH]

## ¶3 · 171.29–172.2

> [p. 171] Quinta causa ficta est loci sanctitas ex multiplici christianorum martyrio, ubi decet sanctissimum caput ecclesie conversari. Sed constat quod locus non sanctificat inhabitantem sed econtra, ut dicitur II. Machabeorum V. Locus enim non est de genere activorum, cum sit quantitas et [p. 172] influencia celestis vel est sanctitati impertinens vel loca sunt alia magis apta.

[ENGLISH]

## ¶4 · 172.3–172.13

> [p. 172] Similiter, si locus capit sanctitatem, per idem malediccionem ab incolis facinus committentibus jn eodem, ut patet II. Regum primo de monte Gelboe. Sed Rome ab imperatoribus et carnificibus sibi subiectis, qui permanencius incolebant locum post et ante quam martyres, fuit multiplicius facinus perpetratum, igitur locus ille foret evidencius maledictus. Et in signum huius multi pape fugiunt illum locum, sicut Balaam propter influenciarum varietatem fecit altaria variari, ut dicitur Numeri XXIII.

[ENGLISH]

## ¶5 · 172.14–172.30

> [p. 172] Similiter, si sanctitas martyrum fugat facinus et locum sanctificat, Jerusalem foret locus sanctissimus, cum ibi predicavit et passum fuit caput martyrum, ibi occisus est uterque Jacobus et multi martyres, ymo in veteri testamento occisi sunt plurimi, ut testatur Christus Matth. XXIII, 37 Jerusalem que occidis prophetas et lapidas eos qui ad te missi sunt, et IV. Regum XXIV, 4 scribitur quomodo Manasses effudit sanguinem innoxium et implevit Jerusalem cruore innocencium, et ob hanc rem noluit dominus propiciari. Difficile autem est sompniare, in qua istarum civitatum occisi sunt plures martyrio. Sed certum est quod Christus predicans, conversans et occisus in Jerusalem, infinitum excedit totum collegium martyrum Rome vel alibi occisorum, et preter hec locus est sanctitate antiquior.

[ENGLISH]

## ¶6 · 172.31–173.20

> [p. 172] Ex istis colligitur quod nec iste quinque raciones nec alie fingende stabiliunt quod oportet realiter Romanum pontificem esse papam. Multi enim Romani pontifices sicut et imperatores erant pessimi antichristi, et civitas illa cum gente [p. 173] sua modo prevalet et modo subditur, cum multe sunt hodie civitates, gentes et comunitates plus divites, inclite et amplius populose. Quomodo igitur apostoli, quibus preceptum est indiferenter omnes gentes, limitarent se ad illum populum, cum possent plus lucrifacere Christo in alio populo eciam non converso. Unde ut credo hec fuit una racio, quare apostoli non receperunt dotacionem fixam in terris, ut ubicumque terrarum spiritus eos moveret ad plus prodessendum ecclesie illuc tenderent indilate. Iuxta quem sensum scribit Apostolus Hebr. XIII, 14: Non habemus hic manentem civitatem sed futuram inquirimus, aliter enim dominium affixum retraheret affeccionem convertendi. Et hec racio, quare Christus non fuit affectus templo, ut patet Mar. XIII, sed predicavit sub divo, nunc in deserto, nunc in montibus, nunc in mari et sub verbis indifferentibus et generalibus, ut patet Matth. ultimo, precepit apostolis predicare.

[ENGLISH]

## ¶7 · 173.21–173.32

> [p. 173] Quantum ad secundam ficticiam ad colorandum connexionem predictam Romani et summi pontificis per institucionem Petri; patet quod innititur foliis sine fructu; non enim plus sequitur: Petrus ordinavit Clementem episcopum Romanum, igitur ordinavit eum summum pontificem quam sequitur, ordinavit Marcum Anthiochie sibi succedere, igitur ordinavit eum sibi succedere in summum pontificem; locus autem (ut dictum est) est indifferens ad papatum et eque plenus papa fuit Petrus Anthiochie sicut Rome, et preterea Anthiochie accepit a populo insignia et non Rome.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 170.1: It is false that Christ ruled and that it becomes his disciples, to do so.
- 170.18: If the clergy hold property, they do it by Cesar's law.
- 171.16: Worldly gifts do not aid the Church but injure it.
- 171.29: Another plea is sanctity of Rome for its many martyrs,
- 172.3: Against this may be set its pollution by much wickedness.
- 172.14: Moreover Jerusalem has higher claims.
- 172.31: It is not proved that the bishop of Rome must be pope.
- 173.7: Endowment would have hindered the apostles' journeys.
- 173.21: That Peter ordained Clement proves nothing or the papacy might be at Antioch.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 170: *dominatus* (folio bar after it (203b)) [THIN]
  - 170: *Et* [R3]
  - 170: *mendacii* [R3]
  - 170: *parce* [R3]
  - 170: *Quo* [R3]
  - 170: *nisi ex lege* (print has nisi ex lege before cesaris) [GAP]
  - 170: *venaices* (misprint: a has no ascender, not d; zoomed leaf 231) [THIN]
  - 171: *quod* [THIN]
  - 171: *non* [THIN]
  - 171: *hoc* [THIN]
  - 171: *autem* [R3]
  - 171: *hiis* [R4]
  - 171: *blasfema* (hyphenated blas-fema; main token covers whole word) [NW]
  - 171: *dominia* [R4]
  - 172: *∅* (folio bar (203d) read as i; not text) [INS?]
  - 172: *illum* [R3]
  - 172: *sanctificat* [R3]
  - 172: *istis* [R3]
  - 173: *inclite* [R3]
  - 173: *illum* [R3]
  - 170: *argentum* (LEFT-odd: italic; comma not carried; 25 is the line number) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Rome fo/its manv martvrs. (171.30).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 169:
6. AB in marg. : Predicaverunt episcopi Romani ante dotacionem.
12. AB in marg. : Dotacio imperatoris deduxit et multiplex malum.
24. Petrus; codd.: P. 27. Codd.: Christi. 3o. finem XV; Rectius:
VIII, g; XV = o.videtur esse: et.

p. 170:
8. sessivam; ita cod. n. AB in marg. : Possessio pape data est a
Caesare, non a Christo vel Petro. i5. B: formans, 21. Codd. :
i3. Cap. XIV. 18. Cap. I. 21. St. Bern. pag. 748.

p. 171:
3i. AB in marg. : Locus non sanctificat hominem.
14. Cap. Iir, pag. 776.

p. 172:
14. AP> in marg. : Jerusalem locus sanccior Roma.

p. 173:
7. AB in marg. : Dotacionem et loci appropriacionem qitare apostoli
fugiemnt. 20. Codd.: apostoli. 21. Codd.: ficticium.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```
