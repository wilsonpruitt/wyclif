# Translation brief: potestate-pape 11-e–11-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-11-e.md chunks/potestate-pape/wyc-potestate-pape-11-f.md chunks/potestate-pape/wyc-potestate-pape-11-g.md` once and fix what it reports.
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

## Glossary (the 255 rows these chunks use; the full file is GLOSSARY.md)

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
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
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
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| laureola | aureole | The theologians' special crown (of virgins, martyrs, doctors). Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| iugum | yoke (a pair) | Ruled 2026-10-02 (*Eccl.* 202.9 ff.). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| humidum naturale | natural moisture | Synonym of *humidum radicale* (row above); G note at use. Ruled 2026-10-02 (*Eccl.* 17, 410.2). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| laxare | loose | Kept apart from *relaxare* "relax". Ruled 2026-10-02 (*Eccl.* 23, 571.29). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| influencia (celestis) | (celestial) influence | Astrological sense. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 172.1). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| connexio | conditional (proposition) | Logic: the "if … then" proposition. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 189.1). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| cultus Dei | worship of God | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-d). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 11-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "279.16–282.33"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 5 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "757 words; 707 unanimous or majority-real; 38 settled by vote (DEL 1, R2 18, R3a 16, R5a 2, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n340–n343 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 5: [TITLE]

## ¶1 · 279.16–281.17

> [p. 279] Secunda vestis estzona, baltheus vel cingulum, latitudinis quasi quatuor digitorum, reticulatam, quasi pellis vipperea vel stricta tunica linea circa renes, per cuius fortem tinccionem notatur, ut castitas sacerdotis nullo incentivorum estu, cogitacione velopere dissolvatur, iuxta illud LuceXII, 35: Sint lumbi vestri precincti. Et sic candor vestis signat mundiciam, zona vero continenciam, ut illic non sordescat, hic non effluat conversacio sacerdotis. De zona legitur Exod. XXVII: distincta quatuor coloribus, scilicet bisso et purpura, iacincto et cocco. Per que iuxta signacionem predictam duplicem duplex quaternarius designatur: Primo notantur quatuor virtutes cardinales, scilicet iusticia, fortitudo, temperancia et prudencia, per quas cinctus animus servat albedinem vestis, per quam sit digna, ut dicitur Apoc. XIV, 1 sequi agnum quocumque ierit. Et est correspondencia electorum in istis quatuor coloratis ad istas quatuor virtutes. [p. 280] cum bissus terre admodo, ut patet de combustis cineribus, ossibus et ceteris albis siccis notat iusticiam, que instar terre solide stat in omni temptacione, ut Aristoteles dicit I Ethicorum sicut tetragonus sine vituperio. Purpuravero ignem pretendens, racione ruboris signat fortitudinem purgatam, ut aurum in camino tribulacionis, ut loquitur scriptura, laccinctus autem celestis coloris, aquam induratam signans, notat temperanciam que massam corporis humani sic temperat, ut in via morum propter amorem celestium non effluat terminis alienis. Coccus vero bis tinctus est genus tincture medius inter rubeum et croceum, quem nos dicimus vermiculum vel subrubeum colorem ex silvestribus frondibus, vel (ut aliis placet) ex quodam verme decoctum; et signat prudenciam vigentem in sanguineis instar aeris temperatis et specialiter si tincti fuerint preter virtutes morales in prudencia conversacionis penalis domini Ihesu Christi. Secundo notantur quatuor humores, scilicet melancolica et colerica, flegma et sanguis, quibus nature sagacitate commixtis humana complexio denotatur. Sic inquam istis quatuor moribus continencia figuratur. Sicut enim electa in mixtis, sic humores in animalibus et proprietates spirituales in mentibus habent sua officia. Terra enim facit mixto constanciam, aqua continuacionem, aer capacitatem celestis influencie et ignis est via recipiendi peregrinas impressiones et quasi luna instrumentalis, mediante qua mitigantur frigiditas et humiditas inferioris duplicis elementi et confortatur qualitas aeris, ut puta raritas atque caliditas. Sic est de complexione hominis corporali [p. 281] et de continencia mentis spirituali, dum memoria proprie fragilitatis ut terra, continuacio dulcis devocionis ut aqua, tenuitas corporalis cibacionis ut aer et raritas muliebris conversacionis ut ignis, faciunt sacerdotem Domini continentem. Nichil enim tantum valet ad domandum carnis desideria, sicut pensare quomodo incinerabitur post mortem hominis facta terra; continuacio vero devocionis, extinguens ocium, precavet omne crimen et per consequens carnis luxum. Ieiunium vero cavens crapulam cum adiutorio celestis radii extinguit ignem libidinis, et caritativa fuga muliebris consorcii et profugienda luxuria supereminens medicina. Evanescas igitur et non expectes in cogitacione vel corpore muliebre consorcium instar ignis, quia nisi habueris ignem amoris, non calesces supernaturaliter.

[ENGLISH]

## ¶2 · 281.18–282.2

> [p. 281] Tercia vestis sunt femoralia, que preter braccas com munes sacerdos induet m signum castitatis eciam interioris, dum vacat divinis officiis. Non enim credi debet sacerdotes veteris testamenti alias continue discooperta carne pudoris incedere, ut solum intrando in sancta verenda tegere iubeantur, sed servando continue castitatem coniugalem voluit sermo Dei, ut sacerdotem fungentem officio sacri ministerii cooperiat castitas singularis; unde quia sacerdotes novi testamenti inconiugati servare debent castitatem virginalem continue, ideo tantum utuntur femoralibus communibus ad denotandum, quod continue non licet eis ut sacerdotibus legis veteris post completum officium, laxare ministerium carnalis copule; eis enim pro servanda castitate [p. 282] est cottidiana necessitas, quibus continue offerrendi summum sacrificium concessa est potestas.

[ENGLISH]

## ¶3 · 282.3–282.15

> [p. 282] Quarta vestis est tunica interior vel iacinctina, qua in utroque testamento utuntur soli pontifices ad denotandum, quod in illis debet precipue duplex castitas scilicet mentis et corporis observari. Pontifex quidem, qui de thesauro suo debet proferre nova et vetera, cum carnalis copula distrahit a spirituali noticia duplicis testamenti, debet observare duplicem castitatem. Ista igitur tunica priori superaddita signat quod dissimilis terrestribus debet de celestibus cogitare. Ideo vocatur tunica interior iacinctina, ut significet cordis mundiciam, et de celestibus cogitatum. Phil. III. 20 dicit Apostolus: nostra conversacio in celo est.

[ENGLISH]

## ¶4 · 282.16–282.33

> [p. 282] Quinta uestis est superhumerale, que hebrayce ephot dicitur quasi casula vel planeta; et contextum erat pilis de auro ac coloribus supradictis. In veteri vero testamento soli pontifices usi sunt hac veste quatuor distincta coloribus, ad sensum de zona expositum; tempore vere gracie utuntur ea quilibet sacerdotes. Signat autem superhumerale fortitudinem operum et pacienciam laborum, per duos humeros denotatas, unde altrinsecus super humeros fibulabantur duo lapides onichini, in quorum dextro inscripta erant sex nomina seniorum filiorum Ysrahel, et sex in alio, denotando quod sacerdos debet recolere de patriarcharum constancia tam in prosperis quam in adversis. Nostrum autem superhumerale non sic inscribitur, quia tempore gracie dimissis cerimoniis antiquis, veniente unico patriarcha, debemus plus inniti simplici veritati.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 279.16: The girdle of four colours. Their significance.
- 281.4: How to tame the flesh.
- 281.18: The breeches a symbol of chastity.
- 282.3: The inner tunic.
- 282.16: The Ephod patience.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 279: *signat* [R4]
  - 279: *hic* [R4]
  - 279: *1* (print "Apoc. XIV, 1 sequi": old-style arabic 1, x-height; the main scan lost it) [INS?]
  - 280: *sicut* [R3]
  - 280: *loquitur* [R3]
  - 280: *coloris* (hyphenated co-|loris; main token holds the whole word) [R4]
  - 281: *induet* [NW]
  - 282: *cottidiana* [THIN]
  - 282: *offerrendi* [R5]
  - 282: *planeta* [NW]
  - 281: *inconiugati* (S-split: one word) [OVERRIDE-SCARPLATE]
  - 282: *onichini,* (LEFT-nw: hyphenated oni-|chini, ; line number 25 follows) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Tlie Ephod (282.16).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 279:
1, 2. Codd.: bissinum splendentis candidum ut deest. 3. Codd. in
marg. : Alba prima vestis. 10. Oportet; B : Sed. 16. Codd. in marg. : Se-
cunda \ona. 18. B : Circa deest. 21. Codd. : Lucae XII. 22. A : Etsicut.

p. 280:
5. Eodem exemplo utitur W. De Civili Dominio I, 54, 1. 26.
7. Prov. XVII, 3.

p. 281:
4. B: ut signis. 18. B: sunt deest. Codd. in marg. : Tercia veslis
femoralia. Castitas sacerdoti necessaria.
20. Cf. Hugo De Sacramentis 1. c. p. 460. Very loosely
quoted.

p. 282:
3 Codd. in marg. : Quarta veslris tunica interior. 16. Codd. in
marg. : Quinta vestis humerale.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 279: illud Apok.XIX, 8: Datum est sponse nt operiat se bissinosplendenti candido. | Bissinuui enim iustificaciones snnt sanctorum. Caro quideui hominis mundiciam,quam exnatura non habet, | studio bono aquirit per graciam, sicut bissus vel linum candorem suum, quem natura non habuit, per studium et industriam arlificis aquisivit, dum multis tunsionibus ac locionibus illustracione solis siccantis quasi quadam violencia atiriium vertitur \oin alborem. | stncta tunica iinea circa renes, per cuius fortem tinccionem notatur, ut ca- | stitas sacerdotis nuilo incentivorum estu, cogitacione velopere dissolvatur, iuxta illud LuceXII, 35: Sint lumbi vestri precincti. Et sic candor vestis signat mundiciam, zona vero continenciam, ut illic non sordescat, Jtic 11011 efftuat conversacio sacerdotiSo | De zona legitur Exod. XXVII: distincta \ quatuor coioribus, scilicet bisso et purpura, iacincto et cocco. | sequi agnum quocumque ierit.
p. 280: sicut tetragonus sine vituperio. | aurum in camino tribulacionis,
p. 281: Non enim credi debet sacerdotes veteris testamenti alias continne discooperta carne pndoris incedere, ut solum intrando in sancta verenda tegere iubeantur, sed servando continue castitatem coniugalem voluit 2? sermo Dei, ut sacerdotem fungentem officio sacri ministerii cooperiat castitas singularis; unde quia sacerdotes novi testamenti inconiugati servare debent castitatem virginalem continue, ideo tantum utuntur femoralibus communibus ad denotandum, Zoqnod continue non licet eis ut sacerdotibus legis veteris post completum officium, laxare ministerium carnalis copule; eis enim pro servanda castitate
p. 282: est cottidiana necessitas, quibus continue offerrendi snmmum sacrificium concessa est potestas. | qua in utroque testamento utuntur soli pontifices | Pontifex quidem, qui de tkesauro suo debet proferre nova et vetera, | Ista igitur tunica | signat quod | debet de celestibus cogitare. Ideo vocatur tunica interior iacinctina, ut significet cordis muudicianu et de celestibus cogitatum. | nostva conversacio in celo est. | Ouinta uestis est supevhumevale, que hebrayce | ephot dicitur | quatuor distincta coloribus, | Signat autem superhumerale fortitudinem operum et pacienciam laborum, per duos humeros denotatas, unde altrinsecus super humeros fibulabantur duo lapides oni-rf chini, in quorum dextro inscripta erant sex nomina seuiorum filiorum Ysvahel, et sex in alio, denotando quod sacerdos debet recolere depatriarcharum constancia tam in prosperis quam in advevsis. Nostrum autem superhumerale non sic inscribitur,3o quia tempove gracie dimissis cerimoniis antiquis, veniente unico patviavcha 7 debemus plus inniti simplici veritati.
```

---

## Chunk 11-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "283.1–286.29"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 6 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "782 words; 754 unanimous or majority-real; 19 settled by vote (DEL 1, R2 12, R3a 5, R6a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n344–n347 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 6: [TITLE]

## ¶1 · 283.1–284.16

> [p. 283] Sexta vestis est racionale vel logyon, quod pectori pontificis in foramine superhumeralis contexitur. Et fuit vestis conformis texture cum superhumerali, habens nomina duodecim filiorum Ysrahel inscripta secundum quatuor ordines in duodecim lapidibus, ut recolendo de sanctis patribus non degenerent ab eis in moribus. In medio autem fuit lapis sardonicus, cui inscribebantur hec duo nomina: iudicium vel doctrina et veritas. Unde secundum Yosephum, dum populus fuit domino placabilis sacerdosque daret populo secundum inspiracionem Dei responsum prosperum, lapis in signum placacionis divine in solito splendore emicuit. Sed ducentis annis antequam scripsit librum Antiquitatum, quod fuit tempore Tyti et Vaspasiani cessavit dictus splendor, quod fuit prenosticum reprobacionis populi ex peccato. Rasa dicit, quod urin et thyrin Hebreum, quod sonat doctrina et veritas, fuit nomen Domini tetragramaton, virtute cuius responsum et splendor populo innuebant et signat mistice, quod pontifex medians inter Deum et populum debet docere doctrinam inhaustam secundum Dei iudicium; et sicut non docebit aliam quam veritas suggerit, sic doctrinam suam opere et racione confirmare non desistit. Concathenatur autem racionale superhumerali [p. 284] in signum, quod habitus et opera sibi debeant coherere, sic quod totum corpus operum a caritate pectoris procederet. Que caritas licet sit modica in sua essencia, tamen extenditur in quadratum, quia secundum lineam protensam a: summo in infimum a dextris amicorum ad sinistrum inimicorum, et ab antiquo ad patres preteritos ad retro quoad filios successores, latitudo vero in operibus debet effectualiter practisari correspondenter ad istam quadraturam, unde ad denotandum istum ordinem prius recitatur racionale in Exodo XXVIII ante superhumerale, quia oportet thesaurum habitus procedere, cum nemo doceat antequam sciat. Sed in ordini docendi oportet opus precedere iuxta illud Act. primo, Cepit Ihesus facere et docere.

[ENGLISH]

## ¶2 · 284.17–285.3

> [p. 284] Septimum ornamentum est mitra, cydaris vel thyara, que imposita capiti, in quo viget sensus, signat quod illis debet committi cura regendi alios, qui ad sensum preexpositum sciunt preeminenter se ipsos regere. Sic enim loquiturApostolus prima Cor. XI 3 de capite ponens caput uxoris virum, caput autem viri Christum et caput Christi Deum; ex quo sequitur, quod Christus est creatura, cum secundum humanitatem regitur a se Deo. Dicitur autem mitra fuisse duplicata, cuius pars interior est bissina, pars vero exterior iacinctiva habens in parte inferiori semicirculum aureum ab auribus occupat amplectentem; per hanc igitur signatur vite mundicia, cum bissus supponitur, celestis conversacio, cum iacinctivus color eminet; donum autem caritatis et sapiencie connectens hec in capitaneo signatur per semicirculum [p. 285] aureum transeuntem per mitram capiti conectentem. Semicirculus autem signat, quod semiplene in via suscipimus ista dona.

[ENGLISH]

## ¶3 · 285.4–285.19

> [p. 285] Octavum ornamentum est lamina aurea, que transiens ab aure m aurem per frontem iuncta est; cum mitra filis iacinctivis, cui insculpebatur nomen Domini tetragramaton, quod in Hebreo ineffabile nominatur; per quod consignatur Deum omnium conditorem et rectorem secundum suam sapienciam esse precipue a pontificibus ostendendum tam opere quam sermone, ita quod nomen inscriptum significet essenciam, aurum sapienciam, semicirculus patens in fronte significet eius lucernam ad extra in fabrica quam creavit accione eius ad intra a nobis abscondita: ora autem huius lamine supposita signat opus creacionis, ora vero superior signat opus gubernacionis, et connexio huius lamine cum mitra signat, quod officio spiritualis prepositure coniungi debeat hec doctrina.

[ENGLISH]

## ¶4 · 285.21–285.30

> [p. 285] Preter hec octo ornamento sunt anuli, vitte vel fibule et tyntinabula, que computantur ut partes vestium predictarum. Debet enim pontifex in suo officio habere tunicam iacinctinam, que poderis dicitur, in cuius margine inferiori forent septuaginta tyntinabula aurea et tot vasculi vel noduli quasi mala punica commixti, ut ingradiendo sanctuarium sonitus audiatur. Sic sub pena mortis debet pontifex sonare verbum sapiencie predicando et opera fructifera commiscendo.

[ENGLISH]

## ¶5 · 285.31–286.29

> [p. 285] Alia autem confibulancia has vestes ad invicem signat cathenam auream, qua caritas connectit omnia opera grata Deo. Unde quatuor causas in [p. 286] genere ponunt doctores talis ornatus pontificis, prima ut excellencia Dei consideretur affectuosius dum eius abiectus vicarius sic ornatur. Secunda ut sacerdotes medii inter Deum et populum tractentur honorabilius. Tercia ut populus intendat cultui divino delectabilius. Et quarta ut divina excellencia consideretur in fabrica sua expressius. Per tunicam quidem lineam dicunt doctores offigurari terram cum suis ornamentis: Baltheus ligans hanc tunicam figuratur occeanum. Tunica iacinctina racione coloris signat aerem. Et tyntinabula cum malogranatis notant tonitrua cum aliis aeris impressionibus. Quidam autem ponunt baltheum cingentem hanc tunicam figurare speram ignis cingentem aerem, superhumerale cum racionali sibi iuncto signat celum ethereum, et multitudo colorum diversitatem stellarum. Duo lapides onichini signant duo luminaria magna celi, duodecim gemme in racionali signant duodecim signa zodiaci, in quibus sunt raciones istorum sublunarium; unde Yob XXXVIII: Numquid nosti ordinem celi et pones racionem eius in terra? Per mitram vero figuratur celum empireum et per laminam auream dominus presidens omnibus creaturis. Et hinc nomen Domini magnum sibi inscribitur. Et hinc creditur Alexandrum magnum adorare Deum pronum in terram, dum vidit formam pontificis sic vestiti, ut narrat Magister Historioarum in historia Machabeorum primo cap.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 283.1: The breastplate of judgment.
- 284.17: The Mitre.
- 285.4: The gold plate on the mitre.
- 285.21: There were besides rings etc. reckoned as parts of the garments mentioned.
- 285.31: Four reasons for thus adorning the priests.
- 286.8: How the vestmemts signify parts of the universe.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 283: *logyon* [R5]
  - 283: *foramine* [THIN]
  - 283: *∅* (the 1 is the folio bar (231d) before Sed) [R3]
  - 283: *urin* [NW]
  - 284: *habitus* [THIN]
  - 284: *antiquo* [R3]
  - 284: *doceat* [R4]
  - 286: *Tunica* (10 is the line number) [R4]
  - 283: *tetragramaton, virtute* (LEFT-nw: two printed words, comma between) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 283:
1. Codd. in marg. : Sexta vestis racionale.
9. Historiam istius miraculi in Josephi Antiquitatum Jud.
lib. III, cap. IX (ed. Franc. 1 588, p. 38b) invenies: Ex lapillis
enim quas Pontifex in humeris gestabat . . . micabat alter . . .
tantum fulgorem emittebat. ut procul eciam intuentibus conspi-
ceretur . . . Sed mirabilius . . .: per duodecim gemmas . . . in
bello victoriam prenunciare Deus solebat, nam priusquam exer-
citus se moveret, tantus fulgor ex eis emicabat ut toti populo
facile innotesceret adesse Deum . . . Desiit tamen esse quam
Sardonix fulgorem emittente annis 200 ante quam haec commen-
taremur irato Deo . . .

p. 284:
3. B: a deest. 17. A in marg. : Septimum ovnamentum est mitra;
B in marg. : septimum.
12. Exod. XXV, 28; XXIX, 5.

p. 285:
1. Codd.: per occiput mitram (sic). 4. Codd. in marg. : Octavum
lamina. 7. Codd. in marg. : Tetragmaton quid signet. 26. Codd. in
marg. : Tintynabula. 33. Codd. in marg.: Vestimentorum pontificis
quatuor ponuntur cause.

p. 286:
21. Job XVIII, 33. 29 Magister Historiarum: vid. Petr.
Comest. 1. c.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 283: Sexta vestis est racionale vel logyon, qnod pectori | pontijicis in fovanune superhumerahs contexitur. | Concathenatnr autem racionale super-
p. 284: humerali in signum, quod habltus et opera sibi debeant coherere, sic quod totum corpus operuni a caritate pectoris procederet. | cum nenio doceat antequam sciat. | Cepit Ihesus facere et docere. | mitra. cydaris vel thyara, | sciunt pre- | eminenter se ipsos regere. | caput uxoris virum, caput autem viri Christuni et caput Christi Deum;
p. 286: Numqtiid nosti ordinem celi et pones racionem eius in terra?
```

---

## Chunk 11-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "286.30–290.27"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 7 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "821 words; 776 unanimous or majority-real; 19 settled by vote (DEL 1, R2 8, R3a 6, R5a 3, R6a 1); 26 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n347–n351 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 7: [TITLE]

## ¶1 · 286.30–288.6

> [p. 286] Notandum autem quod sacerdotibus inferioris ordinis non datur tunica lacinctma nec superhumerale nec racionale nec lamina aurea, sed soli summo pontifici, sicut in nostris sacerdotibus [p. 287] est ordo vestium. Sex enim ornamenta habent simplices sacerdotes in missa; scilicet amictam, albam, zonam, manipulam, stolam et casulam. Per amictam notatur custodia sensuum sacerdotis, quia illud ornamentum tegit caput et collum, in quo sunt omnes sensus; sic clericus debet velare omnes sensus et specialiter tempore misse, ne adulterinis sensacionibus temptet mentem, nec collum, in quo est organum vocis, ministret vocem ab interioribus ad vicium lingue. Sed iuxta Petri monita: Si quis loquitur, quasi sermones Dei prima Petr. IV, 11. Verba enim sacerdotis debent esse evangelium. Alba camisia, que est stricta linea in veteri testamento signat omnia membra corporis sacerdotis divino servicio mancipanda. Sed tempore ecclesie Judeorum, qui spiritu servitutis erant astricti, erat hec tunica striccior, quam est modo, quando dilatamur libertate qua Christus nos liberavit. Sed quia surrepit ommissionis negligencia, cum inordinatis operibus quantumcumque divino cultui mancipemur, ideo quarto ponitur in sinistra manu mapula vel manipula, denotans quod crebro debemus ab oculis mentis sordes abstergere, et contra facta sinistre perpetrata ad opera penalia gratis obligacione perpetua nos parare. Unde quinto assumit stolam sive orarium, que collo sacerdotis imposita, signat, quod iuxta consilium Christi Matth. XI 29 sustulit super se iugum Domini longenimitatis sufferendum. Quod autem stola cancellata per anteriora descendit, signat quod sacerdos sustulit crucem suam sequendo Christum, per [p. 288] arma iusticie a dextris et a sinistris, ut loquitur Christus Luce IV et Apostolus II Cor. VI et debet stola huius perseverancie que sola coronabitur usque ad pedes affeccionum se extendere. Connexio vero cum zona signat concathenacionem perpetue castitatis cum ceteris virtutibus sacerdotis.

[ENGLISH]

## ¶2 · 288.8–289.6

> [p. 288] Sed sexto induit casulam vel planetam ad denotandum quod eminenciori via incedit presbiter christianus, dum habet caritatem ad singulos. Unde ad denotandum perfeccionem rotunditatis et evacuacionem sordium angulorum declinat hec casula a quadratura superhumeralis in veteri testamento ad rotunditatem et simplicitatem. Non enim est lex Christi tam aspera in angulis ut lex vetus, cum nec apostoli nec patres eorum ipsam portare poterant, ut dicit Petrus Act. XV, 10 sed quibusdam circulis et catenulis fuerant a lateribus colligata. Nos autem sub tali concathenacione por tamus suavem et levem casulam a dextris et sinistris. Caritas enim operatur magis, si est; et licet careat multitudine figurarum superhumeralis veteris testamenti propter unitatem simplicem capitis nostri Christi, debet tamen sacerdos esse planeta in populo, ut videant?: opera eius bona. Sic enim docet Christus Matth. V, quod luceat lux vestra coram hominibus. Et. est aliud ornamentum in novo testamento, competens diacono vel levite, quod vocatur dalmatica, cuius nomen est sumptum a regione, ubi primo creditur institutum. Forma vero creditur capta a collobiis, quibus usi fuerunt apostoli. Quidam enim apostolorum successores adiectis [p. 289] manicis usi fuerunt huiusmodi indumentis; et eundem sensum misticum, quem habet casula in presbiteris, habet dalmatica m levitis; ipsi enim paracius et asperius debent caritative proficere tamquam alter Laurencius quam presbiteri etatis et corporis gravioris.

[ENGLISH]

## ¶3 · 289.7–290.19

> [p. 289] Quotlibet sunt talia signa sanctitatis presbiteri et peroracionis virtutum in anima; et utinam hodie non sint falsa. Interdicitur enim sacerdotibus tam rubor vestium quam viredo cum aliis novitatibus mundanis, ad denotandum quod crudelitas lasciva et secularitas sunt in clericis suspendenda. Latitudo vero corone signat per abrasionem temporalium denudacionem intellectus et affectus ad bona que sursum sunt. Abrasio vero pilorum in circulo sensuum specialiter in religiosis signat subtraccionem temporalium, per que sensus secularium suffocantur; et corona iusticie expectatur in eis, cum ad imitacionem Apostoli castigant corpus suum et in servitutem redigunt stricte contenti presentibus. Et sic videtur michi quod omne genus viancium a Christo per peccatum adulterans est saccus plenus mendacio, sic quod ad omnem punctum nostri est mendacium cum peccato, sic quod deserentibus Christus et necessariora bona mundo abscondita potest verificari dictum Christi Matth. XII, 39 Generacio prava et adultera signum querit. Cum enim sensibilibus et mundanis afficimur, de illis loquimur, illa prosequimur et in illis affectu delectato postpositis spiritualibus quietamur. Unde signum huius est quod nos cleri, dimisso signato, [p. 290] tamquam layci legentes literas quarum sensum nescimus, nimis appreciamur cerimonias et sensibilia humanitus instituta ut plus ponderamus quod alba sacerdotis anglici habeat in sinistris humeris biffurcatam varietatem, superinfictam secundum formam humanitus adinventam, quam appreciamur primum mandatum decalogi. Illa enim signat divisionem Anglorum a fide post Britones usque ad tempus Gregorii, quo per eius discipulos sunt conversi. Et revera iste ritus debet generaliter in omnibus christianis trahi in communem: alie naciones usque ad Romanum pontificem debent instar ribaldi vestimenta christianitatis gerere cum labello, ut si iste papa haberet tot commissuras in vestibus, quociens aliquis papa a fide ceciderit ipse forte gereret tunicam pictaciis consutam et non tunicam inconsutilem Ihesu nostri. Et sic patet falsitas in signis episcopalibus introductis.

[ENGLISH]

## ¶4 · 290.20–290.27

> [p. 290] Unde baculus signat pastoris officium ad minandum et conprehendendum oves morbidas, ut sanentur, sed postquam corona baculi versa est in aurum preciosum et frigidum formasset in figuram artificiosam adinvencionis humane, dedignatur pastor cesareus refrigescente caritate curam apostolicam ovibus Christi impendere, sed in subtilitate secularis officii sigillatur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 286.30: Certain ornaments reserved to the high priest.
- 287.1: Vestments common to all priests and their significance,
- 287.7: The Amice.
- 287.14: The Alb.
- 287.21: The Maniple.
- 287.27: The Stole.
- 288.8: The Chasuble.
- 288.28: The Dalmatic.
- 289.1: It signifies for deacons what the chasuble does for priests.
- 289.13: Signification of the tonsure,
- 289.22: too often falsely signified.
- 290.1: attention to rites and and vestments.
- 290.20: Now the significance of all the hishop's ornaments is changed to evil.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 287: *manipulam* [NW]
  - 287: *misse* [THIN]
  - 287: *ne* [THIN]
  - 287: *adulterinis* [THIN]
  - 287: *sensacionibus* [THIN]
  - 287: *temptet* [THIN]
  - 287: *mentem* [THIN]
  - 287: *nec* [THIN]
  - 287: *stricta* [R3]
  - 288: *10* (old-style arabic 10 (Act. XV, 10)) [R4]
  - 288: *por* (word split by the folio bar (por | tamus, 233a); printed first part) [NW]
  - 288: *tamus* (word split by the folio bar (por | tamus); printed second part) [NW]
  - 288: *a* (print "casulam a | dextris"; the main scan lost a (end of the line above the box)) [INS?]
  - 288: *planeta* [NW]
  - 288: *Et* (main "daimatic" is the English side-note "Dalmatic."; the print line opens "Et est aliud") [R4]
  - 288: *levite* [NW]
  - 289: *habet* [R4]
  - 289: *levitis* [NW]
  - 289: *∅* (the inserted i is the folio bar (233b) before quod) [INS?]
  - 289: *illa* (30 is the line number) [R3]
  - 290: *layci* [THIN]
  - 290: *legentes* [THIN]
  - 290: *cerimonias* [NW]
  - 290: *humanitus* [R3]
  - 290: *caritate* [R3]
  - 287: *longenimitatis* (LEFT-nw: hyphenated longe-|nimitatis) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 286:
21. Job XVIII, 33. 29 Magister Historiarum: vid. Petr.
Comest. 1. c.

p. 287:
1. Codd. in marg. : Ornamenta sex sacerdotis. 2. Codd. in marg. :
Amicta. 10. B: ab veterioribus. 11. Codd. in marg. : Alba camisia ;
A in marg. : Estimo quod scriptor omisit misticacionem de \ona. 22. Codd.
in marg.: Stola. 29, 3o. B: longanimitas.
4. Cf. et Hugonem De Sacrament. II, p. IV, cap. IX et seqq.

p. 288:
3. Codd. : debent. 8. Codd. in marg. : Casula. 28. Codd. in
marg. : Dalmatica.
27. Joh. I, 5.

p. 289:
3. Codd.: dyahnatica. 7. Codd.: Quolibet. 8. peroracionis ; an
preparacionis. 8. Codd. in marg. : Vestis rubea et viridis est sacerdolibus
prohibita. 9 Codd. in marg.: Plata. 22. Codd. in marg.: Saccus
plenus mendacio. 28. Codd. in marg. : Signorum cultus est generacio
De Potestate Pape. Iq

p. 290:
12. Codd.: comunam. 20. A in marg. : Bacuhts. 2S. Codd. in
marg.: Crux episcopomm. 32. Codd. in marg. : Atiulus.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 286: Numqtiid nosti ordinem celi et pones racionem eius in terra?
p. 287: Si quis loquitur, quasi sermones Dei | super se iugum Domini
p. 288: luceat hix vestra coram hominibus.
p. 289: Generacio prava et adultera signum querit. | Signorum cultus est generacio prava.
```
