# Translation brief: ecclesia 04-c–04-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-04-c.md chunks/ecclesia/wyc-ecclesia-04-d.md chunks/ecclesia/wyc-ecclesia-04-e.md` once and fix what it reports.
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
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| famosior | best-known [sense] | Pilot. |
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
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 04-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-04-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-04-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "76.25–80.31"
divisions: "cap. 4 (heading 'CAP. IV.' at 69.4); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "992 words; 905 unanimous or majority-real; 67 settled by vote (R2 35, R3a 23, R5a 9); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n113–n117 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 4, part 3: [TITLE]

## ¶1 · 76.25–77.8

> [p. 76] Sed utinam considerarent, primo quod nec locus nec eleccio humana facit membrum ecclesie sed predestinacio divina respectu cuiuscunque qui perseveranter Christum sequitur in caritate et relinquendo omnia temporalia moritur penaliter in defensione legis sue. Secundo considerarent cum formidine conversa- cionem suam, quomodo vite capitis conformantur, quia ex fide debent credere quod nec sunt vel membrum ecclesie, nec illi sunt quibus facta ruit promissio, nisi relinquendo omnia usque ad mortem penaliter secuti [p. 77] fuerint dominum Jesum Christum. Tercio vero confidant in suo humili ministerio ecclesie et non in fastu vel questu seculi, cum solum sic: humilibus promittitur celestis hereditas. Deus enim non potest promittere regnum alicui christiano nisi sub tali condicione tacita vel expressa, ut pertinenter innuitur I° Reg. cap. II° de Hely, et alibi sepius in scriptura. Et utinam nostri prelati ad sentenciam istam attenderent.

[ENGLISH]

## ¶2 · 77.9–78.11

> [p. 77] Quarto obicitur per hoc quod non docetur efficaciter, quando quicunque sit membrum ecclesie qui est in gracia secundum presentem iusticiam, specialiter cum sanctus Thomas dicit hoc expresse, et idem videtur sequi ex dictis Ricardi de Sancto Victore. Aliter enim nemo absolveret prescitum nec incorporaret penitentem per misterium sacramentorum ecclesie, et sic titubaret fides sacramentorum tam ex incertitudine ministri quam ex ignorancia predestinacionis ministrantis. Hic dicitur (ut supra) quod quicunque vocaverit prescitum in gracia membrum ecclesie, equivocat cum Augustino de scriptura sacra, attendens ad modum loquendi vulgarem et reputacionem ecclesie militantis. Ideo detecta equivocacione expressi superius sentenciam sancti Thome. Et idem videtur Ricardus sentire quod, sicut predestinatus in quantumcunque magno mortali manet continue membrum Christi, sic prescitus absque gracia predestinacionis quantumcunque magnam graciam momentaneam habuerit non remanet eius membrum. Sic enim si foret paterfamilias, cedens lignum de silva quod ordinat aliquantulum expoliri, sed composicionem domus sue nunquam ingredi, non vere diceretur, vel quod ipsum lignum preparaverit in partem domus, [p. 78] vel quod unquam fuerit pars domus huiusmodi, quia sic quelibet domus materialis foret nimis magna, habens in composicionem sui omnes materiales substancias que sunt in potencia fieri eius partes. Sic videtur quod domus mundi excidens de massa humani generis quosdam ad ignem perpetuum, quosdam ut sint postes vel alie partes perpetue in domo domini, nec ordinavit nec futurum erat, ut comburendi forent pars ecclesie, quantumcunque politi fuerint ad tempus, sed finaliter reprobandi. Aliter enim diabolus et omnia membra eius forent pars domus domini.

[ENGLISH]

## ¶3 · 78.12–79.3

> [p. 78] Et si dicatur quod Christus habet pro statu viacionis secundum presentem iusticiam tugurium estivale cuius omnes tales sunt partes, tamen cum pro tempore ipsos inhabitat, nihil proposito nostro de tugurio, quia limitatur nobis sermo de sancta matre ecclesia, sponsa Christi, quam ordinavit perpetuam reginam, eternaliter secum mansuram, sine macula vel ruga, ut loquitur apostolus Ephesiis V°, 25, 27: Christus, inquit, tradidit semetipsum pro ecclesia, ut ipse sibi exhiberet ecclesiam gloriosam, non habentem maculam neque rugam. Et de illa dicit sanctus Thomas, De Christo, conclusione VIIIª articulo III°, quod ille est ultimus finis ad quem producitur sancta mater ecclesia per passionem Christi pro statu patrie, non autem pro statu vie; in quo si dixerimus, quia peccata non habemus, nos ipsos seducimus; et veritas in nobis non est (ut dicitur Iª Johannis 1° cap., 8). Unde miror quo spiritu nos qui sumus pregravati macula mortalis peccati et ruga venialis presumimus sine revelacione speciali frontose asserere quod sumus membra illius ecclesie. Et si dicatur quod ista non sunt verba sine racione, arguitur ex principiis fidei [p. 79] scripture quod impossibile est quemcunque prescitum quantumcunque magna gracia ad tempus prepolleat esse membrum sancte matris ecclesie.

[ENGLISH]

## ¶4 · 79.4–79.29

> [p. 79] Nam impossibile est Christum unquam non diligere sponsam suam vel aliquam eius partem, cum necessario ipsam totam diligit ut se ipsum. Sed impossibile° est ut aliquem prescitum sic diligat, ergo impossibile est ut aliquis prescitus sit membrum illius ecclesie. Pro probacione antecedentis suppono hoc famosum principium aput theologos quod Deus non potest quidquam de novo cognoscere sive diligere. Patet per beatum Augustinum VI° DeTrinitate XXVII° et eciam philosophica racio contestatur idem concorditer. Unde doctor profundus, libro primo, correlario XXIIIⁱ capituli pulcre declarat quod Deus nullum noviter diligit neque odit, nec magis aut minus una vice quam alia, nec preces aut quecunque merita bona vel mala flectunt aut mutant voluntatem divinam in minimo huc aut illuc, et quod omnem salvandum aut dampnandum, premiandum vel puniendum sub quocunque gradu voluit ab eterno salvari vel dampnari, premiari vel puniri, sub eodem gradu semper vult precise, et hoc nedum voluntate condicionali vel indeterminata, sed ita absoluta et determinata, sicut vult in presenti vel in finali iudicio aut post volet. Patet ex hoc quod Deus non potest incipere vel desinere quidquam intelligere nec actum voluntatis elicere, tum quia est immutabilis, tum eciam quia tunc noticia aut volucio divina dependeret ab extrinseco plus quam nostra.

[ENGLISH]

## ¶5 · 80.1–80.31

> [p. 80] Ex istis videtur quod Christus semper diligit totam ecclesiam ut se ipsum, quia aliquando sic diliget, scilicet post diem iudicii, quando regnabit cum eo (ut patet ex processu Cantici Canticorum). Aliter enim non foret verum matrimonium ex caritate perpetua Christi consencientis ad divinas nupcias, nisi sponsus qui est una persona cum sponsa ipsam diligat ut se ipsum. Exemplar enim oportet habere summum gradum denominacionis, quam exemplatis communicat, et hinc Ephes. V°, 25, 28, dicitur: Viri diligite uxores vestras, sicut Christus dilexit ecclesiam et semetipsum tradidit pro ea, ut eam sanctificaret, mundans illam lavacro aque in verbo vite, ut ipse exhiberet gloriosam ecclesiam, non habentem maculam aut rugam aut aliquid huiusmodi, ut sit sancta et immaculata. Ita et viri debent diligere uxores suas ut corpora sua. Ex ista fide scripture de sancta matre ecclesia patet cum dicto correlario quod debet semper diligere totam sanctam ecclesiam sicut diliget post diem iudicii; et per idem semper odit quemcunque prescitum, sicut unquam post diem iudicii. Cum enim Deus plene scit qualem finem quicunque prescitus cum ipso faciet et quantam penitenciam agent quicunque predestinati casuri, postmodum perpetuo Dei grati, patet quod necessario omnem predestinatum quantumcunque criminosus fuerit plus diligit, quam aliquem prescitum in quantacunque gracia fuerit temporali, quia primum eternaliter vult habere beatitudinem et alium ignem perpetuum. Testatur autem scriptura quod Deus odit peccatores, ut patet Psalmo V°, 7: Odisti omnes qui operantur iniquitatem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 76.25: They should consider that no office can make a member of Christ;
- 76.31: and reflect whether their life is conformed to that of their Head.
- 77.1: They should rely on humble ministry, not on worldly splendour.
- 77.9: 4. Objection: It is impossible to know who is a member of the Church,
- 77.16: and this discredits the Sacraments.
- 77.20: Answer: In one sense the foreknown may be members of the Church.
- 78.12: But in that sense the affirmation does not affect Our proposition.
- 79.4: Christ cannot cease to love his spouse nor any of her members;
- 80.1: Otherwise Christ would not be truly married to the Church.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 76: *facit* [R3]
  - 76: *conversa-* (first half of conversa-/cionem (cionem is pos 209); b is the margin letter) [NW]
  - 76: *illi* (print 'nec illi sunt') [INS?]
  - 76: *facta* [R3]
  - 77: *vel* (139a is the folio mark) [R4]
  - 77: *I°* [R3]
  - 77: *II°* (print 'cap. II° de Hely' (de is the INS? row at pos 48)) [R4]
  - 77: *de* (print 'II° de Hely') [INS?]
  - 77: *est* ('to' is side-note text) [R4]
  - 78: *Christus* [R3]
  - 78: *tugurium* (print has tugurium) [NW]
  - 78: *III°* [R4]
  - 78: *Iª* [R3]
  - 79: *XXIIIⁱ* (superscript i after XXIII (not a degree sign)) [R4]
  - 80: *ipsum* [R3]
  - 80: *iudicii* [R4]
  - 80: *videtur* [R5]
  - 80: *Christus* [R3]
  - 80: *diliget* [R3]
  - 78: *patrie,* (25 is the line number) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 76:
4. Codd: repungnarc. 10. A in marg. : Nota de papa. 25. AB in
marg. : Triplex consideracio. A A, : nullus locus vel Ieccio. Hus : nullus locus
vel elcccio. B in marg. man. rec: Nec locus nec eleccio facit predcstinatum.

p. 77:
g. A in marg. : Quarta obieccio. 12. B: ideo vidctur; i3: Ricardi
deest. 16. li: tutubarct. 17. 18. AA,: prcdestinacionis ministri.
B: ministrati. 19. A in marg.: Rcsponsio. Prcsciti ct predestinati
quomodo sunt in ecclesia. 23. A: iterum videtur. 15: Ricardus deest.
25. A in marg. : Conclusio. 28. A in marg. : Exemplum.
11. S. Thomas ct Richardus de S. Victore loc. cit.

p. 78:
12. A in marg. : Ficcio. 23. A in marg. : S. Tliomas. 26. 13: non
aut. 3o. Codd.: vcnali. 3i. B: asserunt.
i5. Cf. Thomae Opp. tom. V, 5i, 52. 25. S.Thomas;
Unde hoc erit in statu patriae, non autem in statu viae.

p. 79:
2. A in marg. : Nota bonam racionem. 3. A in marg. : Arguitur
quod impossibile est prescitum esse membrum ecclesie sponse Christi.
(Above i39b without marl; of reference.) 10. A in marg. : Supposicio.
12. A in marg. : Augustinus. 12. Rccte XIV, cap. XVIII, cf. Opp.
Aug.VIII, pag.95ycf.etlib.VIU, cap. XII. B: ideo contcstatur. i3. B in
marg.: Bradwardyn. 16. B: nec partes aut. 22. B in marg. : Probat
prescitum non essc partcm ecclesie.
14. Doctorprofundus; this Is the distinguishing nameofThomasof
Bradwardine, the wellknown theologian et mathematician. He was
confcssor ofEdwardlll and archbishop of Canterbury, and diedi!?4Q.

p. 80:
2. A in marg.: Christus diiigit totam ecclcsiam sicud se ipsum. 9.B:
exemplaris. 24. A in marg. : Conclusio. 2y. li: Testatur aut.
32. A in marg. : Quinta obicccio.
```

---

## Chunk 04-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-04-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-04-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "80.32–84.22"
divisions: "cap. 4 (heading 'CAP. IV.' at 69.4); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "839 words; 762 unanimous or majority-real; 70 settled by vote (R2 41, R3a 19, R3b 1, R5a 7, R6a 2); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n117–n121 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 4, part 4: [TITLE]

## ¶1 · 80.32–81.10

> [p. 80] Sed adhuc instatur quinto per hoc quod non ex-i presse fulcitur ista sentencia ex testimonio sanctorum doctorum vel textu iuris canonici, imo fingitur ad [p. 81] colorandum quod omnia que fuerunt vel erunt sunt Deo presencia, et sic ad tollendum principatum Romane ecclesie fingitur quod ecclesia est corpus et homo, ubicunque sunt fideles; quod Johannes papa XXII negat et philosophia de continuacione requisita ad esse corporis. Unde nisi a signo sensibili possemus discernere qui forent ecclesiastici, non possemus hic cognoscere matrem nostram; quod tamquam maximum inconveniens confunderet religionem christianam, cum nemo tenetur diligere quod non noscit.

[ENGLISH]

## ¶2 · 81.11–82.10

> [p. 81] Hic dicitur quod ista est concors sanctorum sentencia (ut partim patuit ex dictis), nec usquam invenietur aliquem sanctum contradicere isti sentencie, si non fallor. Unde sancti doctores, fides ecclesie et iura canonica tenent illam concorditer. Nam quoad etatem ecclesie sic scribit Augustinus super Psalmo CXLII°: Ecclesia, inquit, que est mulier antiqua, civitas Dei et corpus Christi, habet inicium ab Abel, sicut mala civitas a Caym. Sed contra istud obicitur, primo per hoc quod angeli confirmati qui sunt principalis pars ecclesie totum genus hominum precesserunt. Item, Adam et Eva qui sunt membra sancte matris ecclesie fuerunt priores filio suo Abel, non ergo sumpsit ecclesia inicium suum ab Abel. Quantum ad istud, dicitur quod ecclesia nunc sumitur pro universitate hominum predestinatorum (ut in auctoritate predicta beati Augustini) et nunc pro universitate creature beate (ut patet Encheridion LVI°), et cum in equivocis non sit contradiccio, patet quod nec [p. 82] verba nec sentencia Augustini contradicit supradictis de totali ecclesia. Et ita civitas Dei tempore vel natura precessit civitatem diaboli, cum angeli stantes pro primo instanti mundi erant civitas Dei quodam modo imperfecte, mali autem angeli non erant de civitate diaboli ante peccatum quod post fuit, et prius erant extravagantes presciti ad dampnandum ac excommunicandum se ipsos instituendo sese civitatem superbie; alios autem ex humili subieccione constituit Deus sibi in civitatem gloriosam quam semper inhabitat.

[ENGLISH]

## ¶3 · 82.11–83.5

> [p. 82] Ad secundum obiectum conceditur quod parentes Abel Prius erant imperfecte de ecclesia, sed ille fuit primus hominum qui consumavit viacionem perfectam incorporatus quoad perfeccionem beatitudinis, et sic dicitur quoad dignitatem totum genus suum precedere, unde quoad etatem ac unitatem ecclesie ponitur ista sentencia in decretis XXXII q. IV, Recurrat, sub auctoritate beati Augustini notabiliter in hiis verbis: Ecclesia que peperit Abel, Enoch, Noe et Abraham, ipsa peperit Moysen et prophetas tempore posteriores ante domini adventum, et que istos, ipsa et apostolos et martires nostros et omnes bonos christianos. Omnes enim peperit qui diversis temporibus nati apparuerunt, sed societate unius populi continentur. Tamquam eiusdem civitatis cives labores peregrinacionis experti sunt, quidam autem nunc experiuntur et usque in finem ceteri experientur. Et correspondenter loquitur de ecclesia malignancium: Que, inquit, peperit Caym, Cham, Ysmahel et Esau, [p. 83] eadem ipsa peperit Datan et alios in eodem populo similes, et que istos, eadem ipsa Judam, pseudoapostolos, Simonem magum et ceteros usque ad hec tempora pseudochristianos pertinaciter obduratos, sive sint permixti sive aperta precisione dissenciant.

[ENGLISH]

## ¶4 · 83.6–84.10

> [p. 83] Et post exponit quomodo allegorice docetur in historia veteris testamenti quomodo boni quandoque pariunt bonos, ut Jacob duodecim patriarchas, mali autem quandoque pariunt bonos, ut ancille Rachel pariunt Jacob filios, mali autem quandoque pariunt malos, et boni malos, ut patet de Ismahel, filio Abrahe et ancille. Et postmodum declarat quod palea nullo modo potest converti in frumentum sicut nec caro in spiritum, sed presciti omnes ab illa ecclesia que triumphans est sine macula vel ruga semper divisi sunt. Et sic patet ex testimonio sanctorum Augustini, Crisostomi et decreti quomodo est unica sancta mater ecclesia a principio mundi que eternaliter et impermixte amplexata est a sponsi dextera post diem iudicii. Unde, supposita ad istum sensum unitate sancte matris ecclesie, manifestum videtur quod nullus prescitus sit membrum illius ecclesie; nam solum illa est mater ecclesia pro tempore vie que coronabitur, nec habebit hic alias partes quam habebit post diem iudicii. Sed illa mater nostra post diem iudicii, quando erit sine macula vel ruga, non habebit prescitos sed solum predestinatos partes suas; ergo et modo. Assumptum patet de una sancta matre ecclesia que inutiliter serviret hic sponso, nisi post laborem eternaliter coronetur. [p. 84] Et hec eadem unica que in via fuit sancta ceclesia catholica. Non enim potest fingi quod decreta et sancti doctores loquuntur de alia sancta ecclesia catholica quam de illa, sic quod solum manebit una sancta ecclesia catholica usque ad diem iudicii, et post quando reciperet perfeccionem ultimam extinguetur vel in plures ecclesias dividetur, quia ut Augustinus dicit 111° De Doctrina Christiana cap. XXXII°: Illi qui in die iudicii statuentur a sinistris ut edi (sicut patet Matthei XXV°, 41) nunquam erant de corpore domini, sed

[ENGLISH]

## ¶5 · 84.11–84.14

> [p. 84] continue membra diaboli. Tale, inquam, aggregatum non foret sancta mater ecclesia sine macula vel ruga, quia per idem foret maledicta ecclesia malignancium, sedes sathane et meretrix adulterantis diaboli.

[ENGLISH]

## ¶6 · 84.15–84.22

> [p. 84] Ideo notet adversarius que sit illa mater ecclesia de cuius unitate leges, sancti doctores et ecclesia sic loquuntur et videat si membrum illius sit quivis reprobus. Nam in extravagante Bonifacii VIIIᵛⁱ suadetur multipliciter ex scriptura quod tantum est una talis ecclesia (ut patet cap. II), et idem exprimitur in decretis XXIVª q. I, Loquitur, cum concordanciis legum atque doctoribus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 80.32: 5. Objection: This opinion is not supported by doctors or the canon law.
- 81.11: Answer: All doctors and saints do support it;
- 81.16: as Augustine, who says that the Church began with Abel.
- 81.20: Objection: This would exclude the angels and Adam and Eve.
- 81.26: Answer: The Church sometimes is used only of men, sometimes to include angels.
- 82.11: Abel was the first to lead a perfect life, so in dignity he has the first place.
- 83.17: The Saints testify that there is but one holy mother Church,
- 83.21: of which none that is foreknown is a member,
- 84.11: or the Church would not be without spot or wrinkle.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 81: *colorandum* (139c is the folio mark) [R3]
  - 81: *et* ('gan' is side-note text (the Church began)) [R3]
  - 82: *Ad* [R3]
  - 82: *Et* (print 'Et correspondenter') [INS?]
  - 84: *sed* (print 'sed continue' (italic sed at line start)) [INS?]
  - 84: *loquuntur* [R3]
  - 84: *VIIIᵛⁱ* (superscript vi after VIII) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 80:
2. A in marg.: Christus diiigit totam ecclcsiam sicud se ipsum. 9.B:
exemplaris. 24. A in marg. : Conclusio. 2y. li: Testatur aut.
32. A in marg. : Quinta obicccio.

p. 81:
2. A, corrigerc vult: tollerandum. n. A in marg. ! Responsio.
14. A in marg. : Triplex testamentum. i5. B: concorditer etatem.
ii>. A in marg. : Augustinus. 21. A in marg. : Duplex obieccio. 21. Bs
qui sunt mcmbra. 26. A in marg.: Solucio. 27. A in marg. :
Kcclesie equivocacio. 20. In codd.: Encheridion XLI. Correxi.
19. Aug. Opp. tom V, prig. i58q. ?q. Aug. Opp. tom VI,
pag. 217.

p. 82:
11. A in marg. : Ad secundum. 12. A in marg. : Nota qualiter ecclesia
stimpsit exordium ab Abel, cum tamen angeli Adam et Eva precesserint,
qui sunt priores partes ecclesie qtiam Abel. (Below i3ac without mark of
reference.) B in marg. man. rec. : Ecclesia est unica eternaliter. 18. A
in marg. : Ecclesia quid est. 19 A, in marg. : Nota Augustinus in hoc
capitulo nullam facit mencionem de predestinacione nec de prescitis, ergo
racionem non habet ad propositum. 24. In decret. : Et eiusdem. 28. A
in marg. : Nota continue infra de ecclesia, de prescitis etde predestinatis.
(Above i3gd without jnark of reference.) Jb.: Ecclesia malignancium.
17. Decreti sec. pars, causa XXXII, q. IV, cap. II.

p. 83:
4. In decret. : in affeccione carnali pertinaciter. 6. A in marg. :
Generacio ecclesie. 9. B: pariunt malos. i3. B in marg. man.
rec.:Palea nunquam vertetur in frumentum sicut corpus in animum.
16. A A, : de testimonio. 17. B: unica t1 sancta. 24. 25. AA,:
Sed — iudicii deest.
6. Aug. 1. c: In omnibus enini christianis (fratres adtentlite)
aut per malos nascuntur boni aut per bonos nascuntur mali
aut per bonos boni aut per malos mali ....

p. 84:
8. A in marg. : Augustinus. 11. A in marg.: Nota. i5. B: Igitur
notet. i5. A in marg. : Vis racionis. 20. In codd. : X. 23. A in
marg. : Ecclesia. 26 A in marg. : Conclusio. 28. B in marg. : Nemo
audet se dicere membrum ecclcsie.
18. Scil. : Unam sanctam. Vide supra pag. 25, 1. 26. 2i.Decreti
sec. pars, causa XXIV, q. f, c. XVIII.
```

---

## Chunk 04-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-04-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-04-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "84.23–88.30"
divisions: "cap. 4 (heading 'CAP. IV.' at 69.4); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "993 words; 877 unanimous or majority-real; 98 settled by vote (DEL 2, R2 44, R3a 34, R5a 16, R6a 2); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n121–n125 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 4, part 5: [TITLE]

## ¶1 · 84.23–86.2

> [p. 84] Non ergo est nova ficticia sic loqui de unitate ecclesie, nec dubium quin sit illa que post diem iudicii erit regnum celorum, celestis Jerusalem et sponsa Christi (ut supra meminit Augustinus). Ex istis sequitur ut Sepe repecii) quod nimis magna foret presumpcio quemquam sine formidine vel revelacione asserere quod sit membrum illius ecclesie. Nam nemo nisi predestinatus et sanctus tempore suo sine macula vel ruga est [p. 85] membrum illius ecclesie. Sed nemo sine formidine vel revelacione assereret quod sit predestinatus et sanctus sine macula vel ruga: ergo conclusio. Unde miror qua fronte magis contendentes pro proprietate bonorum ecclesie, magis seculariter viventes, elongati a Christi conversacione et plus steriles ab execucione Christi consilii et precepti plus vendicant titulo participii illius ecclesie bona fortunii per accidens adiacencia illi ecclesie, quam fecerunt apostoli vel sancti patres priores. Numquid credimus quod sic placitantes sunt sancti sine macula mortalis vel ruga venialis? Si dicunt quod sic, desercio Christi consilii cum ocio sancti officii hos condempnat. Jus enim humanum non dat eis titulum taliter vendicandi, et ius divinum docet quod rapinam bonorum cum gaudio susciperent et que sua sunt non sic repeterent (ut patet cap. III° ex testimonio beati Gregorii). Quo iure ergo sic vendicant, cum nitendo sic illi titulo ab eodem se privant? Considerarent ergo condiciones sancte matris ecclesie, antequam redarguti ex proprio opere contra Christi consilia sic instarent. Et quantum ad dictum de Romana ecclesia, suppono quod illa dicatur sancta mater ecclesia catholica, sponsa Christi. Et patet quod illa diffunditur, ubicunque sunt fideles predestinati; unde (ut tetigi superius) Augustinus in epistola ad Dardanum cap. XI°, exponens illud Johannis XVIII°, 14, Expedit ut unus homo moriatur pro populo etc. Cayphas, inquit, prophetavit quod Deus filius suos congregaret in unum. Non, inquit, in aliquem unum locum corporalem, sed congregavit in unum spiritum et unum corpus cuius unum caput est Christus. Ex quo patet quod unitas sancte matris ecclesie stat in [p. 86] unitate fidei et virtutum, licet fideles quantumcunque varie localiter sint diffusi.

[ENGLISH]

## ¶2 · 86.3–88.19

> [p. 86] Unde beatus Isidorus, libro primo De Summo Bono cap. XIX°, ita scribit: Sancta ecclesia ideo dicitur catholica, eo quod universaliter per omnem sit mundum diffusa. Et Hugo, libro II° De Sacramentis parte cap. II°: Sancta ecclesia, id est, universitas fidelium corpus Christi vocatur. Et istam sentenciam innuunt decreta XXIª d.: Quamvis universe per orbem catholice ecclesie unus thalamus sit Christi, tamen sancta Romana ecclesia catholica et apostolica multis sinodicis institutis ceteris ecclesiis prelata est. Quod probat ex illo Matthei XVI°: Tu es Petrus et super hanc petram edificabo ecclesiam meam. Et illam ecclesiam vocat postmodum ecclesiam Romanam, primam apostoli Petri sedem, non habentem maculam neque rugam. Ista ecclesia non potest intelligi dumtaxat iste papa cum istis cardinalibus ac sua familia, cum ipsi cotidie recedunt et veniunt et crebrius quam alius fidelis populus sunt rugosi. Unde super isto textu sic dicit glosa: Argumentum, inquit, est quod ubicunque sunt boni ibi est Romana ecclesia. Et hoc argumentum daret plenam fidem fidelibus. Et sic intelligo decretum XXIVª, q. 1 A recta, ubi canon de Romana ecclesia sic loquitur: Hec est sancta et apostolica mater omnium ecclesiarum Christi ecclesia que per Dei omnipotentis graciam a tramite apostolice tradicionis nunquam errasse probatur nec hereticis succubuit. Ubi notum est hoc [p. 87] non posse intelligi de quolibet papa et suis domesticis. Ideo glosa sic loquitur: Quero, inquit, de qua ecclesia hic loquitur, quia non potest intelligi de papa qui dicitur ecclesia, ut supra eodem, Quodcunque, et VIIª q. prima: Scire debes. Sed certum est quod papa errare potest (ut XIX dist. Anastasius et XL dist. Si papa). Ideo nec ipse nec eius familia est illa ecclesia de qua hic dicitur quod errare non potest. Unde ipsa congregacio fidelium dicitur hec ecclesia (ut De Consecracione d. Iª, Ecclesia). Et sic intelligitur dictum beati Jeronymi positum XXIVª, q. i. Hec est fides. Sancta, inquit, est Romana ecclesia que semper immaculata permansit domino providente et beato Petro apostolo opem ferente in futurum manebit sine ulla hereticorum insultacione atque firma et immobilis omni tempore persistet. Hic non potest intelligi quicunque papa cum suo collegio. Illi enim sunt sepius maculati et insultacione hereticorum tam ab intra quam ab extra tamquam fragilis viator concussi, ut oculata fide patet diebus nostris, cum due partes cardinalium inponunt papa nostro et fratribus eum foventibus hereticam pravitatem, cum (ut inquiunt) nedum nituntur auferre privilegia Romane ecclesie, sed quantum in eis est ipsam destruere. Et omnis talis est hereticus (ut patet XXIIª dist. Omnes, ut patet libro VI°, tractatu de heresi). Cum ergo iuxta decreta Romana ecclesia habet primatum et dignitatem quoad Deum super omnes alias, patet quod illa est totalis ecclesia militans quam Deus plus diligit quam aliam eius partem. Et sic manifeste sequitur ex fide quod non illud collegium sed tota mater in omni gente et lingua dispersa [p. 88] sit illa sancta Romana ecclesia de qua iura quuntur cum sanctis doctoribus. Unde ad imprimendum in nobis istam sentenciam in cantu ecclesie per beatos Ambrosium et Augustinum composito mater nostra sic Deum alloquitur: Te per orbem terrarum sancta confitetur ecclesia. Et in canone misse primo et principaliter offerimus pro sancta ecclesia catholica, ut Deus dignetur pacificare, custodire et adiuvare eam toto orbe terrarum. Unde non dubium oratur pro principalissima ecclesia militante quam suppono esse Romanam ecclesiam, verumptamen inter partes eius in comparacione ad quantitatem sunt papa et suum collegium pars precipua dignitate, dum tamen sequantur Christum propinquius et deserendo fastum atque primatum serviant matri sue efficacius atque humilius. Nam faciendo oppositum sunt nidus hereticorum, apostema putridum et ydolum desolacionis cum aliis monstrosis nominibus in sacra pagina prophetatis.

[ENGLISH]

## ¶3 · 88.20–88.30

> [p. 88] Et ne fingam istam sentenciam, ecce decretum ecclesie De Penitencia d. Iª: Ecclesia, inquit, Christi non habet maculam neque rugam aut aliquid huiusmodi; qui ergo peccatorum sorde aliqua maculatus est, de ecclesia Christi non potest appellari. Maculam, inquit glosa, id est, heresim vel mortale peccatum, neque rugam, idest, scisma vel veniale. Sed hoc credo ego cum sancto Thoma debere modificari ad statum patrie, et hic quicunque est in macula mortalis peccati, protunc deficit ab humido fluent continuante, hoc est, gracia secundum presentem iusticiam.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 84.25: Hence it is presumption to assert oneself to be a member of the Church.
- 85.4: Yet this is done by prelates, whose lives are most unlike Christ's.
- 85.22: The Roman Church may be used as a name of the Catholic Church, including all the faithful.
- 86.17: It cannot be only the Pope and the Curia;
- 87.10: since Jerome's description of the Roman Church applies to them only by contrast;
- 87.28: but must be the whole Church militant.
- 88.12: The Pope and his college are chief in dignity if they follow Christ;
- 88.17: otherwise they are a nest of heretics.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 84: *ut* (print '(ut'; bracket is punctuation) [R3]
  - 85: *magis* [R3]
  - 85: *magis* [R3]
  - 85: *Christi* [R3]
  - 86: *dicitur* [R4]
  - 86: *II°* [R3]
  - 86: *XXIª* [R4]
  - 86: *XXIVª* [R4]
  - 86: *1* (x-height old-style figure 1 ('q. 1:'), not capital I) [R3]
  - 87: *Quero* [R4]
  - 87: *VIIª* [R4]
  - 87: *Iª* [R3]
  - 87: *XXIVª* (one token 'XXIVª,') [R3]
  - 87: *∅* (the V belongs to XXIVª at pos 92; nothing between it and q.) [INS?]
  - 87: *XXIIª* [R4]
  - 87: *Cum* [R4]
  - 88: *Iª* [R3]
  - 85: *membrum* (alinea M and 140a folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 84:
8. A in marg. : Augustinus. 11. A in marg.: Nota. i5. B: Igitur
notet. i5. A in marg. : Vis racionis. 20. In codd. : X. 23. A in
marg. : Ecclesia. 26 A in marg. : Conclusio. 28. B in marg. : Nemo
audet se dicere membrum ecclcsie.
18. Scil. : Unam sanctam. Vide supra pag. 25, 1. 26. 2i.Decreti
sec. pars, causa XXIV, q. f, c. XVIII.

p. 85:
22. A B in marg.:De Romana ecclesia. A in marg. : Romana ecclesia est,
ubicunque sunt tideles. 26. In codd. AB: cap. XVII. A, correxit iu
margine: XI. 27. Codd.: XIX.
27. Opp. Aug. tom. II, 690.

p. 86:
1. B: fiat in unitate. 4. A in marg.: Isidorus; in Codd. cap. XVI.
6. A in raarg. : Hugo. S.A,rectius: innuit decretum . 10. B in marg.:
Ecclesia per universum orbem est diffusa. 21. AAt: inquit et quod.
24. Ainmarg.: A recta. B in textu : Erecta. 27. B in marg. man. rec:
Romana ecclesia nunquam errat. 27. In codd.: A tempore.
3. Isidori De Summo Bono lib. I, cap. XIX, fol. i-]h ed.
Jehan Petit. 6. Hugonis de S. Victore, De Sacramentis lib. II, pars
II, cap. III. Opp. pars II, pag. 417. (Ed. Migne). 9. Decr.
prim. pars dist. XXI, cap. III. 23. Decreti sec. pars, causa
XXIV, q. I, cap. IX.

p. 87:
2. A in marg. : Nota glosam. 14. li: fercntem. 28. A: patet illa.
3l. Codd. ligua.
4— 11. Decreti sec. pars, caus. VII, q. I, c. VII, prima pars
dist. XIX, c. IX, dist. XL, cap. VI; sec. pars, causa XXIV, q. 1,
cap. VI. et XIV. Non est Hieronymi. Polyc. I, 3, 6. Cf. Friedber^ in
Corp. iur. canon. pars I, pag. 970. 24. Dec. I pars dist. XXII, c. I.

p. 88:
8. B: ut dignetur. 9. A in marg : Conclusio. 24. B: inquit —
rugam deest. 26. B: oportet hoc credo.
2i. Decreti sec. pars, causa XXXIII, q. III, cap. LXX. 3i. Decr.
sec. pars, causa XXIII, q. IV, capp: XI and XV.
```
