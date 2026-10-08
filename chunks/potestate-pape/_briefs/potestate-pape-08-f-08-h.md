# Translation brief: potestate-pape 08-f–08-h

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-08-f.md chunks/potestate-pape/wyc-potestate-pape-08-g.md chunks/potestate-pape/wyc-potestate-pape-08-h.md` once and fix what it reports.
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
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
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
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| redarguere | to refute | T. p. 365. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| globus | band | Derogatory collective (*globus reprobus*, *globos claustralium*). Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of things (*globus temporalium*): "mass", untagged with a note (2026-10-02). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| acephala; incapitata | acephalous; unheaded | *Incapitata* pairs with *capitatus*. Ruled 2026-10-02 (*Eccl.* 18, 435.20–23). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| negociatores | dealers | Kept apart from *mercantes* "traders" (*Eccl.*); the servants of the talents parable (Matt. 25). Ruled 2026-10-07 (*Pot. pape* 101.7). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 08-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "185.1–188.17"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "806 words; 739 unanimous or majority-real; 55 settled by vote (DEL 1, R2 35, R3a 15, R5a 4); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n246–n249 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 6: [TITLE]

## ¶1 · 185.1–185.18

> [p. 185] Itaque infra quemcumque centenarium annorum a tempore dotacionis ecclesie facta est notanda contencio inter papas. Sed abhinc ex superhabundanti cautela dyaboli plus cecata est iniquitas Antichristi, cum autem apostoli habuerunt planiores revelaciones quam prophete veteris testamenti et maiorem zelum habeant ad profectum ecclesie, non licet discredere quin prophetaverant hos eventus precipuos ut periculum infidelitatis, ita ut tractus ad inferos caucius caveatur, quin indubie istorum antichristorum dissensio dicit patenter, si velimus attendere, quod gradus et vita eorum discordant; et displicent suis autoribus, Et causa dissensionis est honor mundanus vel globus temporalium, quia aliter non foret facile fingere, unde dissenciendo contendant pocius circa illud officium post dotacionem ecclesie quam perante.

[ENGLISH]

## ¶2 · 185.19–187.20

> [p. 185] Ex ut quibus supra colligo tamquam michi probabile, quod Christus summus propheta Matth. XXIV, 5 dicens, quod mulli venient in nomine suo, dicentes se esse Christus, et multos seducent, intelligit de Romanis pontificibus blasfeme mencientibus, quod sunt eius vicarii, quos autorizat ad taliter dominandum. Et sic videtur michi probabile quod idem sit sensus Apostoli II. Tess. II, 3, 4 ubi prophetat, quod ante diem iudicii oportet, quod veniat dissensio primum et reveletur homo peccati, qui extollitur super omne quod dicitur Deus. Sed tercio videtur michi probabile quod debemus quoad hoc inniti Christi consilio, quod facta tali divisione iam diebus nostris quibusdam dicentibus: Ecce hic Avinione est Christus et aliis dicentibus, nolite credere, quia indubie [p. 186] opera fidelia oportet ostendere Christi vicarium, cui opinio vel eleccio humana est impertinens. Opera autem Christo contraria ostendunt multis quod uterque eorum sit antichristus et per consequens fugiendus, ymo credo indubie utroque clero, qui istis ambobus consensit, neuter clerus habebit contra reliquum evidenciam quod suus episcopus pro quo zelat sit papa, quia (ut alias ostendi) error eligencium non impedit, quin electus sit papa. Nec nos possumus contra illos ex operibus vel revelacione convincere, quod noster Romanus pontifex sit papa. Ideo videtur securum, cum melius foret ecclesie, quod nullus foret huiusmodi, quod vivamus ut ante dotacionem, quando ecclesia communiter regulabatur per socios, et pro neutro asseramus blasfema mendacia, cum tota vita sua debet capi relicto ambiguo, nam nichil nocius, quam quod stat utrumque istorum esse pseudopapam et per consequens Antichristum. Nec est racio vel auctoritas cogens quod alter istorum sit papa, igitur ista fides non est ecclesie imponenda; et nimis leve foret quod utraque istarum parcium imponat relique scisma vel heresim sine causa notoria, et specialiter cum persone aggregate religiosorum in ista sentencia sint divise. Stat enim quod homines inculpate eligant Antichristum, ut patet ex dictis; et stat quod homines viciosissime eligant quem Deus bene elegerit; ideo patet quod argumenta neutram partem necessitant ad credendum suum prepositum esse papam. Ideo nos Anglici debemus quiescere in antiqua religione Christi ut olym, neutri parti credendo nimis faciliter. Si enim uterque istorum est Antichristus, sine tali capite debet ecclesia regulari, sed quis scit hoc? Docet [p. 187] enim Augustinus in De Verbis Domini Sermone XLV ex triplici scripture testimonio signum evidentissimum Antichristi: primum est illud Apostoli Rom. X, 3: Ignorantes Dei iusticiam et suam volentes constituere, iusticie Dei non sunt subiecti. Unde quia illud signum concludit infallibiliter Antichristum; exponit Augustinus idem pertinencius: Quid, inquit, est aliud ignorare Dei iusticiam et suam velle constituere nisi dicere, ego sanctifico, ego iustifico, quod ego dedero sanctum est, dimitte Deo quod Dei est, agnosce, homo, quod hominis est; ignoras Dei iusticiam et tuam vis constituere, iustificare me vis, sufficit tibi ut mecum iustificeris. Vendicant enim quidam secundum leges suas regere totum mundum et tamen nesciunt secundum leges Dei se ipsos regere vel suos domesticos, et cum illi habent pseudodiscipulos publice asserentes quod ipsi melius et universalibus regunt ecclesiam quam Christus vel eius apostoli.

[ENGLISH]

## ¶3 · 187.21–188.17

> [p. 187] Secundum testimonium est illud Joh. V, 43 tactum superius: Ego veni in nomine patris mei et non accepistis me, Si alius venerit in nomine suo, illum accipietis. Super quo dicit Augustinus: De Antichristo dictum est, et omnes sic intelligunt: Ego veni in nomine patris mei et non suscepistis me, si alius venerit in nomine suo, hunc suscipietis. Sed audiamus Johannem: Audistis, quia Antichristus venit, et nunc Antichristi multi facti sunt. Quid autem expavescimus in Antichristo, nisi quia nomen suum honoraturus est et nomen domini contempturus. Quid aliud facit, qui dicit: Ego iustifico? respondet eis subditus, ego ad Christum veni [p. 188] non pedibus sed corde; ubi evangelium audivi, ibi credidi, et ille: Non es mundus. Quare? quia non fui ibi. Hec Augustinus. Et patet, cum oppositorum est eadem disciplina, Antichristus autem et Christus sunt oppositi, oportet quod scriptura condiciones Christi detegens, indirecte condiciones detegat Antichristi. Ideo dicit capitulum predictum de Antichristo: Scrutamini scripturas, quia putatis in illis habere vitam eternam, et ille sunt que testimonium perhibent de me. Unde redarguendi sunt fingentes quod solum erit unus Antichristus, qui procreabitur ex fratre et moniali, quia certum est quod omnis dampnandus erit Antichristus, et scriptura docet nos sic loqui de illo; ideo fabule tales celant multos Antichristos et palliant eorum versucias, sic quod incaucius precaventur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 185.1: In every century since endowment there have been quarrels for the popedom.
- 185.14: This strife has been due to ambition or avarice.
- 185.19: It is to such that Christ's prophecy of Antichrist refers.
- 186.2: The works of the rival popes shews they are antichrists.
- 186.12: The Church would be better without either of them.
- 186.31: We English should not accept either.
- 187.1: The signs of Antichrist as taught by Augustine.
- 188.6: There is not one sole Antichrist but many.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 185: *ut* (print has quibus ut supra colligo tamquam michi; only ut stands here (DEL at 110 drops main's ut, michi is at pos 114)) [INS?]
  - 185: *michi* [R3]
  - 185: *veniat* (print has v) [R4]
  - 186: *cui* [R4]
  - 186: *opinio* [R6]
  - 186: *melius* [R3]
  - 187: *et* [R3]
  - 187: *suam* (5 is the line number) [R4]
  - 187: *illum* [R3]
  - 188: *ille* [R4]
  - 188: *Antichristi* [R3]
  - 188: *et* [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 185:
10. Codd.: ita et. 28. Discessio in Vulgate.

p. 186:
34. AB in marg. : Antichristi Iria signa ponit Augustinus.

p. 187:
4. Codd.: Rom. 1. 10. Cod. : ego sanctifico, ego sancttfico. 21. B
in marg. : Nota ; A in marg. : /. 28. B in marg.: Nota.
1. Serm. GXXIX Opp. tom. V. 633. 28. I. Joh. II, 18.

p. 188:
I. ibi; cod.: et. 4. A: eadem deest. 18. A in marg.: 3.
3. Serm. CXXIX 1. c. 8. Joh. V, 3q. 25. Joh. V, 19.
29. Joh. V, 3o.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 08-g: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-g
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "188.18–192.9"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "824 words; 743 unanimous or majority-real; 65 settled by vote (R2 41, R3a 19, R5a 4, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n249–n253 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 7: [TITLE]

## ¶1 · 188.18–190.15

> [p. 188] Tercium testimonium notificans Antichristi discipulos est quod sint gloriam ab invicem exspectantes et gloriam, que a solo Deo est, non querentes, ut docet Veritas Joh. V; nam in hoc sunt Christo contrarii, qui instanter fecit actus iustissimos, et correspondenter ad illos exspectavit gloriam a solo Deo. Unde in predicto capitulo Johannis de Antichristo: Amen amen dico vobis, non potest filius a se ipso facere quicquam, nisi quod viderit patrem facientem. Ex quo patet quod oportet omnia opera Christi esse iustissima, et sic intelligitur auctoritas Christi sequens: ludicium meum iustum est, quia non quero voluntatem meam sed voluntatem eius, qui misit me, patris. Et patet veritas connexionis sequentis: Si ego [p. 189] testimonium perhibeo de me ipso, testimonium meum non est verum, sed pater testimonium perhibet. Si eciam Baptista sine Christi exaccione testimonium perhibuit Veritati: Ego, inquit, habeo testimonium maius Johanne, opera enim que dedit michi pater ut perficiam; ipsa opera que ego facio testimonium perhibent de me. Ex istis textibus eliciunt sancti versucias antichristi, ipse enim summe sitit honorem et lucrum mundanum, cum Christus omnino fecit contrarium. Ideo docet Augustinus ubi supra quomodo Antichristus nitetur quod sine eius seculari obediencia non est salus, quod cum non habet testimonium ex scriptura, fingit in multis epistolis testimonium a se ipso: Si boni sumus, inquit Augustinus, facite quod scriptum est: Imitatores mei estote, sicut et ego Christi. Si autem mali sumus, quod Deus magis facit, sic nec deserti estis nec sine Consilio remansistis; audite dicentem: Que dicunt facite, que autem faciunt nolite facere. Sed prelati contra hec: Nisi boni fuerimus, peristis. Sed hic est alius, qui veniet in nomine Christi. Sed hunc Antichristum alloquor, igitur vita mea ex te pendebit et salus mea ex te religabitur: Sed fundamentum aliud nemo potest ponere nisi Christum, veni igitur mecum, Antichriste, si vis esse super petram, et noli velle esse michi pro petra. Et patet ex textu Johannis sequenti, quomodo Christus nititur testimonio j iustorum operum et scripture, non autem solis verbis hominum, ut superius dicit Crysostomus esse consuetudinem Antichristi; hec considera et applica ad facta Romanorum pontificum et vide si consonant ritibus antichristi, [p. 190] quod si uterque istorum dicit conformiter ad illam extra vagantem decretalem Bonifacii VIII Unam Sanctam quod nisi quis obediat sibi ut capiti tocius ecclesie, non est de numero salvandorum, oportet utrumque relinquere tamquam alterum Antichristum. Multi enim erant tales de Romanis pontificibus, unde narrat predictus cronicans in libro suo de Floribus Historiarum, quomodo anno gracie DCV papa Sabinianus liberalitatem beati Gregorii predecessoris sui derogavit et sub hoc obtentu manum egenis subtraxit, Gregorius eum per visum ter pro culpa tenacie et huius derogacionis increpavit, et quarto horribiliter increpans et comminans in capite percussit, quo dolore vexatus paulo post obiit.

[ENGLISH]

## ¶2 · 190.16–191.5

> [p. 190] Item, simile narrat Cestrensis libro suo VII MCCVI ad papam Innocencium misit Robertus Lynconiensis epistolam invectivam satis et tonantem, pro eo quod ecclesias Anglie indebitis exaccionibus vexare videretur; hac de causa ad curiam vocatus est, et cum ibi molestaretur, appellavit constanter a curia Innocencii ad tribunal Christi; unde contigit, quod Roberto in Anglia obeunte audita est vox in curia pape: Veni miser ad iudicium; repertusque est in crastino papa exanimis, quasi cuspide baculi in latere percussus. Qui licet perspicacius effulserit miraculis, transferri tamen in sanctorum cathalogo a curia non est permissus. Nec est putandum istos sanctos iregularitatem vel offensam Dei incurrere ex percussione letali summorum pontificum; qui viderunt quod erant precipui [p. 191] Antichristi, persequentes ecclesiam, etreceperunt mandatum a Domino sic tractare hostes ecclesie, pro cuius prosperitate secundum religionem et institucionem Christi, dum erant vivi, a Deo zelaverunt.

[ENGLISH]

## ¶3 · 191.6–191.28

> [p. 191] Item, notat lex ecclesie, quomodo Marcellinus episcopus urbis Rome, qui foret dux christiani exercitus thurificavit ydolis, ut patet distinccione XXI Nunc autem divina, ubi dicit glossa ordinaria quod consilio congregato Confessus quod fecerat et in se tulit sentenciam deposicionis, et post (ut reor) exutus ab illo officio veniens coram Dyocleciano, confessus est se esse christianum et martyr effectus est; considerans enim suam blasfemam vecordiam in papatu et preparans se per satisfaccionem ad martyrium, pro nichilo habuit huiusmodi dignitatem; diebus autem nostris, ut plus involverunt se seculari dominio sunt peiores, quia Christus non diceret de eis: Omnia quecumque dixerint vobis, facite. Nec illi ut sacerdotes legis veteris putant habere vitam perpetuam in scriptura, cum ex eius ignorancia multi antichristi cadunt in multas blasfemias et ex scripture contemptu multos, qui pie vivere volunt in Christo persequuntur, nituntur enim viis variis facere, ut credantur quod sint caput universalis ecclesie, et ipsa indubie est tunc cum paribus acephala quoad ipsos.

[ENGLISH]

## ¶4 · 191.29–192.9

> [p. 191] Sed Augustinus in De Verbis Domini ubi supra: Quid, inquit, tibi fecit ecclesia ut eam velis quodammodo decollare? qui, inquit, sic decollare [p. 192] vult et corpus et caput conatur occidere. Cum enim non sit communicacio Christi ad Belial, quomodo Christo tam contrarius in vita et moribus erit ex eius participio caput ecclesie? Erubescunt, inquit, negare Christum, hoc tamen maius est, cum Christum non vidimus sed credimus, verba autem illius nobiscum sunt, in quibus ipsum negamus, comparate itaque vos Iudeis, illi contempserunt pendentem in ligno, vos contempnitis sedentem in celo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 188.18: Antichrist seeks the praise of man and not of God.
- 189.11: Antichrist claims that without obedience to him is no salvation,
- 189.27: He rests his claims on witness of men,
- 190.1: See how like the Roman pontiffs are to Antichrist.
- 190.16: Grosseteste and Innocent IV.
- 191.6: Repentance and martyrdom of Marcellinus.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 189: *antichristi* (print has lower-case a) [R4]
  - 189: *facite* (hyphenated fa-cite; main token covers whole word) [R4]
  - 189: *Antichristi* [R4]
  - 190: *Bonifacii* [R4]
  - 190: *Sanctam* [R3]
  - 190: *paulo* [R3]
  - 190: *papam* [R3]
  - 190: *iudicium* (folio bar before it (208c)) [R3]
  - 191: *tulit* [R3]
  - 191: *decollare* [THIN]
  - 192: *vult* (print has v) [THIN]
  - 192: *conatur* [THIN]
  - 192: *nobiscum* [R3]
  - 192: *illi* [R3]
  - 192: *celo* [R3]
  - 189: *Augustinus* (LEFT-odd: print = Augustinus) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 188:
I. ibi; cod.: et. 4. A: eadem deest. 18. A in marg.: 3.
3. Serm. CXXIX 1. c. 8. Joh. V, 3q. 25. Joh. V, 19.
29. Joh. V, 3o.

p. 189:
21. B: fuerimus deest. 32. B: applica de.
4. Joh. V, 36. i5. Opp. tom. V, 636.

p. 190:
2. AB in marg. : Obediencia pape nota bene. 9. DCCV; codd. :
LXVll. 10. AB in marg. : Greporins sanctus papa occidit siinm suc-
cessorem. 17. 1206 (sic). Non est Innocentius III sed Innocentius IV.
18. AB in marg.: Appellavit Lincolniensis ad tribunal Christi.
3. Extrav. Comm. lib. I, tit. VIII, cap. 1. o. Polvchronic.
Ranulphi V, 412. 17. Ihid. VIII, 240.

p. 191:
6 AB in marg.: Marcellinus papa ydolatravit. 12. B: exustus.
18. Codd.: in secidari. 26. AB arg. : Caput ecclesie,
9. Cap. VII. Cf. Glossam ordinariam ed. Ven. i5g5, p. 91.
19. Matth. XXIII. 3. 3o. Serm. CXXX De Verb. Joh. VI. Opp.
tom. V, 637. 3i. Sermo XLVI. Opp. tom. V, 23o.

p. 192:
4. AB in marg. : Periculum falsorum fratram. 24. AB in marg. :
Redimere lempus quid est. 28. B : ecclesie deest.
18. Ibid. p. 803/4.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 192: vnlt et corpus et caput couatur occidere. | negare Christum, hoc tamen maius est, cum Chri- | stum non vidimus sed credimus, verba autem iliius uobiscum suut, in quibus ipsum uegamus, comparate itaque vos Iudeis, iiii contempserunt peudeutem in ligno, vos contempnitis sedentem in ceto. | me audis, incipe in Christo vivere, et probabis quod dico, nam cetcra pericnla, de quibus Apostoius, possunt quiescere,™ pericula autem in faisis fratribtts usque ad finem secuii quiescere non noverunt. | hoc est, | tempus redimere, quando aiiquis infert tibi litem | perdere substauciam, ut Deo vaces, uon litibus.
```

---

## Chunk 08-h: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-08-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-08-h
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "192.10–194.6"
divisions: "cap. 8 (heading 'CAPITULUM OCTAVUM.' at 165.1); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "427 words; 400 unanimous or majority-real; 18 settled by vote (DEL 2, R2 8, R3a 7, R5a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n253–n255 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 8, part 8: [TITLE]

## ¶1 · 192.10–194.6

> [p. 192] Et ne pallietur huius negacionis negacio, que potissime consistit in facto, attendamus quomodo superiores satrape, quibus regeretur ecclesia, honorificum reputant legem Christi ignorando contempnere eos qui pie volunt vivere, et pericula eorum, sicut debent ex Ezechielis XXXIV detegere, nituntur omnimode tribulare, ut ostendit Augustinus in De Verbis Domini Sermone LXXXIX: Quisquis, inquit, me audis, incipe in Christo vivere, et probabis quod dico, nam cetera pericula, de quibus Apostolus, possunt quiescere, pericula autem in falsis fratribus usque ad finem seculi quiescere non noverunt. Et intelligit modo Apostoli per falsos fratres generaliter quoscumque falsos nomine christianos. Redimamus itaque tempus, quantum dies mali sunt; hoc est, inquit, tempus redimere, quando aliquis infert tibi litem perdere substanciam, ut Deo vaces, non litibus. Quia, inquam, superiores ecclesie factis negant hanc legem, quam Chrisus in vase suo loquitur, ideo statim multitudine persequuntur eum, qui nititur dare fidem in populo, quod ipsi dicte legi apostoli precipue sunt astricti; et sic ipsi et multi per ipsos perdunt tempus propter lucrum [p. 193] turpissimum, vocatum a ceteris commodum temporale. Nec sunt audiendi discoli, qui fingunt quod omnis res durans sit tempus, et sic clerus emens ecclesiastica beneficia vel secularia dominia emit tempus, quod est hodie necessarium clero, cum layci clericis oppido sunt infesti; antichristiana deliramenta sunt ista et sensus Apostoli subversiva. Intelligit enim Apostolus tempus proprie pro duracione successiva tocius mundi, que quamvis omni homini et omni corpori sit communis, tamen quando homo in illa secundum legem Dei progreditur et allocatur in die novissimo de expensione impensi temporis sibi ipsi proficit ad salutem tunc propter illum proprium et utilem modum habendi redimit sibi tempus. Redimit dico; quia Christus emit tempus toti ecclesie, cum aliter pure naturaliter numerasset tempus hominum. Sed merito Christi factum est tempus acceptabile, quia in brevi tempore homo ex accepcione divina potest beatitudinem promereri. Sed cum ille qui creavit te sine te, non iustificat te sine te, necesse habemus doctrinam Apostoli Ephes. V, 15— attendere: Videte, inquit, quomodo caute ambuletis, redimentes tempus, quoniam dies mali sunt. Oportet igitur preter redempcionem generalem temporis per Christum nobis tempus redimere, quod tunc secundum Augustinum facimus, quando temporalium affluenciam et vitam voluptuosam pretermittimus vel mutamus, ut Christo vivamus accepcius et nobis utilius, tunc enim novo modo habendi acquirimus nobis tempus. Et secundum Augustinum iudicium illius episcopi, ymo iudicium Christi, in ipso sufficeret finem imponere omniliti. Ideo illud iudicium debet [p. 194] dux christiani exercitus, scilicet vicarius Christi, magis attendere, cum filii huius seculi sunt prudentes et callidi; ut ex stultis commerciis habeant hic dies prosperos quoad mundum, sed mali sunt et fatui cum ex tali negociacione dies una perditur valens mille.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 192.10: Our prelates deny Christ in deed.
- 193.12: What it is to redeem the time.
- 193.26: It is to forego a life of self indulgence

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 192: *ut* [R3]
  - 193: *illa* [R3]
  - 193: *allocatur* [NW]
  - 193: *illum* [R3]
  - 193: *quomodo* (hyphenated quo-modo; main token covers whole word) [R3]
  - 193: *caute* [R3]
  - 193: *Augustinum* (hyphenated Augusti-num; main token covers whole word) [R4]
  - 193: *sunt infesti;* (W-split: suntinfesti; -> sunt infesti; (two words run together)) [OVERRIDE-SCAR]
  - 193: *15—* (LEFT-odd: box on the dash of 15—16; print has 16 after it) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 192:
4. AB in marg. : Periculum falsorum fratram. 24. AB in marg. :
Redimere lempus quid est. 28. B : ecclesie deest.
18. Ibid. p. 803/4.

p. 193:
11. Codd. : sensum legem. 12. Cod. : allocaciter. 23, 24. B: quo-
De Potestate Pape. I 3

p. 194:
7. A in marg. : Capitulum Q. 12. A in marg.: Caput ecclesie ne-
cesse est esse Chrialum. Nola Gregorii pro papa JienJo, pro archieph-
copis, pro archipresbyteris et archidiaconis. 26. In Dccr. : literato.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 192: vnlt et corpus et caput couatur occidere. | negare Christum, hoc tamen maius est, cum Chri- | stum non vidimus sed credimus, verba autem iliius uobiscum suut, in quibus ipsum uegamus, comparate itaque vos Iudeis, iiii contempserunt peudeutem in ligno, vos contempnitis sedentem in ceto. | me audis, incipe in Christo vivere, et probabis quod dico, nam cetcra pericnla, de quibus Apostoius, possunt quiescere,™ pericula autem in faisis fratribtts usque ad finem secuii quiescere non noverunt. | hoc est, | tempus redimere, quando aiiquis infert tibi litem | perdere substauciam, ut Deo vaces, uon litibus.
p. 193: quomodo caute ambuletis, redimentes tempus, quoniam | dies mali sunt.
p. 194: In apibus princeps unus est, grues unam sequuntur | ordine \ limitato. Imperator unus, iudex unus pro- | vincie. Romaautem condita duosfratres regessimnl habere uou potuit, sed fratricidio dedicatur. In Rebecce utero Esau et Yacob bella gesserunt. Sic
```
