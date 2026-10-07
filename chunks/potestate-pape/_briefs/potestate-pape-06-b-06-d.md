# Translation brief: potestate-pape 06-b–06-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-06-b.md chunks/potestate-pape/wyc-potestate-pape-06-c.md chunks/potestate-pape/wyc-potestate-pape-06-d.md` once and fix what it reports.
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

## Glossary (the 248 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

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
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
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
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
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
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| brocardicum / brogardicum | brocard | The schoolmen's stock maxim. Ruled 2026-10-02 (*Eccl.* 16, 360.9). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
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
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| preconium | commendation | Ruled 2026-10-02 (*Eccl.* 20, 488.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
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
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 06-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "106.29–110.19"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 2 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "794 words; 757 unanimous or majority-real; 22 settled by vote (R2 13, R3a 6, R5a 3); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n167–n171 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 2: [TITLE]

## ¶1 · 106.29–107.16

> [p. 106] Item, si nostri episcopi habent tantam potestatem faciendi miracula eciam primitiva ut olim, cum sepe foret necessarium uti huiusmodi potestate, culpandi sunt ex ocio potestatis et discredendi tamquam fictores pompatici, cum nesciunt [p. 107] racione vel facto ostendere huiusmodi potestatem. Apostoli enim sicut habuerunt potestatem vexatos a sathana liberandi, sic eciam habuerunt potestatem tradendi Sathane peccatores inficientes ecclesiam. Nam Mar, ultimo dicit Christus: Signa autem eos qui crediderint, hec sequentur: In nomine meo demonia eiicient, Unguis loquentur novis, serpentes tollent, et si mortiferum quid biberint non eis nocebit. Et patet in cronicis quod apostoli habuerunt huiusmodi potestates, ut patet de Paulo Act. ultimo; et quod apostoli habuerunt potestatem tradendi perversos sathane, patet Act. V de Anania et Saphira, et prima Cor. V de fornicario, qui cognovit uxorem patris et prima Thim, primo de Ymeneo et Alexandro, quos Apostolus tradidit sathane propter blasphemiam.

[ENGLISH]

## ¶2 · 107.18–108.24

> [p. 107] Item, secundum Apostolum prima Cor. XII, 4 divisiones graciarum sunt, quas Dominus dividit singulis prout vult; et ille gracie vel sunt potestates vel ad potestates consequentes, igitur sicut non omnes parificantur in graciis, sic nec in potestate. Nec valet dicere quod nostri prelati in potestate precipua sunt pares apostolis, quia summa potestas concessa christiano stat in hoc, quod sit Dei filius adoptivus, cum aliis inde sequentibus, ut puta quod constituatur super omnia bona Dei. Sed ex dubio cuiquam prelato nostro simplex ydiota sibi subiectus in hoc ipsum exuperat, igitur non in hoc debet pompare de preeminencia potestatis, ymo si parificatur apostolis in potestate ministrandi sacramenta et aliunde apostoli ipsum excesserant, videtur quod [p. 108] tota aggregata potestas in apostolis fuit maior, ymo cum apostoli mediate eadem potestate suffecerunt instituere sacramenta et tam miraculose ac tam efficaciter ministrare eadem sacramenta, videtur quod apostoli habuerunt ampliorem et efficaciorem potestatem ad dispensandum ecclesie sacramenta. Nec ostendunt in signis efficacibus, quod habeant vel absconditam potestatem; cum igitur posset esse error in institucione et error in potestatis abusione, racione cuius Deus non conferat sed auferat huiusmodi potestatem, videtur signum luciferinum gloriari sine efficacia operis de huiusmodi potestate. Opus inquam meritorium de celo ecclesie instanter tractum in preteritum gigneret consolacionem et gaudium potentatus et daret fidem subditis quod Deus sibi communicat potestatem. Status autem et potestas magna viancium incuteret eis ex altitudine casus formidinem. Et patet ex secundo capitulo per multa media quomodo in qualibet potestatum novem patres in primitiva ecclesia excesserunt. Aliter enim prelati nostri nimis illuderent subtrahendo usum huiusmodi potestatum.

[ENGLISH]

## ¶3 · 108.25–110.19

> [p. 108] Quantum ad auctorizacionem scripture sacre patet ex modo loquendi beati Augustini IV De Doctrina Christiana VI cap.; quod apostoli et evangeliste qui scripserunt libros canonicos erant eorum autores, licet solus Deus fuerit autor summus. Aliter enim nulla creatura haberet auctoritatem ad aliquid faciendum. Quod autem sacerdotes nostri temporis non habent tantam auctoritatem vel potestatem canonizandi libros sicut sunt libri de biblia, videtur ex universali sermone dicto [p. 109] de veritate et auctoritate scripture. Et patet ex hoc; quod idem esset parificare eorum dicta auctoritati scripture, et asserere quod Spiritus Sanctus et Jhesus noster hec in ipsis loquitur. Sed vite eorum elongacio, sentencie contrariacio et propria confessio contradicunt; vivunt enim voluptuose et sermo eorum sapit avariciam. Sed Sapiencie I, 5 dicitur, quod Spiritus Sanctus discipline effugiet fictum, ideo perit illis evidencia auctoritatis, quod Spiritus Sanctus dicit in illis suas sentencias et cum in Christo non fuerunt Est et Non, ut patet II Cor. I, 17, 18; ipsi autem sepe contrariantur evangelio ac eciam sibi ipsis; ideo perit illis quantum ad illa in quibus extraneant, Christi auctoritas: sepe enim contradicit posterior precedenti. Et quantum ad conformacionem propriam, sunt multa dicta sanctorum paparum eminenciam scripture concorditer confitencium, sicut faciunt sancti doctores, in quibus fundant suam sentenciam, ymo in V Decretalium de sentencia excommunicacionis cap A nobis confitetur papa de sua ecclesia, quod sepe fallit et fallitur, eciam de excommunicacione et absolucione in quibus magis attenderet. Ideo non possent patencius accusare se ipsos de supina blasfemia quam parificare dicta sua extranea evangelio, specialiter cum deficiunt in potestate minori, ut puta interpretacione sermonum facta in loquendo omnia linguarum genera, ut fecerunt apostoli et sui conversi, ymo in exercendo gracias sanitatum. Et ista sunt modicum in comparacione ad [p. 110] superiora carismata. Ostendant igitur istas potestates, conversiones infidelium vel sanaciones infirmorum per suas epistolas, ut factum est cum scripturis apostolorum; et est evidencia quod Christus in eis loquitur, ymo ut dictum est superius, generaliter potestas subtrahitur pro mortali. Sed multi eorum ex ingratitudine incidunt in mortale, ideo necesse est quod potestas si quam in principio habuerunt ex ingratitudine sit subtracta. Item, si sint paris auctoritatis cum nostris auctoribus, cum continue multiplicant leges suas addiscere sicut legem fidei scripturarum, quod est contra leges multas ecclesie, que preferunt theologiam et privilegiant eius discipulos, similiter tunc destruerentur iura canonica, quia tota illa facultas foret pura theologia, quia sermo quem Deus in eis loquitur eque evidenter sicut locutus est olim in scribis fidei- scripturarum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 107.4: The apostles had power to cast out devils and to deliver offenders to Satan.
- 107.18: All are not alike in grace or power,.
- 108.1: Even in the ministrations of sacraments the Apostles had greater power.
- 108.18: It our prelates have these great powers they should use them.
- 108.25: Our priests cannot rule books to be canonical,
- 109.3: nor have their writings any claim to such authority as belongs to Scripture.
- 110.11: If they had such power theological study and canon law would be useless,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 107: *sathana* [NW]
  - 107: *Signa* [R3]
  - 107: *sequentur* [R4]
  - 107: *nomine* [R4]
  - 107: *tollent* [R3]
  - 107: *Dominus* [R3]
  - 107: *parificantur* [NW]
  - 107: *parificatur* [NW]
  - 109: *parificare* [NW]
  - 109: *fictum* [R4]
  - 109: *illa* [R3]
  - 109: *parificare* [NW]
  - 110: *∅* (English side-note word) [R6]
  - 110: *illa* [R3]
  - 107: *Christus:* (W1: Chnstus: -> Christus: (scans: chnstus | christus | chnstus | chnstus)) [OVERRIDE-SCAR]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 24. I. Tim. V, 23. (106.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 106:
11. AR in marg. : Secunda pars. 24. A: utere inquam ; B m marg. :
inquit.

p. 107:
1. B: moii deest. 6. Codd.: sequuntur. 7. Codd.: loquuntur.
5. Marc. XVI, 17-18.

p. 108:
27. Opp. tom. III, 1, 67.

p. 109:
21. AB in marg.: Auctoritas sacre scripture excellit omnes alias
scripturas.
1. De Veritate Sacre Scripture = Book Vlth of Wyclifs Summa
Theologiae ed. Buddensieg (Lipsiae et Londoniis) 1904. 21. V,

p. 110:
12, i3. multiplicant . . . addiscere; ita codd. 14. Codd.: prefuerunt.
i?. B: privilepiar.t 24. Codd : lerem. 29 AB in marg : Le.x
Christi sufficientissnna est.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 106: modico vino propter stomachum tnum et frequentes tuas infirmitates
```

---

## Chunk 06-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "110.20–114.29"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 3 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "962 words; 907 unanimous or majority-real; 36 settled by vote (DEL 2, INS 2, R2 15, R3a 4, R5a 12, R6a 1); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n171–n175 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 3: [TITLE]

## ¶1 · 110.20–111.2

> [p. 110] Similiter, tunc difficultaretur christiana religio ultra patres veteris testamenti vel infideles de secta Machometi,. qui de paucioribus legibus sunt contenti; multo magis in secta Christi; qui Mat. XI, 30 promisit onus- suum esse leve, et ille qui Mat. V, 17 dicit, quod non venit solvere legem sed implere, facit verbum abbreviatum Mat. XXII, 40 dicens, quod in dileccione Dei et proximi lex pendet et prophete. Similiter, Deus foret insufficiens et improvidus, si incomplete dedisset legem suam per eius cariores apostolos, relinquens ingracioribus eius presbiteris ex declinacione ab eius vita et verbis legis tam necessarie complementum. Sic enim fuissent patres primitive ecclesie frustrati a fructu [p. 111] finali legis dominice, cum nescierunt decretales epistolas.

[ENGLISH]

## ¶2 · 111.3–113.5

> [p. 111] Similiter, non plus tenemur credere illis epistolis quam tenemur credere quod auctor eorum sit caput ecclesie militantis, sed hoc non tenemur credere absque formidine, non solum quia nescimus si moritur, verum quia nescimus si prescitus fuerit vel membrum sancte matris ecclesie. Sic enim electis duobus papis de primatu contendentibus christianismus foret perplexus et non sufficeret in Christum credere; non enim teneor plus credere dicto hominis quam teneor de illo credere sanctitatem vel quod Deus in ipso loquitur, sed non teneor pariter credere sanctitatem vite in nostris prepositis, sicut in sanctis apostolis igitur non tantum teneor credere suis scriptis; tunc enim tenerer credere quod sunt confirmati gracia predestinacionis. Similiter, ista sentencia inficeret totam scripturam sacram, cum Apostolus Gal. I, 8 audacter asserit quod si illis vel angelus de celo evangelizaret preterquam quod evangelizatum est, anathema sit. Modo autem multe gentes transferuntur cum Gal. doctrina Apostoli per epistolas decretales. Cum igitur per falsigraphum oportet tantum illis credere sicut apostolo, relinquitur quod oportet apostolo in isto discredere, cum licet eis ut referunt contra apostolum dispensare, eo quod ipsi auctorizant scripta apostoli. Item, Apoc. ultimo propter auctoritatem libri propheta sic loquitur: Si quis apposuerit ad hec, apponet Deus super illum plagas scriptas in libro [p. 112] isto, et si quis diminuerit de verbis libri prophecie huius, auferet Deus partem eius de libro vite et de civitate sancta. In veteri vero testamento est aliud duplex testimonium: primo Deutero. IV, 2 per sanctum Moysen Deus precipit Israeli: Non addetis ad verbum quod vobis loquor neque auferetis ex eo. Et Proverb. XXX dixit vir cum quo Deus est ne addas quicquam verbis illius et arguaris et inveniaris mendax. Cum igitur nostri non doceant quod hec dicit Dominus, illud videretur nimis magna presumcio parificare dicta ilia legi scripture. In cuius confirmacionem unus Papa revocat, suspendit vel abrogat epistolas et bullas alterius, sed facta sua falsificat. Ideo vel oportet falsificare totam fidem scripture vel omnes satrapas sequentes in auctoritate postponere. Hoc tamen papa habet pre aliis, quod sibi ut pape plus credi debet propter vite sanctitatem, cum debet ut sic conformius sequi Christum, quod si manifeste declinat ab hac semita, nullus est simulacior, mendacior et quidquid tunc locutus fuerit de mendacio plus suspectus. Ideo absit michi plus credere cuicumque Romano pontifici, quam quatuor sanctis doctoribus vel eis similibus, primo quia facta et scripta multorum paparum plus discordant a lege Dei; secundo quia non debemus credere verbis hominis nisi de quanto debemus credere quod prima veritas in ipso loquitur. Fides inquam est, si quid sit veritas, verbum Domini ipsam loquitur, libencius autem loquitur sapiencia in iusto sibi benivolo, quam in mendace sibi contrario. Tercio quia criminosus mentitur quicquid dixerit, non auctoritate [p. 113] vel racione sui, sed racione sermonis primi dicentis, credenda est veritas quam ipse balbuciet menciendo. Revera qui convictus est mendax in opere vel sermone, antequam purificetur quicquid dixerit est suspectum.

[ENGLISH]

## ¶3 · 113.6–114.12

> [p. 113] Item, si quilibet papa haberet tantam potestatem edificandi ecclesiam et quicquid aliud faciendi cum sanctis apostolis et cum non excederet Mattheum, Johannem et ceteros citra Petrum, videtur quod, sicut omnes alii apostoli, ut fingitur, erant minoris auctoritatis quam Petrus, sic et quilibet papa ipsum succedens. Si igitur papa habet auctoritatem canonizandi epistolas Pauli, quod ipse non habuit, quia tunc foret per se autenticus, videtur quod quilibet papa sequens omnem apostolum citra Petrum auctoritate excesserat, et sic decretales essent maioris autoritatis quam quatuor evangelia et paris auctoritatis cum Petri epistolis. Sed deliramenta sunt ista, cum tota scriptura capit parilitatem auctoritatis a Spiritu Sancto, quem credimus eius autorem. Nec credo beatum Petrum fuisse maioris auctoritatis quam ceteros, quia ore, digito et auctoritate Domini locuti sunt et fecerant facta sua. Ideo auctoritas Dei non cepit magis vel minus in ipsis. Nec aliquis apostolus in quantum illa privata persona sed in quantum homo divinus; ut loquitur Augustinus IV De Doctrina christiana cap. VI; vel in quantum Christus participative, ut loquuntur multi sancti, ut sic (inquam) sunt omnes paris auctoritatis, unus ad unum et alius ad aliud, secundum quod Deus eis diviserat dona sua, et quicquid aliquis apostolus ut talis dixerit est paris auctoritatis cum [p. 114] quolibet. Et hinc Petrus ut solidum membrum sancte matris ecclesie gaudebat de Pauli iusta correpcione; non enim spectat ad membra corporis usurpare vel remurmurare contra aliena officia. Et sic videtur michi quod quilibet sacerdos debet esse sub non gradu potestatis et auctoritatis secularis, et pure in nomine Domini precipere sic vel sic facere; quod si sit antichristus, membrum dyaboli vel aliter Scarioth, non habet aliquam huiusmodi potestatem. Unde ut sepe repecii, pure de tanto debet christianus implere quod precipit.

[ENGLISH]

## ¶4 · 114.13–114.29

> [p. 114] Sed contra illud arguitur per hoc quod iuxta dicta nullus apostolus vel predestinatus citra Christum est maioris auctoritatis quam quilibet, quod confunderet gradus ecclesie et iura papalia, cum sicut Petrus et ceteri apostoli fuerunt paris auctoritatis, sic debet esse papa et quilibet sanctus episcopus, ymo quilibet predestinatus. Ubi igitur foret papalis sentencia de maioritate et obediencia? Similiter, iuxta dicta de sanctitate debet capi auctoritas, sed unus est reliquo sanccior, igitur maioris auctoritatis quam evangelium. Nec valet referre omnem auctoritatem pure adDeum, quia sunt gradus auctoritatum, cum unus constitutus est sub alterius potestate, aliter enim periret regula obediencie humane et maioritas auctoritatis ecclesie.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 110.29: It would imply that God gave an imperfect law to the apostles.
- 111.3: We are not bound to believe that the pope is head of the Church. What if rival popes are elected?
- 112.12: One pope revokes the decrees of another.
- 112.24: I would rather rely on the four great doctors.
- 113.6: If the pope's claims are allowed, the decretals would be of more authority than the gospels.
- 113.20: All the Scripture is of equal authority, as were all the apostles.
- 114.5: So should it be with priests now, who should speak in the name of the Lord,
- 114.13: Objection: 1. This would confuse all law and order in the Church.
- 114.22: 2. There must be degrees of authority, even if it rests on holiness.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 110: *religio* (20 is the line number after it) [R4]
  - 110: *suum* [R4]
  - 110: *pendet* [R4]
  - 111: *∅* (30 is the line number) [R4]
  - 111: *ad* (italic d with broken bowl, zoomed leaf) [R3]
  - 111: *illum* [R3]
  - 111: *libro* [THIN]
  - 112: *diminuerit* [THIN]
  - 112: *verbis* (print has v) [THIN]
  - 112: *huius* [THIN]
  - 112: *eius* [THIN]
  - 112: *Non* (5 after it is the line number) [R4]
  - 112: *parificare* [NW]
  - 112: *legi* [R4]
  - 113: *illa* [R3]
  - 114: *Sed* [R3]
  - 114: *dicta* [R3]
  - 114: *quia* (25 is the line number) [R4]
  - 111: *apostolis* (LEFT-odd: comma not carried) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 110:
12, i3. multiplicant . . . addiscere; ita codd. 14. Codd.: prefuerunt.
i?. B: privilepiar.t 24. Codd : lerem. 29 AB in marg : Le.x
Christi sufficientissnna est.

p. 111:
ii. AB in marg. : Credere epistolis decretaltbus. 14. A ln marg.:
Xota de Caifa. 20. AB in marg. : ^J^^ } scripture sacre non licet.
21. Codd.: illi. 22 B: quod deest.
. 30. Apoc. XXII, 18, 19.

p. 112:
5. B: precepit. 17. AB in marg. : Credere pape.
7. Prov. XXX, 1, 6.

p. 113:
10. AB in marg.: Auctoritatis paris sunt scripture apostolorum.
2(5. B: in episcopis. 3i. B: in quantmn.
De Potestate Pape. 8

p. 114:
i3. B in marg. : Obiectus de auctoritalis maioritate; A in marg. : /.
20. Codd.: papali. 22. A in marg.: 2. 3o. A in marg. : 3.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 111: vei angelns de celo evangelizaret preterquam qnod evangelizaium est, ana~ thema sit. | Si quis apposuerit ad hec, apponet Deus super illum plagas scriptas in lihro
p. 112: isto, et si quis dimiuuerit de vevbis libri prophecie kuius, auferet Deus partem eitts de libro vite et de civitate sancta. | addetis ad verbum quod vobis loquov neque auferetis ex eo. | vir cum quo Deus est ne addas \ quicquam verbis illius et ar- | guaris et inveniaris mendax. | hec dicit Dominus,
```

---

## Chunk 06-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-06-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-06-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "114.30–118.5"
divisions: "cap. 6 (heading 'CAPITULUM SEXTUM.' at 102.25); part 4 of 9, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "719 words; 697 unanimous or majority-real; 18 settled by vote (R2 11, R3a 4, R5a 3); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n175–n179 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 6, part 4: [TITLE]

## ¶1 · 114.30–115.10

> [p. 114] Similiter, suscipiendo potestatem ordinis, quis suscipit adeo potestatem et auctoritatem quia potestatem pascendi ecclesiam, quod est optimum regimen et iurisdiccio summa, quam Christus umquam instituit, cum plus sit differencie [p. 115] ius Dei quam ius cesaris. Nec dependet potestas regiminis a loco vel populo, quia distinguitur ab actu potestatis, data indistincte a Deo ante locum vel populum, ideo cum non variatur correspondenter ad tale obiectum, manifestum estquod quiescit ante tale iurisdicionis obiectum. Sic enim habuerunt apostoli quiescentes in Jerusalem datam a Spiritu Sancto potestatem regiminis, et tamen nondum fuit ad eorum noticiam distinctus populus limitatus.

[ENGLISH]

## ¶2 · 115.11–117.15

> [p. 115] Ad primum videtur michi, ut sepe tetigi, quod omnis clericus debet pure inniti auctoritati divine, dimittendo auctoritatem gentilem adinventam regibus gencium; qui infideliter blasfemaverant quod sunt Deus, ut patet de Nabugodonosor Danielis IV; et hinc sumpserunt sibi nomen auctoritatis et capitalis dominii, Christus autem docet suos apostolos gentilitatem istam aufugere, ut patet Luce XXII et Matth. XX. Unde quia aliquid licencie remansit in ista gentilitate, ideo remansit cum civilitate verbum auctoritatis, per quod ego intelligo superioritatem potestatis civilis. Sed postquam dotata est ecclesia, introducta sunt irreligiose nomen iurisdicionis et auctoritatis cum similibus, que civilitatem sapiunt. Et sic conceditur quod unus episcopus est reliquo maioris potestatis quam quidam vocant auctoritatem. Referendo autem auctoritatem ad Deum et negando auctoritatem sed promulgacionem inesse formaliter creature neganda foret in apostolis auctoritatis maioritas. Secundo vero intelligendo auctoritatem in quantum dicit Dei preconem habere potestatem ad promulgandum eius sentenciam, sic omnes apostoli vel evangeliste [p. 116] sunt paris auctoritatis, cum ipsa non potest maius aut minus suscipere. Ad quem sensum scriptura sacra est paris auctoritatis utrobique. Sed tercio michi infundabiliter loquuntur quidam de auctoritate, ut dicit maioritatem sanctitatis vel carismatum multitudinis, et quia illud est nobis incognitum, transferunt auctoritatem gentiliter ad ordinacionem humanam, ut quotlibet gradus ponunt in papa, archiepiscopo, rectore et simplici sacerdote, cum quotlibet intercisionibus, que quia auctoritate divina bene possunt fieri secundum divisiones graduum, discrecionis et potestatis quam ipse distribuit, ideo sollempnizantur instituciones humane, quamvis ordinacioni divine contrarie, et observantur amplius quam lex Dei. Sed loquatur sic de auctoritate, qui in scriptura sacra sciverit hoc fundare. Leges autem papales de maioritate et obediencia possunt intelligi, quando institucio humana de preposituris hominum correspondet divino iudicio, sic videtur quod proporcionaliter ut quis ponitur in maiori preeminencia quoad homines, sic ponatur realiter in maiori preeminencia virtutum et gracie quoad Deum; quod quia nunquam vel raro contingit, nec superest (ut credo) ad illud fundandum scripture auctoritas, ideo taceo quoad leges et facta, dicens quod illud bene potest fieri de Dei potencia absoluta, sciens quod sic non fuit inter Christi sacerdotes in ecclesia primitiva. Et patet in parte quomodo dicendum est ad primum obiectum. Ad secundum patet ex dictis, quomodo ex sanctitate ut signo remoto debet capi duplex auctoritas, et non ut de equata mensura, quia tunc diminueretur vel extingueretur ut sanctitas [p. 117] promulgantis, quod est falsum, cum infideles ut Balaam, Cayfas et ceteri dampnabiles prophetarunt Sanctitas tamen est signum auctoritatis divine et firmitatis inaugmentabilis auctoritatis humane, et sic gradus prepositure et auctoritatis civilis nuncupate surrepserunt cum dotacione et temporalium cupiditate non solum in seculares clericos sed in fratres, cum ipsi constituunt tribunos, centuriones, decanos et alios sicut Judei, qui servarunt cerimonias veteris testamenti, ut notatum est Exod. XVIII. Sed servata vera humilitate octuplici, de qua superius, omnia ista superfluerent sicut superfluissent in sanctis apostolis, et sic defectus instruccionis virtutis est causa, quare ista sunt modo utilia.

[ENGLISH]

## ¶3 · 117.16–118.5

> [p. 117] Ad tercium patet quod potestas ordinis est potestas regiminis, quam quilibet habet in quantum presbiter; quam solum cognoscunt qui noverunt universalia, et illa distinguitur a potestate ordinis sive regiminis excedente gradum remississimum potestatis. Et sic idem episcopus habet multas potestates ordinis sive regiminis, ut patet superius. Nec prelatus dat curato novam potestatem regiminis nisi sit fidelis preco Dei prius dantis; ymo videtur michi quod sacerdos prius fuit debitor eidem populo, cui per episcopum suum preponitur, cum apostolus Rom. I, 14 confitetur se esse Grecis Latinis et barbaris debitorem, verumtamen ex novo voto et munere recepto est amplius obligatus. Ritus autem gentilis ecclesie in hac parte videtur dare licenciam ad congregandum commodum temporale et inhabili quoad Deum, et talis iurisdicio non frenata per scripturam maxime induceret sectam Antichristi. Si igitur nostri habent potestates episcopales pares [p. 118] cum apostolis, ostendunt se dampnabiles, quod ociando tantum illis potestatibus abutuntur. Si autem potestates terrenas habuerint supra apostolos, hocfalse et antichristiane habent aprincipe mundi huius.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 114.30: 3, In receiving orders a man receives authority and rule,
- 115.11: I reply: 1. The clergy should rely only on divine authority, having nothing to do with civil power.
- 115.28: All authority belongs to God; man's part in it is only promulgation,
- 116.6: We do not know what grace or power God has given to any man, and we try to make up for our ignorance by ordaining degrees in the clergy.
- 116.32: 2. Holiness is a sign but not a measure of authority.
- 117.1: Balaam and others prophesied though wicked.
- 117.16: 3. The power of orders is also a power to rule,
- 117.23: but a curate does not receive it by a bishop's appointment unless he is a faithful herald of God, from whom the gift comes.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 117: *qui* (10 is the line number) [R4]
  - 117: *illa* [R3]
  - 117: *Grecis* [R4]
  - 117: *Latinis* [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 114:
i3. B in marg. : Obiectus de auctoritalis maioritate; A in marg. : /.
20. Codd.: papali. 22. A in marg.: 2. 3o. A in marg. : 3.

p. 115:
11. B in marg. : Solucio. 23. AB in marg. : Auctoritas potestatis
vel iurisdiccionis. 28. B in marg. : Nota. 3i. B: aucioritas.

p. 116:
3. tercio ; adde: vidctur. 19, 20. Codd.: correspondent. 20. Codd.:
sic videt. 3o. A in marg. : /. 3i. A in marg. : 2.

p. 117:
(none)

p. 118:
6. AB in marg. : Antichristus quis est secundum scripturam. 16. B
inmarg. : Anti valet contra. 24. Ainmarg. : De Antichristo. 27. AB
in marg. : De Antichrislo.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```
