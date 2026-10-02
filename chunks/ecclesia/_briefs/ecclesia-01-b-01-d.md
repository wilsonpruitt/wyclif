# Translation brief: ecclesia 01-b–01-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-01-b.md chunks/ecclesia/wyc-ecclesia-01-c.md chunks/ecclesia/wyc-ecclesia-01-d.md` once and fix what it reports.
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

## Glossary (the 102 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis | necessity of supposition | Conditional necessity. Pilot (*Eccl.* 3.21). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| illabi | to flow into | Ruled 2026-09-28. |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| sciolus | knowing, wise | "smatterer" (the classical sense). Neutral in Wyclif. Pilot (*Eccl.* 5.8) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 01-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "3.14–6.15"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "621 words; 571 unanimous or majority-real; 40 settled by vote (R2 19, R3a 14, R5a 6, R6a 1); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n40–n43 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 2: [TITLE]

## ¶1 · 3.14–6.15

> [p. 3] Hec est sancta ecclesia catholica quam confitentur christiani immediate post fidem in spiritum sanctum propter tria: primo quia secundum Augustinum est summa creatura. Ideo immediate ponitur post trinitatem increatam. Secundo quia amore spiritus sancti Christo in matrimonio perpetuo copulatur. Et tercio quia posita trinitate oportet ipsam habere templum vel domum quam inhabitet. Oportet dico ex necessitate supposicionis atque de congruo. Ista autem ecclesia secundum partem peregrinantem non habet aliquem prescitum partem sui, sicut non [p. 4] habet secundum partem triumphantem, dum est huiusmodi, aliquem miserum vel quomodolibet maculatum, ut ostendit Augustinus, III° de doctrina christiana XXXII°, ubi, postquam ostenderat quod corpus Christi et caput eius Christus sunt una persona, increpat Tyconium in secunda sui regula qua vocat ecclesiam corpus domini bipartitum. Non inquit ita debuit appellare; non enim revera corpus domini est quod cum illo non manebit in eternum. Ideo vocat fideles ad tempus sed prescitos ad dampnacionem ecclesiam similatam. ex ypocritis. Potest autem ista sentencia demonstrari ex scriptura Johannis VI°, 54, ubi dicitur Judeis et per idem cuilibet viatori: Nisi manducaveritis carnem filii hominis et biberitis eius sanguinem, non habebitis vitam in vobis. Sed nemo potest esse membrum corporis Christi, nisi fuerit membrum vivum: ergo nemo potest esse de illo corpore, nisi manducaverit corpus Christi. Quomodo queso potest continuari cum nervis capitis, nisi fide formata in caput crediderit? Quod est ipsum manducare, ut exponit Augustinus omelia XXVª. Habet autem iste cibus contrarie ad cibos corporales virtutem assimilandi sibi manducantem secundum quatuor digestiones, de quibus Rom. VIII°, 3o, scilicet predestinacionem, vocacionem, iustificacionem et glorificacionem. Quamvis enim sic manducans moritur temporaliter, non tamen eternaliter, cum Christus, resurreccio et vita in finali iudicio vivificat omnia membra sua, quia leo rugiens suscitat suam ecclesiam. Caritas autem que nunquam excidit est vinculum [p. 5] continuans membra illius corporis; foret ergo contra racionem, vel quod sponsus in persona propria, vel quod alius ex permissione sua laniaret sponsam suam divisione eterna. Ymmo claudit contradictorium, si bene inspicitur; cum Jeremie XXXI°, 3, sibi dicitur: In caritate perpetua dilexi te. Ista igitur et non lapides est mater nostra per orbem terrarum confitens caput suum. Quomodo queso tam potens, tam sciolus et tam benivolus, sicut est increata trinitas, eternaliter eligeret sibi sponsam quam finaliter repudiaret? Patet ergo ex fide et signacione quid nominis ecclesie catholice quod ipsa est omnes predestinati presentes, preteriti et futuri. Ex istis sequuntur alique conclusiones. Prima, quod nullus vicarius Christi debet presumere asserere se esse caput ecclesie sancte catholice, ymmo nisi habuerit specialem revelacionem, non assereret se esse aliquod membrum eius. Patet ex hoc quod capitalem illius ecclesie oportet esse super omnes angelos beatos, cum ipsi sint membra illius ecclesie, quod soli Christo potest competere inter omnes predestinatos, ut patet Hebr. 1°, 4. Nam Rom. 1°, 4, dicitur Christum esse predestinatum; et sic ecclesia est solum numerUS predestinatorum. Sicut igitur homo sine speciali revelacione non assereret sine formidine se esse predestinatum, sic nec assereret se esse membrum, et per consequens, non caput illius ecclesie. Unde Augustinus super psalmum CXXXI""' postquam ostenderat quod nullum preterquam domum suam exaudit Deus ad vitam eternam: Ille inquit ad domum Dei [p. 6] pertinet qui est in caritate compaginatus lapidibus vivis; qui autem caritatem non habuerit, finalis perseverancie ruinam facit, sed domus stat. Et post docet quod nemo debet ex pretense potestatis vicaria pompare vel minari quod ab eo dependet status ecclesie, sicut fecerunt Judei ex filiacione et merito Abrahe, quia filiis imitacione virtutum et non filiis carnis degenerantibus promittitur hereditas. Et sic est indubie quoad Christi vicarios. Itaque inquit Augustinus in hiis est domus Dei quos predestinavit et prescivit perseveraturos, de quibus dictum est: Ubi steterunt sedes eius. Et hii qui non perseverant, non sunt ipsi ecclesia, non ipsi pertinent ad illud modo tabernaculum et tunc domum, sed solum in hiis qui perseveraverint usque in finem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 3.14: How faith concerning the Church follows immediately on faith concerning the Holy Spirit.
- 3.23: Note. This Holy Church contains none who are reprobate.
- 4.15: The virtue of the sacramental food.
- 5.14: First conclusion. No Pope should presume that he is the Head of this Church.
- 5.23: No one can know whether he is predestinate.
- 5.27: Augustine.
- 6.10: The House of God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 3: *non* (side-note text glued in OCR) [R4]
  - 4: *III°* [R4]
  - 4: *Christi* [R3]
  - 4: *XXVª* [R4]
  - 5: *fide* (f with crossbar, clear) [R3]
  - 5: *nullus* (15 is the line number) [R4]
  - 5: *vicarius* [R3]
  - 6: *pertinet* (first word of line, italic) [R3]
  - 6: *Christi* [R3]
  - 5: *domum* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 3:
1. B in marg. Prov. 3l; ia Cor. 4. B in marg. Aug. 41 Ench. In
codd. XLI. Correxi. 5. AA,: que; B: peregrinat. 10. B in marg:
Nota quod angeli sunt pars ecclesie. 14. A: Qualiter tides de ecclesia
sequitur immediate post fidem de spiritu sancto. B: Nota quare immediate
post fidem in spiritum sanctum p(onitur) iides de sancta matre catholica.
24. AA,in marg: Nota. A in marg: Hec sancta ecclesia non habet presci-
tum partem sui. Continue infra (above the col. 128«=). B in marg: Dicit
ecclesiam catholicam secundum partem triumphantem non habcre partem
sui, dum est huiusmodi, aliquem miserum vel quomodolibet maculatum.
Ex isto videtur (ut sequitur) quod qui non est miser, posterius suam
miseriam dimittens, efficitur pars ecclesie triumphantis. Pro isto (ut apparet
mihi) pro intencione doctoris est notandum quod multitudo, viatores pre-
destinati, miseriis (et) maculis involuti, posterius erunt partes ecclesie
triumphantis, cum illas maculas et miserias excusserint. Sed tamen dum
sunt huiusmodi miscriis involuti, non censentur partes ecclcsie trium-
phantis. Et ideo notanter dicitur, dum csl huiusmodi.
4. Aug. Enchir. cap. XI. VI. Opera (eJ. Maur.) tom. VI, pag. 217.

p. 4:
3. B in marg: Augustinus. 4. B in marg: Christus et corpus eius
sunt una persona. 8. B: reverencia corpus. 12. B in marg: Joh. VI.
i5. A in marg: Virtus cibi sacramentalis. 16. B: Igitur nemo. 21. In
codd. XXVI. Correxi. B in marg: Augustinus. 23. B in marg: Jo.VIII;
B in marg: Christus (sic) digestio.
3. Aug. Opp. III, r, pag. 58. i3. Viator is a traveller on
earth, cf. Wyclif, De civili dom. pag. 4. 20. Tract. in Joh. ev.
cap. VI, Opp. tom. III, 2, pag. 489. 28. Joh. VI, 40. XI, 25.
29. I. Cor. XIII, 8.

p. 5:
1. B: forct igitur. 5. B in marg: Jeremie. 10. B: 1'atct igitur.
II. B in marg: Quid est ecclesia. 14. A B in marg: Prima conclusio.
A in marg: Nullus papa debet se presumere esse caput huius ecclesie.
22. B in marg: Hetft. I. Rom. I. 27. AA, in marg: Augustinus. 28. B:
ostcnderet. AAj: ostendcrit. Correxi. Comp. bclow Alinea O. 29. B:
preter domum; ib. in marg. Nullum preter domum suam audit ad vitam
28. Enarratio in psal. i3i. Opp. IV, 2, 1477.

p. 6:
4. Vicaria. In codd.: vicarie. 10. A in marg: domus Dei. B in
marg: Presciti non pertinent ad ecclesiam catholicam. 29. A in marg:
Tota ecclesia est vidua.
9. Aug. loc cit. pag. 1480. 21. Psal. CXXXI, 11 — 12.
```

---

## Chunk 01-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "6.16–10.15"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "906 words; 825 unanimous or majority-real; 67 settled by vote (R2 43, R3a 17, R5a 7); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n43–n47 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 3: [TITLE]

## ¶1 · 6.16–10.15

> [p. 6] Unde sicut Deus iuravit David, quod de fructu ventris sui (scilicet Christum, qui fuit natus de ventre virginis, et per consequens, de illo homine manu forti) poneret super sedem suam: ita iuravit filiis suis, sub condicione tamen, si custodierint testamentum et testimonia Christi. Ne inquit Augustinus aliquis minaretur promissis Dei et in potestate sua ponat quod promisit Deus, ut impleretur, ideo iuravit, annectens condicionem, ne iam glorieris de promissis et dimittas te non custodire; tunc eris filius David, si custodieris: si autem non, non eris filius David. Filiis David promisit Deus; noli dicere filius sum David, si degeneras; sola vidua sedebit in ecclesia benedicta. Tota ecclesia una vidua est, cuius membra sunt pauperes saturati, quia deserti sunt in hoc seculo, quod non desponsant hereditarie sed relinquunt, non sperant in diviciis honoribus vel amicis, sed si habent contempnunt sperando pure in domino. [p. 7] Quid igitur valet dicere quod solum isti qui sunt Rome sunt ecclesia vel caput ecclesie.' Tales enim uruntur luna per noctem, ut exponit Augustinus psalmo CXX°. Quisquis inquit putaverit ecclesiam in una parte esse et non eam cognoverit diffusam toto orbe. terrarum et crediderit eis qui dicunt: Ecce hic est' Christus et ecce illic, sicut loquitur evangelium Mathei XXIV°, cum ille totum orbem terrarum emerit quoad valorem precii et ille in proximo scandalizatur et uritur a luna. Ad quid igitur oportet contendere circa caput ecclesie? Ipsa inquit Augustinus caro Christi est caput ecclesie, id est, humanitas secundum quam Christus predestinatus est, ut dicit fides scripture Ephes. I°, IV° et V° capitulis et expressius Col. 1°, 18, dicit quod Christus est caput tocius ecclesie. Et istam conclusionem declarat bene dicta decretalis extravagans Bonifacii VIII que sic incipit: Unam sanctam. Igitur inquit ecclesie unius unum corpus, unum caput, non duo capita quasi monstrum. F Secunda conclusio sequens ex quiditate matris ecclesie est quod tantum est una, sic quod non multe ecclesie catholice. Demonstratur sic: Eo ipso quod est ecclesia universalis sive catholica, ipsa continet in se omnes predestinatos. Non est possibile quod sit nisi una talis, igitur non est possibile quod sit nisi una universalis ecclesia. Nam secundum philosophos universale est quoddam totum atque perfectum cui [p. 8] nich.il deest. Unde sicut iuxta Aristotelem primo de celo omnia primo super tria ponimus: sic non dicimus ecclesiam catholicam nisi que in se continet ista tria: partem in celo triumphantem, partem in purgatorio dormientem et partem in terris militantem. Et [in fisuram illius dicunt doctores hostiam vel sacramentum eucaristie dividi in tres partes: Primam immersam sacramento liquido dicunt signare ecclesiam triumphantem, que insorpta et inebriata est intuicione divine essencie, ut loquitur caput ecclesie Cantic. V° 1, exhilarans cives et commensales suos. Inebriamini inquit carissimi. Due autem alie partes in manu domini et merito ecclesie expurgande signantur per illas duas partes quas sacerdos tenet in manibus: Maior supposita signat ecclesiam militantem et minor innixa supposite signat ecclesiam in purgatorio expectantem. Ipsa enim innititur suffragiis militantis ecclesie. Et Pro istis duabus partibus geminamus preces agno qui est caput ecclesie, ut misereatur nobis. Sed pro tercia parte ad cuius locum et requiem aspiramus petimus, ut idem agnus triplicis nature donet finaliter nobis pacem. Et hinc (ut ostendi alias) dictus sponsus secundum humanitatem suam visitavit tria loca ecclesie, scilicet umbilicum nostre habilitabilis, triginta tribus annis in Judea et Jerusalem conversando, limbum in quo patres purgati sunt, morsellum sue ecclesie in anima extrahendo; sed tercio finaliter ascendens in celum cepit captivitatem quam post triumphum coronavit ad dei dexteram collocando.■ [p. 9] Ista ergo est triplex pars unius universalis ecclesie sive catholice, licet quotlibet sint particulares ecclesie, quia tot quot sunt homines predestinati. Et hinc credo quod in simbolo ecclesie confitentur se credere unam sanctam catholicam et apostolicam ecclesiam. Apostoli enim sunt modo in celo in eadem personalitate qua vixerunt in terris, et sunt modo partes plene purgate eiusdem matris ecclesie, auctoritate quorum sui vicarii iam regunt adolescentulam modo querentem sponsum ecclesie; et sic loquitur decretum XXIV, q. I. Manet inquit Leo papa Petri privilegium ubicunque ex ipsius equitate fertur iudicium. Ipse enim residet in celis videns et procurans quod deus liget et solvat. Unde supradicta decretalis sic loquitur: Unam sanctam ecclesiam catholicam et ipsam apostolicam urgente fide credere cogimur et tenere. Unde unitatem illius ecclesie probat ex scriptura multiplici, primo per illud Canticorum VI°, 8: Una est columba mea, perfecta mea: una est matri sue, electa genitrici sue. Ista columba secundum concordem sanctorum sentenciam est mater ecclesia, cuius mater, quia creatrix est trinitas vel divina essencia, cuius genitrix et fotrix est patris sapiencia et ipsa mater virgo et sponsa humanitatis Christi sui capitis. Ex quibus parentibus spiritualiter, et per consequens, gignicione virginea filii ecclesie procreantur, iuxta quod loquitur apostolus 2ª Cor. XI°, 2, Despondi vos uni viro virginem castam exhibere Christo. Cum ergo in tota scriptura non ponitur vel una sillaba sine sensu, non restat quid pertinencius signaret hoc adiectum una [p. 10] in libro sapientissimi Salomonis nisi unitatem ecclesie catholice excludentem pluralitatem. Unde spiritus sanctus in patre Salomonis David sic orat in Christo psalmo XXI°, 21, Erue a framea Deus animam meam et de manu canis unicam meam. Quem textum secundo per decretalem allegatam beatus Augustinus sic exponit tractatu secundo eiusdem psalmi: Framea inquit gladius est, et per gladium mortem intelligi voluit. Unicam meam dixit ecclesiam. Canes sunt qui ceco more latrant nec intelligunt contra quos, eciam cum nichil eis fit, latrant contra viantes, licet velint eis proficere. Et utinam nostri possessionati non sint tales qui conspirant contra catholicos, tangentes eorum potestatem, fastum et ablacionem temporalium solummodo ad medelam.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 6.29: The whole Church is widowed.
- 7.1: The Church is distributed through the whole world.
- 7.4: Augustine.
- 7.12: The Head of the Church is Christ.
- 7.19: Second conclusion. The Catholic Church is only One and not many.
- 7.27: The three parts of the Church.
- 8.6: The three parts into which the consecrated host is broken signify the three parts of the Church.
- 8.18: Mark this.
- 8.22: Christ, as man, visited all.
- 9.11: Peter's privilege of binding and loosing remains where it is rightly exercised.
- 9.21: The begetting of children to the Church.
- 10.4: The unity of the Church proved out of many passages of scripture.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 7: *Quid* (first word after folio mark 128d) [R3]
  - 7: *Rome* [R4]
  - 7: *Christus* [R3]
  - 7: *I°* [R3]
  - 7: *Col* (15 is the line number) [R4]
  - 8: *in* [R3]
  - 8: *insorpta* (print has insorpta) [NW]
  - 9: *ubicunque* (hyphenated ubi-/cunque across line) [R3]
  - 9: *solvat* (leading 1 is margin fragment) [R4]
  - 9: *2ª* [R4]
  - 10: *framea* [NW]
  - 8: *deest* [THIN]
  - 007: *∅* ('ales' already inside neighbour 15 Tales) [DELX]
  - 7: *XXIV°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 6:
4. Vicaria. In codd.: vicarie. 10. A in marg: domus Dei. B in
marg: Presciti non pertinent ad ecclesiam catholicam. 29. A in marg:
Tota ecclesia est vidua.
9. Aug. loc cit. pag. 1480. 21. Psal. CXXXI, 11 — 12.

p. 7:
1. A in marg: Ecclesia est per totum orbem diffusa (above col. 128 J).
4. A: CX; in marg: Augustinus. B: Augustinus super primo voluminc.
11. A in marg: Capud ecclesie. B in marg: Augustinus. 13. B in
marg: Eph. 1, 4, 5. Col. 1. 17. B in marg: Decretalis. A, alia manu iu
marg super. : Scias quia istam decrctalcm falsificat, nichil enim ibi dc
predestinatis, sed decrctalis probat quod subesse Romano pontilici cst de
neccssitate salutis et hoc pcr unam ecclesiam et unum caput. 20. AB
in marg. Sec. conclusio. A in marg. Tantum una et non plures ecclesia
catholica. 27. .A in marg: Tres partes ecclesia.
4. Aug. Opp. tom. IV. pag. l38i. 17. Extrav. Commun.
Lib. I. Tit. VIII. De maioritate ct obeJientia, cap. I.

p. 8:
1. B in marg: Aristotelem. 6. A in marg: Tres partes divise hostie
consecrate signilicant tres partes ecclesie. Binmarg: Purgatorium. 8. B :
immensam; ib.: dicunt dignare. y. Codd: debriata. Correxi. 10. B in
marg: Cant. V». i3. B: expungnande. i5. B: et quatuor innixa.
18. A in marg: Nota. nota. B in marg: Christus creditur (recte dicitur)
agnus tripliciter. 19. B in marg: Agnus tercius. 24. B: umbili-
2. Aristot. rcept oopavoo I, 1. vA ib ?<z tpia itoivta etvat xai
to tpts icaVfij.

p. 9:
4. In codd: quo in simbolo; AA,: confitetur. II. A in marg:
Privilegium Petri ligandi et solvendi. B in marg: 24. q. 1. Lco papa.
16. 15: et tencmur. 18. B in marg. Cant. VI. ib. Una enim columba
mea, perfecta mea, una matri suc. 21. A in marg: Procreacio liliorum
ecclesie. 27. B in marg: 2. Cor. 2. 28. B: cum igitur. 29. B in
marg: Quare (in cod. quid) ecclesia sit una, hic deducitur.
10. Decreti secunda pars, causa XXIV, q. I, cap. V.

p. 10:
4. B in marg: Psalmo 11; A in marg: Unitas ecclesie probatur ex multis
scripturis (below col. 129» ). 5. B:carnis. 6. B in marg: Augustinus.
17. AA,: antichristinos. 19. B in marg: Gen. 6. 20 and 23. Codd:
consumatur. Correxi. 24. B in marg: Eph. 4. 29. Binmarg: Joh. i5.
6. Aug, in psal. XXI. Opp. tom. IV, pag. 98.
```

---

## Chunk 01-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-01-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-01-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "10.16–14.16"
divisions: "cap. 1 (heading 'CAP. I.' at 1.1); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "936 words; 839 unanimous or majority-real; 76 settled by vote (R2 42, R3a 20, R5a 14); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n47–n51 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 1, part 4: [TITLE]

## ¶1 · 10.16–11.10

> [p. 10] Scivit autem Christus ecclesiam suam in pace pretensa per antichristianos ypocritas amarissime persequendam. Tercium testimonium scripture est unitas arche, de qua Gen. VI°, 16°, legitur quod in tempore diluvii in cubito consummatur. Que ad sensum misticum figurat sanctam matrem ecclesiam que in brachio domini conservatur et unico fine mandatorum que est caritas consummatur. Quartum testimonium est dictum apostoli Ephesiorum IV°, 5, asserentis quod unus deus, una fides; ex cuius unitate sequitur quod sit correspondenter una lex, unum regnum sive familia que indubie est universalis ecclesia. Quintum testimonium est de una tunica inconsutili, que non sine misterio ex testimonio Johannis XIX°, 23, remanserat indivisa. Correspondenter oportet esse unicam Christi ecclesiam infringibilibus vinculis caritatis contextam iuxta illud apostoli Rom. VIII°, 35. Quis nos separa&bit [p. 11] a caritate dei? Sextum testimonium est illud Johannis X°, 16: Fiet unum ovile et unus pastor, quod ovile oportet confiteri eandem matrem ecclesiam. Quotlibet sunt scripture et raciones docentes istam sentenciam, ut sicut primus Adam terrenus sine bigamia habuit unicam sponsam carnaliter, sic secundus Adam sine bigamia possibili necessario habet unicam sponsam spiritualiter. Et illum sensum exponit apostolus ex scriptura Genes. II°, 24, ut patet ad Ephesios V°, 3i, de Christo et sua ecclesia.

[ENGLISH]

## ¶2 · 11.11–12.7

> [p. 11] Unde racio potest capi de textu apostoli Iª. Timothei III°, 2, et ad Titum 1°, 7, ubi ex isto fundamento dat legem, quod oportet tam episcopum quam diaconum esse unius uxoris virum. Oportet enim Christi clericum in monogamia consequi caput suum. Unde credo cum decretali fideli non verti in dubium quin foret hereticum pertinaciter negare quod Christus sponsus ecclesie, quem dignatus est vocare sponsam suam, sit monogamus racione unitatis ecclesie sponse sue. Et patet secunda conclusio. Tercia conclusio est quod extra sanctam ecclesiam catholicam non est salus vel remissio peccatorum. Hec est conclusio predicte decretalis in terminis cuius sensum arbitror esse de salute perpetua post hanc vitam, et de remissione peccati contracti, data vita spirituali per graciam. Et tunc conclusio proxima per se est nota: quia nemo potest habere talem salutem nisi vel Christus vel aliquod eius membrum, sed eo ipso quod sic est infra predictam ecclesiam: ergo conclusio; et ad hoc vadunt exempla. Sicut enim tota generis humani posteritas fuit primo virtualiter et materialiter in primo carnali coniugio, sic tota christianorum posteritas est virtualiter in Christo [p. 12] et ecclesia, et per consequens, in primo spirituali coniugio. Solis enim ex deo sic natis dedit potestatem filios dei fieri, et per consequens, iuxta argumentum apostoli coheredes. like Iterum, sicut extra navem Noe non remansit bestia salvata in diluvio: sic extra navem ecclesie non restat homo salvandus post spirituale naufragium.

[ENGLISH]

## ¶3 · 12.8–12.17

> [p. 12] Iterum, sicut membrum non vivit prescisum a corpore: sic nec natura humana per reprobacionem precisa a capite. Et ad hoc sunt quotlibet leges, ut XXIIIª, q. VIIª, sub auctoritate Augustini ad Vincencium decretum sic loquitur: Quemadmodum si prescindatur membrum ab hominis vivi corpore, non potest tenere spiritum vite: sic homo qui prescinditur de Christi iusti corpore, nullo modo potest tenere spiritum iusticie. Et tota ista sentencia patet XXIVª, q. I, per multa capitula.

[ENGLISH]

## ¶4 · 12.18–14.16

> [p. 12] Unde ex dictis Bede sic loquitur unum decretum: Quicunque ab unitate fidei vel societatis Petri quovismodo semetipsos segregant, tales nec vinculis peccatorum absoluti sunt nec ianuam regni celestis possunt ingredi. Item aliud decretum captum ex dicto Bede super primam canonicam Johannis: Omnis qui recedit et non permanet in doctrina Christi, Deum non habet; qui permanet in doctrina, hic et filium et patrem habet. Ex talibus dictis sanctorum et decreto ecclesie duce racione scripture patet tota predicta sentencia, et quod precipue timendum est, patet quod nullus christianus, sed precipue Christi vicarius non est membrum ecclesie, nisi perseveranter secutus fuerit Christum in moribus et doctrina. [p. 13] Quarta conclusio eiusdem decretalis est quod intra predictam ecclesiam est uterque gladius vel potestas scilicet corporalis vel temporalis et spiritualis; quorum uterque debet ad caput ecclesie et eius vicarium pertinere. Patet ex hoc quod dictum corpus, cum sit per se sufficiens, habet in se plenitudinem potestatis. Cum ergo utraque potestas sit necessaria matri ecclesie, patet conclusio. Et hoc figuratum est Luce XXII°, 38, quando apostolis respondentibus Ecce duo gladii hic Christus dixit non superfluum vel diminutum sed satis est. Unde ad denotandum quod uterque gladius fuit Petro pertinens, consequenter dixit Christus Petro percucienti servum pontificis: Mitte gladium tuum in vaginam. Ex quo innuitur ad sensum misticum quod uterque gladius sit in potestate ecclesie, materialis pro ecclesia sed per laicos exercendus, spiritualis vero pro puniendis peccatis per episcopum exercendus. Et sic licet gladius materialis sit in manu regum et militum, hoc tamen erit ad motum et secundum prudenciam sacerdotum. Oportet enim gladium materialem esse sub alio sicut ordo militaris est sub sacerdocio. Et ista est exposicio beati Bernardi, libro secundo ad Eugenium et ad illum sensum loquuntur quotlibet doctores et decreta concorditer. Unde XXIII% q. Vª, Principes, sub auctoritate beati Isidori 111° de summo bono, cap. LIII°, dicit canon quod intra ecclesiam principes seculi habent potestatem, ut per eandem potestatem disciplinam ecclesiasticam muniant. Ex qua conclusione patet, primo quod dicti principes sunt pars dicte ecclesie, cum [p. 14] aliter non essent ad suum propositum intra ecclesiam. Patet secundo quod ipsorum est cohercere rebelles ecclesie, ubicunque requiritur potencia civiliter coactiva. Unde notat Johannes de Deo octo casus in quibus subicitur iudicio vel correccioni seculari: Primus casus est cum clericus est incorrigibilis; secundus est cum propter ambicionem clericus est intrusor, eciam papa; tercius est quando fidem vult subvertere, quartus quando est falsarius, quintus quando facit scisma, sextus quando contempnit excommunicacionem, septimus quando potestas ecclesie deficit, et octavus dum principes seculi petunt tributum ab ecclesia. Et fundat ista per leges multiplices. Cum ergo in nullo istorum casuum debet secularis corrigere nisi conformiter ad scripturam, et per consequens, auctoritate summi pontificis: patet supradicta conclusio.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 11.21: Third conclusion. Outside the Holy Catholic Church there is no salvation or remission of sins.
- 12.5: Church is like Noah's ark.
- 12.8: The reprobate are as limbs cut off from the body.
- 12.12: So says Augustine
- 12.18: and Bede.
- 13.1: Fourth conclusion. Both swords or powers belong to the Church.
- 14.4: Eight cases in which an ecclesiastic is subject to secular judgment or correction.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 10: *Christus* [R3]
  - 10: *pretensa* (hyphenated pre-/tensa across line; H is alinea letter) [R3]
  - 10: *16°* [R3]
  - 11: *16* [R3]
  - 11: *unum* [R3]
  - 11: *II°* [R3]
  - 11: *Iª* [R3]
  - 11: *III°* [R4]
  - 11: *Christi* [R3]
  - 11: *Christus* [R3]
  - 12: *bestia* (trailing b is the margin letter) [R4]
  - 12: *XXIIIª* [R4]
  - 12: *VIIª* [R4]
  - 12: *XXIVª* [R4]
  - 13: *Quarta* [THIN]
  - 13: *Vª* [R4]
  - 13: *quod* (30 is the line number) [R4]
  - 14: *quibus* (qui-/bus hyphenated across line; print then has ecclesiasticus, which the pivot lacks) [R4]
  - 14: *seculari* (secu-/lari hyphenated; 'correction' is side-note text) [R4]
  - 13: *eiusdem* [THIN]
  - 14: *coactiva.* (hyphenated coac-/tiva.; tiva. absent from output, so whole word) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 10:
4. B in marg: Psalmo 11; A in marg: Unitas ecclesie probatur ex multis
scripturis (below col. 129» ). 5. B:carnis. 6. B in marg: Augustinus.
17. AA,: antichristinos. 19. B in marg: Gen. 6. 20 and 23. Codd:
consumatur. Correxi. 24. B in marg: Eph. 4. 29. Binmarg: Joh. i5.
6. Aug, in psal. XXI. Opp. tom. IV, pag. 98.

p. 11:
2. B: Joh. 8; in marg: Joh. 8. Joh. 10. 10— 12. B in marg: Eph. 5. 1.
Tim. 3 et ad Titum 1. 21. AB in marg: Tercia conclusio. A in marg:
Extra sanctam ccclesiam catholicam non est salus vel remissio peccato-
rum (below col. i2gb). 24. B: arbitri.

p. 12:
4. B in marg: apostoli. 5. B in marg: Dicit enim extra ecclesiam non
esse rcmissioncm peccati contracti. Quare igitur addit hoc contracti tum
ut verbum ^ cxtra illam ncc cst remissio peccati contracti nec non contracti.
ii. B in marg. 23, q. 7. 17. B in marg. 24, q. 1. 27. B: duce Romanc.
12. Decr. sec. pars causa XXIII, q. VII, c. IV. 18. ib.
Causa XXIV, q. I, cap. XXVII. 22. Decret. sec. pars
causa XXIV, q. I, cap. XXIV.

p. 13:
l. Codd. in marg: Quarta conclusio. A in marg: Intra ecclesiam est
uterque gladius vel potestas. 7. A: nostri ecclesie. 8. B in marg:
Luce 22. i3. B in marg: Nota de utroque gladio. 19. In decret.
Unam sanctam rectius legcs: sed ad nutum et patienciam sacerdotis.
22. B in marg: Bernhardus ad Eugenium. 26. B in marg: Isidorus 23,
q. 5. 28. B: ecclesiasticam immitit.
i3. Joh. XVIII, 11. 14. Comp. decret. Uuam sanctam I. c.
25. Decret. sec. pars. causa XXIII, q. V, cap. XX.

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
```
