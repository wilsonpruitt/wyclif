# Translation brief: ecclesia 05-c–05-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-05-c.md chunks/ecclesia/wyc-ecclesia-05-d.md chunks/ecclesia/wyc-ecclesia-05-e.md` once and fix what it reports.
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

## Glossary (the 133 rows these chunks use; the full file is GLOSSARY.md)

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
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |

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
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
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
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 05-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-05-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-05-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "100.13–104.17"
divisions: "cap. 5 (heading 'CAP. V.' at 92.6); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "937 words; 862 unanimous or majority-real; 67 settled by vote (R2 44, R3a 20, R5a 3); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n137–n141 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 5, part 3: [TITLE]

## ¶1 · 100.13–102.6

> [p. 100] Dicitur tercio quod nisi christianus sciverit quadrare circulum, non est de membris ecclesie. Quadratura quidem circuli est scibilis, ut patet in Predicamentis, sed fuit in tempore Aristotelis nondum scita. Constat quidem quod figura tripunctalis ad instar trinitatis habet tria puncta supposita quorum nullum excedit reliquum sicut nec latera vel anguli, sed habent figuram et angulos utrobique. Correspondenter mistice tota trinitas personarum est parilis et nocio personarum ut latera nec non et proprietates earum ut anguli, et communem habent essenciam ubique plenariam ut figuram. Et sicut omnes illi tres anguli valent duos rectos, sic omnes tres persone divine valent ydemptice commune principium et commune principiatum. Si ergo in medio trium punctorum sit punctus positus, gerens similitudinem essencie que secundum racionem communicabilitatis distinguitur a personis, tunc figurat illud simul existens quadratum et circulus Deum nostrum qui secundum unum de viginti quatuor prophetis est circulus intelligibilis cuius centrum est ubique et circumferencia [p. 101] nusquam; iste autem simul circulus intelligibilis et quadratum secundum multiplicem racionem miserendi ecclesie constituit quadratum sensibile, quando in plenitudine temporis compaginavit quatuor elementa in quattuor humores ac quattuor complexiones et assumpsit plenum hominem quem sic fecit. Tunc enim sensibile quadratum humanitatis et circulus intelligibilis divinitatis factum est utrumque natura idem suppositum verbi Dei. Et istam sentenciam inculcat sanctus et devotus doctor magister Johannes de Howdan, alloquens amorem qui incarnavit filium in hec verba: Artem nosti, quadrantem circulum quem quadrasti, carnis quadrangulum spere Dei dans per miraculum sauciatum sanando seculum. Isti circulo oportet hominem inniti et secundum quadraturam quatuor virtutum cardinalium incorporari, si debeat esse membrum ecclesie dicente veritate Johannis XV° 4: Sicut palmes non potest ferre fructum nisi manserit in vite, sic nec vos nisi in me manseritis. Oportet enim christianum esse Deo insorptum per amorem, sic quod tota terrestritas instar ferri vel carbonis candentis pro zelo honoris Dei, honore seculi postposito, sit ignita; in cuius signum apostoli ex doctrina Christi Luce XXII° vocarunt se in suarum epistolarum iniciis servos Dei et domini Jesu Christi, ut per hoc reprimatur in eis fastus vel dignitatis apparencia, sed in dominum suum convertatur tota dignitatis tendencia. Sed hodie prepostere de dignitate, primatu et reverencia servi fit tota intencio, de honore vero Christi vel suo contemptu [p. 102] qui stat in legis suo observancia vel despectu non fit scrutinium; quod est signum evidentissimum quod tales superbi prepositi sunt extra Christum et suam ecclesiam, membra regis superbie que suam quadraturam ostentant in figura mundi, figuram autem substancie divine postponendo occultant.

[ENGLISH]

## ¶2 · 102.7–102.12

> [p. 102] Tercio arguitur contra dicta de corpore ecclesie per hoc quod pari evidencia qua illa foret unum corpus, et congregacio prescitorum constitueret unum corpus, consequens falsum, quia nec corpus naturale nec misticum, eo quod non foret forma uniens, nisi foret peccatum, illud autem non continuat sed seiungit.

[ENGLISH]

## ¶3 · 102.13–104.17

> [p. 102] Hic dicitur ex fide scripture quod omnes presciti constituunt unum corpus. Christus enim dicit Joh. VIII° 44, Judeis et principaliter sacerdotibus et phariseis qui dicebantur esse capitales ecclesie: Vos ex patre diabolo estis et desideria patris vestri vultis facere. Ex quo patet quod oportet esse unam generacionem que fuit mala in vulgaribus, peior in secularibus prepositis, sed pessima in prelatis, sicut generacio iustorum secundum tres gradus oppositos eis proporcionaliter correspondet. Si ergo sit una generacio perversorum, oportet quod sit unus iniquus homo habens partes que sunt membra diaboli, et cum non potest esse membrum vel caput nisi in comparacione ad totum corpus integrum, manifestum est quod est unum corpus diaboli, sicut est unum corpus Christi. Ubi autem corpus Christi vocatur corpus misticum propter misterium celestis coniugii inter Christum et ecclesiam Christi, corpus diaboli non est sic misticum sed obscurum, cum sic coniungi diabolo [p. 103] non sonat directe in misterium sed flagellum, et sic corpus diaboli habet esse naturale, cum secundum Augustinum in libro De Natura Boni... omne malum oportet fundari in bono: ergo omne malum moris fundatur in bono nature. Nec est inconveniens sed consonum modo loquendi sanctorum et vulgi vocare quamcunque creatam substanciam ex partibus quantitativis sive materialibus sive formalibus compositam verum corpus, sic enim vocatur aggregatum ex spiritualibus et indivisibilibus legibus corpus iuris. Tale ergo esse naturale habet quecunque aggregata substancia, unita in suo communi ut specie vel genere, et preter esse naturale habet racionalis creatura esse beatitudinis, virtutis vel vicii, ut est de membris Christi atque diaboli. Et loquendo de tali unione vel esse corporis negat Augustinus IIIª De Doctrina Christiana, XXXII° cap., quod ex membris Christi atque diaboli sit unum corpus compositum. Et ulterius quando tangitur de forma uniente corpus diaboli, dicitur quod est dare formam extrinsecam et deformitatem intrinsecam. Forma autem extrinseca est presciencia Dei eterna qua scit et ordinat omnes tales constringi ad penam perpetuam, deformitas autem intrinseca est finalis inobediencia vel superbia, contumacia quam sancti vocant culpam finalis impenitencie vel peccatum in spiritum sanctum. Et sic idem peccatum continuat et seiungit. Continuat enim membra diaboli, constringens eos in tartaris in sua malicia, et segregat eos a consorcio beatorum, sicut calor dissolvens mixtum congregat omogena, cum facit quodlibet elementum [p. 104] mixti dissoluti petere locum suum, sed segregat ethrogena, cum dissolvit compleccionem armonicam, resolvendo partes mixti in suas naturas simplices separatas. Oportet enim in die iudicii ex contrarietate frigoris corporis diaboli et caloris cantatis corporis Christi secundum legem forme ultime corpus bipartitum dissolvi, quando partes leves advolabunt cum capite suo quod est ignis consumens ad mansiones naturales in superis. Partes autem plumbee affeccione terrestri descendunt ad inferos, et sic duo hec nedum sunt duo corpora, sed due persone (ut tetigi cap. XLIII° tercii libri); de quo satis est adducere unum testimonium beati Gregorii, IV° Moralium, cap. XI°. Sicut, inquit, redemptor noster una persona est cum congregacione bonorum (ipse namque caput est corporis et nos huius capitis corpus), ita antiquus hostis una persona est cum cuncta colleccione reproborum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 100.13: A Christian must know how to square the circle.
- 100.27: God is said to be a circle with its centre everywhere and its circumference nowhere.
- 101.3: He has combined the four elements on man and has assumed the square thus made.
- 101.20: The Christian should lose himself in God by love.
- 102.7: 3rd objection: If the predestinate form one body, so must the foreknown.
- 102.13: Answer: The foreknown do form one body
- 102.24: of which the devil is the head.
- 103.6: A body may be composed either of material or formal parts.
- 103.19: The body of the devil is united by an outward form (God's foreknowledge) and an inward deformity (the sin of final impenitence).
- 104.4: At the day of judgment the parts of these two bodies (of Christ and the devil) will be finally separated.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 100: *quadrare* (3 is a margin enumeration, H alinea letter) [R3]
  - 101: *nusquam* [R3]
  - 101: *insorptum* (print has insorptum) [NW]
  - 103: *∅* (inserted run not in print here: line begins K 142c non sonat) [INS?]
  - 103: *Christi* [R3]
  - 104: *Christi* [R4]
  - 103: *elementum* (ele- here, mentum at top of p.104; main token holds whole word) [THIN]
  - 104: *mixti* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 100:
i. B: in hominibus non erit. 5. B : tanquam universalibus. ,3. A in
marg. : Nota de quadratura circuli. B in marg. : Quadratura circuli.
17. In codd: quod liguratur. . _ 32. AA,: cuius — intelligibilis deest.
3i. This passage is not to he found in the prophets.

p. 101:
1. B: iste aut. 2. A A^: racionum misercndi ecclesie ; B: miterendi
cice. 6. B: que sic fecit. 8. A: utramque. B in marg.: Circulus
quadratus. 10. A in marg. : J. Howdan. 11. In codd. : magister
J. de Howdan. 17. B in marg.: In ccclesia essc etc. 19. In
codd.: faccrc fructum. Correx ex Joh. XV 4. 21. B: quod nos.
11. John of Howden (f 1275) was the chaplain of Eleanor,
the mother of Edward I.

p. 102:
5. A: figuram figuram. 7. A in marg. : Malorum congregacio cst
unum corpus naturale sicut bonorum est unum corpus misticum. (Above
1420 witliout mark of reference.) 12. A: continat. i3. A in marg. :
Responsio. 14. B in marg. man. rec. : Ecclesia malignancium per
conscqucns est unum corpus. A in marg. : Triplcx gcneracio mala. 22. A :
corrcsponJent A^: correspondent. 26. B: corpus deest. 3o. B:
Christi deest. 3i. B: cum coniuugi.

p. 103:
3. boni. . . lacuna in codd.; A in marg.: Augustinus. Hic locus in libro
supra laudato non extat; sed plures similes inibi inv^nies. 9. B: ut
supra corpus. 9. A in marg. : Quid est corpus. B in marg. man.
rec : Ex esse virtutis (vel) vicii unum corpus esse non potest. 16. A
inmarg.: Augustinus. 19. A in marg. : Nota de forma uniente malos
in corpus unum. 26. B: et sicut. A in marg.: Conclusio. 28. B:
in carceris. A in marg. : Exemplum.
16. Aug. Opp. tom. II, p. I, pag. 58.

p. 104:
2. A: ethromo gena^A^: etherogena. 5. A: calore; A,: calcc;
I3:calores. 10. Codd.: terrestres. i3. A in marg. : Gregorius. Codd.:
cap. IX. 17. B est cunta (sic). 18. A in marg. : Obieccio. Nota
de continuitate ecclesie. 21. B: Antccedens falsum. 22. B: cum parte.
i3. Opp. Greg. tom. I, pag. 112. 27. In Predicamentis, id
est, in Gategoriis, cf. Categ. Cap. VI. : Itidemque in corpore potes
accipere communem terminum, lineam vel superficiem, qua cor-
poris partes coniunguntur. Aristoteles latine, interpretibus variis,
ed. ac.td. reg. Borussica pag. 3. Arist. graece ed. Bekker I, pag. 4.
```

---

## Chunk 05-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-05-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-05-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "104.18–108.17"
divisions: "cap. 5 (heading 'CAP. V.' at 92.6); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "985 words; 912 unanimous or majority-real; 58 settled by vote (R2 36, R3a 13, R3b 1, R5a 8); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n141–n145 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 5, part 4: [TITLE]

## ¶1 · 104.18–107.11

> [p. 104] Sed adhuc instant sophiste per hoc quod, si ecclesia catholica sit unum corpus et omne corpus est vere continuum, tunc ipsa ecclesia est vere continuum; consequens falsum, quia partes ecclesie distant per quotlibet miliaria sine parte ecclesie media intercepta.: Hic concedi debet conclusio quod ecclesia catholica est vere continuum. Nam omne corpus cuius partes copulantur ad terminum communem est vere contitinuum; dicta ecclesia est corpus huiusmodi, ergo conclusio. Assumptum patet per Aristotelem in Predicamentis, c ipitulo de quantitate, sic describentem quantitatem continuam. Si ergo dicte ecclesie sit quantitas continua secundum [p. 105] quam est formaliter magna, tunc ipsa est vere continua, ymo non solum quelibet pars huius ecclesie continuatur cum aliqua alia eius parte, sed omnes simul copulantur ad eundem terminum communem. Pro quo declarando suppono quod, sicut ecclesia est unum aggregative, sic membrum eius et accidencia sua sunt unum aggregative. Aliter enim non foret multitudinis credencium cor unum et anima una (ut scriptura sacra dicit Act. IV° 32). Ex quo patet quod omnes partes ecclesie collective intellecte copulantur ad eundem terminum communem ex omnibus communibus terminis ecclesie aggregatum. Nam iste communis terminus copulat quamlibet partem quantitativam ecclesie cum alia, hic secundum unam eius partem et hic secundum aliam. Ymo (ut logice loquar) sicut punctus replicatus est tota substancia linee superficiei et corporis quantitatis, sic substancia materialis aggregata est universum corporeum et eius partes sunt proporcionaliter partes mundi. Aliter enim Deus non est locutus per os sanctorum contra scripturam Luce 1°, 70, nec ecclesia foret unanimis uno ore honorificans Deum Rom. XV°. Nec distancia localis nec discontinuac mathematice quantitatis obest, quia similitas secundum interiorem hominem et adnascencia membrorum ecclesie secundum caritatem excedit unitatem sensibilem. Ulterius, cum maior sit unitas gracie quam nature, ostendendum videtur quod non solum quelibet pars ecclesie continuatur cum aha, nec solum quod omnes partes ecclesie continuantur ad invicem, sed quod quelibet eius pars continuatur cum qualibet. Nam omnis pars ecclesie copulatur cuilibet per eundem terminum communem, ergo omnis pars ecclesie continuatur cuilibet. Pro assumpto suppono quod mediator Dei et hominum Christus Jesus plenus gracie et veritatis faciat quamlibet partem ecclesie prodesse [p. 106] cuilibet. Aliter enim non iuvarent se ad integrandum matrem ecclesiam ad profectum cuiuslibet. Tunc arguo sic: Eo ipso quo creatura agendo prodest alteri quodammodo est cum ea, sed quelibet pars ecclesie agendo prodest cuilibet, ergo quelibet quodammodo est cum qualibet. Assumptum videtur ex hoc quod omne sic prodesse est meliorare, et per consequens, ex acquisicione qualitatis que est bonitas est alterare et sic movere, sed secundum philosophum VII°. Phisicorum: In omni motu movens et motum sunt simul. Sic enim concedunt quod sol secundum speciem suam que lumen dicitur est simul cum qualibet parte orbis subluminaris quam alterat, sensibile est ad omnem punctum medii ubi agit speciem suam, et res post sui corrupcionem est in suo effectu modo quo loquitur scriptura Ecclesiast. III° 14: Didici quod omnia opera que fecit dominus perseverent usque in eternum. Ex istis sequitur quod sicut quelibet res est simpliciter eterna secundum esse suum intelligibile, sic est perpetua nedum in sua specie et principiis quiditatis, sed in suis causis individuis et in sua causacione, cum semper sit causacio cuiuslibet rei. Et conformiter est ubique, licet non secundum existenciam individui; et idem videtur sapientem Salomonem sentire Eccl. III° (ubi supra): Quod factum est, inquit, ipsum permanet, que futura sunt iam fuerunt, et Deus instaurat quod abiit. Ecce quomodo primo proponit, quomodo quelibet creatura permanet perpetuo et probat hoc de nobis futuris, eo quod ipsa iam fuerunt, tam in suis causis quam in suis effectibus. Probat hoc iterum de preteritis, eo quod Deus instaurat in fructu operis [p. 107] illud quod nobis preteriit; sicut enim sol non posset agere in orbe sublunari secundum suam speciem, nisi anima mundi vel forma eius que est mundialitas deferret speciem ipsam sustentans secundum aliquid sui, sic non esset possibile rem facere quicquam boni post suam corrupcionem, nisi Deus eternus instauret ipsam, causando eius pretericionem, causando eciam quod res succedens se habet in tali ordine. Et movetur quia res que preteriit pro suo tempore ita causat; sicut enim sequitur: Ista creatura hic causat, ergo hic est, ita sequitur: nunc causat, ergo nunc est.

[ENGLISH]

## ¶2 · 107.12–108.17

> [p. 107] Ex istis videtur quod omnia futura de nec essitate evenient et quod nichil anichilari potest. Nam Deus qui non potest impediri ordinat cuncta esse perpetua. Ideo dicit Ecclesiastes (ubi supra): Non possumus eis quicquam addere nec auferre que fecit Deus, ut timeatur. Si enim pretericio rei non potest destrui, multo minus eius esse quod est previe requisitum, nec aliter esset timendus ut Deus nisi sic fecerit. Quando autem variavi ab ista sentencia, non cognovi ut modo, quomodo res habet multiplex esse, sed omne esse posui existenciam individuam rei in suo genere. Sic redeundo ad propositum, patet quod gracia et caritas Jesu Christi que realiter est ipsemet Christus, est terminus communis copulans quodcunque membrum ecclesie cuilibet alteri. Ista autem copulacio per medium terminum communem tam nobilem est longe prestancior quam copulacio per terminum mathematicum. Et hinc reor Christum qui tantum amat communia tam crebro posuisse se medium. Nam ipse est Dei virtus que consistit in medio inter patrem et filium. Unde voluit concipi in equinoccio vernali quod [p. 108] habet tam diem quam noctem pro medio diei naturalis Luce I° 36. Hic mensis est sextus illi qui vocatur sterilis. Voluit eciam nasci in medio noctis Sap. XVIII° 14, 15. Cum enim quietum silencium contineret omnia, et nox in suo cursu medium iter haberet, omnipotens sermo tuus domine exiliens de celo a regalibus sedibus venit. Tercio voluit poni in diversorio, quod est hospitaliaria media inter duos vicos. Quarto voluit poni in medio duorum animalium, ut patet Luce, II°. Quinto voluit opponere in medio doctorum, Luce, II° 46. Sexto posuit se in medio discipulorum, ministrando, Luce, XXII° 27. Septimo positus est in medio latronum triumphando Joh. XIX°, 18. Octavo post resurreccionem stetit in medio discipulorum, informando, Joh. ultimo. Iste ergo est abbas promittens Matthei XVIII° 20, quod ubicunque duo vel tres congregati fuerint in nomine suo, in medio illorum est.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 104.18: Objection: The Church cannot be one body because its parts are separate in space.
- 104.23: Answer: All the parts have a common point of union in the head.
- 105.22: Local distance does not interfere with this union.
- 105.26: Not only is there a continuous body but every part is in touch with every other,
- 105.34: since each helps all,
- 106.8: and therefore is with it, since things that affect each other must be together.
- 106.18: Every thing that is is eternal, as well in its Causation as in its quidity.
- 107.12: All future things will happen of necessity, and nothing can be annihilated.
- 107.23: The grace and love of Christ is the common term uniting all the members of the Church.
- 108.2: Christ in all things loved the mean,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 104: *ecclesia* (M is alinea letter) [R3]
  - 105: *locutus* [R3]
  - 105: *invicem* (print has invicem) [NW]
  - 106: *III°* [R4]
  - 106: *III°* [R4]
  - 107: *illud* (143a folio mark, N alinea) [R3]
  - 107: *quia* (143b folio mark) [R4]
  - 108: *naturalis* (natu-/ralis hyphenated; main token holds whole word) [R3]
  - 108: *I°* [R3]
  - 108: *15* (arabic 15 (verse number, Sap. XVIII° 14, 15)) [R3]
  - 108: *II°* [R3]
  - 108: *II°* [R3]
  - 104: *secundum* (se- here, 142d cundum on p.105; main token holds whole word) [THIN]
  - 104: *Sed* (print has Sed before adhuc; not in neighbours) [DELX]
  - 105: *quantitatis obest,* (two printed words; * between them is the folio mark, dropped) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 104:
2. A: ethromo gena^A^: etherogena. 5. A: calore; A,: calcc;
I3:calores. 10. Codd.: terrestres. i3. A in marg. : Gregorius. Codd.:
cap. IX. 17. B est cunta (sic). 18. A in marg. : Obieccio. Nota
de continuitate ecclesie. 21. B: Antccedens falsum. 22. B: cum parte.
i3. Opp. Greg. tom. I, pag. 112. 27. In Predicamentis, id
est, in Gategoriis, cf. Categ. Cap. VI. : Itidemque in corpore potes
accipere communem terminum, lineam vel superficiem, qua cor-
poris partes coniunguntur. Aristoteles latine, interpretibus variis,
ed. ac.td. reg. Borussica pag. 3. Arist. graece ed. Bekker I, pag. 4.

p. 105:
• 9. B: et scriptura. A: Act. I". 22.-In codd. Joh. XV; correxi.
26. A in marg. : Conclusio. Nota quclibetpars ecclesie continuatur cuilibct.

p. 106:
8. A A,: bonitatis. 9. A in raarg. : Aristoteles. i5. A: corrump-
cionem. i5. A A^: effectu deest. 16. A in marg.: Conclusio.
Quelibet rcs est perpetua in suis causis in divinis et in sua causacione.
16. Eccl. III, 14: Deus pcrseverent in perpetuum.
q. Aristotelis Physicae auscultat. VII, 1. Ed. Bekker I, 243:T6
os Ttpiitov v.tvoov, jiYj u>5 t6 06 Ivexey, aXX1 ofrsv 7; apj(Yj TY/S
xivnsecog, iailv upa xCu xivot>[t,ey^>. 25. v. i5.

p. 107:
1. A Aj: idem quod. 11. B: illa sequitur. 12. A in marg.: Cor-
relarjum. Nccessitas absoluta. 14. Codd.: impedire. B : cunta.
17. A A,: Si pretericio. 20. Codd.: variam. 23. A in marg. :
Gracia et caritas Jesu Christi est terminus communis copulans quod-
cunque mcmbrum ecclesic cuilibet alteri. 3o. B in marg. man.
rec : Medium in omnibus tenuit Christus. A in marg. : Quomodo
Christus crebro s^ posuit in medio. 3l. A in marg. : Nota octo media;

p. 108:
4. In codd: Sap. VIII. 4. 5. A: contiret. Aj B: continerent.
Correxi e Sap. XVIII 14. 7. In Sap. loc. cit. : durus dcbellator in
mediam exterminii terram prosilivit. 16. A in marg: Copulacio et
unio Christi et in Christo. 19. A A, : Et secundo. 23. A. A,:
mixta singenia. 24. B: quin longe.
7. in diversorio. Cf. Lucae II, 7. 19. Cf. Aristotelis Ethic.
Nic. lib B. 7, ed. Bekker II, 1107. 24. singenia i. e. ouyyEvs-.a.
```

---

## Chunk 05-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-05-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-05-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "108.18–112.9"
divisions: "cap. 5 (heading 'CAP. V.' at 92.6); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "856 words; 776 unanimous or majority-real; 65 settled by vote (INS 1, R2 44, R3a 17, R3b 1, R5a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n145–n149 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 5, part 5: [TITLE]

## ¶1 · 108.18–110.8

> [p. 108] Hec autem fecit abbas noster, ut doceat nos tenere medium virtutis in nostris operibus. Et ex II° Ethicorum extrema ab illo medio in quo virtus consistit deviancia corrumpunt virtutem; nec video quin, si quantitas mathematica continuat elementa, si humor aqueus continuat iuxta singenia, si armonia corporis animalis faciat membra adnata esse continua, quasi longe plus latitudo, longitudo, sublimitas et profundum (de quibus loquitur apostolus Eph. 111° 18) facit unanimes vere unum. Illa eciam aqua sapiencie (de qua Ecclesiastici XV, 3) continuabit unius moris in domo, et demum armonia in trinitate fundata illapsa universali ecclesie ipsam ex membris compaginatam faciet unam sponsam. [p. 109] 143° Unde Bernhardus, De Consideracione, libro V°, ad Eugenium papam, ponit octo modos unitatum. Est, linquit, unitas que collectiva potest dici, ut multi lapides faciunt acervum unum. Est unitas constitubtiva, cum multa membra unum corpus vel multe partes unum quodque totum constituunt. Est et coniugativa qua fit, ut duo iam non duo sint sed una caro. Est et nativa qua anima et caro unus nascitur homo. Est unitas potestativa qua homo virtutis non instabilis non dissimilis sed unus sibimet semper nititur inveniri. Est consentanea, cum per caritatem multorum hominum est cor unum et anima una. Est et votiva, cum anima votis omnibus adherens Deo unus spiritus est. Et est dignativa unitas qua limus noster a Dei verbo in unam assumptus est personam. Et super istas octo unitates dicit in quodam sermone quod est unitas principalis qua tres persone divine sunt una indivisibilis essencia. Et sic omnis unitas potest dici supernaturalis, naturalis vel virtualis. Duo posteriora membra recipiunt divisiones multiplices et cum in equivocis non sit contradiccio, patet quod non repugnat corpus ecclesie non continuari, loquendo de continuacione naturali sensibili, cum quelibet pars eius quantitativa completa in actu non sic continuatur cum alia naturaliter incommunicante, et tamen continuatur alia continuacione spirituali plus forti per spiritum Dei diffusum in cordibus omnium membrorum ecclesie habencium omnia in communi. q Quarto principaliter arguitur per hoc quod ad univocam racionem ecclesie requiritur univoca racio suarum [p. 110] parcium, sed non est talis univocacio in peregrinantibus, dormientibus et beatis. Ergo non univoce constituunt Christi sanctam matrem ecclesiam que non potest dici etherogena, nam si fides ponatur forma constituens membrum ecclesie, videtur quod beati quibus inest clara visio, evacuata fide non sint de membris ecclesie, si caritas adhuc caritas patrie et caritas vie sunt disparium racionum.

[ENGLISH]

## ¶2 · 110.9–110.17

> [p. 110] Sed hic dicitur (ut supra) quod forma exemplaris eternaliter formans ab extra quodcunque membrum ecclesie est predestinacio Dei eterna. Forma autem per se et ab intrinseco constituens membrum ecclesie est predestinacio passiva. Ipsa enim non potest inesse multiplicative, nisi assit ecclesia. Et sic habet quilibet predestinatus fidem formatam caritate predestinacionis secundum quam constituitur ecclesiavel eiusmembrum. Et ita racio est univoca in quocunque salvando. faith

[ENGLISH]

## ¶3 · 110.18–112.9

> [p. 110] Unde sicut crementum et profectus persone non variat eius speciem, quia sic homo secundum variaciones etatum transiret de specie ad speciem, sic etas persone sancte matris ecclesie non variat eius speciem, sed corroborat per accidens racionem ecclesie. Ymmo manet eadem fides in mundo, in purgatorio et in celo. Sed imperfeccio que ex parte est hic evacuabitur in beatis; manebit, inquam, eadem fides que creditur, cum sit veritas eterna, et manebit eadem fides qua et secundum quam creditur, quia manebunt iidem actus et habitus. Est enim prima adhesio quam creatura habet de veritate credenda actus fidei cui accidit obscuritas enigmatica pro via que evacuatur in patria veniente intuicione clara, caritas autem eadem habens in patria confirmacionem loco incertitudinis. [p. 111] Dissensio autem est aput doctores nostros, eo quod aliqui intelligunt fidem aggregative pro adhesione prima cum imperfeccione sequente. Aliqui autem intelligunt fidem personaliter pro illa adhesione cui inest per accidens intuicio vel enigma. Illa autem prima adhesio precedens racionem est eiusdem racionis hic et in patria, sed ibi validior (sicut alibi diffuse exposui). Et sic omnes predestinati habent continue fidem gracia predestinacionis formatam, et sic non cadit a membris ecclesie per mortale, ut patet III°, De Doctrina Christiana XXXII°, et epistola XXXIII ad Bonifacium. Explicat hoc de David et Petro; de David autem explanat hoc in libro De Octo Questionibus ad Dulcicium amicum suum; quorum omnium racio est quia Deus non potest quemquam noviter diligere vel odire, sed sub quocumque gradu amat vel odit aliquem, sub eodem gradu eternaliter sic amat vel odit. Nec est detestabile quod Deus semper odit beatos in celo, nam semper odit peccata eorum preterita, non pro semper, ideo semper amat eos pro sempiterna glorificacione. Unde ecclesia excommunicat tales cum, ipsis existentibus in mortali, notificat eos privari communione sanctorum secundum presentem iusticiam, cum humidum fluens ad tempus eis deficiat, nunquam autem anathematizat tales vel omnino dividit a corpore Christi nec potest. Et ista est plerumque sentencia Augustini, si bene inspicitur, non in dolo. Et patet ex solucione proximi argumenti et huius, quomodo intelliguntur sancti Ysidorus, De Summo Bono. [p. 112] cap. XIX° et Augustinus, epistola XXXIIIª ad Bonifacium, quomodo ecclesia fidelium est ubique diffusa, ecclesia autem hereticorum est in parvo angulo coartata. Predestinati nempe dilatant more celestium fructus suos, alii autem licet sint hinc plures in numero, more terrestrium constringuntur. Christus enim caput prioris ecclesie cui oportet ut secunda subserviat, est potencior patre mendacii quem sic ligat, hoc est, ipsum in membris suis penaliter sic constringit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 108.18: which Aristotle has shown to be the seat of virtue.
- 109.18: Unity may be supernatural, natural or virtual.
- 110.1: 4th objection: If there is but one Church there should be but one way of membership, but we on earth have not the same form as the blessed.
- 110.9: Answer: We have the same form: God's predestination.
- 110.18: Moreover faith and charity are the same, only that in heaven they lose their imperfection.
- 111.1: Difference of opinion as to what Faith is.
- 111.8: All the predestinate have faith and cannot lose iteven by mortal sin.
- 111.21: The Church may rightly excommunicate them for sin, but cannot cut them off from the body of Christ.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 108: *II°* [R3]
  - 109: *partes* (bold 3 is a margin enumeration) [R4]
  - 109: *una* (bold 4 is a margin enumeration) [R4]
  - 109: *semper* (bold 6 is a margin enumeration) [R4]
  - 109: *Deo* (bold 8 is a margin enumeration) [R4]
  - 109: *loquendo* [R4]
  - 109: *univocam* (uni-/vocam hyphenated; main token holds whole word) [R4]
  - 110: *Christi* [R3]
  - 110: *assit* (print has assit) [NW]
  - 110: *non* (bold 1 is a margin enumeration) [NW]
  - 110: *evacuatur* (30 is the line number) [R3]
  - 111: *aput* [R4]
  - 111: *III°* [R3]
  - 109: *suarum* (sua- here, rum at top of p.110; main token holds whole word) [THIN]
  - 112: *XXXIIIª* (no comma; followed by ad) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 108:
4. In codd: Sap. VIII. 4. 5. A: contiret. Aj B: continerent.
Correxi e Sap. XVIII 14. 7. In Sap. loc. cit. : durus dcbellator in
mediam exterminii terram prosilivit. 16. A in marg: Copulacio et
unio Christi et in Christo. 19. A A, : Et secundo. 23. A. A,:
mixta singenia. 24. B: quin longe.
7. in diversorio. Cf. Lucae II, 7. 19. Cf. Aristotelis Ethic.
Nic. lib B. 7, ed. Bekker II, 1107. 24. singenia i. e. ouyyEvs-.a.

p. 109:
1. A in marg.: Bernliardus. A B in marg.: Unitatis octo modi. 10. B:
non instabit. i5. B: una assumptus. 20. A in marg. : Quarta
obieccio. Hic nota. Nota materiam de univoca racione parcium ecclcsie.
B in marg. man. alt.: Predestinacio <T activa
1. Bernhardi Opp. pag. 1048. 16. Cf. sermonem Bernhard!
(Opp. pag. 45o): Unitas principalis que et substancialis est in
trinitate.

p. 110:
4. A A, etheromogena. 9. A in marg. : Responsio. 16. A:
membra; B: ut eius: B in marg.: Quid hominem constituit membrum
ecclesie. 32. A in marg.: Nota bene quomodo manet eadem lides
in celis que est hic.

p. 111:
2. 3. B:prima imperfeccione. 4. A. in marg. : Duplicilcr dicitur fides.
(Above I43d without mark of reference.) 10. A in marg. : Augustinus.
11. In codd. epistola XXXII. Cf. Opp. Aug. tom. II, pag 263. i3. in
codd. A A,: de decem questionibus. B: de conclusio iubet. Correxi;
cf. Opp. Aug. VI, pag. 121. A in marg. : Deus odit ab eterno et diligit
quos diligit et odit. 16. B: sic amat.
29. Isid. De Summo Bono, lib. I, cap. XIX: Sancta ecclesia ideo
dicitur catholica pro eo quod universaliter per omnem sit mundum
ditlusa. Nam hereticorum ecclesie in partibus mundi coartantui.

p. 112:
t. In codd. cap. XVI. In codd. iterum: epistola XXXII. A in
marg. : Ubi est ecclesia. 10. Bin marg. man. alt.: Diffinicio ecclesie.
A in marg. : Quedam descripcio ecclesie. 16. 17. A: assummeret.
23. A: patrinum. B: patuum. A, correxit: patrum. 24. A
B: quod deest. Aj : sequitur quod. 26. In codd. : sequitur quod
nullus. B: nullus patruum. A, : nullum patrum. 20. B in marg. man.
rec: Extra ecclesiam non est salus
```
