# Translation brief: ecclesia 01-e–01-h

You translate these 4 chunk(s) of Wyclif's *Tractatus de ecclesia* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-01-e.md chunks/ecclesia/wyc-ecclesia-01-f.md chunks/ecclesia/wyc-ecclesia-01-g.md chunks/ecclesia/wyc-ecclesia-01-h.md` once and fix what it reports.
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
  smooth nonsense into sense. Report every such case. Open flags for this volume:
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

## Glossary (the 108 rows these chunks use; the full file is GLOSSARY.md)

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
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
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
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis | necessity of supposition | Conditional necessity. Pilot (*Eccl.* 3.21). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 01-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "14.17–16.34"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "551 words; 509 unanimous or majority-real; 37 settled by vote (R2 20, R3a 8, R5a 7, R6a 2); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n51–n53 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 5: [TITLE]

## ¶1 · 14.17–15.16

> [p. 14] Quinta conclusio est ista: Subesse Romano pon-i, tifici omni humane nature est de necessitate salutis. Patet ex hoc quod nemo potest salvari, nisi meritorie subsit Christo; sed ipse est Romanus pontifex sicut est caput universalis ac cuiuslibet particularis ecclesie: ergo conclusio. Nam columba dicitur modo viatrix, quia secundum partem, igitur per idem: ipsa est Romana ecclesia, quia secundum partem. Non enim est racio, quare ipsa modo peregrinatur vel tribulatur nisi quod secundum partem. Et per idem ipsa inhabitat Romam, Angliam et quemcunque locum fidelem» Nam si ubicunque papa fuerit, ibi est Romana ecclesia, quia eadem ecclesia que Rome edificatur [p. 15] per apostolos succedens ex quibuscunque fidelibus, per idem ecclesia Romana sic est in Anglia et ubicunque fuerit fidelis christianus, quia sancta ecclesia catholica; que non potest stringi secundum se totam in Roma vel cetu pape et cardinalium; sed distenditur per tria loca sancta, scilicet celum, locum peregrinacionis et purgatorium. Unde nimis erronee concipiunt qui fingunt quod ubicunque fuerit dominus papa, ibi est Roma, quia superflue equivocaretur in nomine civitatis, sicut pueri vocant Oxonie Romam monticulum Belli Montis; sed ubicunque dominus papa fuerit, ibi est ecclesia Romana, sicut fuit Jerusalem tempore Christi, in Constantinopoli tempore sinodi, ut patet XXII dist. Sacrosancta, in Antiochia tempore cathedracionis sancti Petri et post in Roma tempore predicacionis et passionis Petri et Pauli.

[ENGLISH]

## ¶2 · 15.17–16.34

> [p. 15] Et sic intelligitur dictum pape post Luce XI°, 20. Profecto pervenit in vos regnum dei et illud Luce XVII°, 22: Regnum dei intra vos est; ubicunque enim fuerit corpus, illic congregabuntur aquile. Quamvis enim ecclesia cepit a Judea et Christus caput ecclesie i3o"fuit martirizatus in Jerusalem, tamen racionabiliter vocata est ecclesia Christi secundum quandam preeminenciam propter tria: Primo quia Christus scivit gentes sub Romano imperio loco Judeorum infideliter discredencium inserendas, sicut dixit apostolus Rom. XI°, 23. Secunda causa est, quia maior multitudo mar2tirum ibi triumphavit quam in alia civitate; sic enim [p. 16] ubi homo nascitur ex utero et triumphat gloriose, nomen abhinc contrahit. Cum ergo persona universalis ecclesie secundum multas partes suas ibi nascebatur, segregata ex utero synagoge, et ibi triumphavit crescens in gentibus: ideo fuit consonum quod caperet nomen a civitate metropoli gencium que est Roma. Tercia causa est, ut notetur quod non locus sive antiquitas sed fides formata fundet Christi ecclesiam. Nam quoad personam et quoad tempus prius fuit ecclesia Christi in sedibus prioribus et ad sensum istum dicitur II°.Mach.V°, 19, quod non locus gentem sed gens locum sanctificat. Et hinc credo derelictum licere vocare Christi ecclesiam nomine cuiuscunque loci quem fideles inhabitant, sicut Christus vocatur Nazarenus propter concepcionem, et potest catholice vocari David Bethlehemiticus propter nativitatem, et sic de aliis civitatibus que possent licite dici sue propter inhabitacionem vel propter factum aliud notabile vel passionem. be Notando tamen quod vocando ecclesiam quamcunque nomine loci hoc potest intelligi dupliciter, vel appropriate quoad habitacionem illius loci vel secundum partem, et in hoc sunt quotlibet gradus secundum amplitudinem parcium ecclesie. Non enim est bona causa vocare matrem nostram Romanam ecclesiam propter fastum aut complacenciam imperatoris dotantis ecclesiam nec propter extollenciam domini pape pompantis de parte imperii ex suo primatu sive dominio nec tercio, ut credatur quod ad ipsum oportet omnem christianum recurrere et de necessitate salutis ipsum capitalem recognoscere, sed propter causas topicas supradictas. Cum enim Romana ecclesia sit terminus institutus preter fundacionem in scriptura sacra, satis est habere racionem probabilem cavendo semper de deduccione perfida.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 14.17: Fifth conclusion. Submission to the Pope is necessary to Salvation.
- 14.26: As, wherever the Pope is, there is the Roman Church: so wherever is one of the faithful, there too is the Roman Church.
- 15.11: Local name at Oxford.
- 15.23: For three reasons the Church of Christ is called the Romish Church.
- 16.19: We must be careful how we use local names for the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 14: *tifici* (second half of pon-/tifici hyphenated across line (pon- is pos 118)) [R4]
  - 15: *dominus* ('Local' is side-note text glued) [R4]
  - 15: *Christus* [R3]
  - 15: *Romano* (leading 1 is margin line-number fragment) [R4]
  - 16: *Christi* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 14:
4. A in marg: Octo casus in quibus ecclesiasticus subditur iudicio vcl
correccioni seculari. B in marg: Johannes de Dco. Octo casus in quibus
ecclesiasticus subicitur iudicio seculari i Ecclcsiast. 4, 1, 6, 7, 8 (sic). 8. B :
tercio quando. 12. B: cum principes. ly.ABinmarg: Quinta con-
clusio. 22. B: igitur conclusio. AA,: igitur — partem deest. 27.Ain
marg: Sicut ubicunque est papa, ibi est ecclesia Romana : sic ubicunque
cst lidelis, eciam est ecclesia Romana. 29. B: quia — ecclesia deest.
4. As to Johannes de Deo, a Spanish theologian and pro-
fessor of Divinity in Bologna see Trial. ed. Lechler, pag. 25 1.
18. See Decret. Unam sanctam; cf. pag. 9, I. 20.

p. 15:
2. Binmarg: Probat ecclesiam Romanam esse ecclesiam universalem
aut catholicam. 7. A: errone; B: erronie. B in marg: purgatorium.
14- B. in marg: 22" distinccione. 17. In codd. Matth. XII. Correxi ; B in
marg: Matth. 12. 18. B: Luce 17 deest. 20. B in marg: Quomodo
capit ecclesiam dicens a Judea incepisse est: incepit ab Abel, ut scntit
bcatus Gregorius. 23. A in marg: Propter tres causas ecclesia Christi
vocata est Romana ecclesia (Above col. i3o°). B in marg: Nota quare
ecclesia vocata est Romana ecclesia. 26. In codd: Rom. IX.
I i.BellusMons isReaumont, a royal palace new destroyed, in the
North Suhurbs of Oxford; see Wood's History of the City of Oxford
(ed. Sir J. PeshaU, pag. 3 r t). 14. Decr.prima pars dist. XXII, cap. II.

p. 16:
2. B: ad nomen. n. B in marg: Machabeorum. 12. dereliclum ;
sic in codd. and in Hus, de ecclesia, Opp. tom. I, Fol. 208" . 25. B :
excellenciam. 28. B: nec cstimo ut. I14. B: de seduccione perlida.
```

---

## Chunk 01-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "17.1–20.17"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "875 words; 806 unanimous or majority-real; 51 settled by vote (DEL 1, R2 29, R3a 13, R5a 7, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n54–n57 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 6: [TITLE]

## ¶1 · 17.1–19.9

> [p. 17] Ex istis colligitur, cum solus Christus sit caput tocius ecclesie que non est pars ad aliam iuxta primam conclusionem, oportet concedere quod sicut nullus christianus debet presumere se esse caput universalis ecclesie, sic nec debet sine timore et sine speciali revelacione asserere quod sit caput cuiuscunque particularis ecclesie. Prima pars patet ex conclusione prima; si enim quis sit caput talis universalis ecclesie, tunc est melior angelis effectus, ymmo omni beato spiritu creato, quod soli Christo potest competere secundum apostolum Heb. 1°, 4. Oportet enim ipsum esse primogenitum ex multis fratribus, et per consequens, capitaneum ex dignitate iuris primogeniture. Unde si aliquis christianus foret cum eo caput universalis ecclesie, cum ipsa non potest esse monstrum, habens ex equo duo capita, ut dicit secunda conclusio, oporteret concedere quod est Christus, vel aliter quod Christus foret ipso inferior et humile membrum eius. Ideo apostoli confessi sunt concorditer se esse servos istius capitis et humiles ministros ecclesie sponse sue, nunquam autem presumpsit aliquis apostolorum asserere quod fuit caput vel sponsus dicte ecclesie, quia hoc foret antichristiane adulterari cum regina celi, zelotipando dominum Jesum Christum; quod foret nimis grave, cum Exodi XX°, 5, vere dicitur quod ipse sit fortis zelotes Et secunda pars patet ex hoc quod caput est nomen dignitatis atque officii dignitatis quoad predestinacionem eternam, qua Christus ordinavit prepositos (qui presunt secundum legem suam in ecclesia militante) habere mansiones superiores racione sui regiminis in ecclesia triumphante, quia si prepositi omnino deficiant ab officio ministrandi subditis sensum scripture [p. 18] et motum ad sequendum caput ecclesie, tunc non sunt caput in civitate Dei, sed in civitate diaboli capitis perimendi, quia Sap. VI°, 6, vere dicitur: Durum iudicium hiis qui presunt fiet. Cum ergo nos miseri ignoramus si sumus ad celestem Jerusalem predestinati, (quod tamen ex speciali revelacione habuerunt sancti) patet quod nimia presumpcio foret nobis pertinaciter asserere quod sumus capita cuiuscunque particularis ecclesie que foret pars sancte matris ecclesie, quia notum est ex concordi testimonio sanctorum quod nullus prescitus est vel membrum ipsius ecclesie. Quomodo ergo presumeret aliquis nostrum asserere quod sit caput, cum Eccl. IX°, 1, vere dicitur quod nemo talis scit, utrum sit dignus amore vel odio quoad predestinacionem vel reprobacionem. Insuper si respicimus ad sensum et motum quos in subditos influimus et ex alio latere ad speculum scripture iuxta quam totam vitam nostram regularemus, eligeremus pocius vocari servi et ministri ecclesie quam capita, cum notum sit, si non facimus officium capitatis, non sumus capita, quia secundum Augustinum in libello suo De Decem Cordis maritus perversus non est caput uxoris sue, multo magis prepositus ecclesie qui pure haberet a Deo dignitatem huiusmodi, si a Christo degenerat. Unde postquam Augustinus ostenderat quod femina vere christiana debet dolere de fornicacione viri non propter carnem sed propter caritatem et castitatem debitam viro Christo, dicit consequenter quod Christus loquitur in cordibus feminarum bonarum, ubi vir non audit dicens: Dole de viri tui iniuriis sed noli imitari, quin pocius ipse te imitetur in bono. Nam [p. 19] in eo quod male facit noli eum putare caput tuum sed me Deum tuum. Et probat hoc debere fieri. Si inquit in hoc quod male facit caput est, et consecuturum est corpus caput suum, eunt ambo in precipucium. Ut autem christianus non sequatur malum caput suum, teneat se ad caput ecclesie Christum, huic debens castitatem suam, huic deferens honorem suum, absens sit vir privatus, presens sit vir matri ecclesie coniugatus.

[ENGLISH]

## ¶2 · 19.10–19.30

> [p. 19] Patet ergo quod, sicut infinitum maiorem honorem debemus patri spirituali domino Jesu Christo et sponse sue ecclesie que est regina, assistens a dexteris eius (ut diciturPsal.XLIV0, 10) quam alicui parenti nostro carnali, sic nemo est parens vel proles huius celestis coniugii, nisi faciat debitum quod in predestinacione divina est deputatum isti officio. Nam esse caput vel membrum sancte matris ecclesie est inseparabiliter nomen officii. Ex istis septimo sequitur quod dominus papa, si predestinatus est et exercet pastorale officium, est caput tante militantis ecclesie quantam regit, ut si sic regit capitaliter secundum legem Christi totam iam militantem ecclesiam, tunc est eius particularis capitaneus sub archicapite, domino Jesu Christo. Hoc autem debet supponi in domino Romano pontifice, nisi factum doceat evidenter oppositum, cum clerus iam peregrinans consensit in eum ut capitaneum. Verumptamen non est in potestate alicuius christiani constitucione, eleccione vel acceptacione statuere quod dominus papa sit caputvel membrum sancte matris ecclesie. Nam hoc consistit in predestinacione et gracia Dei nostri.

[ENGLISH]

## ¶3 · 19.31–20.17

> [p. 19] In ista vero materia sunt quotlibet subterfugia, ut unus dicit quod nulla mater ecclesia potest esse; sed [p. 20] iste videtur michi infideli deterior, cum nedum negat fidem scripture et fidem ecclesie de credulitate qua oportet christianum credere ecclesiam sanctam catholicam, sed de facto non est filius illius celestis coniugii, sine cuius gignicione non possumus esse filii Dei, et Per consequens, nec heredes regni. Alii autem dicunt quod sancta mater ecclesia est eciam ecclesia, sed non est aliquid, et sic nec mulier nec corpus Christi mysticum nec regina Sed isti; (ut tetjgj alias) debent negare magnam partem fidei scripture, decreta ecclesie Romane et simbolum fidei christiane. Tercii vero dicunt quod universalis ecclesia non est nec erit ante diem iudicii, sed multi fuerunt et multi sunt qui erunt tunc partes eius, sed nec habet nec habuit partes aliquas, eo quod nec est nec fuit, cum tunc foret universitas predestinatorum qui erunt in die iudicii. Quod est impossibile, cum multi eorum sint generandi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 17.1: Sixth conclusion. No Christian should assert that he is head even of a local Church.
- 17.19: None of the apostles called himself head or spouse of the Church.
- 17.26: A Head must be predestinate,
- 18.6: which no one can know himself to be.
- 18.21: Augustine says that a wicked man is not the head of his wife.
- 19.18: Seventh conclusion. The Pope, if he is predestinate and does his pastoral office, is head of so much of the Church, as is under his government.
- 19.31: Some deny that there is a Church;
- 20.6: Others say that there is a Church, but that it is not a thing (i. e. is only a concept);
- 20.11: Others, that the Church will not exist until the day of judgment.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 17: *Christo* [R4]
  - 17: *fortis zelotes* (print has 'fortis zelotes.' at end of line 25 before Et (two words, italic)) [INS?]
  - 18: *motum* [R3]
  - 19: *in* (130b is the folio mark) [R3]
  - 19: *quod* [R3]
  - 19: *precipucium* (precipu-/cium hyphenated across line) [R4]
  - 19: *∅* ('if' is the side-note (if he is predestinate), not main text) [R6]
  - 19: *Christi* [R3]
  - 19: *iam* (i with dot, not l) [NW]
  - 19: *ut* ('Some' is side-note text) [R4]
  - 19: *unus* (leading a is the margin letter) [NW]
  - 20: *negat* (130c is the folio mark) [R3]
  - 20: *dicunt* (trailing b is the margin letter) [NW]
  - 20: *regina* [THIN]
  - 20: *Sed* [THIN]
  - 20: *isti* [THIN]
  - 20: *sed* [R3]
  - 20: *iudicii,* [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 17:
1. Codd. in marg. Sexta conclusio. 2. B: primam questionem; ita et
7 (questione pro conclusione) et seqq. 9. AA, omnino beato. n. B in
marg: Heb. i°. n. AB: esse deest. 19. A in marg: Nullus papa
debet presumere se esse caput ecclesie (above i3ob without mark of
reference). 23. Codd.: antichristine. 25. B: Exodi XX, 5 dicitur;
et in marg : Exodi 20 V° (pro vere). 3o. A: sue regiminis.

p. 18:
2.B: capitatis perimendi. 3.Binmarg: Sap.VI. 4. B: cum igitur;
sic et in pluribus locis sequentibus eiusdcm codicis. 6. B: quantum
cx speciali. 9— 11. AA,: ecclesie — membrum decst. i3. B in marg:
Eccl. IX0. 19. B: capitis. 21. A B in marg: Augustinus. A in marg:
Vir perversus non est caput uxoris nec est per ipsam imitandus. B in marg:
Maritus perversus non est caput uxoris. 25. B in marg: Augustinus.
22. Capp. III et IX. Aug. Opp. V, 1, 5o, 5G.

p. 19:
4. B: tum ambo. B in marg: Non est imitandus malus prelatus nec est
obediendum ei in hoc quod male facit. 7. B: hinc debens. i3. B
in marg: Ps. 44. 18. AB in marg: Septima conclusio; A in marg:
Papa si est predestinatus et exercet pastorale oflicium, est caput tante
ccclesie quantam regit (abovc u<o'' without mark of referencc). 3r. A
in marg: Contra illos qui negant ecclesiam esse.

p. 20:
3. B : igitur oportet. 6. B: autem deest. 8. B: aliquis. 12. B:
nunc non est. i3. A: culti sunt. 21. B in marg: Eph. V". 32. A in
marg: Omnes clecti qui sunt ccclesia sunt una persona (above i3o'' without
marl; of rcference).
```

---

## Chunk 01-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "20.18–22.5"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "377 words; 342 unanimous or majority-real; 26 settled by vote (R2 15, R3a 7, R3b 1, R5a 3); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n57–n59 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 7: [TITLE]

## ¶1 · 20.18–22.5

> [p. 20] Sed oportet sic opinantes negare maiorem partem scripture sacre et specialiter magnum sacramentum de Christo atque ecclesia de quo loquitur apostolus Ephesiis V°, 32. Immo oportet sic loquentem negare omnem particularem ecclesiam, cum particulare non dicitur nisi in comparacione ad totale et universale. Ideo negata universali et totali ecclesia neganda foret quelibet particularis ecclesia, vel aliter dicendum foret quod Deus cognoscit mille universales ecclesias: quod esset summe hereticum, quia nedum sentiret contra ecclesiam sed omnino destrueret ecclesiam et singulas leges eius. Sic ergo error in logica scripture quem diabolus introducit ad cecandum mentes fidelium, facit filios eius prorumpere in conclusiones multas blasphemas ex quibus mater ecclesia perturbatur. Nam sancti doctores dicunt concorditer quod omnes electi a principio mundi usque ad diem iudicii sunt una [p. 21] persona que est mater ecclesia, ut patet per beatum Gregorium XXIII° Moralium primo capitulo supra Job XIX°, 25, Scio quod redemptor meus vivit. Sciendum inquit quod redemptor noster unam personam se cum sua ecclesia quam assumpsit exhibuit. De ipso enim dicitur: Qui est caput Christus. Rursumque de eius ecclesia scriptum est: Et corpus Christi quod est ecclesia. Et sequitur: Quod Christum inquit, et ecclesiam unam personam credimus, hoc eciam unius persone actibus significari videamus. Et idem dicit XIX° Moralium cap. IX et IV° Moralium cap. IX. De illa siquidem ecclesia cuius Christus est caput (secundum testimonium huius sancti pape) suppono quod fiat nobis sermo. Et patet quod, si christianus foret caput illius ecclesie, tunc vel haberet multa capita quod negat decretalis, vel aliter christianus foret Christo superior. Non enim est color quod quilibet qui est caput partis ecclesie sit caput illius ecclesie, quia tunc nedum dominus papa sed quilibet uxoratus et omne caput bestie foret caput ecclesie, et sic (ut sophiste concedunt) ecclesia haberet monstruosissime caput et membra quotlibet asinina; quod foret nimis sophisticum. Videamus ergo racionem secundum quam Christus dicetur singulariter caput tocius sponse sue post diem iudicii, et patebit luce clarius quod nemo alius potest esse caput illius ecclesie. Sed obicitur per dominum Ardmacanum libro VII°, De Questionibus Armenorum cap. VI, ubi videtur tenere quod idem corpus habet multa capita subordinata, [p. 22] sicut idem populus habet multos dominos, unum subordinatum alteri (sicut patet in materia civili). Et sic videtur dicere quod eadem ecclesia habet multa capita ordinata secundum inferius atque superius.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 20.32: All the elect are one person and that is the Church.
- 21.2: Gregory.
- 21.14: If a Christian could be head of the Church he would be above Christ.
- 21.27: Objection made by Armachanus;
- 22.1: One head may be subordinate to another.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 20: *a* (print: 'electi a principio mundi'; the a stands before principio) [INS?]
  - 20: *principio* (box word is principio (read with 9.1 a / 9.3 ∅ = 'a principio mundi')) [R4]
  - 20: *∅* (nothing between principio and mundi; principio is pos 256) [INS?]
  - 21: *persona* (130d is the folio mark) [R3]
  - 21: *Qui* [R4]
  - 21: *Quod* [R3]
  - 21: *unam* [R3]
  - 20: *iudicii* [THIN]
  - 20: *V°, 32.* (print has verse 32 after chapter (confirmed on leaf n0057)) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 20:
3. B : igitur oportet. 6. B: autem deest. 8. B: aliquis. 12. B:
nunc non est. i3. A: culti sunt. 21. B in marg: Eph. V". 32. A in
marg: Omnes clecti qui sunt ccclesia sunt una persona (above i3o'' without
marl; of rcference).

p. 21:
2. AB in marg: Grcgorius. 4. B in marg: Ecclesia est persona.
5. B in marg: Quomodo Christus assumpsit ecclesiam, tunc (cui?) est una
pcrsona. 5. Codd. cum sua; recte: sancta. 8. B: qui est. 12. B in
marg: Gregorius. 27. A B in marg: Obieccio. Ardmacanus. A in
marg: Contra dicta.
2. Moral. XXIII. Cap. I. Opp. (ed. Maur.) tom. I, 7 3 1 . 27. On
Richard Fitz Ralph, Chancellor of the University of Oxford in 1 3 33,
Archbishop of Armagh, cf. Wyclifs Polemical Works I, qt, cf.
Cod. palat. Vindob. 41 27, fol. i"— zio". De erroribus Armenorum.

p. 22:
1. B: multos deest. 6. A in marg: Responsio. Notatur de capiti-
bus ecclesie. 8. A: deitatem. 12. i3. A: deitas. 9. B in marg:
Divinitas ecclesie universalis est caput extrinsecum, humanitas Christi in-
trinsecum eius est caput. i3. B: eciam deest. i5. A in marg: Duo
sunt paracliti in divinis. 16. B: principative et cum. 18. Binmarg:
Joh. 14. 22. B in marg: Sanctus Petrus ecclcsie presidebat.
24. Moral. XIX, cap. XII. Opp. tom. I, 61 3.
```

---

## Chunk 01-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "22.6–25.22"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "821 words; 751 unanimous or majority-real; 61 settled by vote (R2 38, R3a 17, R5a 5, R6a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n59–n62 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 8: [TITLE]

## ¶1 · 22.6–25.22

> [p. 22] Hic dicitur quod idem corpus ecclesie habet multa capita, ut quelibet particularis ecclesia habet ad minimum tria capita, scilicet divinitatem, Christi humanitatem et capitaneum illius ecclesie. Ecclesia autem universalis que est totum corpus Christi misticum habet duo capita, scilicet caput extrinsecum que est divinitas et caput intrinsecum que est Christi humanitas, et modo ineffabili divinitas et humanitas Christi sunt duo capita tocius ecclesie et cum hoc eciam unum caput: Sicut filius et spiritus sanctus sunt unus paraclitus, intelligendo principative vel essencialiter, et tamen sunt duo paracliti, intelligendo personaliter (cum Joh. XIV°, 16 dicitur: Ego rogabo patrem et alium paraclitum dabit vobis): sic iste due nature sunt duo capita ecclesie, et tamen sunt personaliter unum caput. Particulares autem ecclesie, sicut fuit pusillus grex cui presidebat sanctus Petrus, non erant nisi iuvencule tocius matris ecclesie, sicut exponit Gregorius XIX° Moralium cap. VIII, declarans etatem ecclesie quomodo in principio fuit soror parvula, carens uberibus predicacionis. Unde sic infert: Universe quippe ecclesie que unam catholicam faciunt adolescentule vocantur. Unde beatum Petrum et alias particulares ecclesias vocat membra illius ecclesie quam leenam nominat, Christum vero leonem (ut [p. 23] declarat XXVIII° Moralium cap. XI), dicens quod, sicut membra corporis non sunt ipsum corpus, sic particulares ecclesie non sunt illa sancta ecclesia, sed (ut docet apostolus i° Cor. XII, 12) membra eius. Istis positis dico quod nec dominus Ardmacanus nec aliquis doctor catholicus debet asserere quod aliquis christianus sit caput universalis sed particularis ecclesie, cum non sit color: Hoc caput est illius ecclesie, ergo hoc est caput illius ecclesie; nec est color: Si hoc est caput partis illius ecclesie, ergo hoc est caput illius ecclesie. Sic enim omnis vir foret caput Dei, sicut omnis prelatus inferior foret caput sue matricis ecclesie. Sed apostolus contradicit istis arguciis, I° Cor. XI, 3, dicens: Volo autem vos scire quod omnis viri caput est Christus, caput autem mulieris vir, caput vero Christi Deus. In quo dicto patet ordo capitum et deteccio illarum fallaciarum. Quia aliter eque diceret econtra quod caput Christi et Dei foret tam vir quam mulier. Ecclesia itaque catholica, secundum beatum Gregorium super illo Matthei XXIII°, 34: Ecce mitto ad vos sapientes et scribas, est vinea domini plantata a principio mundi usque ad finem fructificans, quotquot sanctos gignit tot palmites producit. Et sicut nemo est naturaliter caput matris sue sed pars nisi Christus: sic nullus aliorum sanctorum est caput matris ecclesie sed membrum. Sic enim dicit beatus Gregorius (ubi supra) quod beatus Job, beatus Petrus et ceteri precones matris ecclesie sunt os eius, et breviter, quilibet [p. 24] aliorum sanctorum proporcionaliter ad analogiam virtutis sue et proprietatis membri corporalis est pars sancte matris ecclesie. Unde beatus Gregorius IV° Moralium cap. XXXII narrat quomodo a principio mundi Deus ordinavit sponse sue patriarchas secundum virtutum principia tamquam membra radicalia ecclesie inserenda, ut patet de innocencia Abel, de mundicia Enoch, de castimonia coniugali Isaac, de tolerancia Jacob, de spe Noe, de obediencia Abrahe, de paciencia Job, de castitate Joseph, de mansuetudine Moysi, de fiducia Josue, de humilitate David, de zelo Helye, et sic discurrendo per omnes species virtutum; que secundum etatem seculi habuerunt in excessu notabili aliquos patriarchas eorum principia in quorum labores sponsus ordinavit posteros intrare (ut dicitur Johannis IV°). Nec solum isti sed omnes eorum imitacionis filii sunt eadem membra sancte matris ecclesie quod, si alicui desit virtutis officium, deerit sibi indubie quod sit sancte matris ecclesie membrum. Nullus autem eorum unquam presumpsit dicere quod sit caput et dominus matris sue, quia indubie, si aliquis homo sit caput tocius generis christiani (quod est sancta mater ecclesia), tunc ipse est Christus, quia solus Christus est huius generacionis principium; alii autem in ipso sunt palmites. Necesse ergo est hodie seminare istam fidem ecclesie, cum multi ex ignorancia occasione male accepta, dormiendo in nocte ignorancie uruntur a sancta matre ecclesia que est pulchra ut luna. Uruntur dico secundum inferiorem hominem pravitate heretica, quia omnes qui dicunt: Ecce hic, et ecce illic est Christus caput ecclesie, solum eius vicarium demonstrantes. [p. 25] Oportet autem volentes proficere vel iudicare in ista materia primo cognoscere quiditatem sancte matris ecclesie ad modum loquendi scripture sacre et sanctorum qui sensum eius elucidant. Oportet secundo cognoscere materiam predestinacionis divine, quanto sit nobis incognita. Et tunc tercio possunt discernere, si sit sanum vel stolidum quod asseramus absque formidine nos esse membra sancte matris ecclesie, hoc est, de numero predestinatorum. Debemus autem hoc sperare et credere sed cum formidine de gracia perseverancie: ideo talis fides habet formidinem annexam quam non habet fides qua credimus nos esse in gracia secundum presentem iusticiam, cum casus futuri sit nobis incercior quam actus caritatis vel habitus pro presenti. Unde gentilitati inserte loco Judeorum in ecclesia dicit apostolus Rom. XI°, 20. Noli altum sapere, sed time. Timor ergo de casu a finali perseverancia stat cum spe, et cum caritas secundum presentem iusticiam foras mittit timorem de peccato habito pro presenti, videtur tamen quod omnis homo debet habere pro suo tempore specialem revelacionem, quia aliter non foret in firma spe excuciente omnem timorem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 22.9: The Church has two heads, Christ's divinity and his humanity;
- 22.15: as there are two Paracletes,
- 22.17: and yet one.
- 23.1: No local Church is the great universal Church.
- 23.21: Gregory.
- 23.22: What the Church is.
- 23.27: The Saints are only members of holy Church, not heads.
- 24.3: Gregory.
- 24.5: Different virtues were specially displayed in different patriarchs,
- 24.19: yet none of them presumed to call himself head of the Church.
- 25.1: We should know,
- 25.2: a. what is the quidity of the Church; b. our ignorance as to what God has predestined;
- 25.8: c. to believe ourselves predestined without venturing to assert it.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 22: *Christi* [R3]
  - 22: *16* [R3]
  - 23: *declarat* (131a is the folio mark) [R3]
  - 23: *I°* [R3]
  - 23: *Christi* [R3]
  - 24: *dominus* [R3]
  - 24: *Christus* [R3]
  - 24: *Christus* [R3]
  - 25: *Rom. XI°* (token spans 'Rom. XI°' (tight space); degree sign present) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 22:
1. B: multos deest. 6. A in marg: Responsio. Notatur de capiti-
bus ecclesie. 8. A: deitatem. 12. i3. A: deitas. 9. B in marg:
Divinitas ecclesie universalis est caput extrinsecum, humanitas Christi in-
trinsecum eius est caput. i3. B: eciam deest. i5. A in marg: Duo
sunt paracliti in divinis. 16. B: principative et cum. 18. Binmarg:
Joh. 14. 22. B in marg: Sanctus Petrus ecclcsie presidebat.
24. Moral. XIX, cap. XII. Opp. tom. I, 61 3.

p. 23:
1. A in marg : 1'articularis ecclesia non est universalis illa magna ecclesia.
B in marg: Ecclesie particulares unam catholicam constituunt. 4. B in
marg: 1 Cor.XII. 7. 8. A: Nec si lioc est caput illius partis ecclesie,
ergo; B: Nec — ecclesie in marg. 14. B in marg: 1 Cor. XI. 10. B
in marg: Econtra. 21. A B in marg: Gregorius. A in marg: Ecclesia
quid est. B in marg: Matth. 23. 27. A in marg: Membra sanctc ecclesie
sponse Christi sunt soltim sancti. B in marg: Gregorius. 29. B: sunt
i.Greg. Moral. XVIII, cap. XXXV; XXVIII, cap. X. Opp. I, 904,
58i. 21. Greg. in Evang Lih. I. Homilia XIX, Opp I. i5io.

p. 24:
3. 1. Mor. cap. X in codd. Correxi. AB in marg: Grcgorius. 6. AB:
secundum deest. 9. 10. AA,: de spe — Job decst. i3. B : quo secun-
dum. 16. Binmarg: Joh. IV". 18 19. B: in dubio. 20. B: prescripsit
dicere. 21. B: in dubio.
3. Greg. Opp. I, 1 32. 3i. Luc. XVII, 23.

p. 25:
1. AB in marg: Triplex epilogus. B in marg: Quero an Christus qui
est caput univcrsalis ecclesie debeat dici mcmhrum eiusdem ecclesie vel
non. 4-A,: qtii secundum sensum. 8.B: membra deest. 9. 10. B:
hoc sapcre. u. B in marg: Fides qua quis credit se esse membrum
ecclesie habct annexam formidinem. Viator habet lidem qua credit quod
est in gracia (secundum) prcscntem iusticiam. 16. B in marg: Rom.XI.
18. B: liat cum spe. 24. A in marg: Contra dicta. Nullus papa ncc
aggregatum ex papis est capud ecclesic (above i3ic ). 26. AA,: tamen ex.
23. Ad cap. I. cf. Hus, De eccl., cap. I — III. Opp. I. Fol. 196" — 199*.
27. Decret Unam sanctam. Extrav. comm. lib. I, tit. VIII, cap. I.
```
