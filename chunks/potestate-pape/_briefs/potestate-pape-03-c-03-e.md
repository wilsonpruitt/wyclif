# Translation brief: potestate-pape 03-c–03-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-03-c.md chunks/potestate-pape/wyc-potestate-pape-03-d.md chunks/potestate-pape/wyc-potestate-pape-03-e.md` once and fix what it reports.
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

## Glossary (the 211 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
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
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| pencio annua | yearly pension | Ruled 2026-09-28 (3 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| calumpnia (ponere / capere) | challenge (to lay a challenge against / to be open to challenge) | The disputant's formal objection to a premiss. Ruled 2026-10-02 (*Eccl.* 16, 363.18, 363.24, 367.11). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
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

## Chunk 03-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-03-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-03-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "51.11–55.26"
divisions: "cap. 3 (heading 'CAPITULUM TERCIUM.' at 43.10); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1017 words; 903 unanimous or majority-real; 81 settled by vote (R2 34, R3a 12, R5a 34, R6a 1); 33 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n112–n116 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 3, part 3: [TITLE]

## ¶1 · 51.11–52.2

> [p. 51] Quamvis enim sensus misticus scripture non sit de se evidens ignaris ad probandum scolastice figuratum, tamen si probari potest ex racione vel scriptura alia quod sensus iste misticus intentus fuerat ab autore; tunc sensus ille est equivalens literali; et sic sepe probat Apostolus ex figuris veteris testamenti figuratum allegorice in novo, ut patet I. Cor. X. Gal. IV et Heb. VII. Cum igitur non dicetur quid pertinencius figurarunt ista singulariter facta Petro quam prerogativam Petri super alios; videtur quod iste suasiones quietarent fidelem theologum ad fidem questioni proposite adhibendam. Dicat igituradversarius istam sentenciam, vel quod aliquid est a Christo inpertinenter factum; aut ex indifferencia positum in scriptura; vel aliter dicat quid ordo et singularitas prenarratorum operum quoad Petrum pertinencius quam eius preeminenciam super alios figuraret. Cum enim scriptura sacra exprimit et racio necessitat oportere aliquem apostolum esse talem, ecclesia autem generaliter credat hoc de Petro, Deus notabiliter permitteret [p. 52] ecclesiam suam a principio oberasse, si isti fidei falsitas sit substrata.

[ENGLISH]

## ¶2 · 52.3–55.26

> [p. 52] Item, secundo ex opinionibus Petri post ascensionem eadem veritas probabiliter convinci potent, nam soli Petro ostensum est lintheum submissum de celo, in quo erant omnia quadrupedia et repencia terre et volatilia celi, ut patet Act. X, 13 et XI, 7 et sibi soli dictum est de omnibus illis animalibus: Surge Petre, occide et manduca. Lintheum autem quatuor iniciis submissum signat superficiem terre habitabilis hominum, cuius planicies est contexta et trita ut lintheum descendente influencia celi ab oriente, occidente, borea et austro ad temperandum soli planiciem ad usum hominum. Illa autem tria genera animalium submissa in lintheo signant per ordinem seculares dominos ut quadrupedia, vulgus ut terre repencia, et clerum ut volatilia in consideracionem contemplativam temporum volancia. Ista quidem tria genera hominum integrant incolas huius mundi. Petrus autem surrexit armatus virtutibus et occidit de istis tribus generibus, cum extinxit in eis mundialitatem et fecit eos non homines quoad mundum. Sic enim accipitur homo sepius in scriptura, ut patet I. Corinth. III, 3: Cum sint inter vos zelus et contencio, nonne carnales estis et secundum hominem ambulatis? Unde beatus Petrus verbo et opere interpretatus fuit visionem ymaginativam ad hunc sensum, quod manducare suum erat perversos mores in eis prescindere et eos personaliter incorporare ecclesie; sic enim dicit Christus Joh. IV, 32: Ego cibum habeo manducare quem vos nescitis. Quando enim predicator, qui Canticorum IV, 2 dicitur dentes sponse, gladio spiritus occidit carnalitatem et ore ecclesie con- terit ad penitenciam convertendos: tunc spiritualiter comedit conversos assimilando eos in [p. 53] membra matris ecclesie, quod officium pertinuit Petro primarie. Unde Actuum I, 15 legitur quod exsurgens Petrus in medio fratrum oslendit per scripturam veteris testamenti quod oportet loco Yude proditoris alium episcopum eligere, qui suppleat vices suas; et sic secundum prioritatem dignitatis celebravit eleccionem Mathie. Item, Act. II, 14 legitur quomodo Petrus cum undecim elevavit vocem suam loquens pro omnibus contra imponentes eis ebrietatem, ostendens ex scriptura quod sit spiritualis replecio per Spiritum Sanctum Yohelis III prelocuta. Item, Act. II, 31 consequenter predicavit Judeis de resurreccione et predixit eis pre omnibus apostolis quid esset eis necessarium ad salutem, et infra capitulo tercio, 1, 2, Petro et Johanne ascendentibus in templum Petrus habuit preposituram locucionis in claudi sanacione sicut et prenominacionem in serie scripture, Petrus eciam pro omnibus respondit magistratibus templi, ut patet Act. capitulo IV, et pro omnibus protulit mortis sentenciam in Ananiam et Saphiram, ut patet V capitulo, et sic in Symonem magum, Act. VIII. Item, in consilio generali, de quo Act. XV, Petrus protulit pro omnibus sentenciam quod conversi ex gentibus non debeant circumcidi nec legis cerimonias observare. Talem autem preposituram usurpare non presumeret tam sanctus apostolus post missionem Sancti Spiritus docentis ipsum omnem veritatem et confirmantis in ipso omnem a Christo instructam humilitatem, nisi sciret pertinere suo officio accipere magnanimiter huiusmodi dignitatem, que videtur specificata a Christo Math. [p. 54] XVII, 23, 26, quando exactores didragmatis in presencia apostolorum singulariter dicunt Petro tamquam eorum maximo: Magister vester non solvit didragma? quod Salvator docuit in effectu, quando Petrum solum in solucione census sibi coniunxerat: Vade, inquit, ad mare et mitte hamum, et piscem qui primo ascenderit tolle et aperto ore eius invenies staterem, illum sumens da illis pro me et pro te. Tercio confirmatur ista sentencia ex testimonio sanctorum. Nam beatus Dionysius post autores scripture testis precipuus in libro suo De Divinis Nominibus capitulo tercio vocat beatum Petrum verticalem, id est, capitalem seu capitaneum, motus ex dicto Christi Joh. I, ubi in prima vocacione Petri nominat eum Cephas, quod sonat caput. Et libro suo De Ecclesiastica Yerarchia V capitulo vocat eciam beatum Petrum discipulorum verticalem, quod ostendit ex hoc quod ipse principaliter celebravit eleccionem Mathie loco Yude, ut patet Act. I. Unde iste sanctus beati Pauli precipuus discipulus et in morte assistens in libello quem scripsit De Morte Apostolorum sic alloquitur Thimoteum: Cum separarentur ab invicem ducti ad loca supplicii, Paulus Petrum alloquitur in hec verba: Pax tecum, fundamentum ecclesiarum et pastor ovium et agnorum Christi. Hec testimonia non testaretur tam sanctus et tam subtilis theologus se sensibiliter audivisse et tam diligenter notasse, nisi crederet beatum Petrum fuisse caput collegii Apostolorum post [p. 55] mortem Christi, sicut ecclesia sepe inculcat in servicio huius sancti. Et eandem sentenciam tenent leges ecclesie, nam XXIV, q. I Rogamus Marcellus papa sic loquitur: Rogamus vos fratres, non aliud doceatis quam quod a beato Petro et a reliquis apostolis accepistis, ipse est enim caput tocius ecclesie, cui ait Dominus: Tu es Petrus. Etidem patet XXI dist. capitulo. novo, etXXII dist. capitulo. Omnes et Sacrosancta. Item, XXIV, q. Ill De illicita. Item beatus Augustinus in De questionibus veteris et nove legis, LXXIX capitulo, dicit, quod Petrus erat primus inter apostolos. Ideo dicit Christus quod Petrus solveret pro se didragma, ipsum, inquit Augustinus, constituit caput eorum, ut pastor esset gregis dominici. Et idem dicit cap. finali, et in libello Ad Spiritum Sanctum dicit: flere fecisti apostatam et ordinasti in summum pontificem. Nec oporteret tantum immorari in declaracione istius sentencie, nisi fuerit propter tria: primo pro declaracione autoritatum scripture per quas questio ista ostenditur, secundo ut cognoscatur sensus ecclesie, ad quem concedit Petrum habere super alios apostolos preeminenciam dignitatis, et tercio ut Petri vicarii cognoscant formam, secundum quam potestas Petri est ad pastores derivata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 51.11: A mystical sense was intended in these passages.
- 52.3: Peter's distinction continued after the Ascension.
- 52.10: His vision of the great sheet.
- 52.16: Meaning of that vision.
- 53.4: Peter's lead in electing Matthias,
- 53.9: and on the day of Pentecost.
- 53.17: Other Instances.
- 54.10: Testimony of St. Dionisyus.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 51: *Quamvis* [R4]
  - 51: *literali* [NW]
  - 51: *figurarunt* (hyphenated figura-/runt; main token covers whole word) [R4]
  - 52: *veritas* [R3]
  - 52: *lintheum* [NW]
  - 52: *Illa* [R3]
  - 52: *dominos* [NW]
  - 52: *cibum* [THIN]
  - 52: *habeo* [THIN]
  - 52: *manducare* (hyphenated man-/ducare; main token covers whole word) [THIN]
  - 52: *con-* (hyphenated con-/terit; main token holds first half (35 is the line number)) [R3]
  - 53: *oslendit* (leaf 114 zoomed: 3rd letter is tall like the d ascender, no crossbar, unlike the short crossed final t = l) [R4]
  - 53: *Yude* [R4]
  - 53: *eis* (15 is the line number) [R4]
  - 53: *1* (old-style arabic 1, x-height, zoomed) [R3]
  - 53: *prenominacionem* [NW]
  - 54: *et* [R4]
  - 54: *mitte* [R3]
  - 54: *et* [R4]
  - 54: *aperto* [R4]
  - 54: *illum* [R3]
  - 54: *∅* (English side-note word) [R4]
  - 54: *testimonio* (10 is the line number) [R4]
  - 54: *ovium* [R3]
  - 55: *non* [THIN]
  - 55: *aliud* [THIN]
  - 55: *doceatis* [THIN]
  - 55: *quam* [THIN]
  - 55: *Petro* [R4]
  - 55: *novo* (box covers In novo: the word after In) [R3]
  - 52: *superficiem* (W1: supernciem -> superficiem (scans: supernciem | superficiem | supernciem | supernciem)) [OVERRIDE-SCAR]
  - 53: *in Symonem* (W-split: inSymonem -> in Symonem (x1 in the volume; scans: insymonem | insymonem | in | insymonem)) [OVERRIDE-SCAR]
  - 52: *probabiliter* (LEFT-nw: print = probabiliter (scan readings are OCR noise)) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Matthias, (53.5).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 51:
2. B: 34; A in marg. alia manu: Nota quod sensus figuraliler equi-
valet literali. i3. Codd.: tamen sic. 19. Codd.: dicetur.
U De Civili Dominio II, 62 et III, 5 19.

p. 52:
(none)

p. 53:
3. B: ostendit deest. 14. Codd.: pro omnibus. 25. B: exi-
gentibus.
12. Recte Joel II, 28. i3. resurreccione sc. Christi.

p. 54:
12. In capitulo tcrcio Dc divinis nominibus solummodo
lcgitur: Aderat aulem et Jacobus fratcr Domini et Petrus
summa et porrectissima (heologorum summitas. Ed. Col. 1 536.
18. Rcctius: Discipulorum summum ibid. 24. Epistola apocr.
vide Pitra, Anal. sacra IV.

p. 55:
9. Cod.: Omnis. 11. Rcctius: cap. LXX\. 20. Codd.: prop-
tcrea. 27. AB iu marg. : PeLriis caput ecclesie quare nominatur.
3. Cap. XV. 9. Cap. II. Cap. Omnes = Dist. XXII, Cap. 1.
Sacrosancta, Cap. II. 10. De Illicit.a = Cap. VI. Ibid. Aug.
Opp. tom. III, App. p. 7D. Cf. In Joh. Evangel. Opp. tom. III,
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 51: ipsum solum,
p. 52: Surge Petre, occide et mandtica. | Cum sint | inter vos zelus et contencio, nonne carnales estis et secundum hominem ambulatis? | Ego cibum habeo manducarc quem vos nescitis. | dentes sponse,
p. 53: exsnrgens Petrtis \ in medio fratrum ostendit per scripturam veteris testamenti quod oportet loco | Yude proditoris alium episcopum eiigere, | Petrus cum undecim etevavit vocem suam ioquens pro omnibus | de resurreccione
p. 54: Magister vester non solvit didragma? | ad mare et mitte kamum, et piscem qui primo ascenderit tolle et aperto ore eius inveuies staterem, illum sumens da illis pro me et pro te. | discipulorum verticalem, | Cum separareulur ab invicem ducti ad loca supplicii, Paulus Petrum 2? ailoquitur in hec verba: Pax tecum, fundamentum ecciesiarum et pastor ovium et agnorum Christi.
p. 55: Rogamus vos fratres, | non aliud doceatis \ quam quod a beato Pelro et a reliqnis apostolis accepistis, ipse est enim caput tocius ecclesie, cui ait Dominus: Tu es Petrus. | De itticita. | Petrus erat primus inter apostolos. | sotveret pro se didragma, ipsum, | constituit ibcaput eorum, ut pastor esset gregis dominici. | ftere fecisii apostatam et ordinasti in summum pontificem.
```

---

## Chunk 03-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-03-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-03-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "55.27–58.7"
divisions: "cap. 3 (heading 'CAPITULUM TERCIUM.' at 43.10); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "546 words; 492 unanimous or majority-real; 42 settled by vote (DEL 2, R2 17, R3a 9, R5a 13, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n116–n119 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 3, part 4: [TITLE]

## ¶1 · 55.27–58.7

> [p. 55] Quantum ad primum, expeditum est in parte, sed pro secundo notandum quod racio quare Petrus ordinatus fuit a Christo post eum caput ecclesie fuit preeminencia virtutum ad regendum [p. 56] ecclesiam; aliter enim sapiencia patris inprovide eum constituisset ecclesie sue episcopum. Et cum omnes virtutes in genere sint connexe. patet quod Petrus habuit quandam preeminenciam in omni genere virtutum. Tres autem erant virtutes in quibus pertinencius Petrus precellerat, scilicet fides, humilitas, caritas; fides, quam oportetesse petram ecclesie, pre cellebat in Petro, propter quod ordinavit magister Matth. XVI, 16 quod ad questionem, qua quesivit de se ipso, quem dicunt homines esse filium hominis, Petrus pro omnibus responderet: Tu es, inquit; filius Dei vivi. Ubi orthodoxe confitetur humanitatem in Christo. quia signat illum prophetam promissum patribus vel Messiam. Et secunda pars confitetur Christum Dei filium naturalem, quia aliter impertinens foret confessio. Et inter omnes articulos fidei nullus est ad edificandum ecclesiam Christi pertinencior quam secundum beatum Joh. I. Joh. V, 4 Dei filius vincit mundum: Quis est inquit, qui vincit mundum, nisi qui credit quoniam Ihesus est filius Dei. Nam hoc fundamento habito consequenter credendum, quod omnia, que fecit vel docuit; sunt sine calumpnia possibili a tota ecclesia acceptanda. Ideo audivit Petrus a Domino: Beatus es Symon Baryona, quia caro et sanguis non revelavit tibi, sed pater meus, qui est in celis. Et ex ista fide accepit arras prefecture ecclesie. Et ego dico tibi, inquit, quia tu es Petrus, et super hanc petram edificabo ecclesiam meam. De quo August. super Johannem sermone ultimo sic loquitur: Ecclesia quatitur sed non cadit, quando fundatur super petram, unde Petrus nomen accepit, [p. 57] non enim a Petro petra, sed Petrus a petra, petra autem erat Christus. Et propter istas raciones tenentur superiores prepositi predicare fidem ecclesie, unde Luce XXII, 32: Ego autem rogavi pro te, ut non deficiat fides tua, et tu aliquando conversus confirma fratres tuos. Ecce quomodo Christus exauditus pro sua reverencia singulariter rogavit pro fide Petri; et secundo iniunxit sibi primatum officii et per hoc fundamentum operatus est Petrus singulariter supra ceteros apostolos; per hanc; ut supra dixi, fidem extraxit Petrus gladium et percussit servum pontificis auferendo dextram eius auriculam, ut patet Joh. XVIII; per hanc eciam introivit in monumentum Evangelista, qui prius venerat stante foras, per hanc audito ab Evangelista. quia dominus est, misit se in mare, aliis discipulis venientibus navigio ad littus, ubi Christus stabat, ut patet Joh. ultimo, et sic de aliis superexcessivis operibus, que ex vehemencia sue fidei processerunt. Primum autem allegorizatur a sancto Gregorio, ut patet XXIV? q. I, Si Petrus: Primo inquit, docetur quod aurem in specie habere non debent, quam in ministerio non habebant. Sed bonus dominus ipsi refundit auditum demonstrans et ipsos, si convertantur, posse sanari qui in passione Christi vulnerati sunt; tollit eciam gladio spirituali interiorem auriculam male intelligentis de passione Domini, dum vel prescindit errorem quo putant esse dexterum non pati pro Christo, vel quod eius divinitas paciatur. Per secundum allegorizatur quod Petrus, gentes signans, licet tardius venit ad thesaurum fidei quam Johannes ex virginitate [p. 58] sterilis, signans synagogam, tamen prius plenius introivit copiosius ad credendum in Christum. Per tercium vero signatur anagogice quod imitatores Petri et specialiter martyres in sermone fidei citius veniunt ad Christum stantem in littore eternitatis quam alii navigio, qui arte confessorum prudenter certant diu in vita cum hostibus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 55.27: Christ chose Peter for his fitness to rule the Church.
- 56.5: He excelled in faith, humility and charity.
- 56.11: 1. Faith.
- 57.20: St. Gregory's allegorical interpretation.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 55: *Quantum* [R3]
  - 56: *illum* [R3]
  - 56: *a Domino* (one token covers two printed words) [R4]
  - 56: *meus* [R3]
  - 57: *pro* (no letter before pro on the print; 5 is the line number) [NW]
  - 57: *te* [R4]
  - 57: *non* (zoomed: closed-top n) [R3]
  - 57: *fides* [NW]
  - 57: *non* (zoomed: closed-top n) [R3]
  - 57: *in* [R3]
  - 57: *habebant* (zoomed) [R4]
  - 57: *Petrus* (W1: Petrns -> Petrus (scans: petrus | petrns | petrus)) [OVERRIDE-SCAR]
- **Omitted per §3.5 / kept in the English** (margin matter): reference st. Gregory's (57.20); reference 2. Peter's bumility. m (58.8).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 55:
9. Cod.: Omnis. 11. Rcctius: cap. LXX\. 20. Codd.: prop-
tcrea. 27. AB iu marg. : PeLriis caput ecclesie quare nominatur.
3. Cap. XV. 9. Cap. II. Cap. Omnes = Dist. XXII, Cap. 1.
Sacrosancta, Cap. II. 10. De Illicit.a = Cap. VI. Ibid. Aug.
Opp. tom. III, App. p. 7D. Cf. In Joh. Evangel. Opp. tom. III,

p. 56:
19. Codd.; /. Joh. IV. Codd.: quia quam. 20. B in marg. : Excel-
lencia Petri in tribus virtutibus.
26. Matth. XVI, 17. 02. Opp. tom. IV, 1207.

p. 57:
5. ut; B: unde. 8. B: Petri deest. i3. Codd.: Joh. deest.
21. A: allegori\ant. 23. Codd.: qui in. 26. Codd.: saciari.

p. 58:
8. AB in marg.: Ilumilitas. q. B: cementem. 14. rit; B: fit.
18. A in marg.: Fundamentum ecclcsic quomodo dicitur Pctrus. 21. B:
21. Cf. St. Augustini Opp. tom. V, 1688.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 55: Rogamus vos fratres, | non aliud doceatis \ quam quod a beato Pelro et a reliqnis apostolis accepistis, ipse est enim caput tocius ecclesie, cui ait Dominus: Tu es Petrus. | De itticita. | Petrus erat primus inter apostolos. | sotveret pro se didragma, ipsum, | constituit ibcaput eorum, ut pastor esset gregis dominici. | ftere fecisii apostatam et ordinasti in summum pontificem.
p. 56: dicunt homines esse filium hominis, | Tu es, | filius Dei vivi. | Ouis est } | vincit mundum, nisi qui credit quoniam Ihesus est filius Dei. | Beatus es Symon Baryona, quia caro et sanguis non revelavit tibi, sed pater meus, qui est in celis. | Et ego dico tibi, | quia tu es Petrus, et super hanc petrani edificabo ecclesiam meam. | Ecclesia quatitur sed 11011 cadit, quando fuiidatur super petram, unde Petrus nomen accepit,
p. 57: non enim a Petro petra, sed Petrus a petra, petra antem erat Christus. | Ego auiem rogavi | pro te, ut uou deficiat jides tua, et tu aliquando | conversus \ confirma fratres tuos. | 1, Si Petrus: Primo | docetur quod aurem iu specie habere nou debent, quam iu ministerio uon habebaut.
p. 58: maiov est in regno celornm | a me, quia mitis sum ct humilis corde, | Discite a me non mundum fabricare, non creare, non miracula facere, nec mortnos suscitare, sed quoniam mitis sum et humilis corde.
```

---

## Chunk 03-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-03-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-03-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "58.8–62.8"
divisions: "cap. 3 (heading 'CAPITULUM TERCIUM.' at 43.10); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "912 words; 822 unanimous or majority-real; 75 settled by vote (R2 37, R3a 19, R5a 17, R6a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n119–n123 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 3, part 5: [TITLE]

## ¶1 · 58.8–60.9

> [p. 58] Quantum ad secundam virtutem que est humilitas, patet quod necesse est cementem fidei coniungi lapidi ad construccionem celestis edificii, unde Math. XVIII. 1, 2, quando mota est questio, quis maior est in regno celorum magister decreverat, quod parvulus in mente humilior; ideo cum Petrus sit post Christum fundamentum ecclesie, necesse est quod sit quodammodo fratribus suis humilior. Et istam leccionem didicerunt apostoli a magistro Math. XI, 29: Discite, inquit, a me, quia mitis sum et humilis corde, quod Petrus quia eminenter didicerat constitutus est fundamentum primum inter apostolos; unde Augustinus in De Verbis Domini Sermone X: Discite a me non mundum fabricare, non creare, non miracula facere, nec mortuos suscitare, sed quoniam mitis sum et humilis corde. Quamvis autem istam leccionem convenit et oportet quemlibet salvandum advertere. oportet tamen Petrum. si debet esse fundamentum substratum aliis, profundius illam cognoscere, oportet enim fundamentum ecclesie esse humillimum, quia aliter tanta fabrica cuius fundus in terra capitur et cacumen usque ad summum celum erigitur non stabit solidum; fabrica igitur tam gravis in moribus requirit fundacionem [p. 59] in summo gradu humilitatis possibili. Et hec racio quare Christus noluit fundare suam ecclesiam in mundi diviciis tamquam stercoribus vel aquis labilibus nec in mundi gloria vel fastu seculi tamquam ventis. sed in stabili paupertate, que securius, brevius et statui innocencie conformius facit humiles regnum celorum acquirere. Unde. ut declarat Lincolniensis in quodam sermone de humilitate, quod vere humilem iste octo condiciones inseparabiliter consequuntur: Discutiat, inquit, unusquisque se ipsum diligenter, an vere humilitatis signa ipsum sequuntur. Vere namque humilis hiis signis dinoscitur: Si correptus a minori non dedignatur, si non insolescat honoribus, si non elevetur vel delectetur in suis laudibus, si non reddat malum pro malo, nec maledictum pro maledicto sed e contrario benedicit. Si inter equales primus est in ope et ultimus in ordine, primus in labore et ultimus in requie, primus in ministrando et ultimus in recumbendo. Si gracias agit divine benevolencie, si tam libenter obedit quam precipit, si in potestate constitutus prius se noscit subiectum quam prepositum, sicut fecit centurio, de quo Luce VII. Et inter omnes scolas pertinentes preposito et Petri vicario non est alia pertinencior, sicut enim Petrus acute correptus a Paulo, ut patet Gal. II, humiliter toleravit. quando eciam missum est pro illo ad confirmandum centurionem Act. X. non petiit constipacionem comitive elegantis equestrium sed humiliter resedit in Yoppen pedester et requisitus in domo Simonis coriarii iuxta mare venit sibi humilius et instruxit, non expectans ab eo retribucionem temporalium vel [p. 60] donorum, et quando crebro se exposuit ante alios apostolos, non sic fecit gracia mundani honoris vel commodi, sed humiliter, obedienter et serviliter pro supportando onere Christi. Et sic quicquid de ipso legimus sonans in eius maioritatem super alios apostolos dicit maioritatem sue humilitatis atque servicii, quia iuxta hoc debet in eis maioritas attendi, ut patet Math. XVII et Luce XXII ex diffinicione magistri.

[ENGLISH]

## ¶2 · 60.10–60.22

> [p. 60] Quantum ad terciam virtutem, scilicet caritatem, patet quod Petrus socios suos precesserat, patet ex fervore operum, quod oportet correspondenter ex maiori dileccione procedere; et confirmatur ex hoc quod aliter Petrus foret nimis ingratus nisi magistrum tam singulariter eum diligentem a tanta blasphemia abstergentem et super oves suas generose preficientem correspondenter magis dilexerit. Et confirmatur tercio ex hoc; quod aliter magister Joh. ultimo inpertinenter quereret: Symon Johannis, diligis me plus hiis, et statim ex maioritate dileccionis committit sibi suam ecclesiam ad pascendum.

[ENGLISH]

## ¶3 · 60.23–61.12

> [p. 60] Sed notandum (ut supra tetigi) quod multiplex est racio amandi: quidam enim plus amant Christum secundum racionem divinitatis, ut creditur de Evangelista, quidam vero plus amant eum secundum racionem sue humanitatis, ut creditur de Philippo, et quidam secundum racionem dileccionis sui corporis, quod est ecclesia; et sic de infinitis aliis racionibus et istorum subdivisionibus, pro quibus de quolibet sancto dicunt illud Ecclesiastici XLIV, 20 verificari: Non est [p. 61] inventus similis illi. Et sic quilibet humilior est caritativior, et sic de aliis virtutibus; et quoad aliquam earum eminenciam. Videtur tamen Augustinum super Joh. Omeliam CXXIV difficultare istam materiam in hoc, quod inpertinenter tam crebro diceret Johannes de se ipso quod ipsum diligebat Ihesus, nisi eum ultra alios preeminenter diligeret. Et certum est quod proporcionaliter ut Deus quicquam prius diligit est ipsum melius et e contra, et ex alio latere videtur quod si Petrus plus diligit Ihesum suum est ipse melior, et per consequens plus amatur.

[ENGLISH]

## ¶4 · 61.13–62.8

> [p. 61] In ista materia videtur sanctum sic dicere, quod isti duo apostoli signant duas partes ecclesie, Petrus activam et Johannes contemplativam, quarum prima imperfecta finitur in via; et secunda perfeccior consumatur in patria, et sic ad sensum anagogicumChristus plus diligit Johannem dum plus amat vitam in patria, sed Petrus plus amat Christum, quia senciendo miseriam nostram plus diligimusDei misericordiam, veritatem autem contemplacionis, quia nondum apparet nobis, minus diligimus. Et ad istum sensum Christus plus amavit Johannem, quia minus, inquit Augustinus, amat nos Christus miseros quam beatos, sed quam personam de illis plus diligit in celo non innotescit. Ex isto dicto videtur tamen quod in vita activa plus amoris Christi presbiter hic indicat in effectu, et sic Deus eternaliter plus amat membrum suum esse in beatitudine quam in via; et tamen quidquid amaverit eternaliter eque amat; et sic non est nostrum modo cognoscere utrum Deus simpliciter plus amat Petrum [p. 62] in beatitudine quam Johannem. Non, inquit Augustinus, quantum ab alio quolibet Christus diligitur scire poterat, qui cor alterius videre non poterat, et ideo prudenter non dicit Petrus: Domine, Tu scis, quia amo te plus hiis sed asseruit: Domine, inquit, Tu scis, quia amo te; caritatem itaque et alias virtutes Petrus habuit in via secundum aliquam racionem ceteris apostolis plus perfectas.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 58.8: 2. Peter's humility.
- 59.8: Grosseteste's 8 conditions of humility.
- 59.25: Peter's humility shewn in submitting to Paul's reproof;
- 59.31: in his behaviour to Cornelius.
- 60.10: 3. Peters charity.
- 60.23: Different ways of love.
- 61.13: Peter represents the active part of the Church, John the contemplative,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 58: *edificii* (10 is the line number) [NW]
  - 58: *1* (old-style arabic 1, x-height) [R3]
  - 58: *celorum* [R4]
  - 59: *non* (zoomed: closed-top n) [R3]
  - 59: *malo* [R3]
  - 59: *equales* [R4]
  - 59: *instruxit* [NW]
  - 60: *preficientem* [NW]
  - 61: *amat* [R4]
  - 62: *ab* [R3]
  - 62: *te plus* (one token covers two printed words) [R5]
  - 62: *hiis* [R4]
  - 62: *caritatem* [R4]
  - 62: *Petrus* [R4]
  - 61: *quod isti* (W-split: quodisti -> quod isti (two words run together)) [OVERRIDE-SCAR]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 2. Peter's bumility. m (58.8); reference 3. Peters charitv. ^ , _ . (60.10); reference Peter's (62.10).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 58:
8. AB in marg.: Ilumilitas. q. B: cementem. 14. rit; B: fit.
18. A in marg.: Fundamentum ecclcsic quomodo dicitur Pctrus. 21. B:
21. Cf. St. Augustini Opp. tom. V, 1688.

p. 59:
8. Cod.: Lincon. i3. A in marg. : Humilis vere habet oclo con-
diciones ; B. : Octo signa vere hnmilitatis.
io. Cf. Trialogum p. 166, Serm. II, 149.

p. 60:
4. A in marg.: Peiro quidquid ascribitur super alios apostolos dicit
maioritatem sue humilitatis et servicii. 10. AB in marg.; Caritas.
16. B: blesphemia dcest. 23. B in marg. : Racio amandi multiplex.

p. 61:
4. In Joh. Evang. Opp. tom. III, 2, 820.

p. 62:
9. A in marg.: Capitulwn 4»*- 18. post; B: oportet ease. 22. B:
permittendas. -ib- B in marg. : Qjialis debet esse archivicarins Petri;
A in marg.: Vicarius Petri per quid constituatur.
1. Loosely quoted.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 58: maiov est in regno celornm | a me, quia mitis sum ct humilis corde, | Discite a me non mundum fabricare, non creare, non miracula facere, nec mortnos suscitare, sed quoniam mitis sum et humilis corde.
p. 59: unusquisque se ipsum ditigenter, an vere humilitatis signa ipsum sequuntur. Vere namque humilis hiis signis dinoscitur: Si correptus a minori uou dedignatur, si non insolescat Itonoribus, si non elevetur vel delecteiur in suis Jaudibus, si non reddat malum pro malo, nec maJedictum pro maJedicto sed e conlrario benedicit. Si inter equaJes primus est iu ope et idtimus iu ordine, primus in Jabore et uJlimus in requie, primus in ministrando et uJtimus iu recumbendo. Si gracias agit divine benevoiencie, si tam Jibenter obedit quam precipit, si iu potesiate coustitutus prius se noscit subiectum quam prepositum, sicut fecit centurio, de quo Luce VII.
p. 60: Symon Jokannis, diligis me plus hiis, | Non est
p. 61: inventus similis illi. | ipsum melius ioet e contra, | si Petrus plus diligit Ihesum suum est ipse melior, et per consequens plus amatur. | quia minus, | atnat nos Christus miseros quam beatos,
p. 62: quantum ab alio quolibet Christus diligitur scire poterat, qui cor aiterius videre non poterat, et ideo prudenter non dicit Petrus: Domine, Tu scis, quia amo teptus kiis sed asseruit: Domine, inquit, Tu scis, quia amo te; caritatem itaque et alias virtutes Petrus habuit in via secundum aliquam racionem ceteris apostolis plus perfectas. | Status exproprietarius. Status proprietarius. | Privilegium cleri datum a Christo. | Status exproprietarius alcior.
```
