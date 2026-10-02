# Translation brief: ecclesia 03-b–03-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-03-b.md chunks/ecclesia/wyc-ecclesia-03-c.md chunks/ecclesia/wyc-ecclesia-03-d.md chunks/ecclesia/wyc-ecclesia-03-e.md` once and fix what it reports.
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

## Glossary (the 135 rows these chunks use; the full file is GLOSSARY.md)

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
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
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
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
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
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
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
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| zizania | cockle | Douay–Rheims (Matt. 13:25). Ruled 2026-09-28. |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 03-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "51.8–54.22"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 2 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "769 words; 702 unanimous or majority-real; 52 settled by vote (R2 33, R3a 15, R3b 1, R5a 3); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n88–n91 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 2: [TITLE]

## ¶1 · 51.8–52.9

> [p. 51] Tercio colligitur quod adulterantes scripturam sacram in ista sentencia sunt ypocrite, quos prophetavit apostolus Timotheo periculosis temporibus in ecclesiam successuros. Pro cuius declaracione suppono factum, quomodo moderni ecclesiastici fingunt secundum tradiciones humanas quod nedum licet eis, sed peccarent mortaliter, omittendo prosequi pro defensione matris ecclesie. Illud meminit beatus Gregorius (ubi supra). Istis, inquit, si forte dicatur: Cur ista agitis qui seculum reliquistis? respondent illico Deum se metuere et idcirco tanto studio in defendendis patrimoniis Christi insudare. Hodie autem superadditur quod bona pro quorum acquisicione, conservacione et repeticione tantum insistimus sunt bona ecclesie et patrimonium Christi: ideo licet pro bono universalis ecclesie conservacioni eorum insistere. Iste autem fucus ex hoc tollitur quod deserendo ipsa pro Christo tam relinquens quam ecclesia ipsa habet, ut dicit Augustinus super Joh. Omelia VIª. Ideo, ut dicit beatus Gregorius: Frustra laboravit nullo timore cogente, et ut dicitur Psalmo XIII°, 5: Illic trepidaverunt timore, ubi non [p. 52] erat timor. Ecce, inquit, divina voce precipitur: Si quis tulerit tibi tunicam et voluerit tecum in iudicio contendere, dimitte illi pallium. Et rursum: Si quis quod tuum est tulerit, ne repetas. Paulus quoque apostolus discipulos suos cupiens exteriora despicere, ut valeant interna servare, admonet eos dicens: Omnino delictum est in vobis quod iudicia habetis inter vos, quare non magis iniuriam accipitis quare non magis fraudem patimini?

[ENGLISH]

## ¶2 · 52.10–52.15

> [p. 52] Nec valet glosa ypocrite quod hec sunt consilia, non precepta. Si enim sunt Christi consilia et tu in habitu pretendis te super alios Christum diligere, adhereres eius leni consilio, preceptis seculi pretermissis; aliter enim fores ypocrita, offendens in dileccione Dei super omnia.

[ENGLISH]

## ¶3 · 52.16–54.22

> [p. 52] Nec valet secundo dicere quod oportet aliquem solicitari circa hec bona, ne ecclesia defraudetur, quia illis relictis pro Christo tu venus haberes hec bona, et sic ecclesia. Ideo vis exponere te periculo dimittendo perfeccionem divini consilii quam acceptando, Deus non posset de promissione temporalium deficere; nam cum istud officium incumbit laicis, patet quod indigencia ecclesie stat in paucitate procurancium pro spiritualibus bonis ecclesie, sicut fuit de contemplativis, quando crevit ecclesia. Cum ergo istud officium sit alcius, salubrius et ecclesie necessarius, manifestum est quod amor culpabilis temporalium est in causa huius cece eleccionis. Unde Gregorius ibidem capitulo X°: Plus Deo sese amare convincitur qui neglectis hiis que Dei sunt propria tuetur; perdere namque animas hominum ypocrite non timent, et [p. 53] amittere res cum mundo transeuntes quasi districto iudici posituri racionem timent; ac si placatum inveniant, cui desideratis rebus, id est, racionabilibus perditis insensibilia et non quesita conservent. Certum est quod non. Possidere, inquit, in hoc mundo aliquid volumus et ecce veritas clamat: Nisi quis renunciaverit omnibus que possidet, non potest meus esse discipulus. Perfectus ergo christianus quomodo debet res terrenas iurgando defendere quas precipitur non possidere? Itaque cum res proprias amittimus, si perfecte Deum sequimur, in huius vite itinere a magno onere levigamur. Non ergo debemus, periculo nos exponendo, perfecciorem statum relinquere et statum plus periculosum, plus a Christo elongatum et plus tardativum eligere. Nec valet tercia responsio ypocrite qua dicit se propter amorem iniuste occupantis contendere, ne ipse peccet iniusta detencione, sed ut ipse habeat instrumenta virtutum quibus possit ad honorem Dei plus matri sue proficere. Unde pro prima parte dicit beatus Gregorius (ubi supra): Quidam cum nostra rapiunt, solummodo tolerandi sunt; quidam vero servata caritate prohibendi; non tamen sola cura ne nostra subtrahant, sed ne rapientes non sua semetipsos perdant. iste fucus est magis palliatus quam ceteri: nam (sicut alias ostendi) licet inferioribus ecclesie pro bonis fortune contendere, servata caritate utrimque et sancta intencione cum forma procedendi legitima. Ideo debet homo illius responsionis cavere, ne propinquitas ad voraginem periculi preparet ad ruinam. Nam ut dicit beatus Gregorius ibidem: Plus ipsis raptoribus debemus metuere quam inhiare ipsis rebus irracionabilibus [p. 54] defendendis, quia illa non rapta morientes amittimus, cum illis vero et nunc condicionis ordine, etsi corrigi studeant, post percepcionem finalis premii unum sumus. Quis autem nesciat, quia minus ea quibus utimur et plus debemus amare quod sumus? Si ergo pro sua utilitate raptoribus loquimur, iam non nobis que temporalia, sed eciam illis que sunt eterna vindicamus. Qua in re illud est solercius intuendum, ne per necessitatis metum cupiditas surrepat rerum et zelo succensa prohibicio, impetu immoderancie distensa, usque ad odiose turpitudinem contencionis erumpat. Dumque pro terrena re pax a corde cum proximo scinditur, liquido apparet quod plus res quam proximus amatur. Si enim caritatis viscera eciam circa raptorem proximum non habemus, nosmet ipsos peius ipso raptore persequimur graviusque nos quam alter poterat devastamus, quia dileccionis bonum sponte deserentes a nobis ipsis intus est quod amittimus, qui ab illo sola exteriora perdebamus. Sed hanc ypocrita formam caritatis ignorat, quia plus terrena quam celestia diligens contra eum qui temporalia diripit sese in intimis immani odio inflammat.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 51.8: Hypocrites apply Scripture falsely in their own support.
- 52.10: The hypocrite says: a. These are counsels, not commands; as if the counsels of Christ were not to be followed.
- 52.16: b. He says that but for his care the Church would be defrauded;
- 52.24: but the care would be better bestowed on spiritual things.
- 53.16: c. He declares that he acts for the good of the wrong doer:
- 53.25: This is a better excuse but it is dangerously near to evil.
- 53.31: St. Gregory teaches
- 54.5: that we must care only for the eternal interests of the wrong doer;
- 54.15: otherwise we hurt ourselves more than him.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 51: *VIª* [R3]
  - 52: *accipitis* [R4]
  - 52: *ypocrite* [R4]
  - 52: *alios* [R3]
  - 52: *consilio* [NW]
  - 52: *fores* [R3]
  - 52: *∅* ('that' is side-note text (He says that)) [INS?]
  - 52: *solicitari* [NW]
  - 52: *salubrius* [NW]
  - 53: *amittere* (135c is the folio mark) [R4]
  - 53: *voraginem* (30 is the line number) [R4]
  - 54: *iam* (zoomed on leaf: dotted i, no crossbar = iam) [R3]
  - 54: *zelo* (italic z) [NW]
  - 54: *peius* [R3]
  - 53: *mundo* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
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

p. 52:
3. B in marg.: Contra contencionem sacerdotum. i(i. A B in marg. :
Triplex responsio. A in marg. : Contra illos qui loquuntur contra con-
siliorum implecionem. 21. A provisione. 28. AB in marg. :
Gregorius. Ainmarg.: Paupertas cleri iuxta Christi concilia. (Above i35c.)
1. Matth. V, 40, vid. Greg. 1. c. 3. Luc.VI, 3o. 7. I. Cor.
VI, 7. Greg. 1. c.

p. 53:
2. 3. In codd. : invenient. 21. A B in marg. : Gregorius. 25. A B in
marg. : Conclusio. B in marg. : Licet inferioribus ecclesie contendere pro
bonis ecclesie. 27. B: utrumque. 3i. A in marg.: Raptor est a nobis
plus amandus quam res arrcpta per raptorem.
6. Luc. XIV, 33.

p. 54:
10. Codd.:pro liabito; vide Gregor. ubi supra pag. 1007. AB: in inani.
n. Codd. : turpitudinis contencionem. 22. A: inflammant. 27. In codd.:
bona. 32. A B in marg. : Conclusio; B: primo nedum.
```

---

## Chunk 03-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "54.23–58.16"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 3 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "833 words; 747 unanimous or majority-real; 72 settled by vote (R2 47, R3a 18, R5a 6, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n91–n95 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 3: [TITLE]

## ¶1 · 54.23–58.16

> [p. 54] Sciendum vero est quod sunt nonnulli quos caritatis gremio nutriens mater ecclesia tolerat, quousque ad spiritualis etatis incrementa perducat, qui nonnunquam et sanctitatis habitum tenent et perfeccionis meritum exequi non valent. Ad dona namque spiritualia minime assurgunt et idcirco hiis qui sibi coniuncti sunt ad tuenda ea que terrena sunt serviunt et nonnunquam in defensionis eiusdem iracundia excedunt. Et istos nomine religiosos declarat iste sanctus papa involvi duplici malicia, primo quia nedum infirmitate sed sciencia contra conscienciam suam peccant, secundo quia fingendo sanctitatem in defendendo [p. 55] bona ecclesie pro facinore querunt laudes. Ex istis conclusionibus huius sancti demonstrabilibus perpendere potest ecclesiasticus tam regularis quam secularis, si diligenter examinent conscienciam cum scriptura, palpando intencionem, volucionem et motus anime cum intencione supremi iudicis, quod non tam assidue contenderent pro vocatis bonis ecclesie. Patet secundo: Quomodo dominus papa non foveret sed extingueret lites huiusmodi secundum regulam evangelii: si enim committeretur regnis, provinciis et parrochiis examen vite clericorum, sic quod non ministrarentur eis stipendia subtracto sensibiliter eorum ministerio, viveretur superioribus prepositis tolerabilius et sacerdotibus cum populo melius quam est modo. Defectus autem patronorum et populi posset speculator superior facilius corrigere quam totum onus per se cum falsis testibus litem gignentibus supportare. Nec requiritur alia lex in distribuendo officia sacerdotum nisi cognicio a capite per testes probabiles, quod unus sit rector in ministerio sacerdotali, solicicior habiliorem preponere; de quo si non gauderet, depositus foret, ex ypocrisi ac cupiditate suspectus. Et patet tercio quod causa dissensionis et perturbacionis ecclesie sit malicia sacerdotum. Nam eorum virtuositas maxime pacificaret ecclesiam; ideo ex opposito eorum perversitas maxime perturbat ecclesiam, quia peccatum quod est per se causa perturbacionis ecclesie in ipsis est gravius. Dicunt enim contra fidem quod sunt viri sancte matris ecclesie, licet sint apostatantes partes diaboli, et per consequens, faciunt confusionem in fide, confusionem in sacramentis et subtraccionem spiritualis suffragii a Deo per ipsos instrumentaliter derivandi. [p. 56] Unde confidenter prenostico quod ante correccionem nostram secundum statum primevum non deficiet regnorum perturbacio. Cum igitur apostolus raptus fuit usque ad tercium celum, videns longitudinem cursus ecclesie quoad tempus, latitudinem quoad numerum prelatorum et profunditatem quoad sensum quo clerici sunt in sensu domini profundati, verti non debet in dubium quin prophetavit iuxta exposicionem beati Gregorii de ecclesia in instante, vocans eos ypocritas se ipsos amantes, verbum domini adulterantes et cauterizatam conscienciam habentes (ut patet I.Timotei IV°, 2). Signum autem precipuum foret quod clericus ad modum loquendi apostoli se ipsum diligat, si propter affeccionem proprietatis temporalium dimissa cura presbyteri se ipsum sollicitat. Que enim posset esse maior adulteracio verbi domini quam intelligere ipsum ad sensum diaboli iuxta quem defendatur esse hereticum et blasfemum, ymo quod licet ex auctoritate eius committere leve mendacium? Aut quid posset esse magis periculosum cauterium quam clericum habere conscienciam adustam cupidine, quod cessans ab operibus reprehensibilibus in facie ecclesie propter candentem amorem quem habet ad temporalia, publicet et defendat sine fructuosis operibus se esse membrum sancte matris ecclesie. Licet enim talis evacuet cauterio suo fluxum viciorum sensibilem, verumptamen diabolus auctor fluxus talis superflui tantum disseminat per meatus ypocritarum absconditos per totum residuum corporis fluxum peccati lubrici, et sic ex simulata consuetudine factus heresiarcha habet [p. 57] in capite, hoc est, in racione cauterium Antichristi. Nulli enim secundum beatum Gregorium, in Registro, secundo capitulo, periculosius vel amplius nocent in ecclesia sancti Dei. Sed redeundo ad difficultatem dimissam obicitur per sanctum Thomam de Christo, conclusione octava, articulo III°, ubi dicit quod Christus est caput omnium hominum, tam fidelium qui uniuntur sibi in actu per graciam, quam infidelium qui sunt solum in potencia eius membra, et post subdividit secundum predestinatos et prescitos qui recedentes ab hoc mundo totaliter desinunt esse membra Christi. Et probat hoc multiplici racione. Quantum ad hoc testimonium sancti Thome, videtur michi quod ipse equivocat vere dicendo quod Christus secundum deitatem est caput extrinsecum tocius humani generis; quod potest dici aggregative unum corpus naturale, cui eciam Christus benefacit sicut et toti mundo secundum humanitatem, cum virtute passionis Christi acquiritur quedam perfeccio secundaria toti mundo. Et sic secundum humanitatem benefacit toti humano generi, cum punit omnes dampnatos, vel ex infidelitate, ut eos qui non considerant in dominum Jesum Christum, vel ex desperacione qua dimissa debuerunt celestibus aspirare, vel tercio de iudicio temerario quo dimisso debuerunt domino Jesu Christo caritative finaliter adherere. Et sic intelligitur triplex causalis Christi Johannis XVI°, 8: Arguet mundum de peccato, de iusticia et [p. 58] de iudicio. De peccato infidelitatis que autonomatice dicitur peccatum, quia non crediderunt in patrem neque in me; de iusticia quam debuerunt habuisse, aspirando cum mediis congruis ad patriam naturalem, quia ad patrem vado; et de iudicio quo temere arbitrantur dogma mundi atque diaboli ardencius diligendum, cum princeps mundi iudicatus est per Christum docentem oppositum. Et sic opposita fidei, spei et caritatis que corresponderent per ordinem trinitati dampnant prescitos in finali iudicio (ut alias diffuse exposui). Non enim vidi in sancto Thoma vel alio doctore probabili quod totum illud genus sed pars eius predestinata sit sancta mater ecclesia, sponsa Christi et universalis vel catholica ecclesia, corpus Christi misticum de quo scriptura loquitur. Et de tali est nobis sermo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 55.8: Litigation would be suppressed if the Pope asked rulers to withdraw the pay of those who neglected to minister.
- 55.18: The only needful rule being that men should be appointed for fitness and deposed if they deserve it.
- 55.28: Wickedness of priests troubles the Church.
- 56.1: 'Trouble will not cease until we return to the primitive order.
- 56.8: St Paul prophesied of "lovers of themselves" who care for wealth and not for their priestly duty;
- 56.16: "corrupters of the word", who wrest it to defend lying; "having a seared conscience", who proclaim themselves members of the Church but bring forth no fruit.
- 57.5: Objection: Christ is said by St. Thomas to be the head of all men.
- 57.14: In one sense this Is true as to his deity
- 57.20: and as to his humanity.
- 58.11: But St. Thomas does not say that the whole human race is the mystical body of Christ, but the part that is predestinate.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 54: *nomine* [R4]
  - 54: *∅* (pec-/cant is one word, already at pos 242 (peccant)) [INS?]
  - 55: *bona* (135d is the folio mark) [R3]
  - 55: *intencione* (final e slightly broken) [R4]
  - 55: *viri* [R3]
  - 56: *deficiet* [R3]
  - 56: *Cum* [R4]
  - 56: *quid* [R3]
  - 57: *in* (136a is the folio mark) [R3]
  - 57: *per* [R3]
  - 57: *III°* [R4]
  - 58: *Christi* [R3]
  - 56: *confidenter* [THIN]
  - 56: *prenostico* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 54:
10. Codd.:pro liabito; vide Gregor. ubi supra pag. 1007. AB: in inani.
n. Codd. : turpitudinis contencionem. 22. A: inflammant. 27. In codd.:
bona. 32. A B in marg. : Conclusio; B: primo nedum.

p. 55:
io. B: regnis regnis. n. 12. B: ministrentur. ib. Codd.: videretur.
19. A in marg. : De eleccione ad prelacias. B in marg.: Nota deeleccione
in preposituram qua forma (iet. A: cognito a capitc. 20. AB: recto in.
21. B: humiliorem. 25. B: pacificari.

p. 56:
1. A in marg.: Nota bene. 8. B in marg. : Qui dicunt se ipsos
amare secundum apostolum. 10. A in marg. : Verbum domini adulte-
rantes et conscicncia cautcrizata (Above i3oa . Without mark of reference.)
B in marg. : Adultcracio vcrbum (sic) dei nota. Nota habentes conscienciam
cauteriatam (sic). 19. 20. AA,: Aut quod. 24. AB: defcndet.
At corr. in : defendat.
10. Gf. Greg. Expos. in psalm. quint. et I. Timoth. IV, 2.
II. Tim. III, 2.

p. 57:
5. A in marg.: Contra dicta. Nota: In equivoco conceditur quod
Christus est capud tam fidelium quam infideliura omnium. 6. B in
marg.: S. Thomas. AB in marg.: Obieccio. i3. AB iri marg.:
Rcsponsio. 16. B: aggregare. 29. A B in marg. : Joh. XVI.
2. Cf. Gregor. (Regulae past. lib. I, cap. II): Nemo quippe
amplius in ecclesia nocet quam qui perverse agens nomen vel
ordinem sanctitatis habet. Conf. dist. LXXXIII, c. 2, corp. iur. can.
6. Thomae Aquin. Opp. (Ed. Venet. 1774) tom. V, pag. 5i.

p. 58:
1. Codd.: autonomastice. 16. A in marg. : Equivocando conceditur
corpus diaboli esse ecclesiam Christi. B in marg.: Ecclesia Christi nun-
cupative. 23. B : ecclcsie Romane cuius. 27. A in marg. : Presciti
quomodo sunt in potencia membrum (sic) Christi secundum beatum
Tliomam. B in marg. : Sanctus Thomas. 32. B: formem.
```

---

## Chunk 03-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "58.17–60.10"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 4 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "440 words; 390 unanimous or majority-real; 31 settled by vote (DEL 1, R2 15, R3a 11, R3b 1, R5a 2, R6a 1); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n95–n97 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 4: [TITLE]

## ¶1 · 58.17–60.4

> [p. 58] Non repugnat ergo equivocando vocare corpus diaboli ecclesiam Christi, ut posito quod una communitas nominetenus clericorum prescita credatur esse particularis ecclesia, licet committat peccata quantumcunque enormia. Tunc vulgus reputat eam esse ecclesiam, ymo quilibet eorum asserit quod propter ordinem est vir sancte matris ecclesie, racione cuius tituli excecat populum, in fide, officio et ypocrisi indubie menciendo, quia sic idem foret simul membrum Christi et membrum diaboli, ecclesia sanctorum et ecclesia malignancium. Tales enim dicit Thomas eciam membra ecclesie in potencia, licet nunquam reducantur ad actum. Ac si diceretur illud habet potenciam ex sufficiencia passionis Christi et potestate sui arbitrii esse membrum Christi, cum tamen nude sit membrum congregacionis habencium fidem informem, licet nunquam sit membrum corporis Christi mistici. Sed ne ego laborem in istis [p. 59] equivocis, limitavi nomen ecclesie, ut signat sponsam Christi. L Tres tamen evidencie fiunt ad probandum hanc sentenciam. Primo dictum apostoli I. Timothei IV°, 10 Salvator est omnium et maxime fidelium; secundo per illud I. Johannis, II° cap., Ipse propiciacio pro peccatis nostris, non autem pro nostris tantum est, sed eciam pro tocius mundi. Sed in quantum salvat et propiciatur hominibus, est caput eorum: ergo Christus est caput omnium hominum. Tercio per hoc quod. omnes homines sunt fideles, quia habent fidem de Deo. Patet quod ista argumenta procedunt ex equivoco: nam concedi potest cum sancto Thoma quod Christus quoad esse naturale est caput eciam diaboli, et per consequens, caput membrorum suorum, non solum quoad esse naturale, sed eciam quia sunt fratres Christi quoad naturam specificam, quorum omnia peccata ad eorum dampnacionem et penam cedunt, sanctis vero ad gloriam. Et sic misericorditer punit fratres suos ad bonum eorum (ut alias declaravi). Loqui autem sic generaliter atque equivoce est preter propositum nostrum, quia loquimur de capite et membris unius hominis ex sponso et sponsa, de quo Joh. III°, 13 dicitur quod nemo ascendit in celum, nisi qui descendit de celo (ut Augustinus exponit, Joh. Omelia XIIª). M Et quantum ad dictum apostoli, dicitur communiter quod esse salvatorem vel salvare est equivocum ad quatuor: primo generaliter accipitur pro apponere medicinam ad infirmum cuius virtute egrotus sanari poterit, et isto modo salvavit Christus totum mundum humani generis, cum apposuit medicinam passionis, que suffecit redimere multos mundos. Istam autem [p. 60] medicinam apposuit Christus vel obtulit humano generi, cuius septima pars nunquam suscepit eam, sicut semper infideles quos Christus dicit Joh. III°, 18, iam iudicatos, et illos dicit sanctus Thomas esse membra

[ENGLISH]

## ¶2 · 60.5–60.10

> [p. 60] Christi in potencia, non in actu. Alii autem recipiunt medicinam sed finaliter recidivant, ut presciti. Tercii vero receperunt medicinam et post lapsum ad sanctam matrem ecclesiam revertuntur, ut peccatores predestinati. Quarti quippe sanantur virtute meriti Christi nec unquam post incidunt in mortale.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 59.3: Objectors give three proofs of their opinions: 1. St. Paul's words;
- 59.8: 2, St. John's words;
- 59.10: 3. All men are believers since all believe about God. All these arguments rest on a double use of language.
- 59.26: Four uses of the word to save:
- 59.27: I. To some salvation is offered but refused.
- 60.5: Others receive it but fall away. A third sort after falling away return. The fourth class receive and hold to it.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 59: *apostoli* [NW]
  - 59: *I* (print 'I. Timothei') [THIN]
  - 59: *Timothei IV°* (token spans two printed words 'Timothei IV°,') [THIN]
  - 59: *10* ('their' is side-note text; print '10:') [THIN]
  - 59: *Thoma quod* (token spans two printed words) [THIN]
  - 59: *Christus* [THIN]
  - 59: *III°* [R4]
  - 59: *13* (print has verse number '13,' here (Joh. III°, 13)) [DEL]
  - 59: *XIIª* [R3]
  - 60: *Christus* [R3]
  - 60: *Christus* [R3]
  - 60: *18* [R3]
  - 60: *iudicatos* [R3]
  - 60: *membra* (print has membra at start of line 5 before Christi) [INS?]
  - 60: *finaliter* [R3]
  - 60: *humano* (136 folio mark glued) [R4]
  - 060: *∅* ('ercii' is inside neighbour 45 (print Tercii; neighbour reads Tercn)) [DELX]
  - 60: *∅* (Tercii printed whole; scan split i|ercn) [OVERRIDE]
  - 60: *Tercii* (print: Tercii vero (agent 13)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 58:
1. Codd.: autonomastice. 16. A in marg. : Equivocando conceditur
corpus diaboli esse ecclesiam Christi. B in marg.: Ecclesia Christi nun-
cupative. 23. B : ecclcsie Romane cuius. 27. A in marg. : Presciti
quomodo sunt in potencia membrum (sic) Christi secundum beatum
Tliomam. B in marg. : Sanctus Thomas. 32. B: formem.

p. 59:
[.. B: literavi. 3. A B in marg. : Triplex obieccio. 4. B in marg. :
I. Tim. 4, I. Joh. 2. 5. (i. B: per idem. 7. A: nostris non tantum est.
i3. A in marg.: Rcsponsio. 21. A in marg.: Nota. 25. B in marg. :
Augustinus. A B in marg. : Salvacio triplcx. 29. A in marg. : Christus
salvavit totum mundum quoad sufficicnciam.
25. Opp. Aug. III, pars II, pag. 387. .

p. 60:
3. B in marg. : Joh. III. 14. B in marg. : Deus vult omnes homines
salvos fieri. 18. B in marg.: Humanum genus ultra diabolum habet
libertatem arbitrii. 3i. In codd.: quarti. 32. B: distrahati. B in
marg. : Quadruplex digestio prius habetur cap. primo huius tractatus.
```

---

## Chunk 03-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-03-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-03-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "60.11–64.10"
divisions: "cap. 3 (heading 'CAP. III.' at 47.6); part 5 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "944 words; 839 unanimous or majority-real; 87 settled by vote (R2 45, R3a 29, R5a 12, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n97–n101 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 3, part 5: [TITLE]

## ¶1 · 60.11–63.21

> [p. 60] Et sic vere dicit apostolus quod Christus est sal- vator maxime fidelium in tercio et quarto gradu, et intelligunt quidam dictum apostoli I ad Thimoteum II°, 4, directe ad litteram, quod Deus vult omnes homines salvos fieri. the Ad secundum obiectum ex dicto beati Johannis est eadem sentencia. Christus enim est quoad sufficienciam propiciacio, hoc est, medicus vel medicina propiciativa tocius humani generis, quod habet ultra diabolum post ruinam angelorum libertatem arbitrii, ut salvetur, cum totum genus humanum sit homo quidam qui descendendo ab Jerusalem in Jericho incidit in latrones; qui relictus secundum totum semivivus ex gracia Samaritani habuit medicinam dispositam et ministros mercede et instruccione duplicis testamenti provide dispensantes, secundum quam totus ille homo sanari poterit. Sed preter illum hominem naturalem oportet secundum Adam generare spiritualiter unam generacionem priori permixtam que est sancta mater ecclesia. Et in illo corpore sunt aliqui vere membra ut predestinati, quarte digestioni assimilati, sive sint ad tempus discrasiati ut lapsi, sive [p. 61] solide post primam sanacionem in sanitate perpetua stabiliti. Illi autem qui sunt intra dictam ecclesiam non ut partes, sunt in gradu duplici, ut quidam in sua infidelitati perpetuo permanentes qui nunquam receperunt caritatem vel graciam. Et hii sunt tamquam aer aut ventus in homine, in quem nunquam egit suus calor naturalis. Hii autem sive commixti sint localiter sive solum in genere humano, prosunt ad refrigerium sancte matris ecclesie. Hii autem sunt tamquam superfluitates cibi sponsi ecclesie qui spiritualiter digerit predestinatos et demum assimilat. Et iste est cibus de quo loquitur Christus Johannis IV°, 32: Ego cibum habeo manducare quem vos nescitis. Unde superflua illius cibi sunt infecta duplici, ut aliqui sunt in stomacho sancte matris ecclesie recepti per graciam secundum presentem iusticiam, sed ex eorum ypocrisi vel heresi non sunt propter abhominacionem caritatis operantis digesti, sed in hac vita sensibiliter evomendi; de quibus loquitur spiritus sanctus Apocalypsis III°, 16: Neque calidus es neque frigidus, ideo incipiam te evomere de ore meo. Tales autem sunt sive clerici sive laici pretendentes se operari ad edificacionem sancte matris ecclesie quidquid agunt, sed tamen quia habent intenciones frigidas temporalium propter quas principaliter agunt, ideo sunt ypocrite Deo abhominabiles ut aqua tepida que provocat ad vomitum. Et hii sunt Deo maxime abhominabiles racione falsitatis in duplicitate latentis que opponitur veritati. Unde sicut iuxta Aristotelem primo Metyororum VI° cap. [p. 62] aqua sic calida cicius congelatur propter exalaciones frigidas quas pori caloris recipiunt: sic pretendentes sanctitatem huiusmodi sunt periculosissimi hostes ecclesie, per quos ut proditorie aperientes portas ecclesie subintrant frigidi fide et virtutibus; qui plus quam inter fideles extinguunt caritatem vocate ecclesie et congelant. Debet, inquam, ecclesia fervere pura caritate ex simplici participacione Christi qui est ignis per se calidus caritate, et matrem omnium malorum cupiditatem postponere, et per consequens, non adinvenciones lucrativas plus quam legem Dei diligere. Sunt autem intra ecclesiam alii presciti magis absconditi, evadentes evomicionem huiusmodi, ut hii tamquam superfluitas sicca digestionis prime, hii tamquam superfluitas humida digestionis secunde, et hii ut apostemata vel vermes digestionis tercie. Et patet quod non sequitur: Si quicunque viantes sunt in ecclesia, tunc sunt de ecclesia, sed econtra. Nam scimus zizania crescere inter frumenta, corvum pasci in eadem area cum columba et paleam inorreari pro tempore inter grana, et tamen est incommunicans distinccio inter ista, sicut exemplatum est in corpore humano. Ita ymaginari debemus de sancta matre ecclesia, et sic intelligendus est textus I. Joh. II°, 18, cum dicitur: Nunc Antichristi multi facti sunt; ex nobis prodierunt, sed non erant ex nobis, nam si fuissent ex nobis, permansissent utique nobiscum. Sicut enim superfluitas procedit ex cibo et membris solidis, dum tamen non sit ex eis,. sic purgamenta ecclesie procedunt ex ea, non tamen erant ex ea ut partes, cum nulla pars eius potest ab ea excidere. Unde ad discernendum distinccionem puri et superfluorum huiusmodi dicit beatus Johannes epistola secunda canonica: Omnis, inquit, qui recedit et non permanet in doctrina Christi, Deum [p. 63] non habet. Doctrina autem Christi sunt humilitas, caritas et paupertas. Quicunque ergo oderit ista, non imitando Christum ut aquila, scito quod non sit de sua ecclesia. Et sic tres gentes excluduntur a membris ecclesie qui omnino peccant in fide scilicet omnino infideles ut pagani; heretici ut sacerdotes et pharisei cum eis similibus qui nunquam gustaverunt dulcedinem spei beatitudinis ex imitacione sapiencie incarnate, sed resident facietenus in ecclesia gracia affeccionis primatuum temporalium et carnalium voluptatum; tercii vero qui gustaverunt paululum digestionis divine, sed propter defectum caritatis perfecte aut finalis perseverancie excidunt tamquam inhabilia, ut formaliter induant caput Christum; et hii peccant in trinitatem et tres virtutes catholicas (ut dixi superius). Omnes autem tales, dicit Augustinus, non esse de membris ecclesie, sicut in corpore hominis naturali nemo dicit proporcionalia esse membra. Sanctus autem Thomas videtur loqui generaliter, equivocando de membro, scilicet de membro temporaliter vivo et de membro omnino mortuo putativo.

[ENGLISH]

## ¶2 · 63.22–64.10

> [p. 63] Ad tercium negatur ad sensum scripture quod omnes homines sunt fideles. Conceditur tamen cum Damasceno quod omnis homo habet fidem saltem informem cum naturaliter prima impressione entis cognoscit saltem confuse primo omnium Deum esse et omnem articulum fidei. Sed ista fides informis non sufficit denominare hominem fidelem vel partem ecclesie, sed oportet excludere omnem infidelitatem finalem. Et de tali fideli loquitur Christus Johannis X° 28, promittens, ut omnis qui credit in filium non pereat, supple morte perpetua; ille autem credit in [p. 64] filium qui credendo ipsum inheret sibi finaliter per amorem. Unde quia de tali finali inherencia est nobis dubium, ideo docet Augustinus super Johannem, Omelia XIIª, quomodo membrum ecclesie est Deo et cui ipse voluerit revelare satis cognitum. Novit, inquit, dominus qui sunt eius, novit qui permaneant ad coronam, qui permaneant ad flammam, novit in area sua triticum, novit paleam, novit segetem, novit zizania. Ceteris autem est illud incognitum qui sunt columbe et qui corvi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 60.11: Christ is specially the saviour of the third and fourth class.
- 60.16: Answer to the second objection: Christ is a Sufficient propitiation for all men, who have naturally free will and may avail themselves of it;
- 60.26: but they need a second birth in Christ,
- 61.2: which those have not who are in the Church but not of it.
- 61.14: These the Church cannot digest,
- 62.4: since they want the warmth of charity.
- 63.4: Three classes who are not members of the Church 1. Infidels 2. Priests who make profession for the sake of wealth. 3. Those who have tasted of divine grace but lack final perseverance.
- 63.22: All men are not believers in the Scripture sense.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 60: *sal-* (first half of sal-/vator hyphenated across line (vator is pos 82); N is the alinea letter) [THIN]
  - 60: *vator* (second half of sal-/vator (italic)) [THIN]
  - 60: *maxime* [THIN]
  - 60: *fidelium* [R5]
  - 60: *in* [R3]
  - 60: *et* (trailing 1 is the margin number) [NW]
  - 60: *intelligunt* [R4]
  - 60: *II°* [R3]
  - 60: *Christus* [R3]
  - 61: *graciam* (136d is the folio mark) [R4]
  - 61: *III°* [R4]
  - 61: *16* [R3]
  - 61: *Metyororum VI°* (token spans two printed words 'Metyororum VI°') [R4]
  - 62: *exalaciones* (print has exalaciones; 136d is the folio mark) [NW]
  - 62: *II°* [R3]
  - 64: *XIIª* [R3]
  - 61: *solide* (alinea N and 136c folio mark glued) [THIN]
  - 63: *non* (136d folio mark glued; italic non) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 60:
3. B in marg. : Joh. III. 14. B in marg. : Deus vult omnes homines
salvos fieri. 18. B in marg.: Humanum genus ultra diabolum habet
libertatem arbitrii. 3i. In codd.: quarti. 32. B: distrahati. B in
marg. : Quadruplex digestio prius habetur cap. primo huius tractatus.

p. 61:
3. A in marg. : Dupliciter est homo in ecclesia. Ib.: Dupliciter dicitur
non pars in ecclesia. Nota quomodo presciti sunt in ecclesia. II. B:
dirigit. 12. A in marg.: Alia subdivisio. 22. A in marg.: Contra avari-
ciam cleri et aliorum (above i36d without mark of rcferonce). 29. A in
marg. : Aristoteles. B in marg. : Quare aqua tepida cicius congelatur quam
frigida secundum Aristotelem.
29. MeTEo>po).oywu")V A. 12 vide Arist. ex rec. Bekkeri vol. t,
pag. 348: auu.pdXXETai 3' su icpig rr^v TayjJTTjTa r?js irf]^eo)S xal
to itp&Teit)'Ep|i.dvO'ac to oooip. tJ-ottov '{lo^etai.

p. 62:
i5. AB in marg. : Avari, lubrici, cupidi. Correlarium. 18. A in marg. :
Nota. 23. In codd.: Ita deest. cf. Hussi Opp.I, i99h . 24. A in marg. : Nola.

p. 63:
5. B in marg. : Ecce qui non sunt membra ecclesie. 7. B: spei
deest. 8. B: sapiencie in caritate. 16. AB in marg. : Augustinus.
22. A in marg.: Nota fidem predestinatorum et prescitorum. 24. A B in
marg. : Damascenus. 25. Codd.: vel informem.
24. Cf. De fide orthodoxa lib. IV, cap. XI.

p. 64:
1. B in marg. : Quis credit in filium. II. B: Unde deest. A B in
marg.: Augustinus. A in marg. : De salvandis et dampnandis prescitis et
predestinatis. 17. B: Jo. VIII. (o. B in marg. : Nota quare columbe
descensus signat spiritum sanctum. ib: Vidi spiritum sanctum descen-
dentem sicut columbam. Nota proprietaies columbe. 26. A in marg. :
Augustinus.
5. Aug. In Johannis Evang. cap. 3, tractat XII. Opera tom III,
p. II, pag. 38q. 12. Joh. I. 32, cf. Aug. Opp. tom. III, p. II, pag. 33o.
```
