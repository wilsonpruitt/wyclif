# Translation brief: ecclesia 03-f–04-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-03-f.md chunks/ecclesia/wyc-ecclesia-03-g.md chunks/ecclesia/wyc-ecclesia-04-a.md chunks/ecclesia/wyc-ecclesia-04-b.md` once and fix what it reports.
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

## Glossary (the 115 rows these chunks use; the full file is GLOSSARY.md)

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
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |

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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 03-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "64.11–66.2"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 6 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "386 words; 340 unanimous or majority-real; 37 settled by vote (R2 20, R3a 11, R5a 6); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n101–n103 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 6: [TITLE]

## ¶1 · 64.11–66.2

> [p. 64] Unde Augustinus super Joh. Omelia VIa, j exponens illud Johannis primo: Vidi spiritum descendentem quasi columbam de celo et manentem super eum, notat primo quomodo descensus columbe signat mistice spiritum sanctum, quia columba habet gemitum amorosum pro cantu. Spiritus autem sanctus secundum apostolum Romanorum VIII°, 26, postulat pro nobis gemitibus inenarrabilibus. Secundo quia columba sine felle vel laceracione unguium communicat pacis seculum, et tercio quia pascitur puris granis, econtra de corvis et minutis avibus que pascuntur carnibus vel muscas capiunt ut pascantur. Et propter istam similitudinem ad proprietates spiritus sancti precepit Christus suis apostolis Matthei X°, 16, quod sint simplices ut columbe. Secundo notat Augustinus quod descensus singularis columbe super Christum cum voce patris docuit Baptistam quod Christus capitaliter baptizat in spiritu sancto primo cuius principii est unitas in baptismo, qui non suscipit magis et minus secundum merita baptizantum, [p. 65] eo quod Christus non potuit communicare hanc primiciam potestatis suis discipulis. Tercio notat quomodo columba ad sensum allegoricum signat matrem ecclesiam que est una (ut dicitur Canticorum, V° capitulo, de columba). Unde sicut in diluvio columba egressa de archa reversa est, deferens ramum virentis olive, corvo pretextu affectus cadaveris extincto diluvio, sic in sancta matre ecclesia hii exeunt ad tempus et penitencia ducti redeunt, non solum cum verborum foliis, sed fructu bonorum operum, et omnino cum oleo caritatis que supereminenter super alia carismata instar olei supernatat. Ideo signanter dicit apostolus Iª Cor. XII°, 3 1: Adhuc eminenciorem viam demonstrabo vobis. Presciti autem exeunt de archa ut corvi, sed propter amorem temporalium pro quibus instanter placitant demerguntur. Quarto notari potest secundum logicam scripture quomodo spiritus sanctus movetur, cum descendit et postulat gemitibus inexplicabilibus et mane consurgit ad instruendum ecclesiam (ut dicitur Isaie VII°). Sed hoc non facit in natura propria, sed in creatura quam assumit, non ypostatice, sed singulariter ad sui noticiam et caritatis officium peragendum, nec solum in simplicitate columbina apparuit, sed in linguis igneis dispertitis ad docendum quod nedum debemus esse simplices, sed in operibus eciam caritatis ferventes, ut, sicut superbia divisit linguas in sensu, non in loco, tempore edificacionis turris Babel, Genesis XI°, sic econtra humilitas spiritus sancti congreget linguas uniformes quoad sensum, quantumlibet dispares quoad locum. Quinto colligitur ex dictis beati Augustini quod solum illi salvantur ut partes matris ecclesie qui proprietatem deserentes [p. 66] querunt finaliter res communes ecclesie que sunt capitaliter domini Jesu Christi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 64.11: Why the dove is a symbol of the Holy Spirit.
- 65.4: The dove is also a type of the Church.
- 65.19: How the Holy Spirit acts through the creature.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 64: *illud* [R4]
  - 64: *amorosum* [NW]
  - 64: *Christus* [R3]
  - 65: *∅* (nothing between Christus and non; these words are the last line of p.64 (already in p.64)) [INS?]
  - 65: *Iª* [R3]
  - 65: *3* (first digit of '31:'; the pivot splits it (pos 94 = '1:')) [R3]
  - 65: *placitant* (leading 4 is the margin number) [R4]
  - 66: *sunt* (137c is the folio mark) [R4]
  - 65: *XI°,* (no verse; boxed edge mark is the s of sic) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 64:
1. B in marg. : Quis credit in filium. II. B: Unde deest. A B in
marg.: Augustinus. A in marg. : De salvandis et dampnandis prescitis et
predestinatis. 17. B: Jo. VIII. (o. B in marg. : Nota quare columbe
descensus signat spiritum sanctum. ib: Vidi spiritum sanctum descen-
dentem sicut columbam. Nota proprietaies columbe. 26. A in marg. :
Augustinus.
5. Aug. In Johannis Evang. cap. 3, tractat XII. Opera tom III,
p. II, pag. 38q. 12. Joh. I. 32, cf. Aug. Opp. tom. III, p. II, pag. 33o.

p. 65:
2. B in marg.: Nota bene. A in marg. : Spiritus sanctus per diversa
signiQcatur ot quare, ut per columbam, per ignem etc. (Above o7b vvitliout
mark of reference ) i3. B in marg. : i. Cor. 12. 17. A in marg.:
Quomodo spiritus sanctus movetur. 20. Ita codd. Kecte Jerem. VII, i3.
2y. In codd.: congregat.

p. 66:
1. AB in marg. : Conclusio. A in marg. : De capite ecclesie. 10. B:
suam deest. 12. In codd.: canonica. A B in marg. : Bernhardus. B cap. XII.
i3. A inmarg.: fcxclesia que ct quomodo fragrat ungcntis optimis et quo-
modo eius ubera sunt mcliora vino. (Abovc i37c without mark of rcfcrcnce.)
B in marg. : Meliora sunt ubera tua vino et fragrancia ungentis optimis.
i3. A: fraglat. i5. 29. Codd.: ungentis. 21. unde fragret. Codd.: bene
fragret. 26. A A, : inebrient.
7. Aug. 1. c. pag. 340 et Opp. II, 678. Ep. ad Dard. 1 2. Ber-
nardi Opp. pag. 523.
```

---

## Chunk 03-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "66.3–69.3"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 7 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "693 words; 628 unanimous or majority-real; 52 settled by vote (R2 28, R3a 20, R5a 4); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n103–n106 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 7: [TITLE]

## ¶1 · 66.3–69.3

> [p. 66] Ex quibus concluditur quod periculosum foret cuiquam christiano propter fastum vel questum singularem pretendere quod sibi tamquam capiti universalis ecclesie sit necessarium omnes christianos singulariter obedire, dicente Augustino (ubi supra) quod ecclesie non preerat Faustinus episcopus, sed parti preerat (ut dicit epistola ad Dardanum). Christus congregavit ecclesiam suam in unum spiritum et unum corpus cuius unum caput est Christus. Et Bernardus super Cantica sermone XII°: Quisquis et inebriat verbis et fragrat beneficiis, sibi dictum putet: quia meliora sunt ubera tua vino et fragrancia unguentis optimis. Et ad hec quis idoneus? Quis nostrum unum illorum saltem integre perfecteque possideat, ut interdum non in dicendo sterilior et in operando tepidior sit? Sed est que merito et non ficte hoc preconio glorietur, ecclesia utique cui nunquam de universitate sua deest et unde inebriet et unde fragret; quod enim sibi deest in uno, habet in altero secundum mensuram donacionis Christi ac moderacionem spiritus dividentis singulis prout vult. Fragrat ecclesia in hiis qui sibi faciunt amicos de mamona iniquitatis, inebriat in ministris verbi qui vino leticie spiritualis infundunt terram et inebriant eam et fructum referunt in paciencia. Ipsa audaciter secureque sese nominat sponsam, tamquam que vere habet ubera meliora vino ac fragrancia unguentis [p. 67] optimis. Quod etsi nemo nostrum sibi arrogare presumat, ut animam suam audeat sponsam domini appellare, quoniam tamen de ecclesia sumus que merito hoc nomine et re nominis gloriatur, glorie huius participium usurpamus. Quod enim simul omnes plene integreque possidemus, hoc singuli sine contradiccione participamus. Gracias tibi domine Jesu qui nos karissime ecclesie tue aggregare dignatus es, non solum ut fideles essemus, sed eciam ut tibi vice sponse in amplexus iocundos castos eternosque copularemur. Ecce quomodo sancti sub dubio presumpserunt se esse membra ecclesie, sed nonnisi ex presupposita imitacione sponsi ecclesie. Unde sermone XIII° dicit Bernhardus: Si sponsa utique de omni virtute sua vel gracia misericordie audeat sibi quippiam arrogare, quanto minus adolescentule que forte nos sumus? Ecce quomodo dicit forte. Dicamus proinde et nos sponse vestigia insectantes: Non nobis domine, non nobis, sed nomini tuo da gloriam. Dicamus non verbo et lingua tantum, sed opere et veritate: quia aliter non sumus iuvencule, iuxta illud Psalmi LXXVIIⁱ, 36, 37 Quoniam dilexerunt eum in ore suo et lingua mentiti sunt ei; cor autem eorum non erat rectum cum eo, nec fideles habiti sunt in testamento eius. Ecce iste sanctus plane sentenciat quod, nisi habuerimus vitam contemplativam vel activam quam Deus acceptat ad beatitudinem aliter non sumus partes ecclesie. Ideo instar sanctorum decertaremus, quis posset esse in fructuoso ministerio matris sue operosior atque humilior. Et ex hinc iuxta fidem scripture, Matthei XVIII°, 1, sequitur quod sit maior. Christus enim non potuit esse caput ecclesie sine humillimo [p. 68] et pauperrimo ministerio sponse sue. Quomodo ergo eius vicanus preerit uni adolescentule, nisi gerat in moribus vicem Christi, non exigens subieccionem civilem quam Christus non potest exigere? Periculum autem predictum de presumpcione stupida exterreret sensatos, ne contendant circa primatus sancte matris ecclesie vel tamquam in ea aut ex ea capitanei exigant seculariter bona eius. Talis enim presumpcio excluderet contenciosos, ne sint vel membra abiecta huius corporis, cum secundum omnes eius naturas sit compaginata proporcione tali armonica; quod non est possibile quod secundum aliquas eius partes sit contrariacio perpetua, cum oportet ad ultimum quodlibet membrum eius consentanee iuvare quodlibet (ut docet apostolus Ia Cor. XII°). Nam finis pro quo nunc militamus est ut unanimes uno ore sine usurpacione alieni officii in quiete perpetua conletemur; que leticia a nullo queritur, nisi in via tendunt ad finalem concordiam. Temporalia enim abusa tenetur prelatus restituere(ut patet per Archidiaconum XLIVª distinccione et declaravi sexto capitulo....). Et primatum non debet clericus principaliter querere sed laborem; aliter enim est mercenarius, non pastor, ut allegatum est in principio huius capituli ex decreto VIIIª, q. I: Sunt in ecclesia. Super quo dicit Archidiaconus quod in quolibet episcopatu sunt duo, scilicet dignitas et opus ad quod dignitas vere consequitur. Et sic quicunque prepostere ambiunt dignitates, ut sint tamquam mercenarii et non ut membra ecclesie, se reddunt dampnabiles. Et forte in isto capitulo sunt quidam hodie qui non tantum appreciantur lucrum fructus operis evangeliste [p. 69] sicut voluptates temporales, decimas vel honores; et omnes tales sunt venenosi heretici (ut patet libro sexto, tractatu de heresi).

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 66.3: It is dangerous for any one to claim the obedience of all Christians.
- 67.11: Thus the Saints hesitated to call themselves members of the Church.
- 68.1: Christ's vicar must not ask a submission which Christ cannot ask.
- 68.25: A bishopric should be desired for the work, not for the dignity.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 67: *optimis* (137c is the folio mark) [R3]
  - 67: *Quod* [R3]
  - 67: *37* [R3]
  - 67: *1* (arabic verse number '1,') [R3]
  - 67: *Christus* [R3]
  - 68: *pauperrimo* [R3]
  - 68: *moribus* [R4]
  - 68: *vicem* [R3]
  - 68: *XLIVª distinccione* (print ends line 20 with 'XLIVª distinccione,' before et) [INS?]
  - 68: *VIIIª* [R4]
  - 68: *Et* [R3]
  - 67: *nemo* [THIN]
  - 67: *huius* (italic; no punctuation) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 66:
1. AB in marg. : Conclusio. A in marg. : De capite ecclesie. 10. B:
suam deest. 12. In codd.: canonica. A B in marg. : Bernhardus. B cap. XII.
i3. A inmarg.: fcxclesia que ct quomodo fragrat ungcntis optimis et quo-
modo eius ubera sunt mcliora vino. (Abovc i37c without mark of rcfcrcnce.)
B in marg. : Meliora sunt ubera tua vino et fragrancia ungentis optimis.
i3. A: fraglat. i5. 29. Codd.: ungentis. 21. unde fragret. Codd.: bene
fragret. 26. A A, : inebrient.
7. Aug. 1. c. pag. 340 et Opp. II, 678. Ep. ad Dard. 1 2. Ber-
nardi Opp. pag. 523.

p. 67:
9. B: Oportct cciam ut tibi viccm. n. A in marg. : Sancti cum for-
midinc et sub spe dixerunt se csse mcmbra sancte ecclesie. B in marg. :
Nemo audeat sc asscrerc membrum ecclcsie. i3. B: cap. XIII. AB
in marg. : Bernhardus. 21. In Bcrnard's sermon tlie passage runs
as follows: Ne fortc (quod nimis vcreor) dicatur et de nobis: Quoniam
etc. . . conf. Opp. pag. 527. 3i. B in marg. : Matth. XVIII.

p. 68:
6. 13: exerceret. A in marg : Membra sancte ecclesie sunt uuita.
/Above 1371.) i5. B in marg.: i. Cor. XII. 20. Sc. per Guidonem
de Baysis, archidiac. Bononiensem. 21. capitulo; in codd. sequitur
lacuna. VI. capit. scil. huius libri De ecclesia. 24. A in inarg.: 1'relatus.
B in marg. man. rec. : q. 1 vel 2. A B in marg. : Archidiaconus.
24. Decreti secunda pars causa VIII, q. I, cap. XIX.

p. 69:
5. A in marg.: Prima obieccio. |3. AB in marg.: Responsio.
3o. A in marg.: Composicio sancte matris in ecclcsie et parcium pro-
porcio (Bclow i3/a).
3. Ad cap. III. cf. Hus Opp. I. Fol. 199*, 2o5b etc.
```

---

## Chunk 04-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-04-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-04-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "69.5–72.10"
divisions: "cap. 4 (heading 'CAP. IV.' at 69.4); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "702 words; 648 unanimous or majority-real; 42 settled by vote (DEL 1, R2 22, R3a 13, R3b 1, R5a 3, R6a 2); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n106–n109 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 4, part 1: [TITLE]

## ¶1 · 69.5–69.29

> [p. 69] Ut dicta de sancta matre ecclesia magis appareant, obicitur aliter contra dicta. Primo, inquam, videtur quod continuum quantitative componitur ex non quantis, quia sancta mater ecclesia que est corpus Christi misticum componitur quantitative ex multis milibus beatorum spirituum, et per consequens, corpus se habet in proporcione racionali secundum quantitatem ad multitudinem spirituum beatorum. Sed hic conceditur conclusio, ut patet de attomis principiis corporum, de punctis linearum et sic de instantibus cum aliis partibus indivisibilibus continuorum. Et sic conceditur quod sancta mater ecclesia est comparabilis in proporcione racionali, eciam secundum quantitatem multitudinis celestium spirituum. Quantitatem dico virtutis, non molis; sed illam proporcionem novit sponsus ecclesie, nec oportet ex hinc esse proporcionem racionalem inter corpus et animam, vel animam esse partem quantitativam ac quiditativam formaliter sui compositi. Ymmo, equivocando in nomine corporis, concedi potest quod multitudo beatorum angelorum, sicut fuit ecclesia ut est modo, sic fuit corpus Christi misticum, et ita eadem ecclesia habuit aliquando unam quantitativam medietatem, non mole sed numero; que fuit numerus angelorum, et alia medietas fuit numerus hominum eciam secundum naturam corpoream.

[ENGLISH]

## ¶2 · 69.30–71.28

> [p. 69] Secundo obicitur per hoc quod iuxta dicta de quiditate ecclesie omnia que fuerunt vel erunt sunt [p. 70] tempore suo Deo presencia, cum aliter non componeretur ecclesia ex omnibus electis presentibus, preteritis et futuris. Sed conceditur conclusio, ut concedunt sancti concorditer; unde sanctus Thomas, De Christo, conclusione octava, articulo III°, vere dicit quod corpus hominis ecclesie constituitur ex hominibus qui fuerunt a principio mundi usque ad finem eius. Et Chrisostomus In Imperfecto, Omelia XLVIª, exponens [illud Matthei XXIII°, 34: Ecce ego mitto ad vos prophetas et sapientes, ostendit ex fide scripture quod oportet duas generaciones ab Adam usque ad finem mundi concurrere, scilicet generacionem iustorum que est sancta mater ecclesia et corpus Christi, et generacionem perversorum que est ecclesia malignancium et corpus diaboli. Omnium, inquit, iniquorum persecutorum et homicidarum a Caym usque ad finem mundi una generacio est: et si non omnes tempore uno, omnes tamen filii sunt persecutoris et homicide illius Caym. Ideo alibi dic t: Amen dico vobis, non transibit generacio hec, donec omnia fiant. Et illam generacionem demonstrat Christus, quando dicit de presenti: Ecce ego mitto ad vos sapientes et scribas, licet enim Caym persecutor Abel mortuus est, tamen facti sunt gigantes, persequentes filios Seth. Ecce Caym transiit, sed generacio ipsa stetit. Perierunt tercio gigantes in diluvio, sed nati sunt ex Caym Cananei et cetere gentes, persequentes filios Sem. Cananeis mortuis quarto successerunt alienigene, [p. 71] persequentes Iudeos, quinto conversis quibusdam gentibus ad Christum surrexerunt perfidi Iudei genere, martires persequentes christianos, et post ipsos sexto surrexerunt heretici quidam gentiles in eodem genere, martires persequentes; septimo insurrexerunt heretici, ecclesiam persequentes octavo gentiles quoad modicum uniendi, qui licet sint nominetenus clerici, tamen sunt discipuli Antichristi. Sicut ergo ex omnibus istis fit una generacio quoad mores, sic est una generacio iustorum, succedens cum ista quam oportet prosperando procedere. Et iste due generaciones sunt due civitates secunde ecclesie vel duo corpora, Christi et Antichristi; que Augustinus, Gregorius et alii sancti ex fide scripture ponunt concorditer. Nec aliter vere exprimetur sensus spiritus sancti de generacione huiusmodi nec de duracione ordinum vel alterius successim. Unde videtur nimis suspectum verbum modernorum dicere quod dicti sancti erant ignari logice et sequentes scripturam inciderunt in hereses manifestas. Tercioobicitur per hoc quod, sicut institucione humana preficiuntur reges, domini seculares et alii officiarii quoad seculum, sic et clerici constituuntur ordinacione humana partes ecclesie. Oportet ergo sumere ecclesiam in significacione vulgari, concedendo quod predestinatus excommunicatus fit non membrum ecclesie, prescitus autem in gracia est verum membrum ecclesie, quia aliter nemo assumeret sibi nomen ecclesiastici nec quisquam crederet suo proposito in quantum huiusmodi.

[ENGLISH]

## ¶3 · 71.29–72.10

> [p. 71] Hic dicitur (ut supra) quod ecclesia dicitur dupliciter, scilicet vere et pretense. Vere, quod est vere corpus Christi et sponsa eius; pretense, quod viantes reputant corpus Christi, licet sit sinagoga sathane. [p. 72] Primo modo loquendo de ecclesia solum subest ordinacioni Dei eterne vel Christi instituere eius partes. Sicut enim rex terrenus ordinat temporaliter regnum suum, sic rex celestis ordinat eternaliter regnum suum, cum regni illius non erit finis (ut patet Danielis VII°, 14 et Luce 1° 33). Alii autem iuvant vel persequuntur regnum illud quod est ecclesia secundum quod Deus eternaliter ordinavit. Et sic loquendum est de ecclesia vera et de ecclesia pretensa vel mixta; sed de prima est nobis sermo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 69.5: Objection: 1. The Church would have a quantitative relation to the number of the blessed.
- 69.16: Answer: The Church has such a relation of number, though not of mass;
- 69.24: one half is composed of angels and one of men.
- 70.1: 2. Objection: If we are right, all things past and future would be present to God.
- 70.8: Answer: All the Saints agree that they are sO present.
- 70.17: All the wicked make one generation;
- 71.9: and so do all the righteous.
- 71.20: 3. Objection: As lay rulers are humanly appointed, so are the officers of the Church.
- 71.29: Answer: We must distinguish between the true and the
- 71.30: We must distinguish between the true and the apparent Church.
- 72.1: The true Church obeys only the orainance of God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 69: *CAP. IV.* [HEAD]
  - 69: *Christi* [R3]
  - 70: *Thomas* [R4]
  - 70: *34* [R3]
  - 71: *persequentes* (138a is the folio mark) [THIN]
  - 71: *Iudeos* [THIN]
  - 71: *Iudei* (italic capital I) [R3]
  - 71: *iustorum* [NW]
  - 71: *successim* (succes-/sim hyphenated; print has successim) [NW]
  - 71: *preficiuntur* [NW]
  - 71: *Christi* [R3]
  - 70: *XLVIª,* [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 69:
5. A in marg.: Prima obieccio. |3. AB in marg.: Responsio.
3o. A in marg.: Composicio sancte matris in ecclcsie et parcium pro-
porcio (Bclow i3/a).
3. Ad cap. III. cf. Hus Opp. I. Fol. 199*, 2o5b etc.

p. 70:
l. B: dc presencia. 3. AB in marg.: Responsio. 4. A in marg.:
Sanctus Thomas. Nota de generacionibus bonorum atque malorum.
(Above t3S" without mark of rcference.) B in marg. : Affirmat sanctus
Thomas ampliacionem verbi ut vidctur. 8. ABinmarg.: Crisostomus.
q. In codd.: Omelia XXIX. 11. B: Adam deest. 24. A in marg. :
Persecucio ecclcsie sancte ab ecclcsia malignancium. B ln marg. : Commixcio
generacionis prave cum benivola gcneracione Jesu Christi.
5. Thomae Opp. tom V, pag. 5i. 8. Opus imperfectum
(incerti auctoris); Homil. XLV. Chrysost. Opp. (ed. Bernardus de
Montfaucon) tom. VI, pag. CXCIII. E. i5. Op. imp. 1. c.
pag. CXCIV. E.

p. 71:
3. B : genere martires deest. 4. B: heretici deest. (i. 7. B:
quoad modum. 8. A: cum sunt. 17. AA^: verborum.
2}. A: summere. 25. B: sit non. 29. B in marg. : Responsio. ib.
Huplex de ecclesia. 3o. A in marg. : Ecclcsia <T (Abovei38b
witliout mark of refercnce).

p. 72:
2. Instituere corr. A, : AB: iusti cure. i5. A B in marg.: Conclusio.
20. AB in raarg.: Ricardus.
22. Richardi S. Victoris opp. (ed Migne) pars sec. pag. 1 172,
cap.XlX tract. De potestate ligandi et solvendi. 27.Matth. XXIV, 12.
```

---

## Chunk 04-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-04-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-04-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "72.11–76.24"
divisions: "cap. 4 (heading 'CAP. IV.' at 69.4); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "984 words; 893 unanimous or majority-real; 75 settled by vote (DEL 2, INS 1, R2 47, R3a 19, R3b 1, R5a 4, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n109–n113 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 4, part 2: [TITLE]

## ¶1 · 72.11–75.15

> [p. 72] Conceditur tamen quod ordinacione humana clerici constituuntur in officiis ecclesiasticis tam predestinati quam presciti, sed ordinantes eis talia ofncia non habent potestatem ordinandi quod sint membra vel partes vere ecclesie. Ulterius conceditur quod predestinatus quantumcunque fuerit in mortali non desinit esse membrum vere ecclesie, licet excommunicacione pretensa ponatur nominetenus extra temporalem ac corporalem communicacionem pretense ecclesie. Unde Ricardus de Sancto Victore in quodam tractatu De Potestate Clavium qui sic incipit: Quodcunque ligaveris Membrum, inquit, Christi potest dici homo secundum geminam consideracionem, aut secundum predestinacionem aut secundum habitudinem. Secundum predestinacionem potest quis membrum Christi esse et necdum caritatem habere. Juxta namque domini testimonium: Refrigescet caritas multorum. Secundum ergo hanc accepcionem contingit hominem esse membrum Christi et adhuc vinculo debite dampnacionis teneri; secundum habitudinem autem membrum Christi dicitur, quando in se habet hoc, unde hoc ipsum efficitur. Sed numquid membrum Christi [p. 73] caritas illa facit que ad tempus inardescit et in momento refrigescit? Absque dubio qui perseverantem caritatem nunquam accipiunt, nunquam de veris illis Christi membris fuerunt qui corporis eius integritatem perficiunt. Secundum quandam accepcionem tamen possumus et solemus caritatem transitoriam habentes membra Christi dicere propter membrorum ipsius conformitatem quam ad tempus videntur habere. Sed ut a pie querentibus omnem scrupulum amoveamus, dicimus quod triplici modo membrum Christi dici solemus: predestinacione, preparacione, concorporacione. Predestinacione, quando ad vitam divinitus preordinatur; preparacione, quando paganus vel falsus christianus veraciter compungitur et ad veritatem ac caritatem inbuitur; concorporacione, quando ille per corporis ablucionem, iste per sacerdotis absolucionem ecclesie Christi conformatur. Primum agitur proposito divine voluntatis, secundum proposito proprie deliberacionis, tercium vero officio sacerdotis. Ex corporali advertere possumus quid de spirituali edificacione sentire debeamus. Ecce de silva lignum eligitur; ut in edificio ponatur, postea dolatur, et admodum formam congruam dolando preparatur, ad ultimum edificio connectitur et ipsi debite in loco coaptatur. Ecce quomodo unum denique lignum fit edificii membrum: primo sola eleccione, secundo preparacione et tercio compaginacione. Sic sane multi iam sunt membra Christi predestinacione, necdum tamen preparacione; multi vero preparacione, sed necdum tamen concorporacione. Augustinus cum adhuc infidelis esset, secundum predestinacionem [p. 74] membrum Christi fuit, conformiter preparacione membrum Christi extitit, cum corde credens et devocione fervens ad baptismum festinavit. Baptizatus vero et ecclesie consociatus membris Christi concorporatus fuit. Et istam sentenciam docet Augustinus, tercio De Doctrina Christiana, cap. XXXII°: Non enim re vera corpus domini est quod cum illo non erit in eternum. Ypocrite. inquit, non solum in eternum, verum eciam nunc non cum illo esse dicendi sunt, quamvis in eius esse videantur ecclesia. Et idem dicit Chrisostomus In Imperfecto, Omelia IXª: Qui Dei fuerunt perire non potuerunt, quia de Deo nemo rapere potest. Et eadem est sentencia sanctorum doctorum qui se ipsos intelligunt in ista materia; nam aliter fides scripture foret falsa, cum Joh. X°, 27, 28, dicit Christus: Oves mee vocem meam audiunt, et ego cognosco eas, et sequuntur me, et ego vitam eternam do eis, et non peribunt in eternum, et non rapiet eos quisquam de manu mea. Et post probat ex immensitate doni patris (quod est spiritus sanctus) quod nemo potest hoc facere, quia pater suus est omnipotens de cuius manu nemo potest quidquam eripere. Sed Christus et pater suus unum sunt cum spiritu sancto qui est donum suum; quo sibi copulatur ecclesia (ut patet cap. X). Ergo nemo potest oves suas de manu eius eripere. Ipse enim eternaliter elegit quodlibet membrum ecclesie in sponsam; ergo sicut nemo potest desinere esse predestinatus, sic non est possibile quod aliquod membrum sponse sue deserat vel expellat, quia (ut dixi superius) tunc persona eligens foret improvida vel ingrata. [p. 75] Secundo confirmatur idem ex fide scripture 1° Joh. IIª 19, ubi sanctus evangelista loquitur de prescitis qui ad tempus manserunt in gracia. Si, inquit, ex nobis fuissent, permansissent utique nobiscum. Non enim sapit quod ista condicionalis tam alti evangeliste sit impossibilis et heretica. Tercio confirmatur ex dicto apostoli Rom. VIII°, 35, ubi loquens de se et aliis membris ecclesie palam asserit quod nulla creatura poterit eos separare a caritate que est numerus fundatus in Christo Jesu colligans membra sua. Ideo dicit eodem capitulo, 9% Vos autem in carne non estis, sed in spiritu, si tamen spiritus Dei habitat in vobis. Si quis autem spiritum Christi non habet, hic non est eius. Et intelligit quod ille non est pars sui corporis.

[ENGLISH]

## ¶2 · 75.16–75.30

> [p. 75] Et si obicitur per hoc quod prescitus existens in caritate habet hoc vinculum, et per consequens, unionem, sicut predestinatus existens in crimine caret hoc vinculo, et per consequens, unione: patet quod, sicut in humano corpore est dare humidum fluens et humidum radicale, sic in corpore Christi mistico est dare graciam secundum presentem iusticiam et graciam consummatam. Unde sicut apostemata per humidum fluens sunt adnata, non continuata propter disparitatem nature: sic est de membris diaboli, licet pro tempore secundum presentem iusticiam sint adnati. Predestinati autem licet ad tempus priventur fluente gracia, habent tamen radicalem graciam a qua non possunt excidere, et sic habentes duplicem graciam duplici vinculo sunt ligati. Ligamentum tamen primum est insolubile.

[ENGLISH]

## ¶3 · 76.1–76.24

> [p. 76] Sic ergo videtur mihi quod sentencia sanctorum de membris vere ecclesie sit pernecessaria hodie, sicut fuit tempore sinagoge. Sicut enim tunc sacerdotes pretensi dixerunt repugnare promissioni divine quod ipsi vel possessio eorum pereat, sicut recitat Jeremias VII°, cap. 4: Nolite confidere in verbis mendacii, dicentes templum domini, templum domini, templum domini est, sic et modo videtur quosdam prepositos particularis ecclesie qui pretendunt se ex fide convincere quod ipsi capitaliter regant Petri naviculam, sic quod ipsa potest fluctibus seculi concuti sed non mergi. Et sic implicant se ex predestinacione divina non posse dampnari nec temporalia posse a sua ecclesia spoliari, sed de necessitate salutis oportet omnes alios christianos eis subici et tamquam capitales in dominacione seculari ac spirituali omnium bonorum ecclesie dominari. Unde, sicut sacerdotes Aaronite dixerunt quod non peribit lex a sacerdote neque consilium a sapiente neque sermo a propheta (ut dicitur Jeremie XVIII°, 18), sic videntur dicere hodie quod pretensa et particularis ecclesia sit tripliciter stabilita, scilicet Christi promissione, fulcimento legis ecclesie que equivalet fidei christiane, et multorum sapientum constipacione.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 72.11: The foreknown as well as the predestinate may hold ecclesiastical office.
- 73.10: Three ways of being a member of Christ; by predestination, by preparation, by concorporation.
- 74.6: That only is a part of the Lord's body which will remain with Him for ever.
- 74.27: The predestinate cannot cease to be such.
- 75.2: The foreknown cannot continue in grace.
- 75.7: St. Paul says that nothing can separate us from the love of God.
- 75.16: It is objected that this applies to the foreknown who is for the time in charity;
- 75.22: but the foreknown are not parts of Christ's body, but excrescences.
- 76.8: There are prelates who say that the safety of the Church is due to them.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 72: *in* [R3]
  - 73: *edificio* [NW]
  - 73: *formam* [THIN]
  - 73: *congruam* [THIN]
  - 73: *dolando* [THIN]
  - 73: *edificio* [NW]
  - 73: *edificii* [NW]
  - 74: *corpus* [R3]
  - 74: *IXª* [R4]
  - 75: *19* (138c is the folio mark) [R3]
  - 76: *particularis* (parti-/cularis hyphenated across line) [NW]
  - 76: *dominacione* (domi-/nacione hyphenated; 15 is the line number) [R4]
  - 76: *∅* (nacione is the second half of domi-/nacione (pos 112)) [INS?]
  - 75: *IIª* [R3]
  - 072: *∅* (second half of mem-brum; neighbour 202 already membrum) [DELX]
  - 75: *VIII°, 35,* (print has verse 35 after chapter) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 72:
2. Instituere corr. A, : AB: iusti cure. i5. A B in marg.: Conclusio.
20. AB in raarg.: Ricardus.
22. Richardi S. Victoris opp. (ed Migne) pars sec. pag. 1 172,
cap.XlX tract. De potestate ligandi et solvendi. 27.Matth. XXIV, 12.

p. 73:
4. In codd.: que corporis. 11. AB (man. rec.) in marg. : Membrum
predestinacione
Christi (B add.: ecclesie tripliciter) : ^-preparacione (Below i33b);
concorporacione
B man. recent. in marg. : Membrum scilicct secundum habitudinem eius.
AB in marg.: Triplex membrum; A in marg. : Nota. 20. B in marg.:
Exemplum. 26. A: In cod.: lignum sit. 29. A B in marg. :
Exemplum.

p. 74:
1. Codd.: Conformitatis. Correxi. 5. AB in marg. : Augu-
stinus. ii. Jmperfecto sc. opere. A in marg.: Predestinalum
membrum Christi non potest cessare tale membrum. ib. A B in marg. :
6. Aug. Opp. tom. III, pars i, pag. 58. ii. Opus imper-
fectum in Matthaeum. Honi. IX, I. c. pag. L.XI. E. ig. Joh.

p. 75:
3. AA, : pcr tcmpus. 9. B: eos deest. 10. B: minus fundatus.
10. A B in marg. : Obieccio. 19. B in marg.: Solucio. ib. Prcdcstinati
quomodo sunt in ecclcsia et quomodo prcsciti qui sunt ad tcmpus in
gracia. B in marg. : man. rec. Nota de prcdcstinatorum et prescitorum
natura pulcra. 22. A 111 marg : Gracia <T , prescntem msti-
ciam. 26. 27. B: Predestinati autcm. Cod. A, liabet: vero (Sic eciam in
Hussi tractatu legcs. Opp. I, 204b). 3o. B: Ligamentum cum.

p. 76:
4. Codd: repungnarc. 10. A in marg. : Nota de papa. 25. AB in
marg. : Triplex consideracio. A A, : nullus locus vel Ieccio. Hus : nullus locus
vel elcccio. B in marg. man. rec: Nec locus nec eleccio facit predcstinatum.
```
