# Translation brief: potestate-pape 11-b–11-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/potestate-pape/wyc-potestate-pape-11-b.md chunks/potestate-pape/wyc-potestate-pape-11-c.md chunks/potestate-pape/wyc-potestate-pape-11-d.md` once and fix what it reports.
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

## Glossary (the 289 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| uxoratus | married | Ruled 2026-10-02. |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6); the adjective (*status exproprietarius*) "propertyless", 2026-10-08 (*Pot. pape* 146.25). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
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
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| forisfactura | forfeiture | Noun beside *forisfacere* "forfeit". Ruled 2026-10-02 (*Eccl.* 15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| affidacio | affiance | Betrothal by plighted trust; keeps the play on *confidit*. Ruled 2026-10-02 (*Eccl.* 20, 475.22). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| pseudoclerici | false clerics | Cf. *pseudomonachus*. Ruled 2026-10-02 (*Eccl.* 21, 511.17). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| pseudochristus | false christ | Matt. 24:24 (DR "false Christs"). Ruled 2026-10-07 (*Pot. pape* 28.32). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| officiarii | officers | Ruled 2026-10-07 (*Pot. pape* 86.19). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| preeminencia | preeminence | Kept apart from *primatus* "primacy". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| Pseudo (as a noun) | the Pseudo | Wyclif's name for the false pope of the eleven conditions (ch. 6). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| pseudopapa | pseudo-pope | Cf. *pseudocardinales*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 180.33). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| Cestrensis | the Chester [chronicler] | Ranulf Higden, *Polychronicon* (S note at first occurrence in a chunk). Ruled 2026-10-08 (coordinator, delegated; conformed in 06-h … 09-b). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |

---

## Chunk 11-b: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-b
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "268.28–271.21"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 2 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "631 words; 593 unanimous or majority-real; 27 settled by vote (DEL 3, R2 17, R3a 5, R5a 2); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n329–n332 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 2: [TITLE]

## ¶1 · 268.28–271.16

> [p. 268] Ex istis plane colligitur sensus discernendi sacerdotem cesareum a Christi discipulo, nam cesareus innititur titulo cesaris, dominacionem exigens et observans, ac intentus mundialibus fit exhinc in officio quod Christus instituit negligens [p. 269] vel remissus. Sed presbiter christianus innititur titulo elemosine ex gracia nec affidatur cum temporalium perpetuitate, sed reputans hoc ad onus instanter, inturbate et humiliter sine dominio complet ministerium sibi creditum, paratus sustinere cum gaudio ablacionem ymo rapinam temporalium si contingat. Nec videtur quod ista nomina sint directe opposita, cum sacerdos christianus sit sacerdos cesareus vel remisse simul vel per vices; oportet tamen omnem sacerdotem cesareum salvandum titulum imperialem deserere et in predicto titulo finaliter consumare. Unde multi decipiuntur in hoc, quod ignorant sensum scripture et doctorum, qui sepe simpliciter et in sensu composito intelligunt huiusmodi aggregata, ut sicut Apostolus dicit, quod nichil potest eos separare a caritaie Dei, subintelligendo simpliciter predestinatos. Sic Aristoteles concedit de eodem, quod album desinit esse et musicum manet, et ignorancia logice facit stultos credere quod nullus papa potest peccare, eo quod peccare repugnat racioni papali vel saltem ipsam denigrat, et sic faceto scemate dicta doctorum de papa intelligunt condicionaliter, reputative, vel in una persona generalis et debiti officii descripcionem, ut Christus sepe alloquitur Petrum et ceteros omnes apostolos. Et istomodo loquitur Jeronymus cum Lyncolniensi de papa, ut patet ex dictis. Sed et Bernhardus libro II de papa sic loquitur: Indagemus ad hoc diligencius, quis sis, quam geris pro tempore personam in ecclesia Dei, quis es, sacerdos magnus, summus pontifex, tu princeps [p. 270] episcoporum, tu heres apostolorum, tu primatu Abel, gubernatu Noe, patriarchatu Abraham, ordine Melchisedech, dignitate Aaron, auctoritate Moyses, iudicatu Samuel, potestate Petrus, unccione Christus. Et sequitur: Sunt quidam et alii Celi ianitores et? gregum pastores, sed tu tanto gloriosius, quanto differencius utrumque pre ceteris nomen hereditasti, habent illi sibi assignatos greges singuli singulos, tibi universi crediti, unus uni nec modo omnium, sed pastorum cum pastor. In istis tredecim et aliis descripcionibus foret beatus Bernhardus stulto stulcior, si sine revelacione diffinitive assereret quod papa sibi contemporaneus huiusmodi sit de facto; sed talis debet esse ex veritate assumpti nominis, sicut erant alique persone eiusdem nominis, cum prophetetur se gerere personam Christi in terris, in quo congregantur omnium sanctorum patrum laudum principia, quod si mentitur ex obliquitate vite in nomine: Ve mendaci illi cum suis complicibus. Ex istis colligo tercio, concedendo quod oportet in ordine sacerdotali tam quoad potestatem quam ministerium esse gradus, ut prepositi innitantur, quis paracius, humilius aut fructuosius ministret ecclesie, et sic conceditur quod sicut in lege veteri figuratum est tam per Moysen quam Aaron et ceteros succedentes, oportet esse in lege nova unum omnium aliorum sacerdotum principem dominum Ihesum Christum, qui non posset patencius ostendere suam stulticiam aut huius dignitatis carenciam quam promulgando de se ipso in populo illud nomen; licet enim Christus sepe expressit et sepius tacuit unigeniti dignitatem, alia tamen racio subest in aliis, cum necesse fuit illam fidem de Christo detegere. In nobis autem oportet cum timore sperare quod erimus Christi membra, quod est valde continens. [p. 271] In ipso autem necesse fuit verbum Dei esse unigenitum Dei patris, unde videtur quod cogens ad credendum ut fidem, quod ipse sit caput sancte matris ecclesie, extollitur super Christum, quia Christus docuit illud abscondite in tantum quod elicere ex scriptura unionem ypostaticam humanitatis et divinitatis Christi, sine qua non foret caput universalis ecclesie est multis difficile. Illud autem, quod Christus docuit latenter et abscondite de se ipso, illud docmatizat Antichristus inordinate, publice et infideliter de se ipso. Inordinate dico, quia sine evidencia que fidem gigneret quoscumque qui illud negaverint conatur extinguere; et hoc non est medium apostolicum sed apostaticum antichristive fidei inductivum.

[ENGLISH]

## ¶2 · 271.17–271.21

> [p. 271] Sed contra illud multi arguunt quod stat feminam vel laycum esse papam, cum verisimile sit beatam virginem post ascensionem inter ceteros propinquius sequi Christum, et stat laycum esse superiorem in moribus quocumque presbitero.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 268.28: How to discern a Caesarian priest from a disciple of Christ.
- 269.7: The two may be confused at times but not finally.
- 270.1: St. Bernard's ideal pope.
- 270.10: He did not say the pope of his time was such.
- 270.21: Christ is the chief priest; no other should claim the office.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 268: *Ex* [R4]
  - 269: *christianus* (hyphenated chri-|stianus; main token holds the whole word) [R3]
  - 270: *patriarchatu* [R5]
  - 270: *Abraham* [R5]
  - 270: *Petrus* [R5]
  - 270: *unccione* [R3]
  - 270: *et* (5 is the line number) [R3]
  - 270: *∅* (the is the English side-note) [R6]
  - 270: *sacerdotali* [R3]
  - 270: *innitantur* [R4]
  - 270: *descripcionibus* (W1: descripciombus -> descripcionibus (scans: descripcionibus | descnpciombus | descripciombus | descripciombus)) [OVERRIDE-SCAR]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 268:
8. Codd. in marg. : Dominacio pape iJilerdicilar universali*.
12, i3. et iure ; codd.: opere creationis metiio, i3 Patris ; codd.: po-
testatis. 28. B. in marg. : Omnes pape post dotacionem e. v. dicuntur
cesarei sacerdoles. Rec. inan.
lo. Ps. XLIX, 11. 11. Ps. CIII, 27. 14. Ps. II, 8.

p. 269:
20. B in marg. : Multorum solucio argumentorum. Rec. man. 21. Codd.
in marg. : Papam non posse peccare. 3o. Codd. in marg. : Pape laus.
16. Rom. VIII, 39. 3o. 1. c. pag. 75 1.

p. 270:
(none)

p. 271:
1. Codd. in marg. : Caput universalis ecclesie non est papa. 9. la-
tcnter ; codd.: rarenter. i3. Codd.: digueret. 18. Codd. in marg.
Papa fuit virgo Maria.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 268: principes super omnem terram; eis tu successisti in hereditatem; ita tn heres et orbis hereditas, ac quamvis hec porcio te contingat, id sobria consideracione pensandum; non enim reor per omnem modum, sed sane quodamtemts; dispensacio, | super illum tibi credita est, non data possessio. | extollit se super omne quod dicitur Deus. Si quis, | usurpat hanc potestatem, contradicit illi, qui dicit: Meus est orbis terre et pleuitndo eius. Kon tu ille. de quo propheta: Et erit omnis terra possessio eius. Christus hic est, qui possessionem sibi veudicat et iure creacionis et merito redemciouis et dono Pairis. Cui enim alteri dictum est: Postula a me et dabo tibi gentes, hereditatem tuam etpossessionem tuam, terminos terre, possessionem et dominium, cede huic, tu curam illius habe, pars tua hec, ultra ue exteudas manum. | idem est preesse et dominari, | cum bene preest, qui preest in sollicitudine, villa eciam subiecta est villico et dominus parvulus pedagogo. Ita et tu f iuquit, presis, ut provideas, ut consulas, ut procures et serves, presis ut prosis, presis ut fidelis servus et prudens, ut des subiectis escam in tempore, hoc est, ut dispenses, uon ut imperes; hoc fac et dominari te nou affectes homiuum homo, ut uon domiuetur tui iniusticia.
p. 269: nichil potest eos separare a caritaie Dei, | Indagemus ad koc diligencius, quis sis, quam geris pro tempore personam in ecclesia Dei, quis es, sacerdos magnns, summus pontifex, tu princeps | Pape laus. Bernh.
p. 270: episcoporum, tu heres apostolorum, tu primatu Abel, guberuatu Noe, patriarchatu Abraham, ordine Melckisedech, dignitate Aaron, auctoritate Moyses, iudicatu Samuel, potestate Petrus, unctione Christus. | Sunt quidam et alii Celi ianitores et? gregum pastores, sed tu tanto gloriosius, quanto differencius utrumque pre ceteris nomen hereditasti, habeut illi sibi assignatos greges singuli singulos, tibi universi crediti, unus \ uni nec mcdo omnium, | sed pastorum cum uuus omuium pastor.
```

---

## Chunk 11-c: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-c
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "271.22–274.33"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 3 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "733 words; 706 unanimous or majority-real; 15 settled by vote (DEL 1, R2 6, R3a 3, R5a 5); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n332–n335 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 3: [TITLE]

## ¶1 · 271.22–273.3

> [p. 271] Hic dicitur quod beata virgo fuit papa secundum extensionem nominis doctam superius; fuit enim excellenter mirabilis sanctitate, sicut et fuit sacerdos; et concordat genus gramatice cum sanctis peritis linguarum sic de papa loquentibus. Limitando autem signum ad propositum, dictum est quod papa est quicumque viator, qui sequitur Christum similius, ubi femella excluditur, quia quantumcumque sit sancta femina, propter infirmitatem sexus non permittitur evangelizare publice in ecclesia nec orare detecto capite, ut dicit Apostolus prima Cor. XI. Ideo mulier non est ydoneus capitaneus ecclesie nec [p. 272] viator simillimus sequax Christi. Et sic excluditur tam mulier quam angelus a pape nomine. De papa vero Agnete, de qua Cestrensis libro V, que post vocata est Johannes Anglicus, cum ceteris pseudoPapis? patet quod false vendicaverat nomen pape. Quoad secundum obiectum de laycis, patet logico quod laycus potest esse papa. Et videtur de Dei potencia absoluta possibile quod omnis nunc vians foret membrum dyaboli vel quod desit clerus ecclesie, j quod esset magis mirabile. Ego autem credo quod est necessarium ex supposicione quod sint multi viantes continue a tempore ascensionis usque ad diem iudicii sancciores ceteris, qui teneant statum et ordinem clericalem, sic quod ordinacioni divine repugnat, quin toto clero perverso usque ad laycos Deus subito illuminaret aliquem eorum, sic quod viveret pure exproprietarie et sancte de sorte Domini: ettunc foret clericus, licet nec aliqua septem arcium sit imbutus nec secundum ritus episcopales sit humanitus ordinatus. Ista autem evidencia non probat quod sic est de facto, sed videtur suadere quod sic potest esse de Dei potencia absoluta, Eleccionem autem Dei in talibus oportet omnem fidelem concedere, quia homo non eligit racionaliter alium ad aliquam dignitatem, nisi quia reputat eum dignum, sed si est dignus ad aliquid, est a Deo preelectus, quod debet credere; ideo nemo debet eligere quemquam ad aliquid, nisi reputet eum a Domino preelectum, et hoc est notum apud eos qui vident quod necesse est Deum ad [p. 273] omnem accionem creature concurrere preagendo. Et patet ex lege triplici ad idem ex IX cap. allegata.

[ENGLISH]

## ¶2 · 273.4–273.11

> [p. 273] Sed ulterius pro materia argumenti miror in tribus, primo quomodo adversarius non erubescit concludere primatum cuiuscumque Romani pontificis ex primatu sacerdotis Aaronitici in veteri testamento, secundo quomodo concluderetur officiorum singularis preeminencia ex lege veteri, et tercio quomodo tot ritus et ornatus episcopales ex legalibus legis veteris surrepserunt.

[ENGLISH]

## ¶3 · 273.12–273.16

> [p. 273] Quantum ad primum, cum legalia cessare debuerant, summum autem sacerdocium cum ritibus suis figuravit Dominum, qui iam venit, quare igitur non debuerunt cessare in sacerdocio Christi, nisi forte adhuc expectetur infideliter Antichristus?

[ENGLISH]

## ¶4 · 273.18–273.25

> [p. 273] Item, non videtur racio quare sequi debemus summum sacerdotem legis in hiis ritibus, quin per idem in aliis iam omissis, ut puta in uxoracione et successione hereditaria summi pontificis in suo oneroso officio et in parva porcione de sorte Domini. Non enim est racio diversitatis sufficiens, quod Machomed et Sergius colarunt de utroque testamento eis placitum, cetera displicibilia omittentes.

[ENGLISH]

## ¶5 · 273.27–274.33

> [p. 273] Item, in novo testamento debet ecclesia magis dimittere figuras et tamquam etate proveccior evacuando que erant parvuli, plus simulari ecclesie triumphanti; sed in beatis cessat omnis talis figura atque exaccio, cum sint ad ultimum unicordes; igitur in ecclesia apostolica debent ultra legem veterem ad illum statum accedere. Et hec racio, quare apostoli docuerunt in facto, verbo et [p. 274] scripto, quod cessarunt huiusmodi legalia; nec inducerentur nova ad onus ecclesie, ut patet Act. XV, ymo apostoli fuissent nimis immemores future ecclesie pretermittendo exempla in facto, verbo et scripto, quomodo successores sui episcopi militarent. Unde pro ulteriori sensu notandum quod omnis summus sacerdos legis veteris figuravit Christum in omnibus factis suis legalibus. Ideo autonomastice et singulariter ipse dicitur summus sacerdos et episcopus animarum et hinc illa multitudo sacerdotum et suorum officiorum fuit in Christo unico consumata, ut pulchre docet Apostolus Heb. IX, et Heb. VII dicitur: plures facti sunt sacerdotes secundum legem etc. Et hec racio quare apostoli non vocarunt se papas sanctissimos, capita universalis ecclesie vel universales pontifices, sed habendo secum summum pontificem usque ad consumacionem seculi, vocarunt se servos Christi in tribulacione, socios et ministros ecclesie; unde ista religio servata fuit tunc tempore beati Gregorii, et ex decreto suo incorporata legi ecclesie distinccione XCIX Prime sedis et cap. Ecce. Quare igitur non magis periculoso tempore plus indigni sine divisione vel phariseica expectacione inniterentur unite pontifici. Revera videtur iuxta distinccionem predictam et veritatem facti paparum sequi quod vel sunt personaliter Ihesus noster, vel quod sunt infidelitate peiores sacerdotibus legis veteris figuraliter expectantibus Ihesum Christum, cum propinquissime preparant viam Antichristo. Non igitur sequitur hec dominativa precellencia ex lege veteri.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 271.22: Cavil; that doctrine would make the B. Virgin pope.
- 271.31: A woman may not be pope.
- 272.5: A lay man might be pope,
- 272.18: even though he had no degree and had not been ordained by man.
- 273.12: With Christ's coming the rites of the old law are done away.
- 273.28: We should take as model the Church triumphant.
- 274.8: Christ the one high-priest.
- 274.16: The apostles did not call themselves popes or heads of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 271: *nominis* [NW]
  - 272: *ritus* [NW]
  - 272: *racionaliter* (hyphenated raciona-|liter; main token holds the whole word) [R4]
  - 272: *∅* (second half of raciona-|liter, which the main scan already holds whole at pos 180) [INS?]
  - 273: *iam* [R4]
  - 273: *cessat* [THIN]
  - 273: *omnis* [THIN]
  - 273: *talis* [THIN]
  - 273: *figura* [THIN]
  - 273: *illum* [R3]
  - 274: *singulariter* [NW]
  - 274: *illa* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 271:
1. Codd. in marg. : Caput universalis ecclesie non est papa. 9. la-
tcnter ; codd.: rarenter. i3. Codd.: digueret. 18. Codd. in marg.
Papa fuit virgo Maria.

p. 272:
2. Codd. in marg. : Papa Agnes midier.
3. See below. Cf. et Hus, De Eccl. fol. 2 2o\ Johannis
Wyclifs Cruciata, Pol. Works, ed. Buddensieg 619; Agnes ibidem
Anna nominatur. See Dollinger, Papstfabeln des Mittelalters,
pag. 16.

p. 273:
2. B: Exo. Codd. in marg. : Primatus pape non concluditur ex simili-
ludine. 9. A: singulavum.
De Potestate Pape. 1 &

p. 274:
\.\. Codd. in marg. : Apostoli non vocarunt se sanctissimos vel
capita.
i?. Ct'. Hus Opp. 219. 22. Cap. III. 2'3. Cap. V.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 274: Prime sedis
```

---

## Chunk 11-d: write to `/Users/wilsonpruitt/wyclif/chunks/potestate-pape/wyc-potestate-pape-11-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-potestate-pape-11-d
work_la: Tractatus de potestate pape
work_en: On the Power of the Pope
volume_slug: potestate-pape
editor: Johann Loserth
year: 1907
pages: "275.1–279.15"
divisions: "cap. 11 (heading 'CAPITULUM UNDECIMUM.' at 265.17); part 4 of 13, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [johanniswyclift00mattgoog, johanniswyclift01mattgoog, latinworks19wycl, tractatusdepotes00wycl]
check: "956 words; 872 unanimous or majority-real; 60 settled by vote (R2 37, R3a 15, R5a 6, R6a 2); 24 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks19wycl, leaves n336–n340 (printed p. = leaf − 61)"
status: draft
---

# *De potestate pape*, chapter 11, part 4: [TITLE]

## ¶1 · 275.1–276.23

> [p. 275] Quantum ad secundum scribit dominus Ardmacanus in De Questionibus Armenorum libro XI in fine cap. V de questione Armenorum: Ex isto capite sequi michi videtur, quod conclusio ad potestatem ligandi et solvendi sive remittendi peccata sive retinendi, sive baptisandi aut consecrandi aut benedicendi, et breviter quoad quantumcumque potestatem actus sacramentalis expressam a Christo in evangelio, quiscumque sacerdos in ordinacione sua totam accipit aut nichil ipsius, quoniam singulis in simul et indivise sunt date a Christo, et Matth. XIV, 6 ac Mar. X, 9 mandat ipse, quod Deus coniunxit, homo non separet. Unde videtur racionabiliter posse concludi, quod hec potestates sacramentales in omnibus sacerdotibus sunt equales. Hec doctor. Sed notandum quod crescente multitudine presbiterorum m sciencia et potencia variata, potest racionabiliter limitari sacerdotibus habilioribus singulariter officium, attestans in eis preeminenciam dignitatis, salva tamen potestate sacerdotibus inferioribus tempore necessitatis vel indisposicionis superioris presbiteri sacramenta ista et sacramentalia ministrandi; nam in lege veteri, ubi magis attenderant ad tales ritus sensibiles, propter indisposicionem summi pontificis non solum licuit sacerdoti inferiori, sed debuit supplere ministerium summi pontificis: aliter enim quando summus sacerdos foret infirmus vel sompno nocturno vel alia causa pollutus, sequeretur inconveniens legis Dei; aliquando enim polluti sunt ad vesperum, ut dicitur Levitici XV, 5 et Deuteronomio XXIII, et aliquando usque ad septimum diem, ut dicitur Ezech. XLV. Cum igitur debuerunt cottidie offerre super altare incensi [p. 276] vespere et mane, ut patet Exod. XXX, patet, quod inferior sacerdos potestatem habuit defectus summi pontificis exsupplere. Quare igitur non in lege nova, ubi ritus talis minus attenditur? Hoc enim officium pertinebat singulariter cum paribus ad summum pontificem, ut patet Exod. XXX et XXXIX et Levitici VIII, oportet tamen tam ex parte superiorum quam inferiorum quam eciam tocius populi cavere pericula. Ex parte superiorum, ne exinde superbiant, putantes hoc eis contingere pure ex institucione divina, secundo ne ad illum statum sumantur inhabiles, et tercio omnino ne ex cupiditate eorum tale ministerium sit venale. Sacerdotem autem inferiorem oportet cavere ab istis et omnino, ne ex pre sumpcione temeraria det scandalum fratri suo. Et omnem fidelem oportet attendere ne talibus nimis ponderante precio innitatur. Aliqui enim plus appreciantur hos ritus bene sed humanitus adinventos quam evangelium vel mandata decalogi. Periculosum est, inquam, iudaice hos ritus preternecessarios nimis attendere; Deus enim supplet defectus eorum ex aliis operibus virtuosis.

[ENGLISH]

## ¶2 · 276.25–277.10

> [p. 276] Secundo principaliter sic arguitur: Ex lege veteri eliciunt sancti et leges ecclesie quod propter distincciones ordinum sunt ministeria episcopo deputata. Unde Dyonisius in De Ecclesiastica Yerarchia ponit tres ordines ecclesie, scilicet ordinem yerarchicum, quem episcopalem intelligit, ordinem sacerdotalem vel presbiteralem et ordinem ministerialem, et distinguens proprias operaciones uniuscuiusque istorum ordinum, [p. 277] narrat quomodo ad supremum ordinem, scilicet episcopalem, spectat sacerdotum consecracio, divini ungenti perfeccio et sacri altaris benediccio. Unde censeretur hodie insanus qui diceret quod quilibet sacerdos habet potestatem ordines conferendi, baptizatos confirmandi, ecclesias et ornamenta sacerdotalia benedicendi et sic de benediccionibus ornamentis et aliis ritibus, que per sapientes et sanctos antiquos episcopali dignitati sunt propria.

[ENGLISH]

## ¶3 · 277.11–279.15

> [p. 277] Quantum ad istud, patet ex dictis quomodo licite possunt fieri et licite pretermitti. Ideo requiritur magna prudencia ad acceptandum ista in suo ordine. Quidam enim putant sine istorum sacramentorum et sacerdotum ordine non posse recte viare ecclesiam, unde tantum ponderant has cerimonias, quod offendentem plus puniunt quam qui infideliter in caritate deficiat. Conceditur igitur cum beato Dyonisio quod sunt tales tres ordines sacerdotum, cum iuxta decretum Crysostomi positum distinccione XL Multi sunt sacerdotes et pauci sunt sacerdotes. Sed non oportet, quod sacerdos ex gracia Dei factus superior accipiat exinde novum ecclesiasticum sacramentum, dum ego omnino omitterem habere episcopalem consecracionem, antequam accipere presumerem hoc episcopale ministerium; est enim preternecessarium et predicacione, oracione ac multis aliis cultibus Dei inferius, nec non ad multos cultus Dei non tam necesse sicut creditur requisitum. Conceditur ergo, quod benediccio, consecracio et alia ministracio episcopalis est laudabilis rite facta. Sed grave est quod ecclesia [p. 278] oneretur tam multiplici cerimonia, gravius quod tantam vim ponat in illa, et gravissimum quod nemo potest salvari a Deo, ut dicunt, nisi credat et accipiat secundum formam iam currentem huiusmodi sacramenta. De istis autem in tractatu De Sacramentis est sermo lacior. Et sic conceditur quod vestes sacerdotales et ornamenta episcopalia possunt introduci pie et religiose, licet mendaciter et impie communius sint accepte, ut tractantes ritus humanos et statuta hominum, notant quinque vestimenta sacerdotalia, quibus communiter induitur celebrando, et variantur in parte ab ornamentis sacerdotum veteris testamenti, ut declarat Hugo libro secundo De Sacramentis parte IV. Singularis, inquit, habitus sacerdotibus Christi in ministerio traditur, ut per id quod foris apparet quales intus esse debeant ostendatur, sacrarum autem vestium ritus partim a veteri testamento assumptus est et partim a patribus novi testamenti adiectus. Legitur enim Exod. XXVIII, XXIX, XXX et XXXIX quomodo Moyses indueret Aaron fratrem suum, primo tunica bissina, que grece poderis id est talaris dicitur, que a collo usque ad talos extenditur, que in novo sacerdocio non solum de bisso sed de lino contexitur; ipsa autem modificata membris corporis et aptata nichil superfluum aut dissolutum in vita sacerdotis debere esse ostendit. Sed in novo testamento laxatur post dotacionem ecclesie, cum multa temporalia preter necessaria officio sacerdotis sibi monstruoso adiaceant. Hec autem vestis ob spem candoris nomen Albe sortitur, que signat spiritualem mundiciam ministrorum, iuxta [p. 279] illud Apok XIX, 8: Datum est sponse ut operiat se bissino splendenti candido. Etsequitur exposicio: Bissinum enim iustificaciones sunt sanctorum. Caro quidem hominis mundiciam quam ex natura non habet, studio bono aquirit per graciam, sicut bissus vel linum candorem suum, quem natura non habuit, per studium et industriam artificis aquisivit, dum multis tunsionibus ac locionibus illustracione solis siccantis quasi quadam violencia attritum vertitur in alborem. Oportet quidem crebro castigare corpus et in servitutem redigere, sicut dicit Apostolus prima Cor. IX se fecisse; et sic positus in aqua tribulacionis et tunsus tortoribus ac interim sole iusticie consolatus a tribulacionibus siccatus et calore veritatis accensus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 275.4: Sacerdotal powers are equally and indivisibly in all priests, yet some acts may be limited to those fittes to perform them.
- 276.7: Yet the danger of such distinctions must always be kept in mind.
- 277.11: Too much stress is laid on difference in orders.
- 278.8: Vestments may be rightly used. Their origin and purpose.
- 278.22: What were used in the old law.
- 278.23: The Alb.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 275: *videtur* [R4]
  - 275: *et* [R3]
  - 275: *et* [R3]
  - 275: *sua* (10 is the line number) [R4]
  - 275: *et* [R3]
  - 275: *equales* [R4]
  - 276: *illum* [R3]
  - 276: *pre* (hyphenated pre-|sumpcione; main token holds the first half (the i is the line number 15); sumpcione follows at pos 104) [R3]
  - 278: *illa* [R3]
  - 278: *foris* [R4]
  - 278: *novi* [R3]
  - 278: *primo* [R3]
  - 279: *Apok XIX* (one token covers two printed words (Apok. XIX,)) [THIN]
  - 279: *ut* [R3]
  - 279: *bissino* (hyphenated bis-|sino; main token holds the whole word) [R5]
  - 279: *mundiciam quam* (one token covers two printed words) [THIN]
  - 279: *ex natura* (one token covers two printed words) [THIN]
  - 279: *non* [THIN]
  - 279: *sicut* [R3]
  - 279: *in* (10 is the line number) [R3]
  - 276: *Quare igitur* (W-split: Quareigitur -> Quare igitur (two words run together)) [OVERRIDE-SCAR]
  - 278: *sint accepte,* (W-split: sintaccepte, -> sint accepte, (two words run together)) [OVERRIDE-SCAR]
  - 277: *tam* (LEFT-odd: box in blank gap after tam) [OVERRIDE-SCARPLATE]
  - 279: *attritum* (LEFT-nw: italic; t before r and u read as t (one crossbar tall t)) [OVERRIDE-SCARPLATE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 275:
1. Codd. in marg. : Potestatem plenam accipit sacerdos quilibet ta
consecracinne. 3o. Codd.: aniea enim. 32. B: Deut. XXVIII.

p. 276:
(none)

p. 277:
18. Codd.: qui deest. 3i. A in marg. : Dionysius concedit tres
ordines ecclesie secundum officia distinctos.

p. 278:
8. Codd. in marg. : Vestimenta episcopalia (solum B:) possant intro-
duci pie et religiose. 19, 20. Codd. ifratribus.
10. Hugo De Sacram. Opp. (ed. Mog. 16 17) III, 449.

p. 279:
1, 2. Codd.: bissinum splendentis candidum ut deest. 3. Codd. in
marg. : Alba prima vestis. 10. Oportet; B : Sed. 16. Codd. in marg. : Se-
cunda \ona. 18. B : Circa deest. 21. Codd. : Lucae XII. 22. A : Etsicut.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 275: Ex isto | capite sequi mtcht vtdettir, qtiod concnisio ad po- | b testatem ligandi et solvendi stve remittendi peccata | sivc retinendi, sive baptisandi aut consecrandi aut beuedicendi, et breviter qtioad quantnmcumque potestatem actus sacramentalis expressam a Christo in evangelio, quiscumque sacerdos in ordinacione \osua totarn accipit aut nichil ipsius, quoniam singulis in simul et indivise sunt date a Christo, et Matth. XIV, 6 ac Mar. X, 9 mandat ipse, quod Deus coniunxit, homo non separet. Unde videtur racionabiliter posse concludi, quod hec potestates | sacramentales in omnibus sacerdotibus sunt equales. | ad vesperum,
p. 276: Ritus sacerdotales episcopales.
p. 277: Multi sunt sacerdotes et pauci sunt sacerdotes.
p. 278: De Sacramentis | habitus sacer- \ | dotibus Christi in ministerio traditur, ut per id quod foris apparet quales intus esse debeant ostendatur, sacrarum autem vestium ritus partim a veteri testamento assumptus est et partim a patribus uovi testamenti adiectus. Legitur enim Exod.20 XXVIII, XXIX, XXX et XXXIX quomodo | Moyses indueret Aaron fratrem suum, primo tunica | ^issina, que grece poderis id est talaris dicitur, que a collo usque ad talos extenditur, que in novo sacerdocio non solum de bisso sed de lino con- | texitur; ipsa autem modificata membris corporis et aptata nichil superfluum aut dissolutum in vita sacerdotis debere esse ostendit. | Hec autem | vestis ob spem candoris nomen Albe sortitur, que signat spiritualem mundiciam ministrorum, iuxta
p. 279: illud Apok.XIX, 8: Datum est sponse nt operiat se bissinosplendenti candido. | Bissinuui enim iustificaciones snnt sanctorum. Caro quideui hominis mundiciam,quam exnatura non habet, | studio bono aquirit per graciam, sicut bissus vel linum candorem suum, quem natura non habuit, per studium et industriam arlificis aquisivit, dum multis tunsionibus ac locionibus illustracione solis siccantis quasi quadam violencia atiriium vertitur \oin alborem. | stncta tunica iinea circa renes, per cuius fortem tinccionem notatur, ut ca- | stitas sacerdotis nuilo incentivorum estu, cogitacione velopere dissolvatur, iuxta illud LuceXII, 35: Sint lumbi vestri precincti. Et sic candor vestis signat mundiciam, zona vero continenciam, ut illic non sordescat, Jtic 11011 efftuat conversacio sacerdotiSo | De zona legitur Exod. XXVII: distincta \ quatuor coioribus, scilicet bisso et purpura, iacincto et cocco. | sequi agnum quocumque ierit.
```
