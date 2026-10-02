# Translation brief: ecclesia 07-b–07-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-07-b.md chunks/ecclesia/wyc-ecclesia-07-c.md chunks/ecclesia/wyc-ecclesia-07-d.md chunks/ecclesia/wyc-ecclesia-07-e.md` once and fix what it reports.
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

## Glossary (the 141 rows these chunks use; the full file is GLOSSARY.md)

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
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| castra caynitica | Caim's castles | The friars' houses; the Wycliffite English name (CAIM = the four mendicant orders' initials). Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
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
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| inobedienciarius | disobedient man | The negative of *obedienciarius*. Ruled 2026-10-02 (146.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 07-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-07-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-07-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "146.29–148.24"
divisions: "cap. 7 (heading 'CAP. VII.' at 142.2); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "430 words; 395 unanimous or majority-real; 23 settled by vote (R2 15, R3a 3, R5a 5); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n183–n185 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 7, part 2: [TITLE]

## ¶1 · 146.29–147.24

> [p. 146] Quod autem preceptum regis in hac parte non obviat legi Dei nec veris privilegiis Westmonasterii sic ostendo: Scrutetur homo totam scripturam et non inveniet quod pro debito, pro occisione iniusta, [p. 147] immo generaliter pro quocunque peccato debet pro fugus habere refugium, quia tunc Deus foveret proditorem proprium in suo crimine; quod non potest. Unde Deuteronomii XIX° et Josue XX°, ubi datur lex profugorum et constituuntur civitates refugii, limitatur quod solum occidentes nescii et inmunes criminis debent ibi habere refugium, ne a cognacione occisi effundatur sanguis innoxius, nec habitabant ibi perpetuo, sed Levite habebant custodiam sex civitatum refugii, nec acceptarent nisi insontes qui a casu preter intentum fratrem suum occiderint; illi autem non exibant civitatem nisi ad purgandum se in loco occisionis quod ignoranter occiderint fratrem suum usque ad mortem summi pontificis. Tunc enim redirent libere in domum propriam extra civitatem refugii; patet ista lex Numeri XXXV° et Josue XX°. Si ergo in tota lege nova et veteri (ubi diffuse tangitur ista materia) non limitatur locus refugii nisi insontibus qui casualiter fratrem suum occiderint, que foret in christianis ceca presumpcio sub colore pietatis defendere hostes Dei, regis et regni? Per hec patet responsio ad argumentum quod fundatur in privilegio concesso a rege monasterio supradicto.

[ENGLISH]

## ¶2 · 147.25–148.24

> [p. 147] Supponitur autem quod habeat privilegium sub isto tenore verborum quod liceat sibi tueri quoscun- que fugitivos ex quacunque causa, eciam in causa lese regie maiestatis, adhuc totum istud est generalis concessio sed secundum leges hominum in generali concessione principis nunquam veniet speciale, nisi quod concederetur a principe in casu quo fuerit particulariter [p. 148] explicatum. Cum ergo non sit in potestate principis concedere quod vergeret ad Dei iniuriam, ad destruccionem regni sui, ad enervacionem regalie et legum per quas regeret regnum suum, patet quod illud suppositum in casu nobis exposito non includitur in illo privilegio generali. Quid queso foret magis ad Dei iniuriam quam facere domum suam speluncam latronum? aut quid foret magis destructivum regnorum quam protegere in nidis ad hoc deputatis hostes Dei ecclesie atque regni. Ecclesiastici X°, 8 scribitur: Regnum de gente in gentem transfertur propter iniusticias, iniurias, contumelias et diversos dolos. Cum ergo secundum sanctos qui emendare potest et negligit absque dubio participem criminis ut sic se constituit, ideo patet quam patenter minaretur ruinam regno talis erroris tolerancia sive defensio. Unde alias ostensum est quod monasterium, habens facultatem ad defendendum proditores Dei, cuiusmodi sunt singuli criminosi, non habet ut sic privilegium, sed pocius corruptelam. Unde sicut monti Ethne non sonat in privilegium quod includat ultra alios montes ignem suimet consumptivum, sic nec dicto monasterio foret privilegium facultas fovendi proditorem Dei tam sui quam totius Anglie destructivum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 146.29: This command was not so contrary to the law of God.
- 147.1: God's Jaw provides no refuge for debtors or criminals.
- 147.25: It is said that Westminster has a privilege to shelter all criminals,
- 148.1: Such a privilege does not go beyond the explicit intentions of the granter,
- 148.8: or the grant would be invalid as injurious to God and the kingdom.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 146: *non* (E at line end is the margin letter) [R3]
  - 147: *immo* (148d is the folio mark) [THIN]
  - 147: *generaliter* [THIN]
  - 147: *fugus* (second half of pro-/fugus) [NW]
  - 147: *quoscun-* (first half of quoscun-/que; has is the English side-note) [THIN]
  - 147: *que* (second half of quoscun-/que) [THIN]
  - 147: *fugitivos* [THIN]
  - 148: *explicatum* [THIN]
  - 148: *Cum* [THIN]
  - 148: *8* (print: Ecclesiastici X°, 8 scribitur) [DEL]
  - 148: *Cum* (round C, not g) [R4]
  - 147: *XX°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 146:
6. D: specialiter deest. A in marg. : Nota dc obediencia ad regem
continue infra. (Above 8d without mark of reference.) 12. D: su-
pradictos. i3. D: mandatum huiusmodi. 23. D: egressus fuit.
32. D: debito et pro occisione iniusta nimis gcneraliter.

p. 147:
t. A in marg. : Nota de refugiis profugorum insoncium iniusti occi-
dentis nullus est Iocus refugii. 3. D: quod esse non potest. 4. B:
Josue X. 6. A B : quod soli; B: occidentes vestigii ct. 22. D:
Per hoc. 25.26. D : liabet privilegium sub isto colore. 26. A : tcneri.

p. 148:
5. D: istud. 10. 11. D: Eccl. XX. 11. A B: transferetur.
l5. D: ideo deest. 26. D: Iterum nec. 3r. D: factus sit.
32. August. Epist. ad Maced. CLIII, Opp. tom. II, 532 A.
```

---

## Chunk 07-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-07-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-07-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "148.25–152.13"
divisions: "cap. 7 (heading 'CAP. VII.' at 142.2); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "885 words; 832 unanimous or majority-real; 41 settled by vote (R2 22, R3a 11, R3b 2, R5a 5, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n185–n189 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 7, part 3: [TITLE]

## ¶1 · 148.25–151.33

> [p. 148] Item, nec regi licet privilegium tale concedere nec sacerdoti suo accipere nisi ex titulo elemosine vel misericordie et ad augendum in populo caritatem, sed constat quod non est elemosina vel opus misericordie dare abbathie licenciam, ut sustineat perpetuo debitorem, ne unquam satisfaciat, vel quod voluptuose vivendo aliena consumat, quousque factus fuerit inpotens ad solvendum. Cum enim secundum Augustinum non dimittitur peccatum, nisi restituatur ablatum, [p. 149] patet quod licenciare ad hoc foret licenciare hominem ad peccandum, quod Deus non potest, et per consequens non continetur sub opere misericordie privilegium tale concedere, nec tenderet ad augmentum amicicie vel caritatis in populo communi commune ius de satisfaccione debitoris precludere. Et patet tam ex parte donatoris quam receptoris quod ad tale privilegium est indisposicio utrobique. Nec moveat quod ex tali privilegio quandoque bonum contingeret, ut puta debitoris depredati misericors expectacio vel aliter criminosi ex tutela refugii finalis conversio, quia Deus non posset permittere peccatum fieri, nisi exinde occasionaliter bonum contingeret. Ideo absit, dicit Apostolus, ut faciamus mala, ut bona eveniant. Docto igitur quod libertas talis sonaret in caritatem et elemosinam, posset concedi singulariter illi loco privilegium sub ista condicione quam necesse est in omni donacione legitima habere tacitam vel expressam. Unde videtur quod prelati nostri debent humiliter pulsare dominos, ut tales errores nostre ecclesie previe corrigantur, antequam invadant hostes forinsecus, quia ex testimonis Christi Matth. X°, 36 nulli plus infestant matrem ecclesiam quam eius domestici inimici. Tercio principaliter arguitur sic ad idem de iure nature: Frustra invocat legis auxilium qui offendit in eam, sed dicti fugitivi rebellando offenderunt in legem Dei, ecclesie et in legem regni: ergo iustum est pro tempore sue obstinacie quod careant in omnibus istis legis suffragio. Maior autem capitur ut regula per se nota in iure canonico et demonstrari potest ex fide evangelii Matthei V°, 25, ubi Christus precipit: Esto consenciens adversario tuo cito, dum es in via cum eo, ne forte adversarius tuus tradat te iudici et iudex [p. 150] tradat te ministro et in carcerem mittaris, ubi secundum exposicionem beati Augustini oportet intelligere legem Dei adversantem cuilibet peccatori, quia nisi sibi consenserit hic in via, accusabit eum in finali iudicio cum demonibus detrudendum. Si ergo lex Dei mitissima non potest non adversari suo offendenti, quia tunc sequeretur quod falsitatis malicia superet veritatem, manifestum videtur quod omnis alia lex secundaria non excusat sed accusat, non iuvat sed reprobat, stante obstinacia offensoris. Dicti autem fugitivi iuxta nobis exposita offenderunt in legem Dei ex inobediencia suis prepositis, offenderant insuper in legem ecclesie racione multiplici, quia (ut dicunt docti in illis iuribus) inobedientes mandatis suorum principum committunt quoddam genus sacrilegii, et cum inobedientes remanserint legi Dei de obediendo legibus regis sui, que lex iusta illos protegeret? Et insuper secundum quod informati sumus occisus erat primus invasor et ecclesie pollutor. Quomodo ergo lex libertatis illius ecclesie defenderet tam ingratum et illegitimum eius pollutorem excommunicatum de iure? Non enim palliari potest defensio arrestati legittime et intenti salvari in vita et membris, ut invadat contra legem Anglie suos legitimos arrestantes. Cum enim arrestacio et occisio sunt contraria, patet quod miles arrestans sine extraccione gladii vel cultelli non ostendit occiso necessitatem se defendendi sed pocius legitime paciendi; et patet ex facto multiplici, supposita veritate narrati, quod erant inobedientes patriis legibus pro qua inobediencia continuanda querebant subterfugia [p. 151] dicti loci. Que queso maior inobediencia regi nostro quam nolle tractari secundum leges suas, sed proprias leges proponere secundum quas et non secundum alias velint tractari, et illis, non regni legibus, obedire? Revera sic hostes crudelissimi depopulantes regnum offerrent regnicolis quod si velint consentire legibus quas illi volunt statuere concordabunt, sed non exinde gauderent privilegiis regni nostri. Mirum itaque foret quod rex et regnum tales hostes intra se defenderent. Idem enim foret contradicere legibus regis per quas regeret regnum suum et contradicere regalie, cum rex non foret rex nisi propter preeminenciam et officium legis sue. Ideo dicit beatus Gregorius quod qui diligit regem diligit eius legem et demonstrari potest ex illo Johannis XIV°, 23. Si quis diligit me, sermonem meum servabit; idem enim est Deum diligere et sermonem vel legem eius servare, et sic indubie est de rege. Unde inobediencia legibus est radix tocius nequicie. Exhinc enim ceciderunt angeli de celo, expulsus fuit Adam de paradiso et breviter sine contumacia que est inobediencia non recte denunciatur heresis vel excommunicacio; nec est possibile regnum dissolvi nisi ex inobedie ncia legi sue. Si enim maior pars regni nostri vel prope nollet stare legibus regni nostri, sed sparsim acciperet municionem ecclesie commovendo sedicionem in populo, pretendendo utrobique libertatem ecclesie, quomodo staret regnum? Et si non licet regi talem hostem domesticum de castris ecclesie sue extrahere, quomodo liceret in regno non tantum subiecto ecclesias Dei invadere et remissius proditores vel hostes occidere? Nam ubi est maior falsitas atque iniuria coloracior, ibi est pena iustior.

[ENGLISH]

## ¶2 · 152.1–152.13

> [p. 152] Ex istis colligitur, supposita veritate informacionis, quod dicti duo profugi post tantam inobedienciam non sunt homines legii regis nostri, nam idem est derelinquere dominum et derelinquere legem suam; sed ipsi patenter dereliquerant legem regis, cum invaserant citantem ad standum legi regni, volentes cum hoc rege invito incolere terram suam. Ideo omne suffragium privilegii regis tenentur amittere, et cum in eadem dampnacione sint omnes qui fovent aut favent iniuriam dicte cause in contemptum regis et regni, et specialiter hii qui sub pena excommunicacionis ad defensionem legum regni et regalie regis specialiter sunt iurati, patet quante illi forisfaciunt contra regem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 148.25: All royal grants must be for the good of the people,
- 149.1: but the grant claimed would be simply a license to sin.
- 149.15: Therefore the privilege even if granted must be taken conditionally.
- 149.24: 3. He who breaks the law cannot claim its help.
- 150.10: These fugitives were offenders against the law of God and the Church;
- 150.18: and the man slain was the first to fight in the Church.
- 151.1: There can be no greater disobedience than to withdraw oneself from the law.
- 151.24: The realm cannot stand if the Church protects sedition,
- 152.1: The refugees had renounced their allegiance.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 148: *in* [R3]
  - 149: *patet* (149a folio mark, G margin letter) [R3]
  - 149: *licenciare* [R3]
  - 149: *aliter* (149b is the folio mark) [R4]
  - 149: *ut* [R3]
  - 149: *obstinacie* (print spelling) [NW]
  - 150: *offenderunt* [R4]
  - 150: *in* [R4]
  - 150: *invasor* [R4]
  - 151: *proprias* [NW]
  - 149: *et* [THIN]
  - 150: *subterfugia* (subter- here, 149c fugia at top of p.151; main token holds whole word) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 148:
5. D: istud. 10. 11. D: Eccl. XX. 11. A B: transferetur.
l5. D: ideo deest. 26. D: Iterum nec. 3r. D: factus sit.
32. August. Epist. ad Maced. CLIII, Opp. tom. II, 532 A.

p. 149:
5. D: communi deest. 6. B: ut patet. 20.21. D: ecclcsie pri-
vilegiate. 24. A in marg. : Tercia responsio.
14. Rom III, 8.

p. 150:
2. A in marg. : Augustinus. 5. B: detradendum. 5. 6. A A,:
lex Dei iustissima. A in marg. : Lex Dei est noster adversarius. D: non
potest adversari. 8. D: lex contraria. 12. offendcrant: codd.
AB D. Aj corr.: offcnderunt. i5. D: committant. 25. D:
occisio et arrestacio. 26. 27. A A, vcl cultelli — dcfendendi deest. B
se: deest. 29. A A: erant deest.
2. Aug. Sermo IX, De Decem Chordis cap. III, Opp. tom V, 49,
Serm. CCLI, cap. VIII, Opp. tom. V, 1037.

p. 151:
2. D : nolle tractarc. 9. 10. defenderet in codd. u. A in marg. :
Lcgi regis esse inobcdientem nocet multnm. (Above 140° without mark
of reference.) 14. A in marg. : Gregorius. i5. D: demonstrare.
17. A 13: enim deest. 22. D: non rite. 29. D: liceret.

p. 152:
1. A in marg: Conclusio. 3. B D: regis deest. 7. B: rege
invicto. 9. D: sunt omnes. 9. 10. D: favent dicti cause.
14. A in marg. : Conclusio. 24. D: notandum. B: excommunicatus
proptcr. 3o. D: facit. 32. A A B,: quocunque deest.
```

---

## Chunk 07-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-07-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-07-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "152.14–156.14"
divisions: "cap. 7 (heading 'CAP. VII.' at 142.2); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "904 words; 817 unanimous or majority-real; 74 settled by vote (R2 50, R3a 18, R3b 3, R5a 3); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n189–n193 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 7, part 4: [TITLE]

## ¶1 · 152.14–154.25

> [p. 152] Ex quibus videtur quod publice excomunicantes ministros regis sine examinacione diligenti delicti, et specialiter si iurati sunt legem ipsam defendere, offendunt nimium. Nam Gen. XVIII°, 20, 21, dicit omnisciens ad dandum exemplum iudicibus, quomodo diligenter examinent causam, antequam ferant iudicium: Clamor, inquit, Sodomorum multiplicatus est; descendam et videbo utrum clamorem opere compleverint an non est ita ut sciam. Nec sufficit notorietas substancie facti, sed oportet quod sit notorium qualitate; quia notum est quod excommunicans propter operacionem legitimam iniuriatur excommunicato excommunicando se ipsum. in Nec est color excommunicare capitaneos operacionis legitime propter hoc quod preter eorum consensum, auctonsacionem vel occasionem datam aliquis de comitiva fecit opus indebitum, quia sic Christus foret excommunicandus pro facto Scarioth, et quilibet dux exercitus pro quocunque facinore commisso a persona sui exercitus et (quod evidencius est) quilibet prelatus [p. 153] pro quocunque scelere subditi sui gregis; que si essent vera tolleretur a prelatis potestas excommunicandi subiectos, cum non licet excommunicato excommunicare quemquam, ymmo cum ut sic sit hereticus, non licet sibi ministrare aliqua sacramenta. Nec cadit excusacio quod prelatus non excommunicat, sed denunciat tales excommunicatos de iure, quia talis denunciacio est defamacio minimis; et ve illi qui taliter scandalizat fratrem suum. Est autem excommunicacio iniusta tripliciter: Primo quando sacerdos ex rancore et zelo vindicte excommunicat subditum licet reum. Secundo quando prelatus pocius pro temporalibus quam pro amore et correccione subditi eum excommunicat, licet excomunicandus fuerit bono modo. Et tercio quando indiscrete excommunicat subditum propter factum legitimum. Talis autem excommunicator videtur plus polluere sanctam ecclesiam quam corporaliter occidens hominem ad altare; pro quo notandum quod corporalis pollucio videtur esse excommunicacioni inpertinens, nisi de quanto sapit peccatum, tum quia pollucio per sputum vel alia pondera nature foret turpior quam pollucio per semen vel sanguinem, tum eciam quia illa pollucio deletur per locionem corpoream. Ex istis videtur, cum iniuste excommunicans fratrem suum (quantum in eo est) occidit animam et virtutes, sed corporalis homicida non occidit ut sic nisi corpus solummodo, sequitur quod, sicut anima excedit corpus, sic occisio in animam perpetrata excedit in malicia occisionem corporis. Ex quo videtur, cum peccatum non potest subiectari in lapide vel edificio corporali, quod locus per se non polluit suos incolas, sed [p. 154] econtra, cum II° Machab. V°, 19, scribitur: Non propter locum gentem, sed propter gentem locum dominus elegit. Et patet quod pollucio loci non impediret racionabiliter cultum Dei, nisi de quanto horrorem incuteret ex peccato, et cum maius peccatum maiorem horrorem incuteret, sequitur quod peccatum gravius commissum in sanctuario pocius retraheret a divino servitio. Nec aliud volunt leges ecclesie debite intellecte. Non enim licet clerico Christi cecari in stulticia phariseica (de qua Matthei XV°), plus appreciando locionem corporalem ex pluri horrore sordis corporee quam locionem spiritualem a sorde anime, cum secundum diffinicionem Christi, que exeunt a corde interioris hominis, hec sunt que preponderanter coinquinant hominem. Eta hic miratur tota ecclesia laycalis quare clerus excommunicat cum tanta instancia et fervore pro suo debito corporali, vel pro sensibili privilegio ex tradicionibus hominum introducto; clericos autem non sic excomunicant pro rependendo debito spirituali, cum tamen peccatum sit infinitum gravius et debitum illud quoad Deum sit obligacius. Plus eciam foret ad privilegium et iustificacionem ecclesie quod prevaricatores mandati Dei per censuras ecclesie sint correcti quam quod omnes ritus humani legi Christi superadditi sint quantumcunque multipliciter regulariter ac solempniter observati.

[ENGLISH]

## ¶2 · 154.26–156.2

> [p. 154] Recoleremus siquidem quod propter preponderan- ciam ritus phariseici legi Dei destructe sunt Jerusalem et Judea (ut patet Matthei XV° et Luce XIX°). Recoleremus eciam quomodo privilegium est lex privata ad commodum privilegiati concessa a principe, [p. 155] et per consequens foret clero magnum privilegium quod adiutorio dominorum temporalium foret exoneratus ab istis cerimoniis humanitus introductis, propinquius sequendo Christum pure secundum regulas primevas a Christo traditas. In hoc enim habemus supra laycos privilegium singulare. Mirantur insuper seculares quomodo non licet eis communicare cum excommunicato a sacerdote pro questu suo vel excellencia seculari, et hoc sub pena excommunicacionis maioris, licet autem communicare cum gravius excommunicatis a Deo sine inferencia tante pene, ut patet de simoniacis, de sacerdote fornicario et eius amasia. Ymmo licet cardinales tamquam heretici vel scismatici sint divisi a capite, tamen dicimus seculares excommunicatissimos, si ab eis subtrahant elemosinas suas que sunt bona pauperum, licet iniustissime peius predonibus occupent aliena. Licet autem (ut inquiunt in Westmonasterio) communicare cum excomunicato quoad Deum racione iniuste detencionis debiti vel iniuste occisionis proximi, eciam sustinendo eum in sua malicia, sed laicis non licet communicare cum minus excommunicatis ab eis pro bonis ecclesie. Talia autem multa deliramenta finguntur per que layci mendaciter illuduntur; licet enim falsitates ficte quandoque prosunt per accidens, subditos a facinore deterrendo, absit tamen christianum contra fidem scripture uti istis fallaciis pro hoc fine. Notum est enim ex fide scripture quod nemo ad sui dampnum excommunicatur, nisi racione delicti proprii excommunicatus fuerit quoad Deum. Notum est iterum quod nemo propter corporalem communicacionem cum excommunicato incurrit periculum, nisi sit particeps criminis cum eodem. Et notum est tercio quod infinitum periculosius est communicare culpabiliter cum excommunicato a Deo, qui solum excommunicat [p. 156] pro mortali, quam communicare nudei5o"0 corporaliter cum excommunicato solum ab homine.

[ENGLISH]

## ¶3 · 156.3–156.14

> [p. 156] Tercio miratur secularis ecclesia quod clerus instat erga brachium seculare, ut omnes excommunicati sui per quadraginta dies, remanentes a prelatis quos ipsi signaverint non soluti, mancipentur carceri seculari, quousque secundum eorum arbitrium satisfecerint, quantumcunque sophistice sint ligati. Non enim meretur eorum ingratitudo tale subsidium, cum regula iuris divini sentenciat quod privilegium indultum tenetur amittere qui sibi concessa abutitur potestate. Abusus ergo tendens ad enervacionem regni et bonum privatum bono communi preponderans meretur ablacionem privilegii sic abusi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 152.14: It is an offence to excommunicate the King's servants without careful enquiry.
- 152.27: Persons in authority are not to be condemned for wrong done by their subordinates without their consent.
- 153.10: Excommunication is unjust: 1. if inflicted from spite, 2. from avarice;
- 153.15: 3. if undeserved.
- 153.25: Unjust excommunication is worse than murder.
- 154.15: Men want to know why the wicked clergy are not excommunicated.
- 155.6: The rules as to relations with excommunicated persons are bad.
- 155.28: No such relation is dangerous except a share in the crime.
- 156.3: The Prelates' privilege of imprisoning excommunicated persons should be taken away,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 152: *et* (15 is the line number) [R3]
  - 153: *pro* (149d is the folio mark) [R3]
  - 153: *∅* (pre-/latus is one word, already whole at pos 80 (prelatus)) [INS?]
  - 153: *excomunicandus* (excomuni-/candus, single m as printed) [R4]
  - 153: *factum* [R3]
  - 153: *edificio* [NW]
  - 154: *II°* [R3]
  - 154: *Christi* [R3]
  - 155: *et* (150a is the folio mark, N margin letter) [R3]
  - 155: *∅* (nothing between et and per; these words are the last lines of p.154 (already in p.154)) [INS?]
  - 156: *instat* (print: clerus instat; the trailing c is the margin alinea letter) [NW]
  - 153: *incolas* [THIN]
  - 155: *excommunicat* (ex- here, communicat at top of p.156; main token holds whole word) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 152:
1. A in marg: Conclusio. 3. B D: regis deest. 7. B: rege
invicto. 9. D: sunt omnes. 9. 10. D: favent dicti cause.
14. A in marg. : Conclusio. 24. D: notandum. B: excommunicatus
proptcr. 3o. D: facit. 32. A A B,: quocunque deest.

p. 153:
10. A in marg. : Tripliciter facit excommunicacio iniusta. B in marg.
man. alt. : Excommunicacio tripliciter. i5. A in marg. : Nota; De
excommunicacione persone vel Ioci. (Above i io1 without mark of re-
ference.) A A,: fuerit deest. 24. D: corporalem. Ex istis videtur,
quod. 28. A B: solo modo. 32. D: p« = persone; rectc: g se.

p. 154:
i. A B : I. Mach. D. Mach. VI. 4. 13 : honorem incuteret. 5. D:cum
magis. 5. B : honorem D : errorem. 11. A : quam corrcxit e : quando.
i3. B: exemit. i5. A in marg. : Nota trcs miraculose questiones
laicales a, b, c. (Below i4gJ without mark of refercnce.) 17. D:
scnsuali. 18. D: non excommunicant ; non alia manu in marg. ad-
ditum. 23. D: censure in textu, corr. inmarg. : censuras. 26. D:
recoleremus propter; A: proptcr deest. 27. D: distincte.
10. Matth. XV, 18—20.

p. 155:
4. B: sequendo excmplum. 14. D: in capite.

p. 156:
1. D: pro mortalibus. 3. D: quomodo clerus. 4. A in
marg. : Brachium seculare. 7. D: satisfecerunt. 25. B : puni-
cionis. 35. A in marg. : Ignorancia non excusat.
```

---

## Chunk 07-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-07-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-07-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "156.15–157.24"
divisions: "cap. 7 (heading 'CAP. VII.' at 142.2); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "314 words; 290 unanimous or majority-real; 19 settled by vote (R2 12, R3a 6, R5a 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n193–n194 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 7, part 5: [TITLE]

## ¶1 · 156.15–157.13

> [p. 156] Et iterum videtur clerum tam leviter et incircum- specte excommunicantem involvere seculares in sua excommunicacione erronea, cum ex eorum ducatu sepe per talem excommunicacionem pretensam puniunt innocentes, et per consequens, cum nec tenentur credere quod eorum quelibet excommunicacio sit iusta, nec ex fide scripture vel racione tenentur obedire clero in ista incarceracione servili, videtur ex timore peccati consensus quod non debent ante legitimam examinacionem cause et forme excommunicacionis punicioni huiusmodi consentire. Cum enim racio scripture sacre sit optimus legum interpres, patet quod adiutorium promissum a principibus in hac parte debet intelligi cum condicione quod talis incarceracio sit de numero operum elemosine pro quibus punientes sunt in finali iudicio premiandi. Sed scrutetur fidelis evangelium Matthei XXV° et videat si incarceracio excommunicatorum iniuste in aliquo operum misericordie sit contenta. Nec ignorancia excusat simpliciter ne peccetur, cum Paulus ex ignorancia veritatis scripture commisit blasphemiam, [p. 157] o(ut patet Iª Thymothei 1°). Nec dicat aliquis quod Anglia processit prospere, quando ecclesia habuit talia privilegia sic defensa, quia audacter assero quod non exinde promeruit, sed sicut iniquitas Amorreorum fuit in congregari per CCCCᵗᵒˢ annos et amplius (ut patet Gen. XV°); ex cuius cremento finaliter sunt destructi: sic timendum est de gente Anglie, nisi clerus redeat ad spiritualem humilitatem, ut olim, cum clerus ut anima et secularis ut corpus debent concorditer constituere virum unum; quod non potest fieri nisi ex mutua observancia legis Christi. Sepe enim in pruritu prosperitatis mundane est populus insensibiliter quoad Deum amplius peioratus.

[ENGLISH]

## ¶2 · 157.14–157.24

> [p. 157] Hortandi tamen sunt domini seculares ne arguendo per locum ab insufficienti similitudine auferant vera privilegia ecclesie propter cupidinem temporalium vel vindictam. Hortandi sunt secundo ne ex invidia vel alia causa pretergrediente caritatis regulas sit fugitivo culpa imposita vel prodicionis suspicio palliata. Et hortandi sunt tercio ne alicubi et specialiter infra septa ecclesie sanguinem effundant innoxium, sed honorent sanctam matrem ecclesiam secundum regulas quas Christus sibi instituit; ad que omnia oportet omnino consulere sensum catholicum scripturarum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 156.23: or allowed only after lay trial.
- 157.14: Lay rulers must, however, be reminded of their duties to the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 157: *Iª* (150b folio mark; print Iª Thymothei) [R3]
  - 157: *CCCCᵗᵒˢ* (superscript tos as printed) [R4]
  - 157: *olim* [R3]
  - 157: *peioratus* [NW]
  - 157: *culpa* (150c is the folio mark) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 156:
1. D: pro mortalibus. 3. D: quomodo clerus. 4. A in
marg. : Brachium seculare. 7. D: satisfecerunt. 25. B : puni-
cionis. 35. A in marg. : Ignorancia non excusat.

p. 157:
4. B: exinde proverant (sic). i3. A A^: peioratur. 14. A in
marg. : Nota bonas hortaciones. 20. D: ne aliter. 20. 21. D:
infra cepta. A A, B : Christus deest. 24. A in marg. verba tsclie-
chica : Nu zbohem mylym potahnyem dale. Id est: Age, cum Deo caro
(matcriam) porro tractabo.
```
