# Translation brief: potestate-pape 12-s–12-u

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-12-s.md chunks/potestate-pape/wyc-potestate-pape-12-t.md chunks/potestate-pape/wyc-potestate-pape-12-u.md` once and fix what it reports.
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

## Glossary (the 321 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate / suppliant | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. Of one who prays to God himself (*devotus Dei orator*, *Pot. pape* 68.17) "suppliant", with a **C** note; ruled 2026-10-07. |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
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
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
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
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| philargiria | love of money | 1 Tim. 6:10 *radix omnium malorum cupiditas*. Ruled 2026-10-02. |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
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
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| ydiota | unlettered man | Never "idiot". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| forisfactura | forfeiture | Noun beside *forisfacere* "forfeit". Ruled 2026-10-02 (*Eccl.* 15). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| licencia | licence | Permission granted, which Wyclif sets against *potestas*; never "power". Ruled 2026-10-07 (*Pot. pape* 41.21).|
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
| negociatores | dealers | Kept apart from *mercantes* "traders" (*Eccl.*); the servants of the talents parable (Matt. 25). Ruled 2026-10-07 (*Pot. pape* 101.7). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| negociacio | dealing | Pairs with *negociatores* "dealers". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 194.5). |
| Cestrensis | the Chester [chronicler] | Ranulf Higden, *Polychronicon* (S note at first occurrence in a chunk). Ruled 2026-10-08 (coordinator, delegated; conformed in 06-h … 09-b). |
| infundabilis; infundabiliter | without foundation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 195–196). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| provisio (papal) | provision | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* ch. 12). |
| decimacio | tithing | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.26). |
| decimantes | tithe-payers | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.24). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |

---

## Chunk 12-s: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-s.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-s
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "385.32–389.27"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 19 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "866 words; 764 unanimous or majority-real; 80 settled by vote (DEL 1, R2 56, R3a 18, R5a 4, R6a 1); 22 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n446–n450 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 19: [TITLE]

## ¶1 · 385.32–386.26

> [p. 385] Ulterius quantum ad decisiones heresum, pro quibus dicitur esse necessarium esse papam, patet quod a tempore dotacionis cesaree alii fuerant [p. 386] apciores ad discernendum veritatem catholicam quam papa cesareus. Et si dicitur quod auctoritate sui debent vocati decidere, cum solus papa potest synodum congregare, picta et ficta tradicio balbutitur; nam auctoritate illius debet christianus ad edificacionem ecclesie proferre sentenciam a quo capit scienciam; quod est pape impertinens, cum singulariter fit a Deo; debet igitur fieri synodus ex mocione divina consensu unanimi. Ad quem consensum debet papa precipue laborare et in defectu sui alius fidelis ecclesie, ut cesar vel alius magis ydoneus. Unde credo quod facta synodo ad discernendum quid est naturaliter hostia consecrata Robertus et multi prelati cesarei proferrent satis nudam sentenciam nec excederent in diccione procuratoria cesarem vel simplicem ydiotam. Alii autem dicunt quod est quantitas, alii vero quod est qualitas, et tercii quod est panis et sic de aliis variis sentenciis, quas non probant. Ideo sanum videtur fideles se tenere in limitibus quos lex Christi edocet et in aliis curiositatibus non musitare vel plus sapere quam oportet; sufficit enim fides scripture certificare quoad omnia agibilia vel credibilia, que necesse est viantes cognoscere. De toto isto patet diffuse alibi et cetera.

[ENGLISH]

## ¶2 · 386.27–386.35

> [p. 386] Possunt autem abusiones Romani pontificis reduci ad numerum duodecim, ut alie abusiones communiter reducuntur. Prima quod institutis ad hoc cardinalibus dimissis ministeriis que Christus instituit, eligant unum caput, quem ex institucione cesarea papam vocant. Hoc nedum caret auctoritate scripture, sed videtur societati apostolorum et eleccioni Mathie singulariter facte per Dominum repugnare.

[ENGLISH]

## ¶3 · 387.1–387.21

> [p. 387] Secunda quod mundanos honores contra Christum et apostolos tantum affectant. Debet enim recolere, quia ex Matth. XX debet esse omnibus fratribus suis servus, unde Gregorius II. Pastoral. VI: Petrus, inquit, autore Deo sancte ecclesie principatum tenens a bene agente Cornelio, et sese ei humiliter prosternente, inmoderacius venerari recusavit seque illi similem recognovit dicens: Surge, ne feceris, et ego ipse homo sum, sicut et tu. Patet historia Act. X. 26. Et sequitur: Paulus bene agentibus fratribus prelatum se esse nesciebat, cum diceret: Non quia dominamur fidei vestre sed adiutores sumus gaudii vestri. Atque illico adiunxit: In fide enim statis, ac si id quod pretulerat, aperiret dicens: Ideo non dominamur fidei vestre, quia fide statis; equales enim vobis sumus, in quo vos stare cognoscimus; quasi prelatum se esse fratribus nesciebat, cum diceret: Facti sumus sicut parvuli in medio vestrum, prima Tess. II, 7. Et rursum, nos autem servos vestros per Christum. Patet . . . .

[ENGLISH]

## ¶4 · 387.22–388.2

> [p. 387] Tercia est quod papa innitatur seculari dominio. Unde Gregorius ubi supra: Ne presidentis animus ad elacionem potestatis sue delectacione rapiatur. Recte Ecclesiastici XXXII. 1 dicitur: Ducem te posuerunt, noli extolli sed esto in illis quasi unus ex illis. Hinc eciam Petrus ait: Non dominantes in clero sed forma facti gregis. Hinc eciam Veritas per semetipsam dicit: Scitis quia principes gencium dominantur eorum, non sic erit inter vos. [p. 388] Ideo secundum Bernhardum: Nihil intoxicat ani- mum pape plus quam dominandi libido.

[ENGLISH]

## ¶5 · 388.3–388.12

> [p. 388] Quarta quod papa sit dux loquens grandia, magnificando suam potenciam et faciens modicum m effectu. Ex hinc itaque docet beatus Gregorius, ut patet XCIX distinccione: Quod papa non debet vocari universalis episcopus. Hec enim est condicio Antichristi, cum Christus cepit facere et docere, celans suam potenciam, nisi de quanto est necessarium ipsam detegere et credere ad salutem. Mendax autem potestatis ostensio inducit perfidiam Antichristi.

[ENGLISH]

## ¶6 · 388.13–388.30

> [p. 388] Quinta quod papa, dimissa arte paciendi iniurias et facta evangelica inducendi timorem filialem subiectis, innitatur crudeliter pugnis corporalibus et vindictis non solum in causa Christi ad vindicandum suas iniurias, sed precipue in causa propria ad magnificandum suas potencias, et ad hoc allegat Gregorius II Pastor ubi supra, illud Matth. XXIV, 48: Quod si dixerit malus ille servus in corde suo: Moram facit Dominus meus venire, et ceperit percutere conservos suos, Dominus suus inopinate veniet et ponet partem eius cum ypocritis. Inter ypocritas, inquit, iure deputatur qui ex simulacione discipline ministerium regiminis vertit in usum dominacionis. Deficiente enim spirituali armatura et specialiter gladio spiritus, necesse est quod papa cesareus innitatur refrigescentibus armis timorem servilem inducentibus prepostere contra Christum.

[ENGLISH]

## ¶7 · 388.31–389.27

> [p. 388] Sexta quod papa appetat dominari nedum pecunia et prediis sed suis fratribus, non secundum racionem, qua similantur bestiis ad brutalitatem [p. 389] in honorem Domini expurgandam, sed, dimissa illa sollicitudine vicaria pro Christo, nitatur modo Luciferi secundum omnem racionem que sapit excellenciam suam fratribus suis et specialiter in testinacionem veritatis precellentibus dominari. Istam materiam declarat Gregorius II Pastor. VI notans primo quod culpa ex insufficiencia proprii regiminis induxit huiusmodi prelaciam, secundo quod prelatus debet esse humilis socius bonis subditis, et tercio quod regimen suum debet exercere cum debita severitate in feras egentes regimine, ut puta contra eos in quibus Ihesus contempnitur. Et adducit ad hoc illud Genesis XLVI, 34: Pastores ovium sumus. Secundo Genes. IX, 1 dicit Deus terror vester ac tremor sit super cuncta animalia terre; in quo esse super homines prohibetur. In hoc enim, quod metum sibi a perverse viventibus exigunt, quasi non hominibus sed animalibus dominantur. Ex istis elicit sanctus tercio multas demonstrabiles veritates, prima quod contra naturam est et superbia Luciferi velle ab equalibus in natura et moribus dominari, secunda quod curatus ut prosit debet appetere illud officium, non ut presit, et tercia quod nemo assumeret pastoris officium nisi evidenter haberet artem spiritualis medici ad prodessendum anime subditorum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 385.32: Pope's judgment as to heresies valueless.
- 386.27: Twelve abuses of the pope. 1. Method of election.
- 387.1: 2. Claims of honours,
- 387.1: 2. Claims of worldly honours,
- 387.22: 3. and of secular rule.
- 388.3: 4. Much boasting with little performance.
- 388.13: 5. Encouragement to war, especially in support of his own power.
- 388.31: 6. Unauthorized claims to rule.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 386: *congregare* [R3]
  - 386: *quam* [R3]
  - 387: *tu* [R3]
  - 387: *cum* [R3]
  - 387: *equales* [R4]
  - 387: *nesciebat* [R3]
  - 387: *Ne* [R3]
  - 388: *intoxicat* [THIN]
  - 388: *ani-* (hyphenated ani-|mum; main token holds the first half) [THIN]
  - 388: *mum* (second half of ani-|mum) [THIN]
  - 388: *Quinta* [R4]
  - 388: *evangelica* [THIN]
  - 388: *∅* (folio bar after evangelica (257ᶜ in margin) read as i) [THIN]
  - 388: *inducendi* [THIN]
  - 388: *facit* [R3]
  - 388: *meus* [R3]
  - 388: *inopinate* [R4]
  - 388: *vertit* (leaf zoom: both t's of vertit have the crossbar, not l) [R4]
  - 388: *prediis* [R4]
  - 389: *illa* [R3]
  - 389: *testinacionem* (print has testinacionem (after "specialiter in" at line end), kept as printed; 5 is the line number) [NW]
  - 389: *metum* [R3]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Eccl. XXXI. (387.30).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 385:
2. Cod.: Matth. XIX. 9. B: amiciciam. 11. contrakere; Adde:
matrimonia. 32. Codd. in marg. : Hereses decidere ad quem spectat.
De Poteatate Pape. 2:

p. 386:
19. Codd. : de aliis de variis. 27. Codd. in marg. : Abusiones pape.
29. Codd. in rnarg. : i.

p. 387:
1. Codd. in marg. : 2. :. Codd. perperam: II Past. XVII. 6. Codd. :
benedicente. 10. Codd.: Historia. n. Codd.: benedicenlibus.
20. Codd. : vestri. 21. Patet . . . Adde : historia II Cor. IV, 5. 22. Codd.
in marg. : 3. 24. B: rapiatur deest. A in marg. addit. 25. Codd.:
5. Gregorii De Cura Pastorali II, 6. 14. II Cor. I. 23.
23. Gap. VI. 27. I Petri V, 3.

p. 388:
3. Codd.: IV. i3. Codd. in marg. : 5.
l. St. Bernardi De Consideracione III, r. G. Cap. III.
Primae Sedis.

p. 389:
5. testinacionem ; ita codd. 6". Codd.: Cap. XVII. 2H. Codd. in
19. St. Gregorius 1. c.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 385: Quos Deus couiunxit, honw nou separet.
p. 387: autore Deo sancte ecclesie principatum teueus a bene agente Coruelin, et sese ei hnmiliter prosternente, inmoderacius | venerari recusavit seque illi | similem recognovit dicens: Surge, ne feceris, et ego ipse homo sum. losicut et tu. | Paulus bene agentibus fratribus prelatum se esse nesciebat, cuni diceret: Non quia dominamur fidei vestre sed adiutores sumus gaudii vestri. Atque illico adiunxit: In fide euim statis, ac si id quod | pretulerat, aperiret dicens: Ideo non domiuamur jidei vestre. quia fide statis; equales enim vobis sumtis, iu quo vos stare cognoscimus; quasi prelatum se esse fratribus uesciebat, ctim diceret: Facti sumus sicut parvuli in medio vestrum, prima Tess. 20II, 7. | nos autem servos vestros per Christum. | Ae presidentis animus acl elacionem potestatis sue clelectacione rapiatur. | Ducem te posuerunt, noli extolli sed esto in illis quasi unus ex illis. | Xou dominautes in clero sed forma facti gregis. Hinc eciam Yeritas per semetipsam dicit: Scitis quia priucipes gen- Socium dominantur eorum, uou sic erit inter vos. | Eccl. XXXI.
p. 388: Nihil intoxicat ani~ mum pape plus quam dominandi libido. | Quod papa non debet vocari universalis episcopus. | Onod si dixerit malus ille 20 servus in corde sno: Moram facit Dominus meus venire, et ceperit percutere conservos suos, Dominus suus inopinate veniet et ponet partem eius cnm ypocritis. Inter ypocrifas, | iure depufatur, qui ex simulacione discipline ministerium regiminis | verlit in usum dominacionis.
p. 389: Pastores ovium sumus. | terror vester ac tremor sit super cuncta animalia terre; | In hoc enim, quod metum sibi a perverse viventibus exigunt, quasi non hominibus sed animalibus dominantur.
```

---

## Chunk 12-t: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-t.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-t
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "389.28–393.30"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 20 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "897 words; 797 unanimous or majority-real; 67 settled by vote (DEL 2, R2 50, R3a 12, R5a 3); 33 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n450–n454 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 20: [TITLE]

## ¶1 · 389.28–391.10

> [p. 389] Septima quod papa negligat disponere se in mentis mundicia, ut pro subiectis debite interpellet. Hoc enim est inseparabiliter papale officium, cum talis debet tamquam intercessor pacificans inter Deum et populum mediare. Inficitur autem oratoris officium per superbiam, ut patet in sex abusionibus predictis et per avariciam [p. 390] que est alia radix malicie. Sicut enim fistula per quam transiret liquor inficitur per metalli rubiginem inherentem, sic inficitur rectoris fistula ad orandum, quando temporalibus nimis afficitur, cum ad hoc consequitur servitus ydolorum; et sicut liquor non descendit per fistulam ad subiectum, nisi proporcionaliter ad scaturiginem sit depressa, sic sacerdos orando non mediat inter Deum et populum nisi deponendo elacionem de se ipso humiliter senciat, subiciendo se debite quoad Deum. Ideo caveret papa, quomodo de necessitate salutis tenetur orare pro populo, et precipue emundare spirituale organum ab istis duobus criminibus; aliter enim nedum omittendo peccaret, sed mediando inficeret gregem suum, dicente Gregorio primo Pastoralis X: Cuncti, inquit, liquido novimus, quia cum is qui displicet ad intercedendum mittitur, irati animus ad deteriora provocatur. Qui igitur adhuc desideriis terrenis astringitur, caveat ne districti iram iudicis gravius accendens, dum loco delectatur glorie fiat subditis autor ruine. Octava abusio est quod papa oneret se infundabiliter onere alieno. Hic autem exprimit Gregorius primo Pastoralis sub hiis verbis: Hinc precipites colligant cum quanta culpa ex proprio appetitu ceteris preferri non metuunt, si sancti viri plebium ducatum suscipere Deo eciam iubente timuerunt. Moyses suadente Domino trepidat, infirmus quisque, ut honoris onus suscipiat, anhelat; et qui ad casum valde urgetur ex propriis, humerum libenter opprimendus submittit ponderibus alienis; que egit ferre non valet, eciam auget, quod [p. 391] portet. Ex istis videtur quod prelacia ecclesiastica sine peccato saltem veniali non poterit acceptari. Omnes enim quotquot venerunt sunt fures et latrones, qui accipiunt illud propter honorem vel commodum temporale, quod plus prelaciam quesitam sollicitudo et actus eorum diiudicant. Si igitur sine tali obligacione superaddita possumus plus vel tantum prodesse populo, ad quid querimus vincula temporalium et professione superaddita colligari?

[ENGLISH]

## ¶2 · 391.11–391.27

> [p. 391] Et sub ista octava stulticia sunt mille alie germinantes, ut nona abusio est, quod papa presumit per totum christianismum statuere duces spirituales et medicos, pro quorum ducatu oportet ipsum summo iudici respondere. Sic, inquam, non fecerunt Petrus, Gregorius etceteri sancti ecclesie primitive, sed permiserunt aliorum apostolorum instituciones et expertorum elecciones procedere. Nam hoc debet populus plus curare, dicente Gregorio primo Pastoralis IX capitulo: Cum curam populi electus presul suscipit, quasi ad egrum medicus accedit. Unde creditur quod provisiones, reservaciones et privilegiaciones tam amplas induxit non amor salutis subditi vel excellens specularis prudencia sed mater cupiditas; cum ubi lucrum tollitur cessant constituciones huiusmodi, eciam licet magis prodessent ecclesie.

[ENGLISH]

## ¶3 · 391.28–392.7

> [p. 391] Decima abusio est, quod papa presumit ultra Christum vel sanctos apostolos concedere sic cece indulgencias et privilegia, cum ignorat communiter si Deus hec approbat, vel ad utriusque partis deterius reprehendit. Nam vel est indulgencia talis sophistica vel personalis et empta vel dignis quibus proficeret nimis parca. Si igitur [p. 392] servus timeret sibi expendere corporalem thesaurum domini dominorum, et specialiter presumendo blasfeme potestatem et modum proprium regi regum, cum enim talis non humiliter intrat per ostium, sed ascendit superbe dirumpens tectum ecclesie caritatem, et sophisticat thesaurum Domini, restat ut in finali iudicio condempnetur.

[ENGLISH]

## ¶4 · 392.9–392.21

> [p. 392] Undecima abusio est quod papa in preficiendo duces christiani exercitus contra dyabolum, in preiudicium Christi acceptat personas vel respicit suum commodum temporale. Nichil enim convinceret evidencius quod venit proditor Antichristus, cum subdole seducit christianum exercitum per capitaneos subdolos secte sue, ymo cum Christus in paciendo accipit denominaciones membrorum suorum, ut patet Matth. XXV, manifestum est quod falsius, nequius et multiplicius quam Scarioth crudelioribus hostibus legis veteris tradunt Christum, ut tangit Crysostomus Omelia XXVII Operis Imperfecti.

[ENGLISH]

## ¶5 · 392.22–393.30

> [p. 392] Duodecima abusio est quod papa tam in persona sua quam in suis satrapis innititur tam studio quam praxi contrariis legi Christi, cum lex Dei et ars curandi sua postponitur et ars cesarea vel antichristiana inducitur. Et istum abusum Gregorius sepe conquiritur, unde mandat libro II cap. primo: Quod rector sit pre cunctis contemplacione suspensus internorum, curam in exteriorum occupacioue non minuens. Cum enim predicare verbum Dei et curare animas secundum artem Christi sit precipuum pape officium, patet quod ad eum spectat dimissis curis terrenis verbo illi intendere. Et idem credit iste sanctus in monitu legis Dei. [p. 393] Unde libro II cap. XVIII: Dum, inquit, per animarum presulem terreni exercetur officium iudicis, a gregis custodia vacat cura pastoris et subiecti veritatis lumen apprehendere nequeunt, quia dum pastoris sensus terrena iudicia occupant, vento temptacionis impulsus, ecclesie oculos pulvis cecat. Quod cum Christus a ventris voracitate compesceret, adiunxit dicens: Attendite igitur vobis, ne graventur corda vestra in crapula et ebrietate, illico sic adiunxit: Aut in curis huius vite. Ubi pavorem adiciens, ne forte, inquit, superveniat dies illa repentina, cuius qualitatem denuncians: Tamquam laqueus, inquit, veniat super omnes, qui habitant super faciem omnis terre. Hinc iterum dicit: Nemo potest duobus dominis servire; hinc Paulus religiosorum mentes a mundi consorcio conveniendo suspendit dicens: Nemo militans Deo implicat se negociis secularibus, ut ei placet cui se probavit. Hinc ecclesie rectoribus et vacandi studia precipit et consulendi remedia ostendit dicens: Secularia ergo iudicia, si habueritis contemptibiles qui sunt in ecclesia illos constituite ad iudicandum, ut illi videlicet dispensacionibus terrenis inserviant, quos dona spiritualia non exornant, ut quia penetrare intima nequeunt saltem foris necessaria operentur. Hinc Moyses a Getro alienigena iudicatur quod terrenis negociis populorum stulto labore deserviat, cui consilium mox prebetur, ut pro se alios ad iurgia dirimenda constituat, et ipse liberius ad erudiendos populos spiritualia archana cognoscat.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 389.28: 7. Failure to make intercession for his subjects.
- 390.23: 8. Readiness to accept undue burdens for the sake of honour or reward.
- 391.11: g. Claims of patronage.
- 391.28: 10. False grants of indulgence.
- 392.9: 11. Grants of patronage for selfish ends.
- 392.22: 12. Opposition in study and deed to Christ's law.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 389: *interpellet* (hyphenated inter-|pellet (30 line number); main token holds the whole word) [R4]
  - 390: *ruine* [R3]
  - 390: *∅* (to is the English side note (8. Readiness to accept ...)) [R6]
  - 390: *precipites* (print "Hinc 25 / precipites colligant"; the main scan lost precipites) [INS?]
  - 390: *timuerunt* (hyphenated ti-|muerunt; main token holds the whole word) [R3]
  - 391: *curam* [R3]
  - 391: *egrum* [R4]
  - 391: *∅* (25 is the line number) [R4]
  - 391: *approbat* [R3]
  - 391: *proficeret* [R3]
  - 392: *preficiendo* [NW]
  - 392: *∅* (folio bar after teris (258ᶜ in margin) read as i) [INS?]
  - 392: *contemplacione* [R3]
  - 393: *iudicia* [R3]
  - 393: *vento* [R3]
  - 393: *compesceret* [R4]
  - 393: *ebrietate* [R4]
  - 393: *vite* [R3]
  - 393: *illa* [R3]
  - 393: *iudicia* [R3]
  - 393: *in* [R3]
  - 393: *foris* [R3]
  - 393: *stulto* [THIN]
  - 393: *∅* (30 is the line number) [THIN]
  - 393: *erudiendos* [THIN]
  - 393: *populos* [THIN]
  - 393: *archana* [NW]
  - 390: *novimus,* (LEFT-odd: folio bar after comma, not text) [OVERRIDE-SCARPLATE]
  - 390: *hiis* (W2: print = hiis) [OVERRIDE-SCARPLATE]
  - 391: *germinantes,* (LEFT-odd: ink has comma) [OVERRIDE-SCARPLATE]
  - 391: *Gregorio* (LEFT-odd: Gre-|gorio hyphenated, line number 20 glued) [OVERRIDE-SCARPLATE]
  - 393: *Attendite* (W2: italic, print = Attendite) [OVERRIDE-SCARPLATE]
  - 393: *adiunxit:* (LEFT-odd: hyphenated ad-|iunxit:) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 389:
5. testinacionem ; ita codd. 6". Codd.: Cap. XVII. 2H. Codd. in
19. St. Gregorius 1. c.

p. 390:
21. B: gloriose. _3. Codd. in niarg. : S, 33. Codd.: quem
eger ferre.
16. St. Gregorius l. c. 2<S. De Cura Past. I, cap. V, i.

p. 391:
2. Codd.: sine puncto. 12. Codd. in marg. : 9. 28. Codd. in

p. 392:
7. A: itidicio tn marg. addittir. 9. Codd. in marg. : //. 22. Codd.
in marg. : 12. 3o. B: non deest.

p. 393:
i. Est cap. VII sec. partis. 8. Luc. XXI, 34. 10. Luc.
XXI, 34. 14. Luc. XXI, 35. i5. Luc. XVI, i3. 17. I Tim.
II, 4. 20. I Cor. VI, 4, 29. Exod. XVIII, 17, 18.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 389: Pastores ovium sumus. | terror vester ac tremor sit super cuncta animalia terre; | In hoc enim, quod metum sibi a perverse viventibus exigunt, quasi non hominibus sed animalibus dominantur.
p. 390: liquido novimus, \ quia cum is qui displicet ad | interccdendum mittitur, irati animus ad deteriora provocatur. Qui igitur adhuc desideriis terrenis astringitur, caveat ne districti iram iudicis gravius | accendeus, dum loco delectatur glorie fiat subditis autor ruine. | Hiuc 2precipites colligant cum quanta culpa ex proprio appetiiu ceteris preferri non uietuunt. si sancti viri plebium ducaiuni suscipere Deo eciam iubcnte tiniuerunt. Moyses suadente Domino trepidat, infirmus quisque, ut honoris ouus suscipiat, anhelat; | et qui ad casum valde urgetur ex propriis. humerum libenter opprimendus submittit ponderibus alienis; que egit ferre non valet, eciam auget, quod
p. 391: Cum curaui populi electus presul suscipit, quasi acl egruiu medicus accedit.
p. 392: Qtiod rector sit pre cunctis contemplacione suspensus internorum, cnram in exteriorum occupacioue non minuens.
p. 393: per animarum presulem tevveni exercetur officium iudicis, a gregis custodia vacat cura pastoris et subiecti veritatis lumen apprehendere nequeunt, quia dum | pastoris sensus terrena iudicia occupant, vento temptacionis impulsus, ecclesie ocuios pulvis cecat. Ouod cum Christus a ventris voracitate compesceret, adiunxit dicens: Atteudite igituv vobis, ne graveutuv covda vestra in crapula et ebrietate, illico sic ad- \oiunxit: Aut in curis huius vite. Ubi pavorem adiciens, ne forte, inquit, superveniat dies illa repeutina, cuius qualitatem deuuncians: Tamquani laqueus. iuquit, veniat super omnes, qui habitaut super faciem omnis terre. Hinc iterum dicit: Nemo | potest duobus dominis servire; hinc Paulus religiosorum meutes a mundi cousorcio conveniendo suspendit dicens: Nemo militaus Deo implicat se negociis secularibus, ut ei placet cui se probavit. Hinc ecclesie rectoribus et vacandi studia precipit | et consulendi vemedia ostendit \ dicens: Secularia ergo iudicia, si habueritis contemptibiles qui sunt iu ecclesia illos coustituite ad iudicandum, ut illi videlicet dispensacionibus terreuis insevviant, quos dona spiritualia non exovuant, ut } quia penetrare | intima nequeunt saltem fovis necessaria operentur. Hinc Moyses a Getro alienigena iudicatur quod terrenis negociis populorum stuito labore deserviat, cui consilium mox prebeiur, ut pvo se alios ad iurgia dirimenda constituat, et ipse liberius ad | erudiendos populos spiritualia archana cognoscat. A subiectis vero inferioragereuda sunt, arccioribus celestia cogitanda ut scilicet oculum, qui pro videndi gressibus preeminet, cura pulveris uon obscuret.
```

---

## Chunk 12-u: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-u.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-u
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "393.31–397.17"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 21 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "784 words; 737 unanimous or majority-real; 38 settled by vote (DEL 1, R2 17, R3a 15, R5a 5); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n454–n458 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 21: [TITLE]

## ¶1 · 393.31–395.7

> [p. 393] A subiectis vero inferiora gerenda sunt, arccioribus celestia cogitanda ut scilicet oculum, qui pro videndi gressibus preeminet, cura pulveris non obscuret. [p. 394] Caput namque subiectorum et oculi sunt cuncti qui presunt. Et hinc creditur quod dotati sunt exinde more peccancium ad contradictoria obligati. Tenentur enim racione superaccepti doni a mundi principibus amplius servire illis quam prius, et debent minus deservire eis, cum non illuminantur ex accepcione temporalium sed cecantur et per ante tenebantur servire illis secundum totum ingenium vel donum, quod a Deo habebant, quia in toto illo eis proficere quoad Deum, et aliud mundanum ac laycale servicium est abhominabile dominis et sui meriti tardativum. Cum igitur tenentur habere aliquam providenciam et gubernacionem circa bona collata et ingeniacio sua sit tantum finita, videtur quod oportet ipsam quoad servicium meritorium post dotacionem diminui, cum exinde fracta sit et debilitata, quia circa contraria est dispersa. Et hoc creditur movisse apostolos constituisse dyaconos ad ministrandum mensis, apostolis ipsis intendentibus verbo Dei, ut legitur Act. VI. Et revera illud mensarum ministerium videtur habere maiorem racionem meriti quam occupacio qua dotati sunt circa temporalia preter necessaria occupati. Et ex istis videtur quod sicut dotati ad onus dampnosum spiritus receperant coniugium cum temporalibus monstruosum, sic dotantes ex ceca pietate dampnificarunt ambas partes altrinsecus directe ad contrarium meriti, quod stulte intenderant. Unde creditur beatum Gregorium non obstante reliccione tocius patrimonii, quod reliquerat, habens omnia in communi, nec obstante humilitate tota ac parcitate post pinguem dotacionem ecclesie, nec obstante tota suspensione [p. 395] sollicitudinis circa temporalia et inveccione contra philargiam, propter admissionem temporalium venialiter peccavisse et hinc ad purgacionem sui et augmentum meriti Deum ipsum in febribus et dolore capitis per longa tempora punivisse. Alii autem fingunt quod hoc accidit, quia oravit temere pro Trayano.

[ENGLISH]

## ¶2 · 395.8–395.21

> [p. 395] Sed mirantur nonnulli, quare Romana ecclesia non canonizat Constantinum magnum, qui dotavit ecclesiam nec tantum sollempnizat eum, ut orientalis ecclesia, ut notat Cestrensis libro IV, cap. CXII quomodo Greci sollempnizant eius festum XI die. Maii. Sed audivi ad hoc poni causam triplicem, prima fundatur super mendacem blasfemiam, quod debuit dedisse totum imperium suum clero, et quia eius medietatem iniuste detinuit ac in sacrilegio illo sine satisfaccione obiit, tamquam hereticus est dampnandus et per consequens a sanctorum cathalogo semovendus, et sic forent dampnandi omnes morientes reges vel domini temporales.

[ENGLISH]

## ¶3 · 395.22–395.28

> [p. 395] Secunda causa videtur coloracior quod canonizacio videtur fuisse alieno Cesari nimium sumptuosa, ideo ut papa habeat cesares magis subiectos suo imperio noluit tantum colere servum suum, fecit tamen magis mirabilia in vita sua, quam illi reges fecerant in morte quos ex nuda relacione vel gracia pecunie canonizat.

[ENGLISH]

## ¶4 · 395.29–397.16

> [p. 395] Tercia causa realis ponitur quod hoc ideo non evenit, quod tantum onerando ecclesiam cum temporalibus stulte, tantum dampnificaverat se et clerum, quod dispendium quia subtraxit ab [p. 396] orientali ecclesia, propterea ipsum laudat. Ipsi enim ut fratres de statu exproprietario cum iubilo Deum laudant. Nec est color, si talis dominacio vel mundi gloria videatur preciosa febricitanti in animo cuius affeccio discrasiata non sapit celestia, propterea sic est de illo et eius opposito senciendum, quia oportet fidelem credere in omnibus sano palato et iudicio Ihesu nostri. Nec cecemur in isto, quod dominari sic seculariter sit licitum ac meritorium, ideo congruit clero nostro, quia sic purgare latrinas foret eis conveniens. Sed (si non fallor) facere illud officium foret clero minus inconsonum, quam sic dominari terrestribus, que Apostolus vocat stercora, cum nec foret Deo tantum displicens nec adeo ledens mentem. Ista pauca dixerim, alia recitative, alia reputative, assertive ad honorem matris ecclesie; unde super omnibus dictis meis in ista materia testem consciencie mee invoco Deum meum, quod intendo primo honorem et utilitatem sancte matris ecclesie: ad hoc enim obligatur strictissime ex mandato Domini quilibet christianus, cum quoddammodo infinite plus debemus matrem illam diligere quam parentes carnales vel temporalia aut nosmet ipsos. Intendo secundo quod honor et profectus predicte femine stat principaliter in similitudine conversandi et sequendi sponsum ecclesie, excuciendo omnes tradiciones humanas extraneas que ab expedicione illius itineris retardarent. Et cum ista ambo sint articuli fidei christiane, que cuncti fideles ultra opinionem magnificare tenentur ac cum in mediis ad hunc finem contingit [p. 397] multipliciter oberrare, intendo tercio et protestor quod docto per papam, per quodcumque membrum ecclesie vel aliquam creaturam quod erro in mediis, volo humillime ac paratissime revocare; unde ut procedam securius innitor fundamentaliter summo lapidi, qui est via, veritas et vita, domino Ihesu Christo, capiens testimonium a sanctis doctoribus, de quanto consonant legi sue. Alia vero ab istis tamquam tardativa vel contraria parvipendo; unde credo ut fidem ecclesie, quod quicumque non observat statum et legem quam Christus instituit, quam eciam in se et suis apostolis vita et verbo docuit et servavit, non sequitur Christum per artam viam, que ducit ad celum, sed incedit per latam viam, que ducit membrum dyaboli ad infernum.

[ENGLISH]

## ¶5 · 397.17–397.17

> [p. 397] Explicit tractatus de potestate pape Johannis W.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 394.2: False position of the endowed; they owe more service for gifts which make them less capable of service.
- 394.30: St. Gregory's gift of all his patrimony involved venial sin.
- 395.8: Why Constantine is not
- 395.10: canonized as in the Eastern Church.
- 395.29: Because he burdened the church with endowments
- 396.1: which he took from the Eastern Church.
- 396.16: Wyclif's protest of intention to honour and serve the Church;
- 396.27: which is most honoured and advanced by following the Bridegroom.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 393: *non* [THIN]
  - 394: *presunt* (print "qui presunt."; the main scan also lost qui (no row queued for it)) [THIN]
  - 394: *onus* (25 is the line number) [R4]
  - 394: *patrimonii* [R4]
  - 395: *dampnificaverat* [R5]
  - 396: *opposito* [R3]
  - 396: *∅* (s of the English side note (Wyclif's protest ...)) [R4]
  - 396: *intendo* (print "quod intendo" ends the line above primo; the main scan lost intendo) [INS?]
  - 396: *gloria* (LEFT-odd: print = gloria; box on vel) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 393:
i. Est cap. VII sec. partis. 8. Luc. XXI, 34. 10. Luc.
XXI, 34. 14. Luc. XXI, 35. i5. Luc. XVI, i3. 17. I Tim.
II, 4. 20. I Cor. VI, 4, 29. Exod. XVIII, 17, 18.

p. 394:
3o. Codd. in marg. : Dotacionem sanctus Gregortus admittens non
excusatur quin peccat venialiter. i. Codd.: patrimonium.

p. 395:
i3. Codd. in marg.: Lonstantinum magnum dotatorem quare non ca-
noni\at ecclesia. 17. A: sacrilepo.
G. Cf. De eccl, p. p3i— 534. 11. Cf. Ranulplii Polychr,

p. 396:
19, 20. C. (Cod. XI, E. 3): quia intendo primum. 23. C: injinito.
24. C: camalia. 32. Codd.: ac tamcn.
i5. Cf. Wytlifs Protestationes (e cod. univ. Pragensis XI E 3)
impressae per Condentinum Hofler, Anna von T.uxemburg. Dcnk-
schriften der Wiener Akademie XX, 147.

p. 397:
i. A in marg. : Nota. Protestatw. 9. C: retardancia. 12. C: in
suis. i3. C: vite et racio. 17. B: Wyk. A fol. 262, col. 2 : Scriptoris
cuncti memores sint ista legentes atque precentur ei requiem iubilei.
Neb gest toho dobrze hoden (— isto namque dignissimus estj.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 393: per animarum presulem tevveni exercetur officium iudicis, a gregis custodia vacat cura pastoris et subiecti veritatis lumen apprehendere nequeunt, quia dum | pastoris sensus terrena iudicia occupant, vento temptacionis impulsus, ecclesie ocuios pulvis cecat. Ouod cum Christus a ventris voracitate compesceret, adiunxit dicens: Atteudite igituv vobis, ne graveutuv covda vestra in crapula et ebrietate, illico sic ad- \oiunxit: Aut in curis huius vite. Ubi pavorem adiciens, ne forte, inquit, superveniat dies illa repeutina, cuius qualitatem deuuncians: Tamquani laqueus. iuquit, veniat super omnes, qui habitaut super faciem omnis terre. Hinc iterum dicit: Nemo | potest duobus dominis servire; hinc Paulus religiosorum meutes a mundi cousorcio conveniendo suspendit dicens: Nemo militaus Deo implicat se negociis secularibus, ut ei placet cui se probavit. Hinc ecclesie rectoribus et vacandi studia precipit | et consulendi vemedia ostendit \ dicens: Secularia ergo iudicia, si habueritis contemptibiles qui sunt iu ecclesia illos coustituite ad iudicandum, ut illi videlicet dispensacionibus terreuis insevviant, quos dona spiritualia non exovuant, ut } quia penetrare | intima nequeunt saltem fovis necessaria operentur. Hinc Moyses a Getro alienigena iudicatur quod terrenis negociis populorum stuito labore deserviat, cui consilium mox prebeiur, ut pvo se alios ad iurgia dirimenda constituat, et ipse liberius ad | erudiendos populos spiritualia archana cognoscat. A subiectis vero inferioragereuda sunt, arccioribus celestia cogitanda ut scilicet oculum, qui pro videndi gressibus preeminet, cura pulveris uon obscuret.
p. 394: Caput namque subiectorum et oculi sunt cuncti
```
