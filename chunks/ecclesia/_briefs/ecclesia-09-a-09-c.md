# Translation brief: ecclesia 09-a–09-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-09-a.md chunks/ecclesia/wyc-ecclesia-09-b.md chunks/ecclesia/wyc-ecclesia-09-c.md` once and fix what it reports.
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

## Glossary (the 144 rows these chunks use; the full file is GLOSSARY.md)

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
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |

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
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| famosior | best-known [sense] | Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 09-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-09-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-09-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "182.7–186.31"
divisions: "cap. 9 (heading 'CAP. IX.' at 182.6); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1149 words; 1039 unanimous or majority-real; 91 settled by vote (R2 55, R3a 31, R5a 3, R6a 2); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n219–n223 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 9, part 1: [TITLE]

## ¶1 · 182.7–182.10

> [p. 182] Pri- Sed contra dicta arguitur sic: Videtur enim primo quod equivocatur in nomine privilegii, cum communitas non vocat privilegium nisi excellenciam quam habet una persona super aliam quoad mundum.

[ENGLISH]

## ¶2 · 182.11–183.33

> [p. 182] Hic dicitur quod illud assumptum indicat sic vocantes terrena diligere, et despicere vel odire celestia, quia voluntas trahit intellectum ad affectuosius cogitandum et nominandum rem cui mais infigitur: ad quem sensum dicitur Joh. III°, 31: Qui de terra est de terra loquitur. Et hinc apostoli et sancti priores reputarunt ista terrena ut stercora, sicut patet in dictis et factis eorum et exprimit Apostolus Philipp. III° cap. Ergo quod communitas sic loquitur et attendit, non nisi accusat ipsam perversam a Deo et verificat dictum Evangeliste Ia Johannis V°, 19: Totus mundus in maligno positus est et dictum Christi Matthei XII°, 34: Ex habundancia cordis os loquitur. Ideo debemus attendere qualiter secundum regulas fidei est loquendum: cum autem privilegium sonat in maioritatem prerogativam vel preeminenciam creature, manifestum est quod partes ecclesie tam militantis quam triumphantis sunt privilegiate a Deo. Ideo dicunt sancti doctores communiter quod Christus et mater sua habuerunt singularia privilegia super alios, et ita de apostolis et aliis beatis, quilibet habet dispariter [p. 183] donum suum, ut manifestavit Apostolus. Iª Cor. XII°, 4, dicens quod divisiones graciarum sunt, Notet ergo fidelis racionem privilegii et videbit quod principaliter sit in donis spiritualibus a Deo appropriate collatis, unde, si argumentum factum moveret, diceret consequenter quod nulla est lex, possessio vel dominium nisi de bonis temporalibus, quia de illis principaliter vel precise loquitur communitas, in tantumquod statim audito de bonis, applicant ad mundi divicias; et locuto de episcopatu, rectoria vel alio nomine prelacie, statim applicant ad dotem temporalem dimissa consideracione de officio; et ita de aliis. Non sic autem in primitiva ecclesia vel scriptura sacra; ideo postponendo viciosam consuetudinem debemus loqui conformiter sanctis doctoribus. Non enim reperi rem in scriptura sacra vocatam sub nomine privilegii, sed doctores et usus ecclesie vocant eam sic communiter, ut patet de sancto Evangelista, de sancto Petro et Romana ecclesia. Et patet quod innitendo pure modo loquendi vulgari totus conventus Christi non foret privilegiatus sub aliquo gradu, nisi forte fingatur quod Scarioth fuit privilegiatus in hoc quod Deus permisit eum portare loculos, et sic introductum esset privilegium in ecclesiam cum superbia ex contencione circa maioritatem et secularem obedienciam quam Christus nitebatur in suis destruere. Non ergo concedendum est quod solus dominus temporalis privilegiavit, edificavit vel dotavit ecclesiam, cum ecclesia canit quod Christus privilegio amoris Johannem dilexit apostolum; et idem est de quolibet singulari dono Dei, ut patet ex descripcione privilegii. Unde non expressius posset quis ostendere se iuste perditurum privilegium per abusum quam negando Christi privilegia vel preponderando privilegia terrena.

[ENGLISH]

## ¶3 · 184.1–186.13

> [p. 184] Secundo videtur quod non licet clero insistere circa privilegia terrena cuiusmodi videntur esse exempciones, prerogative, proprietates et seculares dominaciones, cum videntur repugnare privilegiis Christi que non licet amittere. are Hic dicitur, primo quantum ad exempciones quod, licet videantur esse male de genere, tamen contingit subditum bene uti illis sicut et aliis actibus malis de genere; est enim contra regulas ecclesie triumphantis quod quis sit exemptus ne superior illuminet inferiorem, et ita contra regulas nature est quod subditus sit exemptus, ne ducatur vel corrigatur per superiorem in casu quo deviet vel delinquat. Unde videtur idem inpetrare oppositum et luciferine querere licenciam ad peccandum; diaboli enim exempti sunt a tali regimine et (ut ego credo) a privilegiacione, quia nulla excellencia quam habent cedit dampnatis ad bonum utile, sed econtra beati sunt summe privilegiati, in tantum quod nullum privilegium vie valet homini, nisi de quanto preparat ad querendum privilegium regni. Quia tamen contingit prepositos ecclesie esse ceciores ducendis vel inniti in visitacione fastui vel questui plus quam correccioni, ideo expedit per accidens a talibus temporalis exempcio. Non autem debet talis esse perpetua nisi cognito quod perpetuo erit prepositus deses, inscius vel avarus, quia aliter (ut recitat Lincolniensis) hoc inconveniens sequeretur quod quantumlibet bonus pastor videns exemptum strangulare oves, pro quibus reddet racionem in die iudicii, non audebit propter exempcionem pape exagitare vel exterrere lupos mordentes tam nequiter oves suas. Hoc autem non potest dici privilegium sed rete diabolicum. Unde privilegium foret eximi a iurisdiccione talis pape, si fuerit qui [p. 185] propter pecuniam et casum particularem, in minori parte eciam ob defectum sui contingentem, statuerit exempcionem talem ut legem perpetuam. Nam diabolus et membra sua seducendo populum ab observancia legis Christi videntur inducere exempcionem huiusmodi, ne inferior fruatur suffragio sui prepositi, ut innuit Augustinus libro secundo De Ordine. Et quantum ad alia insignia perquisita de portando mitram, crucem et baculum ac ordinando clericos extensius vel striccius, cum aliis vocatis privilegiis istis similibus, cum ut plurimum sapiunt fastum et non commodum, sunt sepe non privilegia sed diabolica sagena quibus pisces natantes in mari huius seculi capiuntur; et sic dicendum videtur de privilegiis terrenis seculariter impetratis. Unde Augustinus in libro De Agone Christiano, cap. IV: Gaudet piscis quando hamum non videns escam devorat, sed piscator cum eum ceperit, torquentur eius viscera primo, deinde ab omni leticia sua per ipsam escam de qua letatus est trahitur ad consumacionem. Sic sunt omnes qui de bonis temporalibus beatos se putant unde bonis nichil nocet ablacio temporalium, cum ipsa non diligunt. Unde inter omnes cautelas diaboli mundana preeminencia est prima sagena diaboli; de illa enim primo temptavit Christum. Nam Matthei IV°, 8, 9, dicitur quod ostendit sibi omnia regna mundi dicens: Hec omnia tibi dabo, si cadens adoraveris me. Et revera propter minus privilegium adoramus sepius membra sua, cum tamen profitemur in baptismo quod abrenunciamus sathane et omnibus pompis eius. Talis itaque finalis preponderancia secularis privilegii est signum infallibile membri diaboli, et sic [p. 186] videtur mihi quod contendentes superbe circa talia privilegia nisi redeant humiliter ad unitatem subiecti invicem, non sunt de sancta matre ecclesia, dicente decreto Pelagii pape XXIV, q. I. Pudenda: Ecclesia, inquit, una est, ut patet in canticis, et illa est que fide formata per orbem diffunditur; quod beati Augustini testimonio comprobemus. Audite quid in quodam opere suo preclarissimus doctor dicat ecclesie Ait enim quod, cum nullo modo recte potest dici ecclesia in qua scisma est, restat ut, quoniam nulla esse ecclesia non potest, ea sit quam in sedis apostolice per successiones episcoporum radice constitutam nullorum hominum malicia eciamsi nota excludi non possit.

[ENGLISH]

## ¶4 · 186.14–186.31

> [p. 186] Ex isto notandum, primo quomodo iste papa allegat venerabiliter Augustinum: quod divisi a Christo per invidiam extrudentem caritatem non sunt membra ecclesie. Patet secundo quod, si collegium Romanum sit sic divisum scismate, tunc ipsum non est caput vel pars ecclesie, quia deficit unio apostolica. Unde dicit quod, si talis episcopus consecrat alium, non consecracio sed execracio debet dici. Et tercio notari potest quomodo crescente superbia et cupiditate primatus de loco ecclesie, potest fieri synagoga sathane, cum nemo potest esse Christi vel Petri vicarius, nisi sequatur eos in moribus, ut patet XLª dictinccione: Non est facile. Et patet quod licet clero insistere circa privilegia terrena, de quanto promovent ad eterna; quod oportet exemplo sanctorum et fide scripture pensari, nullomodo amittendo privilegia que Christus dedit propter aliquod bonum mundi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 182.7: Objection: Privilege is generally understood of worldly things.
- 182.14: If so, it is the fault of the people who use the word.
- 183.5: It might as well be said that law and possession apply only to earthly goods.
- 183.12: Such is not the language of the primitive Church.
- 184.1: The Church ought not to insist on earthly privileges such as exemptions and endowments.
- 184.6: Exemptions are bad in kind, although they may sometimes serve a good purpose.
- 184.27: Good prelates ought not to be hampered by them.
- 185.9: Privileges of wearing mitre etc. are often a snare of the devil.
- 186.15: The Roman college may be the synagogue of Satan and not the head of the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 182: *CAP. IX.* [HEAD]
  - 182: *quem* [R3]
  - 182: *III°* [R4]
  - 182: *III°* [R4]
  - 183: *donum* (154a folio mark, A margin letter) [R3]
  - 183: *Iª* [R3]
  - 183: *dominium* (and is the English side-note) [R4]
  - 183: *introductum* [R3]
  - 184: *Christi* [R3]
  - 184: *illis* [R4]
  - 184: *aliis* [NW]
  - 184: *exemptus* (print: quis sit exemptus, ne superior; missing from main scan) [INS?]
  - 185: *Christi* (5 is the line number) [R3]
  - 186: *Christo* (15 is the line number) [R4]
  - 186: *Christi* [R3]
  - 186: *XLª* [R4]
  - 184: *cum* (clear m) [R3]
  - 185: *propter* (154b folio mark glued) [THIN]
  - 186: *talia* (154c folio mark glued) [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 182:
1. B: religione quoque. in codd. : est hec; corr. c tcxtu Aug.
6. Cap. IX; A: Tit. vacat in A; solum in marg. ib. Prima obicccio. A:
sic deest: B: primo deest. it. A in marg.: Responsio. 19. B:
attcndat. ii. A: habuocia. 3i. B: quibus habet.

p. 183:
5. A. in niarg.: Privilcgium dcbet essc in donis spiritualibus. (Abovc
1 5-i without mark of refercnce.) it. AA,: temporalium. 19. B:
quod dcest. 20. 22. B : sub aliquo — privilcgiatus decst. 26. B:
suis defervere. 29. A in marg. : Conclusio.

p. 184:
1. A in marg. : Secunda obieccio. 6. A in marg : Responsio:
Nota contra exempciones continuc infra. 22.24. B : P'us — cxempcio:
deest. 2(>. A in marg. : Lincolniensis. 3i. B: potest decst.

p. 185:
i5. A in marg. : Augustinus. 16. de agone; A hab. rasuram.
18. A, corr. vult. : torquet. 21. A in marg. : Mundana preemincncia
est sagena diaboli. 32. A A, : Mcmbrum diaboli.
7. cap. XVIII (?) vid. Opp. I, ?2q seqq. 16. Opp. VI, 245.

p. 186:
2. A in marg. : Conclusio. 33. A in marg. : Tercia obieccio.
?. Dec. sec. pars. Causa XXIV, q. I, c. XXXIII, a few
words having been altered.
```

---

## Chunk 09-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-09-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-09-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "186.32–190.16"
divisions: "cap. 9 (heading 'CAP. IX.' at 182.6); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "795 words; 710 unanimous or majority-real; 62 settled by vote (DEL 2, R2 35, R3a 18, R5a 6, R6a 1); 23 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n223–n227 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 9, part 2: [TITLE]

## ¶1 · 186.32–187.15

> [p. 186] Sed tercio obicitur, cum privilegia quibus Christus dotavit ecclesiam sunt perfecciora quam terrena privilegia [p. 187] succedencia, sicut et status vivencium secundum illa privilegia est statu moderno perfeccior atque ad servandum facilior, videtur quod non licuit a privilegiis illis et statu recedere; nam nulli persone licet magis bonum sibi in eleccione postponere: ecclesia, sponsa Christi est persona, cum sit virgo ex cap. VI°, ergo non licet sibi privilegia Christi et statum evangelice paupertatis relinquere. Confirmatur primo per decretum De Consecracione, dist. Vª, Non mediocriter, ubi dicitur quod graviter peccant qui eligunt minus bonum sibi maiori bono postposito. Confirmatur secundo ex dictis libro V°, cap., ubi docetur quod oportet viantem semper meliorando procedere. Et tercio confirmatur ex hoc quod consilia Christi sunt perpetua et sponse sue indispensabilia.

[ENGLISH]

## ¶2 · 187.16–188.13

> [p. 187] Hic videtur mihi quod unum concluditur ex assumpto necessario, cum omnis christianus debet sequi Christum in moribus quantum sufficit, unde videtur mihi quod beatus Silvester potest dici ex pietate suscepisse elemosinas Cesaris corporales ad exonerandum eum, ad excitandum eius devocionem et procurandum tenerius pro fidelibus quam faceret populus laycalis; quod, cum stat cum paupertate evangelica, patet quod clerus non debet exinde inniti proprietati vel fastui, sed ad sui tedium secundum partes plus abiectas ministrare pauperibus de collatis elemosinis. Unde tales elemosine non possunt donari in perpetuam elemosinam quomodocunque clerus vixerit, sed sub condicione saltem tacita quod clerus sit vere sequax apostolorum in vita et opere. Et ita credo quod oportet ut reputet sibi omne tediosum ministrare pauperibus et fore gaudiosum, dando operam contemplacioni [p. 188] et predicacioni, quod fideles layci accipiant illud onus (ut alias exemplificavi de Augustino et aliis sanctis). Unde quia fragilitas humana prona est ad relinquendum primam caritatem de elemosinis, superbiendo, se ipsam nimis laute pascendo et pastoris officium relinquendo, ideo apostoli et sancciores ecclesie talia reliquerunt. Unde mirum est si collacio rei temporalis sit clero privilegium; ymmo apostolis petentibus illam a Christo audivisset responsum superius: Nescitis quod petatis. Nonne docet experiencia quod dotacio talis subicit dotatos mundane sollicitudini, servicio et exaccioni, et per consequens distrahit ab amore Christi et ministerio sacerdotali?

[ENGLISH]

## ¶3 · 188.14–190.12

> [p. 188] Quomodo ergo non foret privilegium ab incita- mento huiusmodi liberari, unde decretum recitat XIª, q. Iª, ex epistola beati Petri ad Clementem scriptum sub hac forma: Te quidem oportet irreprehensibiliter vivere et summo studio niti, ut omnes vite huius occupaciones abicias, ne fideiussor existas nec advocatus licium fias neve in ulla alia occupacione prorsus inveniaris mundani negocii occasione perplexus. Neque enim iudicem neque cognitorem secularium negociorum hodie te vult ordinare Christus, ne prefocatus presentibus hominum curis non possis verbo Dei vacare. Hec vero opera que tibi minime congruere dicimus exibeant sibi invicem vacantes laici, et te nemo occupet ab hiis studiis per que salus hominibus datur. Quomodo ergo licet nobis ab ista regula apostolica recedere quibus relictum [p. 189] est a Deo ecclesiam gentilium ad perfectam legem Christi convertere? Non enim cadit auctoritas vel racio dispensandi; unde verisimile est quod radix tocius perturbacionis in seculo est cleri declinacio a lege Christi ad vitam et tradiciones civiles. Christus autem semper reliquit in una parte ecclesie sue vel alia aliquos fideles qui mundum deserant, et in illis forte abiectis primatibus stat fides et continuacio sancte matris ecclesie. Et patet quod sepe non est privilegium vocata dotacio cleri in temporalibus, et per consequens auferendo a clero ista non oportet quod auferantur ab eo privilegia, sed pocius amoto prohibente sit ecclesia apostolica restituta ad vera privilegia primitiva; quod ego credo dominos temporales in casu debere facere sub pena dampnacionis gravissime. Numquid credimus esse magnum privilegium episcopo vel abbati quod habeant furcas et puteum, in quibus dampnati regulariter trucidentur, et sic de carcere, de aliis mundanis privilegiis sive insigniis? Ymmo non foret privilegium prelato quod haberet efficaciam, ut quicquid tetigerit statim convertatur in aurum, quia tunc periret aer deferens inspirandus, periret vescibile et tegumentum corpori temperatum. Unde in detestacionem huius philargirie legitur beatum Evangelistam convertisse frondes silvestres in aurum et litoria saxa in gemmas. Iste sanctus statim potuit fuisse aput mundum ditissimus et secundum gloriam mundanam preclarissimus, dominatissimus et famosissimus, si non repugnasset perfeccioni apostolice et privilegio concesso a Christo; aliter enim peccasset graviter omittendo. Nam habens in potestate tam [p. 190] faciliter proficiendi sibi et aliis, glorificando ecclesiam plus quam Cesar, non haberet excusacionem de negligenti desidia, sed scitur demonstracione certissima quod omne spirituale privilegium superat quodcunque corporale privilegium in infinitum, et sic non est privilegium clerum stipari seculari milicia, vesci in auro, uti fibula vel habere secundum mundanam gloriam splendencia ornamenta. Omnia enim ista gentes exquirunt (ut patet I° Machabeorum IX° et XI°), Christus autem et eius discipuli cum habere possent facillime hec omnia, si non repugnarent sue perfeccioni, quia repugnant, ideo omnia ista penitus respuerunt.

[ENGLISH]

## ¶4 · 190.13–190.16

> [p. 190] Sed quarto arguitur sequi ex dictis: quod nullum sit corporale privilegium, ymmo quod nedum licet secularibus sed debent sub pena excommunicacionis auferre bona a clericis quibus putantes se benefacere erraverunt.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 187.1: The Church ought not to have left the state (of poverty) appointed by Christ.
- 187.18: Silvester may have acted from pious motives.
- 187.29: The clergy should gladly leave laymen to minister to the poor
- 188.1: and devote themselves to preaching.
- 189.9: The removal of endowment may be a restoration of primitive privilege,
- 189.17: worth much more, than the right of gallows etc.
- 189.25: The apostles were poor by choice.
- 190.13: It is said that, if this be true, all temporal privileges are abolished.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 187: *privilegia* [R4]
  - 187: *Vª* [R4]
  - 187: *tenerius* (tene-/rius; main token holds the whole word (154d folio mark glued)) [R4]
  - 187: *Et* [R3]
  - 188: *et* (print begins p.188: placioni et predicacioni; main donari is spurious) [R4]
  - 188: *predicacioni* [R3]
  - 188: *quod* [R3]
  - 188: *incita-* (first half of incita-/mento; F is the margin letter) [NW]
  - 188: *XIª* (15 is the line number) [R3]
  - 188: *Iª* [R3]
  - 189: *est* (154d folio mark, F margin letter) [R3]
  - 189: *Christi* [R3]
  - 190: *faciliter* [THIN]
  - 190: *proficiendi* [THIN]
  - 190: *I°* (cap-height I, not old-style 1) [R3]
  - 190: *Christus* [R3]
  - 190: *ymmo* [R4]
  - 186: *privilegia* (pri- here, 154d vilegia on next page; main token holds whole word) [THIN]
  - 187: *illa* [R3]
  - 188: *fideles* [THIN]
  - 188: *illud* [THIN]
  - 190: *et* [THIN]
  - 190: *ecclesiam* (155a folio mark follows) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 186:
2. A in marg. : Conclusio. 33. A in marg. : Tercia obieccio.
?. Dec. sec. pars. Causa XXIV, q. I, c. XXXIII, a few
words having been altered.

p. 187:
16. A in marg.: Rcsponsio. A, : vcrum ; in codd. A. 13: um (verum?)
9. Decr. III, pars De Cons. dist. V, c. XXIV.: Non mediocriter
crrat qui magno bono prefert mediocre bonum.

p. 188:
9. A A,: audivissent. 16. Epistola Petri. Non est epistola beati
Petri, sed Clementis ad Jacobum. A in marg. : Nota decretum super hoc
quod clerus non debet se implicare mundo. :o. In codd.: ne vcl;
correxi e dccret. I. c. A in marg. (above i54*without mark of reference):
Nec omnia infra posita sunt pro paupertate que est optimum privilegium.
23. A in marg. : Zname, id est, noscimus. 28. A in marg. : De abla-
cione temporalium et cleri paupertatc.
16. Cap. XXIX. De secularibus negociis episcopus cognoscere
non debet.

p. 189:
6. A in marg. : Conclusio. 7. A, corrig. vult. : dcscrunt. 12. A
A, : amoto: decst. 17. B: Quod: e deest. 23. A,: vcstimcntum.
26. B in margine man. alt. : Evangelista frondem convcrtit in aurum.
2S. 29. A A,: ct secundum — dominatissimus : deest. 3o. A: re-
pnngnasset.

p. 190:
5. A A,: in finitum. 6. B: seculari deest: vcsci; frrte legendnm
vestiri |= vesli(ri)]. 10. B: haberc possint. n. A, corr.: sed
quia; B: repugnat. i3. A in marg. : Quarla obieccio. iS. A
in marg. : Ablacio lcmporalium quomodo cst limitanda. 21. A in
marg. : Responsio.
```

---

## Chunk 09-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-09-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-09-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "190.17–194.25"
divisions: "cap. 9 (heading 'CAP. IX.' at 182.6); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "958 words; 855 unanimous or majority-real; 81 settled by vote (DEL 3, R2 50, R3a 21, R5a 6, R6a 1); 22 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n227–n231 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 9, part 3: [TITLE]

## ¶1 · 190.17–194.12

> [p. 190] Hic dicitur quod prima pars est falsa, sed secunda est mihi vera in casu; nam cum omne privilegium sit ad commodum privilegiati, patet quod multis dominis temporalibus et aliis assunt terrena privilegia ad exercicium virtutis. Hoc autem contingit communius laicis quam clericis, quia officium dispensandi temporalia et dominanter cohercendi subiectos est eis pertinencius, et clerici declinantes ad mundum communiter peccant gravius. Conceditur tamen quod ministracio temporalium, ne clerus dispergatur ad inhonestis mediis mendicandum, foret in casu clero in privilegium, sicut contigit III Regum XVII° quod Helias privilegialitcr fuit pastus per corvum. Et breviter ministracio temporalium non est clero in privilegium, nisi de quanto promovet ad sequendum Christum in moribus et impetrandum privilegium [p. 191] amoris sui; quod contigit, cum Christus accepit elemosinas a laicis et sanctis feminis. Et secundum istam condicionem dotata fuit ecclesia non ad tardandum vel ad retrahendum eam a perfeccione primeva. Unde excommunicatissime peccant sive clerici sive laici qui hoc privilegium antiquum ecclesie scienter auferunt vel minuunt, et hinc XXV, q. II, sic loquitur Leo papa: Privilegia ecclesiarum et monasteriorum sanctorum patrum auctoritate instituta nulla possunt improbitate convelli, nulla novitate mutari. In quo opere auxiliante Christo fideliter exequendo necesse est sedis Romane pontifices perseverantem exhibere famulatum. Dispensacio enim nobis credita est et ad nostrum reatum tendit, si paternarum regule sanccionum nobis consencientibus vel negligentibus violentur. Talia sunt multa decreta: quod non licet antiquioribus privilegiis novis subsequentibus derogare. Cum ergo antiquissima et validissima privilegia, instituta a Christo, steterunt in paupertate altissima, sequitur quod non licet cuiquam privilegium illud subtrahere. Cum ergo privilegium illud stat in habendo cuncta exproprietarie in communi, sic quod sibi repugnat dominacio civilis et conversacio secularis, videtur quod hoc non licuit sine gravi periculo introducere in clerum. Unde XXVª q. I, canon sic loquitur: Que ad perpetuam generaliter sunt ordinata utilitatem, nulla commutacione varientur, nec ad privatum commodum trahantur que ad bonum sunt commune prefixa. Ex istis colligitur, cum nec dominus secularis debuit nec potuit dare clero in privilegium dominacionem [p. 192] secularem, stante illo ordine, nec licuit clero illam accipere, patet quod error, si ex ignorancia in illud processerit, debet utrimque celeriter emendari. Patet prima pars ex hoc quod non licet deteriorare proximum, auferendo ab eo privilegium a Deo datum, ad perficiendum in suis limitibus precipuis tantum statum, sed necessario foret deterioracio, quia deieccio status cleri ad laycos, habere dominacionem huiusmodi. Ideo non licuit seculari hoc facere. Unde tercio decretalium, Nec clerici vel monachi, capitulo Relatum, precipit papa quod monachi incorrigibiles vivendo seculariter alios corrumpentes eiciantur aliis religiose viventibus introductis, ubi tamquam per se manifestum supponitur quod secularis conversacio sit clericali inferior; nec dubium quin repugnat statui et perfeccioni cleri quod sic per affeccionem et occupacionem temporalium degradetur; ideo propter repugnanciam non potest fieri talis dotacio stante ordine. Non enim est privilegium peiorare. for Et ex eodem patet quod non licet clero a perfeccione primitiva deficere, sicut non licet laico sponsam Christi sic inficere. Si enim non licet laico auferre suas elemosinas que sunt bona abiectissima, multo minus liceret auferre elemosinas a Deo institutas que sunt bona et privilegia Dei potissima. Quomodo ergo liceret seculari ordinacionem Dei inficiendo corrigere cui non licet iuxta falsigrafos suam culpam quam commisit ex ignorancia emendare? Numquid tam affectata ignorancia excusat dominum secularem: Si enim secularis cui minus repugnat mundialitas ex tali inclinacione ad seculum, non obstante quod putat in hoc prestare Deo obsequium, reddit eum [p. 193] dampnabilem, quanto magis necessitando personam cleri cui plus repugnat conversacio secularis? Revera si talis ignorancia omnino excusat, per idem excusaret quemlibet viciosum; nam, ut patet primo Ethicorum, sicut omnis homo appetit naturaliter esse felix, sic appetit media que credit ducere ad hunc finem, ut voluptuosus ponit felicitatem in cibariis delicatis, luxuriosus in actibus venereis, avarus in mundi diviciis, superbus in mundanis honoribus, et sic de aliis in quibus ignorans amplius delectatur. Sed quis diceret ignoranciam talem simpliciter excusare? Sic ergo posito quod Cesar ex ignorancia crediderit se prestare Deo obsequium in dando clero Christi mundi gloriam, sicut est accusabilis ex eleccione fatua et amore prepostero affectando talia sibi ipsi, sic est plus accusabilis retardando proditorie et cum mundano toxico precipuos milites exercitus christiani. Aliter enim foret elemosina privilegiare clerum eciam religiosum, ut sit voluptuosissime, delectabilissime et splendidissime cibatus, uxoratus et in omni mundi gloria pre omnibus secularibus predotatus. Sed quid privilegio tali insanius? Unde sola fabrica, cum super fallaciam equivocacionis privilegii decipit totum mundum, quia cum dominus temporalis potuit meritorie concedere hec privilegia, sicut clerus ea accipere, et potuit utrimque esse dampnabilis fastus et ignorancia: ideo neutram partem assero, nec quod succedentes abutuntur privilegio, sed veritatem condicionalem ut fidem christianam defendendo relinquens prepositis veritatem de inesse ex operibus iudicandam. Quinto arguitur per hoc quod iuxta sepe dicta paupertas evangelica et omnino spiritualia insignia que Christus concessit sue ecclesie stant cum cesarea [p. 194] dotacione, et ex hinc aliquod bonum ecclesie evenietis (ut patet in proximo argumento): ergo melius est quod ecclesia sic dotetur, et per consequens, Cesar dotavit ecclesiam supra Christum. Maior videtur ex hoc quod beatus Silvester et alii sancti episcopi et domini seculares non approbassent dotacionem huiusmodi, si fuisset ad deterioracionem ecclesie, sed curia Romana instetisset olim pro privilegiis antiquis ecclesie et propter facilitatem fuissent olim restituta, cum tam dotantes quam dotati statim annuerent expropriacioni, dato quod esset meritoria.

[ENGLISH]

## ¶2 · 194.13–194.25

> [p. 194] Hic dicitur negando primam consequenciam, nisi forte assumptum sit impossibile. Nam videtur multis quod laureola martirii qua milites Christi plus strenui decertarunt in floribus ecclesie, convertendo tam expedite tantum populum, non stetissent simul subiecto et tempore cum dotacione cesarea, nec tam abiecta paupertas, calcato mundo, submisso clero Christi consilio, voluntarie paciendo, nec tanta aspiracio ad bona patrie contempta confidencia in bonis fortune vel bonis nature, et per consequens non fuisset tanta status securitas sequendo Christum per compendium arte vite que ducit ad celum. Nam omnia ista quatuor cum suis correlativis videntur esse dotacioni terrene contraria.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 190.27: But we allow such privileges as help the clergy in their duties.
- 191.5: It is wrong to take away ancient privileges;
- 191.17: and the oldest and greatest privilege is poverty granted by Christ.
- 192.1: If this wrong has been committed (by endowment) it should be set right.
- 192.20: It is wrong for the clergy to receive endowments as for the laity to give them.
- 193.1: Ignorance is not always an excuse.
- 193.31: It is argued that endowment is consistent
- 194.2: with evangelical poverty; and, since it brings some good, must be a gain to the Church.
- 194.13: The first assumption is doubtful,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 190: *assunt* [NW]
  - 190: *Et* [R3]
  - 191: *amoris* (H 155ª is folio mark and margin letter) [R3]
  - 191: *improbitate* (10 is the line number) [R4]
  - 192: *secularem* [THIN]
  - 192: *stante* [THIN]
  - 192: *ignorancia* [R3]
  - 192: *capitulo* (capi-/tulo hyphenated; main token holds whole word) [R3]
  - 192: *Christi* [R3]
  - 193: *dampnabilem* (K 155ᶜ is margin letter and folio mark) [R3]
  - 194: *dotacione* [R3]
  - 194: *∅* ('as' is the English side-note (as-/sumption); box word Hic already present) [INS?]
  - 191: *dominacionem* (domina- here, cionem at top of p.192; main token holds whole word) [THIN]
  - 192: *ordine* [THIN]
  - 192: *accipere* [THIN]
  - 192: *patet* [THIN]
  - 192: *quod* [THIN]
  - 192: *Deo* [THIN]
  - 192: *obsequium* [THIN]
  - 193: *cesarea* [THIN]
  - 194: *ex* [THIN]
  - 192: *∅* (second half of capi-tulo; neighbour 74 already capitulo) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 190:
5. A A,: in finitum. 6. B: seculari deest: vcsci; frrte legendnm
vestiri |= vesli(ri)]. 10. B: haberc possint. n. A, corr.: sed
quia; B: repugnat. i3. A in marg. : Quarla obieccio. iS. A
in marg. : Ablacio lcmporalium quomodo cst limitanda. 21. A in
marg. : Responsio.

p. 191:
q. A: sanctorum paternum. 2?. A: cunta; A, cnrr. in: cuncta.
3o. A in marg. : Non licuit clcro reciperc dominacionem ncc licuit dorainis
7. Dec. II. p. caus. XXV, q. II, c. II. a& Dec. II. p.
caus. XXV, q. I, c. III.

p. 192:
2. A in marg.: Conclusio. 6. B: in suis militibas. 26. A:
10. Decr. Greg. IX, lit. III, tit. L, cap. VII. mutatis aliquot
verbis.

p. 193:
16. 17. In codd. mundana toxica. 22. A in marg. : Protcstacio:
lioc verbum extinctum est. 3i. A in marg. : (jninta obieccio.
4. Cap. II, III.

p. 194:
12. A in marg. : Rcsponsio. 14; A in marg. : Nota quattior.
iS. A,: calcata. 24. cprrel'" in codd. 33. A in marg. :
Conclusio.
```
