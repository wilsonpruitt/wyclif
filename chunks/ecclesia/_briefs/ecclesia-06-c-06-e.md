# Translation brief: ecclesia 06-c–06-e

You translate these 3 chunk(s) of Wyclif's *Tractatus de ecclesia* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-06-c.md chunks/ecclesia/wyc-ecclesia-06-d.md chunks/ecclesia/wyc-ecclesia-06-e.md` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.


## The working card

# TRANSLATOR CARD — one *De ecclesia* chunk

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Adapted from `chunks/dialogus/CARD.md` (2026-10-01). Read it, then `GLOSSARY.md`, then your
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

*Tractatus de ecclesia*, ed. Johann Loserth (Wyclif Society, 1886), from the plates of archive.org
`latinworks10wycl` (**leaf = page + 37**). Written 1378–79, after Gregory XI's bulls against *De
civili dominio*, as the Schism opened. A **treatise**, not a dialogue: Wyclif speaks in the first
person, states conclusions, raises objections against them (*instatur*, *obicitur*, *arguitur*) and
answers them (*dicitur*, *respondetur*). Its subject is what the church *is* (the number of the
predestinate), and from that, headship, membership, the pope, endowment and sanctuary.

**Sigla** (Loserth): **A** Vienna, ÖNB Cod. Pal. 1294 (his base); **A₁** Vienna 3929 ("almost wholly
valueless"); **B** Prague, University Library X.D.11, whose early reader's marginal glosses Loserth
prints ("B in marg: …"); **D** Dublin, TCD C.1.23 (chapter 7 only). Cite variants with these sigla.

**The page foot** (in your brief as "apparatus", by page) has two blocks, both keyed to the line:
the variants (`26. AA₁: tamen ex.`) and Loserth's source references (`27. Decret. Unam sanctam.
Extrav. comm. lib. I, tit. VIII, cap. I.`). The OCR of it is rough: read it for sense, not letter by letter.

## The job

The Latin in your scaffold is **established and frozen** (three-witness vote + plate reading). Fill
`[TITLE]` (short, lower case: "headship: the pope is not head of the church"), each `[ENGLISH]`, the
notes and the transcription notes; set `status: translated`; lint; report.

- **Headings:** keep `## ¶k · range` exactly. **Never change a range; never split a paragraph.**
  (The pilot headed its paragraphs with Loserth's alinea letters A, B, C; the scaffolds do not
  carry them, so leave the ¶ numbers.)
- **Never alter the Latin.** A word that looks wrong: read the apparatus for that line first; then,
  if still doubtful, the plate (`text/ecclesia/raw/leaves/nLEAF.jpg`, LEAF = page + 37 padded to four digits: p. 1 = `n0038.jpg`). A variant
  that gives the sense → translate it + **T** note citing the siglum; a compelling emendation →
  translate it + **T** note "(our emendation)"; neither → translate the print and flag it. Never
  smooth nonsense into sense. Report every such case. **Loserth's printed text governs** (ruled
  2026-10-02): translate it, his own emendations included, unless it will not construe; a manuscript
  reading is chosen only then, and **A₁ alone never outweighs the print**; every departure gets a T note
  giving both readings. Open flags for this volume:
  `text/ecclesia/PLATE-FLAGS.md` (read it if your pages are listed there).
- **English layout:** `[N]` at the same word as `[p. N]` in the Latin (the chunk's first `[p. N]` is
  implicit). Supplied words in `[brackets]`, sparingly. Quotations in quotation marks: Loserth
  italicises quotations, but the scaffold does not carry italics (`italics: none`), so find quoted
  matter by sense and by the source references at the page foot.
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
   Key rulings for this volume: *ecclesia* church (**lower-case**) · *ecclesia militans / triumphans /
   dormiens* the church militant / triumphant / sleeping · *quiditas* quiddity · *caput* head ·
   *membrum* member · *predestinati* the predestinate · *presciti* the foreknown · *papa* pope ·
   *vicarius Christi* vicar of Christ · *sponsa* bride · *caritas* charity (never love) · *dominium*
   lordship · *viator* wayfarer · *patria* homeland · *ex fide* as faith teaches (with a genitive:
   "from the faith of scripture") · *sentencia* teaching · *evidencia* evidence (the rest: GLOSSARY).
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
   | per idem | by the same token | "in the same way" |
   | ymmo | indeed, rather (correcting upward) | (omitted) |
   | patet; constat | it is clear; it is evident | |

   "Now" is reserved for the minor premiss, or the step that brings a new premiss to bear (*Illos
   autem parentes debemus …*, 1.17). An *autem* that only extends the same step is "and" (*Illis autem
   cultis …*, 1.19).
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
  CONVENTIONS §4; Hus's reuse where Loserth notes it: "cf. Hus, De eccl.").
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your
  report with a status: `editor` (Loserth's source reference at the page foot), `to-verify` (from
  memory: every patristic or canon-law identification you did not read in this session), `verified`
  (you read the source text this session: say where; local PL at `~/patrologia/sources/pl/tei/`).
  ⛔ Never pass memory off as verified. Id `E<chunk>-<n>` (`E02a-1`), cited in the note:
  "(LEDGER E02a-1)". Loserth's references to the *Corpus iuris canonici* (Decretum, Extravagantes)
  are `editor`; give them in modern form (*Extrav. comm.* 1.8.1) and say the form is ours.

## The pilot (`pilots/wyc-ecclesia-01a.md`, pp. 1.1–5.13)

A reviewed model of register and note style, read for that. Two cautions: its Latin was established
before the re-extraction (**your scaffold's Latin governs**), and it predates some GLOSSARY rulings
(**GLOSSARY governs**: e.g. the pilot's "by faith" for *ex fide* becomes "as faith teaches"). Its
ledger rows are V-01…V-19 in `LEDGER.md`. **Chunks 01-a and 01-b** fall inside the pilot's pages:
start from the pilot's English and notes for those pages, bring them into line with your Latin, the
card and GLOSSARY, keep its ledger ids, and say in your report what you changed. **01-a** also fills
`## Headnote` from the pilot's headnote, keeping each `[verify]` until its ledger row is verified.

## Side-notes

Already read against the plates (WORKFLOW 5; 1,293 notes, `text/ecclesia/sidenotes.fixed.tsv`) and
placed in your scaffold's section. ⛔ Do not edit them. One that is plainly wrong (garbled, or at
the wrong line): report it under Latin doubts as `side-note page.line`.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/ecclesia/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk(s)**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words per chunk, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?

## Glossary (the 132 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
| adolescentula | young maiden | Song 1:2, 6:7 (DR "young maidens"). Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |

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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 06-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "123.28–126.13"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 3 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "590 words; 550 unanimous or majority-real; 33 settled by vote (R2 14, R3a 18, R5a 1); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n160–n163 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 3: [TITLE]

## ¶1 · 123.28–125.32

> [p. 123] Ad illud autem videtur dicendum iuxta sepe dicta quod Christus in primo instanti mundi fuit sponsus ecclesie predestinacione, in confirmacione autem angelorum dedit dotem parti sponse sue et sic in confirmacione [p. 124] Abel iusti et aliorum sanctorum usque ad incarnacionem, manente continue eadem desponsacione, cum Cesar semper Augustus continue auget dotem. In incarnacione vero fecit secundas nupcias, creando quandam reginam partem tocius ecclesie que quadam proprietate dicitur ecclesia christiana. Tunc enim dux et legifer noster familiarius alloquens sponsam suam (ut dicit apostolus Hebr. 1°) per assumpcionem humanitatis inducit arma nostra et ut gigas superavit hostes ecclesie, redimens partem sponse incarceratam et docens aliam quomodo sequeretur eius vestigia. Unde tota doctrina christiana stat in ista oracione ecclesie qua rogamus sponsum per adventum eius in carnem, ut doceat nos terrena despicere et amare celestia. Despicere, id est, in affeccione postponere. Ille enim despicit temporalia qui a summa sede anime ipsa abicit et facit ipsa intencioni celestium abiectissime ministrare. Et bene foret sibi qui perfecte didicerit istam regulam religionis, tunc enim foret in recta via sequendi sponsum et assumptam iuvenculam in regnum celorum. ad- Tercio vero in ultimo adventu faciet agnus nupcias consummatas, coronando et confirmando reginam integram que est una columba et universalis ecclesia, non pars alterius ecclesie (ut patet Apoc. XXI°). Et super ista consideracione dependet magna pars sensus scripture et servicii ecclesie. Nam ex fide erit una totalis ecclesia glorificata post diem iudicii, et illa secundum magnam partem est modo sponsa in celo, in purgatorio et in mundo. Ideo illa est continue una universalis et sancta mater ecclesia, et illa est quam [p. 125] debent leges intelligere et omnis christianus reverenter intendere; illa, inquam, figurata est in Salomone et templo, ut canit ecclesia. Frustra namque ordinaretur vel legeretur quod Salomon haberet tot reginas, tot concubinas et tot adolescentulas, nisi ut figurando Christum significet nobis suum coniugium cum spiritibus celestibus, tam angelis quam animabus, quam cum adolescentibus viantibus; ex quibus omnibus componitur una columba que est universalis ecclesia, eadem que coronabitur in patria, quia aliter foret continue alia et alia universalis ecclesia. Frustra eciam ordinaretur et legeretur construccio templi Salomonis (de quo III° Reg. VI° cap.) ad figurandum Christum et ecclesiam, que est templum suum (ut dicit apostolus Iª Cor. 111° 17). Sicut enim fuerunt tres partes templi: prima in quam totum vulgus et alienigene intraverunt, quam sacerdotes in tempore Christi negociacionibus occuparunt (ut patet Matthei XXI°, 12). Et illa signat militantem ecclesiam in qua sunt eciam alienigene ut presciti. Secunda vero fuit corpus ecclesie populo Israhelitico deputata, signans perfecciores pure Israhelitas a rugis in purgatorio depurandos. Tercia vero fuit sancta sanctorum in quam soli sacerdotes intrarunt solempniter semel in anno. Et illa signat triumphantes, ut exponit apostolus Hebr. IX°, 1 1: Christus assistens pontifex etc. Sic, inquam, tota fabrica templi signat universalem ecclesiam iuxta fidem. Unde istum articulum fidei tenentur episcopi docere inferiores sacerdotes et populum, quia aliter ignorarent usum servicii ecclesie ad cuius noticiam obligantur, et specialiter illum articulum fidei ecclesiam sanctam catholicam quem omnis catholicus debet scire.

[ENGLISH]

## ¶2 · 126.1–126.13

> [p. 126] Et patet quod Christus semper est caput ecclesie. Unde ego credo quod, quicunque episcopus vere presidet in particulari ecclesia, remanet post mortem suam caput vel patronus eiusdem ecclesie. Quamvis enim moriatur in corpore, procurat tamen in spiritu pro subditis eciam fervencius quam in via, et post diem iudicii habebit quandam preeminenciam et illuminacionem, sicut in angelis longe alterius racionis quam prepositura viancium. Ideo rogamus, ut sanctos episcopos semper habeamus patronos in celis. Sed illi non contendebant circa primatus, adulterantes scripturam sacram, ut populus astringatur in via credere quod ipsi sunt capita sancte matris ecclesie.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 123.29: but he was always head by predestination.
- 124.4: In the incarnation he made second nuptials, raising a part of the Church to be Queen.
- 124.22: At the last advent the Lamb will make marriage consummate and the whole Church will be crowned as Queen.
- 125.4: Solomon's queens, concubines and virgins figure the three states that compose the Church.
- 126.1: A good bishop remains after death patron of his (local) Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 123: *Christus* [R3]
  - 124: *familiarius* [R4]
  - 125: *III°* [R4]
  - 125: *Iª* (15 is the line number) [R3]
  - 125: *12* (print "XXI°, 12)."; main token holds the whole number, lost its 1) [R3]
  - 126: *illi* (10 is the line number) [DEL]
  - 125: *debent* (145c folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 123:
i. A in marg. : Nota; replicacio. 4. A in marg. : Responsio.
Omnia predestinatorum capita sunt capita ecclesie. 11. A in marg.:
Quarta obieccio. 21. A: corrumpta. 22. A A^: manet.
25. A in marg. : Responsio. Prima diflicultas. B inmarg. : Utrum Christus
fuit ante incarnacionem. 3o. A m marg. : Christus in primo instanti
mundi fuit sponsus ecclesie.
3o. Cf. Hus, De ecclesia, Opp. tom I, 198*.

p. 124:
4. A in marg. : Christus in incarnacione originavit ccclesiam christianam.
8. A in marg. : Nupcie Christi per incarnacionem. 12. B in marg. :
Tota doctrina christiana stat in una oracione. i5. B: preponere.
22. A in marg. : Nupcie consumacionis. B: nupcias consumptas. 25. B:
Moralium XXI.
3. Cf. WycIiPs De Benedicta Incarnacione cap. V, pag. 67.

p. 125:
4. A: regninas; A in marg. : Concubine, regine, adolescentule Salo-
monis. i3. A: III Reg. VI cap. i5. A in marg. : Distinccio
templi Salomonis ad ecclesiam. 16. A: primam in; B in marg. man.
rec. : Tcmpli partes tres. 16. A: aligenigene. 23. Codd. : qua;
3. Vide supra pag. 97 1. 5. 4. Cant. VI, 7.

p. 126:
1. A in marg. : Conclusio. 4. A: est (in red ink) suam est caput.
7. B: quandam primiciam. 14. Ainmarg.: Secunda difficultas. Utrum
verbum est homo Christus Jesus ante incarnacionem. B in marg. man.
rec: Ante incarnacionem verbum est homo Christus Jesus. 21. B:
missa. 32. B in marg. man. rec: In triduo.
```

---

## Chunk 06-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "126.14–130.17"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 4 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "999 words; 910 unanimous or majority-real; 72 settled by vote (R2 24, R3a 33, R3b 3, R5a 9, R6a 3); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n163–n167 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 4: [TITLE]

## ¶1 · 126.14–128.9

> [p. 126] Secunda difficultas logica est, utrum debet concedi, posito quod essemus ante incarnacionem, quod verbum est homo Christus Jesus. ht videtur quod sic, nam secundum rectam philosophiam et logicam creatura nedum habet existenciam in suo singulari sed tam esse ydeale in verbo quam esse potenciale in causis secundis. Cum ergo ante incarnacionem fuit illa sancta massa materialis in patribus, quam postmodum assumpsit de virgine, et spiritus habuit esse in humana specie, videtur quod totus Christus habuit humanitus esse potenciale, et sic esse. Confirmatur secundo exb hoc quod sacerdos conficiens in sancto triduo vere conficeret corpus Christi, sicut dicunt doctores concorditer, in tantum quod hoc foret tunc verum hoc est corpus Christi (ut recitavi in tractatu De Incarnacione); quare ergo non foret verum ante incarnacionem quod verbum est Christus, cum tunc habet corpus quod post unit sibi, sicut est de corpore suo pro triduo? [p. 127] Tercio confirmatur ex hoc quod ecclesia foret aliter acephala, cum tunc non haberet caput intrinsecum sicut post, et cum non potest habere taliter nisi unum caput, videtur quod Christus ante incarnacionem fuit caput sponse sue intrinsecum, quia aliter vel haberet duo capita vel idem foret caput extrinsecum et caput intrinsecum. Et ad illud sonant quotlibet scripture (ut allegavi alias de beato Jeronymo in quadam epistola ad Paulum et Eustochium). Hic dicitur quod patribus veteris testamenti fuit hec vera: verbum est homo Christus Jesus. Ipsi enim secundum sanctos habuerunt eandem fidem quam nos habemus. Ideo sicut nos credimus creacionem mundi, carnis resurreccionem et vitam eternam, hoc est. quod Deus tempore suo creat mundum, quod mortui resurgent, et quod beati vivunt eternaliter post diem iudicii, ita utraque ecclesia credit incarnacionem, scilicet quod Christus pro suo tempore incarnatur. Et sic proposicio nostra! Christus est homo, foret in signo utrobique vera, non quia tunc est quod Christus est homo, sed quia verum est quod Christus est homo pro suo tempore. Nec video quod Christus est homo pro illo tempore, cum tunc componeretur ex corpore et anima quam assumeret pro illo tempore, et potissime foret primus Adam secundum materiam et non secundum raciones seminales, qualiter apostolus dicit Levi fuisse in lumbis Abrahe, et qualiter Anselmus dicit: Omnes nos fuisse Adam, sed limitatum est ad existenciam individuam humanitatis Christi. Et ad primam instanciam dicitur quod non sequitur: Hoc eternaliter fuit et hoc est iste homo, ergo iste homo eternaliter fuit, deducendo pure creaturam. [p. 128] Conceditur tamen de Christo quod ipse eternaliter fuit Deus; nec sequitur: Si iste homo habet esse potenciale in causis secundis, ergo iste homo est pro eadem mensura, quia tunc omne individuum quod posset esse foret, et sic esse in potencia est distrahens. Vel concesso quod Christus habet esse creatum pro mensura data, quod est, esse cause secunde, tamen tunc non habet esse Christi, quia tunc haberet existenciam humanitus singularem.

[ENGLISH]

## ¶2 · 128.10–128.17

> [p. 128] Et sic respondetur ad secundam instanciam con- cedendo assumptum, cum Christus fuit in triduo tam corpus quam anima, sed cum Christus non assumit corpus ypostatice nisi mediante anima, patet, cum nondum creata est anima Christi pro tempore veteris testamenti, non pro illo tempore est Christus, nec sufficit ad esse individuum esse specificum, quia tunc omnes effectus absolute necessario evenirent.

[ENGLISH]

## ¶3 · 128.18–128.28

> [p. 128] Ad tercium negatur assumptum, cum ecclesia semper fuit capitata per verbum quod mansit perpetue eadem persona et sic idem caput post et ante. Conceditur tamen quod post illas nupcias celebratas in utero virginis, quando Christus fuit murus et antemurale sponse sue, fuit caput racionis duplicis et duplicis nature et sic simul caput intrinsecum et caput extrinsecum eiusdem ecclesie. Et sic ad auctoritates potest dici (ut alias) quod Christus est pro tempore veteris testamenti nedum secundum deitatem sed secundum causas secundas, et sic possunt ipsi dici christiani.

[ENGLISH]

## ¶4 · 128.29–129.11

> [p. 128] Tercia difficultas naturalis est, quomodo manet idem corpus inanimatum aliis partibus corruptis continue generatis. Sed ad illud dictum est alias quod est dare corpus successivum tam continue quam interpolate, et ita est de domo materiali, sive ecclesia, sic quod existente secundum totam aliquam fuit illa que permansit [p. 129] in principio, adhuc manet; et est eadem domus successiva que fuit a principio usque in finem; sicut posito quod ignis incipiat partibiliter generari et cum hoc corrumpi, tunc ignis successivus mensurat secundum partes utrumque motum, et sic corrumpitur inanimatum ad corrupcionem tocius et manet continue, dum corrumpitur. Et si queratur, quando consecrande forent ecclesie, dicitur quod ille est ritus humanitus introductus, ideo non est vis de tali consecracione assistente sanctitate persone incolentis. Istam autem materiam relinquo aliis.

[ENGLISH]

## ¶5 · 129.12–129.17

> [p. 129] Sed quinto arguitur, probando sequi ex dictis omnem honorem et obedienciam inpendendam prelato confundi et omnem exaccionem corporalis debiti, cum deficeret probacio predestinacionis vel sanctitatis, et illud secundum racionem foret fundamentum talia vendicandi.

[ENGLISH]

## ¶6 · 129.18–130.17

> [p. 129] Hic negatur assumptum, quia (ut patet alibi) operibus debet credi, nec licet prelato aspirare ad lucrum vel honores illis dimissis, quia ut sic redderet se indignum illis lucris atque honoribus. Unde oraremus omnes, ut ecclesia sicut in suis primitivis attendat pure fructuoso operi sine ambicione temporalis commodi vel honoris. Modo vero ad tantum invalescebat oppositum quod de clero nostro potest dici illud Ysaie III°, 12: Populum meum exactores sui spoliaverunt et mulieres dominate sunt eius. Et sequitur: Popule meus qui beatum te dicunt, ipsi te decipiunt. Nam qui olim erant rectores anime, iam perversi sunt in exactores pecunie; qui olim zelabant pro honore divino contempto honore mundano, modo econtra lege Dei et per consequens honore eius postposito, preponderantes tradiciones [p. 130] humanas nimis dediti sunt mundo, qui olim dediti sunt ministerio apostolico, contempto temporali lucro, modo econtra totaliter inhiant temporali comodo, insolencia mundana et ocio introducto. Et tum extorta sunt nomina: Nam qui olim nominarunt se a Deo vocatos apostolos, hodie contendunt se permissione divina ab homine nude electos; qui olim nominarunt se servos domini Jesu Christi, hodie retorquent, ut nominentur domini reverendissimi et patres beatissimi, et (quod est summus gradus ypocrisis) vocant se servos servorum Dei, licet sint in opere, et per consequens, in nomine reali servi precipui patris mendacii et mendacissima membra diaboli. Et sic necesse est iuxta propheciam scripture ut pervertantur mendacio et ypocrisi singuli non electi. Tales autem, ut docet Augustinus in libro De Vita Christiana, non sunt veraciter christiani.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 126.14: A difficulty: Whether before the incarnation the Word was the man Christ Jesus. Yes; for he was so both ideally and potentially.
- 126.24: Confirmation: In the three days the body to which he was afterwards united was his.
- 127.1: Confirmation: Otherwise the Church must have been headless.
- 127.10: Reply. The fathers of the O. T. believed in the incarnation,
- 127.19: so far that Christ would be man in due time.
- 128.1: We must be careful to distinguish between potential and actual being.
- 128.10: Christ assumed the human body with the soul. He had the soul in the three days but not in O. T. times.
- 128.18: The Church would not be headless, for the word was always its head, but in another way since the incarnation.
- 129.12: Objection: We should not know to whom to pay honour or even debt.
- 129.18: Answer: As to honouring prelates we must judge them by their works.
- 129.25: Prevailing abuses.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 126: *incarnacionem* (print has incarnacionem) [NW]
  - 126: *conficeret* [R3]
  - 126: *Christi* [R3]
  - 127: *cum* (146a folio mark) [R3]
  - 127: *Christus* [R3]
  - 127: *Christus* [R3]
  - 127: *Christus* [R3]
  - 127: *signo* [R4]
  - 127: *Christus* [R3]
  - 127: *Christus* [R3]
  - 127: *Christi* [R3]
  - 128: *con-* (con-/cedendo hyphenated; main token holds first half (b is the margin alinea letter)) [R3]
  - 128: *Christi* [R3]
  - 128: *eadem* [R4]
  - 129: *III°* [R4]
  - 128: *permansit* (per- here, 146b mansit at top of p.129; main token holds whole word) [THIN]
  - 130: *nimis* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 126:
1. A in marg. : Conclusio. 4. A: est (in red ink) suam est caput.
7. B: quandam primiciam. 14. Ainmarg.: Secunda difficultas. Utrum
verbum est homo Christus Jesus ante incarnacionem. B in marg. man.
rec: Ante incarnacionem verbum est homo Christus Jesus. 21. B:
missa. 32. B in marg. man. rec: In triduo.

p. 127:
io. A in marg. : Responsio. i5. A A,: deus deest. i5. B:
resurgunt.
2h. Ep. Pauli ad Hebr. VII, 5. 27. Anselmi, De conceptu
virginali et originali peccato cap. XI. (Opp. ed. Gerberon, pag. 101.)

p. 128:
1. B: Concedit. 5. B: esse in persona. 16. In cod. A,
spec"ra ; A B: speculum. 29. A in marg. : Tercia difficultas.

p. 129:
6. A: ad corrumpcionem. 6. A in marg. : Nota. 12. A in
marg. : Quinta obieccio 18. A in marg. : Responsio. 20. A in
marg. : Nota processum. 22. B: attendat deest. 25. A in
raarg. : Is. Illa. 29. A At : sunt deest. 3i. A in marg. :
Avaricia cleri.

p. 130:
1. Sumus in codd. Correxi. 8. B:extorqucnt ut vocentur. 9. Ain
marg. : papa. 3o. B: quod sint. 3l. A in marg. : Lljst. XL.
Hic nota contra sanctitatem pape.
16. cap. VI, comp. Aug. Opp. Append. in tom. VI, pag. 186.
3i. Decr. I pars, dist. XL, cap. II: Non est facile.
```

---

## Chunk 06-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "130.18–133.25"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 5 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "785 words; 713 unanimous or majority-real; 61 settled by vote (R2 32, R3a 26, R3b 2, R5a 1); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n167–n170 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 5: [TITLE]

## ¶1 · 130.18–131.28

> [p. 130] Unde si quis zelans pro profectu sancte matris ecclesie, habens in animo scintillam virtutis constancie, posset dicere quod tyriaca est contra exactores huiusmodi, extorquentes sine recompensa plus debita bona pauperum sancte matris ecclesie ex titulo quod sunt membra principalia eiusdem matris sine macula vel ruga, qui possunt temptacionibus et tribulacionibus adversancium concuti sed non superari a membris diaboli vel submergi, ut dicunt iura canonica de sancta matre ecclesia: ideo ex ore proprio debent potentes mundi ab eis requirere quod ostendant secundum eadem iura procuratorium sufficiens in fructu operis quod sunt illi quibus bona sancte matris ecclesie sunt debita vel donata, quia dist. XLª scribitur: Non sanctorum filii sunt qui tenent loca sanctorum, sed [p. 131] qui exercent opera eorum. Et ista tyriaca obtunderet cauterium rubiginosum diaboli quod non gracia sanacionis sed gracia spoliacionis apponitur membris Christi. Conceditur ergo quod tam honor quam stipendium sunt impendenda Christi sacerdotibus, sed oportet eos ex operibus dare probabilem evidenciam quod sunt tales, cum nemo contra conscienciam daret bona sancte matris ecclesie membris diaboli; nam secundum leges humanas qui dat pseudoprocuratori debitum creditoris, tenetur in penam negligencie, et si perdiderit datum creditori tribuere quod est suum. Multo plus creditor matris sue, et specialiter si negligit discernere utrum exactor sit fidelis procurator sancte matris ecclesie, quod iudicabit secundum opera et regulas scripture. Nam liquido constat fidelibus quod decime, oblaciones et alie private elemosine debentur sancte matri ecclesie. Qua fronte ergo excomunicaret infructuosus operibus evangelicis subiectos simplices, nisi dent sibi bona sancte matris ecclesie, cum sit evidens ipsum non esse de illa, sed in illa, tamquam eius hostem precipuum et ypocrisi atque mendaciis eius infidelissimum proditorem. De isto inferius. Sexto arguitur contra dicta in racione secunda; videtur enim, si Christus desponsavit matrem ecclesiam cuius fuit filius, quod filius foret senior matre sua, sicut est honorabilior, melior et formalior quam est illa, et sic ydemptificaret sibi omne membrum ecclesie (ut sepe innuitur in sanctis doctoribus et scriptura).

[ENGLISH]

## ¶2 · 131.29–132.29

> [p. 131] Hic dicitur quod Christus desponsavit matrem suam que est totalis ecclesia non secundum se totam, sed secundum synagogam ex qua Christus secundum carnem prodiit, et sic reliquit patrem et matrem (ut sancti doctores exponunt dictum suum Matthei XIX°, 5) [p. 132] et adhesit uxori sue, sed illud dictum oportet sane intelligi. Nam Christus assumens illud quod prius non erat non perdidit vel desiit esse illud quod erat, quia manet absolute necessario eternaliter plenus Deus, sed reliquit assumendo humanitatem esse solum Deus, cum fuit humanitas que est aliud quam deitas. Et sic ubi prius fuit summe beatus cum patre stante illa beatitudine cum patre assumpsit miseriam fraternam condicionis humane, et sic reliquit matrem synagogam, non deserendo membra predestinata in veteri testamento, sed cum eis assumendo ecclesiam gencium, (ut docet Apostolus Romanorum IX°, 24). Verumptamen multos carnaliter Iudeos reliquit tamquam ineptos ad fabricam sancte matris ecclesie et secundum dotem novam adhesit uxori sue que fit plurimum ex gentibus, et sic honorat matrem ecclesiam tamquam ipso priorem et superiorem eo quod est duarum naturarum creatarum utraque. Et secundum corpus erat subditus parentibus suis carnalibus, ergo multo magis parentibus suis spiritualibus, hoc est, sibi et sancte matri ecclesie. Sicut enim tam secundum corpus quam animam erat subditus trinitati, sic secundum corpus erat subditus sibi secundum animam. Verumptamem videtur quod non sit senior quam universalis ecclesia sed econtra, cum ipsa sit coetanea cum mundo et senium dicit rei mortalis periodum naturalem. Sed est antiquior quam creatura alia, cum sit antiquus dierum, et sic est honorabilior et melior quam mater ecclesia, proporcionaliter ut deitas excedit creaturam.

[ENGLISH]

## ¶3 · 132.30–133.25

> [p. 132] Sed difficultas est, utrum Christus secundum humanitatem sit forma ecclesie. Et videtur mihi quod sic; nam sicut forma vivmcat et movet corpus ad actus [p. 133] suos, limitans sibi et partibus suis crementum et alia accidentia naturalia, sic se habet nedum divinitas Christi extrinsecus sed humanitas eius intrinsecus ad sanctam matrem ecclesiam; unde blasphemum est cogitare quod subest potestati humane posse celebrare divorcium inter Christum et matrem suam, sicut carnaliter ymaginamur de defectu in carnali coniugio. Ecclesia enim est virgo spiritualiter intelligendo sicut tota multitudo celestium civium agnum sequencium (ut dicitur Apocalyps. XIV°, 1), unde tales virgines possunt post corrupcionem recuperare virginitatem, sicut non contingit de virginitate carnali, quamvis semper possunt esse virgines. Nam eo ipso, quo predestinatus habet celibatum, recipiens a sponso ecclesie semen fidei, gignendo filium Dei, est virgo, sponsa Christi, et per consequens, soror et frater eius germanus, et per idem, mater eius, cum gignit Christum spiritualiter ex semine sponsi in anima conversa ad Christum. Et istam materiam pulchre tangit decretum ex doctrina Augustini, ut patet XXVII q. prima: Nupciarum, ubi dicitur quod ecclesia tota virgo est, cum Apostolus IIª. Corinthiorum XI°, 2 dicit: Aptavi vos uni viro virginem castam exhibere Christo. Et ab illo viro cum vivit perpetuo, non licet recedere spiritualiter fornicando, ideo coniugatus manet spiritualiter virgo. Sed

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 130.18: A cure is wanted for the evils of extortion which infest the Church.
- 131.9: We ought to see that we pay dues only to those who claim them rightly.
- 131.23: Objection: If Christ was a son of the Church he was older than his mother.
- 131.29: Answer: His mother was the Synagogue,
- 132.9: which he left for the "Church of the Gentiles''.
- 132.30: Christ's humanity is the form (i. e. the organic principle) of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 130: *matris* (N is alinea letter) [R4]
  - 130: *XLª* [R4]
  - 131: *filius* [R3]
  - 131: *melior* [R4]
  - 131: *formalior* (print has formalior) [NW]
  - 132: *huma-* (huma-/nitatem hyphenated; main token holds first half (P is alinea letter)) [R3]
  - 133: *IIª* [R4]
  - 132: *∅* (second half of huma-nitatem; JOIN onto 225 huma- -> humanitatem) [DELX]
  - 132: *humanitatem* (print: huma-/nitatem (agent 13); scan split) [OVERRIDE]
  - 132: *∅* (margin mark) [OVERRIDE]
  - 132: *∅* (joined at 225) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 130:
1. Sumus in codd. Correxi. 8. B:extorqucnt ut vocentur. 9. Ain
marg. : papa. 3o. B: quod sint. 3l. A in marg. : Lljst. XL.
Hic nota contra sanctitatem pape.
16. cap. VI, comp. Aug. Opp. Append. in tom. VI, pag. 186.
3i. Decr. I pars, dist. XL, cap. II: Non est facile.

p. 131:
12. Creditor; fortasse dcbitor legendum. i3. B: est fidelis. 23. A in
marg.: Scxta obieccio. 25. B: sua decst. 26. A,: formosior pro:
formalior. 29. A in marg.: Nota bcne. Responsio: Christus despon-
savit sibi matrem suam erclcsiam non secundum se totam.

p. 132:
1. 2. A A,: sane intelligere. 3. A in marg.: De incarnacione.
5. A: assummendo. 12. A B: Romanorum; IX. deest; in codd.
lacuna. 25. B: ut ita sit. 27. A in marg. : Differencia inter
senium et antiquitatem. 3o. B in marg. man. rec. : Utrum Christus
secundtim humanitatem sit forma ecclesie. A in marg. : Dubium.

p. 133:
7. A in marg. : Sponsa Christi. 14. B: sponso semen fidei
gignendi. 21. A B: II Cor. X. A in marg. ccrr. Cor. XI. 24. 25. B:
idem coniugatus. 26. A in marg.: Dubium. A B in marg. : TJtrum
Christus et quodlibet membrum ecclesie sit eadem ecclesia in (A : deest)
numero (B manu rec). 3o. B: anima deest.
19. Decr. II. pars, causa XXVII, q. I, c. XLI]
```
