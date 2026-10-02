# Translation brief: ecclesia 17-h–18-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-17-h.md chunks/ecclesia/wyc-ecclesia-18-a.md chunks/ecclesia/wyc-ecclesia-18-b.md` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.

Standing rules (from the *De ecclesia* briefs, 2026-10-02):
- Do NOT search the Patrologia or other sources; a separate checker verifies them afterwards. Give the
  editor's reference, the modern form in the English, and "to be checked" with a fresh LEDGER id per item
  (never reuse an id).
- Notes open with their bold class codes, `**S/C.**`, never bare letters mid-note. No process words in
  the notes ("the report", "the coordinator", "brief").
- OCR scars (stray English or margin letters, line numbers read as words, glued or broken words,
  numerals read as letters) stay out of the chunk: translate the print's word and list each scar in your
  final message only (page.line, token, likely print reading). The coordinator fixes the Latin.
- Flag every place the established Latin may have LOST a word (it does not construe, especially at a page
  head or foot) or DOUBLED one: page.line and the suspicion. Translate the print as it stands; supply a
  missing word only in brackets with a T note. The editor's print governs; list any departure.


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

## Glossary (the 151 rows these chunks use; the full file is GLOSSARY.md)

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
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| viacio | wayfaring | The state of the *viator*. Ruled 2026-10-02 (42.30). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| digestio | digestion | The recurring figure of the four digestions (Rom. 8:30). Ruled 2026-10-02 (60.29 ff.). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| ociatores | men of leisure | Ruled 2026-10-02 (201.27). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |

---

## Chunk 17-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "412.15–415.7"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "671 words; 610 unanimous or majority-real; 48 settled by vote (DEL 1, R2 22, R3a 22, R6a 3); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n449–n452 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 8: [TITLE]

## ¶1 · 412.15–415.7

> [p. 412] Sed videamus fel commixtum cum mellis dulcedine. In morte (inquit) Christi cepit esse ecclesia, a qua morte sacramenta sumpserunt efficaciam. Patet ex dictis in prima responsione et secunda quomodo error iste nedum tolleret honorem sancte matris ecclesie ex sua antiquitate fundata in fide scripture, sed innuit interempcionem meriti matris nostre et tollit fidem patrum veteris testamenti dehonorando sanctam matrem ecclesiam. Item manifeste responsio obviat sibi ipsi, quia ante mortem Christi fuit ita quod est multitudo omnium christianorum habencium ex integro rectam et eandem fidem per Christum et suos apostolos promulgatam et a sanctis patribus in conciliis generalibus declaratam, ut declaratur in responsione. Ideo ante mortem Christi fuit ita quod est ecclesia. Non enim incepit ecclesia in triduo, quando dicitur [p. 413] Christum non esse, nec sapit incarcerantibus presens tempus quod a morte Christi sacramenta sumpserunt suam originem, sicut patet querendo que sacramenta et quando sumpserunt a dicta morte originem. Nec valet alia responsio qua dicitur quod descripcio predicta ecclesie non compeciit ecclesie in sancto triduo, tum quia tunc descripcio non valeret que tam cito deficeret in floribus ecclesie primitive, tum secundo quia iuxta declarata descripcio ecclesie compeciit christianis ante mortem Christi et per idem in sancto triduo. Non ergo deserenda est tam cito dicta descripcio, cum in fine adicitur quod stabit non obstantibus meis obiectibus in eternum. bed revera fingere descripcionem per quam excluderetur a racione ecclesie tam sanctum apostolorum collegium cum suo abbate pro toto tempore sue viacionis videtur presumpcio, cum presciti dicuntur esse de sancta matre ecclesia et in principio mundi ante creacionem hominis sicut et lapsis ambobus parentibus fuit ecclesia (ut patet Encheridion LXIV°). Ulterius respondendo ad quintam raciunculum dicitur! quod sicut continue manet eadem species hominum non obstante quod individua variarentur, sic manet continue eadem universalis ecclesia non obstante quod membra alia generentur et alia corrumpantur. Sic (inquit) manebit idem homo in numero non obstante quod partes equales alie generentur et alie corrumpantur. Quare rogo non sic erit de corpore Christi mistico quod est ecclesia? Et revera illud est bene dictum dummodo consequenter. Oportet enim ecclesiam catholicam esse unam personam sponsam et non formaliter speciem vel universale quod sit multorum singularium, sed [p. 414] est una persona successiva a principio mundi usque ad diem iudicii, et post habebit illa persona omnia eius membra, simul perpetuo beata et illius persone nunc una pars est militans et nunc alia, sed sicut nulla pars est reliqua, sic tota illa ecclesia non est pars eius aliqua sed una totalis et gloriosa incommunicabilis persona. Non enim capit ingenium humanum quod iste pauce persone militantes quas falsarius vocat universalem ecclesiam sint alie persone coniunctim vel divisim, ymmo ad alietatem cuiuscunque simplicis persone sequitur alietas multitudinis que ipsam personam caruerit a multitudine que ipsam personam tamquam partem habuerit. Ideo illa ecclesia catholica que durat a principio usque in finem mundi non est persone vel multitudo fidelium que nunc est secundum se totam, sed illa multitudo est pars illius ecclesie catholice que est in magno tempore et semper post diem iudicii, sed in nullo instanti temporis est per totum ante novissimum electum nec in aliqua parte talis temporis, et talis ecclesia augeri potest sed non minui, non quod eadem multitudo predestinatorum in numero sit nunc plures homines et nunc pauciores, sed quod idem commune ad sanctam totalem ecclesiam militantem sit nunc maius et nunc minus, sicut loquitur scriptura Act. VI° de crescente numero discipulorum. Sicut ergo idem tempus in numero non maioratur vel minoratur, sic nec eadem ecclesia in numero nisi accipiendo ecclesiam communiter pro capite et quacunque multitudine totali membrorum suorum. Sic enim maioratur ecclesia, ut homo stante unitate capitis ut anime. Sed ista veritas necessitat ad ponendum quod omnia que fuerunt vel erunt sunt pro suo tempore causancia unum integrum, cuius pars est pro parte temporis totalis [p. 415] ipsum integrum mensurantis. Et sic concedi potest quod ista nunc sunt, demonstrando omnia que fuerunt vel erunt, intelligendo parcialiter collective. Sed coloracius quoad logicam concedi potest quod hoc totum existens ista est nunc sed non ista, quia tunc infinita instancia forent simul in eodem instanti (de qua logica patet alibi).

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 412.18: This is true but the error lies in asserting that the Church began at the death of Christ.
- 412.29: The Church cannot have begun in the three days.
- 413.5: My opponent says that his definition does not apply to the Church in the three days.
- 413.11: This is an early desertion of a definition which, he declares, will stand for ever.
- 413.21: 5. My opponent urges that the whole may continue while the parts vary.
- 414.4: The Church does not consist of successive parts,
- 414.16: since it loses none, but goes on increasing till it has gathered in all the elect,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 412: *∅* (dulce-/dine.: main pos 105 already holds dulcedine., so this second-half token is empty (hyphen convention)) [DEL]
  - 412: *Christi* [R3]
  - 412: *fundata* (clear f) [R4]
  - 412: *fide* (clear fi) [R3]
  - 412: *meriti* (clear ri) [R3]
  - 412: *incepit* (clear in) [NW]
  - 412: *triduo* [R5]
  - 413: *Christi* [R3]
  - 413: *variarentur* (clear ri) [R3]
  - 413: *Christi* [R3]
  - 414: *alietas* (print reads alietas) [NW]
  - 414: *iudicii* [R4]
  - 415: *ipsum* (alinea Q and 186b folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 412:
2. B in marg. : Quatuor consilia apostolorum et quatuor fuerunt
solempnes sinodi, ut patet XVI. dist. Omnibus. 2. B: XV.
10. B: potest deest. i5. A in marg.: Contra hoc quod dicitur
quod ecclesia incepit post mortem Christi. 19. B: honorem dcest.
20. 21. A A,: sed innuitur.
2. Dist. XV vel XVI. Omnibus non extat. Cf. pp. 388, and 3g8.

p. 413:
1. incarcerantibus ; ita codd. 17. B in marg. : Ante lapsum
primorum parentum erat ecclesia. 20. A in marg.: Quinta responsio.
20. LXIV°; recte LVII. 23. B: individua — quod deest. 3o. A in
marg. : Ecclesia quid est? B in marg. : Ecclesia est una persona successiva.

p. 414:
18. B: sed in illo instanti. 19. 20. B: vero in aliqua. 23. A A,
secundum quod idem.

p. 415:
2. B: ista autem sunt. n. A in marg.: Prima responsio. An
presciti qui habent fidem sint de ecclesia et predestinati in mortali sint
tunc extra ecclesiam. 19. A in marg.: Sanctus Thomas.
11. Cf. p. 114, 1. 23. 20. Sancti Thomae Aq. Comment.
in tercium Iibr. Sent. dist XIII, q. II, Solutio. Opp. tom. IX, pag. 1 56.
```

---

## Chunk 18-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "415.9–418.1"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 1 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "585 words; 519 unanimous or majority-real; 56 settled by vote (R2 28, R3a 22, R5a 4, R6a 2); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n452–n455 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 1: [TITLE]

## ¶1 · 415.9–418.1

> [p. 415] Ulterius restat approbando veritatem et reprobando falsitatem transcurrere per responsiones ad alias quinique raciunculas que supersunt. Prima autem respons dicit, primo quod omnes presciti renati baptismate sunt membra sancte ecclesie catholice; secundo dicit quod nulli predestinati errantes a recta fide sunt membra sancte matris ecclesie, et tercio dicit quod nec Petrus nec Paulus nec David nec aliquis alius pro tempore pro quo deviat a recta fide est pars ecclesie catholice. Ista est venenosa triplicitas: prima tamen suadetur est sentencia sancti Thome super III° Sentenciarum dist. XIII, q. IIª, dicentis quod, sicut in corpore naturali membra uniuntur et sunt unum per colligacionem quandam nervorum et iuncturarum, ut fiant unum continuacione, sic (inquit) in corpore Christi mistico omnes qui colligati sunt ad invicem per fidem rectam sunt unum in corpore ecclesie; et sic infidelis non pertinet ad unionem corporis ecclesie quod est unum simpliciter, nec paganorum, hereticorum et separatorum ab ecclesia est Ghristus proprie [p. 416] caput nisi in potencia. Ista autem verba non faciunt pro supradicta sentencia, cum solum predestinati colligati sunt per fidem rectam, eo quod omnes alii continue peccato indelebili peccant mortaliter, et sic sunt perpetuo heretici qui soli simpliciter separantur a corpore Christi mistico. Sed quod dicitur sanctum Thomam in solucione ad tercium argumentum plane dicere quod presciti existentes in gracia sunt vera membra ecclesie, sicut manus abscindenda est membrum, quousque fuerit actualiter abscisa, dicitur quod hoc debet intelligi de ecclesia secundo modo dicta, ut includit granum et paleam; que ecclesia secundum Augustinum III° De Doctrina Christiana XXXII° non est corpus domini nec eciam corpus domini bipertitum, et sic presciti baptizati habent secundum presentem iusticiam incorporacionem in illa mixta ecclesia et quandam adnascenciam cum vera ecclesia, sicut habet stercus in venis miseraicis, sed nunquam sunt pars corporis Christi; et ista est sentencia Augustini epistola XXXIIª ad Bonifacium. to Quantum ad secundum errorem, patet quod capit instanciam de omnibus predestinatis a fide errantibus qui quamvis a fide ad tempus devient, Deus tamen ex eleccione predestinacionis eos semper eque diligit. Et hinc dicit Christus Johannis X, 16: Alias oves habeo que non sunt ex hoc ovili et vocem meam audient. Super quo textu notat Augustinus super Johan. Omelia XLVª quomodo Christus dicit se habere oves de gentibus adhuc convertendis; hec, inquit, secundum [p. 417] predestinationem dicta sunt. Ideo (ut dixi superius) ponit Ricardus de Sancto Victore tres gradus membrorum ecclesie. Quamvis autem predestinati deficiunt a fide et gracia secundum presentem iusticiam, habent tamen fidem infusam secundum graciam predestinacionis. Si ergo secundum doctorem prescitus existens in mortali secundum fidem infusam sit membrum sancte matris ecclesie, licet omne peccatum mortale concommunicetur infidelitas, multo magis omnis predestinatus foret membrum sancte matris ecclesie. Ad aliam raciunculam primo dicitur quod non est eadem racio ecclesie militantis et ecclesie triumphantis secundo dicitur quod ecclesia triumphans infinitum distat in perfeccione essenciali ab ecclesia militante; tercio dicitur quod nullo modo est una ecclesia ex hiis, cum tantum differunt sicut substancia et accidens que non sunt unum aliquo modo. Et ista dicitur esse sentencia Augustini, Epistola XXXII, ad Bonifacium, ubi distinguens inter ecclesiam militantem et triumphantem ponit ecclesiam triumphantem esse sine macula vel ruga, triumphans autem est immunis ab omni culpa. Isti tres errores sunt manifestiores prioribus, quia equus cecus continue profundius sese Iprecipitat. Nam quoad primum utraque est univoce ecclesia, ideo oportet quod sit eadem generalis racio utriusque. Quoad secundum patet, cum ecclesia militans erit ecclesia triumphans, contradiccionem claudit quod infinitum distent in perfeccione essenciali; eedem enim persone que iam sunt ecclesia militans erunt ecclesia triumphans (ut patet ex fide). [p. 418] Quoad tercium errorem patet ex testimonio sanctorum

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 415.9: 6. Our opponent says a) the foreknown when baptized are members of the Church, b) the predestinate erring from the faith are not members, c) as neither were the Saints, while in error.
- 416.1: He alleges the authority of St. Thomas,
- 416.6: but St. Thomas was using "Church" in our second sense (see p. 409).
- 416.21: Authorities to show that the predestinate are members even when in error.
- 417.12: My opponent says a) there is a difference in nature between the Church militant and triumphant; b) they differ infinitely in essencial perfection; c) they do not form one Church.
- 417.24: But a) since both are the Church, they are alike in nature; b) those who now make up the militant will be the triumphant Church.
- 418.1: c) the Saints testify that the body of Christ is made up of the Church militant, dormant, and triumphant.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 415: *CAP. XVIII.* [HEAD]
  - 415: *sunt* (2 is a margin argument numeral) [R4]
  - 415: *III°* [R4]
  - 416: *III°* [R4]
  - 416: *XXXIIª* [R4]
  - 416: *XLVª* [R4]
  - 417: *secundo* (2 is a margin argument numeral) [R3]
  - 417: *racio* (print has whole racio; side-note overlaps line end) [NW]
  - 417: *utriusque* (2 is a margin argument numeral) [R4]
  - 415: *IIª,* [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 415:
2. B: ista autem sunt. n. A in marg.: Prima responsio. An
presciti qui habent fidem sint de ecclesia et predestinati in mortali sint
tunc extra ecclesiam. 19. A in marg.: Sanctus Thomas.
11. Cf. p. 114, 1. 23. 20. Sancti Thomae Aq. Comment.
in tercium Iibr. Sent. dist XIII, q. II, Solutio. Opp. tom. IX, pag. 1 56.

p. 416:
5. A: seperantur. i3. A in marg.: Augustinus. 16. A in
marg. : Nota quomodo presciti sunt in ecclesia et tamen nunquam sunt
pars ecclesie. 18. A,: meseraicis. 23. A in marg. : Prede-
stinatus carens fide est de ecclesia. 28. In codd.: Omelia XLIX;
A in marg. : Augustinus.
i3. vid. sup. pag. 4. 20. Not epistola XXXII, but XCVIII
(alias XXIII). Opp. II, pag. 263. 23. Cf. Wyclif, De Civili
Dominiol, cap. II, p. i5. 28.Aug. Opp. tom. III, parsll, pag.600.

p. 417:
8. B: licet — ecclesie deest. 12. A in marg. : Secunda responsio.
Tres errores. 24. B: profundus. 25. A in marg.: Contra illos
2. Richardus, De Potestate Iigandi et solvendi, pars II, cap. XX
(ed. Migne pag. 1172). 1 2. Compare p. 114, 1. 3i. iq. Aug.
Opp. tom. II, pag. 658.

p. 418:
3i. B: et fundamento. 35. Unde; nude (?).
```

---

## Chunk 18-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "418.2–422.18"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 2 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1086 words; 938 unanimous or majority-real; 127 settled by vote (DEL 1, R2 78, R3a 41, R3b 1, R5a 4, R6a 2); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n455–n459 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 2: [TITLE]

## ¶1 · 418.2–420.18

> [p. 418] ecclesia quod est unum corpus Christi misticum compositum ex ecclesia militante, dormiente et triumphante, sicut allegatus est superius Augustinus, Encheridion LXIV° cap- LXV° cap. et LXIX° cap., et in De Questionibus veteris et nove legis cap. XLVII°. Non ergo tantum differunt sicut substancia et suum accidens, cum utraque ecclesia dicitur substancia eiusdem speciei specialissime, quia homo; ymmo secundum philosophos substancia et accidens sunt unum aliquo modo, quia unum per accidens, sicut oportet doctorem dicere de personis ecclesie et fide qua ille persone sunt formaliter ecclesia. Et quantum ad evidenciam captam ex testimonio Augustini, patet quod inducit ignoranciam arguentis. Nam verum est (ut sepe docet Augustinus ex fide scripture) quod ecclesia est maculata et rugosa dum militat, sed omnino sine mortali vel veniali dum triumphat. Sed omnino dementis foret ex istis arguere diversitatem specificam illarum ecclesiarum, vel quod non fit una ex illis, vel quod una infinitum excedit aliam in perfeccione essenciali. Nam beatus viator et dampnatus sunt eiusdem speciei specialissime, componunt unum genus humanum et sunt pares in perfeccione essenciali; et tamen sunt illius condicionis quod inferior est plenus macula et rugosus, et secundus est omnino sine macula vel ruga. Accidens ergo non variat tantum unam substanciam ab alia. Nec valet dicere quod est dare unum aggregatum ex substancia et accidente, ut puta ex habitu fidei infuso et substancia aggregatis, tum quia negatur talis unitas in fundamento responsionis, tum eciam quia talis habitus fidei manens perpetuo migraret de subiecto in subiectum et reciperet peregrinas predicaciones formales alienas a natura universalium, unde in confirmacionem supradicte sentencie. [p. 419] Et contra istam sentenciam pertinenter notandus est Cardinalis in VI°, De Eleccionibus, cap. Fundamenta. Pertinenter dico, primo quia cardinalis, secundo quia papa et tota curia approbavit suam sentenciam in hac parte, et tercio ex affeccione nominis et cognominis, cum fuit Johannis Monachi. Scribit enim primo describendo ecclesiam quod est convocac fidelium, quia omnes fideles ad se vocat, cum extra illam unicam non sit salus; hec quandoque dicitur militans et quandoque triumphans: Non, inquit, quia sunt due, sed una, habens diversas qualitates. Intendit autem doctor quod non sunt due ecclesie catholice, sed una tantum, habens duas partes solum per accidens differentes. Ideo subdit: prima est secundum Augustinum in tempore peregrinacionis, altera determinante mansionis, prima in labore, altera in requie, prima in via, altera in patria, prima cum hoste pugnat, altera sine hoste regnat; et hinc prior ecclesia dicitur militans et secunda triumphans. Nam Job VII°, 1 scribitur: Milicia est vita hominis super terram, et Apostolus IIª Thymotei II°, 3: Labora sicut bonus miles Christi Jesu. Oportet enim in via laborare certando contra carnem, mundum et demonem; sed homo superando fit victor et consummata victoria fugatis hostibus fit per Dei graciam triumphator. Et allegat pro modo loquendi leges multiplices. Secundo dicit quod hec ecclesia militans est corpus Christi misticum 111 quo congregantur fideles. Et inter illos eciam sunt [p. 420] infideles, ut allegat per leges multiplices, sed ecclesia triumphans tantum habet bonos, quia in illa non est macula mortalis neque ruga venialis (ut patet De Penitencia, distinccione prima, capitulo Ecclesia), et huius corpus scilicet ecclesie militantis caput est Christus ut sponsus. Et hec ecclesia militans fiet triumphans post resurreccionem universaliter, et cotidie fit triumphans in membris particulariter, ita quod ecclesia militans est sponsa, sed ducta in domum sponsi universaliter vel in suis membris fit uxor. Unde Apoc. XXI°, 9, dixit angelus beato Johanni: Veni et ostendam tibi sponsam, uxorem agni. Sic, inquit, reperio quod illa que est sponsa mariti ducta in domum efficietur uxor, Digestis, De Ritu Nuptiarum, Minorem. Et sicut hoc exemplo eadem mulier primo est sponsa et per qualitatem duccionis adiectam fit uxor, sic ecclesia militans vel anima fidelis hic sponsa Christi ducta in celestem Jerusalem uxor censebitur.

[ENGLISH]

## ¶2 · 420.19–420.26

> [p. 420] Istam celestem legem de articulo fidei a scriptura sacra per sanctos doctores et doctores iuris canonici elaboratam addiscerent legiste precipue et omnes catholici. Christus, inquit doctor, dicitur lapis angularis, duos parietes connectens adinvicem, quia ab Abel iusto in veteri testamento usque ad novissimum electum in fine seculi fideles connectit, constituendo ecclesiam, continue manens summus.

[ENGLISH]

## ¶3 · 420.27–422.18

> [p. 420] Ex istis tercio patet destruccio erroris triplicis supradicti. Nam dicte differencie inter ecclesiam militantem et triumphantem non sunt differencie substanciales, sed valde accidentales, quia aliter nulla ecclesia militans foret triumphans; quod est contra predicta [p. 421] et contra totam speciem militantis ecclesie. Si enim ista multitudo erit ecclesia triumphans, et ista multitudo est ecclesia militans, infallibiliter sequitur quod ecclesia militans erit ecclesia triumphans. Ex quo patet quod non differrent perfeccione essenciali excessu infinito, sicut substancia et accidens, et, si nemo militans Deo post victoriam triumphabit, periret ab ecclesia animus militandi contra scripturam IIª Tim. IV, 8: De reliquo reposita est mihi corona iusticie quam reddet mihi in illa die iustus iudex; non quod nulla ecclesia est triumphans vel beata ante diem iudicii, sicut fingunt heretici, sed ut dicit Cardinalis particulatim: sicut spiritus transeunt ad gloriam, sic erunt ecclesia triumphans que quondam fuit militans. Ex quo secundo sequitur quod spiritus hominis est eadem persona cum homine, quia ecclesia que est modo militans, hoc est, multitudo personarum fidelium erit triumphans in. nudo spiritu; aliter enim non diceret Apostolus ad Philippenses 1°, 23: Desiderium habens dissolvi et esse cum Christo, sicut diffuse et pulchre declarat Hugo, De Sacramentis, parte prima libri secundi, cap. XI°, in quo diffuse declarat quod Christus separata anima a carne et persona fuit et Deus et homo, ubi inter alia sic scribit: Anima quippe in quantum spiritus est racionalis ex se et per se habet esse personam, et quando corpus ei sociatur, eadem cum ipsa persona esse incipit; in quantum enim corpus cum anima unitum est, una persona cum anima est, sed tamen personam esse anima ex se habet, in quantum est racionalis spiritus, corpus vero hoc habet ex anima, in quantum unitum [p. 422] est racionali spiritui. Istam autem materiam diffuse exposui in quodam tractatu De Anima, ubi ostendi quod anima, corpus et compositum sunt tres res sed idem homo in numero. Et idem expresse dicit venerabilis Anselmus in De Incarnacione cap. VII° quod, sicut in materia de trinitate multe persone sunt una substancia, sic in materia de incarnacione multe substancie vel nature sunt una persona. Et beatus Bernardus in Sermone De Nativitate qui sic incipit Hodie scietis quia veniet dominus. Attende, inquit, quia sicut in illa singulari divinitate trinitas est in personis, unitas in substancia, sic in ista speciali conmixcione incarnacionis trinitas est in substanciis, in persona unitas, utrobique tamen sine scissione vel confusione substancie vel persone. Verbum enim et anima et caro in unam convenere personam, et hec tria unum et hec unum tria non confusione substancie sed unitate persone.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 418.17: There are defects in the militant Church that are not in the triumphant, but this does not make a specific difference.
- 419.1: Description of the Church given by Cardinal John:
- 419.6: a) it is the assembly of all the faithful, and has two parts, militant and triumphant;
- 419.26: b) in the militant Church there are wicked, but in the triumphant only the good.
- 420.27: Hence we see that the differences between militant and triumphant are not essential, but accidental,
- 421.8: and as spirits pass to glory they become part of the Church triumphant.
- 421.15: The spirit is the same person as the man.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 418: *in* [R3]
  - 419: *∅* (inserted run is the end of p.418 already in the main scan; p.419 begins Et contra istam) [INS?]
  - 419: *istam* [THIN]
  - 419: *primo* (1 is a margin argument numeral) [R4]
  - 419: *fidelium* (italic) [R4]
  - 419: *1* (italic x-height numeral with no cap height = old-style 1 (leaf zoomed)) [R3]
  - 419: *congregantur* (italic) [THIN]
  - 419: *inter* [THIN]
  - 419: *illos* [THIN]
  - 420: *Christi* [R3]
  - 420: *scriptura* (alinea E at the edge, not text) [R3]
  - 420: *legiste* (print reads legiste) [NW]
  - 420: *∅* (see is the English side-note (Hence we see)) [INS?]
  - 420: *predicta* (pre- here, dicta at top of p.421 with 187 folio mark; main token holds whole word, p.421 pos 0 is et) [THIN]
  - 421: *IIª* [R3]
  - 421: *iustus* [R4]
  - 420: *∅* ('umphans' already inside neighbour 53 triumphans) [DELX]
  - 418: *Encheridion* (Enche-/ridion; ridion absent from output (next token LXIV), so whole word) [OVERRIDE-MARK]
  - 418: *LXIV°* (no comma; followed by cap.) [OVERRIDE-MARK]
  - 419: *IIª* (italic, superscript a) [OVERRIDE-MARK]
  - 420: *ecclesia* (eccle-/sia; output holds both halves; 30 is the line number) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 418:
3i. B: et fundamento. 35. Unde; nude (?).

p. 419:
1. A in marg. : Cardinalis. Nota distinccionem inter ecclesiam militantem
et triumphantem ; et ecclesia militans quomodo est hic sponsa et in celis
est uxor (Above 186'1 without mark of reference). 8. B in marg. :
Nota quid est unica ecclesia catholica tantum. i5. B: in tempore
peregrinacionis deest. 28. B: in marg. : Ecclesia militans est corpus
Christi misticum.
2. Sexti Decret. lib. I, tit. VI, cap. XVII. 6. De Johannis
Monachi (f i3t3) glossa in Sextum cf. Savigny 1. c. VI. io3,
419. Jocher. Gelehrtenlexicon II. iq33.

p. 420:
6. A in marg. : Conclusio. n. In codd.: Apoc. XIX. 16. B:
a directa fit. 17. B: fidelis huius. 22. A in marg. : Quomodo
Christus est lapis angularis. 24. B: testamenti. 3t. A in
marg. : Ecclesia nunc militans postea erit triumphans.
4. Decr. II pars, causa XXIII, q. III, cap. LXX. 14. Bigg.
lib. XXIII, tit. II, De Ritu Nuptiarum 4.

p. 421:
i5. A in marg.: Spiritus hominis est cadem pcrsona cum homine.
21. A in marg. : Hugo. B in marg.: Quod homo est anima sua.
26. et 2y. in codd. persona; corr. e tcxtu Hugonis 1. c.
21. Hugonis de S. Victore, De Sacram, lib. II, p. I; cap. XI
(ed. Migne pag. 409).

p. 422:
3. B: tres nature sed. 5. A in marg.: Anselmus. 7. A A,:
vel substancie. g. A in marg. : Bernhardus. 14. In codd.: per-
sonis; A in marg. : persona, ut habetur in textu. S. Bernhardi. 19. A in
marg. : Tercia responsio. 25. A in marg. : Ecclesia est diffusa per
totum orbem et per maiorem partem orbis non est ecclesia.
5. Anselmi, De Fide Trinitatis Opp. pag. 479 Bernhardi
in vigilia Natalis Domini. Sermo III. Opp. 1. c. pag. 41.
19. Compare p. 11 5, 1. 1.
```
