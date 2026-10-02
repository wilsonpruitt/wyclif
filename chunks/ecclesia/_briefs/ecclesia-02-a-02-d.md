# Translation brief: ecclesia 02-a–02-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-02-a.md chunks/ecclesia/wyc-ecclesia-02-b.md chunks/ecclesia/wyc-ecclesia-02-c.md chunks/ecclesia/wyc-ecclesia-02-d.md` once and fix what it reports.
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

## Glossary (the 118 rows these chunks use; the full file is GLOSSARY.md)

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
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| bigamia | bigamy | Canon-law sense: a second marriage (successive, or to a widow), a bar to orders; a **C** note at the first occurrence in each chunk says so. Ruled 2026-10-01 (3 sites; first *Eccl.* 11.6). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis | necessity of supposition | Conditional necessity. Pilot (*Eccl.* 3.21). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| contingens ad utrumlibet | contingent either way | T. p. 364. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| metaphisica | metaphysics | *Inter omnes metaphisicas* → "among all the metaphysics": he counts the doctrine of the church as one (T. p. 368). Pilot. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 02-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-02-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-02-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "25.24–28.7"
divisions: "cap. 2 (heading 'CAP. II.' at 25.23); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "558 words; 506 unanimous or majority-real; 43 settled by vote (R2 21, R3a 20, R3b 2); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n62–n65 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 2, part 1: [TITLE]

## ¶1 · 25.24–26.7

> [p. 25] Contra dicta obicitur probando, primo quod prima conclusio ad sensum expositum non est de intencione domini Bonifacii nec alicuius sui successoris, cum ex illo capitulo Maioritatis et obediencie intenditur quod [p. 26] omnes principes seculi secum conversantes debent parere sibi et cuicunque pape qui fuerit pro tempore ut capiti sancte matris ecclesie. Ex quo videtur innuere quod ipse et quicunque papa sit caput universalis ecclesie. Et eodem modo videtur quod intelligit Romanam ecclesiam singulariter illam in qua ipse presidet cum cardinalibus cui sit necessarium obedire.

[ENGLISH]

## ¶2 · 26.8–26.19

> [p. 26] ic dicitur quod nullus papa citra Christum potest catholice illud intendere: ideo non debet supponi in domino papa tanta blasfemia. Nam iuxta secundam conclusionem unica est talis ecclesia cuius caput est Christus, et non habet in terris multa capita, ne sit monstrum. Cum ergo nullus Christi vicarius sit Christus, sequitur quod nullus Christi vicarius sit caput illius ecclesie. Antecedens istius consequencie ponitur in dicta decretali secundum quamlibet eius partem. Nec videtur catholicum quod dicta decretalis sit in hoc impossibilis vel improvide posita quoad logicam vel metaphysicam.

[ENGLISH]

## ¶3 · 26.20–28.7

> [p. 26] Sed hic posset responderi tripliciter: primo quodl Christus et tota successio suorum vicariorum sunt unum caput aggregative, sed nullus eorum per se. Verumtamen non credo aliquem catholicum sani capitis hoc sentire, quia tunc negaretur Christum esse caput universalis ecclesie, sed unum aggregatum cuius Christus foret pars, et sic integrum corpus Christi non haberet Christum caput; quod reputo non minus hereticum quam blasfemum. Similiter, cum Christus sit caput tocius multitudinis vicariorum suorum et ipsi caput tocius residui, videtur quod ipse sit archicaput tocius ecclesie et nullus eorum. Vocatur enim caput matris ecclesie quod non communicat cum membris corporis in natura alia singulari, quia aliter haberet [p. 27] ecclesia nimis magnum et monstruosum caput; quod repugnaret perfeccioni opmcis, et si caput eius foret tale aggregatum, insuper nullus papa foret caput illius ecclesie. Si dicatur secundo quod quilibet Christi vicarius est participacione ipse Christus, instatur tripliciter: aprimo per hoc quod talis participacio non tollereta. distinccionem personarum et capitum, et sic mater ecclesia haberet mille capita. Secundo per hoc quod foret temeraria presumpcio vicarium Christi cui non fit revelacio asserere quod sit Christus, quia tunc verificaretur illud Luce XVII°, 23, de Antichristo dictum: Ecce hic et ecce illic. Sed Christus precipit: Nolite ire neque sectemini. Tercio per hoc quod iuxta hanc evidenciam quilibet christianus qui est membrum Christi foret caput universalis ecclesie. Et sic ecclesia foret nimis monstruosa, quia haberet quodlibet membrum caput, et per consequens, nullum aliud membrum. Vocatur enim caput universalis ecclesie persona capitalis vel principalis ecclesie quod notum est vicario Christi non posse competere, quia tunc foret super omnes angelos vel creaturas beatas in celo. Ideo tercio dicitur quod loquimur de tota ecclesia militante cuius quilibet papa est caput. Contra hunc asensum instatur tripliciter: primo videtur quod sunt tot ecclesie quot persone ecclesie, et per combinacionem longe plures, et per consequens, non foret tantum una ecclesia ad sensum decretalis in secunda conclusione expositum. Nam ista ecclesia foret iste persone fideles, que sunt omnino alie quam persone viantes tempore Petri: ergo et omnino alia ecclesia; et per idem, cum ista ecclesia individuatur ab istis personis, [p. 28] videtur quod quantumcunque corrupta vel gravata sit, erit de ecclesia, et per consequens, quicunque prepositus ecclesie foret nimis multociens viduatus et desponsatus ultra bigamiam, trigamiam et quemcunque gradum a nobis cognitum, et cum ecclesia non sit per accidens ecclesia, videtur quod mortua huic mundo manet ecclesia, sed triumphans.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 25.24: Objection: Our exposition is not what Pope Boniface intended.
- 26.1: He meant to claim the obedience of all princes to the Pope.
- 26.8: Answer: We must not attribute such blasphemy to the Pope.
- 26.20: It is urged 1. that Christ and his successive vicars make up one Head.
- 26.23: This denies the headship of Christ,
- 27.1: and of each individual pope.
- 27.5: 2. that each Vicar of Christ is by participation Christ. But a. there would be a thousand heads.
- 27.9: b. the vicar could not assert that he was Christ
- 27.14: c. every member of Christ would be a head.
- 27.24: 3. that we speak of the militant Church of which each pope is head.
- 27.27: But the Church would be always changing its individuality,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 25: *CAP. II.* [HEAD]
  - 26: *omnes* [THIN]
  - 26: *principes* [THIN]
  - 26: *catholice* [R4]
  - 26: *caput* (trailing b is the margin letter) [R4]
  - 27: *ecclesia* (131c is the folio mark) [R4]
  - 27: *instatur* (print has instatur (in-, not m)) [NW]
  - 27: *tripliciter* [NW]
  - 27: *conclusione* (conclu-/sione hyphenated; 131d is the folio mark) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 25:
1. AB in marg: Triplex epilogus. B in marg: Quero an Christus qui
est caput univcrsalis ecclesie debeat dici mcmhrum eiusdem ecclesie vel
non. 4-A,: qtii secundum sensum. 8.B: membra deest. 9. 10. B:
hoc sapcre. u. B in marg: Fides qua quis credit se esse membrum
ecclesie habct annexam formidinem. Viator habet lidem qua credit quod
est in gracia (secundum) prcscntem iusticiam. 16. B in marg: Rom.XI.
18. B: liat cum spe. 24. A in marg: Contra dicta. Nullus papa ncc
aggregatum ex papis est capud ecclesic (above i3ic ). 26. AA,: tamen ex.
23. Ad cap. I. cf. Hus, De eccl., cap. I — III. Opp. I. Fol. 196" — 199*.
27. Decret Unam sanctam. Extrav. comm. lib. I, tit. VIII, cap. I.

p. 26:
i. A : conversantcs parere. A, : parerent correxit in marg. 8. B in marg :
Responsio. 20. B in marg : Tcrcia responsio. 3i. B in marg: Quid
vocatur caput matris ecclesie? 33. B: in natura aut.
i'">. Decret. Unam sanctam. Extrav. comm. lib. I, tit. VIII, cap. I.

p. 27:
2.3. AA,: si — aggregatum decst. ig.Ainmarg: Caput universalis
ecclesie quid vocatur. B in marg: Caput ecclesie. 24. A in marg: Nullus
(papa) est capud ecclesie militantis. B in marg : Probat subtiliter quod
papa non est caput ccclesic niilitantis. 32. Codd : et alia. 33. iudTatur
in codd. Thc place here is certainly corrupt.

p. 28:
r. Quacunque corrupta vel g'uata in codd. g. A : unitatis. io. A,:
erunt pape. i3. B: in Romane ecclesie.
```

---

## Chunk 02-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-02-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-02-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "28.8–32.8"
divisions: "cap. 2 (heading 'CAP. II.' at 25.23); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1020 words; 941 unanimous or majority-real; 67 settled by vote (R2 36, R3a 26, R3b 1, R5a 4); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n65–n69 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 2, part 2: [TITLE]

## ¶1 · 28.8–30.11

> [p. 28] Si dicatur secundo quod manet continue eademb ecclesia propter unitatem capitis scilicet pape, non tollitur quin adhuc tot sunt ecclesie quot erant pape; quod est contra decretalem. Similiter, querendo de quiditate illius ecclesie, patet, cum sit date persone, ipsa non dependet ab ipso capite in racione ecclesie, cum decapitata ab isto capite manet eque sancta et sana; cum tamen iuxta responsionem hoc caput et hec ecclesia consequerentur se in morte et vita (nam sequitur expositorie: iste persone sunt hec ecclesia que durabit per totam vitam illius hominis): ergo iste persone sic durabunt, et per idem desinent, isto papa mortuo, quod nec oportet de ecclesia materiali nec spirituali, cum stat quod iste sit primus mortuus, tota ecclesia sua superstite. Nec oportet quod iste sit capitaneus omnium istorum in viacione, quia stat quod sit prescitus, aliis in ampliori gracia eciam secundum presentem iusticiam et finaliter perseverantibus ac viam oppositam viantibus. Similiter, eadem ecclesia apostolica cui Petrus presidebat manet modo et manebit continue, ut dicit ista opinio cum decreto. Iste ergo papa non potest esse caput super ista totali ecclesia, quia tunc haberet ex equo tot capita quot papas, et per consequens, talis ecclesia successiva non capit suam unitatem ab isto papa, cum habuit unitatem eandem quam modo, antequam ipse fuerit, sicut et habebit post eius corrupcionem. [p. 29] Quomodo ergo caperet esse suum a membro tam accidentali, cum more fluminis labentis ecclesia illa habet nunc unum et nunc alium in facie seculi presidentem? Nulla ergo istarum viarum et specialiter ista verificat quod quicunque fuerit Romanus pontifex, sit caput universalis ecclesie cui oportet omnem christianum de necessitate salutis obedire. Si dicatur tercio quod manet eadem ecclesia hominum a principio mundi usque ad novissimum electum (sicut dicit beatus Gregorius, XIX° Homiliarum, cum aliis sanctis), et illa capit unitatem a capite Deo et capite Christo qui a principio mundi manet in causis secundis, et habet membra fidem eius tenencia et quicunque fuerit papa pro tempore suo, oportet quod tota pars illius ecclesie secum conversans sit sibi subiecta ut capiti et abbati. Et ista responsio est subtilior quam priores. Sed non videtur mihi salvare decretalem ad sensum expositum sed pocius infringere illum sensum; quod videtur multipliciter. Nam primo patet quod preter istam ecclesiam oportet ponere aliam superiorem ex omnibus angelis et hominibus compositam cuius ista est pars. Et per consequens, ista non est universalis ecclesia, cum sit particularis, quia aliter forent due; quod est contra conclusionem secundam dicte decretalis. De totali autem que est omnes ecclesie extra quam non est salus nec possunt esse multe tales est nobis sermo. Item, quilibet Christi vicarius est filius talis ecclesie, quomodo igitur pater vel caput? Item, quilibet nostrum sicut et istorum paparum ignorat si sit membrum talis ecclesie: omnino ergo non debet presumere quod sit capitaneus omnium illorum propter apostolos et alios sanctos ignotos qui secundum aliam formam dominati sunt sue ecclesie. [p. 30] Item, cum sancti pape post mortem non perdunt dignitatem capitalis regiminis sue ecclesie, videtur quod manent capita ecclesie sue in patria; illa enim dignitas foret illis laureola. Nam sicut nullum membrum ecclesie potest desinere esse membrum ecclesie, sic videtur quod nullum caput cuiuscunque particularis ecclesie potest desinere esse caput eiusdem ecclesie, et per consequens, sunt mille particulares ecclesie, quarum capita sunt multorum paparum capita. Non ergo est verum quod unica est mater ecclesia cuius oportet quemcunque Romanum pontificem esse caput.

[ENGLISH]

## ¶2 · 30.12–31.2

> [p. 30] Item, tempore ante incarnacionem fuerunt multe particulares ecclesie quarum quelibet iam est eadem ecclesia, sed triumphans que quondam fuit militans, et illarum nullus Romanus pontifex fuit caput preter Christum; nec dubium quin ille ecclesie distinguuntur ab universali ecclesia et ab aliis particularibus ecclesiis: ergo multe sunt particulares ecclesie, et per consequens, una universalis ecclesia ex eis collecta; que sub iurisdiccione nullius Petri vicarii tamquam capitis sunt subiecte. Non enim patet evasio, loquendo de predestinatis fidelibus (de quorum numero non est Christus), quin ecclesie ille differunt ab invicem, sicut multitudines illarum personarum distinguuntur ab invicem, et si ecclesia dicit aggregata per accidens, tunc illa aggregata distinguuntur tam secundum subiecta quam secundum formas aggregatas longe plus quam Petrus albus et Petrus musicus. Si enim Deus servasset totam ecclesiam militantem tempore viacionis Christi usque hodie conversantem in Anglia et creasset novas ecclesias, sicut de facto fecit in Francia et alibi, tunc distinguerentur. Quare ergo modo non distinguuntur? Notemus ergo ecclesiam quam talis primo et per se regit, et invenietur quod [p. 31] non sit unica columba Christi, quia bene est isti, si sit abiectum membrum illius ecclesie.

[ENGLISH]

## ¶3 · 31.3–31.12

> [p. 31] Conformiter arguitur contra quamcunque opinionem in ista materia, querendo sollicite de quiditate illius ecclesie. Nam ista ecclesia que complete viat pro tempore Christi non potest esse alia quam ista eadem ecclesia, et sic de qualibet alia ecclesia singulari. Ex quo patet quod continue est alia et alia ecclesia, vians ad alietatem personarum ex quibus componitur; non enim valet negare sillogismum expositorium nec ei similem, nisi subsit plana diversitatis racio exprimenda etc.

[ENGLISH]

## ¶4 · 31.13–31.18

> [p. 31] Ideo dicunt doctores periciores quod dominus papa non est caput universalis sed particularis ecclesie, dum tamen perseveranter vixerit tamquam papa, sicut dicit septima conclusio capituli proximi; et sic videtur concedendum quod de possibili sit papa ipso superior hic in terris.

[ENGLISH]

## ¶5 · 31.19–31.32

> [p. 31] Posito quod unus alius perfeccius doceat et regat plurem populum conformiter legi Christi, sicut potest esse de summo sacerdote ecclesie Asiane, videtur tamen mihi quod non debemus contendere circa illud de inesse, quod iste quicunque conversans nobiscum sit talis, sed supponere excellenciam Romani pontificis super aliis eciam quoad Deum, quia certum est quod non est superior nisi fuerit superior quoad Deum. Ex quibus videtur mihi quod nullus Romanus pontifex cui non sit facta specialis revelacio assereret vel opinaretur quod subesse sibi sit de necessitate lsalutis cuiuslibet christiani. Nam (ut logici arguunt) multi sunt christiani pro suo tempore qui non subsunt sibi, sicut nec ipsemet qui est precipuus christianus.

[ENGLISH]

## ¶6 · 32.1–32.8

> [p. 32] Item, iuxta sepe dicta non sic assereret quod sit predestinatus, eo quod non est de substancia fidei catholice quod iste sit predestinatus. Ideo si assit sibi firma spes de hoc, oportet quod ex dono supernaturali fiat sibi specialis revelacio, sed si non sit predestinatus, non est capitaneus in ecclesia sancta Dei. Ergo non sic assereret quod subesse sibi tamquam capiti ecclesie sit de necessitate salutis cuiuslibet christiani.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 28.8: and there would be as many churches as there were popes.
- 28.22: Nor is it certain that a Pope is head of his contemporaries, for he may be reprobate.
- 29.12: It may be said that Christ is immanent in second causes and so obedience is due to the Pope as Christ's agent.
- 29.22: The Church would not be universal, and sO would contradict the decretal.
- 29.29: No pope knows whether he is a member of the Church.
- 30.12: There were churches before the Incarnation that had no pope at their head;
- 30.18: therefore the Church, that contains them, is under no pope.
- 31.13: The better opinion is that the Pope is head of a local Church.
- 31.23: Note this.
- 31.27: No pope should assert that subjection to him is needful to salvation;
- 32.1: Nor even declare that he is predestinate,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 28: *expositorie* [NW]
  - 28: *viacione* (print has viacione) [NW]
  - 30: *fuit* (f with crossbar) [R3]
  - 30: *vicarii* [R3]
  - 30: *Christus* [R3]
  - 31: *abiectum* [R3]
  - 31: *Christi* [R3]
  - 31: *Christi* [R3]
  - 32: *assit* (print has assit) [NW]
  - 30: *Item* [THIN]
  - 31: *non* (132a folio mark glued; reading is non) [THIN]
  - 32: *sepe* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 28:
r. Quacunque corrupta vel g'uata in codd. g. A : unitatis. io. A,:
erunt pape. i3. B: in Romane ecclesie.

p. 29:
X. A in marg: Hic nota. 10. B in marg: Gregorius electum; ibid.
Codd : Grcgorius XXIII. Moral. cap. I, Correxi. Cf. Greg. Opp. tom. I,
pag. 1 5-10. |3. B iu marg: Christus a principio mundi manet in
causis secundis. 23. 24. H: forent secundo.

p. 30:
6. A: sicut videtur. 10. B: cst untim. II. A: quenciinquc.
20. In codd. ittrediccione. 23. B: distinccioncm ab invicem.

p. 31:
4. A : querendo querendo. i3. A B in marg : Conclusionis responsio.
A in marg: Nota de subesse pape ut dicitur de necessitate salutis (above
col. i32b without mark of reference). 16. B capituli XXI (pro cpxi).
22. A in marg: Nota bene. 22. B: circa idem. 27. A in marg:
Ha, ha A B in marg: Conclusio.
i*">. Sce pag. 19. 1. 18.

p. 32:
21. A: omnem omnem. 25. B: bergmanis.
33. Extravag.Commun. lib. V, tit. VII, cap. II. Meruit carissimi.
```

---

## Chunk 02-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-02-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-02-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "32.9–36.24"
divisions: "cap. 2 (heading 'CAP. II.' at 25.23); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1152 words; 1033 unanimous or majority-real; 107 settled by vote (R2 45, R3a 35, R5a 24, R6a 3); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n69–n73 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 2, part 3: [TITLE]

## ¶1 · 32.9–33.34

> [p. 32] Item, stat christianum habere graciam a Deo cum hoc quod non credat esse aliquem talem papam, eo quod non oportet Deum uti eo ut ministro, dando quamcunque graciam. Et per idem, stat ipsum cum aliis paribus mori in gracia sine tali subieccione recognita; quo facto foret salus facta christiano sine subieccione huiusmodi. Ergo illa non est de necessitate salutis cuiuslibet christiani. Antecedens videtur satis possibile de communi lege. is Item, in maiori libertate est christianitas posita tempore legis gracie quam fuit posita tempore ante legem vel tempore sinagoge, sed tunc non oportuit omnem salvandum subici summo sacerdoti, levitico vel primogenito, sed suffecit servando iusticiam credere jn dominum Jesum Christum: ergo multo magis extenso merito Christi Jesu secundum legem perfecte libertatis. Minor patet de Job gentili, de bragmannis et multis aliis philosophis qui sine sensibili obediencia facta sacerdoti tali ex fide et iusticia operum sunt salvandi. Quare ergo non sic possent Greci et Indy subditi sancto Thome? Immo sic fuit de Paulo et multis conversis suis tempore sancti Petri. Non enim facit ista extravagans decretalis, ut christianitas ligetur servilius quam perante, ut patet de extravagante Clementis sequente in qua ostenditur quod rex Francie non exinde fuit sibi plus subditus quam perante. [p. 33] Item, nemo fit perplexus ex lege Christi obligatus ad impossibile, sed hoc contingeret data ista sentencia: ergo oportet ipsam esse mendacium. Minor probatur per hoc quod multi infantes statim post baptismum mortui non habent prudenciam, ut taliter subsint pape, nec virtutes infuse inclinant ad talem subieccionem, sicut inclinant ad subieccionem domino Jesu Christo. Et idem videtur de multis fidelibus adultis in diversis insulis qui neque si est huiusmodi papa audierunt. Similiter, pro tempore intercidente inter mortes paparum sunt christiani eque fideles ut ante vel post, et cum tunc non sunt sic subditi, sequitur quod talis subieccio non sit de necessitate salutis cuiuslibet christiani. Stat autem infantem in illo meditulio temporis nasci, baptizari et mori quem oportet concedere salvari, licet non sit subiectus tali Romano pontifici. Similiter, si ecclesia militans indigeret tantum influxu huius pape, videtur quod decapitata sentiret saltem in effectu subtraccionem suffragii; sic enim periret sancta mater ecclesia eciam interduo, nisi haberet influenciam domini Jesu Christi. Et si solum per accidens iste influit, quomodo est hoc de necessitate salutis ecclesie? Similiter, tunc ad perversionem domini pape necessitaretur totus populus christianus perverti, cum tunc deficeret sibi salus; sed maioris partis ecclesie potestati non subest quod papa sit moraliter bonus: ergo nec quod ipsa sit moraliter bona. Nemo enim potest dicere quod a papa prescito ut membro diaboli dependet salus cuiuslibet christiani, nec aliquis finget quod papa in quantum huiusmodi sit confirmatus in gracia. Similiter, supposito quod papa decrepitus cedat papatui et succedat alius minus bonus, sicut videtur multis probabiliter fuisse de Celestino et Bonifacio VIII° qui

[ENGLISH]

## ¶2 · 33.35–33.35

> [p. 33] 24. 25. B: nunciaretur. 29. A: scito. A, corr. in marg: prescito.

[ENGLISH]

## ¶3 · 33.36–36.4

> [p. 33] 34. Celestine V., the predecessor of Boniface VIII. was Pope from July 5, 1294 to Dec. i, 1294. [p. 34] edidit hoc decretum, tunc videtur ex vi communionis sanctorum quod, si sit talis salutis dependencia, salus Bonifacii pocius dependet a spirituali suffragio Celestini quam econtra, quia aliter introitus vulpinus in illud officium necessitaret Deum ad mendicandum a vulpe tali suffragium sue ecclesie. Videtur ergo quod Jnfluencia domini pape non sit nisi per accidens necessaria de quanto racione meriti sui est gratus Deo et utilis ecclesie pro qua orat; et talis necessitas ex supposicione, ex vi communionis sanctorum est in quocunque membro ecclesie, plus tamen in papa quam in aliis, si dictis et nomini facta compensent, vivendo similius vite Christi; et conformiter dicitur de subieccione et obediencia, quod ipsa debet extendi generaliter ad omnes, eciam ad discolos et tyrannos, sed precipue ad dominum papam, sicut ipse debet esse spiritualiter subiectus et obediens sue ecclesie, et sic obediencior atque in servitute subieccior quam aliquis subditorum. Confirmatur ex fide scripture Act. X°, de Cornelio cuius oraciones Deus accersivit ante colloquium cum papa Petro veniente ad eum pedestri et hospitante in domo corriarii; cuius diffinicio fuit talis: Non est personarum acceptor Deus, sed in omni gente qui timet eum et operatur iusticiam acceptus est illi. Nec dubium quin, si Deus misisset alium, eque fuisset Cornelius salvatus, ut patet de eunucho baptizato a Philippo (de quo Actorum VIII° cap.) et de gentibus conversis a Paulo et Barnaba (de quo Actorum XV°). Non enim diffinierunt apostoli ut gentes obedirent Petro, sed quod gracia spiritus sancti et domini Jesu Christi sufficit ubique terrarum cuilibet christiano. [p. 35] Item, cum non sit pertinens isti responsioni loqui de subieccione nisi de subieccione civili quali subditus subicitur domino seculari, videtur responsionem istam innuere quod oportet omnem christianum, si vult esse filius ecclesie, esse sic subiectum domino pape. Quod videtur falsum, cum nec Christus nec aliquis eius apostolus exegit talem subieccionem, sed manifeste prohibuit (ut patet Luce XXII°). Cum ergo multi christiani tunc temporis ante dotacionem ecclesie consecuti sunt salutem, ut oportet ex fide credere de sanctis martyribus qui non fecerunt talem subieccionem Romano pontifici, cum omnibus eis suffecit ad salutem fides formata et caput Christi: videtur quod inducere aliam subieccionem necessario fiendam Christi vicario sapit heresim. Christus enim in detestacionem subieccionis huiusmodi lavit pedes discipulorum suorum et tergebat lintheo quo se succinxit, Joh. XIII°. Petrus eciam post ascensionem fuit missus a sociis cum Johanne in Samariam (ut patet Act. VIII° et Gal. II°), sicut pacienter sustinuit ut debuit reprehensionem a Paulo (ut patet Gal. II°). Iste autem non sunt exacciones subieccionis civilis a subditis, sed pocius humiliacionis penes quas attenditur eorum maioritas, et sic vixerunt multi pape martyres in maximo cremento ecclesie. Dotatio ergo ecclesie non introduxit novum articulum fidei, ut sit necessarium ad salutem cuiuslibet christiani sic subici Romano pontifici. Confirmatur ex fide scripture: Nam Act. IV° diffinit Petrus quod Christus factus est in caput anguli et non est in aliquo alio salus. Nec enim est aliud nomen sub celo datum hominibus in quo nos oporteat salvos fieri. Cum ergo nomen [p. 36] cuiuscunque christiani pontificis sit aliud quam nomen huius capitis, sequitur quod in nullo tali nomine oportet ecclesiam salvari. Loquitur autem scriptura de nomine reali cui oportet credendo subici.

[ENGLISH]

## ¶4 · 36.5–36.24

> [p. 36] Secundo confirmatur ex textu apostoli I. Cor. 1° et 111° capitulis, ubi apostolus recitat inter carnales conversos fuisse contenciones et scismata. Unus inquit dicit: Ego quidem sum Pauli, ego autem Apollo, ego autem Cephe. Et post ostendit quod non refert per quorum apostolorum ministrum convertantur, cum tamen credant in fundamentum ecclesie quod non potest poni aliud preter id quod positum est, Christus Jesus. Sicut autem non refert per quam lucernam illuminetur domus ad hoc quod operarius faciat opus suum per quod acquirat stipendium, sic non refert per quem Christi ministrum, sacerdotem vel laicum, christianus accipiat lumen fidei, ut mereatur salutem perpetuam. Nec dubito quin nullus Christi vicarius presumeret asserere quod necesse est, ut lumen fidei cuilibet christiano per ipsum veniat et sic salus; quia hoc esset nedum asserere ipsum confirmatum in gracia et doctrina, sed parificare ipsum cum Christo, cum nonnisi per ipsum Deus posset communicare virtutem sue ecclesie.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 32.9: God can give grace otherwise than through him.
- 32.18: The Church is in greater freedom now than under the old Jaw, yet even then obedience to the chief priest was not needful to salvation.
- 33.1: Such subjection would bind men to do impossibilities.
- 33.10: Christians are none the less such in the interval between two Popes.
- 34.7: The influence of the Pope depends on how far he is pleasing to God.
- 35.8: The early Christians were not thus subject to the Pope.
- 36.5: St. Paul teaches that it does not matter through whom Faith is received.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 32: *credere* (cre-/dere hyphenated across line) [R3]
  - 32: *dominum* [R4]
  - 33: *influenciam* [NW]
  - 33: *Christi* [R3]
  - 34: *Celestini* [R4]
  - 34: *∅* ('of' is side-note text (The influence of the Pope)) [R4]
  - 34: *subieccior* [NW]
  - 35: *fiendam* (print has fiendam) [NW]
  - 36: *ubi* [R3]
  - 36: *parificare* [NW]
  - 35: *responsioni* (clear e in print) [NW]
  - 34: *X°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 32:
21. A: omnem omnem. 25. B: bergmanis.
33. Extravag.Commun. lib. V, tit. VII, cap. II. Meruit carissimi.

p. 33:
(none)

p. 34:
3. A: Celestii. 5. B: nunciaret. 10. B: vi oracionis. 14. B
obieccione. 20. AB: accercivit. A, corr. in: acceptavit. B in marg
Act. X. 27. B in marg: Act. VIII. 29. B in marg: Act. 5. 29. B
apostoli deest.
23. Act. X, 34, 35.

p. 35:
i. Isti responsioni refers to the beginning of the chapter. 2. AA,:
nisi de subieccione deest. 6. A in marg: Papa non exigeret ab aliquo
civilem subieccionem. 8. B in marg : Luce 22. 17. B in marg : Joh. III.
19. B in marg: Act. VIII. Gal. II. 29. B in marg: Act. IV. 3o. B: in
anguli. 3i. B: nomen deest.

p. 36:
5. B in marg: I. Cor. I. 10. 16. AB: ministerium; A,: misterium.
19. A: uter lumen. 25. B in marg: Math. 24. 3l. B in marg:
Augustinus.
3i. See Aug. Serm. CCXCII in natali Joh. Bapt. Opp. tom. V,
p. 2, pag. 1172 et seqq.
```

---

## Chunk 02-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-02-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-02-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "36.25–38.24"
divisions: "cap. 2 (heading 'CAP. II.' at 25.23); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "454 words; 403 unanimous or majority-real; 46 settled by vote (R2 30, R3a 15, R5a 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n73–n75 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 2, part 4: [TITLE]

## ¶1 · 36.25–38.24

> [p. 36] Tercio confirmatur ex prophecia Christi Matth. XXIV° 5, quam necesse est impleri. Multi inquit venient in nomine meo, dicentes: Ego sum Christus, et multos seducent. Cum ergo quicunque de se sic opinatus fuerit supra sanctos apostolos dicit implicite quod est Christus, videtur quod de quocunque tali (ut exponit Augustinus) verificatur Christi necessaria prophecia, et per consequens, supponendum est quodcunque [p. 37] dogma huius esse (ut dicit Christus) dogma falsum ecclesie seductivum. Unde iuxta seriem prophecie Christi ista blasphemia presupposita erit seminarium preliorum etc. Ex istis videtur mihi nimis temerarium asserere quod aliquis papa in decretali sua intenderit dictum sensum; sed sive Christus immediate sive quicunque eius discipulus ubicunque terrarum a spiritu sancto missus converterit in virtute Christi quamcunque personam vel populum, sufficit sibi cum finali perseverancia ad salutem. Et satis est sibi pro fide articuli de ecclesia catholica, ut credat fide formata quod sit una universitas fidelium predestinatorum, salvanda virtute meriti Christi, licet non expressius et particularius descenderit ad aliquem eius vicarium. Nec oportet credere vel implicite quod iste quicunque Romanus pontifex sit caput cuiusquam particularis ecclesie, nisi Deus ipsum predestinaverit, quia aliter oporteret fidem catholicam esse falsam et christianum fateri mendacium. Et ita, sicut non est de substancia fidei credere explicite quod iste Bonifacius, Clemens vel Urbanus sit predestinatus vel membrum sancte matris ecclesie, sic nec est de necessitate salutis omnium christianorum secum conversancium, ut explicite credant ipsum esse caput cuiusquam ecclesie, nisi facta et vita evangelica evidencius moveant ad credendum. Sed benedictus dominus matris nostre qui nostre peregrinanti iuvencule diebus istis providit caput catholicum, virum evangelicum Urbanum sextum qui rectificando instantem ecclesiam, ut vivat conformiter legi Christi, [p. 38] ordinatur ordinate a se ipso et suis domesticis. Ideo oportet ex operibus credere quod ipse sit caput nostre ecclesie, cum mediate vel immediate influit motum tendendi sursum ad corpus Christi, ubi congregabuntur et aquile; et in facto docet mediate vel immediate mundana spernere et sapide sentire celestia. Ista autem fides de nostro capite tam graciose et legitime nobis dato est credenda cum quadam formidine de corona sue finalis perseverancie. Ideo necesse est nobis fructuosa oracione pulsare Deum continue, ut ipse semper vacet nobis et eligat caput tale. Nec dubito quin ipse detestaretur hunc sensum decretalis predicte quod sit de absoluta necessitate salutis cuiuslibet christiani subesse sibi in mundanis honoribus vel servicio seculari, cum non querit nostra sed nos, volens instar apostoli aliquem fructum spiritualem in nobis sicut in ceteris gentibus impertiri. Nec dubium quin nos omnes tenemur subesse sibi de quanto tamquam verus Christi vicarius mandat magistri sui consilia et non ultra. Et sic licet omnes christiani tenentur esse subiecti invicem in timore, sibi tamen (in quantum talis) est necessarium ex supposicione subici, cum regit tam evangelice tantum gregem. Et ex istis potest colligi sensus decretalis catholicus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 36.25: Those who thus set themselves above the apostles, imply that they are Christ.
- 37.11: Concerning the Catholic Church a Christian has only to believe that it is the whole body of the predestined.
- 37.26: God is to be praised for the election of Urban VI,
- 38.12: who will doubtless reject this false sense of the decretal.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 36: *∅* ('thus' is side-note text (Those who thus)) [INS?]
  - 37: *dogma* (133a is the folio mark) [R4]
  - 37: *ecclesia* (133b is the folio mark) [R4]
  - 37: *una* (following a is side-note text) [R4]
  - 37: *meriti* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 36:
5. B in marg: I. Cor. I. 10. 16. AB: ministerium; A,: misterium.
19. A: uter lumen. 25. B in marg: Math. 24. 3l. B in marg:
Augustinus.
3i. See Aug. Serm. CCXCII in natali Joh. Bapt. Opp. tom. V,
p. 2, pag. 1172 et seqq.

p. 37:
1. Huius; scilicet cuiuscunque talis, vid. pag. 36. 1. c. 3o. 3. A A,.
Clnisti deest. 5.ABinmarg: Conclusio. Ainmarg: Nota quam eccle-
siam sanctam tenemur credere (bclow i33"). B in marg: Nota bene articulum
fidei credendum de ecclesia catholica. 14. B: expressimus. 19. AB
in marg: Conclusio. 20. B: de obcdiencia fidei. 27. In Codd.
AB: nostri. A, : nostre. 29. AB in marg: Nota de Urbano VI.
27. Archbishop Bartholomeo Prignani of Bari was elected Pope
on April 8thby the cardinals and crowned on Easter-Sunday ( 1^78).

p. 38:
1. In codd. orditur. 2. 3.B: caput nostrum ecclesie. 3. 4. B: influit
modum. 6. A A,: sapida sentire. B in marg: Ecce quomodo Urbanum
esse caput nostrum dicit csse lidem credendam cum formidinc. 21. In
codd. sibi tam. 23. AA,: regcm. Et. 25. AB in marg: Obieccio
prima. A in marg: Contra dicta. 28. AB in marg: Responsio. 3o. B
et conscqucns.
5. Lucae XVII, 3y. 21. Eph. V. 21.
```
