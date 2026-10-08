# Translation brief: potestate-pape 10-b–10-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-10-b.md chunks/potestate-pape/wyc-potestate-pape-10-c.md chunks/potestate-pape/wyc-potestate-pape-10-d.md` once and fix what it reports.
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

## Glossary (the 298 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| dotacio | endowment | |
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
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
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
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| caracter in actu | character in act | Ruled 2026-10-02 (*Eccl.* 21, 513.18). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| obsequium (for the dead) | duty | Kept apart from *servicium* "service", *officium* "office". Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| iurisdiccio | jurisdiction | Cf. *potestas iurisdiccionis*. Ruled 2026-10-07 (*Pot. pape* 23.17). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
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
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| negociatores | dealers | Kept apart from *mercantes* "traders" (*Eccl.*); the servants of the talents parable (Matt. 25). Ruled 2026-10-07 (*Pot. pape* 101.7). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| negociacio | dealing | Pairs with *negociatores* "dealers". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 194.5). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio | boast; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |

---

## Chunk 10-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "223.13–228.13"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 2 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1119 words; 1013 unanimous or majority-real; 89 settled by vote (R2 52, R3a 19, R5a 15, R6a 3); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n284–n289 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 2: [TITLE]

## ¶1 · 223.13–228.13

> [p. 223] Quantum ad primum obiectum de ministerii pape insufficiencia, patet quod falsum assumitur, ut patet de Christo, Petro et ceteris papis, sub quibus crevit ecclesia. A tempore autem, quo dimisso papali officio mundo intenderant, de tanto erant magis circa temporalia sitibundi, quia Ecclesiastes V, 9 dicit Salamon: Avarus non implebitur pecunia, et qui amat divicias fructus non capiet ex eis. Unde in predicta cronica que intitulatur Flores historiarum dicitur, quomodo anno domini 1226 magister Otho nunccius domini pape ostendit literas domini pape consilio regni nostri apud Westmonasterium, in quibus papa allegavit scandalum Romane ecclesie et obprobrium vetustissimum, notam scilicet cupiditatis que radix est omnium malorum, in hoc precipue, quod nullus potest aliquod negocium in Romana curia expedire, nisi effusa magna summa pecunie et donorum exhibicione. Sed quoniam scandali huius et infamie Romana paupertas est causa, deberent matris inopiam [p. 224] sublevare filii naturales, quia nisi a vobis et aliis viris honestis dona receperimus, deficerent nobis vite necessaria, quod esset omnino Romane incongruum dignitati. Ad illud itaque scandalum penitus eradicandum per consilium fratrum nostrorum sancte Romane ecclesie cardinalium, quandam providimus formam, cui si volueritis consentire, a scandalo matrem vestram poteritis liberare et in curia sine donorum obsequio exhibicionem iusticie obtinere. Forma autem provisa est hec: Petimus inprimis ab omnibus ecclesiis cathedralibus duas nobis prebendas exhiberi, unam de porcione episcopi et alteram de capitulo, et similiter de cenobiis, ubi diverse sunt porciones abbatis et conventus, a conventibus quantum pertinet ad unum monachum equali facta distribucione bonorum suorum, et tantumdem de abbate. Sed postquam maturatum est consilium, posuerunt responsum in ore magistri Johannis archidiaconi Bedfordensis, qui, cum dixisset nunccio quod peticio concernit ius regis, ius dominorum secularium et multorum absencium patronorum, clerus ille non potuit in eorum absencia finaliter respondere. Interimque venit dominus Johannes Marescallus et alii nunccii regis, districcius inhibentes quod nec clerus nec Otto nunccius attemptet aliquid quod tangit feodum regis nec molestet clerum Anglie, qui tenet baronias vel alias elemosinas de rege in capite. Sic scandalosa pape peticio est frustrata. Habet autem mandatum regis racionem vivacem. Cum enim ante dotacionem ecclesie fuit regnum nostrum iure possessionatum conformiter legi Christi, nimis monstruosum foret quod papalis exaccio extorqueret aliquid contrarium iuri regni. Rex autem nedum debet defendere secularem ecclesiam, sed [p. 225] ecclesiam cleri Anglie in sua libertate primeva, ut dicit beatus Ysidorus de summo bono libro III et corporatur XXIII questio V: Principes. Christus autem prohibuit vicariis suis dominacionem huiusmodi, et in signum confirmacionis ac subieccionis cleris seculari dominio dedit per Petrum tributum Cesari, ut patet Matth. XVII; potens igitur blasfemie tali resistere et omittens nimis est culpabilis ex consensu. Et dico quod fuit scandalosa peticio, quia non posset patencius accusare curiam, quam sibi contradictorius nominat sanctam sedem. Si enim tanta cupiditatis macula sic regnat in illa curia, indubie sequitur quod papa et cardinales sunt rei illius criminis vel consenciendo, auctorizando vel ipse in persona propria illam facinorosam cupidinem committendo; nam ex fide pro nullo bono possibili committerent tantum crimen, igitur multo magis non pro temporali iudicio tantum ab apostolicis alieno. Iterum, videtur quod forma excedit peticionem apostolicam, tum quia multi centenarii paparum possent de tanta elemosina sustentari, eciam complendo plenum papale officium, ut dicit Bernhardus libro IV ad Eugenium, et testatur Apostolus prima Thim. VI, 8—10, ubi dicens quod radix omnium malorum est cupiditas pro remedio sic subdit: Habentes igitur alimenta et quibus tegamur hiis contenti simus. Forma igitur apostolica ibi deest, cum Apostolus consulit pro relevamine multorum sanctorum Jerusalem quod quilibet ecclesie Chorinthiorum qui voluerit benediccionem dare sanctis Jerusalem reponat quod placuerit dare abscondite, ut patet II. Cor. IX. [p. 226] Hic autem papa et cardinales diffiniunt dominative quantum de redditu annuali in animarum periculum papa vult habere de Anglia, Ista, inquam. non est vox egentis sed exactoris bona pauperum rapina subdola subtrahentis. Cum enim papa ante dotacionem ecclesie sine tali elemosina melius exercuit papale officium et post dotacionem ad valorem multiplicis regni nostri sit magis cupidus et in operibus plus remissus, probabile est quod plus elemosine magis accenderet eius cupidinem, ut dixi superius ex Salamonis sentencia Ecclesiastes V. Sic enim contingit in aliis regnis nostri: temporis, quos dotarunt domini, ut quiecius complerent episcopale officium et minus subditos onerarent, in quo, quia dereliquerunt Christi regulam, in toto contingit oppositum. Sunt enim in visitacionibus plus cupidi, minus intendentes spirituali profectui et plus subditis onerosi, in tantum quod, ut experti referunt, multitudo ministrorum episcopi excoriat pauperes, ut scriptor, sigillator, barbitonsor et ceteri secundum superfluas cerimonias introducti. Item, querendum est quo iure papa vendicat a regno Anglie tam dominanter subsidium; non iure divino, cum ipsum limitat vite necessaria, de quanto sustentat in evangelio laborantem, ut patet I. Cor. IX. Cum igitur papa non evangelizat Anglie, sed consumendo personas atque pecuniam per suam vocatam iusticiam multipliciter debilitat regnum nostrum, videtur quod non exinde meretur a nobis benediccionem recipere. Ideo oportet quod iure cesaris vendicet huiusmodi principatum, ut multipliciter declaratum est VIII cap. Sed cum regnum Anglie non subiacet Romano imperio, videtur quod non iure vel concessione [p. 227] cesaris debet ipse dominium in nobis vel nostris possessionibus vendicare. Non enim habet ex titulo cesaris amplius dominium, quam originaliter habuit qui donavit. Sed patet ex facto et cronicis quod rex noster devicit cesarem, licet ad morulam ex casu proditorio sibi per modum tyrannidis est subiectus. Notet igitur homo cartam cesaris de dotacione ecclesie XCVI distinccione Constantinus cum aliis cronicis, et videbit quod regnum nostrum, sicut non subiugatur imperio, sic nec Romano pontifici, nisi sicut quilibet christianus debet ex lege caritatis subdi alteri, et conversi fuerunt subditi sancto Petro. Sed longe hoc a forma sic vendicandi subsidium. Unde videtur michi quod consulendum est regno Anglie quod eo accepcius subdatur vero pape (sicut contigit de multis Romanis episcopis) quo liberius modo quo debet homo promerens illud facit, cavendo semper ne aliquis pontifex vendicando dominium blasfemet in eum, quia nichil magis enervat imperium. Sic enim translatum est Romanum imperium in Germanos et tantum aporiatur quod vix sibi subditur civiliter dux vel comes. Et generaliter sic decrescit dominium quod est blasfemo clericali dominio subiugatum. Satis est igitur quod regnum nostrum tantum sibi obediat, quantum docere potest ex scriptura, in qua est omnis veritas, quod populus obedire debuit sancto Petro, docto ex sanctitate vite et operis quod sit verus Petri vicarius, ymo posito quod sit blasfemus, adhuc videtur michi quod populus debet obedire sibi dupliciter: [p. 228] primo in quantum est creatura Dei, dicens naturaliter veritatem catholicam faciendam, et secundo resistendo, dum a lege Dei exorbitat, cum naturaliter illud petit. Sic autem obedivit Paulus Petro Gal. II et sic obedierunt reges et clerici pseudopapis ipsos deponendo. Obediendo autem homini secundum racionem falsam, ut puta secundum racionem qua false creditur habere potestatem vel excellenciam quam adeo non habeat, est utrumque peccatum dampnabile, cum ut sic colitur Antichristus et abhominacio desolacionis stans in templo, de qua legitur evangelium cum propheta.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 223.13: The plea is false, tor the Church throve most when poor.
- 223.23: Attempt at extortion by the pope's legate Otto.
- 224.22: How it was repelled.
- 225.9: The request was scandalous.
- 225.20: It claimed much more than was needed and did not follow the precedent of St. Paul.
- 226.12: Experience shews evil of endowment.
- 226.23: The pope has no right to exact money from England.
- 227.7: Constantine's donation gives no dominion here.
- 227.21: Harm done by the popes in weakenig the Empire.
- 227.30: Limits of obedience to the Pope.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 223: *ut* (15 is the line number) [R4]
  - 223: *Flores* [R4]
  - 224: *naturales* [THIN]
  - 224: *penitus* [R4]
  - 224: *obtinere* [NW]
  - 224: *multorum* [R4]
  - 224: *clerus* [R4]
  - 225: *illa* [R3]
  - 225: *8—10* (print "Thim. VI, 8—10,"; one token) [R3]
  - 225: *cupiditas* [R4]
  - 225: *hiis* [R4]
  - 226: *annuali* [R4]
  - 226: *nostri* [R4]
  - 227: *∅* (15 is the line number) [R4]
  - 227: *vite* (30 is the line number) [R4]
  - 225: *relevamine* (LEFT-nw: hyphenated rele-|vamine; print has v) [OVERRIDE-SCARPLATE]
  - 226: *rapina* (LEFT-odd: box in blank gap after rapina; nothing printed there) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 223:
23. A in marg. : Nota. 29. A in marg.: Pape postulacio pvo sub-
9. Opp. tom. VIII, App. pag. 79, cap. XXXVIII. 22. Flores
Historiarum ed. by H. R. Luard vol. II, 184.

p. 224:
5. Codd.: eradicandum dccst. Addidi.

p. 225:
i5 . auctori\ando ; codd.: autendo. Cf. Sex species consensus, e. £.
Serm. IV, 359 ipse; ita codd.
3. Decreti Secunda Pars, Causa XXIII, Quaest. V, cap. XX.
De Potestate Pape. ! 5

p. 226:
25. Codd. : rure Jomhtio. 26. A: sustentant.

p. 227:
17. Codd. : Sed contigit. Hic locus corruptus esse videtur. 32. Codd.
in marg. : Obedire pape.
7. Rex Richardus captus a duce Austriae et venditus imperatori
Henrico v. Flor Hist. I, 107, 114 e Matth. Paris II, 394.

p. 228:
14. Codd. in marg. : Potestatem papa si habeat a domino.
11. Matth. XXIV, i5; Dan. IX, 27. 16. Gap. II.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 223: Bomim est facultates cum | dispensacione erogare pauperibus, sed melius est pro intencione seqnendi Dominum semel douare, et absohitum sollicitudine egere cum Christo. | Avarus nou im- 20plebitur pecunia, et qui amat divicias fructus non capiet ex eis. | Otho nunccius domini pape | ostendit literas domini pape cousilio regui nostn | apud Westmonasteritim, in quibus papa allegavit scandalum Romane ecclesie et obprobrium vetustissimum, notam scilicet cupiditatis que radix esi omnium malorum, iu lioc precipue, quod nullus potest aliquod negocium iu Romaua curia expedire, 3onisi effusa magna summa pecunie et donorum exhibicione. Sed quoniam scandali huius et infamie Romana paupertas est causa, deberent matris in- | Pape postulacio pvo subsidio.
p. 224: opiam sublevare filii naturaJes, quia nisi a vobis et aliis viris honestis dona receperimus, deficerent nobis vite necessaria, quod esset omnino Romane incongruum dignitati. Ad illud ilaque scandalum peuitus eradicandum per cousiiium fratrum no- | strorum saucte Romane ecclesie cardinaJiitm, quandam providimus formam, cui si votueritis consentire, a scandaio niatrem vestram poteritis liberare et iu curia sine \ donorum obscquio exhibicionem | iusticie obtiuere. Forma atttem provisa est liec: | Petimus inprimis ab omnibus ecclesiis cathedraJibus duas uobis prebendas^ exhiberi, unam de porcione episcopi et alteram de capituio, et similiter de cenobiis, ubi diverse sunt porciones abbatis et conventus, a conventibus quantum pertinet ad unumiS monachum cquaJi facta disiribucione bonorum suorum, et tantumdem de abbate. Sed postquam maturatum est consiiium, posuerunt respousum in ore magistri Johannis arcJiidiaconi Bedfordensis, qui, cum dixisset nunccio quod peticio concemit ius | regis, ius dominorum sccuJarium et muJlorum ab- | sencium palronorum, cJerus iile non potuit in eorum | absencia finaliter respondere. Interimque venit dominus JoJiannes MarescaJJus et aJii nunccii regis, districcius inJiibentes quod ncc cierus ncc Otto^ nunccius attemptet aJiquid quod tangit feodum regis ncc moJestet cJerttm AngJie y qui tenet baronias vcl aJias eiemosinas de rege in capite.
p. 225: sanctam sedem. | radix omnium malorum est cupiditas | Habentes igitur alimenta et quibus tegamur hiis contenti simus.
p. 227: vero pape
p. 228: abhominacio desolacionis stans in templo, | Sacrosancta Romana ecclesia non ab apostolis sed ab tpso Domino primatnm obtinnit. | Petrns et Panlns erant | socii in nrbe Romana,
```

---

## Chunk 10-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "228.14–232.13"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 3 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "916 words; 858 unanimous or majority-real; 49 settled by vote (DEL 2, R2 24, R3a 8, R5a 15); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n289–n293 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 3: [TITLE]

## ¶1 · 228.14–230.21

> [p. 228] Sed secundo arguitur quod papa habet potestatem talem a Domino, ut dicit decretum XXII distinccione Sacrosancta, ubi Anacletus papa sic loquitur: Sacrosancta Romana ecclesia non ab apostolis sed ab ipso Domino primatum obtinuit. Ex quo sequitur quod non ab imperatore vel homine sed immediate a Deo papa habet excellentissimam dignitatem. Et idem confirmatur secundo ex submissione regnorum, et tercio ex testimonio doctorum de potestate pape absolvendi a pena et a culpa scribencium. Quantum ad primam partem huius argucie debet supponi quod iste papa intellexit per sacrosanctam Romanem ecclesiam non basilicam vel mixtum putridum, sed sanctos Petrum et Paulum et ceteros qui inhabitaverant illum locum. Ideo in eodem decreto dicit quod Petrus et Paulus erant socii in urbe Romana, unde signanter dicitur quod primatum obtinuit. Debet supponi secundo quod loquitur de primatu hominum quoad Deum, ex primicia virtutum et edificacionis ecclesie et non [p. 229] de primatu diviciarum temporalium vel glorie humane. In hoc enim Scarioth qui possedit agrum de mercede iniquitatis, ut dicit Petrus Act. primo, Petrum excesserat, propter quod sancti et specialiter apostoli timuerunt impetrare sibi redditus de bonis pauperum. Et ex istis patet tercio quam nuda foret argucia: Romana ecclesia non ab apostolis sed ab ipso Domino primatum obtinuit, igitur omnis Romanus pontifex vel alius debet in gloria mundana precellere vel seculariter dominari, quin pocius ex decreto sequitur quod Romanus pontifex tenetur servireilli populo, non sibi dominando vel ipsum suspendendo, sed pro illo efficaciter exorando, ut allegat Paulum fecisse Rom. primo: Licet, inquit, pro omnibus apud Dominum omnium sanctorum effundatur oracio, hiis tamen verbis Paulus beatissimus Romanis proprio cyrographo pollicetur dicens: Testis enim michi est Deus, cui servio in spiritu meo, in evangelio filii eius, quod sine intermissione memoriam vestri facio semper in oracionibus meis. Ex isto decreto videtur quod papa Anacletus noluit asserere quod ipse debuit super omnes alios dominari civiliter vel primatum habere quoad Deum super omnes alias personas ecclesie militantis, quia sic querendo gloriam propriam, ut dicitur Joh. V, haberet signum evidentissimum Antichristi, ymo Bonifacius VIII. in sua extravagante Unam sanctam non audebat expresse illud asserere, quia tam fideles quam infideles pertinenter sibi obicerent: Tu de te ipso testimonium perhibes, testimonium tuum non est verum. Unde in istam perplexitatem ex dotacione et exaltacione cesaris involvuntur Romani pontifices, quod imperatore [p. 230] querente ab eis: si ipsi in potestate, dignitate vel primatu quoad Deum excedunt omnes mortales alios iam viventes, oportet ipsos illud concedere, quia aliter, ut inquiunt, nemo debet credere quod sunt pape, et cum a Deo non habent illam preeminenciam, ut patet ex dictis, nec beatus Petrus illud concederet, patet eis concedendum quod hoc habent a cesare. Nam beatus Paulus Petri socius confessus fuit fideliter prima Cor. XV, 9: Ego, inquit, sum minimus apostolorum, qui non sum dignus vocari apostolus. Quare igitur sic non profiteretur Romanus pontifex, si imperialis dignitas non obstaret? Et sic necessitari videtur ex dotacione tam imperator quam suus episcopus involvi blasfemiam. Et sic verum concluditur quod a Deo immediate et non a natura humana papa habet excellenciam dignitatis, sed oportet quod mereatur illam excellenciam dignitatis humiliter sine pompa. Et revera non est medium merendi ipsam accipere dignitatem talem cesaream.

[ENGLISH]

## ¶2 · 230.22–231.27

> [p. 230] Quantum ad secundum partem argucie, patet quod non est color si regna vel persone submittunt se improvide Antichristo, quod propterea ampliatur in eo potestas vel iurisdiccio; ymo dyabolus negaret istam arguciam, cum filii sui subiecti per peccatum non augent in eo potenciam, eo quod tam ipse quam fidelis concederet quod non capit potestatem suam ab indignissimo servo suo, sed habet ipsam ab inicio a solo Deo. Non igitur ex submissione tali docetur quod papa habet a Deo vel homine preeminenciam aliqualem, sed pocius cum omnis populus vel involuntarie sic sibi subicitur vel non debet sic sibi subici, evidenter sequitur ex tali subieccione blasfema carencia dignitatis. Unde non video quomodo papa posset patencius accusare se ipsum [p. 231] quam respondendo, ut narratur in quodam gesto Anglie, quomodo vacante episcopatu Dunelmie ex quadam subdola subtilitate clerici rex dicitur misisse pape, ut illud beneficium conferat suo clerico: rex autem et regnum ex scitu pape perante decreverant quod non obstante quacumque donacione pape promotus pape non perciperet fructus beneficii regni nostri, nisi regi et regno visus habilis, distribuendo illos fructus provide infra regnum, ipsum regnum velit incolere. Habito itaque longo consilio de literis regis papa fertur taliter respondisse: Et si rex misisset asinum pro illo beneficio, habuisset. Quod responsum manifeste indicat papam, et si prius dignus fuit ex lege privata papali illud officium contulisse, ab illo privilegio excedisse, quia XI questio III ex decreto beati Gregorii sic habetur: Privilegium omnino debet amittere, qui sibi permissa abutitur potestate. Maior autem in isto non posset esse abusio, quam scienter constituere indignum in clericali officio. Ista autem fallacia imaginatur de potestate ecclesiastica quod secularis potest eam dare sicut bovem vel asinum, vel quod ex defectu defensionis partis contrarie preposito spirituali acquiritur, si instituitur in quibusdam tradicionibus humanis. Sed deliramenta sunt ista.

[ENGLISH]

## ¶3 · 231.28–231.31

> [p. 231] Quantum ad tercium partem, patet quod doctoribus istis non debet credi nisi ut testibus vel autoribus in quibus Christus loquitur velut probantibus suam sentenciam racione.

[ENGLISH]

## ¶4 · 232.1–232.3

> [p. 232] Quantum ad testimonium eorum, patet, cum tam potestas quam absolucio sit insensibilis, testimonium tante distancium non est conveniens.

[ENGLISH]

## ¶5 · 232.4–232.13

> [p. 232] Quantum ad secundum membrum, non est signum quod Deus eis revelavit istam sentenciam, cum non patet ex scriptis vel factis apostolorum, et quatuor maiores doctores hoc non recitent. Augustinus autem sepe recitat quomodo non debet credi sibi nisi de quanto se fundaverit ex scriptura. Nec dubito quin nec racio nec autoritas hoc convincit. Ideo ve illis, qui introduxerunt hunc errorem novellum infundabilem in ecclesiam sanctam Dei.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 228.14: The pope said to have his primacy direct from God.
- 228.26: This is true only of a pope who follows Peter and Paul
- 228.33: and of a spiritual primacy.
- 230.4: Perplexity in which the popes are involved by their claims.
- 230.22: The right to rule is not increased because subjects submit rashly.
- 231.1: Scandalous saying of a pope.
- 232.1: The absolving power of the pope cannot be proved.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 228: *obtinuit* [R3]
  - 228: *putridum* [NW]
  - 228: *illum* [R3]
  - 229: *Deus* [R3]
  - 231: *literis* [R3]
  - 231: *beneficio* [NW]
  - 232: *insensibilis* [NW]
  - 228: *Petrus* (W1: Petrns -> Petrus (scans: petrns | petrns | pclrus | petrus)) [OVERRIDE-SCAR]
  - 228: *supponi* (LEFT-odd: supponi + glued line number 25) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 228:
14. Codd. in marg. : Potestatem papa si habeat a domino.
11. Matth. XXIV, i5; Dan. IX, 27. 16. Gap. II.

p. 229:
2. Act. I, 18. 18. Rom. I, 9. 29. Extrav. Gomm. De
Maioritate et Obediencie I, VIII, r.

p. 230:
(none)

p. 231:
2i. Codd. : Istam autem fallaciam. 25. Codd.: si; sed?
2. Walsingsham Ypodigma Neustriae pag. 283. Hist. Anglic.
II, 382. Vid. Loserth, Studien zur Kirchenpolitik Englands im
XIV. Jahrh., Sitzungsberichte der Wiener Akademie CXXXVI, 27.
18. Cap. LXIII.

p. 232:
8. Codd. in marg. : Credere doctoribus quando debemus. iq. Codd.
in marg.: Pape inslitucio a cesare. 3o. Indiam; recte: Judeam.
18. Gap. XIV. Loosely quoted.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 228: abhominacio desolacionis stans in templo, | Sacrosancta Romana ecclesia non ab apostolis sed ab tpso Domino primatnm obtinnit. | Petrns et Panlns erant | socii in nrbe Romana,
p. 229: possedit agrum de mercede iniquitatis, | Testis enim michi est Deus, cui servio in spiritu meo, in evanlogelio filii eiiiSy quod sine iutermissione memoriam vestri facio semper in oracionibus meis. | Unam sanctam | Tu \ de te ipso testimonium perhibes, testimonium tunm non est verum.
p. 230: si ipsi in potestate, dignitate vel primatu quoad Deum excedunt omnes mortales alios iam viventes, | sum minifnus | apostolorum, qui non sum diguus vocari apostolus.
p. 231: Et si rex misisset asintim pro illo beueficio, habuisset. | Privilegium omnino debet amittere, qui sibi permissa abutitur potestate.
p. 232: Constantinus impc- | rator quarto die sni baptismi privilegium Romane | ecclesie pontifici contnlit, 111 in toto orbe pontifices ita hunc caput habeant sicut iudices regem. In quo privilegio ita inter cetera legitur: Tribuimus ei potestatem atque vigorem et honorificenciam imperialem, decernentes ut principatum teneat tam super quatuor sedes: Alexandrinam, Anthiochinam, Jerusolinutanam et Constantinopotitanam; celsior et princeps cunctis sacerdotibus tocius mundi existat.
```

---

## Chunk 10-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-10-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-10-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "232.14–235.34"
divisions: "cap. 10 (heading 'CAPITULUM DECIMUM.' at 222.19); part 4 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "761 words; 698 unanimous or majority-real; 38 settled by vote (DEL 2, R2 20, R3a 8, R5a 7, R6a 1); 25 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n293–n296 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 10, part 4: [TITLE]

## ¶1 · 232.14–235.34

> [p. 232] Patet autem ex predictis quomodo Romanus pontifex fuit consocius aliis pontificibus usque ad dotacionem ecclesie et exhinc ex auctoritate cesaris cepit capitaliter dominari, unde decretum XCVI distinccione quod non possumus pro verecundia negare sic loquitur: Constantinus imperator quarto die sui baptismi privilegium Romane ecclesie pontifici contulit, ut in toto orbe pontifices ita hunc caput habeant sicut iudices regem. In quo privilegio ita inter cetera legitur: Tribuimus ei potestatem atque vigorem et honorificenciam imperialem, decernentes ut principatum teneat tam super quatuor sedes: Alexandrinam, Anthiochinam, Jerusolimitanam et Constantinopolitanam; celsior et princeps cunctis sacerdotibus tocius mundi existat. Et specificat posterius iurisdicionem sui episcopi, specificando patrias, Yndiam, Greciam et cetera secundum quatuor partes mundi. Propter hoc quidam vocant hanc potestatem iurisdicionis indulgencias et alia privilegia paparum cesarea. [p. 233] Et hinc nimirum defidant christiani in Yndia, in Grecia et aliis contratis hoc privilegium, scientes quod non est hominis dare potestatem spiritualem, sed solius Dei, ut dicit Lynconiensis, Epistola XXIII, et sic postponunt indulgencias suas et privilegia, scientes quod secundum dignitatem persone habebit a Deo indulgenciam, nec suum est talem concedere, nisi instrumentaliter in quantum fuerit fidelis Domini promulgator; et aliter illudit populo. Quam sentenciam audivi de papa nostro Urbano VI ipsum dixisse cardinalibus Gregorii qui excessit decalogum ac quia increpans eorum limitavit eos ad vitam apostolicam primevam, conspiraverant contra eum, eligendo sibi Robertum Gilbonensem, virum ut dicitur dissolutum, superbum, bellicosum et legis Christi ignarum. Ideo procul ab Anglicis scola sua, cum Luce XVII, 23 de tali divisione dicit Christus: Nolite abire neque sectemini; nolite abire a religione primeva quam ab apostolis didicistis, neque sectemini talem ducem, cum duceret edos suos in precipicium principis tenebrarum. Sequamur autem Urbanum, de quanto precurrat reccius viam Christi et non ulterius; ymo supposito quod dictus Robertus miraculose sic currat, cum eo debemus humiliter sequi ambos, quia ut recitatur a Gregorio, XXIIª distinccione, De Constantinopolitana sedes vel loca non distrahunt, quin debemus in bono indifferenter imitari meliores; cum, inquit, culpa nou exigit omnes secundum racionem humilitatis equales sumus. Licet igitur multi [p. 234] Romani pontifices sint preeminenter boni, de quibus intelliguntur leges et dicta doctorum, multi tamen ignari vite apostolice mundanum dominium siciebant; hoc autem et consensum eius ac aliorum errorum debemus fugere ut venenum, et specialiter errorem de indulgenciis et de ficta potestate iurisdicionis sive regiminis quam dicunt ex auctoritate imperatoris se extendere per totam habitabilem nostram singulariter quoad Romanum pontificem. ex ista radice fingunt quod solus ipse potest indiffinite concedere indulgenciam et alia spiritualia dona Dei. Et error huiusmodi, ut estimo, est causa, quare nec imperator nec papa sufficit exercere in Yndia, in Grecia, vel Yudea et aliis patriis, dissencientibus quibusdam suis erroribus et quibusdam Antichristi legibus, iurisdicionis officium. Error enim modicus in principio inducit maximum consequenter. Si igitur solus Romanus pontifex habet iurisdicionem universalem super Yndos, Saracenos et Barbaros, quare non exercet eam in eos, sicut apostoli fecerunt in infideles populos et rebelles? Si tantum habet iurisdiccionem super eos qui volunt obedire suo dominio, tunc est papalis iurisdiccio mirabiliter diminuta et dependens a voluntate populi ab eis capitur. Illa autem est alterius racionis quam potestas regiminis apostolica quam imperator non potest concedere, sed divisa per istam divisionem bipapalem variaretur ut populus sibi consenciens, vel diminueretur finaliter ad non quantum; quod superbia non sinit concedere, ideo dicit quod habet potestatem regiminis super totum mundum. Ymo cum illa potestas sit subiective [p. 235] in spiritu, videtur quod manet perpetuo ut caracter; et sic haberemus plurimos papas simul, et sic pape moderni redderent se nimis dampnabiliores ex ocio potestatis; cum enim, ut inquiunt, habent tantam potestatem ut Petrus et Paulus simul, ymo ut Ihesus habebat humanitus, nec potest fingi defectus ex Deo, sed ex eis, quare non fructificant ut ante dotacionem cum huiusmodi potestate? Videtur quod ex potestatis abusu durissimum iudicium ex confessione propria illis fiet. Petrus enim veniet ad iudicium cum suis conversis et quilibet apostolorum cum suis, ut dicit beatus Gregorius super evangelia Omelia XVII, sed talis antichristus veniet cum suis perversis condempnandus. Nec valet antichristiana ficticia qua dicitur papam habere tantam potestatem secundum legem Christi, sicut apostoli ad regulandum populum et insuper habet potestatem ad regulandum populum secundum leges quas ipse condidit et illi regimini propter variacionem temporis oportet attendere, quia nichil patencius indicaret condiciones filii perdicionis, qui secundum Apostolum extollitur super omne quod dicitur Deus, quia certum est quod Christus non potest tales leges condere, sic regere vel taliter dominari. Sacerdotes itaque Christi habent potestatem ante istam iurisdicionem cesaream edificandi populum, ubicumque terrarum quantum sufficiunt, predicando, sancte conversando vel instar sanctorum doctorum scriptis sentenciam catholicam commendando; talem autem potestatem regiminis independentem ab invicem habuerunt apostoli plus et minus, Paulus ut estimo magis Petro.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 232.19: A decretal attributes the pope's primacy to the gift of the Emperor.
- 233.1: Eastern Christians disregard its indulgences and privileges.
- 233.10: The Cardinals revolted from Urban VI, because he tried to keep them to the apostolic life.
- 234.1: Many Roman pontiffs have been worldly.
- 234.11: These false claims cause a - Joss of jurisdiction.
- 235.4: Why do not modern popes exert the power they claim.
- 235.29: Paul had the power of edifying even more than Peter.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 232: *negare* [R3]
  - 232: *quarto* [R4]
  - 232: *ut* [R3]
  - 232: *iudices* [R3]
  - 232: *Anthiochinam* [R5]
  - 232: *Jerusolimitanam* (box on the J; main split the word (i + erusolinutanam, the latter DEL)) [R4]
  - 233: *contratis* [NW]
  - 233: *non* (main split no + u) [R3]
  - 233: *Quam* [R4]
  - 233: *cardinalibus* [R5]
  - 233: *Gregorii* [R4]
  - 233: *primeva* (20 is the line number) [R4]
  - 233: *Constantinopolitana* (hyphenated Constantinopoli-|tana; main token holds De + the whole word, De already stands at the preceding position) [R4]
  - 233: *equales* [R4]
  - 234: *sint* [THIN]
  - 234: *preeminenter* [THIN]
  - 234: *intelliguntur* [R4]
  - 234: *ex* [R3]
  - 234: *ista* [R3]
  - 234: *radice* [R3]
  - 234: *Illa* [R3]
  - 234: *illa* [R3]
  - 235: *quas* (20 is the line number) [R4]
  - 233: *XXIIª distinccione,* (LEFT-nw: two printed words, superscript a after XXII) [OVERRIDE-SCARPLATE]
  - 234: *pontificem.* (LEFT-odd: glued line number 10) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 232:
8. Codd. in marg. : Credere doctoribus quando debemus. iq. Codd.
in marg.: Pape inslitucio a cesare. 3o. Indiam; recte: Judeam.
18. Gap. XIV. Loosely quoted.

p. 233:
8. A in marg. : Nota. 12. decalogwn. Codd. in marg. : Lichy
gedenadc\ty R\iehor\ — falsus Gregorins XI. i3. eorum ; adde: ava-
riciam vel luxuriam. 22. Codd. in marg. : Sequi papam in quo debemus.
23. Codd.: precucurrit.
4. Roberti Grosseteste Epp. ed. Luard pag. 90. 27. Gap. IX.

p. 234:
1. sint; recte: fuerint. 4. Codd.: consensui. 11. Codd. in marg.
Jurisdiccio papa. 3t. vel. Codd.: ut.

p. 235:
i5. Godd. in marg. : Jarisdiccio vel potestas apostolorum.
1 3. Gregor. 1. c. Opp. (ed. Migne) II, 1 148. 23. II. Thess. II, 4.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 232: Constantinus impc- | rator quarto die sni baptismi privilegium Romane | ecclesie pontifici contnlit, 111 in toto orbe pontifices ita hunc caput habeant sicut iudices regem. In quo privilegio ita inter cetera legitur: Tribuimus ei potestatem atque vigorem et honorificenciam imperialem, decernentes ut principatum teneat tam super quatuor sedes: Alexandrinam, Anthiochinam, Jerusolinutanam et Constantinopotitanam; celsior et princeps cunctis sacerdotibus tocius mundi existat.
p. 233: nou est kominis darc potestatem spiritualcm, | sed solius Dei, | Nolite abire neque scctemini; | culpa nou exigit omnes secundum racionem humilitatis equales sumus.
p. 235: cum suis couversis | extollitur super omne quod dicitur Deus,
```
