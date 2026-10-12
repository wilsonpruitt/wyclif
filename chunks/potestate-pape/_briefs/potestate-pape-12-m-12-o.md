# Translation brief: potestate-pape 12-m–12-o

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-12-m.md chunks/potestate-pape/wyc-potestate-pape-12-n.md chunks/potestate-pape/wyc-potestate-pape-12-o.md` once and fix what it reports.
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

## Glossary (the 362 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |

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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
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
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| sciolus | knowing, wise | "smatterer" (the classical sense). Neutral in Wyclif. Pilot (*Eccl.* 5.8) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
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
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| perplexitas | perplexity | The noun beside *perplexus* "perplexed". Ruled 2026-10-02 (*Eccl.* 19, 470.3). |
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
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| laxare | loose | Kept apart from *relaxare* "relax". Ruled 2026-10-02 (*Eccl.* 23, 571.29). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
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
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| criminosus | criminous man | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| deliramenta | ravings | Ruled 2026-10-07 (*Pot. pape* 06-c). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| sessiva | seisin | So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| allocari (in an account) | be allowed | Accounting sense. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 193.18). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| penalis | hard, of hardship | Beside *penalitas*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 280.20). |
| pastor cesareus | caesarean shepherd | The *papa cesareus* family. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 290.24). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| inhabilitas | lack of qualification | Beside *inhabilis* "unqualified". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 316.9). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| pseudopontifices | false pontiffs | Cf. *pseudoclerici*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 335.1). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| civilitas cesarea | caesarean civil standing | After *civilitas* "civil standing" and *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.31). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |

---

## Chunk 12-m: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-m.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-m
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "360.19–364.33"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 13 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "994 words; 914 unanimous or majority-real; 54 settled by vote (R2 40, R3a 9, R5a 4, R6a 1); 26 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n421–n425 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 13: [TITLE]

## ¶1 · 360.19–361.11

> [p. 360] Non igitur sequitur: Multum malum exinde contingeret, igitur non hoc, sed eius contrarium est tenendum. Sic enim de strueretur maior pars legum et sermonum Christi et facienda forent mala ut bona eveniant. Propter talia igitur inconveniencia expedit, quod fidelis teneat se in limitibus legis Christi, videlicet non exigendo plus vel attencius de temporalibus quam hec docet. Quantum vero ad gravandos videtur quod a summo pontifice usque ad minimum sacerdotem omnes peccant in recipiendo bona pauperum et ecclesiasticas dignitates, nam quilibet papa in quantum talis tenetur esse sanctissimus viatorum, et sub illo colore accipitillud nomen; quod videtur [p. 361] esse nimis magna presumpcio. Nam iuxta decretum beati Jeronymi recitatum X capitulo et testimonium Bernhardi et Lyncolniensis papa debet esse qualis ibi reputative describitur; sed tunc foret sanctissimus viatorum, igitur ad hoc tenetur; non enim est evidens quod tam sancti et scioli doctores oleo adulacionis linirent pontificem menciendo de illo, pronunciantes de ipso laudes que nec insunt nec inesse debeant. Ideo planum est ex eorum sentencia quod papa debet esse sanctissimus et per idem quilibet papa.

[ENGLISH]

## ¶2 · 361.12–361.23

> [p. 361] Item, beatus Gregorius libro II De Cura Pastorali cap. primo dicit quod pastor ecclesie debet se habere ad subditos sicut pastor bestiarum se habet ad bestias quas custodit. Sed constat quodnulla earum equiparatur pastori in prudencia vel virtute, igitur pastor ecclesie debet in virtute omnes subditos suos excellere, quia alia excellencia non est pertinens. Cum igitur papa sit pastor tocius residue universitatis fidelium, videtur quod debet supponi ipsum in prudencia et virtute cunctos illos excellere. Aliter enim eque maneret et pasceret eum subditus ut econtra.

[ENGLISH]

## ¶3 · 361.24–362.5

> [p. 361] Item, papa consentit multipliciter, quod vocetur pater beatissimus et vendicat honores ultra omnes mortales alios; cum igitur supponi debet quod hec facit religiose et debite, vel quod sit apostata Antichristus, videtur quod approbantes hec facta papalia, tenentur in istis supponere veritatem et laudis talis materiam. Si igitur veritas est quod ipse est hic pater beatissimus, tunc est viator sanctissimus; et idem sequitur si sitmaxime honorandus, cum honor sit ex quo premium virtutis, [p. 362] ut dicunt philosophi et beatus Jacobus II cap. Et patet ex hoc principio quod Deus honorat hominem proporcionaliter ad virtutem; videtur igitur quod papa, cum dicit se digne consentire antecedenti consentire debeat consequenti.

[ENGLISH]

## ¶4 · 362.7–363.13

> [p. 362] Item, papa (ut ipse et sui fautores asserunt) gerit singulariter vicanam vicem Christi m terris, sic quod ipse infinitum excedit alios quoscumque episcopos, sicut Christus infinitum excessit apostolos, ut patet de indulgenciis et equiparanciis quotquot aliis episcopis et sibi in excellencia; sed totum illud foret mendacium, nisi eos proporcionaliter excederet in virtute, igitur hoc debet supponi. Non enim debet supponi quod papa propter fastum et questum seculi mendaciter debeat ad talia aspirare. Ideo dicit Gregorius ubi supra: Oportet namque ut pastor metiri sollicite studeat, quanta tenende rectitudinis necessitate constringitur, sub cuius estimacione populus grex vocatur; igitur necesse est ut sit cogitacione mundus, accione precipuus, pre cunctis contemplacione suspensus. Item, ad esse veri pape requiritur originalis Dei eleccio, sed Deus non eligit ad papale officium nisi dignum et virtute cunctos ceteros preeminentem, igitur aliter non est papa. Maior ex fide sepe dicta supponitur; oportet enim Deum concurrere cum quolibet agente creato et omne opus creature legitimum primitus approbare; cum igitur secundum humanitatem non eligit regulariter papas, patet quod oportet eum secundum divinitatem eleccione eterna eligere [p. 363] quemlibet verum papam. Minor autem patet ex hoc, quod pastor (in quantum huiusmodi) debet esse medium inter Deum et populum et per consequens in virtute Deo propinquior, ut diffuse declarat beatus Gregorius ubi supra. Et patet ex hoc quod distribuere beneficia, decidere causas civiles et cetera, que non sunt preeminencie virtutum officia, sunt abiectum officium laycale, ideo iuxta beatum Gregorium ad papam non pertinent. Deus igitur eligit eum in papam qui ad iuvandum populum preeminet potestate, et aliter in isto deficiens est Antichristus et pseudopapa, ex ficcione mendacii et fraudacione officii.

[ENGLISH]

## ¶5 · 363.14–364.33

> [p. 363] Ex istis videtur quod nemo sumeret sibi honorem papalem, ut dicit Apostolus, nisi a Deo revelacione abscondita sit vocatus; nam debet cognoscere quod nisi virtute preemineat est contrarius veritati. Sed quis scit hoc? Cum igitur gracia fastus vel questus accipiens dignitatem huiusmodi se ipsum excommunicat in principio, patet quam magnum periculum est in presumpcione talis officii. Ideo dicit Gregorius primo Pastoralium IX: Cum curam populi electus presul suscipit, quasi ad egrum medicus accedit. Si igitur adhuc in eius corpore passiones vivunt qua presumpcione percusso mederi properat, qui in facie vulnus portat. Et infra XI: Sollerter se quisque meciatur, ne locum regiminis assumere audeat, si adhuc in se vicium dampnabiliter regnat. Et hinc superna voce Levit. XXI. 17 ad Moysen dicitur, homo de semine tuo per familias qui habuerit maculam non offerat panes Deo suo nec accedat ad ministerium eius. Et forte si prelati forent a Deo examinati radicitus, cognosceretur quod ex [p. 364] perversa affeccione pocius preessendi quam promerendi suscipiunt illud onus. Quod evidenter convincitur ex hoc quod amplectentes temporalia dimittunt officium promerendi, quod oportet laycos si volunt memores esse salutis proprie iudicare. Et sic videtur melius fore ecclesie quod non foret prelatus cesareus. Sic enim Petrus et ceteri apostoli instar Christi preeminenciam illam aufugerant et ministerialiter propter meritum apud Deum absconditum subesse elegerant. Unde Gregorius primo Pastoralium III: Hec breviter diximus, ut quantum sit pondus regiminis monstraremus, ne temerare sacra regimina quisquis impar his est audeat et per concupiscenciam culminis ducatum suscipiat perdicionis. Hinc etenim Jacobus pie prohibet dicens: Nolite plures magistri fieri, fratres mei. Hinc mediator Dei et hominum percipere regnum vitavit in terris, qui supernorum spirituum scienciam sensumque transcendens ante secula regnat in celis, Scriptum quippe est, Ihesus cum cognovisset, quia venturi essent ut raperent et facerent eum regem, fugit in montem. Quis enim principari hominibus tam sine culpa potuisset quam is, qui inculpate regeret illos quos creavit? Sed quia idcirco in carne venerat, ut non solum nos per passionem redimeret, verum eciam per conversacionem doceret, exemplum se sequentibus prebens rex fieri noluit, ad crucis vero patibulum sponte convenit, oblatam gloriam culminis fugit, penam probrose mortis expeciit, ut membra eius discerent favores mundi fugere, terrores hominum non timere, pro veritate adversa diligere timendo prospera declinare.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 360.28: The pope is bound to be the holiest of men,
- 361.1: if not, he should not take the name of pope.
- 361.24: So too of the honours that he claims,
- 362.7: and of the powers that he is supposed to wield.
- 362.24: To be a true pope he must be chosen by God.
- 363.14: Hence none should take papal honours who does not know himself called of God; but none can know this.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 360: *a* (the main token read the English side note "of"; the printed a (end of the line above, "videtur quod a") has no other slot) [R4]
  - 360: *pontifice* [R4]
  - 361: *magna* [THIN]
  - 361: *testimonium Bernhardi* (one main token covers two printed words) [THIN]
  - 361: *et Lyncolniensis* (one main token covers two printed words) [THIN]
  - 361: *pater* (25 is the line number) [R4]
  - 361: *beatissimus* [R4]
  - 361: *veritatem* (hyphenated veri-|tatem (30 line number); main token holds the whole word) [R4]
  - 362: *antecedenti* [R3]
  - 362: *gerit* [R3]
  - 362: *terris* [NW]
  - 362: *namque* [R3]
  - 362: *vocatur* [R3]
  - 362: *est ut* (one main token covers two printed words) [R5]
  - 362: *suspensus* (hyphenated su-|spensus; main token holds the whole word) [THIN]
  - 362: *∅* (true is the English side note (To be a true pope ...)) [THIN]
  - 362: *Item* [THIN]
  - 362: *Dei* (the main token read the English side note "by"; this slot is the only one for the printed Dei) [R4]
  - 362: *∅* (folio bar after fide (251ᵇ in margin) read as i) [INS?]
  - 363: *huiusmodi* (20 is the line number) [R4]
  - 363: *portat* [R3]
  - 364: *carne* [R3]
  - 364: *membra* (mem | bra split by folio bar (251ᵈ in margin); main token holds the whole word) [THIN]
  - 364: *eius* [THIN]
  - 364: *diligere* [THIN]
  - 362: *Oportet* (W1: Oporfet -> Oportet (scans: oporfet | oporiet | oportet | oporfet)) [OVERRIDE-SCAR]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Correxi. (364.33).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 360:
3. Codd. in marg. : Vivere de quo posset sacerdos, si decime non
essent. 10. A: instrumentali ; B: in sacramentali. 24. B: se deest.
25. B: non deest. 3i. Codd. in marg. : Sanctissimus viatorum debet

p. 361:
20. B: pastor deest.
12. Greg. 1. c. 24. Cf. Hussii Opp. I, 229 a,

p. 362:
ii. B: et deest. Hic locus corruptus est. 17. Codd. in marg. :
Pastor qnalis esse debeat per totum hic.
18. Cap. I.

p. 363:
23. Rectius: Cum causam. 34. Codd.: ex deest.

p. 364:
i3. Codd.: ne intrare. i3, 14. Cod. : quisquis est is nuper audeat.
11. 1. c. i5. Jac. III, 1. 20. Joh. VI, i5.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 360: Sanctissimus viatorum debet papa esse.
p. 361: ibpater ueatissimns
p. 362: Oporfet namque ut pastor metiri sollicite studeat, quanta tenende rectitudinis necessitate coustringitur, sub cuius estimacione populus grex vocatur; igitur necesse estut sit cogitacione mundus, accione precipuus, pre cunctis contemplacione suspensus.
p. 363: Cum curam populi electus presul suscipit, quasi ad egrum medicus accedit. Si igitur | adhuc in eius corpore passioues vivunt qua presumpcione percusso mederi properat, qui in facie vulnus portat. | Solierter se quisque meciatur, ne locum regiminis assumere audeat, si adhuc in se vicium dampnabiliter regnat. Et hinc losuperna voce Levit. XXI. 17 ad Moysen dicihir, Jiomo de semine tuo per familias qui habuerit | maculam non offerat panes Deo \ suo nec accedat ad ministerium eius.
p. 364: Hec breviter diximuSj ut quantum sit pondus regiminis monstraremus y ne temerare sacra regimina quisquis impar his est audeat et per concupiscenciam culminis ducatum suscipiat perdicionis. Hinc etenim | Jacobus pie prohibet dicens: Nolite plures magistri fierij fratres mei. Hinc mediator Dei et hominum percipere regnuni vitavit in terris, qui supernorum spirituum scienciam sensumque transcendens ante secula regnat in cetis. Scriptum quippe est, Ihesus | cum cognovisset, quia venturi essent ut raperent et facerent eum regem, fugit in montem. Quis enim principari hominibus tam sine culpa potuisset quam is, qui inculpate regeret illos quos creavit? Sed quia idcirco in carne venerat, ut non solum | nos per passionem redimeret, verum eciam per conversacionem doceret, exemplum se sequentibus prebens rex fieri noluit, ad crucis vero patibulum sponte couvenit, oblatam gloriam cutminis fugit, penam probrose mortis expeciit, ut mem\bra eins | discerent favores mundi fugere, terrores hominum non timere, pro veritate adversa diligerej timendo prospera declinare.
```

---

## Chunk 12-n: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-n.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-n
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "365.1–368.34"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 14 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "876 words; 837 unanimous or majority-real; 22 settled by vote (INS 1, R2 11, R3a 6, R5a 4); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n426–n429 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 14: [TITLE]

## ¶1 · 365.1–367.3

> [p. 365] Hic possumus palpare si plus diligimus Christum sequendo eius vestigia, quam sacerdotes cesareos propter mundum. Et hec racio (ut credo) movit Augustinum epistola ad Cirillum, quando dixit, postquam allocutus est beatum Jeronymum iam mortuum: Testor Deum, quod a tempore illo pocius desideravi subesse quam preesse. Nam iuxta legem et diffinicionem Christi Matth. XX: Maior, superior vel prelatus ecclesie, debet subesse ministerio suis subditis, que servitus dum defuerit prelato cesareo non est papa, non enim habet cesar vel Deus potestatem sic mutandi officia prelatorum ecclesie, stante vero nomine eorum quod Christus instituit; Deus enim non potest in contradiccionem, cum tunc foret contrarius sibi ipsi. Ideo licet cesar ordinet, quod regulariter episcopus suus presit aliis episcopis, recipiendo a toto populo honores mundanos, et totus populus subsit generaliter suo decreto, non propterea sequitur quod sit papa; hoc enim potest competere layco ut cesari vel alii abiecto membro dyaboli. Racio igitur papatus consistit in humiliori officio ministrandi, sicut stetit in beato Petro et ceteris, quod solius Dei est creature concedere. Et patet, quod magis periculosa mutacio regis superbie stat in hoc quod excecat homines, mutando sacerdotes ad contrarium officii quod Christus eis instituit. Equivocato enim officio necesse est ut producant ecclesiam et fructus equivocatos. Et patet generaliter de omni curato sive presbitero quod a signo valde probabili indigne appetit pastoris officium, quando tam [p. 366] remote, tam sumptuose et periculose laborat ad primatum ecclesiasticum obtinendum, quia si pure vel principaliter intendit edificacion em ecclesie, plana est via, brevior, securior et Deo placencior, laborando indiffinite sicut fecerunt apostoli. Quod si primatum pure aut primo intendit, inhabilitat se ad omnem statum ecclesie, cum preponit regem superbie regi vero; et sic videtur quod ecclesia regulanda ut olim eligeret sibi presbiterum vel quod apostoli infidelis gentis constituant sibi presbiteros, quos percepto veneno dyaboli abicere, Et, patet quam extraneum est a Romano pontifice symoniace principatus ecclesiis assignare; hoc enim foret minus dissonum in milite vel alio populari; ex quibus convincitur quod papa tam perplexe se onerans in tam alieno officio atque ambiguo, propter reputatum commodum temporale nimis gravat suum officium, cum fatue reddit se participem criminis hominum, quos sic prefert Sic eciam dicitur ampliare potestatem eorum quam Deus minuit vel non causat, et restringere potestatem eorum, quam Deus amplificat. Quomodo igitur respondebit Deo stultus tam precipitanter et blasfeme sibi contrarius; non enim est fundabile quod habet potestatem in episcopis. ipsis sciencioribus et: copiosius claves? ecclesie habentibus potestatem ordinis sic restringere vel laxare. Nam de potestate propria hoc non potest, quos igitur funes habet circa potestatem alienam maiorem sua potestate, quam Deus dat appropiate ad prodessendum ecclesie? Non igitur valet fingere blasfemiam ad magnificandum suam potenciam, sed necesse habet stabilire ecclesiam in statu et religione primeva, quam Christus instituit, [p. 367] non excedendo limites in sacramentis et sacramentalibus evangelicis, quia tunc est indubie Antichristus.

[ENGLISH]

## ¶2 · 367.4–367.13

> [p. 367] Sed obicitur per hoc quod, si papa debet esse sanctissimus viatorum et aliter non est papa, sequitur quod omne peccatum mortale vel veniale debet degradare papam, quod est contra legem distinccione XL: Si papa, in qua dicitur quod solum debet deponi pro heresi. Et iterum videtur idem de regibus, episcopis et quibuscumque ministris ecclesie, ymo summus sacerdos in lege veteri non fuit regulariter sanctissimus, cum sepe fuit pollutus.

[ENGLISH]

## ¶3 · 367.14–368.10

> [p. 367] Hic dicitur quod maior pars huius difficultatis stat in signacione termini magistralis, ut aliqui intelligunt papam, ut dicit autonomastice super quoscumque alios mirabilem sanctitatem, sicut Christus se habuit ad suos apostolos. Et sic intelligunt homines de Romano pontifice in hiis que lucrum et honorem mundanam sapiunt, sed non in vita secundum forum consciencie quoad Deum. Et isto modo loquuntur tres sancti doctores predicti. Alii autem intelligunt papam, ut dicit episcopum supereminentem in aliqua sanctitate, ut Ambrosius, Augustinus et ceteri vocati sunt pape. Sed postquam declinavit clerus ad civilitatem, vocati sunt quicumque pape, qui ad decidendum principaliter causas ecclesie seculares sunt humanitus instituti. Et super ista equivocacione currunt raciones, nam Christus fuit papa, quem degradaret quodcumque peccatum, ideo stultum foret christianum ea intencione assumere [p. 368] nomen pape. Ideo caverunt de hoc Petrus, Gregorius et alii sancti, ignorantes si sunt membra dyaboli. In medio vero acceperant sibi sancti episcopi nomen pape, et in tercio propter blasfemum fastum et questum assumpserunt sibi confuse illud nomen prelati cesarei ultra auctoritatem novi vel veteris testamenti. Unde secus est de nomine pape et aliis nominibus primo officiorum, cum papa dicit principaliter preeminenciam sanctitatis. Et patet ex equivocacione solucio.

[ENGLISH]

## ¶4 · 368.11–368.14

> [p. 368] Secundo obicitur per hoc, quod iuxta hanc viam quilibet debet esse papa, ut debet esse sanctissimus viatorum. Debet enim esse papa et quocumque iam viante sanctior.

[ENGLISH]

## ¶5 · 368.15–368.34

> [p. 368] Hic dicitur quod logica secundum sensum compositum et divisum in ista materia est cavenda. Non enim est aliqua sanctitas qua prepolleret peccator, quin debet esse sanctior, quia aliter non peccaret. Verumtamen nec in statu vie nec statu lapsus debet homo composite esse sanctissimus viatorum, quia subducto omni peccato foret gradus excessuum sanctitatum. Sed post lapsum non est alius sanctus vivens vitam communem quin debet esse sancior. Sed ut credo quilibet predestinatus debet finire in gradu sanctitatis non summo sed sibi debito. Unde luciferina presumpcio videtur quod christianus accipiat sibi nomen talis preeminencie sanctitatis. Ideo sancti concorditer illud respuerant. Quid igitur moveret Romanum episcopum ultra obligacionem apud Deum absconditam ex professione humana spontanea sibi assumere tale nomen; professio namque et officium mutantur ab officio et more apostolico ad legem et officium Antichristi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 365.7: The true papacy consists In service.
- 365.25: Ambition of office shews that a man has been blinded by Satan.
- 366.13: The pope should not appoint prelates.
- 367.4: Objection: The pope would be subject to deprivation for every sin.
- 367.14: In this matter much depends on the meaning of Pope;
- 367.21: whether it connotes holiness or worldly supremacy.
- 368.11: Objection: Every one ought to be pope, since every one ought to attain the highest holiness.
- 368.20: Even among the saints there are degrees of holiness,
- 368.27: and it is devilish presumption to claim the highest.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 365: *si plus* (one main token covers two printed words) [THIN]
  - 365: *prelato* [R3]
  - 365: *∅* (folio bar after sive (252ᵃ in margin) read as i) [INS?]
  - 366: *remote* (faded leaf; print "remote,") [THIN]
  - 366: *Et* (main lost the line "Et patet quam extraneum est a Romano ponti-" and kept only "fice"; this slot takes the line's first word, the rest (with pontifice whole) is the GAP row at pos 75) [R3]
  - 366: *patet quam extraneum est a Romano pontifice* (print line "Et patet quam extraneum est a Romano ponti-|fice,"; Et given at pos 74, ponti-fice joined) [GAP]
  - 366: *propter reputatum commodum temporale* (print "ambiguo, propter reputatum commodum tempo-|rale nimis"; ambiguo already at pos 103) [GAP]
  - 366: *ipsis* (main splits ipsis into ir + sis on the faded leaf; whole word given here, next token ∅) [THIN]
  - 366: *∅* (rest of ipsis, given whole at pos 157) [THIN]
  - 366: *sciencioribus* (main splits it into 5circirir + r; whole word given here, next token ∅) [THIN]
  - 366: *∅* (rest of sciencioribus, given whole at pos 159) [THIN]
  - 366: *et* [THIN]
  - 366: *copiosius* [THIN]
  - 366: *claves* [THIN]
  - 366: *ecclesie* [THIN]
  - 368: *testamenti* [R4]
  - 368: *preeminencie* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 365:
4 Codd.: Augustinus. 8. B in marg. : Prelatus vere non est dum
viciose deficit a ministerio.
4. Videtur esse Ep. CXXXIV ad Apringium, ubi leges: Cuius
utilitatibus servio, cui non tam praeesse quam prodesse desidero.

p. 366:
(none)

p. 367:
8. B in marg. : Papa st debel esse sanctissimus solum sequitur incon-
veniens. i5. magislralis ; A: ingracilis. 10. B in marg.: Papa quid
signat.
8. Decreti Prima Pars, dist XL. cap. VI.

p. 368:
iy. Codd. in marg. : Sanctissimus si debet esse omnis homo. 3i. et ;
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 365: Testor Deum, quod a tempore illo pocius desideravi suhesse quam preesse.
p. 367: Si papa, | qnod solum debet deponi pro heresi.
```

---

## Chunk 12-o: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-12-o.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-12-o
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "369.1–373.28"
divisions: "cap. 12 (heading 'CAPITULUM DUODECIMUM.' at 316.24); part 15 of 21, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "1051 words; 1010 unanimous or majority-real; 26 settled by vote (R2 17, R3a 8, R5a 1); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n430–n434 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 12, part 15: [TITLE]

## ¶1 · 369.1–370.32

> [p. 369] Sed tercio obicitur per hoc, quod Nicolaus de ordine fratrum Minorum dicitur de comuni consensu cardinalium et cleri ordinasse, quod non erit amplius papa nisi de suo ordine; quodvidetur racionabile, cum ille sit status perfectissimus viatoris, ut patet in Sexto: Exiit qui seminat. Cum igitur illa ordinacio non potest dissolvi nisi per fratrem minorem papam, quod nunquam contigit, videtur quod abhinc non fuit aliquis verus papa. Pro isto supponuntur leges ecclesie, primo quod hec ordinacio fuit valida, secundo quod illa non potest tolli nisi per papam et clerum, et tercio quod nunquam in aliqua synodo tollebatur; tunc videtur quod repugnat ipsam tolli nisi per papam fratrem minorem, quia esto quod cras tolleretur per papam secularem. Sed contra repugnat stante lege ista quod papa huiusmodi sit electus, igitur repugnat legibus predictis quod ordinacio illa taliter dissolvatur. Hic patet quod ecclesia humanis tradicionibus insolubiliter cathenatur; et utinam non forent leges alique papales minus racionales quam est ista. Stat igitur solucio in duobus, primo quod decretalis talis non valuit, secundo quod ordines et alia sacramenta possunt ministrari licite, nullo papa cesareo existente, nec oportet plus dilatare istam materiam. Quantum ad tercium punctum de necessitate privilegiorum etregiminis capitalis in fide catholica, patet quod Christus cum lege sua per se sufficit. Signa autem ut cruces, baculum et similia, que Cesar instituit, ut [p. 370] patet XCVI distinccione Constantinus, non vocamus privilegia, sed deliramenta, et, ut Crysostomus loquitur super epistolam ad Thym racionabiliter deridenda. Si enim videres senem puerilibus ornamentis indutum non gracia ludendi, sed maniace necessaria regimini sui corporis repudiantem, nonne deridendo diceres huiusmodi insanire? Multo magis presbiter vel prelatus, qui preponderat signa muta et putrida ante virtutes signatas est ut maniacus deridendus, et per tutorem tamquam decrepitus insaniens regulandus. Ideo necesse est reges et principes honorem melancolicum, ut puta copiam temporalium suorum subtrahere, quia ille facit omnes tales prelatos, ultra hoc quod sapuerunt apostoli vel primitiva ecclesia insanire. Contentemur igitur de paucis ritibus quos ex doctrina Christi servarunt apostoli, et omnino honeste superadditos vere et modeste non preponderanter vel ypocritice observemus. Omnia enim talia non expediunt vel sunt licita, nisi de quanto iuvant ad observanciam mandatorum. Unde videtur adulterina degeneracio, quod mandata Dei quasi neutra respicimus, et cum tradicionibus hominum sumus insolubiliter desponsati. Domini igitur, quorum bonis abutimur, debent sua subtrahere, ne ex alieni peccati participio maculentur; nec obest huic sed prodest quod principibus limitatum est a Deo officium ad tuendam ecclesiam, ut patet in decreto beati Ysidori in de summo bono libro III. Et hic notant multi quod dicit ad tuendum, non spoliandum ecclesiam.

[ENGLISH]

## ¶2 · 371.1–371.33

> [p. 371] Sed constat sciolos quod non est color: Si beatus iste dicit quod principes debent tueri, et non dicit quod debent spoliare ecclesiam, igitur non licet eis ex caritate medicinaliter auferre temporalia ab ecclesia delinquente. Sicut enim magna est distancia inter celum et terram, sic multum distant predanter spoliare et medicinaliter sic auferre. Ideo notaret sic arguens, quod sanctus doctor dicit: Principes debere tueri ecclesiam, non dicit dotare temporaliter vel ditare. Unde maior elemosina foret principibus tueri ecclesiam in limitibus religionis quam Christus instituit quam dare sibi quantamlibet elemosinam corporalem; et hoc possunt, cum possunt culpabiliter hos privilegii limites per accidens destruere, et per consequens possunt meritorie eosdem privilegii limites stabilire. Qui enim habet secundum leges dyaboli facultatem peccandi, habet pocius facultatem secundum leges Dei sibi et ecclesie promerendi. Ideo sicut seculares possunt obesse ecclesie per stultam et secularem dominorum dotacionem, sic possunt facilius atque licencius prodesse ecclesie per prudentem eorum subtraccionem. Pro declaracione autem conclusionis predicte capio quod status exproprietarie vivendi, in quo vixit clerus ante dotacionem, sit melior clero atque perfeccior quam quotquot seculares mundi divicie; quod probo per hoc quod proporcionaliter ut aliquid adiacet viatori plus ipsum habilitans ad beatitudinem acquirendam est ipsum melius atque utilius; sed status ille ad finem illum magis habilitat, igitur est habenti plus utilis.

[ENGLISH]

## ¶3 · 371.34–372.5

> [p. 371] Minor probatur tripliciter: primo per hoc quod Ihesus noster aliter inconvenienter daret ecclesie [p. 372] illum statum, cum posset eque faciliter dotasse quantumcumque clerum suum in mundi diviciis; non enim est potentis, prudentis et benevolentis sic magis bonum postponere, quia tunc vel foret invidus vel ignarus.

[ENGLISH]

## ¶4 · 372.6–372.16

> [p. 372] Similiter, quantumcumque divicie accumulentur, eciam cum securitate mundana perpetua non ponunt possessionatum nisi profundius in statu proprietario minus perfecto. Cum igitur status ille ideo dicitur principaliter minus perfectus, quia est plus a beatitudine tardativus, (ut sepe patet j ex fide evangelii) sequitur quod status ille sit proprietate contraria clero utilior. Contrariorum enim oportet unum esse perfeccius tamquam habitus et reliquum imperfeccius tamquam privacio.

[ENGLISH]

## ¶5 · 372.17–373.8

> [p. 372] Similiter, omne opus misericordie vel elemosine spiritualis est- pocius quam opus misericordie vel elemosine corporalis, sed dare tuicionem quoad statum et privilegia que Christus instituit est opus misericordie spirituale, non comparacione ad ditacionem mundanam, igitur est ipsa prestancius. Aliter enim Christus invide peiorasset apostolos, vocando eos a mundi diviciis ad purum statum exproprietarium, sicut et fratres contra caritatis regulas dampnificarent pueros et alios divites seculares, dum faciunt eos fratres, ymo procurarent et laudarent plus homines qui facerent eos proprietarios quam conditores suorum ordinum, vel patres qui fecerant eos fratres; quod credo eos dicere esse apostatarum sentenciam; vel aliter sequitur, quod donantes ordinibus illis loca et domicilia ad habitandum et contractas, peccarent graviter, et sic ipsi suum ordinem observando; debent enim iuxta falsigraphum vivendo [p. 373] in statu possessionato meritorius plus prodesse ecclesie. Ideo stulte et sine causa quam Deus approbat viverent sic parce atque penaliter, si sic deficiat perfeccio sui status. Ideo ipsi debent esse singulariter pugiles huius sentencie, nedum quia est fundamentum sui ordinis, sed quia leges ecclesie et fides scripture cum racionibus idem dicunt.

[ENGLISH]

## ¶6 · 373.9–373.28

> [p. 373] Et per idem sequitur quod in dominis temporalibus et tota ecclesia foret status ille utilior, quia aliter religiosi stulte et irreligiose facerent multos fratres. Et patet ex eodem quod sue cessio temporis non impedit, sed requirit quod debemus sic vivere, ymo temporis periculositas, temptacionis crudelitas et temporalium detestabilitas docent nos nunc pocius mundana relinquere; nam senescente mundo est homo pronior ad avariciam, et hinc dyabolus temptans in hoc acucius est caucius obviandus. Et patet, quod est contra racionem hec avaricia, quia res mundane sunt plus solito magis flexibiles, et peiores homines sunt plus debiles ad gaudendum in illis et vita breviores; cum igitur non faciant sed excitant ad sitibundius appetendum, patet ex doctrina in caritate sapiencie quod illis remotis sunt futura spiritualia appetenda, et illi qui ex obligacione vivunt vitam exproprietariam nimis degenerant, si isti sentencie tacite vel expresse contradicant.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 369.1: Pope Nicholas is said to have ordained that the Pope should always be a Franciscan.
- 369.10: This ordinance can be repealed only by a franciscan Pope and has not been so repealed,
- 369.20: All such decrees are void.
- 370.2: It is madness to set symbols above the virtue symbolized.
- 370.16: Let us be content with the rites which the apostles learned from Christ.
- 370.25: Rulers should withdraw endowments abused by the clergy.
- 371.1: To do so is not Church but to protect it.
- 372.17: To maintain the ordinances of Christ is a work of charity far higher than worldly gifts.
- 372.27: Otherwise the state of possessioners is higher than that of Friars.
- 373.9: As the world grows older avarice increases and needs to be more resisted.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 369: *ordinasse* [NW]
  - 369: *in Sexto* (one main token covers two printed words) [THIN]
  - 369: *Exiit* [THIN]
  - 369: *illa* (252ᵈ is the folio mark (bar after illa)) [R3]
  - 369: *illa* [R3]
  - 369: *cras* [R3]
  - 369: *illa* [R3]
  - 370: *Thym* (abbreviation Thym. as printed; punctuation not carried) [R3]
  - 370: *et* [R3]
  - 371: *predanter* [NW]
  - 371: *illum* [R3]
  - 372: *elemosine* (hyphenated elemo-|sine; main token holds the whole word) [R4]
  - 372: *vel* [R4]
  - 372: *peiorasset* [NW]
  - 372: *proprietarios* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 369:
1. Codd. in marg. : Nicolaus papa de ordine Minorum statuit ut solum
de suo ordine fiat papa. 10. A: supponentur. 22. Codd.: irracio-
nales. 26. B in marg.: Solucio. 3i. B: suffecit. 3i. Codd. in
marg. : Insignia pape vel aliorum.
1. De ordine fratrum Minorum. Cf. Polychronicon Ranulph
Higden VIII, 268. 6. Tit. XII, Cap. III.
De Potestate Pape. 24

p. 370:
3o. Codd. in marg. : Auferre temporalia a clero delinquente.
1. Cap. XIV. 3. Chrysostomus I. c. 3o. Decreti Sec.
Pars, Causa XXIII, Quaest. V, cap. XX, ex Isidori De Summo
bono III, cap. LIII.

p. 371:
24. Codd. in tnarg. : Status exproprteiartus est meltdr clero.

p. 372:
33. Contractas = contratas = country. 35. Codd.: ad deest.

p. 373:
23. faciant; ita codd. 29. Codd. in marg. : Auferre bona tempo-
ralia. argumentum bonum.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 369: Exiit qui seminat.
p. 371: Principes debere tueri eccle- | siam, non dicit dotare temporaliter vel ditare. \
```
