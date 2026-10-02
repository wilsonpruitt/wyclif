# Translation brief: ecclesia 04-f–05-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-04-f.md chunks/ecclesia/wyc-ecclesia-05-a.md chunks/ecclesia/wyc-ecclesia-05-b.md` once and fix what it reports.
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
| pars peregrinans; peregrinari | the pilgrim part; to be a pilgrim | Augustine's *peregrinatio* (Ench. 56). Pilot. |
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |

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
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
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
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). Ruled 2026-10-02 (*Eccl.* 72.24). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| zizania | cockle | Douay–Rheims (Matt. 13:25). Ruled 2026-09-28. |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 04-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-04-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-04-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "88.31–92.5"
divisions: "cap. 4 (heading 'CAP. IV.' at 69.4); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "766 words; 705 unanimous or majority-real; 46 settled by vote (R2 23, R3a 17, R5a 5, R6a 1); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n125–n129 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 4, part 6: [TITLE]

## ¶1 · 88.31–90.8

> [p. 88] Unde glosa obicit in contrarium per duo capitula, videlicet XXIIIª, q. IV, cap. Forte et cap. Hec [p. 89] autem vita, ubi vere dicitur quod quamdiu sumus in hoc mundo, non deficiet nobis ruga venialis. Et solvit tripliciter: primo quod ecclesia quandoque large sumitur, ut granum et paleam complectatur, ut in allegatis capitulis, quandoque stricte pro puro grano, ut XXXIIª q. IV: Recurrat, ubi sic scribitur (ut supra tetigi): Itaque, inquit Augustinus, sive intus versari videantur sive aperte foris sint, quod caro estcaro est, quod palea est palea est. Et semper ab illius ecclesie que sine macula est vel ruga unitate decisus. Vult iste sanctus dicere (ut patet ex dictis) quod impossibile est prescitum esse membrum sancte matris ecclesie vel predestinatum a maternitate illa deficere, quomodocunque secundum presentem iusticium varientur. Secunda responsio glose est quod aliud est esse de ecclesia et aliud esse in ecclesia, ut patet XXIIIª q. IV: Vasis ire et supra exposui. Tercia responsio distinguit de quadruplici habitudine viantis ad sanctam matrem ecclesiam. Quidam autem sunt in ecclesia nomine et re ut obedientes catholici, quidam nec re nec nomine ut pagani, quidam nomine tantum ut presciti ypocrite, et quidam re licet videantur nomine esse foris ut predestinati, quos satrape videntur in facie ecclesie condempnare. Ecce decretorum concordia sentencie supradicte. Unde videtur nimis blasphema heresis papam vel collegium suum credere quod in quantum eliguntur in illo officio tenent primatum tocius ecclesie. Oportet enim quod sint filii imitacionis in moribus parentum quorum [p. 90] pretendunt se gerere vicariam potestatem. Aliterenimp sunt de generacione pessima meretricis diaboli. Generacio enim sunt Christi, neque constat ex sanguinibus ut in propagacione naturali neque ex voluntate carnis ut in electis nude ex affeccione carnali neque in electis pro pompa seculi que nascitur ex voluntate viri, sed ex Deo nati sunt tamquam filii imitacionis per graciam adoptantem et tunc ex condicione generis patrizabunt.

[ENGLISH]

## ¶2 · 90.9–92.5

> [p. 90] Tercio dicitur ad obiectum de noticia matris nostre quod satis cognoscitur a fideli: est enim dare noticiam distinctam et confusam et utraque potest subdividi, quoad personam vel circumstanciam, quoad sensum vel intellectum, quoad fidem vel racionem. Si cenim cognosco caput ecclesie et tamen ipso ostenso michi nude in specie humana nescirem ipsum ab alio discernere. not Unde, cum fide ambulamus et vivimus, consonum est quod nos quasi modo geniti infantes confuse in velamento fidei habeamus noticiam matris nostre: sic enim nec prescitos reprehendimus nec predestinatos extollimus viciose, sed correspondenter ad noticiam tam membra matris nostre quam infideles sibi et nobis inimicos diligimus; illos autem quos videmus vivere secundum legem Dei reputamus esse filios regni, et sic de aliis habemus maiorem evidenciam, de aliis minorem. De illis tamen nunc credimus quod sunt membra matris nostre vel meretricis opposite plus quam fide. Unde, quesito a me de quacunque persona vel populo conversante nobiscum utrum sit membrum matris nostre, sic quod videndo ipsum videamus parcialiter matrem nostram, dico quod ego ignoro sed reputo vel suppono ex modo conversandi sic vel sic, nec est inconveniens sed consonum statui vie quod ignoremus [p. 91] et nesciamus in particulari illud quod cognoscimus in communi; et illa scimus demonstracione intellectus limitati per fidem quod hec est mater nostra, licet demonstracio sensualis hoc non certificet. Unde neminem conversantem nobiscum debemus absolute contempnere sed vicia, quia ignoramus si in hoc despicimus matrem nostram et omnino sponsum ecclesie. Et ita certi sumus quod quidquid bene agimus secundum legem sponsi, in hoc honoramus et proficimus matri nostre. Nec est difficile scire voluntatem sponsi, quia ex fide cognoscimus omne factum naturaliter vel meritorie fieri secundum beneplacitum voluntatis divine. Et sic possumus facillime voluntatem divinam cognoscere in effectu, et ita cum omnes debemus esse domestici fidei et sic de familia huius coniugii, debemus regulariter honorem sponsi et profectum sponse utrobique primo intendere, sicut exemplificat, Hugo De Sacramentis, libro 11°, parte IIª, secundo capitulo, ex textu apostoli Iª. Cor. XII°. Quamvis enim visio subiectatur in oculo, ipse tamen videt prius toti corpori quam sibi ipsi, et ita de quolibet membro humani corporis in tantum quod naturaliter membrum ignobilius ut brachium exponitur ad mutilacionem pro membro nobiliori ut capite, et quelibet pars naturalis integri intendit principaliter et finaliter conservacionem et bene esse suo toti. Et ita debet quilibet christianus quoad sanctam matrem ecclesiam, nullum membrum contrariando alteri sed iuvando; unde intendens prepostere proprietati commodi aspirat implicite secundum luciferinam superbiam ad honorem Deo proprium qui constituit universitates creaturarum que gracia sui finaliter ordinantur, quelibet autem pars unius tocius [p. 92] creati debet plus esse gracia sui tocius quam gracia sui ipsius. Et sic omnes creature et singule sunt finaliter propter Deum: et hec est racio, quare religio christiana ordinatur amare communi vivendo mentaliter in communi. Unde Christus non potuit civiliter dominare.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 88.31: Objection drawn from the gloss.
- 89.3: Answer: a. The Church means sometimes the visible Church mixed of good and evil.
- 89.15: b. To be in the Church is not be of the Church.
- 89.19: c. Men's different relations to the Church,
- 90.9: The faithful have a sufficient knowledge of the Church, although an imperfect one.
- 90.16: Knowledge not going beyond belief fits our state here.
- 91.1: and such a knowledge we have of the Church.
- 91.10: Nor is it difficult for us to know the divine will,
- 91.26: which is that we should serve the Church,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 88: *XXIIIª* [R4]
  - 89: *Et* (leading a is the margin letter) [NW]
  - 89: *granum* [R3]
  - 89: *palea* [R3]
  - 89: *XXIIIª* (one token 'XXIIIª,' (pivot splits XXI | IIª)) [R3]
  - 89: *∅* (IIª is the tail of XXIIIª (pos 128); no separate word) [R6]
  - 90: *Christi* [R3]
  - 90: *nostre* (Q is the alinea letter) [R4]
  - 90: *noticiam* (noti-/ciam hyphenated across line) [R4]
  - 91: *∅* (nothing between et and nesciamus; these words are on p.90 (already in p.90 text)) [INS?]
  - 91: *ex* ('Nor' is side-note text) [R4]
  - 91: *IIª* [R3]
  - 91: *Iª* [R3]
  - 92: *gracia* (141a is the folio mark; R is the alinea letter) [THIN]
  - 92: *sui ipsius* (token spans two printed words) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 88:
8. B: ut dignetur. 9. A in marg : Conclusio. 24. B: inquit —
rugam deest. 26. B: oportet hoc credo.
2i. Decreti sec. pars, causa XXXIII, q. III, cap. LXX. 3i. Decr.
sec. pars, causa XXIII, q. IV, capp: XI and XV.

p. 89:
3. A in marg.: Triplex solucio. 5. B in marg.: sint quod caro est,
quod palea est. 14. A in marg. : Ecclesia Christi sponsa. Nota. 16. A
m marg. : De ecclesta esse, in ecclesia esse, quid est. 17. A: Vasis
cnim. 20. B: et — nomine dcest. 26. A in marg.: Conclusio. Elcccio
pape vcl cardinalium non facit cos primatum tenerc in ecclesia sed
imitacio sancta.
6. ibid, XXXII, q. IV", cap. II. 17. Decr. sec. pars, causa
XXIII, q. IV, cap. XXIII.

p. 90:
2. A in marg. : Generacio Dei. (Above 140*.) B: sunt deest. 8. A:
patrissabunt. 9. A in marg. : De noticia. 19. A in marg.:
Noticiam qualem habemus de ecclesia et de partibus eius hic in via.
25. Hic locus corruptus esse videtur; tortasse legedum : tamcn non credi-
mus. 26. B: iidem. 27. A in marg. : Questio. 27. B: Unde
qucso. 3i. A in marg.: Responsio.

p. 91:
n. A in marg. : Conclusio. 17. A in marg.: Hugo. 20. B: prius
deest. 22. 23. AAa: ut brachium deest. 29. A m marg. : conciusio.
17. I have not been able to find this passage in Hugo de
S. Victore 1. c. but comp. lib. I, pars X, cap.VI.

p. 92:
5. A A, : dominare. In vigilia Pcntccostcs. i5. A: vcrissimile.
16. A,: auderet. 19. A in marg. : Ecclesie equivocacio.
Adcap. IV. cf. Hus, De eccl. fol. 216", 204°, 204b, 2o3b, t96b, 197%
198", 199", 2oo\ 1 1. Cf. Cod. pal. Vindobon. 1430, Libri septem
de paupertate Salvatoris seu de mendicitate fratrum. fol. 1" — 118;
fol. 1 ", in margine : Iste est liber magistri Adalberti Ranconis de Erici-
nio in Boemia. Et fuit reverendi domini Ricardi primatis
Ybernie doctoris eximii sacre theologie quem ipsemet dominus
Ricardus composuit contra fratres mendicantes in curia Romana
ad instanciam Clementis papa VI.
```

---

## Chunk 05-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-05-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-05-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "92.7–96.19"
divisions: "cap. 5 (heading 'CAP. V.' at 92.6); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "921 words; 824 unanimous or majority-real; 87 settled by vote (R2 61, R3a 21, R3b 1, R5a 4); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n129–n133 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 5, part 1: [TITLE]

## ¶1 · 92.7–92.18

> [p. 92] Sed adhuc obicitur contra dicta per hoc quod communitas intelligit per Romanam ecclesiam papam et cardinales quibus est necessarium omnibus aliis obedire. Et sic intelligit maior pars ecclesie in tantum quod dominus Ardmacanus scribit Innocencio pape librum De Pauperie Christi tamquam capiti universalis ecclesie. Et talem stilum a maioribus et minoribus recipiunt pape communiter, ubi utrinque est verisimile quod nec papa nec suus fidelis subditus audiret talem blasfemiam, si stilus ille foret scripture sacre contrarius. Quare ergo non potest universalis ecclesia vocari quecunque universitas fidelium viatorum?

[ENGLISH]

## ¶2 · 92.19–94.9

> [p. 92] Hic dicitur (ut supra) quod multi laborant in equivocis, loquendo de ecclesia, unde communiter universitas predestinatorum viancium vocatur universalis ecclesia tam in legibus quam in doctoribus. Et racio potest esse in hoc quod ipsi habent equivoce racionem inperfeccionis in obscuritate fidei qua filii superioris ecclesie sunt purgati. Et quod plus est: Aliqui desceni4iadunt [p. 93] particularius ad gradus universalitatum, et hii vocant ecclesiam Latinorum universalem ecclesiam, hii ecclesiam Grecorum vel Hebreorum, et sic de aliis linguis aut gentibus de quarum universitate solum considerant. Et hoc contingit vel ex radice superbie vel ignorancie. Nam quidam ex fastu aspirant quod sint magnarum universitatum capita. Quod non laudo, et hinc credo quod scole que olim vocate sunt studia generalia propter doctrinam septem arcium, nunc dicuntur universitates, cum sint quasi punctus in comparacione ad primam universitatem creatam. Quandoque autem ex ignorancia quidam vocant datam particularem congregacionem universalem ecclesiam, non putantes esse ecclesiam ampliorem, ut III Reg. XIX, 18, alloquitur Helyas Deum, quoniam ipse solus relictus est fidelis in populo, et tamen audivit divinum responsum quod Deus reliquit sibi septem millia qui non curvaverunt genua ante Baal (ut meminit apostolus). Sic quidam maniaci putant quod non sit fidelis in terris nisi sit eis seculariter subiectus, cum tamen stat quod sint multe gentes ignote linguis priores illis in ecclesia sancta Dei. Quando ergo doctores sic loquuntur ex circumstanciis, potest perpendi equivocacionis sue deteccio, ut vocando episcopum Romanum caput universalis ecclesie intelligitur quod sit caput tante Latine ecclesie quantam regit. Quod reputative vel suppositive potest dici de quocunque Romano pontifice cuius opera papalia ad hoc movent. Sed ne laboraverim in istis equivocis, limi avi ad universalem ecclesiam, distinctam contra particularem, que quidem universalis est unica, habens omnes alias eius partes. Nam (ut ostendi superius, cap. II) sunt multe [p. 94] tales particulares ecclesie: ideo decreta ecclesie et sancti doctores non debent vocare illam particularem et pauperem ecclesiam sic artatam in angulo ecclesiam sanctam catholicam. Verumptamen si papa ut olim regat illam secundum legem Christi principaliter et capitaliter tam in moribus quam in dubiis decidendis, tunc cum suo collegio potest dici virtualiter universalis ecclesia in effectu. Sed hec est solum per accidens dependens ab opere et non a nudo nomine.

[ENGLISH]

## ¶3 · 94.10–94.15

> [p. 94] Unde (ut dixi superius) solus Christus potest esse caput ecclesie sancte catholice. Ipsa enim (ut dicit Augustinus in epistola ad Dardanum) hdbet solummodo unum caput; nec movet quod respublica habet imperatorem et papam capita unum subordinatum alteri (ut exemplificat dominus Ardmacanus).

[ENGLISH]

## ¶4 · 94.16–95.1

> [p. 94] Nam caput tocius ecclesie oportet simul in unum exemplare tam spirituale quam seculare regnum, et cum hoc regnum ierarchie celestis ad quod officium nulla alia creatura potest attingere. Unde bene est pape, si habet a Christo virtutem ad regendum se ipsum et pauculas oves in spiritualibus, licet non blasphemet quod sit caput universalis ecclesie paris potestatis cum Christo. Nec debet eius vicarius sentire heretice quod regat parcialem ecclesiam viantem tam seculariter quam spiritualiter, dum Christus solum spiritualiter rexit utramque ecclesiam. Ideo sufficit eius vicario quod tam in temporalibus quam in spiritualibus regat spiritualiter eius iuvenculam. Nam vivendo seculariter Christus non potuit exemplare utrumque officium. Quomodo ergo eius vicarius? [p. 95] Regnum ergo imperatoris est independens

[ENGLISH]

## ¶5 · 95.2–95.29

> [p. 95] regimine pape et econtra. Utrumque tamen per accidens iuvat reliquum, licet prepositura spiritualis sit dignior. Regimen autem Christi respicit essenciali causacione regimen utriusque sui vicarii. Unde ne vicarii Christi inducantur in blasphemiam, usurpando ex verbis floridis honorem Deo proprium, necesse est doctores cavere ab adulacionibus et instar beati Gregorii vinum et oleum alternare. Nam secundum Commentatorem in prologo tercii Phisicorum sicut quidam assuescunt sic venenum comedere quod totum cibarium vertatur in substanciam venenosam: sic quidam sic assuescunt opinionibus falsis quod instruccioni veritatis redduntur inhabiles. Correspondenter evenit de honoribus (ut patet inferius cap...) Unde hodie non valet vocare prepositum nisi reverendissimum, sanctissimum et beatissimum, quia in quolibet inferiori gradu est dulia, sed in superlativo gradu est latria qua non est honor amplior expectandus. Correspondenter ad ista non quietatur prepositus vocari caput ecclesie militantis, sed exigit vocari caput universalis ecclesie et ecclesie tocius catholice. Utrobique tamen possunt predicta sane concipi, ut quod Deus sit in tali preposito tamquam in imagine adorandus velsecundo quod inter signandos prepositos ille sit reverendissimus, sanctissimus et tempore suo beatissimus, dum tamen nomen et meritorium ministerium correspondent; quod debet supponi in preposito reputative, non diffinitive asseri, dum tamen nec ocium nec commissum notorie contradicant.

[ENGLISH]

## ¶6 · 96.1–96.19

> [p. 96] Et sic Potest intelligi papam esse caput universalis ecclesie vel in quantum ministratorie propinquius gerit ministerium Christi quem induit, vel secundo equivocando in universali, universaliori et universalissimo intelligatur per universalem ecclesiam tota ecclesia militans quam hic regit; que debet supponi extencior quam alia militans cui vicarius eius preest. Melius tamen foret inniti modo loquendi scripture et instar apostolorum vehemenciori ac humiliori ministerio totalis ecclesie propter blasphemam ydolatriam precavendam. Nam dum papa non supereminet quoad Deum, sed appreciatur honorem secularem plus opere servili ecclesie, tunc facit populum non adorare eum, sed statum communem in alio ad sui dedecus et ypocrite detrimentum. Et ita ecclesia Romana potest sumi tripliciter: vel pro ecclesia catholica (ut in fine proximi capituli), vel pro papa, vel coniunctim et divisim pro suo collegio. Sed hec duo membra postrema sunt extorta.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 92.7: Objection: The Roman Church is commonly understood of the Pope and Cardinals.
- 92.15: Why may not "the whole Church" mean the whole of any body of the faithful.
- 92.19: Answer: Whole is used in various senses
- 93.1: and commonly in too low a sense
- 93.10: as of Universities.
- 93.14: Many do not know how great the Church is.
- 93.20: And some madmen think that only their subjects are in the faith.
- 93.29: We mean the Church truly universal
- 94.4: which Pope and Cardinals may represent if they rule rightly.
- 94.10: But only Christ can be its head;
- 94.16: to offer a model, of spiritual and secular rule.
- 94.22: The Pope has to rule only spiritually.
- 95.2: The emperor's rule is independent of the pope.
- 95.15: Prelates demand undue honours.
- 96.1: The Pope may be head of the Church, as meaning the militant Church that is under his rule.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 92: *CAP. V.* [HEAD]
  - 93: *18* (15 is the line number) [R3]
  - 93: *avi* (zoomed on leaf: 'limi avi' with an inkless gap before avi (a sort did not print; limi[t]avi by sense) - ink has avi) [R3]
  - 94: *Christus* [R3]
  - 94: *unum* [R4]
  - 94: *caput* [R3]
  - 95: *Christi* [R3]
  - 95: *Commentatorem* [R4]
  - 96: *Et* [THIN]
  - 96: *sic* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 92:
5. A A, : dominare. In vigilia Pcntccostcs. i5. A: vcrissimile.
16. A,: auderet. 19. A in marg. : Ecclesie equivocacio.
Adcap. IV. cf. Hus, De eccl. fol. 216", 204°, 204b, 2o3b, t96b, 197%
198", 199", 2oo\ 1 1. Cf. Cod. pal. Vindobon. 1430, Libri septem
de paupertate Salvatoris seu de mendicitate fratrum. fol. 1" — 118;
fol. 1 ", in margine : Iste est liber magistri Adalberti Ranconis de Erici-
nio in Boemia. Et fuit reverendi domini Ricardi primatis
Ybernie doctoris eximii sacre theologie quem ipsemet dominus
Ricardus composuit contra fratres mendicantes in curia Romana
ad instanciam Clementis papa VI.

p. 93:
2. B: ut bene vocant. 4. de quorum: in codd. 6. 7. B: quod
sicut. 21. 22. B: quod sicut; ib. B: ignote lingue. 2S. A in marg. :
Papa quomodo est caput ecclesic.
18. Mtllia virorum, cf. III Reg. XIX, 18: cf. Ad Rom. XI, 3. 4.

p. 94:
10. A in marg. : Solucio obiectns. Solus Christus est caput ecclesie
sancte catholice. 14. B: unum scribo animatum alteri. )5. B:
dominus Dardinandus. 24. Ainmarg.: Solucio obiectus. Papa debct
spiritualiter regere utramque partem ecclesie ct non seculariter. 28. A
in marg. : Conclusio.
12. Cf. Opp. Aug. II, pag. 678.

p. 95:
2. B: tamen dcest 4. B: Regnum autem. 7. A in marg:
Contra adulatorcs ad papam. 10. A in marg. : Commentator. B: Nam
— assucscunt dccst. i5. Num. capituli dcest. 18. B in marg. maii.
rec. : Revercndissime sanctissime cum vocatur, ydolatratur. 23. A in
marg. : Sensus duplex. 25. A in marg. : Nota dc titulis pape quomodo
debent intelligi.
10. Coramentator is the scholastic name of Averrhoes (Ibn
Roschdj.

p. 96:
10. AB: blasphemiam. 16. A in marg : Equivocacio ecclesie
Romane ad tria. 20. A in marg.: Secunda obieccio. 22. A in
marg. : Purgatorium. 24. B: unio sunt. 26. A in marg. :
Responsio. 29. A in marg. : Arismetricus et geometer hec videant.
(Abovc 141" wilhnut mark of reference.)
```

---

## Chunk 05-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-05-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-05-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "96.20–100.12"
divisions: "cap. 5 (heading 'CAP. V.' at 92.6); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "833 words; 767 unanimous or majority-real; 48 settled by vote (INS 1, R2 28, R3a 17, R5a 1, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n133–n137 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 5, part 2: [TITLE]

## ¶1 · 96.20–97.3

> [p. 96] Secundo principaliter arguitur contra dicta per hoc quod nichil unum et specialiter non unum corpus componitur ex spiritibus in purgatorio, ex viantibus in mundo et ex triumphantibus in celo, cum continuacio et unio sint de essencia corporis, eo quod aliter periret sciencia linearum. no Hic negatur assumptum, nec est continuacio vel uni cum sit accidens de essencia cuiuscunque substancie; nam in quotquot partes quantitativas corpus martiris divisum fuerit, manet durante forma idem corpus in numero, et Christus fuit humanitus in limbo et mortuus in sepulchro. Absit ergo quod credamus animas fidelium defunctorum tunc non esse partes [p. 97] ecclesie, quando instar Abel a quo cepit ecclesia sunt secure de sua beatitudine corpori Christi insolubiliter incorporate.

[ENGLISH]

## ¶2 · 97.4–97.5

> [p. 97] Unde in cantu ecclesie die Dedicacionis sic canitur: Rex Salomon fecit templum

[ENGLISH]

## ¶3 · 97.6–97.6

> [p. 97] Cuius instar et exemplum

[ENGLISH]

## ¶4 · 97.7–97.7

> [p. 97] Christus et ecclesia.

[ENGLISH]

## ¶5 · 97.8–97.8

> [p. 97] Sed tres partes sunt in templo

[ENGLISH]

## ¶6 · 97.9–97.10

> [p. 97] Trinitatis sub exemplo Ymma, summâ, media.

[ENGLISH]

## ¶7 · 97.11–97.11

> [p. 97] Prima signat vivos cunctos,

[ENGLISH]

## ¶8 · 97.12–97.12

> [p. 97] Et secunda iam defunctos,

[ENGLISH]

## ¶9 · 97.13–97.13

> [p. 97] Redivivos tercia.

[ENGLISH]

## ¶10 · 97.14–98.22

> [p. 97] Et quantum ad combinaciones parcium corporum tam eiusdem speciei quam disparium, dictum est diffuse alibi; quem ille solus inter homines per se perfecte novit numerum talium cuius sapiencia non habet numerum mensurantem. Et quantum ad lineas, dicitur quod licet resolvantur in attomos manent eedem, unde priorem et cerciorem noticiam habet de eis arismetricus geometro. Alia autem est racio continuacionis, unde prius considerat arismetricus de quantitate continui quam geometer, uterque tamen sicut ignorat quantitatem numeri attomorum compositi, sic ignorat eius precisam quantitatem; quadam tamen estimacione capta a sensu excedit geometer arismetricum, cum suffragio sensus cognoscit quomodo dyameter quadrati superat costam suam. Intellectus tamen ultra imaginativam percipit utrumque errorem: nam sicut in quadratis de costis nobis finitis quoad numerum punctorum contingit accipere dyametros [p. 98] eorum que paria puncta precise continuant, sic indubie quantumcunque magna fuerit figura quadrata contingit accipere dyametrum, que paria puncta contineat cum suo latere, ut capiendo dyametrum que de qualibet costa transversatili precise contineat unum punctum. Tunc precise quot sunt puncta in costa, precise tot sunt latera transversatilia, et precise tot puncta continet data dyameter. Et tamen contingit accipere aliam diametrum in cuius composicionem racione obliquacionis plura vel pauciora puncta ingrediantur. Nec scietur diffinite proporcio aut quantitas diametri respectu lateris, nisi scita quantitate numeri punctorum ex quibus componitur. Ideo querendum est de qua diametro arguens velit loqui, cum inter eadem puncta contingit accipere infinitas lineas, quarum nulla divisibiliter excedit a rectitudine racione variacionis punctorum dyametrum quantitative componencium. Et sic communiter est dyameter super qua cadit imaginacio maior costa, ut communiter dicitur in medietate proporcionis duple, sed certitudo deficit in tali imaginacione, cum error sensus in capiendo lineas corrigitur ex subtilitate intellectus (ut alias exposui).

[ENGLISH]

## ¶11 · 98.23–99.31

> [p. 98] Sed redeundo ad materiam de ecclesia dicitur primo quod sicut sensus errat circa magnitudinem et rectitudinem linee, quia ignorat numerum punctorum ex quibus componitur, sic viantes errant circa magnitudinem dignitatis vel meriti viantis, quia ignorant numerum et mensuram in quibus verbum eternaliter disposuit ponere sponsam suam. Multi enim obliquant a rectitudine iusticie, et sensus infixi in legibus humanis hoc non Percipiunt, sed intellectus considerans veritatem ac sapienciam scripture probabiliter percipit quod declinant a mandatis domini, quia solum in speculo scripture sacre discitur, tenetur et docetur sapiencia mandatorum. [p. 99] Dicitur secundo quod propter elongacionem a vera ecclesia et ab irradiacione luminis capitalis frequenter putatur ecclesiam Christi esse continuam quoad locum et tempus, dum tamen membra Christi et sponse per vacuitates predestinacionis et operis rarenter sunt positi. Multi enim putant totum populum et totum genus sibi succedencium esse christianos verissimos et capitales precipuos in area sancte matris ecclesie, cum tamen sunt vacuitates et membra diaboli. Sicut enim iuxta naturales et perspectivos videns silvam vel campum segetum a longinquo iudicat totum esse continuum consitum arboribus vel frumento, sic nos inperfecta fide videntes ecclesiam a longinquo, non obstante quod habeat in se arbusta sterilia atque zizannia, iudicamus eam plenam fructuosis arboribus et frumento. Et ad istum sensum exponit Lincolniensis propheciam Michee VII°: Ve, inquit, tanta christianismi dilatacio, tanto opere Christi et suorum mediante lege scripture elaborata, est hodie velut in brevis anguli angustia coartata. Plurimam namque mundi partem occupavit infidelitas et a Christi ecclesia separavit; de parte vere dicta christiana separavit a Christo scisma, de parte vero residua que respectu duarum prenominatarum admodum est parva et pauca (ut puto) non modicam porcionem separavit a Christo pravitas heretica, quasi autem totalitatem residui concorporarunt diabolo et separarunt a Christo septem criminalia peccata, ut iam voce lugubri plangat Christus dicens: Ve mihi quia factus sum sicut qui colligit in autumpno racemos vindemie, non est botrus ad comedendum. Uvas preciosas desideravit anima mea;

[ENGLISH]

## ¶12 · 100.1–100.12

> [p. 100] sanctus de terra et sanctus in hominibus non est Nam sponsus ecclesie plus invenit de ficu fatua et vite sterili, plus de zizannia quam de lignis fructiferis et frumento. Nam vitis que solebat facere uvas, ex quibus tamquam uberibus solebat mater ecclesia inebriare suos palmites (ut superius exponitur aBernardo) iuxta vaticinium prophete Isaie V° 2 facit labruscas, id est, fatuitates honoris mundani atque discordias. Ideo non restatut quid tales terram occupant in agro dominico, nisi ut reserventur colligendi in finali iudic et (ut dicitur Matthei XIII° 30) ad laudem ecclesie comburendi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 96.20: Objection: The Church dormant, militant and triumphant is not one body, since these parts are separate.
- 96.26: Answer: Separation is no bar to unity.
- 97.1: The souls of the blessed are incorporate in Christ's body.
- 97.19: A mathematical digression,
- 98.23: Men judge each other wrongly because their minds are fixed on human law.
- 98.31: The study of Scripture would make them wiser.
- 99.1: Some think that Christ's Church is united as to time and space, whereas the true members of Christ are scattered.
- 100.1: The visible Church contains more tares than wheat.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 96: *quod* [R3]
  - 96: *componitur* (com-/ponitur hyphenated; main token holds whole word) [R3]
  - 96: *Hic* [R3]
  - 97: *summâ* (leaf zoom: circumflex over final a) [R4]
  - 97: *attomorum* (atto-/morum hyphenated; main token holds whole word) [R4]
  - 98: *eorum* [THIN]
  - 98: *que* [THIN]
  - 98: *∅* (inserted "each" is the English side-note; print has Sed at box, no extra word) [INS?]
  - 98: *humanis* (huma-/nis hyphenated; main token holds whole word) [R3]
  - 98: *hoc* [R6]
  - 99: *frequenter* (is is the English side-note) [R3]
  - 99: *Christi* [R3]
  - 99: *vacuitates* (5 is the line number) [R4]
  - 99: *VII°* [R6]
  - 100: *sanctus* [THIN]
  - 100: *de* [THIN]
  - 100: *est* [R3]
  - 99: *secundo* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 96:
10. AB: blasphemiam. 16. A in marg : Equivocacio ecclesie
Romane ad tria. 20. A in marg.: Secunda obieccio. 22. A in
marg. : Purgatorium. 24. B: unio sunt. 26. A in marg. :
Responsio. 29. A in marg. : Arismetricus et geometer hec videant.
(Abovc 141" wilhnut mark of reference.)

p. 97:
6.Cuius: in codd.: Qxiorum, ut habet missale Andegavense apud Daniel.
I. c. Cuius in Sermonibus mixtis, Sermonc Proplcr fralres mcos et proxi-
mos Psalm. CXXI et in secunda partc Scrmonum super evangelia, Ser-
mone Egrediente Jesu de templn ait illi, MarciXlU leges (cf. Cod. Palat.
Vindob. 3928 fol. 97° ct fol. i57d). Ki. quem (sic) in codd. 20. li:
5. See Daniel, Thes. hymnol. tom. V, pag. 106.

p. 98:
2 B : signa quadrata 17. A: quantitatem. a3. A in marg. : Nota

p. 99:
1. A in marg. : Nota quare iudicium nostrum errat circa ecclcsiam.
(Above 14.2" without mark of reference.) 1. 3. B: a vera — ecclesiam
deest. 16. A. in marg.: Lincolniensis. 17. A in marg. : Ecclesia sancta
catholica quantum sit artata. iS. In codd.: medi". In codd.: qui
factus. 22. Codd.: vero. 3i. B: Uvas preter quas desideravit.
29. Prophct. Michaeae VII, 1. 2.

p. 100:
i. B: in hominibus non erit. 5. B : tanquam universalibus. ,3. A in
marg. : Nota de quadratura circuli. B in marg. : Quadratura circuli.
17. In codd: quod liguratur. . _ 32. AA,: cuius — intelligibilis deest.
3i. This passage is not to he found in the prophets.
```
