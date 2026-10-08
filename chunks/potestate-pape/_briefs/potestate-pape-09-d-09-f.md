# Translation brief: potestate-pape 09-d–09-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-09-d.md chunks/potestate-pape/wyc-potestate-pape-09-e.md chunks/potestate-pape/wyc-potestate-pape-09-f.md` once and fix what it reports.
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

## Glossary (the 236 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| iugum | yoke (a pair) | Ruled 2026-10-02 (*Eccl.* 202.9 ff.). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio | boast; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| fantasticus | imaginary | Cf. *fantasia* "imagination". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 203.4). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 09-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "204.30–207.22"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "633 words; 591 unanimous or majority-real; 34 settled by vote (R2 23, R3a 9, R5a 2); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n265–n268 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 4: [TITLE]

## ¶1 · 204.30–205.26

> [p. 204] Sed ceca argucia, unde cap. IX ex auctoritate beati Augustini magister sic loquitur: Quodcumque ligaveris super terram etc, hoc est ego Deus [p. 205] et omnes celestis milicie ordines et omnes sancti in gloria mea laudant vobiscum et confirmant, quos ligatis et solvitis. Non dixit, quos putatis ligare et solvere, sed in quos exercetis opus iusticie vel misericordie. Aliter autem opera vestra in peccatores non cognosco. Quis igitur non horreret, quod sacerdos cogit Deum et totam triumphantem ecclesiam consentire culpabiliter sue stulticie vel quicquid in isto fecerit ad ratam prudenciam imputare, vel quod populus sine iudicio debet credere esse confirmatum adeo, quicquid sacerdos fecerit in hac parte. Tales blasfemias et mille permittit Deus in peccatum ecclesie, confitens vero erit optimus iudex peccati proprii, considerans si perfecte dolet de commisso in Deum, si humiliter proponit et non vult sic peccare amplius. Sacerdos autem qui apponit materiam in confitentem ignorat hoc; verumtamen multum valet apud utramque ecclesiam, quod quis humiliter confiteatur presbitero, quod ipse secundum clavem sciencie aptet sanificam medicinam, et quod oret ac supportet cum ceteris membris Christi pro scelere confitentis. Sic enim secundum Augustinum super Johanne Sermone CXXI, ecclesia sanctorum in racione meriti dimittit peccata.

[ENGLISH]

## ¶2 · 205.27–207.22

> [p. 205] Quantum ad secundum pomposum, quod est ordinis vel status dignitas, consideraret sic pompans dignitatem naturalem et statum dyaboli, et in quantam indignitatem incidit per peccatum, ut pulchre declarat Augustinus in De Verbis Domini Sermone LIII: Melior est, inquit, virginalis [p. 206] sanctitas quam pudicicia coniugata, sed attende superbiam et humilitatem, iungeque virginitati tue humilitatem et eris matre tua melior, quod si tu virgo admittas superbiam et mater tua servet humilitatem, ipsa est longe melior te superba. Nam sicut bonum bono adiunctum facit integrum magis bonum, sic hoc malum facit totum malum sive bono adiunctum fuerit sive malo; privat enim te racione membri humilis capitis, quod est Christus, quod si est, ut patet in lucifero, qui est melior te natura, ubi est potestas vel dignitas, de qua pompas? Nichil, inquam, foret clero utilius et specialiter Christi vicario quam sentire humiliter de seipso, quod Augustinus declarat subtiliter et devote, dicens quod genus humanum post lapsum omnino indiguit celesti medico, quod quia non suffecit ad ipsum ascendere, Deus ineffabiliter descendit ad ipsum, docens vita, opere et sermone, quomodo oportet genus humanum si sanabitur humilitate contraria vie superbie qua adeo recesserat sanum redire ad dominum. Et hec racio, quare Christus servavit in vita et doctrina summam pauperiem et humilitatem; Antichristus autem querit mundanam gloriam Christo contrarie, ut dicitur Joh. V; et ideo licet papa sic fecerit (ut dicit Augustinus) non est de Christi ecclesia, quia si sit verus papa est homo humillimus, mundanos honores et lucrum seculi parvipendens. Et sic Christus est humanitus via, per quam oportet omnem salvandum incedere, que via cum sit arta impossibile est tumentem superbia per illam semitam penetrare. Sed de quanto collisus stante illo tumore plus illi vie facietenus innititur, de tanto comportando prohibens [p. 207] plus offendit. Nec est talis tumorositas vera magnitudo, sed innaturalis mundana aquositas, que repugnat omnino Christi vicario, quia aliter est mendacissimus Antichristus. Et sicut dicitur Johannis XIV. 6: Viator habet, qua vult ire, cum Christus est via, quo vult ire, Christus est veritas et ubi vult manere, Christus est cursiv. Quamvis autem in via non sunt insidie, cum sit Christus, tamen iuxta illam sunt multa pericula, iuxta illud Psalmi CXXXIX, 6: Iuxta iter scandalum posuerunt michi. Vis secure incedere, tene te in via regia et omnino desere mundum ac eius gloriam, quia aliter es indubie Antichristus et non de Christi ovibus. Christus enim non potest superbum talem ad se trahere, cum oportet exaltacionem ad Deum per humilitatem procedere. Ideo quomodocumque pompaveris, exaltando te ipsum et querendo mundi gloriam, ille qui sentenciavit, quod qui se exaltat humiliabitur, et qui se humiliat exaltabitur, non potest mutare suam sentenciam, quin talis sit magis alienus a Christo et per consequens Antichristus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 205.6: God does not confirm all binding and loosing of the priest.
- 205.27: Danger of pride in order or State.
- 206.6: Need of humility.
- 207.8: The proud cannot walk in the wavy Which is Christ

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 205: *autem* [R3]
  - 205: *virginalis* (hyphenated virgi-nalis across the page; main token covers whole word) [THIN]
  - 206: *quam* [THIN]
  - 206: *humilitatem* [THIN]
  - 206: *tu* [R3]
  - 206: *et* [R3]
  - 206: *humilitatem* [R4]
  - 207: *Iuxta* [R4]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Dan8er order Pride (205.27); reference 6. Matth. XXIII, 12. (207.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 204:
to. AB in marg. : Clavium abusio et pampa. 19. Codd.r ille.
2. Hier. Gommcnt. in Ev. Matth. Lib. III, cap. XVI, v. 19.
Mignc XXVI, 118. 3i. Magistcr, i. c. Pctrus I.ombard. 1. c.
pag. 887.

p. 205:
1. Codd. : omnes. 14. AB in marg. : Confessio que Jil sacerdoti.
32. AB in marg. : Dignitas unde causatur.
24. Opp. tom. V, 5q5. 32. St. Aug. Serm. CGCLV, Opp.
tom. V, 1379 Loosely quoted.

p. 206:
12. B: pompos. 23. Codd.: in marg. Antichristus quis est. Via est

p. 207:
5. Codd. in marg. : Viatur attendat Christum. 10. Codd. in marg. :
Antichrislus. 17. Codd. in marg. : Gloriam fugere (Cod.: sugere)
debet prelatus.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 204: Tibi dabo claves regni celorum, hunc } | locuni aliqni non intelligentes, sumunt aliquid de superciliophariseorum, ut dampnare innoxios vel solvere se putent noxios, | cum apud Beum non sentencia sacerdotum sed vita reorum queratur. Sed sicut Levit. XIV ostendere se sacerdotibus iubentur leprosi, quos illi muudos vel leprosos non faciuut, sed discernuuf, | Quodcumque ligaveris super terram etc. hoc est ego Deus
p. 205: et omnes celestis milicie ordines et omnes sancti in gloria mea laudant voHscum et confirmant, quos ligatis et solvitis. Non dixit, quos putatis ligare et solvere, sed in quos exercetis opus iusticie vel | misericordie. Aliter autem opera vestra in pcccatores non cognosco. | ir ir 'x | Melior est,
p. 206: ginalis sanctitas qnam pudicicia coniugata, sed attende superbiam et humilitatem, iungeque virginitati tue humilitatem et eris matre tua melior, quod si tu virgo admittas superbiam et mater tua servet hnmilitatem, ipsa est longe melior te superba. | Antichristus quis est. Via est Christus.
p. 207: Tnxta iter scandalum postierunt michi. | qni se exaltat humiliabiiur, et qni | se humiliat exaltabitur,
```

---

## Chunk 09-e: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-e
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "207.23–210.14"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "629 words; 564 unanimous or majority-real; 51 settled by vote (DEL 1, R2 31, R3a 12, R5a 6, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n268–n271 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 5: [TITLE]

## ¶1 · 207.23–209.16

> [p. 207] Quantum ad tercium scilicet vite sanctitatem, patet quod necesse est gloriantem sic in laudibus hominum considerare se sollicite in speculo scripturarum. Consideret igitur papa et impleat ea que exposita sunt de Petro, et tunc non delectabitur in laude hominum nec in mundana gloria, sed in spe premii absconditi in Christo, et sic non video, quin affectans humanas laudes et gloriam propter vite sanctitatem sit detestandus ypocrita et mendaciter contrarius sibi ipsi, nam [p. 208] si talis prius est sanctus, luciferina affeccio laudis hominum extinguit sanctitatem quam reperit. Si sit semper non sanctus, inducit in se et populum blasfemum mendacium. Unde papa Petrus II Petri II. i prophetat de talibus: Erunt, inquit, pseudoprophete in populo, sicut in vobis erunt magistri mendaces, et post diffuse describit eos dicens, quod sunt velut irracionabilia pecora, in hiis que ignorant blasfemantes. Tales forentilli, qui dicerent, quod habent ex eleccione hominum eciam notorie perversorum potestatem absolvendi a pena et a culpa et concedendi ex supererogatis meritis sanctorum, distributis ad libitum indulgencias sine fine. Ettales communiter ignorant voces proprias: et illos beatus Judas describit per hoc, quod ma iestatem blasfemant, et ubi sanctus Michael disputans cum dyabolo pro Moysi corpore, non est ausus in ipsum inferre iudicium, hii tamquam muta animalia offendunt in hiis, que norunt noticia sensibili, cum audent ultra archangelum maledicere quibuscumque qui voluntati sue restiterint, licet ignorent de eis divinum iudicium. Et super hec blasfemant gravius dicentes, quod oportet Deum virtute eleccionis eis assistere et quecumque promiserint ad implere. Unde sanctus Apostolus describit eos nota sextuplici superborum: Hii, inquit, sunt in epulis suis macule, convivantes, sine timore se ipsos pascentes, nubes sine aqua, que a ventis circumferuntur, arbores autumpnales infructuose, bis mortue, eradicate fluctus feri maris, despumantes suas confusiones, sidera errancia, quibus procella tenebrarum conservata est in eternum. Et ista sex, cum sint scriptura sacra, decet [p. 209] exponere. Quantum ad duo prima, patet quod spectant ad peccatum carnis, cum quantum ad modum convivandi sunt macule in abstracto, convivant enim mundi dominos et carnales amicos contra doctrinam Christi Luce XIV, 12— 14: Cum facis prandium aut cenam, noli vocare amicos tuos neque cognatos neque vicinos neque divites, ne forte et ipsi reinvitent te et fiat tibi retribucio. Sed cum facis convivium, voca pauperes, debiles, claudos, cecos, et beatus eris. Istud autem servaretur in nobis potissime, qui vivimus de elemosinis laycorum et bonis pauperum. Quamvis autem licet convivare, tam spiritualiter infirmos quam sanos, ut spiritualiter edificentur et reedificent, hoc tamen non debet fieri racione commodi temporalis.

[ENGLISH]

## ¶2 · 209.17–209.22

> [p. 209] Secunda gentilitas est sessio, quam Christus docuit in facto aufugere, quando in eadem tabula atque perapside discipulos suos pavit, ut patet Matth. XXVI, quod non observant hii, qui sollempnizant convivia de bonis pauperum sedentes singulariter tamquam reges in solio.

[ENGLISH]

## ¶3 · 209.23–209.30

> [p. 209] Et quoad tercium scilicet modum prandii: Si in nostris episcopis sit gentilitas ritus ex superbia episcopi introducta, patet quod omnia eorum convivia sunt macule in abstracto, quod si secundo timore Dei postposito nimis sumptuose paverint se ipsos non pauperes, et hoc gracia voluptatis sue ac glorie secularis, quis dubitat, quin de illis prophetaverat sanctus Judas?

[ENGLISH]

## ¶4 · 209.31–210.14

> [p. 209] Quantum ad secundum iugum, quod concernit peccatum mundi, dicitur primo, quod sunt nubes sine aqua, que a ventis circumferuntur, nubes, que exalantur de terra, ut sint medium inter laycos et celum, scilicet ecclesiam triumphantem, quod si sint sine pluvia predicacionis, ad quemlibet impulsum venti fortune pro congregandis et [p. 210] conservandis temporalibus circumducti, signum est quod eclipsant radiacionem solis iusticie et signant pestilencias spirituales. Et quantum ad secundum, patet quod prelati racione ordinacionis divine, qua debent spiritualiter fructificare subiectis, debent esse arbores autumpnales. Quod si habent istam triplicitatem dyaboli, primo quod sint infructuosi quoad opus ewangeliste, secundo quod sint bis mortui secundum spiritualem racionem proprie persone et prelati, et tercio quod sint eradicati sine spe insercionis in vite vera fructificando secundum legem Christi, tunc sunt illi de quibus Apostolus prophetavit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 207.23: We must not claim praise of men for holiness.
- 208.9: Falsity of claim to distribute the merits of the Saints.
- 209.3: Those whose hospitality is for pleasure and show.
- 209.31: Those who not preaching are like waterless clouds,
- 210.4: Those who are like fruitless trees.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 207: *speculo* (25 is the line number) [R3]
  - 208: *II Petri* (one token covers two printed words) [R4]
  - 208: *sicut* [R3]
  - 208: *iestatem* (ma | iestatem split by folio bar (213a), no hyphen) [R5]
  - 208: *hii* [R4]
  - 209: *dominos* [NW]
  - 209: *facis* [R4]
  - 209: *facis* [R4]
  - 209: *cecos* (10 is the line number) [R4]
  - 209: *quin* (30 is the line number) [R4]
  - 209: *Quantum* [R3]
  - 208: *papa Petrus* (W-split: papaPetrus -> papa Petrus (x1 in the volume; scans: papapetrus | papapetrus | papa | papapetrus)) [OVERRIDE-SCAR]
  - 209: *12—* (LEFT-odd: dash between numerals; print 12—14) [OVERRIDE-SCARPLATE]
  - 210: *autumpnales.* (LEFT-nw: print = printed) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 6. Matth. XXIII, 12. (207.32).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 207:
5. Codd. in marg. : Viatur attendat Christum. 10. Codd. in marg. :
Antichrislus. 17. Codd. in marg. : Gloriam fugere (Cod.: sugere)
debet prelatus.

p. 208:
4. Codd. in marg. : Prelati mali qnomodo ab apostolis sunt descripli.
16. B: ut ubi. 21. Codd.: restituerint.
16. Judae Ep. I, 8, 0, 10. 24. Judae 12, i3.

p. 209:
(none)

p. 210:
(none)
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 207: Tnxta iter scandalum postierunt michi. | qni se exaltat humiliabiiur, et qni | se humiliat exaltabitur,
p. 208: propkete in populo, sicut iu vobis erunt uiagistri mendaceSj | iestatem blasfemant, | disputans cum dyabolo pro Moysi corpore, non est atisus in ipstim iuferre iudicium, hii tamquam muta auimalia ojfendunt in hiis, que norunt noticia sensibili, | sunt iu epulis suis macule, convivantes, siue timore se ipsos pascentes, nubcs sine aqua, que a ventis circumferuntur, arbores autumpnales infructuose. bis mortue, eradicatc, fluctus feri maris, | despumantes suas confusiones, sidera errancia, quibus procella tenebrarum conservata est in eternum.
p. 209: Citui facis prandium aut cenam, noli vocare amicos tuos neque cognatos neque vicinos neque divites, ne forte et ipsi reinvitent te et fiat tibi retribucio. Sed cum facis conviviunt, voca pauperes, debiles, >cIaudos, cecos, et beatus eris. | sine aqua,
p. 210: arbores autumpnales. | bis mortui | j cV j mar is despumantes suas confusiones; | sydera volancia;
```

---

## Chunk 09-f: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-09-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-09-f
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "210.15–214.2"
divisions: "cap. 9 (heading 'CAPITULUM NONUM.' at 194.7); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "853 words; 785 unanimous or majority-real; 53 settled by vote (DEL 2, R2 30, R3a 19, R5a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n271–n275 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 9, part 6: [TITLE]

## ¶1 · 210.15–212.14

> [p. 210] Quantum ad tercium iugum, quod concernit peccatum dyaboli, dicitur primo quod sunt fluctus feri maris despumantes suas confusiones; quod fit, quando Antichristi sunt instrumenta impii et crudelis dyaboli, cui proprietates maris inseparabiliter sunt coniuncte; tales enim involvunt simplices in caribdim, quando spumant mendacia de sua fantastica potestate; hoc enim erit eis blasfema confusio in die iudicii. Sexto et ultimo icitur dicitur quod tales pseudo sunt sydera volancia; tradunt enim naturales quod ex materia terrestri viscosa ad supremum intersticium aeris exalata fit materia secundum formam et disposicionem variam sublimita; et dicitur, postquam fuerit ignita et mota, nunc stella cadens, nunc draco ardens, et nunc stella cometa. Ita mortaliter ex statu laycali lutoso sunt aliqui ad supremum statum militantis ecclesie exaltati, quos cum malignus tetigerit, sunt succensi superbia, cupiditate et omni genere peccatorum, sed cum summe in Deum, qui est ignis, recalcitrant, decidunt secundum [p. 211] raciones Deo absconditas, nunc uno modo, nunc alio, in formam polipi vel abiecte materie, quibus procella tenebrarum perpetuo parata est post diem iudicii. Prepositi autem et specialiter summus pontifex timerent sibi de sensu hoc mistico et specialiter de superbia vel laude humana, de extollencia sui status; ipsa enim est spuma fantasticum Antichristi, cum ad nichil valet nisi ad frustrandum mercedem Domini dicentis Matth. VI, 2: Amen, dico vobis receperunt mercedem suam, et Joh. V, 44 quomodo potestis credere, qui gloriam ab invicem recipitis, et gloriam que a solo Deo est non queritis? Debemus enim, laudes humanas et occasiones earum aufugere, dicente Paulo papa, prima Tessa. II, 5, 6. 9 Neque, inquit, aliquando fuimus in sermone adulacionis sicut scitis, neque in occasione avaricie, Deus testis est, neque querentes ab hominibus gloriam, operantes continue, ne aliquem vestrum gravaremus, predicavimus in vobis evangelium Dei. Et antequam papa fuerit conversacione contrarius vite Pauli, dimitteret omnem eleccionem, omnem gloriacionem et omnem occupacionem, que hodie consequitur papas nostros. Unde beatus Crysostomus Omelia XXVIII Operis Imperfecti super Matth. XX, 27: Quicumque voluerit inter vos primus esse erit vester servus. Secularem, inquam, primatum desiderare et si racio non est, tamen causa est, quia etsi iustum non est, tamen utile est, primatum autem ecclesiasticum concupiscere neque racio est neque causa, quia neque iustum est neque utile. Quis enim sapiens ultro se subiceret servituti laboris, et quod [p. 212] maius est periculo tali, ut det racionem pro omni ecclesia apud iustum iudicem, nisi forte qui non credit iudicium Dei, nec timet uti abutens primatu suo ecclesiastico seculariter convertat eum in secularem. Ex istis videtur primo, quod non licet j papatum vel aliquam dignitatem ecclesiasticam eleccione humana appetere, quia ut sic primatus stulte se supponit periculo, stulte quia non humana eleccio facit ius presidendi, sed promulgat in casu, quo in electo presint virtutum insignia, et insuper constituit se obligaciorem ad populum, nec accrescit exinde profectus, sed periculum, et ideo sancti apostoli non susceperunt primatum talem ab homine.

[ENGLISH]

## ¶2 · 212.15–213.13

> [p. 212] Videtur secundo quod, sive Robertus sive: Urbanus, sive quicumque alius, appetit sic preesse ecclesie Anglie, signum probabile est quod sit fugibilis Antichristus; unde beatus Crysostomus ubi supra: Quicumque desideraverit primatum in terra, inveniet confusionem in celo, ut iam inter servos Christi non sit de primatu certamen, non festinet unusquisque, quomodo aliis maior appareat, sed quomodo omnibus inferior videatur, quoniam non qui maior fuerit in honore ille est iustior, sed qui inferior fuerit hic est maior. Ideo primatus in populo non est ab aliquo appetendus. Quomodo igitur non habebit ecclesia nostra talem suspectum, qui et nescit fidem scripture et se ipsum vel familiam suam privatam regere, et tamen presumit se digniorem sciencia et virtute, ut regat tantam ecclesiam? Utinam ecclesia vellet dicere talibus sentenciam Christi et beati Crysostomi Ad talem primatum pertinet respondere Deo pro animabus sibi subditis in die iudicii et servire illis evangelice laboriosius atque humilius, [p. 213] contempto omni seculari commodo vel honore. Quod si Robertus vel alius nobis facere voluent, non contradicimus, Deus sibi retribuat, unde beatus Crysostomus ubi supra: Principes ecclesie fiunt, ut serviant minoribus suis et ministrent eis quecumque acceperunt a Christo, ut suas utilitates negligant et illorum procurent, ut si opus fuerit nec mori recusent pro salute eorum, sicut fecit Apostolus. Cum igitur hec sit religio paparum, patet quam culpabiles a Deo sunt principes seculi, qui consensu stulto ipsam dissolverint, specialiter promittendo thesaurum regni et legiorum suorum ad ipsos confluere.

[ENGLISH]

## ¶3 · 213.14–213.28

> [p. 213] Tercio patet ex dictis quomodo sancti susceperunt primatus huiusmodi, scientes quod humana eleccio vel est primatui suo impertinens vel nociva. Est enim in primatu tali servitus laboriosa et mundo abiecta ac infructuosa, sed meritoria quoad Deum, et illam voluerunt sancti doctores pro fructu premii promerendo. Est secundo in primatu extollencia mundana periculosa et insufficiencia vel negligencia perficiendi officium ruinosa, que paulative augebatur racione dotacionis ecclesie, et illam noluerunt sancti pastores ecclesie; et hinc post dotacionem inolevit religio prelatorum, quod verbo et mente dicerent in talibus eleccionibus nolens volo, quia nolens hoc secundum nefarium volo primum.

[ENGLISH]

## ¶4 · 213.29–214.2

> [p. 213] Et patet in parte quomodo solvenda sunt dicta Crysostomi et obiectus communes facti in ista materia. Modo autem cautela dyaboli et incuria secularium ad perturbacionem magnam ecclesie, dicitur in facto contrarium, scilicet quod nolens ministerium evangelicum vel mercedem volo primatum et commodum temporale, et necesse [p. 214] est istam perversionem currere quousque hec duo separata fuerint sicut in ecclesia primitiva.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 210.15: Those who are like wild waves and become the instruments of the devil.
- 210.24: Those are like wandering stars who in high place in the Church are afire with pride.
- 211.4: All prelates should shun human praise.
- 212.5: Desire of Church dignities wrong and foolish.
- 212.15: The contention of the rival popes marks them as Antichrists.
- 212.31: Primacy involves responsibility for souls at the judgment and service here on earth.
- 213.1: Rulers of the Church should sacrifice their own advantage in all things.
- 213.16: The duties of a primacy are hard and default in it dangerous,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 210: *peccatum* [R3]
  - 210: *feri* [R4]
  - 210: *maris* [R3]
  - 211: *absconditas* [THIN]
  - 211: *9* (verse range "5, 6, 9:" ends the line above the box; the main scan lost the 9) [INS?]
  - 211: *si racio* (one main token covers two printed words) [THIN]
  - 211: *non* [THIN]
  - 212: *suo* [R4]
  - 212: *Crysostomi* (hyphenated Cryso-|stomi:; main token crysoad = Cryso + Ad with stomi lost, so the whole word here) [R4]
  - 212: *Ad* (printed "Ad" before talem; main glued it into crysoad) [INS?]
  - 212: *animabus* [NW]
  - 213: *facere* (the main "1" is a speck before facere; main misread facere as tacere at pos 13) [R3]
  - 213: *fiunt* [R4]
  - 213: *suas* [R4]
  - 213: *legiorum* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 210:
(none)

p. 211:
i5. papa; ita cod. 25. Codd. in marg.: Appelere primatum secu-
larem. 26. Codd. : /. Matlh. XX.
25. Recte Homilia XXXV ex cap. XX.

p. 212:
10. 13: causu; ib. Codd. : prefuit.

p. 213:
(none)

p. 214:
5. Codd. in marg. : Papa apostaticus. <>. Codd.: vel deest.
ayut : B: caput. 24. Codd.: electori. 29— 32. lege — lege twice.
6. Decr. Prima pars, dist LXXVIIII, cap. IX.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 210: arbores autumpnales. | bis mortui | j cV j mar is despumantes suas confusiones; | sydera volancia;
p. 211: Amen, dico vobis receperunt mercedem stiam, | quomodo potestis credere, qui gloriam ab invicem recipitis, et gloriam que a solo Deo est non queritis? | aliquando fuimus in sermone adulacionis sicut scitis, neque in occasione avaricie, Deus testis est, neque querentes ab hominibus gloriam, operantes continue, ne aliquem vestrum | gravaremus, predicavimus in vobis evangelium Dei. | Quicumque voluerit inter vos primus esse^ erit vester servus. Secularem, | primatum desiderare et siracio 11011 est, tamen causa est, quia etsi iustum 3o non est, tamen utile est, primatum autem ecclesiasticum concupiscere ueque racio est neque causa, quia neque iustum est neque utile. Ouis enim sapiens ultro se subiceret servituti laboris, et quod
p. 212: maius est periculo tali, ut det racionem pro omni ecclesia apud iustum indicem, nisi forte qui non credit iudicium Dei, nec timet uti abutens primatu sno ecclesiastico secularitcr convertat eum in se- | Quicumque desideraverit primatum in tcrra, inveniet confusionem in celo, ut iam inter | servos Christi non sit de primatu certamen, non festinet unusquisque, quomodo aliis maior appareat, sed quomodo omnibus inferior videatur, quoniam non qui maior fuerit in honore ille est iustior, sed qui inferior fuerit hic est maior.
p. 213: Principes ecclesie | fiunt, ut sevviant minoribus suis et ministrent eis quecumque acceperunt a Christo, ut suas utilitates negligant et illorum procurent, ut si opus fuerit nec mori recusent pro salute eorum, sicut fecit Apostolus.
p. 214: Si quis pecunia vci gracia humana vel tumuttu poputari sine canonica eleccione fuerit intronizaius, non apostoticus sed apostaficus habeatur.
```
