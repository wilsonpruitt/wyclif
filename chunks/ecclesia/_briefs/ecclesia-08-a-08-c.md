# Translation brief: ecclesia 08-a–08-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-08-a.md chunks/ecclesia/wyc-ecclesia-08-b.md chunks/ecclesia/wyc-ecclesia-08-c.md` once and fix what it reports.
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

## Glossary (the 131 rows these chunks use; the full file is GLOSSARY.md)

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
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| redarguere | to refute | T. p. 365. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 08-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-08-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-08-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "157.26–160.24"
divisions: "cap. 8 (heading 'CAP. VIII.' at 157.25); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "686 words; 646 unanimous or majority-real; 32 settled by vote (R2 21, R3a 11); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n194–n197 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 8, part 1: [TITLE]

## ¶1 · 157.26–160.12

> [p. 157] Quia sciencia secundum philosophos gaudet extraneis ac sciencie de sancta matre ecclesia sit nimis extraneus infamis casus qui contigit nuper in Anglia et in Roma, ideo gracia declaracionis fidei et cavendorum errorum ecclesie restat parumper disgredi circa [p. 158] ista, primo supponendo tria per ordinem. Primo, inquam, ex supradictis supponatur predicta sentencia de quiditate sancte matris ecclesie, nec est illa abicienda a Christi ecclesia, cum nec contingit ecclesiam speculative nec practice quicquam cognoscere nec meritorie debite conversari, si sit omnino destituta ab eius noticia. Nam iuxta dicta XVⁱ cap. theologus foret nimis inscius racionum scripture et fidei orthodoxe qui omnino ignoraret quiditatem sancte matris ecclesie. Nec dubito quin deest decretistis, legistis et philosophis fructuosa speculacio qui omnino ignorant quid sit sancta mater ecclesia. Nam omnes leges humane sunt finaliter ad defendendum iusticiam huius matris et purgandum eam ab erroribus quibus pro tempore vie temptacionum adversitatibus implicatur. Cum ergo finis inponit maximam necessitatem operibus, ex II° Phisicorum manifestum est quod oportet omnes doctores speculativos statuere matrem nostram ut regulam ad tractatum speculabilium mensurandum, et per idem nemo intendit praxi laudabili, nisi in quantum tenderet ad honorem vel commodum huius matris; nec dubium quin nemo viat meritorie secundum beneplacitum sponsi ecclesie, nisi dequanto operaturad honorem et commodum sponse sue. Et hinc precipitur in primo mandato secunde tabule quod fidelis honoret patrem et matrem, quod indubie principaliter intelligitur de Christo et sua ecclesia. Nec honorat eam vel diligit fideliter quam non noscit. Ideo necesse est, ut omnis fidelis det operam ad cognoscendum direccius matrem suam. ab- Secundo supponitur quod procedatur in isto tractatu sine duplicitate mendacii. Nam mendacium est precisa cautela per quam diabolus illudit fidelibus, ut [p. 159] honorent meretricem secum adulteram tamquam reginam et matrem fidelium sponsam Christi. Unde istam sentenciam de quiditate sancte matris ecclesie oportet ut fundamentum supponere, ut sciatur qui procurant pro eius veris privilegiis et qui degenerant, in quo consistit verum privilegium ac edificacio ecclesie et in quo stat eius oppositum secundum fidem scripture, et de congruitate status moderni in comparacione ad florem etatis ecclesie iuxta modum loquendi scripture. Sed in ista materia sunt quidam moderni doctores approbantes mendacium et dicentes quod veritates tales scripture non sunt dicende tum propter perturbacionem ecclesie, tum eciam propter scelera que hostes ecclesie ex eorum audacia perpetrarent. Unde arguitur et tenetur quod doctores vocati ex mandato domini regis et iurati ad dicendum veritatem de casu qui nuper contigit in Westmonasterio ad honorem Dei, ad utilitatem ecclesie et ad expurgacionem errorum in regno, ut exinde stet constancius in virtute, mentiri debuerant propter duo: primo pro fama sua servanda qui actenus reputati sunt hostes ecclesie; quilibet autem debet diligencius servare famam propriam quam famam alienam pro qua in casu mentiri est licitum. Secundo debuerant mentiri ad conservandum privilegia ecclesie que essent aliter destructa, veritate detecta dominis temporalibus et patronis. Cum autem dicta privilegia sint prestanciora quam vita hominis pro qua servanda licitum est mentiri, multo magis debuerunt mentiri pro illis privilegiis conservandis. Quantum ad principium illius sentencie patet ex tractatu De Mendacio quod est cuilibet fideli detestabile ut hereticum et blasphemum. Nam si aliquod mendacium sit meritorium et aliquod superhabundans [p. 160] in menciente ultra quam oportet, aliquod autem in extremo deficiente apud eum qui ex cauterizata consciencia nimis parce mentitur, sequitur quod habitus mendacii inter hec duo extrema tenens medium foret virtus. Patet consequencia ex diffinicione virtutis posita II° Eth. VI°, cap.: Virtus est habitus electivus in medietate consistens quoad nos determinatus racione. Hoc tamen abhorreret gentilis philosophus Aristoteles, cum IV° Ethicorum, C. IV°, tractans de virtute veridici et duplici vicio falsidici, ita scribit: Per se autem mendacium pravum et fugiendum, verum autem et bonum laudabile.

[ENGLISH]

## ¶2 · 160.13–160.24

> [p. 160] Item, cum omnis virtus sit de genere tertii boni maximi, descendens desursum a patre luminum qua virtute nemo abuti potest (ut sepe meminit beatus Augustinus), sequitur quod omnis virtus mendacii sit a Deo, et cum omnis pater et auctor virtutis sit autonomatice virtuosus, sequitur quod Deus, pater et auctor mendacii, sit summe mendax, sicut Christus secundum humanitatem foret homo mendacissimus potens esse, et per consequens, nullus fidelis dubitat esse blasphemum, cum Manichei blasfemi dixerunt micius quod non Deus bonus, sed Deus malus sit origo et principium talis mali.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 157.26: Digression on the shameful event which has lately happened in England and in Rome.
- 158.1: Three postulates: 1. The quidity of the Church as already explained.
- 158.30: 2. That we abjure all falsehood.
- 159.10: Some doctors say that it is right to give false opinions in such a case,
- 159.20: for the sake of one's OWN reputation,
- 159.24: or to maintain the privileges of the Church.
- 160.2: This would make lying a virtue,
- 160.19: and God a liar.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 157: *CAP. VIII.* [HEAD]
  - 158: *II°* [R3]
  - 159: *honorent* (150c folio mark, A margin letter) [R3]
  - 159: *consistit* (150d is the folio mark) [R4]
  - 160: *II°* [R3]
  - 160: *C* (print: Ethicorum, C. IV°; round C) [R4]
  - 158: *supponendo* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 157:
4. B: exinde proverant (sic). i3. A A^: peioratur. 14. A in
marg. : Nota bonas hortaciones. 20. D: ne aliter. 20. 21. D:
infra cepta. A A, B : Christus deest. 24. A in marg. verba tsclie-
chica : Nu zbohem mylym potahnyem dale. Id est: Age, cum Deo caro
(matcriam) porro tractabo.

p. 158:
1. B in marg. man. alt. : Posteriora prius dicit. A in marg. : Tres sup-
positiones. (Below i5oc without mark of reference.) 12. A in marg. :
Racio: Necessaria est noticia de sancta matre ecclesia.
iG. Cf. Arist. <frooty.vj; <iv.poaaE(u; B. 2. Opp. tom. I, 194.
2 5. — 2y. Cf. supra pag. 1.

p. 159:
l. B: honorent meretricium. 5. B: quod eius vcris. 14. A
in marg. : Opinio. 22. B in marg.: Fame causa licet mentiri. B:
quibus autem dcbet. 24. Codd.: debuerunt. 3o. A in marg. :
Rcsponsio. Contra scntenciam quc dicit licitum cst mentiri.

p. 160:
9. Vide Trialogum lib. III, cap. I (ed. Lechler, pag. 128). Cf.
Arist. Eth. Nic. II, VI. graece, Opp. II, 1 106; latine, Opp. III, 544.
17. Aug. Retract. lib. I, Cap. IX; De Lib. Arbit. II, cap. XIX.
Opp. I, i3, 607.
```

---

## Chunk 08-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-08-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-08-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "160.25–163.27"
divisions: "cap. 8 (heading 'CAP. VIII.' at 157.25); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "748 words; 672 unanimous or majority-real; 58 settled by vote (R2 43, R3a 13, R5a 2); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n197–n200 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 8, part 2: [TITLE]

## ¶1 · 160.25–162.5

> [p. 160] Nec dubium quin non sit dare virtutem in homine, quin eius ydea vel exemplar sit in Deo et Deus virtute supra genus est taliter virtuosus, ut non posset exemplare iusticiam, misericordiam, patienciam, liberalitatem, et sic de et aliis, nisi ipse foret summe iustus, misericors, paciens et liberalis, et sic de principiis cuiuscunque generis virtutis. Et sic antecedenter ad virtutem mendacii [p. 161] oportet Deum esse summe mendacem. Non enim est fingendum quomodo pertinencius denominaret habitus mendacii subiectum suum quam mendax, cum mentiri sit opus virtutis. Item, suppono ex fide scripture quod Deus dicit quicquid creatura aliqua bene dicit; patet ex hoc quod omnis creatura ut sic est organum Dei principalius dicentis quam sua fistula, iuxta modum loquendi Psalmi LXXXIV, 9: Audiam quid loquatur in me dominus Deus. Et Apostolus IIª, Corinthiorum XIII°, 3: An experimentum queritis eius qui in me loquitur Christus. Ex quibus cum veris sequitur quod tam trinitas quam Christus humanitus facit in omni christiano mendace quodcunque mendacium virtuosum, et cum virtuosum non sit distrahens sed pocius viciosum, sequitur quod Deus simpliciter facit mendacium, et cum dicit falsum eadem intencione qua christianus pie menciens, sequitur quod Deus principalissime mentitur et per consequens mendax est, ut pater eius, ut Christus dicit Johannis VIII°, 44 de ipso diabolo. Cum enim Deus illo modo mendacium loquitur, ex propriis loquitur, cum sit fons et origo mendacii, et ita cum dicit angelis veritatem in verbo, nobis menciendo foret duplex animo, et forent in eo est et non contra Apostolum IIª, Cor. 1°, 17. Ymo, cum ipse sit omnis veritas, negando veritatem virtute mendacn, se ipsum negare posset, contra Apostolum IIª Thymotei II°, 13, et foret racione mendacis principii cateclismus tocius fidei christiane. Cum enim Deus mentiri potest iuxta sic opinantes nec potest habere denominacionem virtutis, nisi habeat ipsam in summo et quodam modo infinite, sequitur ex infinitate sue mendacitatis immense quod in tota fide sue scripture potuit totam ecclesiam decepisse [p. 162] dolose. Aliter enim esset dare finem sue mendacitatis immense, usque ad quem et non ultra potuit decepisse; quod credo non dabitur, cum dicitur communiter quod sit infinitum misericors sed finite solum modo miserator.

[ENGLISH]

## ¶2 · 162.6–163.27

> [p. 162] Quantum ad illas duas evidencias quod debuissemus mentiri contra iuramentum nostrum tam pium atque legitimum coram consilio regis nostri, Deum contestor et numina quod inter omnes doctrinas vel consilia que audivi non occurrit mihi aliquod difficilius aut detestabilius. Ideo videtur mihi quod minus male potuit fuisse dictum ad partem quam publice sic in scolis, nam sic menciens manifeste incurrisset periurium et infamiam quam vitabat, et ita conclusisset culpabiliter, secundum metam redargucionis maxime sibi ipsi. Ideo minus malum est sine dampno anime pacienter pati detracciones et scandala, quam menciendo et per consequens iniuriando toti universitati create, offendere dominum veritatis. Non enim ymaginari potest casus nec inveniri ficticia in quo vel qua licitum est mentiri, immo crescente mendacio eciam in clero plus solito esset opus doctoris proferre de thesauro scripture raciones et sanctorum testimonia in detestacionem mendacii et non fovere mendacium mendaciis allegacionum et sophisticis argumentis. Ego quippe horrerem introducere scolam istam tamquam doctor mendacii, cum ex fragilitate nimis proni sumus ad hoc sine abduccione peregrina per scienciam menciendi; doctor itaque, docens quod licitum est mentiri, inperfecte procedit, nisi doceat quomodo licitum est mentiri, et per consequens, nisi doceat quomodo debemus mentiri, et sic secundum scolam mendacii foret laudabile mentiri fingendo false doctores extraDi5ibneos [p. 163] et dicta sanctorum doctorum pro ista sentencia coloranda. Sed quis crederet tali scole: Et dico mendaciis allegacionum, quia allegatum est contra me dictum Augustini, super illo Psalmi Vⁱ, 7: Perdes omnes qui loquntur mendacium, sub hac forma: Multa, inquit, videntur pro salute aut commodo alicuius non malicia, sed benignitate mendacia: quale fuit illarum obstetricum in Exodo que Pharaoni falsum renunciaverunt, ut infantes filiorum Israel non necarentur, sed eciam ista non in re, sed in dolo laudantur. Et hic notant allegantes hanc formam verborum quomodo aliquis est pius dolus quo licet nobis proximum menciendo decipere. Sed ego respexi multos libros Augustini in quibus dicit concorditer quod iste obstetrices in isto mendacio peccaverunt, licet peccatum fuerit Hebreis proficuum, unde cum nullum bonum sit irremuneratum, Deus pro pietate quam habuerant fecit eas taliter premiari. Unde Magister Historiarum super Exodi cap. III° quod sic incipit: De indole obstetricum, sic loquitur: Quia timuerunt Deum, edificavit illis domos, id est, locupletavit eas, cum essent pauperes, vel fecundavit eas, cum essent steriles. Augustinus vero dicit obstetrices venialiter peccasse, Gregorius vero videtur velle quod mortaliter; dicit enim quod merces benignitatis earum non potuit in eterna vita retribui, sed pro culpa mendacii in terrenam compensacionem declinata est.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 161.26: So the whole Christian faith would fall to pieces.
- 162.6: No worse doctrine was ever propounded than this, that we ought to lie to the King's Council.
- 162.20: No case can be imagined in which it is lawful to lie.
- 163.1: The false doctrine is supported by false quotation.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 161: *oportet* (151a folio mark, C margin letter) [THIN]
  - 161: *Deum* [THIN]
  - 161: *esse* [THIN]
  - 161: *est* (short ascender with crossbar = t) [R4]
  - 161: *in* (10 is the line number) [R3]
  - 161: *IIª* [R3]
  - 161: *Christus* [R3]
  - 161: *Christus* [R3]
  - 161: *IIª* [R3]
  - 161: *IIª* [R3]
  - 161: *13* [R3]
  - 162: *∅* (debuisse-/mus is one word, already whole at pos 39) [INS?]
  - 162: *regis* [R3]
  - 163: *Vⁱ* (superscript i after V (Psalmi Vⁱ, 7)) [R4]
  - 163: *III°* [R4]
  - 163: *Quia* [R4]
  - 161: *decepisse* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 160:
9. Vide Trialogum lib. III, cap. I (ed. Lechler, pag. 128). Cf.
Arist. Eth. Nic. II, VI. graece, Opp. II, 1 106; latine, Opp. III, 544.
17. Aug. Retract. lib. I, Cap. IX; De Lib. Arbit. II, cap. XIX.
Opp. I, i3, 607.

p. 161:
10. A A, II. dcest. 12. veris ; ita codd. iX. B : pie incuciens. 20. A
in marg.: Arguitur quod Deus non potcst mentiri. 22. B sit decst. 25. A:
Cor. I. A, : I Cor. I. 2K. In Codd.: Thymotci II. 33. li : ct mensc-

p. 162:
5. B in marg. man. alt. : Misericors est Deus infinite, sed finite est
miserator. 8. B in marg. man. alt. : Jurat. 17. A in marg :
Conclusio. 20. B in mar^. mnn. alt.: Nota de non committcndo
mendacio. 23. A: thczauro; sic ct in sequentibus

p. 163:
.4. A in marg. : Augustinus. Nota. Pro mcndacio ohstitricum in Exodo et
contra. B in marg mnn. alt. : I)c obstetricum mendacio. 9. In codd.
non deest. Correxi cx Ang. In psalm. V. Opp. IV, p. iS. 10. Vcrba
Augustini I. c. : Scd eciam ista non re, sed indolc laudanlur. 19. Exodi
cap. scq. lacuna in codd.; addidi e hist. scol. Petri Comcstoris. A in
marg. : Magistcr historiarum. 20. Ap. Petrum Com. non de indole
sed de dolo leges.
18. Vide Petri Comest. hist. libri Exodi cap. III. (Ed. Argentina
i5t 5, fol. e, ?.) De Petro Com. Cf. Wyclifs Pol. Works II, pag. 454.
24. Moralium lib. XVIII, cap. III, Opp. tom. I, pag. 55g.
```

---

## Chunk 08-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-08-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-08-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "164.1–168.3"
divisions: "cap. 8 (heading 'CAP. VIII.' at 157.25); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1004 words; 912 unanimous or majority-real; 74 settled by vote (R2 42, R3a 21, R3b 1, R5a 9, R6a 1); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n201–n205 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 8, part 3: [TITLE]

## ¶1 · 164.1–166.15

> [p. 164] Unde in textu originalis beati Augustini inveni sic scriptum: ista non re, sed indole laudantur. Nec dubium quin sic habent libri correcti, tum quia magnus ille doctor Petrus Comestor intitulat capitulum suum De indole obstetricum, et sic loquitur sanctus Thomas secunda secunde q. CXª; tum secundo quia tunc textus Augustini diceret non in re, sed in dolo laudantur, nunc autem dicitur non re, sed indole laudantur; tum tercio quia dato hoc textu sic perverso adhuc militat in oppositum pervertentis, cum textus dicit quod non laudantur re. Certum est tamen quod in re fecerunt bonum opus de genere, quod fuisset virtuosum, si fuisset non infectum mendacio. Unde econtra est sentencia Augustini quod obstetrices laudantur in re vel opere, non autem in dolo quo regem mendaciter fefellerunt. Unde inveni in margine originalis beati Augustini sic scriptum: indolem vocat profectum; sicut enim est corporalis indoles corporaliter crescencium, sic est spiritualis indoles spiritualiter proiiciencium. Vult ergo Augustinus dicere quod ista verba mendacia obstetricum non laudantur in re mendacii, sed in profectu vel fructu qui exinde provenit crescencie Hebreorum. Est ergo sentencia Augustini quod Deus non posset sinere peccatum fieri, nisi exinde bonum proveniat; unde propter bonum exinde occasionaliter proveniens vocatur peccatum Ade a beato Gregorio necessarium atque felix. Et dicitur a beato Augustino expediens; unde XIV°, De Civitate Dei, cap. XIII°, sic scribit: Audeo dicere superbis esse utile cadere in aliquod apertum manifestumque peccatum, unde sibi displiceant qui iam sibi placendo ceciderant. Salubrius enim [p. 165] Petrus sibi displicuit quando flevit quam sibi placuit quando presumpsit. Sed per se notum est theologis quod non exinde peccandum est, quod bonum ex gracia Dei exinde proveniat. Unde credo quod peccatum publicum doctorum quo manifeste approbant mendacium ut virtutem, et mendax allegacio originalium, ut mendacio pallient dictum suum, vertetur ex gracia Dei illis in commodum, dum tamen in isto se corrigant et recognoscentes defectum suum humiliter resipiscant. Quis rogo aliter caperet eos in testimonium vel allegacioni eorum crederet, dum dicerent quod privatum commodum meritorium sit mentiri; revera nescio que opinio redderet hominem plus infamem. Quantum ad secundam evidenciam quod propter salvanda privilegia ecclesie sicut in casu qui nuper contigit meritorium sit mentiri, manifestum est quod dogma illud inficiendo privilegia redderet procuratorem ecclesie nimis suspectum; cum enim omne privilegium vel libertas sit fundatum in veritate que est sponsus ecclesie, manifestum est quod professione veritatis et non mendacii veritati oppositi defenderetur, dicente eadem veritate Joh. VIII°, 31, 32: Si vos manseritis in sermone meo, vere discipuli mei eritis, et vos cognoscetis veritatem, et veritas liberabit vos. Ex quibus patet cum fide scripture quod, de quanto orator ecclesie declinat a sermone Dei qui est veritas in verba mendacii que sunt sermones diaboli, ut sic se ipsum inhabilitat ad privilegia et libertates ecclesie procurandum; nam nulla talia dantur nisi per sponsum ecclesie, veritatem que odit omne mendacium. Ideo dicit Joh. VIII°, 34: Omnis qui facit peccatum servus est peccati. Nec dubium quin omnis faciens mendacium ut sic peccat, ideo mendacium est pessimum medium ad procurandum bona ecclesie. Nam mentitor ut sic offendit in naturam divinam a qua [p. 166] omne bonum profluit sponse Christi, et ut sic offendit in totam ecclesiam, quia contra hoc mandatum domini: Non loqueris contra proximum tuum falsum testimonium, Exod. XX°, 16, iniuriatur ut sic sancte matri ecclesie: ideo absit ecclesiam expetere huiusmodi oratorem. Nam secundum Augustinum super Psalmum Vᵘᵐ: Si hoc dicitur quod est, verum dicitur, et ut sic ad eum qui est acceditur; si autem hoc dicitur quod non est, mendacium Jit et a veritate receditur. Ideo dicit propheta: Perdes omnes qui loquuntur mendacium. Unde ne quis arbitretur perfectum et spiritualem hominem pro ista temporali vita in cuius morte non occiditur anima, sive sua sive alterius, debere mentiri, non inmerito in alio loco scriptum est: Os quod mentitur occidit animam.

[ENGLISH]

## ¶2 · 166.16–168.3

> [p. 166] Ex quo patet quod pro tota universali ecclesia salvanda nullus sapiens mentiretur, nam cum omne mendacium sit peccatum contra naturam, eo quod tota natura fuit pure in veritate sine mendacio primitus instituta, quis procuraret pro bono ecclesie per verba mendacia? Nonne domini seculares audientes quod per dogma falsum, quia per mendacium, sit privilegium ecclesie defendendum, ex naturali lumine statim convincerent quod totum privilegium sit mendax et frivolum quod indiget sic fulciri mendaciis? Nonne iterum audientes doctorem ecclesie dogmatizare publice quod privilegia ecclesie sunt per mendacia inpetranda, suspicarentur probabiliter quod tota suggestio qua impetrantur bona ecclesie sit mendax et falsa, et per consequens, omnia illa bona forent ex defectu fundamenti stabilis auferenda? Nonne tercio credens ecclesiam sic privilegiatam [p. 167] approbare mendacia diffideret quod ecclesia illa recipiens ex titulo elemosine a seculari principe bona huiusmodi sub condicione quod rependat spirituale suffragium, mentiretur in defraudando a promisso suffragio. Ideo ista opinio foret pessima ad bona ecclesie fideliter procurandum. Et eadem est consideracio de causis civilibus, quod inpossibile est ut mendacia illas vel contenciones aliquas legitime promoverent. Consideremus ergo quod Christus incurrebat aput sacerdotes, phariseos et scribas apparenciam diffamacionis, maxime ex hoc quod detegendo veritatem et reprobando eorum vicia purgavit ecclesiam et ut sic aquisivit sibi nomen quod est super omne nomen, superans quamlibet famam mundi. Sic nos christiani debemus tenere veritatem et privilegia ecclesie Christi defendere quantum sufficimus nec curare de fama alia, nisi de quanto adicitur ex virtute. Sed tercio notandum pro ulteriori declaracione privilegiorum ecclesie quod privilegium est privata lex, concessa a principe ad commodum ecclesie vel persone. Unde (si non fallor) omnis bona lex temporalis vel humanitus adinventa pro utilitate ecclesie vocari potest privilegium ecclesie, cum omnis talis lex sit privata quoad tempus et populum. Unde quod legiste vocant talia iura communia non obest quin sint privata, quia in communitate legum est dare quotlibet gradus, et lex privata potest crescere in communitate quoad tempus, locum et personam. Lex autem caritatis quam omnis homo debet semper et ubique tenere est ius communissimum sicut alie leges condicionales quas ipsa implicat. Addo eciam distinccionem ecclesie vel persone, quia si tantum esset una creatura racionalis privilegiata, tunc non privilegiaretur ecclesia. Privilegium ergo est specialis licencia [p. 168] creature utendi utibili vel fruendi fruibili, et illud speciale vel privatum licere est lex, ut patet in communi sermone de lege.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 164.21: Augustine does not praise the Egyptian midwives for lying.
- 165.14: To allow lying on behalf of the Church would make her advocates suspected;
- 166.20: and throw doubt on all her rights and privileges.
- 167.9: Christ spoke truth without regard to his reputation.
- 167.18: All laws made for the benefit of the Church may be called privileges, as being in some degree private laws.
- 167.29: The universal law is that of charity.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 164: *profectu* (leaf zoom: tall hooked f, not t) [R3]
  - 165: *Petrus* (151c is the folio mark) [R4]
  - 165: *privilegia* [R4]
  - 165: *in* [R3]
  - 166: *Christi* [R3]
  - 166: *16* [R3]
  - 166: *Vᵘᵐ* (superscript um after V (Psalmum Vᵘᵐ)) [R4]
  - 166: *per* (round p) [R3]
  - 166: *privilegiatam* (main token holds the whole word privi-/legiatam; glued 3 is the bold argument numeral) [R4]
  - 167: *suffragio* (5 is the line number) [NW]
  - 167: *Christus* [R3]
  - 167: *Christi* [R3]
  - 167: *legiste* (print spelling) [NW]
  - 168: *creature* [R3]
  - 164: *textu* [THIN]
  - 164: *beati* [THIN]
  - 164: *inveni* (v as printed) [THIN]
  - 164: *sic* (151b folio mark and alinea E glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 164:
8.9. B: nunc— latidantur: deest. 3o. A in mar<;. : Nota Augustinum,
qnod utile est in casu pcccarc.
2. Aug. ut supra, Opp. tom. IV, p. iR. 6, Thomas Aq. Opp. (Ed.
Venet. 1774) tom. IV, p. 3n. 20. Aug. I. c. Opp. VII, pag. 366 A.

p. 165:
4. A in marg. : Conclusio. u. 12. A,add.: quod propter privatum.

p. 166:
0. A in marg. : Augustinus. i>. Aug. 1. c. : Si cnini Ijoc dicitur
quod est, verum dicitur, si aulcm hoc dicitur quod non cst, mendacium
cst. 23. B.: ex natura lumine. 23. li: convinccret. Reclius :
convincerentur.
7. Aug. 1. c. Opp. IV, p. I, p 18. 9. Psalm. V, 7.
16. Sap. I, 1 :.

p. 167:
18. A, Sed ultcrius. ig. A in marg : Quid cst privilegium ?
22. A. iu marg. : Omnis lex humanitus adinventa utilis est privilegium.
25. A,: quod iuriste. 32. distinctim in codd.

p. 168:
1. B: et fruendi. Codd.: usibili. 2. A A, patet deest. 7. A
in marg. : Nota de privilegiis ecclesie continue infra (Abovc i52° withont
mark of reference). i5. B: ut deest. 16. A: et ss. (literae ss.
extinct.). 28. Racionale sive racionabile; codd.: racio'".
```
