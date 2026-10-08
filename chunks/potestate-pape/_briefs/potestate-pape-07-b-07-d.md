# Translation brief: potestate-pape 07-b–07-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-07-b.md chunks/potestate-pape/wyc-potestate-pape-07-c.md chunks/potestate-pape/wyc-potestate-pape-07-d.md` once and fix what it reports.
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

## Glossary (the 231 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
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
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| forisfactura | forfeiture | Noun beside *forisfacere* "forfeit". Ruled 2026-10-02 (*Eccl.* 15). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
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
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 07-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "138.32–142.12"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "740 words; 707 unanimous or majority-real; 25 settled by vote (R2 12, R3a 3, R5a 9, R6a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n199–n203 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 2: [TITLE]

## ¶1 · 138.32–141.15

> [p. 138] Quantum ad secundum argumentum de illo Matth. X, ubi recitatis nominibus apostolorum Petrus preponitur, indubie notatur primatus Petri, [p. 139] quem Christus intenderat, ut scilicet Petrus sit capitaneus et pugil precipuus ad ducendum Christi exercitum sibi similius, scilicet fide, humilitate et passione, ideo Petrus querendo de vita evangeliste signantis vitam contemplativam recepit responsum a Deo: Quid ad te, tu me sequere Joh. ultimo, 19. Istum igitur sensum comportant argumenta duo facta, ut sepe repecii, et non dominacionem vel honorem secularem, aut, ut dicit Bernhardus, potestatem seculariter castigandi; sicut caput verbis et intuitu, non autem corporali invasione vel instrumentali defensione, pascit et regit residuum corporis, quod si pape deficiunt visus, auditus et omnis sensus ad regendum capitaliter corpus Christi, quid sibi et pape vel capiti Christi ecclesie? Revera nulla eleccio vel approbacio humana potest facere quod talis fit caput vel articulus Christi ecclesie, sed mendaciter presumendo sic nomen fit caput ecclesie malignancium et synagoge sathane. Homo enim habet ex se potenciam vadendi et esse membrum dyaboli, sed non habet nisi a Deo esse membrum ecclesie; oportet enim proximum Christi vicarium esse instar sui spiritualem, ut docet Luce IX, 55, 56 de tribus apostolis appetentibus humanam vindictam: Nescitis, inquit Christus, cuius spiritus estis, filius hominis non venit animas perdere sed salvare. Miticia namque et non guerra possidebunt terram vivencium, ut docet Veritas Matth. V. Et hinc notat Crysostomus super primam epistolam Thym. Omelie V: Non, inquit, ait apostolus auctorabiliter neque dominative neque cum potestate, sed fili, ait, Thymothee, et ideo [p. 140] dicit Bernhardus, quod pascendas non premendas suscepit Eugenius oves Christi; debet enim pugnare tamquam spiritualis miles cum gladio spiritus, ad spiritualem Dei iniuriam vindicandam. Sed postquam mixta est cum religione sacerdotum civilitas, surrepsit in clero superbia, civilis exaccio et monstruosum dominium, ita quod illud Psalmi IX de Antichristo loquentis verificatur hodie: Dum superbit impius, incenditur pauper. Et quantum ad illud tactum de clavibus singulariter datis Petro, ut dictum est, nulli fideli licet ambigere; quin Petrus tamquam generalis attornatus gerebat personam ecclesie, ubi recepit potestatem non singulariter pro se et quocumque Romano pontifice sed generaliter et supereminenter pro quocumque sacerdote similius sequenti, cui est quicumque locus vel eleccio humana impertinens, quia donacio istarum clavium est divinum misterium. Sunt enim dicte claves potestas et sciencia ad edificandum ecclesiam, que signanter debent esse in quolibet sacerdote, et (ut credo) erant in Paulo excellencius quam m Petro. Cum enim impium videtur sine racione ponere in Petro ocium et potestatis abusum, Paulus autem ex fide scripture prima Cor. XV, 10 plus omnibus laboravit, videtur quod habuit amplius potestatis; laboravit, inquam, evangelizando, scribendo et persecuciones amplius paciendo, et clavis potestatis regiminis quam dicimus auctoritatem singulariter Petro competere non fundatur. Potestas enim ad regendum ecclesiam [p. 141] datur unicuique episcopo, quantum potest matri sue proficere, sive evangelizando sive sacramenta ministrando sive oracione, contemplacione, exemplacione edificando. Unde propter excellenciam, quam debemus habere, claves iste dicuntur singulariter sacerdotibus Christi competere, sic quod potestas sit materiale spiritualis clavis presbiteri, et formale est sciencia Dei; non sciencia mathematica, non logica vel disputacio scolastica, sed sciencia scripture, quam episcopus debet excellenter cognoscere et docere. Unde sicut materia prima non potest esse sine forma materiali nec econtra, sic videtur michi quod potestas clavium sacerdotalium non potest esse sine predicta sciencia nec econtra.

[ENGLISH]

## ¶2 · 141.16–142.12

> [p. 141] Unde Johannes XXII et alii seculum sapientes, quia non excesserant in istis clavibus et earum officiis, finxerunt claves potestatis et auctoritatis, quas congregando pecunias simplices sue tyrannidi et ypocrisi subiecerunt. Sicut enim sunt due vie, una descendendi in viciis ad infernum et alia ascendendi in virtutibus ad ecclesiam triumphantem, sic sunt due porte sive introitus. Sacerdos autem debet habere claves ad serandum portas inferi a simplicibus sibi subditis et ad aperiendum simplicibus portas celi, et sic debet aperire pascendis ovibus thesaurum virtutum, et ipse primo virtuosis operibus sequelam ovium exemplantibus et excitantibus introire. Unde quotquot potestates vel sciencias tales prelatus habuit, tot claves habet, que omnes solum duas constituunt. Quod autem claves iste specificantur ad excomunicaciones et absoluciones, Deus huius seculi per fastum et avariciam cecando simplices introduxit. [p. 142] Et sic intelligo decretum XXIV, q. I, Quodcumque cum eis similibus, que omnia oportet intelligi potestate militantis ecclesie non errante; quod solum est verum quando iudicio triumphantis ecclesie est conformis; non enim potest aliter aperire ianuam regni celorum eciam sibi ipsi. Si autem claves iste quoad materiam sint verse in affeccionem terrenam et quoad formam declinant monstruose a sciencia apostolorum ad artem luciferi, necesse est quod tales suis clavibus aperiant portas suas et dogmatizent discipulorum suorum precipicium ad infernum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 139.1: Peter was not to maintain his primacy by force,
- 140.10: The gift of the keys was to Peter as attorney for the Church.
- 140.22: Paul held the keys (knowledge and power) even better than Peter.
- 141.16: John XXII an others forged keys which subjected simple men to their tyranny.
- 141.29: It is false that the keys mean excommunication and absolution.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 139: *a Deo* (one token covers two printed words) [THIN]
  - 139: *Quid* [THIN]
  - 139: *tu* [R3]
  - 139: *sed fili* (one token covers two printed words) [R6]
  - 140: *∅* (English side-note word) [R6]
  - 140: *supereminenter* (hyphenated superemi-nenter; main token covers whole word) [R4]
  - 140: *∅* (second half of superemi-nenter, main scan already holds whole word) [INS?]
  - 142: *aliter* (S-split: one word; print = aliter (no s); margin figure after it is a line number) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Peter's (142.13).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 138:
18. Cap. I, p. 769. 24. Cap. VI, p. 749. Recte: ministerium
tuum et ministerium te.

p. 139:
30. A in marg. : Claves Petrus recepit non simpliciter pro se sed ge-
neraliter pro ecclesia.
31. Opp. tom. XI, 527.

p. 140:
7. A in marg. : Ad 2; B in marg. : Ad secundum in secundo argu-
mento. 10. A in marg. : Ad 2 in secundo argumento. 19. AB in
marg. : Claves potestas et sciencia ad cdificandum ecclesiam; ib. A in
marg. : Claves Petrus recepit non singulariter pro se sed generaliter pro
ecclesia. 25. AB in marg. : Paulus habuit amplius potestatis.
1. Ubi supra. 9. Psal. X (sec. Hebr.) 2.

p. 141:
17. non ; adde: parum; ib. AB in marg. : Clavium abusus quomodo Jit.

p. 142:
1, 2. B: Quicunque. i3. B in marg. : Ad 3.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 138: intelligit scripttiram sacram, qtiam Spiritus Sanctus flagitat, | Nullum tibi venenum, nullum gladium plus formido, quam libidinem dominandi; | Si hec faciSf | honorificas ministerium tuum, non mediocris est iste principatus. Hoc enim est ex- | tirpare malas bestias a terminis tttis, quo greges tui securi in pascua educantur. Domabis lupos } sed ovibus non dominaberis. Pascendas utique non premendas suscepisti.
p. 139: Qnid ad te, tu me sequere | cuius spiritus estis, filius hominis non venit animas perdere sed salvare. | ait apostolus auctorabiliter neque dominative neque cum potestate, sedfili,
p. 140: pascendas non premendas | Dum superbit impius, incenditur pauper. | plus omnibus laboravit,
```

---

## Chunk 07-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "142.13–146.33"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1052 words; 980 unanimous or majority-real; 55 settled by vote (R2 33, R3a 13, R5a 9); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n203–n207 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 3: [TITLE]

## ¶1 · 142.13–144.30

> [p. 142] Quantum ad tercium argumentum de adventu Petri ad dominum super aquas cum aliis exemplis audaciam Petri signantibus, patet quod docent ad sensum expositum vicarium Petri obligari diversissime ad faciendum similiter. Unde non video quomodo patencius, turpius aut convincibilius posset papa mendax allegare pro sua preeminencia quam afferre dictas autoritates ad confirmacionem sue preeminencie, faciendo ad sensum misticum eis contrarium; quia hoc esset afferre dampnacionem suam ex verbis propriis. Cum igitur ambulacio Petri super aquas signat suppeditacionem temporalium sub- affeccione per quam viam vicarius Petri ut talis duceret ecclesiam plus vel minus, que maior confusio quam allegare illud iudicium ex lege Domini et cum hoc vivendo sub aquis mundi profundius in fastu et questu seculi, perplexius profundari? Deus enim ex ore proprio iudicat huiusmodi servum nequam. Si igitur sequimur Petrum moraliter in dictis audaciis, debemus postponere vecordiam omnium omissionum temporalium, omnium tribulacionum [p. 143] corporalium et omnium amissionum favorum mundialium, ut similius sequamur Christum et Petrum et induemus formalius corpus suum, cum secundum doctrinam prima Petri V, 3 debemus esse forma facti gregis non coacte sed ex animo. Quomodo igitur non proficit sed officit ad hoc seculare dominium; unde beatus Evangelista prenuncius Antichristi, qui statum tocius ecclesie previdit prophetice Apoc. XII, 3— 4 sic effatur: Ecce, inquit, draco magnus rufus habens capita septem et cornua decem et in capitibus eius septem dyademata, eciam cauda eius trahebat terciam partem stellarum celi, et misit eas in terram, et draco stetit ante mulierem, que erat paritura, ut cum peperisset, filium devoraret. Mulier ista amicta sole habens lunam sub pedibus est mater ecclesia, sponsa Christi, habens ipsum qui est sol iusticia amplexantem, cum de sponso Cantic. II, 5 dicit sponsa Christi: Leva eius sub capite meo, et dextra illius amplexabatur me. Ista mulier habet lunam sub pedibus, quando omnia temporalia, que sunt ut luna mutabilia, appetitui ecclesie substernuntur iuxta illud Apostoli Philipp. III. Omnia detrimentum esse et arbitror ut stercora, ut Christum lucrifaciam. Hec mulier habet capitaliter duodecim apostolos et eorum veros vicarios; hec mulier, ut dicit Johannes, parturiens cruciatur ut pariat, quia Christi vicarii signando Christum in animabus fidelium, utrimque sicut oportet varie tribulantur, cum Act. XIV, 21 dicitur per multas tribulaciones oportet nos intrare in regnum celorum et prima Cor. IV, 15 post multas tribulaciones expressas dicit Apostolus in Christo Jesu per evangelium, [p. 144] ego vos genui Et Gal. IV, 19 signanter dicit Apostolus: filioli mei quos iterum parturio, donec formetur Christus in vobis. Ideo dicitur quod mulier peperit filium masculum, qui redempturus est omnes gentes. Draco autem est quicumque capitalis in ecclesia Antichristi, draco propter venenum ypocrisis et voracitatem populi simplicis. Magnus autem propter pretensionem potencie, rufus propter effusionem sanguinis, quem consilio, auxilio et specialiter omissione causat in ecclesia ex consensu; necesse quidem est ut veniant bella inter gentes et regna pro inordinato amore temporalium, quando sacerdotes Christi, qui debent mundum relinquere, sunt maxime mundiales. Septem capita sunt universitas peccatorum vel evidenciarum, quibus suadet se esse caput ecclesie. Et decem cornua universitas potentatuum, quimilitant sub vexillo huius principis Antichristi. Cauda eius est cleri communitas, que exemplo suo trahit stellas in terram, quando viros contemplativos inducit, ut deserentes splendorem virtutum et situm altum in firmamento ecclesie mundialiter conversantur. Oportet igitur quod Christi vicarius sit minime mundialis, ut patet Joh. XVII, et I. Joh. V, quia aliter submergit se in mari non cum Petro ambulans fideliter super aquas. Et iste sentencia evangelica movebat beatum Bernhardum libro III ad Eugenium, quando dixit: Nullum tibi venenum, nullum gladium tibi formido, quam libidinem dominandi.

[ENGLISH]

## ¶2 · 144.31–146.22

> [p. 144] Unde Augustinus sermone XIV De Verbis Domini notans navicellam Petri signare ecclesiam et mare seculum, cuius fluctus sunt persecuciones tyrannorum inflicte fidelibus, docet quomodo [p. 145] nauta huius navicelle debet artemonem arbori crucis infigere et ipsum lignum cum Christo suspenso ut velum erigere et sic eum efficaciter respiciens erit securus a turbine. Et hinc dicit sPetrus nauta huius navicelle: Christus passus est pro nobis, nobis relinquens exemplum, ut sequamur vestigia eius. Et beatus Johannes: Sicut Christus pro nobis animam suam posuit et nos debemus pro fratribus animam ponere. Huic igitur velo simplex conversacio et vera confessio religentur et tuti esse possumus, quantumlibet mare seviat aut ventus incuciat, quod nostra navicella non mergetur; quantumlibet inter flatus et fluctus seculi conturbetur. Sed notet fidelis quod in ista nave non navigat nisi qui in humilitate et paupertate odit seculum, sequendo Christi vestigia. Ideo dicat fidelis prepositus: Si tu est Christus, non miror si solidam carnem super liquantes aquas suspenderis, sed fac quod mirer, iube me ex potestate divina venire ad te super aquas, quod non facit fidelis ad sensum misticum nisi calcata affeccione cunctorum temporalium imitetur Christum in moribus, et sic papa prepollens in talibus est verus Christi vicarius, ut tangitur in quarto argumento, quo Petrus Joh. ultimo misit se in mare ex calore fidei satis salvum. In quo; ut reor, datur intelligi quod stat christianum meritorie sequi Christi vestigia et sic esse in corpore Christi mistico, quod est Petri navicula, licet videatur in facie errantis ecclesie esse foris. Decet enim scripturam sacram esse gravidatam multiformi [p. 146] sentencia, ut preter literam factum illud signat iuxta quod martyrio cicius venitur ad Christum stantem in eternitatis littore, quam contemplacione vel officio confessorum. Et preter hec tercio signatur quod sicut apud Deum est possibile quod quis intromittat se cum mundo et adiutorio ac miraculo suo evadat periculum, ut dicit Christus Luce XVIII, 24 27 quam difficile qui pecunias habent regnum Dei introibunt; facilius est camelum per foramen acus transire, quam divitem in regnum Dei. Et dixerunt, qui hec audiebant, et quis potest salvus fieri? Et ait illis: que impossibilia sunt apud homines possibilia sunt apud Deum. Et videtur michi quod illam difficultatem signavit Petrus Matth. XIV, 30, quando veniens super aquas ad Dominum propter ventum validum cepit mergi; quamvis enim multi divites proni ad pompam, quos oportet finaliter mundum deserere, innitentes Christi adiutorio salvabuntur, via tamen veniendi navigio est clero securior, quia lignum salutis supponitur, ut medium impulsivum periculorum, que ex aquis mundi contigerint.

[ENGLISH]

## ¶3 · 146.23–146.33

> [p. 146] Ex quo videtur quod clerus sed papa precipue debet viare per illam semitam, in qua posset securius et expedicius sequi Christum; securius, quia status exproprietarius est elongacior a periculo temptatorum, et expedicius, quia minus intricatur cum mundo et hostibus, qui a legis Dei observancia retardarent. Unde propulsa vecordia ex temporalium pinguedine talis exproprietarius est ad martyrium pro Christo paracior; in cuius signum cronicantes notant quod post dotacionem fuerunt pauci vel nulli pape martyres.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 142.13: Peter's boldness in walking on the sea gives no authority to his vicar.
- 142.32: His courage should be an example,
- 143.1: teaching us not to fear worldly trouble,
- 143.14: In the Apocalypse the woman is the Church and the changing moon beneath her feet a symbol of things temporal.
- 144.6: The dragon signifies the chief Antichrist.
- 145.1: How the ship of the Church is to be navigated.
- 145.15: The navigator must follow Christ in humility and poverty.
- 146.5: The rich man may be saved by Christ's power, but the way of poverty is safer.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 142: *ad* [R3]
  - 142: *ad* [R3]
  - 142: *iudicium* [R3]
  - 143: *animabus* [NW]
  - 144: *genui* [THIN]
  - 144: *pretensionem* [NW]
  - 144: *Et decem* (one token covers two printed words) [R4]
  - 145: *velo* (print has v) [R3]
  - 145: *tu* [R3]
  - 145: *mistico* (30 is the line number) [R4]
  - 146: *Luce* [THIN]
  - 146: *XVIII* [THIN]
  - 146: *24* [THIN]
  - 146: *27* [THIN]
  - 142: *audaciis,* (W1: audacns, -> audaciis, (scans: audacns | audacus | audaciis | audacns)) [OVERRIDE-SCAR]
  - 143: *Christi,* (W1: Chnsti, -> Christi, (scans: christi | chnsti | cnnsti | chnsti)) [OVERRIDE-SCAR]
  - 143: *Christum* (W2: print = Christum (OCR chnstum is noise)) [OVERRIDE-SCARPLATE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Peter's (142.13).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 142:
1, 2. B: Quicunque. i3. B in marg. : Ad 3.

p. 143:
3. induemus (sic); Cod.: minemus. 4. Cod.: Petri IV. 10. AB in
marg. : Mulier ecclesia sancta cuius filium araco voluit devorare.
24. esse. Codd.: feci.

p. 144:
■ 8. B in marg. : Draco agnus rufus.
28. Ubi supra. 3i. Opp. tom. V, Append. p. 1 32.

p. 145:
i. artemonem ; B in marg. : anlempnam. Aug. : Sed in his sensacionibus
erigatur antenna. 5. AB in marg. : Petri navicula. 6. Codd.: se-
quimur.
5. I. Petri I, 21. 7. I. Joh. III, 16. 9. Aug. 1. c. loosely
quoted. 17. Matth. XIV, 28. 26. Joh. XXI, 7.
De Potestate Pape. IO

p. 146:
(none)
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 143: forma facti gregis non coacte sed ex animo. | draco magnus rufus habens capita septem et cornua decem et in capitibus eius septem dyademata, eciam cauda eius trahebat terciam partem stellarum celi, et misit eas in terram, et draco stetit ante mulierem, que erat | loparitura, ut cum pepensset, filium devoraret. | eius sub capite meo, et dextra illius amplexabatur me. | Omnia detrimentum esse | arbitror ut stercora. ut Christum lucrifaciam. | per multas tribulaciones oportet nos intrare in regnum celorum | in Christo Jesu per evangelium,
p. 144: ego vos genuu | filioli mei qitos iterum parturio, donec formetur Christus in vobis. | Nullum tibi venenum, nullum gladium tibi formido, quam libidinem dominandi. | navicellam Petri signare ecclesiam et mare seculum,
p. 145: Christus passus est pro nobis, nobis relinquens exemplum, ut sequamur vestigia eius. | Sicut Christus pro nobis animam suam posuit et nos debemus pro fratribus animam ponere. Huic igitur velo | simplex conversacio et vera confessio religentur et tuti esse possumus y quantumlibet mare seviat aut ventus incuciat, quod nostra navicella non mergetur; quantumlibet inter flatus et fluctus seculi conturbetur. | Si tu est Christus, | sed fac | iube me | venire ad te super aquas, | misit se in mare
p. 146: quam difficile qui pecunias habent regnum Dei introibunt; facilius est camelum per foramen acus transire, quam divitem in regnum | Dei. Et dixeritnt, qui hec audiebant, et quis potest salvus fieri? Et ait illis: que impossibilia sunt apud homines possibilia sunt apud Deum. | et facilius.
```

---

## Chunk 07-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-07-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-07-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "146.34–147.26"
divisions: "cap. 7 (heading 'CAPITULUM SEPTIMUM.' at 135.12); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "173 words; 162 unanimous or majority-real; 8 settled by vote (R2 6, R3a 1, R5a 1); 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n207–n208 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 7, part 4: [TITLE]

## ¶1 · 146.34–147.26

> [p. 146] Nec obest talis sensus varietas, cum aqua nunc signat divicias, nunc tribulaciones et nunc populum [p. 147] in scriptura. Posset et quartus sensus moralis elici ex isto opere secundum doctrinam Crysost, super secundo capitulo, II. Thym, morali V, scilicet quod vadentes in mundi diviciis tamquam vertiginosi habent de spiritualibus incertum iudicium. Constat quidem naturalibus quomodo in vertiginosis spiritus, qui sunt vehicula interiorum sensuum, circumducti faciunt apparenciam eciam quieti corporis, ac si corrotaretur homine stante fixo. Sic cogitacione et fantasia fixis in temporalibus detecto timore Dei inmobilis, diviciis se sperificantibus ad corrupcionem sensibilium instar aque, necesse est fantasiam et affeccionem vertiginosi proporcionaliter circumduci; et talis non foret bonus dux itineris ad sequendum. Unde erivatis multis malis avaricie imaginatur iste sanctus animam talis extrahi et peccata sua in qualitates sensibiles commutari. Videres tunc, inquit, animam pallidam trementem, verecundantem, velatam, agoniam habentem, se ipsam miserabiliter contempnentem. Et hec racio quare Christus voluit duces sue ecclesie instar sui a mundialibus elongari, ne fantasia corrupta contempnant veras divicias, et talis indubie licet reputacione humana, tamen non auctoritate Domini foret papa.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 147.4: A man engaged in worldly pursuits sees spiritual things confusedly.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 147: *morali* (hyphenated mo-rali; main token covers whole word) [R4]
  - 147: *spiritualibus* [NW]
  - 147: *incertum* (hyphenated in-certum; main token covers whole word) [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 146:
(none)

p. 147:
4. Codd.: vadantes. 12. sperificantibus. B: ad modum spere se ro-
tantibus ; additur et in A in marg. 25. tamen; A: tantum. 27. B in
marg. : Ad 5. 3i. AB in marg. : Papa non est verus vicarius Christi,
dum Christum non imitatur.
3. In Ep. II ad Timoth. cap. II Hom. V, Opp. tom. XI, 628.
19. pag. 628.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 146: quam difficile qui pecunias habent regnum Dei introibunt; facilius est camelum per foramen acus transire, quam divitem in regnum | Dei. Et dixeritnt, qui hec audiebant, et quis potest salvus fieri? Et ait illis: que impossibilia sunt apud homines possibilia sunt apud Deum. | et facilius.
p. 147: Videres tunc, | animam pallidam trementem, loverecundantem, velatam, agoniam habeutem, se ipsam miserabiliter contempnentem. | non dormitabit neque | dormiet, qui custodit Ysrahel,
```
