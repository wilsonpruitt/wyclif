# Translation brief: ecclesia 02-e–03-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-02-e.md chunks/ecclesia/wyc-ecclesia-02-f.md chunks/ecclesia/wyc-ecclesia-03-a.md` once and fix what it reports.
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

## Glossary (the 128 rows these chunks use; the full file is GLOSSARY.md)

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
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
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
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| globus | band | Derogatory collective (*globus reprobus*, *globos claustralium*). Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 02-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-02-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-02-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "38.25–42.9"
divisions: "cap. 2 (heading 'CAP. II.' at 25.23); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "764 words; 697 unanimous or majority-real; 57 settled by vote (R2 34, R3a 14, R5a 7, R6a 2); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n75–n79 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 2, part 5: [TITLE]

## ¶1 · 38.25–41.6

> [p. 38] Sed contra ista instatur tripliciter: Videtur enimL primo quod subditi debent consulere scripturam sacram in quocunque quod papa mandaverit. Quantum ad istud, concedi debet conclusio, cum nemo debet parere sibi plus quam alii, nisi in quantum est superior Christi vicarius, et per consequens, nisi in quantum obeditur principalius Jesu Christo; sed in omni obediencia [p. 39] Jesu Christo debet christianus consulere legem suam; ideo in omni obediencia christiani in quantum huiusmodi debet obedienciarius consulere legem Dei; et ideo ordinarunt iura ecclesie quod lex scripture tam generaliter et tam precipue a sacerdotibus et specialiter maioribus debet sciri, ne turbentur aut musitent quid et qualiter ad mandatum superioris debeant respondere. In ista scola instructa est legio Thebayca et omnes martyres, immo in illa scola instructi sunt omnes qui monitis non sapientibus caritatem Dei et proximi contradicunt iuxta illud Christi Matth. X°, 37: Qui amat patrem vel matrem plus quam me, non est me dignus; et istam leccionem docent apostoli Act.V°, 29, dicentes quod obedire magis oportet Deo quam hominibus. Ideo dicit Christus Matth. X°, 35: Non veni pacem mittere in terram sed gladium. Veni ergo separare hominem adversus patrem suum, et filiam adversus matrem suam, et nurum adversus socrum suam, et inimici hominis domestici eius. Amiciciam enim carnalem propter Deum venit Christus dissolvere, quia ille qui videtur esse familiaris homini quoad mundum est hostis suus ut plurimum quoad Deum (ut dicitur Michee VII°). M Beatus Jeronymus super illo capitulo videtur exponere textum evangelii ad hunc sensum quod Christus venit ad separandum hereticos ab ecclesia quam illudunt. [p. 40] Simulant enim ex palliata ypocrisi quod sint filii Dei per graciam adopcionis et filie ecclesie matris sue pro cuius iuribus tantum zelant. Dicamus inquit scriptum de hereticis; non enim nostram salutem sed sua querunt lucra, et deceptum gregem pedibus suis conterunt. Pater heretici est Deus qui creavit eum, et mater ecclesia; socrus ad literam est mater alterius coniugum. Ast uxor nati dicitur esse nurus, cum ergo Christus secundum humanitatem sit sponsus anime, imo tocius ecclesie; et cum hoc conceptus de spiritu sancto tamquam matre sua iuxta illud quod allegat Jeronymus.... Tulit me mater mea in uno capillorum meorum (caro enim est capillus anime), patet quod spiritus sanctus, cum sit mater Christi sponsi ecclesie, est socrus anime que vendicat esse sponsa Christi, quia mater mariti. Et ex eadem consideracione anima pretendens se esse uxorem filii spiritus sancti dicitur nurus eius. Heretici ergo qui pretendunt se esse nuros spiritus sancti quem vendicant socrum suam, separantur ab eo per Christum detecta eorum fallacia, et ita cum universalis ecclesia sit domus domini Jesu Christi, et per consequens, omnes heretici qui sunt facietenus in ecclesia sunt pretense eius domestici, patet quod omnes illi sunt illi homini patrifamilias inimici. Huius inquit Jeronymus inimici sunt qui putantur in domo Christi esse, hoc [p. 41] est, in ecclesia et palliantes a capite non recedere contra caput sentiunt. Heretici inquit cum ante crediderint scripturis que a spiritu sancto scripte sunt et edite, transferunt se ad novas doctrinas et fermentum phariseorum et mandata hominum, dumque sermonem Dei contempnunt, socrui sue faciunt iniuriam.

[ENGLISH]

## ¶2 · 41.7–41.31

> [p. 41] Christus ergo ex vita et doctrina venit confutare hereticos, ut discernantur a fidelibus et postmodum separentur. Et ita subtiliter et catholice potest intelligi secundum hunc sanctum per filium, filiam et nurum hereticus qui pretense et false se nominat filium Dei patris, filiam matris sue, sapiencie Dei patris et nurum spiritus sancti et sic cognatissimum trinitati. Sed vita et doctrina Christi sunt optimum speculum, ubi possunt hec discerni, cum manifestum sit quod omnis homo et solum talis qui est in vita et doctrina Christo contrarius est hereticus, et omnis christianus et solum talis qui est in vita et doctrina Christo conformis est ut sic ab heresi elongatus. Christus ergo venit non ad faciendum primam separacionem que est proprie per peccatum, sed ad faciendum sequentem, ut per eum discernantur heretici et ab ecclesia separentur. Et hec racio quare oportet omnem catholicum cognoscere scripturam sacram. Et certus sum quod, licet prelati nostri ipsam et professores suos dissipant et conculcant, lapides clamabunt, hoc est, seculares domini in sensu scripture a domino illustrati defendent fidem catholicam, quia pharisei volentes obturare ora discipulorum scripturam istam confitencium audierunt divinum responsum: Dico vobis, quia si hii tacuerint lapides clamabunt, Luce XIX°, 40. Magnam enim vim habet veritas scripturarum.

[ENGLISH]

## ¶3 · 42.1–42.9

> [p. 42] Secundo principaliter obicitur per hoc quod iuxta supradictam sentenciam nullus laicus teneretur credere de sacerdote suo, curato sive episcopo quod sit membrum ecclesie vel vere habens nomen talis officii, et periret omnis honor impendendus prelatis et fides populi laicalis; immo nullus viator teneretur credere Romane ecclesie in canonizando sanctos de privatis provinciis et titubaret cultus ecclesie in solemnizando festa et reliquias sanctorum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 38.25: Objection: Subjects will have to consult Scripture before obeying the Pope. Answer:
- 38.29: They ought to do so.
- 39.24: St. Jerome on the sword sent by Christ.
- 41.13: The life and teaching of Christ are the glass, by which heretics may be discerned.
- 42.1: Objection: All respect for the clergy would perish.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 39: *Christi* [R3]
  - 39: *Act.V°* (token prints as 'Act.V°,' (no space); degree sign present) [R3]
  - 39: *Christus* [R3]
  - 39: *Christus* [R4]
  - 40: *Simulant* [R3]
  - 40: *Christus* [R3]
  - 40: *Christi* [R3]
  - 40: *nuros* (print has nuros) [NW]
  - 41: *cum* ('Christ' is side-note text glued) [R4]
  - 38: *obediencia* (obe- here, 133c diencia at top of p.39; main token holds whole word) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 38:
1. In codd. orditur. 2. 3.B: caput nostrum ecclesie. 3. 4. B: influit
modum. 6. A A,: sapida sentire. B in marg: Ecce quomodo Urbanum
esse caput nostrum dicit csse lidem credendam cum formidinc. 21. In
codd. sibi tam. 23. AA,: regcm. Et. 25. AB in marg: Obieccio
prima. A in marg: Contra dicta. 28. AB in marg: Responsio. 3o. B
et conscqucns.
5. Lucae XVII, 3y. 21. Eph. V. 21.

p. 39:
3. A in marg: In obediencia ad superiorem consulenda est scriptura
sacra. (Above i33c ; without markof reference.) 4-Incodd: in ordinarunt.
Correxi. II. B: concor(diter) contradicunt. 12. B in marg: Math. 10,
Act. 5. 16. A in marg: Dissolucio carnalis amicicie. 24. B in marg:
Michee 7. 23. AB in marg: Jeronimus; B: exponere exponere. A iri
marg: Divisio hereticorum ab ecclesia. 25. 26. B in marg infcr. : Christus
venit ad separandum hcreticos ab ecfciesia quam illudunt. Pater autem
heretici estDeus: pater sccundum creacionem et mater ecclesia secundum
hcretici prctensionem. Spiritus sanctus est socrus animc, cum sit mater
9. With rcterencc to the legio Thebaica see Bordieu diss. crit.
sur la martyre de la legion Thebeennc. Amst. 1705. 20. Com-
mentar. Hieron. in Mich. proph. lib. II, cap. VI. (Migne tom. XXV,
pag. 1281).

p. 40:
sponsi anime seu ecclesie. Anima vero est nurus spiritus sancti, cum se
pretendit esse sponsam lilii spiritus sancti, qui lilius dicitur esse Christus.
Hcreticus ergo prctendit se lilium, filiam et nurum, quem Christus venit
separare a patre, matre et socru. Et patet brevissima textus : Veni separara
hominem adversus palrem suum et Jilium adversus matrem.
1. B: quod sint dei. 2. B: lilie matris sue pro quibus viribus.
5. 6. B: contrivit. B in marg infer.:
Deus pater per creacionem,\ /Hereticus pretensus iilius per adopcionem,
Ecclesia nurus, \ { Hereticus filia secundum pretensionem,
Spiritus sanctus socrus ' ^Hereticus nurus secundum simulacionem.
12. Jeronymus: in codd. seq. lacuna. i5. In codd: ecclesie quod.
Correxi. 21. B: et igitur. 25. AB: huiusmodi inquit. A, correxit:
huius; vid. Comm. Hieronymi 1. c.
6. Commentar. Hieronymi in Michaeam 1. c. pag. 1180.

p. 41:
1. In codd. false: hoc est ecclesia. 4. B : transferuntur; ibi incodd.:
ecce transferunt. 9. B: possunt intelligi. 12. B in marg: Quomodo
hereticus est filius matris sue sapicncic Dci patris. i3. B: Scd et vita.
[4. AA,: ubi poterunt discerni. AB in marg: Conclusio. 18. B in
marg: Nota: quid cst hereticus 21. B in marg (ad prior. loc. pertinet)
Tulit me mater mea in uno capillorum meorum. 27. B: catholicam et
pharisei. 28. A: abturare. 3o. B in marg: Luce 19.

p. 42:
i. A B in marg : Secunda obieccio. i. B : iuxta deest. 2. B: tenetur.
10. A B in marg: Responsio. n. A in marg: Fides. i3. B: habitum.
14. B in marg: Fides sumitur tripliciter secundum Augustinum. Ibid:
Augustinus. ifi. B: Secundo dcest. 17. Fidelis; Hus addit: hominis.
A in marg: Fidei distinccio. Ibid.: Fidcs de ecclesia catholica cum cari-
tate sufficit ad salutem (both thesc glosses below i33d without mark ot
reference). 21. B: singulare.
14. Opp. August. VIII, pag, (J29.
```

---

## Chunk 02-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-02-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-02-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "42.10–47.5"
divisions: "cap. 2 (heading 'CAP. II.' at 25.23); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1117 words; 1064 unanimous or majority-real; 40 settled by vote (R2 14, R3a 20, R3b 1, R5a 3, R6a 2); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n79–n84 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 2, part 6: [TITLE]

## ¶1 · 42.10–43.23

> [p. 42] Sed constat ex dictis quod neutrum sequitur, sed eius oppositum; pro quo notandum quod fides nunc sumitur pro actu credendi quo creditur, nunc pro habitu credendi per quem creditur, et nunc pro veritate que creditur, ut docet Augustinus XIII°, De Trinitate capitulo II° et III°. Secundo notandum quod alia est fides que est credulitas fidelis explicita et alia fides implicita, ut catholicus habens habitum fidei infusum vel acquisitum explicite credit ecclesiam catholicam in communi, et in illa fide communi credit implicite vel confuse quodcunque singulare contentum sub sancta matre ecclesia, sicut logici vere dicunt quod sciendo ens esse in suo analogo sciunt omnia et singula in communi. Sic (ut sepe dixi) si quicunque christianus habuerit fidem caritate formatam in quantumcunque communi, sufficit cum virtute perseverancie ad salutem. Deus enim qui dedit primam fidem dabit clariorem, nisi fidelis ponat obicem. Non enim exigit Deus, ut omnes filii sui pro omni viacione sua cogitent continue in actu particulari de qualibet fidei particula, sed [p. 43] satis est quod postposita desidia habeant fidem in habitu formatam. Ex istis patet tercio quod quilibet laicus fidelis tenetur credere quod habet Christum sacerdotem suum, rectorem, episcopum atque papam, et sic de aliis sanctis Christi vicariis. Sed accedendo ad difficultatem dicitur: cum actus sunt suppositorum singularium et nostri fideles laici communicant cum suis presbyteris et curatis, necesse est quod habeant fidem de illis: ideo laici tenentur de aliquibus prepositis suis credere saltem implicite quod sunt partes ecclesie et capita sua, et de aliis non tenentur, et utrumque membrum potest subdividi, vel quod tenentur credere sic de illis secundum presentem iusticiam vel simpliciter secundum predestinacionem. Tunc dicitur quod laici non tenentur credere aliter de suo preposito nisi verum. Patet sic: Nemo tenetur quidquam credere, nisi quod Deus movet eum credere; sed Deus non movet hominem ad credendum falsum: ideo non debet credere falsum; licet enim ex fide falsa quandoque bonum proveniat et Deus moveat ad substanciam actus, tamen Deus non sic movet hominem, ut fallatur (ut patet libro sexto, tractatu de mendacio, capitulo

[ENGLISH]

## ¶2 · 43.24–44.7

> [p. 43] Ex istis patet secundo quod pastor tenetur monere subditos suos per instrucciones operum virtuosorum, ut fidem sibi adhibeant quod sit talis. Patet ex hoc quod aliter acceptando tale officium peccaret mortaliter, ymmo inducendo hostes in ecclesiam domum Dei foret proditor Dei sui. Quando ergo subditus non cognoscit talia fructuosa opera sui prepositi, non tenetur credere quod sit talis. Si autem cognoscit implicite, tenetur proporcionaliter credere, et quando [p. 44] cognoscit explicite, tunc tenetur credere quod sit talis secundum presentem iusticiam et cum formidine ac condicionaliter quod sit talis simpliciter (ut dictum est superius de papa nostro). Non enim oneravit Deus sic suam ecclesiam, ut necessitata sit falsum credere de suis prepositis cum hoc quod non dent materiam sic credendi.

[ENGLISH]

## ¶3 · 44.8–46.22

> [p. 44] Ad aliam difficultatem de canonizacione sanctorump patet quod correspondenter quodammodo est dicendum: Quamvis enim sit vehemencior evidencia ex testimonio Romane ecclesie quod persona quam canonizat sit membrum ecclesie triumphantis, et amplior evidencia, si pro sancto Deus operetur miracula, tamen utrobique in tali materia potest esse illusio. Nam sicut ex confessione legum ecclesie ipsa militans decipit et decipitur (ut patet V° decretalium, de sentencia excommunicacionis A nobis) in tantum quod quandoque multos excommunicat qui sunt soluti et valde acceptabiles quoad Deum: sic contingit quod aliquos absolvat et ascribat cathalogo sanctorum cum hoc quod apud Deum sint iustissime condempnati. Ideo absit christianum credere quod de necessitate salutis oportet omnem fidelem credere explicite de isto et quocunque quem ecclesia nostra canonizat, ut eo ipso sit beatus, quia tunc haberemus simbolum nimis longum. Nec debemus explicite credere de quoquam tali quod non sit sanctus, sed excuciendo consideracionem de talibus, adherendo parti nobis probabiliori, credendo cum condicione vel pie cum formidine dubitando; de aliquibus autem sanctis credimus absque formidine eciam explicite quod sunt sancti, ut de apostolis, martiribus et sanctis primitive ecclesie; de aliis autem [p. 45] modernioribus qui canonizantur racione parentele, questus vel muneris non oportet nos apponere tantam fidem; nec quemquam canonizatum intendo asserere vel defendere non esse partem ecclesie triumphantis, sed cum quadam formidine dubito, si hoc credo, cum scio quod hoc est possibile; et hoc existente vero credo illud implicite quod ignoro, nec volo contendere ad probandum proterve de quolibet citra Christum quod sit beatus, quamvis de multis hoc credam absque formidine. Nec miracula iam currencia dant omnibus veram fidem, cum potest committi potestas diabolo in penam peccati generacionis adultere signa querentis et fidem necessariam insensibilium dimittentis, ut portentis suis antichristiane inducant plurimos in errorem (de quorum indiciis dictum est libro sexto, sexto capitulo). Solet autem vocari miraculum nunc materialiter quodcunque opus a Deo miraculose factum, et sic sollicitantur multi ad deducendum conclusiones male sonantes, cum quelibet creatura videtur sic esse miraculum quoad Deum. Sed formaliter sumiter miraculum pro operacione Deo propria mirabili creature, et sic beati non faciunt miracula, licet sint quandoque occasio, ut Deus ad instanciam precum eorum seu menti faciat miraculum. Et tunc dicuntur hn facere tale miraculum subauctentice vel ministratorie sicut solent. Et illa discrecio miraculi est eis abscondita nisi quibus Deus revelare voluerit. Et utinam non multiplicarentur tot ceremonie et signa in nostra ecclesia, cum facta sanctorum et omnes ritus alii non sunt laudabiles, nisi de quanto elevant animum ad [p. 46] diligendum dominum Jesum Christum. Et videtur multis quod fides confusa de oracione sanctorum unicius, et per consequens, intencius, securius et melius colligeret in chnsticolis fidem Christi quam tanta explicita multiplicitas sanctorum in dies introducta. Sic enim confuse cognoscimus de quolibet beato vel dampnato, prescito vel predestinato quod ipse est huiusmodi, cum qua confusa noticia stat dubietas particularis, et ignorancia cum distincta noticia de communi: ex tali itaque canonizacione multiplici ultra ritum veteris testamenti et nostre primitive ecclesie secundum partem prodest et secundum partem obest; et verisimile est multis quod plus nocet, cum multitudo ritus tollens libertatem ecclesie est causa multorum errorum. Et omnis talis sanctus oraret pro nobis efficacius, supposito quod dimisso cultu suo diligeremus amplius Jesum nostrum. Multi enim sunt sancti nobis incogniti canonizatis beaciores qui plus prosunt nobis orando quam dicti sancti quorum festa devocione particulari percolimus, cum secundum dignitatem elemosinarii prosit oracio sanctorum qui plus diligunt eos qui magis diligunt Deum suum.

[ENGLISH]

## ¶4 · 46.23–46.23

> [p. 46] Est et aliud malum ecclesie, quod superiores nostri

[ENGLISH]

## ¶5 · 46.24–47.5

> [p. 46] exigunt ut credatur suis approbacionibus et reprobacionibus in cunctis suis iudiciis, quam exigunt ut credatur fides sacre scripture que est fides catholica, et plus persequuntur pro complecione suarum tradicionum, puniendo contravenientes asperius, quam faciunt contra blasphemantes in precipuam fidem Christi, sic quod de eis dici potest illud Psalmi XLI, 10: Qui edebat panes meos magnificavit super me supplantacionem. Voluptuosus quippe presidens sub pallio pacis ecclesie querit bona pauperum que sunt autonomatice [p. 47] panes Christi, et ille magnificat phariseice tradiciones proprias quibus tyrannice spoliat populum cui dicit verbo et opere quod equivalent vel superant legem Dei. Hoc autem est in effectu supplantacio legis

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 42.15: Distinction between explicit and implicit faith.
- 43.3: Whiat men are to think of their priests.
- 43.24: The pastor is bound to show himself by good works a part of the Church.
- 44.8: Canonization not a certain proof of sanctity.
- 45.10: Nor do miracles prove sanctity.
- 45.23: Saints do not work miracles, though they may be the occasion of them.
- 46.1: A general trust in the prayers of the Saints would be better than individual honours to them.
- 46.23: Prelates punish more severely breaking of their laws than of Christ's.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 42: *II°* [R3]
  - 42: *Secundo notandum quod alia est fides que est credulitas fidelis explicita et alia fides implicita, ut* (print has both lines (p.42 ll.16-17) before catholicus) [GAP]
  - 42: *viacione* (print has viacione) [NW]
  - 43: *Christum* [R3]
  - 45: *Christum* [R4]
  - 46: *securius* (print has securius (r-i-u), not secunus) [NW]
  - 46: *Christi* [R3]
  - 46: *Christi* [R3]
  - 46: *diligendum* [THIN]
  - 46: *Jesum* [THIN]
  - 46: *videtur* (134b folio mark glued) [THIN]
  - 46: *fides* [THIN]
  - 46: *confusa* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 42:
i. A B in marg : Secunda obieccio. i. B : iuxta deest. 2. B: tenetur.
10. A B in marg: Responsio. n. A in marg: Fides. i3. B: habitum.
14. B in marg: Fides sumitur tripliciter secundum Augustinum. Ibid:
Augustinus. ifi. B: Secundo dcest. 17. Fidelis; Hus addit: hominis.
A in marg: Fidei distinccio. Ibid.: Fidcs de ecclesia catholica cum cari-
tate sufficit ad salutem (both thesc glosses below i33d without mark ot
reference). 21. B: singulare.
14. Opp. August. VIII, pag, (J29.

p. 43:
3. AB in marg: Conclusio; Ainmarg: De prepositis quoniodo tencn-
tur subditi credere. (Above i34»without mark of referencc.) B in marg:
Hic nota, quomodo credendum est prepositos nostros esse partcs ccclesie.
Ibid.: Laici tenentur credere de aliquibus suorum prcpositorum quod
sunt partes ecclesie. 23. B quinto; tractatu de mendacio in marg, non in
tcxtu. Liber sextus is I suppose the Dc Veritate S. Scripture.

p. 44:
4. B: ornavit. 8. A in marg: de canonisacione sanctorum ab
ecclesia Romana quomodo est credendum. 16. A: patet deest. B in
marg: V. decretalium. 19. A in marg: De sanctis quomodo est
credendum. (Above i34b without mark of reference.) 3l. B: quod deest.
16. Decr. Gregr. IX, lib. V, tit. XXXIX, cap. XXI. A nobis.

p. 45:
i. B in marg: Quomodo sciendum est de canonisacione sanctorum
modernorum. 5. B: formidine subito. n. B: unam (idem. 12. AB:
generalis. A,: genera''. 14. Codd: antichristine. 16. B: quinto
capitulo. 17. A in marg: De miraculis. Miraculum quid est? AB in
marg: Miraculum. 21. B in marg: Miracalum dupliciter sumitur.
25. B in marg: Miraculum lit a sanctis subautentice. 3i. B in marg:
De quanto sunt ritus laudabiles.

p. 46:
2. B in marg: De oracione sanctorum. 23. B in marg: Prelati
exigunt quod suis sentenciis adhibeatur fides quarum transgressores
vehementer puniunt. 28. B: punientes. 3i. B in marg: Qui edebat
panes meos magnificavit supcr me. 32. B: Voluptuosus — Christi etc.

p. 47:
i. Codd: auionomasiice. 5. A: elc. Kcnmerton psano (written).
Kenmerton — Kemenon, a vi lage near Tewkesbury in Worcestershirc.
The neighbourhood is men.ioned in Walsingham (II, 3oy) as liaving sent
supporters to Sir John Oldcastle. 7. A in marg: Contra dicia arguitur.
14. Ain raarg: Conclusio. 24. capit. seq. lacuna; Ainmarg: Augu>tinus.
5. Ad cap. II, cf. Hus, De eccl. fol. 199% seqq. 204'', 2oc)h, 1 1 2" etc.
24. Decreti secunda pars, causa VIII, q. I, cap. XIX. 16. Ad
Philipp. II, 21.
```

---

## Chunk 03-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "47.7–51.7"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 1 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "850 words; 780 unanimous or majority-real; 52 settled by vote (R2 33, R3a 13, R5a 5, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n84–n88 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 1: [TITLE]

## ¶1 · 47.7–47.13

> [p. 47] Sed tercio principaliter obicitur per hoc quod, data ista sentencia, tolleretur omnis exaccio debiti ecclesie et extingueretur omnis lex contencionis m clero, cum debitor posset fingere ecclesiasticum non esse dignum vel talem qui sic bona ecclesie vendicaret, et quantum ad excommunicacionem que est ultimum refugium, diceret quod non ligat.

[ENGLISH]

## ¶2 · 47.14–48.22

> [p. 47] Hic dicitur quod, si lex Dei debite scrutaretur nobis, non tantum contenderemus circa bona ecclesie, cum manifestum sit quod prescitus vel quicunque clericus sine peraccione sui ministerii compensante qui plus propter honorem, voluptatem vel questum seculi contendit, bona ecclesie occupat vel acceptat, quam propter honorem Dei et edificacionem ecclesie, ut sic false aliena vendicat et consumit, et per consequens, licet versucias talium detegere et subtrahendo bona pauperum resistere (ut diffuse dictum est lib. VI, cap....), unde sub auctoritate beati Augustini scribitur in decretis VIIIª, q. 1: Sunt inquit quidam in ecclesia prepositi de quibus apostolus Paulus dicit: Sua querentes, non que Jesu Christi. Quid est: Sua querentes [p. 48] non Christum gratis diligentes, non Deum propter ipsum Deum querentes, temporalia consequentes, lucris inhiantes, honores ab hominibus appetentes. Hec quando amantur a preposito et propter hec servitur Deo, quisquis talis est, mercenarius est, inter filios se non computet. of Unde quia omnes confitemur nos principaliter propter honorem Dei et spiritualem profectum ecclesie tales preposituras appetere, ad discernendum si sumus ypocrite, oportet credere operibus nostris, specu scripture et testimonio sanctorum. Unde Gregorius XXXI°, Moral. cap. IX, et infra, satis explicat istam materiam in tribus conclusionibus; supponens primo quod mens iusti vel veri christiani debet esse tam affectu quam intellectu collecta intrinsecus, sic quod nichil suum exterius derelinquat. Patet ex hoc quod aliter peccaret contra hoc mandatum: Diliges dominum Deum tuum ex toto corde, ex tota anima et ex tota mente. Cum ergo non debet peccare, sequitur quod non debet esse fracta sic in intellectu et affectu circa temporalia, quia ut sic amor uni debitus dispergitur circa multa.

[ENGLISH]

## ¶3 · 48.23–50.7

> [p. 48] Isto supposito patet, primo quod sancti dum se intra semet ipsos sic colligunt, occulta tam de statu proprio quam de statu proximi comprehendunt. Patet ex hoc quod lux vera que non potest personas accipere, necessario secundum capacitatem irradiat talem mentem. Et hoc figuratum est Ezechiel VIII, 3, ubi sic legitur: [p. 49] Emissa similitudo manus apprehendit me in cincinno capitis mei et elevavit me spiritus inter terram et celum et adduxit me in Jerusalem in visione Dei iuxta ostium interius quod respiciebat ad aquilonem, ubi erat statutum ydolum zeli ad provocandum emulacionem. Manus missa est operativa volucio divina, cincinnus capitis est collecte cogitaciones mentis quibus habitis mens incomplete trahitur a terrenis, cum nec habet animum omnino celestem nec omnino in terrestribus soporatum, sed inter terram et celum in visione Dei in Jerusalem ducitur, quia zelo caritatis qualis debet esse mater ecclesia contemplatur. Et signanter animus talis adducitur ad ostium interius quod respicit ad aquilonem, quia interna contemplacione intra ecclesiam plus prava quam recta fieri deprehendunt, dum clerici in aquilonis pariete, id est, ad solis sinistrum oculos flectunt et elongata austerna caritate habundant frigore viciorum; cuius causa est globus temporalium quem ecclesia sola specie fidelis adorat; ex hinc enim zelus sponsi ecclesie ad feriendum ypocritas provocatur. Secundo patet ex quo signo perpenditur, si ecclesiastici flagrant terrenis, celestibus pretermissis: cum enim amor sit pondus animi, nec sit possibile hominem moveri libere quo affeccio mentis ipsum non tulerit, patet quod ex operibus debet mentis affeccio iudicari. Si ergo vides quod ecclesiasticus quantum ad perpetuacionem, quantum ad defensionem et quantum ad amissionem temporalium plus insudat, quam facit pro spiritualibus, quis dubitat quin eis magis afficitur? Unde quantum ad perpetuacionem temporalium sic [p. 50] loquitur iste sanctus: postposita quippe cura filiorum sepe eos videas se contra pericula immensi laboris accingere, maria transmeare, adire iudicia, pulsare principatus, palacia irrumpere, iurgantibus populorum cuneis interesse. Cum autem pro spiritualibus acquirendis non apponunt tantam diligenciam, quis dubitat quin ista temporalia magis amant?

[ENGLISH]

## ¶4 · 50.8–51.7

> [p. 50] Et quantum ad retencionem, patet idem ex maioritate diligencie quam apponimus pro temporalibus quam pro spiritualibus defendendis. Ypocrita, inquit Gregorius, assumpto sancte conversacionis habitu filiorum custodiam deserit et temporalia queque defendere eciam iurgiis querit. Exemplo suo eorum corda perdere non trepidat et quasi per negligenciam amittere patrimonia terrena formidat. In errorem discipulus labitur et tamen cor ypocrite nullo dolore sauciatur. Ire in iniquitatis voraginem commissos sibi conspicit et hec quasi inaudita pertransit; at si quod sibi leviter inferri temporale dampnum senserit, in ulcionis iram repente ab intimis inardescit. Et mox paciencia rumpitur, mox dolor cordis in vocibus effrenatur, quia dum animarum dampna equanimiter tollerat, iacturam vero rerum temporalium repellere eciam cum spiritus commocione festinat, cunctis veraciter indicat teste mentis perturbacione quid amat. Ibi quippe est grande studium defensionis, ubi est grandior vis amoris. Et quoad amissionem bonorum hominis, est idem indicium, quia indubie quicunque plus dolet de amissione boni fortune quam boni virtutis, ut sic, indicat se plus diligere temporalia quam virtutes, cum sit maxima apud philosophos quod dolor amissi et amor [p. 51] habiti suis temporibus correspondent. Unde Gregorius ubi supra: Quanto magis terrena quis diligit, tanto privari eis vehemencius pertimescit. Qua enim mente in hoc mundo aliquid possidemus, non docemur nisi cum amittimus. Sine dolore namque amittitur quidquid sine amore possidetur, que vero ardenter diligimus habita, graviter suspiramus ablata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 47.7: Objection: This would disable the clergy from enforcing their dues.
- 47.14: Answer. It would be better if dues were less enforced
- 48.7: Our pretence of good motives must be tested by our acts and by Scripture.
- 49.1: Explanation of Ezekiel's vision.
- 49.22: How we may judge whether priests are worldly:
- 49.27: by eagerness to obtain wealth;
- 50.8: by care to keep
- 50.28: by grief for its loss.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 47: *CAP. III.* [HEAD]
  - 47: *qui* (134d is the folio mark) [R4]
  - 47: *lib* (print 'lib. VI,') [NW]
  - 47: *VIIIª* [R4]
  - 47: *1* (x-height old-style figure 1 ('q. 1:'), checked on leaf) [R3]
  - 47: *Quid* [R4]
  - 48: *non* (first word of page, italic) [R3]
  - 48: *occulta* (zoomed on leaf: second c has an ink speck inside but no e-bar = c) [NW]
  - 49: *manus* [R3]
  - 49: *ubi* (5 is the line number) [R3]
  - 49: *zelo* (italic z) [NW]
  - 49: *Et* (135a is the folio mark) [R4]
  - 49: *ad* (print 'adducitur ad * ostium') [INS?]
  - 50: *loquitur* [R3]
  - 50: *∅* ('keep' is side-note text (by care to keep it)) [INS?]
  - 50: *∅* ('its' is side-note text (by grief for its loss); line starts Et) [R4]
  - 50: *indicat* (30 is the line number) [R3]
  - 51: *habiti* (135a is the folio mark) [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 47:
i. Codd: auionomasiice. 5. A: elc. Kcnmerton psano (written).
Kenmerton — Kemenon, a vi lage near Tewkesbury in Worcestershirc.
The neighbourhood is men.ioned in Walsingham (II, 3oy) as liaving sent
supporters to Sir John Oldcastle. 7. A in marg: Contra dicia arguitur.
14. Ain raarg: Conclusio. 24. capit. seq. lacuna; Ainmarg: Augu>tinus.
5. Ad cap. II, cf. Hus, De eccl. fol. 199% seqq. 204'', 2oc)h, 1 1 2" etc.
24. Decreti secunda pars, causa VIII, q. I, cap. XIX. 16. Ad
Philipp. II, 21.

p. 48:
habetur in decretali supra memorata. 4. in codd: preposito propter.
6. A in marg: Nota qui sunt qui diligunt que sua sunt, non que domini
Jesu Christi ; ib: Contra clerum pravum et avarum. (This gloss above i34d
without mark of reference). 7. B: contitemur nec principaliter.
12. A in marg: Gregorius. 23. AB in marg: Prima conclusio.
24. Verba Gregorii . . . colligunt, mira ac pcnetrabili acie occulta eciam
aliena delicta deprehendunt ; B: statum. 2S. B in marg: Ezech.VIII.
ibid: Emissa similitudo manus apprehendit me in cisinno (sic) capitis etc.
12. Greg. Moral. XXXI, cap. XII (vel IX) Opp. tom. I, ioo5.
18. Matth. XIII, 37.

p. 49:
1. A in marg. : cincinnus. 4. Codd.: respicit. Correxi. 5. B : statum.
7. AA,: colore cogitacionis. i5. AA, : intcr. 18. A in marg. : Pastor
negligens continue infra. (Above i?5".) 22. A B in marg.: Secundo con-
clusio. B in marg.: Nota optimc quomodo vere discernendtim est, quis
appetit preesse in ecclesia propter lionorem Dei ct spiritualem profectum
animarum. 25. B: atfecto.
7. and 11. Gregorius I. c.

p. 50:
10. AB in marg. : Gregorius. 16. 17. B: rei in. 18. AA,: at sibi
quid. B: at si quid sibi. 28. A in marg. : Amissio temporalium est
minus dolenda quam amissio virtutis.
1. Gregorius 1. c. 10. 1. c. cap. XIII.

p. 51:
i. A B in marg. : Gregorius. 2. A : in terrena. 3. B: Contra enim
mente. 8. AB in marg. : Tercia conclusio. A in marg. : Contra defen-
sorcs iurium ct consuetudinis humanc gracia proprie avaricie et victoric.
l5. AB in marg.: Gregorius. 16. B: dicitur, cur certa; ibid: in codd:
ita agitis. 22. B in marg. : Contra eos qui se dicunt contenderc
debere pro acquirendo bona ecclesie, dato quod presint in ccclesia Dei.
23. A in marg. : Nota fucum. 25. B in marg. : Augustinus.
10. 2. Timoth. III, r. 25. Aug. In Joh. evang. trac. VI.
Opp. III, pars II, pag. 33o seqq. 26. August. Annot. in Job.
Opp. III, 1, pag. 675. Gregor. 1. c. cap. XIII.
```
