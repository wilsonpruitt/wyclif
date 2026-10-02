# Translation brief: ecclesia 06-f–07-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-06-f.md chunks/ecclesia/wyc-ecclesia-06-g.md chunks/ecclesia/wyc-ecclesia-07-a.md` once and fix what it reports.
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

## Glossary (the 147 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| digestio | digestion | The recurring figure of the four digestions (Rom. 8:30). Ruled 2026-10-02 (60.29 ff.). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 06-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "133.26–137.11"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 6 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "819 words; 705 unanimous or majority-real; 94 settled by vote (R2 59, R3a 26, R5a 9); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n170–n174 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 6: [TITLE]

## ¶1 · 133.26–136.8

> [p. 133] dubium est tactum in quarto argumento de unitate numerali ecclesie, utrum Christus et quodlibet membrum ecclesie sit eadem ecclesia in numero, et videtur quod sic ex triplici conveniencia numerali. Primo, inquam, videtur quod quantumcunque partem anima hominis adequate actuaverit, quantumcunque materia corporea [p. 134] varietur, manet continue idem homo, ut hic supponitur. Quare ergo non sic de homine ecclesie cuius forma est Christus manens in eternum? Secundum exemplum naturale est quod anima cuicunque membro copulata fuerit remanet tam anima quam membrum eadem persona hominis. Quare ergo non sic de Christo et ecclesia, sic quod quodlibet membrum eius sit Christus, ut sonant multe auctoritates? Tercio videtur quod sicut Christus mansit eadem persona in numero pro tempore mortis sue, tam in sepulchro mortuus quam in inferno vivus, ita videtur eandem personam ecclesie disiunctive regnantem in celo et peregrinantem in mundo, et sic Christus assumpsit ypostatice personam ecclesie peregrinantis in beata virgine. be Hic oportet prudenter intelligere unitatem persone j. quam sancti exprimunt ex scriptura, ut patet de octo generibus unitatum quas exprimit beatus Bernhardus, ut recitatur in proximo capitulo in responsione ad tercium argumentum. Et tunc loquendo ad sensum doctorum concedenda videtur sentencia cuiuslibet horum trium argumentorum. Nam primo concedi potest quod manet continue eadem ecclesia que est collectim omnes predestinati et singillatim singuli, ac singulus eorundem omnes uniti in Christo capite, sed tunc oportet intelligere personam ut caput, basim tocius compositi et quodlibet membrum suum confuse tamquam absorptum in Christo absconditum, sic quod ecclesia Christi dicat Christum cum quocunque fideli sibi incorporatum. Si enim papa dicitur ecclesia propter virtutem quam influit in ecclesiam, [p. 135] ut dicitur XXIVª, q. prima: Quodcunque, et VIIª, q. prima Scire debes, multo magis primus papa admirabilis dominus Jesus Christus. Iterum, si procedentes carnaliter ab Adam primo dicuntur fuisse ipse in quo originaliter peccaverunt, multo evidencius descendentes a secundo Adam dicentur fore secundus Adam in quo finaliter requiescent. Nam semen fidei quod est veritas est magis communicativum quam semen corporeum. Iterum, si combustibile vel ignibile ut lignum, carbo vel ferrum dicitur post ignicionem vulgariter esse ignis, cum alium ignem non percipimus hic nobiscum, multo magis spiritualiter comestus a Christo et plene digestus ab eo usque ad quartam digestionem que est glorificacio; ille ergo cui vivere Christus est, sicut sunt omnes sancti qui vivunt Deum: manifestum videtur ad hunc sensum quod sunt vita eorum que Christus est. Et patet quomodo verum est quod benefaciendo vel persequendo membra Christi, ut sic, taliter respicitur ipse Christus (ut patet Matthei XXV°, et Act. IX°, 5). Patet secundo quod martires nunquam possent sustinuisse tot passiones et fecisse tot mirabilia nisi per incorporantem et assimilantem membra capiti loquentem et operantem in eis dominum Jesum Christum. Et patet tercio causa quare Christus precepit suis declinare a mundo et sensibilibus et proicere totam scienciam, curam et affeccionem in ipsum, quia aliter non assimilantur sibi, quia nichil plus obstat assimilacioni cordi, capiti et corpori ecclesie quod est Christus, quam mundana affeccio. Ipse enim sepe in evangelio vocatur regnum celorum, corpus quod sequuntur aquile, et vita omnibus ipsum viventibus. Et patet [p. 136] quomodo dicendum est ad secundam racionem et terciam, concedendo sentenciam catholicam, in qua manuducunt, et cavendo diligenter ab errore intellectus et scandalo auditorii. Posset enim seductus credere quod omnis christianus foret idem personaliter cum Christo secundum corpus et animam, ita quod non forent dispares persone essencie vel nature, quod foret nimis erroneum.

[ENGLISH]

## ¶2 · 136.9–136.30

> [p. 136] Unde ne darem scandalum scole, distuli istam materiam. Aliquis enim est participative Christus ut quodlibet membrum eius, et aliquis personaliter ut solum ipsum caput, et illi qui non capiunt istam distinccionem, non capiunt sensum huius scripture Qui adheret Deo, unus spiritus est, et quomodo vinculum caritatis vel gracie est forcius quam vinculum naturale, ut dicit Augustinus in libro De Vera Religione XCI°, et tactum est cap. proximo in solucione tercii argumenti. Et patet quomodo intelligendi sunt doctores sancti, concedentes istam sentenciam, ut Augustinus, Crisostomus et Bernardus cum aliis qui sapiunt Deum et legem scripture. Et patet secundo quomodo tolli debent argumenta sophistica in ista materia, ut hii instant, si beati singuli sunt persona Christi, tunc sunt personaliter ipse Christus, et sic tantum Christus est homo, et omnis homo est omnis homo, cum aliis arguciis multipliciter in materia de trinitate. Sed hii non considerant quod multa possunt esse eadem persona communicative, participative vel secundum esse intelligibile, licet non personaliter, et patet quod consequencie multiplicate non procedunt.

[ENGLISH]

## ¶3 · 136.31–137.11

> [p. 136] Ultimo patet quod non est repugnancia in equivoce concedentibus et negantibus eandem proposicionem [p. 137] sensibilem, ut unus catholice negat quod ipse est Christus, sicut fecit Baptista, quia non fuit personaliter ipse Christus, et alius concedit quod omnis qui Christum induit est Christus (ut patet de sanctis predictis). Unde captandum est auditorium cui sic varie est loquendum, nec videtur esse concedendum quod omnis christianus sit Deus, licet omnis res sit Deus, et omnis substancia secundum esse intelligibile est Deus (ut patet in materia De Ideis), ut omnis homo est idem Christo, quia eadem species, et Christus est deitas, et tamen non est idem deitati.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 133.26: Christ and every one of his members make up one Church,
- 134.16: We must be careful to understand rightly what is unity of person.
- 135.4: The predestinate may be truly said to be Christ.
- 135.25: To gain this unity with Christ we must throw awa all worldly affections.
- 136.9: This oneness with his members does not take from Christ's separate personality as head.
- 137.1: In many cases the same words may be affirmed or denied according to the sense in which they are used,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 133: *Sed* (print: Q (alinea) Sed dubium; main lacks Sed, Q is not text) [INS?]
  - 133: *∅* (the 1 is a margin enumeration; print: quod sic ex) [INS?]
  - 134: *Tercio* (3 is a margin enumeration) [R4]
  - 134: *tam* [R3]
  - 135: *ut* (147b folio mark, Q alinea) [R3]
  - 135: *VIIª* [R4]
  - 135: *Christo* [R4]
  - 135: *Christus* [R3]
  - 135: *Christus* [R3]
  - 136: *et* (147b folio mark, R alinea glued) [R3]
  - 136: *sunt* (a is a margin letter) [R4]
  - 136: *secundo* (b is a margin letter) [NW]
  - 137: *fuit* [R3]
  - 137: *Christus* [R3]
  - 135: *XXIVª* [THIN]
  - 135: *q* [THIN]
  - 135: *Quodcunque* [THIN]
  - 136: *dicendum* [THIN]
  - 134: *∅* (English side-note (careful to under-), not text) [OVERRIDE-MARK]
  - 135: *XXV°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 133:
7. A in marg. : Sponsa Christi. 14. B: sponso semen fidei
gignendi. 21. A B: II Cor. X. A in marg. ccrr. Cor. XI. 24. 25. B:
idem coniugatus. 26. A in marg.: Dubium. A B in marg. : TJtrum
Christus et quodlibet membrum ecclesie sit eadem ecclesia in (A : deest)
numero (B manu rec). 3o. B: anima deest.
19. Decr. II. pars, causa XXVII, q. I, c. XLI]

p. 134:
11. Hic verbura omissum esse videtur. 16. A in marg. : Re-
sponsio. Nota quomodo omnia membra Chrisii sunt Christus cum corre-
spondenciis. (Above 147* without mark of reference.)

p. 135:
i. A in marg. : Papa quomodo dicitur ecclesia. 4. B: ab: deest.
16. Deum: hic aliquot verba excidisse videntur. 28. 29. B: assimu-
lantur... assimulacioni.
1. Comp. Decreti sec. pars, causa XXIV, q. 1, c. VI, et causa
VII, q. i, c. VII. i5. Philipp. I, 21.

p. 136:
3. B in marg. : Error intellectus et scandalum sunt cavenda.
9. A in marg. : Christus dupliciter dicitur. 12. A B: Salomon.
A^ corr. in marg. : solum. 17. B: de una religione. 21. A in
marg. : Contra dicta. 27 B : Sed hiis.
14. 1 Cor. VI, 17. 17 Cf. above pag. 109.

p. 137:
i3. B in marg. man. rec. : Unio Christi cum ecclesia est res pure
sacramenti. 26. B in marg. : Corpus est Christus personaliter.
21. B in marg. : Christianus sacramentaliter et participative.
i3. Non extat ap. Augustinum, et est fortasse ab ipso Beda
ad I Cor. 10 collectum ex tract. 26, 27, Aug. in Joan., vide
notam (455) Friedbergii ad Decr. III, p. De Consec. c. XXXVI.
(Corp. iur. can. I, i326.)
```

---

## Chunk 06-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-06-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-06-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "137.12–141.31"
divisions: "cap. 6 (heading 'CAP. VI.' at 116.1); part 7 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1025 words; 906 unanimous or majority-real; 104 settled by vote (DEL 1, R2 52, R3a 39, R3b 1, R5a 8, R6a 3); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n174–n178 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 6, part 7: [TITLE]

## ¶1 · 137.12–138.8

> [p. 137] Et ista sentencia tangitur in decretis, De Consecracione, d. IIª. Quia passus, ubi Augustinus dicit quod Christus in eucaristia commendavit corpus suum quod eciam fecit nosmet ipsos. Nec aliter digne accipimus quoad beatitudinem, nisi simus predestinati ad corpus eius, ut vivamus in eternum (ut exponit Augustinus super Joh. in omelia). Glosa ergo sic distinguit: Non, inquit, fecit nos corpus suum quod natum est de virgine et sumitur in altari, sed corpus suum spirituale quod est ecclesia. Et illa unio est pure res huius sacramenti (ut dicam alibi). Videtur tamen planius dicendum et modo loquendi sanctorum conformius quod idem est corpus in numero quod est ecclesia, et corpus in sacramento ac natum de virgine, cum sit ipse Christus. Aliter tamen est Christus ipsum corpus quia personaliter, et aliter christianus quia sacramentaliter, unus proprie et alius participative; et sic credo ego propheciam Christi intelligi [p. 138] Matth. XXIV°, 5: Multi venient in nomine meo, dicentes quia ego sum Christus, et multos seducent. Non enim reor aliquem christianum vel pseudoapostolum dicere quod ipse est Christus personaliter, sed sacramentaliter per incorporacionem in corpus Christi misticum; nam Ephesiorum V°, 27, scribitur: Dico autem sacramentum magnum in Christo et ecclesia. Illa autem pretensio solum nuncupative ecclesiasticorum seducit plurimos.

[ENGLISH]

## ¶2 · 138.9–138.16

> [p. 138] Septimo et ultimo arguitur contra dicta de gracia predestinacionis que est insolubile ligamentum membrorum ecclesie. Mirum namque videtur multis quomodo aliquod accidens absolutum non potest perdi, quomodo ipsum stat cum mortali, et quomodo ipsa semper rectificat verum dominium, sic quod verum dominium stet cum mortali sicut stat cum prescito ad tempus iustificacio.

[ENGLISH]

## ¶3 · 138.17–138.23

> [p. 138] Hic dicitur quod quicunque posuerit sentenciam doctoris profundi in correlario XXIIIⁱ cap., libri primi, scilicet quod Deus non potest quicquam noviter diligere vel odire nec vicissim aliquid odire vel diligere plus vel minus. Quicunque, inquam illud concesserit habet ponere graciam predestinacionis ad sensum expositum.

[ENGLISH]

## ¶4 · 138.24–141.31

> [p. 138] Unde non credo quemquam posse falsificare hoc fundamentum, quia indubie si est falsum est summe hereticum. Nam dato quod Deus quemquam predestinavit, sicut oportet ex fide scripture concedere Rom. VIII°, 30, de quadruplici gradu assimilacionis membrorum ecclesie, scilicet vocacione, predestinacione, [p. 139] iustificacione et glorificacione, patet quod est dare correspondenter ad predestinacionem Dei eternam unam predestinacionem passivam que incepit sicut incepit esse, quod iste est predestinatus. Et illa predestinacio cum sit precipuum donum Dei gratissime datum, cum nemo potest mereri suam predestinacionem, eo quod non potest inesse nisi insit primo instanti predestinati, ideo patet ex communi sermone dicto de eracia quod illa predestinacio est gracia precipua, sed dicitur ad aliquid, sicut sciencia, meritum et multa talia que vocantur qualitates. Nulla enim qualitas est res absoluta, potens per se existere, et sic conceditur quod non potest perdi, cum sit fundamentum glorificacioni vel beatitudini, que nec eciam potest perdi. Nam si alterum istorum perditur, ipsum fuit, et si unquam fuit, cum non potest esse accidenter predestinacio vel beatitudo, ipsum semper erit, et per consequens, non perditur, ideo si perditur, non perditur; et patet ad primum mirum. X Quo ad secundum dicitur, cum nemo dubitat quin multi predestinati peccarunt mortaliter, tam peccato originali quam actuali, ut patet de David, Petro et Paulo, et predestinacio non potest perdi iuxta dicta, manifestum est quod gracia predestinacionis stat cum peccato mortali, verumptamen repugnat peccato in spiritum sanctum, sicut gracia presciti secundum presentem iusticiam repugnat dampnacioni, licet aggregatum ex illa gracia et presciencia inferat necessario dampnacionem (ut patet XXXIIIª q. quarta, Vasis ire, et capitulo sequenti ex testimonio Augustini). Unde concedendum est quod Deus infinitum plus diligit Petrum quoad mores eciam dum negat eum, quam diligit Scarioth dum est [p. 140] in gracia, quia cum necessario semper eque diligit, semper diligit Petrum ad beatitudinem, cum scit eum finaliter converti, Scarioth autem semper diligit ad penam perpetuam, cum eternaliter videt omnia preterita vel futura sibi presencia, ut hic supponitur. Et patet quod gracia predestinacionis quam quidam vocant graciam prevenientem est quantumlibet melior quam gracia nude secundum presentem iusticiam quam quidam vocant graciam comitantem. Sed optima est gracia qua homo nnahter perseverat, que ducit ad confirmacionem et gloriam quam quidam vocant graciam consumantem. Et iste gracie sunt naturarum disparium, cum preter bonitatem supernaturalem dicunt relacionem ad mercedem. Nec est negandum quin prescitus habet graciam prevenientem, concomitantem et eciam consumantem opus aliquod bonum, sicut predestinatus habet graciam secundum presentem iusticiam. Sed sic contendens equivocat gratis eciam in signis nec effugiet, volens concordare in principiis fidei de modo diligendi Dei et methaphisica de quiditate gratie, quin proporcionaliter ut Deus diligit hominem est ipse gratus Deo, et proporcionaliter habet graciam, non quod illa gracia sit res, que posset per se existere, ut grosse et heretice concepit Pelagius, sed quod gracia sit qualitas spiritualis vel denominacio qua quis est formaliter gratus Deo. Et patet quod homo potest esse episcopus, dominus et minister ecclesie, eciam prescitus, existens in gracia secundum presentem iusticiam, sed homo non est cum hoc membrum sancte matris ecclesie. Unde sicut heres parvulus caret dominio, dum tamen tempore suo sit [p. 141] dominus omnium, sic predestinatus in mortali caret dominio, dum tamen alio tempore habet dominium, cum Deus eternaliter vult quod illud habeat pro suo tempore. Y Et si queratur, quare repugnat dominium in predestinato peccante mortaliter, dicitur quod ipse est tunc expers iusticie et cuiuscunque virtutis moralis, et per consequens, expers dominii quod oportet fundari in iusticia morali. Habet tamen iusticiam naturalem ad membra et omne quod placet Deo ut habeat, sicut et habet prescitus, et supra hoc habet iusticiam in predestinacione fundatam quam ad tempus obscurat piaculo. Unde non audeo dicere quod omnis peccans mortaliter non sit tunc membrum ecclesie, sicut videtur decretum dicere De Consecracione, d. I, Ecclesia, quia tunc esset tanta vel maior ambiguitas de prelatis, utrum sint membra ecclesie, sicut est de eis, ponendo solum predestinatos esse membra ecclesie, quia suspicionem probabilem habemus de mortali, qualem non habemus quod prepositi sunt presciti, et periret obediencia prelatis, cum non sic debemus honorare membra diaboli nec dare eis elemosinam, cum scimus quod egenis membris Christi est debita; sic enim vacaret beneficium intrusoris cotidie tam de iure quam de facto, et sic contra testimonia sanctorum nimis perturbaretur ecclesia. Alia autem sunt dubia concernencia ecclesiam que patent alibi, ut quod Christus existens humanitus fons vivus plenus gracie est quantumlibet melior moraliter quam totum residuum corpus ecclesie, cum gracia unionis sit alterius racionis quam gracia posteris derivata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 138.9: Objection: Difficulties in the doctrine of predestination.
- 138.17: Answer: It is involved in Bradwardine's doctrine of God's unchangeableness in love or hate.
- 139.5: Predestination is God's chief gift, and from its nature it cannot be given at all unless carried to fulfilment.
- 139.20: The predestinate may sin mortally,
- 140.8: but they have in them the grace of final perseverance.
- 140.22: Grace is not a thing but a quality by which man is pleasing to God.
- 141.5: A predestinate man sinning mortally, forfeits his dominion for the time.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 137: *Consecracione* [R4]
  - 137: *IIª* [R4]
  - 137: *cum* [R3]
  - 137: *Christus* [R3]
  - 138: *Christus* [R3]
  - 138: *Christi* [R3]
  - 138: *∅* (print: Illa autem pretensio; no a) [INS?]
  - 138: *pretensio* (print has pretensio) [NW]
  - 138: *∅* (of is the English side-note) [INS?]
  - 138: *XXIIIⁱ* (leaf zoom: dotted superscript i after XXIII) [R4]
  - 138: *membrorum* [R4]
  - 140: *gracia* [R3]
  - 141: *Christi* [R3]
  - 141: *intrusoris* (print has intrusoris) [NW]
  - 141: *Christus* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 137:
i3. B in marg. man. rec. : Unio Christi cum ecclesia est res pure
sacramenti. 26. B in marg. : Corpus est Christus personaliter.
21. B in marg. : Christianus sacramentaliter et participative.
i3. Non extat ap. Augustinum, et est fortasse ab ipso Beda
ad I Cor. 10 collectum ex tract. 26, 27, Aug. in Joan., vide
notam (455) Friedbergii ad Decr. III, p. De Consec. c. XXXVI.
(Corp. iur. can. I, i326.)

p. 138:
1. A: Matth. XXIV deest et hab. lacunam. 6. A: V deest.
8. A,false: ecclesiasticorum sacramentorum. 9. A in maig. : VII.
obieccio. 12. B in marg. man. alt.: Gracia predestii.acionis non
potest perdi. Stat cum mortali. i3. B: ipsa non; Ax habet: ipsum.
Sed rectius A: ipsa (scil. gracia). 16. A, B: iustificato. 17. A in
marg. : Responsio, utrum predestinacio stat in eodem cum mortali. (Above
i47d without mark of reference.) 18. In codd.: XXXII; vide supra
pag. 79. 24. A in marg.: De predestinacione.
18. sc. Bradwardini v. supra pag. 79.

p. 139:
5. B: principium domini. 7. A: nisi nisi. 27. A: repungnat.
28. A Aj: patet deest.
29. Decr. II. pars, Causa XXIII, q. IV, c. XXIII.

p. 140:
2. B: ad peccatum. 4. A in marg. : Nota de gracia triplici, B in
marg. man. alt. : Gracia predestinacionis preveniens. 10. B in
marg.: comitantem. 16. B in marg.: Consumantem. 21. A in
marg : Quid est gracia. 21. B: ut deus — habet deest.
28. B: et prescitus. 3l. B: tempore — alio deest.
1. Cf. Hus, De ecclesia, Opp. tom. I, 200".

p. 141:
5. A in marg.: Nota. i5. A in marg. : Utrum omnis peccans
mortaliter non sit tunc membrum ecclesie. B in marg. : Episcopus in
mortali non est protunc membrum ecclesie. 18. 10. A habet rasuram :
suspi . . . bilem. 3o. B: cum: deest.
i3. Dec. III. p. dist. I, c. VIII.
```

---

## Chunk 07-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-07-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-07-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "142.3–146.28"
divisions: "cap. 7 (heading 'CAP. VII.' at 142.2); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1049 words; 966 unanimous or majority-real; 68 settled by vote (R2 35, R3a 24, R3b 2, R5a 5, R6a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n179–n183 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 7, part 1: [TITLE]

## ¶1 · 142.3–143.30

> [p. 142] Convenimus ex mandato domini regis ad dicendum secundum videre nostrum veritatem in casu nobis exposito ad honorem Dei, ad profectum ecclesie et ad stabilimentum prosperum regni nostri, et hec tria in tractatu nostro se invicem consequuntur. Casus autem nobis expositus in compendio fuit iste: Duo viri armorum, homines legii regis nostri fuerunt inobedientes regi et legibus suis, et per consequens regno, in redempcione unius captivi Hyspaniensis, filii comitis de Dene in cuius custodia et redempcione rex noster secundum leges suas debuit habere precipuum interesse. Unde quia noluerunt reddere regi nostro captivi custodiam per quem captivum regnum redimeret multos milites suos in Hispania captivatos, mandati sunt per regem et regnum tuciori regis carcere mancipari. Sed secundo superaddentes inobediencie priori exierunt contra mandatum regis violente de carcere et prostrato custode carceris intrarunt septa Westmonasterii, in quibus vendicarunt omnino eximi a subieccione regis ex illius ecclesie libertate. Et tercio, [p. 143] minando quod exirent de terra nostra coniuncti nostris capitalibus inimicis, dicuntur arma sibi parasse, literas salvi conductus ab hostibus procurasse et consilium domini nostri regis tamquam falsum publice difidasse. Istis suppositis cum multis aliis que nunc esset nimis longum disserere, queritur utrum licet regi et regno suo in casu isto facere ut dicti captivi de Westmonasterio extrahantur. Et dicunt canoniste et civiliste tam regni nostri quam imperii quod, supposita veritate casus, non obstante quocunque privilegio Westmonasterii licet eos extrahere. Theologi autem dicunt concorditer quod, supposita veritate casus expositi, licet eos extrahere, servando tamen eos in vita et membris incolumes. In isto autem articulo intendo condicionaliter ex supposicione ventatis casus narrati procedere, et nec invasionem occisi nec suam occisionem propter ignoranciam occulte circumstancie comprobare. Quibus suppositis conclusio theologorum suadetur tripliciter. Pro primo argumento suppono primo legem domini Exodi XXI° capitulo, 14, datam Moysi: Si quis de industria occiderit proximum suum et per insidias, ab altari meo evellas eum, ut occidatur, ubi notatur primo ex natura condicionalis quod lex ista debet esse perpetua. Secundo notatur quod mora talis in sanctuario non debet esse ex aliquo privilegio perpetuo constipata, ideo dicit evellas eum. Tercio notatur quod summus gradus sanctitatis loci non debet aliquem talem in immunitate ecclesiastica conservare, cum ab altari qui est locus dignissimus ecclesie talis homicida evelli debeat.

[ENGLISH]

## ¶2 · 143.31–144.22

> [p. 143] Secundo supponatur factum sapientis regis Salomonis 111° Regum 2° cap., ubi fecit occidi Joab ad cornu [p. 144] altaris in tabernaculo domini, non obstante quod in exercitu patris sui David plus aliis militibus laboravit. Cuius occisionis doctores triplicem causam eliciunt ex scriptura. Primo, quia occidit Abner et Amasan tempore pacis ex vulpina industria, et tunc non gauderet immunitate ecclesie ex lege iam proximo allegata. Secundo, quia conspiravit cum Adonia et Abiathar contra regem. Et tercio precipue, quia rex timuit sibi quod Joab superstes in regno pacem populi perturbaret. Ideo subditur: David autem et semini eius et domui et trono eius sit pax in eternum a domino. of Ex istis tercio sic arguitur ex lege Dei quam non est fas homini inpugnare, licet nedum de altari Dei propter timorem perturbacionis regni fugitivum ad occidendum extrahere, sed ibidem eum occidere, ut patet ex dictis; sed infinitum minus esset fugitivum salvum in vita et membris extrahere; ergo, posita vehementi suspicione regis et sui consilii de prodicione vel perturbacione regni per tales fugitivos futura, licet eos secundum formam predictam extrahere et in tuta custodia conservare.

[ENGLISH]

## ¶3 · 144.23–145.18

> [p. 144] Nec valet dicere quod lex antiqua non obligat homines legis nove, tum quia super ista lege veteri fundant leges ecclesie iura sua, ut patet de quattuor qui non gaudebunt immunitate ecclesie, non licet ergo destruere principia legis ecclesie, tum quia arguitur ex legis divine iusticia per locum a maiori facti nostri iusticia, tum eciam quia tunc non remaneret nobis ecclesiasticis titulus decimas vendicandi, cum non ex lege nova sed veteri autorizatur nobis solucio decimarum. [p. 145] Nec valet secundo quod Joab commisit peccata. gravia, que plus movebant quam suspicio de perturbacione futura, tum quia sic est in casu nostro de superba eorum inobediencia, tum eciam quia certum videtur ex textu quod timor perturbacionis regni Salomonis fuit causa occidendi Joab precipua, quia ignoravit si priora crimina sint dimissa; ideo punicio quattuor personarum de quibus ibi fit mentio fuit precipue ad pacificandum in posterum regnum suum. Nec valet tercio dicere quod expectaretur quousque probata fuerit regni perturbacio sive prodicio, quia illa probacio foret nimis diutina contra prudenciam precavendi regno pericula; sed hoc videtur probabile quod non inferretur eis lesio corporalis, antequam culpa eorum fuerit notoria vel secundum leges patrie probata legitime. Aliud enim est dampnare hominem de reatu et aliud ad tutelam regni servare ipsum vehementer suspectum in salva custodia.

[ENGLISH]

## ¶4 · 145.19–146.28

> [p. 145] Quarta ficticia qua dicitur Salomonem in proposito illicite iudicasse non habet colorem, cum sic diceretur de opere legitimo aliorum quos sequimur ex auctoritate scripture. Cum enim scriptura tantum commendat sapienciam suam et non reprobat sed multiplici municione approbat illud factum, videtur ex sufficiencia scripture quod fuit factum legitimum. Sic enim supponunt leges humane bonitatem persone quousque probetur contrarium; immo omnes leges humane approbant iudicis inferioris iudicium quousque eius iniusticia convincatur. Secundo principaliter arguitur sic ad idem: Videtur quod quilibet legius homo regis Anglie tenetur tantum [p. 146] vel plus obedire sibi, sicut monachus abbati in quibuscunque que non sunt contraria legi Dei, sed monachus tenetur virtute obediencie et sub pena carceris obedire abbati in hiis que non sunt contraria legi Dei: ergo multo magis ad tantam obedienciam tenetur quilibet Anglicus suo regi specialiter in necessariis regimini regni sui. Ex quo sequitur quod servientes regis de sua privata familia tenentur parere sibi et suo sapienti consilio in huiusmodi licitis et honestis; sed mandatum est per regem et dictum consilium (sicut narratur) ut ad pacificandum regnum extrahant a Westmonasterio inobedienciarios predictos; ergo cum mandatum hoc vergit ad necessitatem regiminis regni sui, non obvians sed consonans legi Dei, sequitur quod dicti subditi tenentur in hoc parere monitis regis sui. Assumptum patet ex hoc quod obligacio regi est maior, cura regiminis regni est necessarior et pena delinquencium in regem est ex scriptura fundabilior. Nam beatus Petrus precipit christianis quod sint subiecti regibus Iª Petri II°, 13, et Apostolus precipit Rom. XIII°, 1 et Heb. XIII°, 17, Christi discipulis obedire prepositis, immo in veteri lege, quia Semei egressus est extra Jerusalem contra monita regis sui, ideo ex precepto sapientis Salomonis iustissime est occisus. Patet historia III° Reg. II° cap. Non autem inveniuntur tante evidencie ex scriptura quod monachus sub tanta pena parere debet abbati in monitis preter fidem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 142.3: As commanded by the king, we give our honest opinion on the case laid before us.
- 143.5: The question is whether it was lawful to take certain prisoners out of sanctuary at Westminster.
- 143.14: Taking the case stated as true, it was lawful for three reasons:
- 143.18: 1. God's law as given Ex. XXI, 14.
- 143.31: 2. The precedent of Solomon with Joab,
- 144.13: 3. because of danger to the realm.
- 144.23: O. T. precedents are valid, or there is no authority for, tithes.
- 145.1: 2. In this case there are the same grounds for action as in Joab's.
- 145.10: 3. It is unsafe to wait until treason is completed.
- 145.19: 4. Solomon's act is approved by Scripture.
- 146.1: 2. The King's subjects should obey him in everything not contrary to God's Jaw.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 142: *CAP. VII.* [HEAD]
  - 143: *minando* (148b folio mark, A alinea) [R3]
  - 143: *condicionaliter* (condicio-/naliter hyphenated; main token holds whole word) [R4]
  - 143: *primo* (print: suppono primo legem) [INS?]
  - 143: *Regum* [R4]
  - 143: *2°* (arabic 2 with degree sign) [R3]
  - 144: *semini* (10 is the line number) [R3]
  - 144: *lege* (30 is the line number) [R4]
  - 145: *gravia* [R3]
  - 146: *Iª* [R3]
  - 146: *II°* [R3]
  - 146: *13* [R3]
  - 146: *III°* [R4]
  - 146: *II°* [R3]
  - 145: *Nec* (148c folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 142:
2. B: ad dicendam. 4. D (Codex Dublin.): et stabilimentum. 6. A
in marg. : Casus. 9. B: fuerint. 21. 22. A A, B: exui a.
[. The Continuation of the Eulogium Historiarum gives an
account agreeing with Wyclif: Ipsi timentes perdere redemp-
cionem sui prisonarii noluerunt ipsum producere ad domini
regis man.latum. Rex per concilium eius obiecit eis quod ipsi
fecerunt carcerem in domibus suis infra regnum suum contra
suum mandatum et voluntatem ; et misit eos ad turrim Londonie.
Ipsi vero prostrato eorum custode fugierunt ad Westmonasterium.
Constabularius turris venit, ut eos reduceret et Johannes
Haule resistens interfectus fuit .... tamen Ricardus Shakille
ibat cum eo. Eul. Hist. III, ?4? comp. Rolls of Parlament vol.
III, pag. 10*, 5ob, 5i\

p. 143:
1. A Aj: convicti (coniucti). 4. A in marg. : Utrum licet in
casu inlra posito invadere monasterium. 6. A in marg. : Questio.
8. A in marg. : Responsio legistarum. it. A in marg. : Responsia
theologorum. i5. A A, B: casus deest. 22. A in marg. : Dtiplex
supposicio. 23. D: natura condlcionali 3l. B: Salomonis —
in thabernaculo deest.

p. 144:
4. D: Prima. i3. D: Ex istis tribus. A in marg. : Prima
responsio. 16. B in marg.: iubet occidere. 23. A in marg. :
Ficticia. 26. D: qui nunc gaudebunt. 26. 27. B: distrahere
priticipia. 28. B: facti ut nostri. 29. 3,0. D: ecclesiasticus.
10. III, Reg. II, 33.

p. 145:
1. A in marg. : Ficticia. 4. A B: superbia. 6. B in marg.
man. rec. : Absque completa investigacione suspicionis est occidendus.
7.8. B: Ideo punicior. 10. A in marg. : Ficticia. 11.12. D: illa
paracio. 12. D: diutina que excluderet prudcnciam. ij. In
codd.: inferreretur. 19. A in marg. : Ficticia. 22. A B: tante
commendat. 2(i. D: bonitates persone quousque probatur. 3o. Bl
Tercio principaliter. A in marg.: Secunda rcsponsio.

p. 146:
6. D: specialiter deest. A in marg. : Nota dc obediencia ad regem
continue infra. (Above 8d without mark of reference.) 12. D: su-
pradictos. i3. D: mandatum huiusmodi. 23. D: egressus fuit.
32. D: debito et pro occisione iniusta nimis gcneraliter.
```
