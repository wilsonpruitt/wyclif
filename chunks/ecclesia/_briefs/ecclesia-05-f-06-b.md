# Translation brief: ecclesia 05-f–06-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-05-f.md chunks/ecclesia/wyc-ecclesia-06-a.md chunks/ecclesia/wyc-ecclesia-06-b.md` once and fix what it reports.
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

## Glossary (the 127 rows these chunks use; the full file is GLOSSARY.md)

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
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |

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
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 05-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-05-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-05-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "112.10–115.33"
divisions: "cap. 5 (heading 'CAP. V.' at 92.6); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "937 words; 853 unanimous or majority-real; 69 settled by vote (R2 37, R3a 26, R3b 1, R5a 4, R6a 1); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n149–n152 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 5, part 6: [TITLE]

## ¶1 · 112.10–114.12

> [p. 112] In ista vero materia est quidam doctor describens ecclesiam sub hac forma: Ecclesia, inquit, est universalis multitudo omnium christianorum, habencium ex integro rectam et eandem fidem per Christum et apostolos divulgatam et a sanctis patribus et consiliis generalibus declaratam. Et patet quod loquitur de una sancta ecclesia catholica, quia aliter non assumeret pro genere quod ipsa ecclesia sit multitudo omnium christianorum. Primo, inquam, videtur quod nulli patres veteris testamenti fuerunt de illa ecclesia, quia illa non fuit antequam Christus eam genuit per effluxum sanguinis et aque de suo latere dormientis in cruce (ut dicitur Joh. XIX° 34), sed hoc non fuit pro tempore patrum veteris testamenti, ergo nec illa ecclesia. Ex quo sequitur quod cum extra illam ecclesiam non est salus (ut patet in extravagante Bonifacii VIII1. Unam sanctam), nullus patrum veteris testamenti salvabitur. Non enim foret pertinens decreto dicere quod extra unam sanctam et catholicam ecclesiam non est salus nisi intenderit quod nemo salvabitur nisi fuerit de illa. Secundo sequitur quod Christus non sit de illa ecclesia quia non est de universali multitudine omnium christianorum, eo quod non est [p. 113] christianus, sed ipse Christus a quo dicitur quilibet christianus, et per consequens, nec est de numero salvandorum nec caput nec aliqua pars ecclesie catholice. Nam a Christo ut capite denominantur fideles servi Christi christiani (ut patet Act. XI°, 26). Ergo sicut Romanus non est Roma nec Israhelita ipse Israhel, et breviter, nulla generacio passiva est ipsum principium generans, sic nullus christianus est Christus sed Christi, et periret fides scripture de capite et de membris ecclesie; et multo evidencius sequitur quod beata virgo non fuit membrum illius ecclesie, quia in sancto triduo non fuit illa ecclesia nec fuit posterius sibi incorporata. Tercio sequitur quod nulla sit talis ecclesia, quia nulla multitudo omnium christianorum habet ex integro eandem rectam fidem, tum quia defective et corrupte habet multitudo omnium christianorum fidem Christi, tum eciam quia nullam unam fidem habent omnes illi christiani nec pro specie nec pro aggregato. Nec valet hoc sophisma: Isti habent fidem, sed nullam fidem habent. Nec valet fingere fidem que creditur, quia talia negantur a sic describente, et illis positis inculte aggregantur in descripcione tam anxie elaborata. Nam multi christiani habent fidem valde peccatis obliquatam, tam presciti quam predestinati, et multi simpliciter infideles habent fidem creditam valde rectam. Quarto sequitur quod nec apostoli nec alii fideles erant de ecclesia, antequam fides fuit per Christum et apostolos divulgata et a sanctis patribus in consiliis generalibus declarata; quod fuit diu post ascensionem domini et mortem apostolorum. Nam nemo fuit de ecclesia catholica, antequam illa fuit, sed illa non fuit, antequam fuit ita quod illa est: sed cum non fuit ita quod illa [p. 114] est, antequam dicta conscripcio sibi compeciit, sequitur quod tunc primo fuit ecclesia; quod esset valde inconveniens, primo quia Christus ex latere suo non formasset ecclesiam, secundo quia nulli fideles fuissent de ecclesia ante consilia dicta generalia, et sic beatus Stephanus et multi alii christiani fuissent mortui extra fidem ecclesie; tercio quia complentes prima consilia post ascensionem fecissent primo ecclesiam catholicam, quia posito quod essemus per diem ante prima consilia, post ascensionem foret nobis verum quod nondum est ecclesia catholica, quia nondum verificata est descripcio.

[ENGLISH]

## ¶2 · 114.13–114.22

> [p. 114] Quinto sequitur quod, ut generabuntur et morientur fideles, erit nova et nova ecclesia catholica, et per consequens, forent plures quam mille ecclesie catholice; quod est contra decretalem Bonifacii Unam sanctam. Et consequencia videtur ex hoc quod ut sic erunt nove et nove multitudines christianorum, et per consequens, non manebit per tot et tantas transmutaciones eadem ecclesia in numero, sicut patet querenti diligenter quid foret illa ecclesia que sic continue remaneret.

[ENGLISH]

## ¶3 · 114.23–114.30

> [p. 114] Sexto sequitur quod omnes presciti in gracia forent membra ecclesie catholice, et nulli predestinati dum erraverint in fide forent partes sancte matris ecclesie; quorum primum videtur falsum de Scarioth et aliis hereticis, et secundum videtur fuisse falsum de David, Petro, Paulo et eis similibus pro tempore quo fuerunt infideles. Quorum utrumque est contra sanctorum sentencias et raciones factas superius.

[ENGLISH]

## ¶4 · 114.31–115.33

> [p. 114] Septimo videtur quod non sit ecclesia triumphans, eo quod in patria non habuit fidem ut dicitur. Jit sic nulla multitudo erit perpetuo ecclesia sponsa Christi, vel aliter ecclesia ad sui perfeccionem fiet non ecclesia quod est contra scripturam et racionem. [p. 115] Octavo videtur quod ecclesia catholica nullibi sit nec aliquam partem habet, cum nichil sit, et sic ecclesia Romana non foret dignior aut indignior quam ecclesia catholica. V Istas evidencias facio, ut dicatur seriose ad materiam et formam racionum, nullibi declinando a veritate de virtute sermonis, quia sentenciam quam ego exposui de ecclesia volo defendere de virtute sermonis, communicando capciosissime sophiste et cuicunque fideli vel infideli volenti quantumlibet protervire. Si autem ista descripcio non sit valida, ad quid ponitur pro cognoscenda sancta matre ecclesia? Nono videtur, supposita communi logica iam currente, quod ecclesia universalis non sit aliquid, quia nec substancia nec accidens, et per consequens, cum nulla sit pars universalis ecclesie, ipsa foret tam quantitative quam qualitative indivisibilis, et per consequens, nec dominus papa nec Romana ecclesia foret caput universalis ecclesie, eo quod non sequitur: Si ipse exercet officium capitis in aliquos istorum, ergo in istos, quia pari evidencia diabolus foret caput eiusdem ecclesie et haberet quotlibet capita tam bona quam mala. Decimo et ultimo videtur quoad proprietates et accidencia ecclesie quod ipsa non habet sexus distinccionem, virginitatem, etatem vel alia accidencia que fides scripture sibi attribuit, et per idem, non habet privilegium vel peccatum, temporalia vel regulam vivendi, cum non magis tendat ad unitatem quam membra diaboli, cum in illis sit pax quam Christus Matthei X°, 34, dicit venire dissolvere. Istas instancias pueriles contra rudimenta fidei oportet fidelem clare dissolvere, quia in principiis errorum oportet diligenter obstare, cum eorum admissio abducit in devium.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 112.10: Erroneous definition of the Church as the multitude of Christians who keep whole the true faith.
- 112.20: This definition excludes the O. T. Saints
- 112.31: and Christ himself,
- 113.4: so that he would not be the head of the Church.
- 113.13: The mass of Christians never keeps the faith quite whole.
- 113.26: The apostles would be out of the Church, with all who lived before general Councils had declared the faith.
- 114.13: Death and birth would be always making a new Church.
- 114.23: The Church would include all the foreknown in present grace and exclude all predestinate who were in error.
- 114.31: There would be no Church triumphant.
- 115.1: The Catholic Church would be nothing.
- 115.5: These opinions really follow from the premisses.
- 115.13: There would be no single head to the Church.
- 115.23: The Church would lose all the attributes that Scripture assigns to her.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 112: *∅* (print: In ista vero materia; no de) [INS?]
  - 112: *quod* (1 is a margin enumeration) [R3]
  - 112: *quia* [R4]
  - 112: *fuit* [R4]
  - 112: *Christus* [R3]
  - 112: *sit* [R4]
  - 112: *ecclesia* [R4]
  - 112: *∅* (only one ecclesia in print (pos 232) before quia) [INS?]
  - 113: *Christus* [R3]
  - 113: *generalibus* (genera-/libus hyphenated; main token holds whole word) [R4]
  - 114: *patria* (print has patria) [NW]
  - 115: *distinccionem* (distinc-/cionem hyphenated, 144c folio mark glued; main token holds whole word) [R4]
  - 115: *34* (arabic verse number) [R3]
  - 112: *illa* (output token \\\a stands for printed illa) [OVERRIDE-MARK]
  - 112: *de illa* (box spans de illa; output has only ^e before ecclesia, illa missing) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 112:
t. In codd. cap. XVI. In codd. iterum: epistola XXXII. A in
marg. : Ubi est ecclesia. 10. Bin marg. man. alt.: Diffinicio ecclesie.
A in marg. : Quedam descripcio ecclesie. 16. 17. A: assummeret.
23. A: patrinum. B: patuum. A, correxit: patrum. 24. A
B: quod deest. Aj : sequitur quod. 26. In codd. : sequitur quod
nullus. B: nullus patruum. A, : nullum patrum. 20. B in marg. man.
rec: Extra ecclesiam non est salus

p. 113:
9. AA,: capite et membris. 10. A A, : et multo — ecclesie
deest. 20. B: hoc solum: Isti. 21. AA,: fingere que crcditur.
27. A in marg.: Argumenta contra quandam descripcionem ecclesic
continue infra. (This is below 144» without mark of reference.) 20. In
codd. plerumque : consiliis pro conciliis.

p. 114:
8. B; stetissent. i5. 16. AA,: et per — catholice deest.
32. A,: habent lidem.

p. 115:
o. In codd. so'0. ig. B: ipse exercitet. 27. At: temporale.
3i. A(: pluries contra.
33. Ad cap. V. cf. Hus, De eccl. fol 2o5*\
```

---

## Chunk 06-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "116.2–120.13"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 1 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1091 words; 1000 unanimous or majority-real; 73 settled by vote (R2 46, R3a 22, R5a 4, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n153–n157 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 1: [TITLE]

## ¶1 · 116.2–118.5

> [p. 116] to Sed adhuc instatur finaliter deducendo ad conformia inconveniencia ad qualia adversarii deducuntur. Primo enim videtur quod ecclesia tamquam monstrum habeat mille capita, et sic de aliis membris monstruose fabricatis, et sic foret simul virgo et corruptissima synagoga et Christi ecclesia. Hic dicitur (ut sepe) negando assumptum; nam non sequitur: Ista capita sunt istius, demonstrando sanctam matrem ecclesiam, ergo sunt capita istius, nec sequitur: Ista sunt capita istorum qui sunt ista ecclesia, ergo sunt capita huius ecclesie, quia sunt capita istorum singillatim. Et tamen nullum eorum est caput istorum. Ad hoc ergo quod sinta capita ecclesie, oportet quod ecclesia habeat illa omnia et singula tamquam eius capita. Cum enim caput iuxta Aristotelem dicatur ad aliquid, patet sophistis quod non sequitur: Hoc caput, hic pater vel hoc membrum est huiusmodi, ergo est caput, pater vel membrum illius, nec sequitur: Hoc est caput naturale huiusb capitanei, existentis caput date ecclesie, ergo hoc est caput illius ecclesie. Non enim oportet equivocando in capite, si hoc sit caput capitis, tunc hoc est caput cuiuscunque capitati ab illo capite, et correspondenter de aliis membris. Quelibet enim pars predestinati potest dici pars corporis ecclesie, nullum tamen est membrum ecclesie nisi persona predestinata, et omnis talis est membrum ecclesie sicut proporcionaliter dicendum est in humano corpore. Et patet quod ad noticiam illius materie de sancta matre ecclesia nedum oportet scire theologiam et iura canonica, sed omnino logicam, phisicam et ethicam que omnes subserviunt [p. 117] matri nostre. Sicut enim non sequitur: Pater in divinis generat, et ipse est natura divina, ergo ipsa generat, ita non sequitur: Ista persona capitatur istis capitibus, et ista persona est hec ecclesia, ergo hec ecclesia sic capitatur. Nam ecclesia dicit abstractive multitudinem fidelium secundum racionem qua uniunturin capite; ad quem sensum ecclesia non potest esse non ecclesia vel dampnari. Ecclesia ergo non est monstruose composita. Sed quoad secundum, conceditur quod ecclesia est virgo, cum sit sponsa virginis Jesu Christi ex qua ut vera matre spiritualiter procreamur, et sic est castissima secundum se totam in patria; hic tamen, fornicando cum adulterante diabolo et sic membris eius, multis criminibus parcialiter est corrupta (ut patet ex fide scripture Ezechielis XVIII°). Verumptamen nunquam recipitur ut sponsa beatifice amplexanda in dextera in lecto sponsi, antequam fuerit pura virgo omnimode sine ruga; Christus enim est sponsus virginitatis. Et quantum ad tercium punctum, dicitur quod omnis sinagoga que est pars sancte matris ecclesie est ecclesia, non econtra. Et ideo tam crebro vocatur synagoga in veteri testamento ecclesia, sed non memini quod in novo testamento aliqua particularis ecclesia dicitur synagoga (cuius racio dicta est alibi). Secundo obicitur per hoc quod iuxta dicta sequitur eandem personam verbi esse filium, patrem et sponsum ecclesie; quod est contra leges tam nature quam ecclesie, cum nunquam desponsavit quis licite matrem suam. Hic dicitur concedendo conclusionem assumptam, cum Christus nedum desponsat universalem ecclesiam sed desponsacione perpetua quodlibet membrum eius. Et quantum ad leges allegandas in contrarium, patet quod [p. 118] loquuntur de contractu, de cognacione et desponsacione carnali, non autem spirituali, sicut debemus loqui in proposito et eo debemus eam magis attendere, quo est preciosior, proprior et in scriptura sacra expressior.

[ENGLISH]

## ¶2 · 118.6–118.32

> [p. 118] Nam secundum illam omnes salvandi sunt filii Dei et veri fratres ex utroque parente, ymo secundum logicam Christi rectissimam Matthei XII°, 50: Quicunque filius regni voluntatem patris sui fecerit qui in celis est, ipse suus frater, soror et mater est. Et sic sine distinccione sexus spiritualis omnis christianus predestinatus, sive masculus sive femina, est frater, soror, mater et sponsa Christi. Ideo Canticorum V°, 1, dicitur ecclesie Veni in ortum meum soror mea sponsa. Ymo ecclesia est vere domus Dei, civitas regis iusticie, regnum celorum, ortus conclusus, fons signatus et alia que scriptura ad sensum misticum sibi attribuit. Nam in spiritualibus eadem substancia habet in se sine repugnancia quotlibet raciones vere earum denominaciones, ut exemplariter videre possumus quomodo contrariorum species et intenciones sunt simul in medio et in mente. Et ille qui ignorat hoc est valde indispositus ad cognoscendum catholice illud celeste coniugium. Nam Ysaie XXVI°, 1, dicitur de Christo et sancta ecclesia: Salvator ponetur in ea murus et antemurale. Christus enim secundum divinitatem inmediate complectitur sponsam suam, et secundum humanitatem qua minutus est paulominus ab angelis est antemurale, quia dux belli diro certamine superans hostes ecclesie, et sic de quotlibet racionibus quas omnes apostolus Iª Corinth. XV°, 28 compendiose complectitur, dicens quod Christus est omnia in omnibus.

[ENGLISH]

## ¶3 · 118.33–119.11

> [p. 118] Unde ignari scripture divertunt ad tales pueriles instancias, quando aliunde deficiunt argumenta et dicunt quod scriptura nostra est impossibilis in tantum [p. 119] quod quidam dicunt nullam esse ecclesiam catholicam. quia non est dare universalia ex parte rei. Quidam vero dicunt quod ecclesia est ecclesia, sed non est aliquid sed aliqua, nec aliquod est membrum ecclesie, et sic scriptura sacra de capite ecclesie, de anima eius et de aliis eius membris est manifeste impossibilis. Et sic videtur quod habent dicere communiter quod, sicut ecclesia nichil est, ita nichil valet, et sic Christus foret mercator stultissimus qui tradidit semet ipsum pro dicta ecclesia et nimis illuderet christianis de sponsalibus, de privilegiis et de attributis ecclesie.

[ENGLISH]

## ¶4 · 119.12–120.2

> [p. 119] Nam si ecclesia non sit ens vel aliquid, tunc non est verum nec bonum, et cum nichil valet nisi proporcionaliter ut est bonum, sequitur quod ecclesia nichil valet. Sequitur enim secundum rudimenta discipline: Utrumque istorum est bonum, deducendo duas particulares ecclesias, ergo utrumque istorum est res aliqua, et sic mille res forent una res que, licet raciocinetur, vivat bene, male, exercens actus humanos, subiectans accidencia velut substancia, tamen nichil est. Unde habet partes et est satis sensibilis, divisibilis et sic de aliis denominacionibus, sed nullum est caput vel membrum eius, nec aliquid est intra, extra vel pars ecclesie, cum nunquam incepit, incipit vel desinet. Et sic nedum domus materiales non manebunt post ablacionem minime partis materialis per auram vel avem, et sic oporteret indies de novo consecrare ecclesias, sed et communitates, ut conventus, abbathie, atque religio deficerent continue et innovarentur, ut quevis persona de talibus deficit, vel quomodolibet innovatur, et periret appropriacio temporalium, eo quod non superesset collegium cui temporalia sunt donata. Non enim iure hereditario carnali sed imitacione [p. 120] spirituali a qua forte degenerantur, debent tales elemosinas vendicare.

[ENGLISH]

## ¶5 · 120.3–120.13

> [p. 120] Item, iuxta dicta totum genus humanum est unus E homo, divisus in duos homines, et uterque eorum habet Deum et dominum Jesum Christum pro capite, ergo uterque eorum est corpus domini, et per consequens, ille totus homo foret corpus domini et sic sine racione reprobaret Augustinus Ticonium de corpore domini bipertito. Nec est evidencia quod exercitus vel populus facit quidquid facit pars eius, quin per idem ille magnus homo foret simul corpus Christi et corpus diaboli, salvatus et dampnatus, quia secundum partes, ergo etc.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 116.2: 1. We have to solve the difficulties that we have raised against our adversaries
- 116.7: that the Church is a monster, having a thousand heads, and that she is a virgin and a corrupt synagogue, and Christ's Church.
- 116.19: The difficulty as to heads rests on an equivocation. A head may belong to the Church without being the head of the Church.
- 117.9: 2. The Church is a virgin, polluted now by sins of her members, but to be purified for final glory.
- 117.19: 3. Every synagogue that is a part of Holy Church is a Church.
- 117.26: It is objected that Christ would be at once son, father ind husband of the Church.
- 118.1: There is no reason why such relations should not exist spiritually;
- 118.13: as the Church is truly all the things that she is called in Scripture.
- 119.1: Some say that the Catholic Church (as an universal) has no real existence.
- 119.12: If the Church is nothing it cannot be good.
- 119.17: Any local church may be something and so a thousand somethings may make up one which, in spite of all it does and is, we are to call nothing.
- 119.26: By similar reasoning we might conclude a house or a corporation has no continuous existence, since the parts vary.
- 120.3: Objection: If a whole is all that its parts are, man is at once the body of Christ and the body of the devil.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 116: *CAP. VI.* [HEAD]
  - 116: *mille* [R3]
  - 116: *est* (25 is the line number) [R3]
  - 117: *matri* (144c folio mark) [R3]
  - 117: *Christi* [R3]
  - 118: *loquuntur* [R3]
  - 118: *debemus* [R4]
  - 118: *loqui* [R3]
  - 118: *Christi* [R3]
  - 118: *ecclesie* (she is the English side-note) [R4]
  - 118: *1* (short old-style arabic 1 (verse), not capital I) [R3]
  - 118: *Christus* [R3]
  - 118: *Iª* [R3]
  - 118: *28* (print: Corinth. XV°, 28 compendiose) [INS?]
  - 119: *quod* (145a folio mark glued, D alinea) [THIN]
  - 119: *quidam* [THIN]
  - 119: *nullam* [R3]
  - 119: *quevis* (30 is the line number) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 116:
3. A in marg.: Prima obieccio. 7. A in marg.: Responsio.
12. singillatim: ita cod. A ct B. A, : sigillatim. 16. B: de sophistis.
17. 18. B: membrum est huius. 28. A in marg. : Correlarium.

p. 117:
9. A in marg. : Nota argumenta logica de materia capitis ecclesie.
(Below 144= without mark of reference.) i3. B: sic deest. i5. A in
marg. : Nota. 24. A in marg.: Secunda obieccio. Item est filius pater
et sponsus ecclesie, puta Christus etc. 29. A in marg. : Responsio.
9. Conf. Hus, De ecclesia, Opp. tom. 1, iqS*.

p. 118:
24. Ysaie; Codd. Vsidorus. Correxi. 26. Ainmarg. : Christi
respectus ad ecclesiam. 33. A in marg. : Duplex opinio.

p. 119:
i. A A,: quidam diceret. 5. In codd.: scriptura sacra. 12. A in
marg. : Obieccio. 22. B: sed deest. 23. 24. B: vel partes.
24. B: vel delinet. 29. B: innovearuntur.

p. 120:
2. B: elemosina. 3. A in marg. : Tercia obieccio. 14. A in
marg. : Responsio. Totum genus humanum est unus homo divisus in duos
homines et unus illorum est corpus domini et alius est corpus diaboli.
Contra Ticonium. 23. A in marg. : Augustinus contra Ticonium.
8. In tertio libro De Doctr. Christ. cap. XXXII. 22. Cf.
Hus, De ecclesia, Opp. tom. I, 2o6b-
```

---

## Chunk 06-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "120.14–123.27"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 2 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "868 words; 790 unanimous or majority-real; 65 settled by vote (R2 35, R3a 21, R3b 3, R5a 5, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n157–n160 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 2: [TITLE]

## ¶1 · 120.14–121.28

> [p. 120] Hic dicitur concedendo assumptum, cum non possunt esse plures quam duo homines, et ita conceditur quod uterque istorum duorum hominum habet Deum pro capite, non pro parte eius, sed principaliter extrinsecus influente, et sic unus eorum est corpus domini quod est sancta ecclesia, sed alter non est corpus domini, sed corpus diaboli. Et sic non sequitur: Hoc corpus est domini, ergo hoc est corpus domini. Et hoc intendit Augustinus, 111° De Doctrina Christiana, XXXII° cap., increpans Ticonium, quia vocavit prescitos corpus dominicum. Non enim est totum corpus naturale corpus domini bipertitum, nisi utraque pars fuerit corpus domini. Et cum Augustinus XXXII° postquam ostendit quod Christus et corpus suum quod est ecclesia sunt una persona, increpat eum in secunda regula qua vocat totum genus hominum corpus domini bipartitum. Non, inquit, sic debuit appellare. Non enim revera domini corpus est quod cum ipso non [p. 121] erit in eternum, sed dicendum fuitde corpore domini vero atque permixto, aut vero atque simulato, quia non solum in eternum, verum eciam nunc ypocrite non cum illo esse dicendi sunt. Ecce quam plane iste sanctus diffinit quod presciti non sunt de Christi ecclesia. Unde De Consecracione, d. IIª Hoc sacramentum, dicit canon quod per cibacionem eucaristie societatem vult intelligi corporis et membrorum quod est ecclesia in predestinatis. Et De Penitencia, d. IVª, Si ex bono; et sepe infra habetur quod nemo est de regno Christi quod est ecclesia, nisi vere filius quem pater dedit sibi. De quo dicit Joh. 111°, 16, quod oportet ut non pereat, sed habeat vitam eternam. Et sic multi sunt in ecclesia qui vocantur filii nuncupatim qui non sunt de ecclesia. Conceditur ergo quod homo qui est humanum genus est partim prescitus et partim predestinatus, et sic tempore suo partim salvatus et partim dampnatus, sed ille non est ecclesia, quamvis faciat quidquid facit aliquis homo, quia ad unitatem requiritur unitas capitis, sed ut dicit apostolus IIª Cor. VI°, 1. Que convencio Christi ad Belial? Non ergo sunt duo capita ex equo vel subordinata, cum secundum apostolum que a Deo sunt ordinata, sunt. Et sic homo humani generis est corpus naturale sed non corpus ecclesie propter diversitatem contrarietatis capitum et equivocacionem ordinacionis divine ad gloriam et ad penam.

[ENGLISH]

## ¶2 · 121.29–122.6

> [p. 121] Et patet quid concedi debeat et quid negari in ista materia. Nam concedi debet quod homo generis humani facit quidquid aliqua eius pars facit, et simul est [p. 122] beatus in celo et dampnatus in inferno, et est ambe iste ecclesie sed neutra illarum, et corpus illud secundum se totum est domini, sed non est corpus domini nec est corpus diaboli, cum totum integrale non est eius pars quantitativa sed est eius partes quantitative, et sic est collectim corpus domini et corpus diaboli.

[ENGLISH]

## ¶3 · 122.7–123.10

> [p. 122] Unde videtur mihi quod illi non minus heretice quam blaspheme scandalizant sanctam matrem ecclesiam qui dicunt quod habet ut partes componencia tot membra diaboli, quia indubie tunc foret turpissima et a Deo maxime odita, quia secundum magnam partem. Et cum Canticorum IV°, 7, de illa dicitur: Tota pulchra es amica mea et macula non est in te, et apostolus Eph. V°, 27, dicit illam esse ecclesiam, non habentem maculam neque rugam, et illud dicit decretum (ut patet in fine XIII cap.): cum ergo nullus debet dubitare quin omnia ista loquuntur de sancta matre ecclesia, manifestum videtur quod illa non habet in sui composicionem aliquod membrum diaboli, sed sicut prudens paterfamilias non adoptat in filium quem scit perdere patrem suum, sic de Deo, quia iuxta apostolum, si ordinaret filios, et heredes. Cum ergo iuxta decreta ille cadit in heresim qui aliter exponit scripturam sacram quam spiritus sanctus flagitat, sicut et ille qui imponit tantum vicium sancte Romane ecclesie, et indubie scandalum tale redundaret in Dei blasphemiam, quomodo rogo foret gratus matri ecclesie vel sponso suo qui imponeret eis tantam calumpniam? Nonne Exodi XXI°, 17 cap., precipitur lege sponsi: Qui maledixerit patri vel matri moriatur? Non ergo imponamus matri nostre malediccionem et heresim cuiusmodi necessario est singulus prescitorum. [p. 123] Sed instatur quod, sicut omnes partes predestinatorum sunt partes ecclesie, ita omnia capita predestinatorum sunt ecclesie capita, et sic caput aggregatum foret caput ecclesie. Hic dicitur (ut supra tetigi) quod illud probabiliter concedi potest de capite naturali et, intelligendo ecclesiam personaliter ut per accidens vel contingenter, est ecclesia, cum partes quantitative predestinati ordinantur ad beatitudinem. Sed locuti sumus communiter equivoce de capite, ut est persona regens capitaliter; quod est Christo proprium quoad totam ecclesiam.

[ENGLISH]

## ¶4 · 123.11–123.27

> [p. 123] Quarto arguitur per hoc quod iuxta dicta ecclesia foret per totum tempus veteris testamenti acephala, eo quod. non potest habere caput nisi Christum, sed tunc non habuit Christum caput, ergo tunc non habuit caput. Et per idem videtur sequi quod eadem ecclesia fuit pro tempore crementi quotlibet membra sua, quia pro nullo instanti fuit nisi fideles qui tunc fuerunt. Unde in exemplo tacto in fine secundi argumenti videtur quod non manet eadem domus, quacunque parte ablata vel noviter veniente, quia per idem ablata iterum tanta et alia noviter veniente, et sic qualibet parte domus corrupta et una secundum se totam noviter generata, maneret eadem domus, sicut est de domo ecclesie. Hic sunt tres difficultates. Prima, utrum Christus fuit ante incarnacionem, quia certum est quod eternaliter fuit verbum Dei et semper caput ecclesie. Sed videtur non fuisse caput eius intrinsecum antequam fuit homo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 120.14: Answer: Mankind is divided into two, and in a sense they both have God for their head, but only one is the body of the Lord.
- 121.16: Mankind is not the Church.
- 121.29: Mankind does whatever each of its parts does,
- 122.1: but it is not the body of the Lord or the body of the devil.
- 122.5: A whole is not its part, but its parts.
- 122.7: It is a slander on the Church 10 say that the reprobate form part of her.
- 123.12: 4. The Church of the O. T. would have been headless, since Christ was not then its head.
- 123.25: Christ before his incarnation was not intrinsically head of the Church,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 121: *IIª* [R3]
  - 121: *IVª* [R4]
  - 121: *IIª* [R4]
  - 122: *corpus* [R3]
  - 122: *odita* (print has odita) [NW]
  - 123: *Christum* [R3]
  - 123: *Christum* [R3]
  - 123: *fuit* [R3]
  - 123: *Christus* [R3]
  - 123: *fuit* [R3]
  - 121: *erit* (145b folio mark glued) [THIN]
  - 121: *eternum* [THIN]
  - 121: *dicendum* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 120:
2. B: elemosina. 3. A in marg. : Tercia obieccio. 14. A in
marg. : Responsio. Totum genus humanum est unus homo divisus in duos
homines et unus illorum est corpus domini et alius est corpus diaboli.
Contra Ticonium. 23. A in marg. : Augustinus contra Ticonium.
8. In tertio libro De Doctr. Christ. cap. XXXII. 22. Cf.
Hus, De ecclesia, Opp. tom. I, 2o6b-

p. 121:
6. A in marg. : Presciti non sunt de Christi ecclesia. 22. In
codd. : que communicacio. Correxi e II Cor. VI, i5.
6. Decreti III. pars, De Consecratione dist. II, cap. LXIII: Hunc
cibum et potum societatem vult intelligi. 10. Decreti II. pars,
causa XXXIII, quest. III, dist. IV, cap. VIII. 24. Rom. XIII, 1.

p. 122:
14. A A, illam esse: sequitur lacuna; ecclesiam: deest. i5. B: sicut
dicit. 20— -12. A A,: in — ordinarct deest. B: quem sit. 29. A:
Nonne eodem XXI. A, corr. in marg. 3o. A, in marg. add. : morte,

p. 123:
i. A in marg. : Nota; replicacio. 4. A in marg. : Responsio.
Omnia predestinatorum capita sunt capita ecclesie. 11. A in marg.:
Quarta obieccio. 21. A: corrumpta. 22. A A^: manet.
25. A in marg. : Responsio. Prima diflicultas. B inmarg. : Utrum Christus
fuit ante incarnacionem. 3o. A m marg. : Christus in primo instanti
mundi fuit sponsus ecclesie.
3o. Cf. Hus, De ecclesia, Opp. tom I, 198*.
```
