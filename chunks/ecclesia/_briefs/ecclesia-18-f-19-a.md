# Translation brief: ecclesia 18-f–19-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-18-f.md chunks/ecclesia/wyc-ecclesia-18-g.md chunks/ecclesia/wyc-ecclesia-19-a.md` once and fix what it reports.
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

## Glossary (the 182 rows these chunks use; the full file is GLOSSARY.md)

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
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |

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
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| cantaria | chantry | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |

---

## Chunk 18-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "435.26–438.26"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 6 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "766 words; 700 unanimous or majority-real; 49 settled by vote (INS 2, R2 29, R3a 14, R3b 1, R5a 3); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n472–n475 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 6: [TITLE]

## ¶1 · 435.26–436.18

> [p. 435] iqua pars eius haberet proprie possessiones, cum non sit proprie unum totum vel aliquid, nec quisquam foret in ecclesia vel de ecclesia. Non enim in ecclesia, quia sic foret pars datorum fidelium, et sic omnes componerent aliquod unum corpus; nam si sufficit ad esse hominis vel alterius rei esse de aliquibus quod sit de numero illorum, tunc quidlibet foret de mundo et omnis prescitus vel predestinatus foret tam de prescitis quam predestinatis et quelibet [p. 436] multitudo de qualibet, et sic (ut sophiste arguunt) aliquis numerus non haberet partem vel partes ut numerus indivisibilium; aliquis autem est numerus qui habet partes et non partem, ut numerus rerum divisibilium non communicancium, aliquis vero est numerus qui habet partes et partem, ut Petrus et caput suum. Deliramenta sunt ista sophismata et modo loquendi philosophorum contraria de populo, exercitu et aliis artificialibus, sed specialiter sunt contraria scripture et sanctis doctoribus. Oportet ergo omnem talem multitudinem habere partes (sicut patet ad sensum). Nam videndo silvam, populum vel arenam videtur aliquid distincte secundum pyramidem radialem cuius basis terminatur ad multitudinem, et constat quod in casu non sic videtur una simplex pars talis multitudinis sicut nec videtur punctus vel linea. Ideo relinquitur quod talis multitudo divisibiliter videatur, sicut habet operaciones proprias et est obiectum multorum actuum.

[ENGLISH]

## ¶2 · 436.19–438.18

> [p. 436] Et confirmacio huius est quod continuacio non est nisi accidens, non faciens substanciam esse aliquid et per idem sequitur quod vocata religio vel ritus humani non faciunt personas esse substanciam postquam erant non substancia, nec capit sensus dispositi quod conventus tam sensibilis tam edax et tam multipliciter operativus sit indivisibiliter multiplicatus, ut quiditas hominis, nec negabitur quin talis conventus sit ecclesia particularis; et si sit nichil, tunc mutari potest per hominem ab aliquo in non aliquod et econtra. Et est obiectum sensus subiectumque accidentis, et tamen non est res obiecta vel subiecta, quod est contra grammaticam. Foret eciam omnino sine peccato vel gracia, quia nullum tale vel accidens sibi inesset a pari nulla pars vel denominacio sibi inesset, et tunc ecclesia ex tribus hominibus et tribus angelis in nulla proporcione se [p. 437] haberet ad aliquam partem sui, quia sic una medietas foret indivisibilis et alia medietas quantitativa foret equalis suo toti, si debeat dici totum; et sic illud totum haberet quatuor medietates inequales, ut ecclesia ex quatuor hominibus inequalibus haberet duos minores homines et quatuor medietates quantitativas illorum quatuor hominum pro suis medietatibus, et sic in quacunque proporcione volueris una medietas est maior reliqua. Et mirum videtur quod pars, medietas, mundus et maior pars rerum artificialium sit nichil, nam scriptura ita Johannis V° dicit spiritum, aquam et sanguinem esse unum, et communiter patet idem de aliis aggregatis que dicuntur unum. Nam predicato per se inferiori predicatur per se superius, ut si ecclesia sit persona, tunc est racionalis nature individua substancia. Redeundo ergo ad propositum notandum est fideli quod diligenter caveat ab heresi ista recenti qua dicitur quod ante mortem Christi non fuit sancta mater ecclesia nec quod ex militante et triumphante est una totalis ecclesia constituta sed quod presciti et membra dyaboli sunt partes sancte matris ecclesie, domus Dei et speciale habitaculum trinitatis, quia (ut sepe assumpsi) Augustinus in Encheridion LVI° exponens fidem ecclesie super ista particula Sanctam ecclesiam catholicam ita scribit: Rectus itaque confessionis ordo poscebat ut trinitati subiungeretur ecclesia tamquam habitatori domus sua et Deo templum suum et conditori civitas sua; que tota hic accipienda est non solum ex parte que peregrinatur in terris a solis ortu usque ad occasum laudans nomen domini et post captivitatem vetustatis cantans canticum [p. 438] novum, verum eciam ex illa que in celis semper ex quo condita est cohesit domino nec ullum malum sui casus est experta hec ecclesia in sanctis angelis beata persistit et sue parti peregrinanti sicut oportet opitulatur, quia utraque una erit eternitatis consorcio et nunc una est vinculo caritatis. Iste sanctus episcopus condidit ecclesie libellum quem vocavit Manuale ad finem quod fideles recte intelligant fidem suam, ubi quoad primum articulum notat quomodo immediate post eternitatem trinitatis increate hoc est, in mundi principio secuta est sancta mater ecclesia in qua sit trinitatis habitacio et expresse duas partes illius totalis ecclesie scilicet celestem et terrenam commemorat. Unde, ut spes nostra in ista fide catholica confirmetur, ordinatur in ympno ecclesie quod postquam nulla nostra in Christo accepit cesivam in celo, et angelus conservus hominum prohibuit se adorari a Johanne, Apocalypsis penultimo, ut sic caveant fideles peregrinantes a domino:

[ENGLISH]

## ¶3 · 438.19–438.19

> [p. 438] Triumphat ille splendide

[ENGLISH]

## ¶4 · 438.20–438.20

> [p. 438] Et dignus amplitudine

[ENGLISH]

## ¶5 · 438.21–438.21

> [p. 438] Soli polique patriam

[ENGLISH]

## ¶6 · 438.22–438.26

> [p. 438] Unam facit rempublicam, quasi diceret: Caput ecclesie Christus, Deus noster est dignus ex merito passionis sue habere civitatem tam amplam, que sit totalis ecclesia facta ex ecclesia militante in solo et triumphante in polo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 435.30: nor could any one be in or of the Church.
- 436.12: A multitude has parts as our sense tells us.
- 436.19: It is impossible to believe that a convent is an indivisible unity (like the quidity of man); it would have to be an object and not an object
- 436.31: and could have neither sin nor grace.
- 437.9: Thus we should be brought to the wonderful conclusion that almost all things are nothing.
- 437.17: The faithful must beware of the heresy that there was no Church until the death of Christ.
- 438.7: Augustine teaches that the Church is from the beginning of the world and that it consists of two parts, heavenly and earthly.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 436: *loquendi* [R4]
  - 436: *faciens* [R3]
  - 436: *aliquid et* (main token covers two printed words (aliquid, et)) [R4]
  - 436: *∅* (et already held in main token 148 (aliquidet); print has et once) [INS?]
  - 436: *sensibilis* (print sensi-/bilis across lines; main token sensi+side-note, no main token for -bilis, so whole word given) [NW]
  - 436: *gracia* [R3]
  - 436: *vel* (main token is English side-note nor; print at box is vel) [THIN]
  - 436: *accidens sibi* (coordinator: printed sibi has no main token (agent 10)) [THIN]
  - 436: *inesset* [THIN]
  - 437: *haberet* (folio mark 189ª glued) [R5]
  - 437: *est* (line number 10 glued) [R3]
  - 437: *Christi* [R3]
  - 437: *militante* [NW]
  - 438: *consorcio* (line number 5 glued) [R4]
  - 438: *trinitatis* [THIN]
  - 438: *increate hoc* (main token covers two printed words) [THIN]
  - 438: *ecclesia* (line number 25 glued) [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 435:
3. 4. B : Si ergo sit proprie, sequitur. 10. AA,: cesarea; B: cesarie.
29. A Aj! doctorum fiddium.

p. 436:
16. B: nec linea. 19- A in marg : Noia. M. B in marg.:
Nota quod continuacio non facit aliquod corpus esse unum. 24. B:
quam edax 24. A At: sit — conventus deest.

p. 437:
i3. 14. B: predicatur. 17. A in marg. : Nota bene. 19. A in
marg.: Longe ante Christi mortem fuit sancta ecclesia de qua non sunt
presciti (Below 1S9» without mark of reference). 24. A in marg.:
Augustinus. 24. In codd. LXIV. 26. Incodd.: Rectus itaque
et conformis ordo. Corrcxi e textu August. Enchirid. cap. LVI. Opp. tom.
VI, pag. 217. 29. In codJ : creatori. Correxi e textu Aug.

p. 438:
4.1n codd.: perstitit. i5. nulla ; recte: natura 27. A: factus est
19. A verse from the hymn "Chorus novae Hierusalem" in the
Sarum Breviary, at Vespers on Sunday after Easter (Matthew).
```

---

## Chunk 18-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-18-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-18-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "438.27–441.25"
divisions: "cap. 18 (heading 'CAP. XVIII.' at 415.8); part 7 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "718 words; 630 unanimous or majority-real; 76 settled by vote (R2 32, R3a 35, R3b 1, R5a 7, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n475–n478 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 18, part 7: [TITLE]

## ¶1 · 438.27–440.4

> [p. 438] Quamvis enim pro instanti quo factus est primus homo fuit illa ecclesia constituta, tamen novo modo post ascensionem fuit pars eius inferior super partem eius superiorem in celestibus collocata. Partem autem eius inferiorem intelligo totam naturam humanam que secundum partem suam que est Christi humanitas [p. 439] taliter exaltatur; et ad destruendum istos errores in fide laborarent episcopi quorum principale officium foret fidem illam docere atque defendere nec non et errores in fide ista deviancium postposita solicitudine eorum que questum sapiunt declarare. Nam propter cecacionem temporalium oblita est fere ecclesia angelorum, et cum Encheridion LXI° sic scribit sanctus doctor Augustinus: Hec autem que in sanctis angelis et virtutibus Dei est ecclesia, tunc nobis sicuti est innotescet, cum ei coniunctifuerimus in Jine ad habendam beatitudinem sempiternam; ista vero que ab illa peregrinatur in terris eo nobis nocior est quod in illa sumus et quia hominum est quod et nos sumus. Et quod nulli presciti sint membra illius ecclesie sic declarat: Hec sanguine mediatoris nullum habentis peccatum ab omni est redempta peccato. Sed constat quod peccatum finalis impenitencie quale est in omni prescito non potest redimi vel deleri, ut in assimili docet Augustinus in De Dono Perseverancie VI°: Multi, inquit, finalem perseveranciam possunt non habere sed nullus amittere. Unde, quia ecclesia sancta catholica autonomatice dicitur ecclesia, ideo aput auctores scripture et sanctos doctores ipsa specialiter intelligitur, quando ecclesia nominatur, ut Ephes. V°, 25— 27°: Viri diligite uxores vestras, sicut et Christus dilexit ecclesiam et semetipsum tradidit pro ea, ut eam sanctificaret, mundans eam lavacro aque in verbo vite, ut exhiberet ipse gloriosam ecclesiam non habentem maculam aut rugam aut aliquid huiusmodi, sed utsit sancta et immaculata. Ubi non dubium quin loquitur limitate de ecclesia que est universitas predestinatorum, nam illam redemit, illam glorificabit post diem iudicii, illa erit non habens [p. 440] tunc maculam sive rugam, et illa est corpus Christi quod fovet et diligit; et nullo modo verificatur ista de numero prescitorum, quantumcunque magna sanctitate ad tempus appareat prepollere

[ENGLISH]

## ¶2 · 440.5–440.23

> [p. 440] Nec vidi evidenciam unde crederetur quod anteX mortem Christi non erat ecclesia, nisi forte per locum ab insufficienti similitudine, capta ex textu Apostoli Ephes. V°, 31: Erunt, inquit, duo in carne una. Sacramentum hoc magnum est, ego autem dico in Christo et in ecclesia. Sicut enim ex latere primi Adam resoluti in soporem formata est Eva uxor sua (ut patet Gen. II°), sic ex latere secundi Adam dormientis in cruce formata ecclesia, uxor sua (ut patet Joh. XX°). Sed ante priorem formacionem non fuit Eva, ergo ante secundam formacionem non fuit ecclesia. Ista informis argucia induceret ex omnimoda similitudine in errores tocius fidei christiane, ut puta quod Christus non fuit mortuus, quod ecclesia habuit esse materiale ex sanguine et aqua effluxis de latere Christi, et quod Christus non formavit ecclesiam de suo latere, sed ipso soporato et ignorante solum passive contulit ad formacionem ecclesie. Et sic non foret Deus redemptor vel sponsus ecclesie.

[ENGLISH]

## ¶3 · 440.24–441.25

> [p. 440] Ideo oportet intelligere hoc sacramentum ad literamY iuxta sensum historicum expressum de primis parentibus, et supra hunc sensum oportet intelligere hoc sacramentaliter vel mistice de Christo et ecclesia secundum catholicam similitudinem a Christo et sanctis doctoribus expressatam. Christus enim secundum deitatem sicut ordinavit domum sponse sue mundum sensibilem, sic prius dignitate ordinavit sponsam ecclesiam sibi domum, sed utrumque factum est in principio mundi. Et sicut Deus immisit soporem in [p. 441] Adam muliere formata ex eo sine priori contractu mutuo ad assensum, sic primus Adam secundum deitatem ex eternis racionibus exemplaribus formavit in principio mundi eciam ecclesiam sine previa consideracione consensus meritorii, quia (ut dicit Augustinus Enchiridion LVI°) ecclesia celestis semper ex quo condita est cohesit domino. Nam tam angelus quam homo creabatur in gracia gratificante, posterius autem in plenitudine temporis formavit ecclesiam suam humanitus que per multa millia annorum fuit prius dum dormiens in cruce mortuus fecit eam formosam ex principiis eam mundantibus, virtute quorum tota prior ecclesia, sicut et ecclesia sequens accepit vitam spiritualem et pulchritudinem vite naturali superadditam. Et sicut preter materiam coste Adam oportet multiplicari spiritualiter, quia miraculose nobis abscondite aliam materiam ex quibus constituitur mater Eva, sic principaliter mundiciam vel virtutem corporalem sanguinis et aque redempcionis humane oportet dare ampliorem spiritualem mundiciam et virtutem ex eis originatam que se extendit ad totam ecclesiam preteritam et futuram; sed procul undique hoc venenum pestiferum, ut credatur ante mortem Christi non fuisse ecclesiam, sed Christum cum suis apostolis fuisse viando solummodo synagogam.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 439.21: In Scripture etc. the Church means the predestinate.
- 440.5: Insufficient argument from the creation of Eve.
- 441.7: The Church was from the first in grace, but received a new glory at the crucifixion.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 438: *primus* (alinea letter V glued) [R4]
  - 439: *in* (print has in fine as two words) [R3]
  - 439: *27°* [R3]
  - 440: *Christi* [R4]
  - 440: *per* [R3]
  - 440: *31* [R3]
  - 440: *∅* (1 already held in main token 31) [INS?]
  - 440: *II°* (leaf zoom: degree sign broken open on right, looks like ᶜ) [R3]
  - 440: *secundum* (alinea letter a at right edge glued) [R4]
  - 441: *Adam* (alinea letter b glued) [R5]
  - 441: *gratificante* [R4]
  - 441: *Christi* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 438:
4.1n codd.: perstitit. i5. nulla ; recte: natura 27. A: factus est
19. A verse from the hymn "Chorus novae Hierusalem" in the
Sarum Breviary, at Vespers on Sunday after Easter (Matthew).

p. 439:
7. A in marg. : Augustinus. Presciti non sunt de ecclesia, probatur per
Augustinum. In codd. Encheridion LXIX. 12. A A,: quo in illa.
14. A A,: presciti sunt. 16. A in marg.: Nota. ly. In codd.:
dc bono persevcrancie. 28. A A,: atque rugam.
19. Aug. Opp. tom. X, pag. 826.

p. 440:
5. A in marg. : Apparens argumentum pro incepcione ecclesie post
mortem Christi. 9. B in marg. : Magnum sacramentum desponsacionis
inter Christum et ecclesiam. 12. Codd. : Gen. 111°. 23. A in marg. : Quo-
modo tormata est ecclesia. 25. A At: expresse. 33. Codd.: sic Deus.

p. 441:
6. Incodd.: Enchiridion LXIV. 10. A in marg. : Nota. 11. B:
dormkns deest. 25. A: synagogam. Sequitur lingua Bohemica:
Hospodyne mylostywy, racz hrzyechy slare y nowe odpustyiy. Id est : Miseri-
cors domine, dimittcre digneris nobis peccata vetera nec non recentiora
:y. A in marg.: Utrum presciti gerant ordines et oflicia ecclesie.
```

---

## Chunk 19-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "441.27–445.29"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "954 words; 844 unanimous or majority-real; 91 settled by vote (INS 1, R2 59, R3a 24, R5a 7); 19 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n478–n482 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 1: [TITLE]

## ¶1 · 441.27–442.25

> [p. 441] Supposito ex fide scripture elaborata a sanctis doctoribus quod solum predestinati sint membra sancte matris ecclesie, restat dubitandum ulterius si [p. 442] presciti gerant ordines et officia illius ecclesie. Et videtur ex dictis quod non; nam Deus summe sapiens non daret potestatem inhabili. Sed nullus talis habet potestatem huiusmodi si non per Deum, ergo nullus talis habet huiusmodi potestatem. Est autem inhabilis, quia in mortali peccato necessario dampnabili continue, ut suppono ex dictis XXVI° capitulo libri Vⁱ. Confirmatur ex Decreto, XIª, q. III, ubi ex dicto beati Gregorii sic habetur: Ipse ligandi atque solvendi potestate se privat qui hanc pro suis voluntatibus et non subditorum moribus exercet. Si ergo pro leviori peccato habens potestatem ordinis ipsa privatur, multo magis pro graviori peccato ipse qui reciperet huiusmodi potestatem ab ea excluditur; culpandus itaque foret Christus, si ecclesie sue preficeret membrum diaboli tam inhabile et nocivum. Non ergo habet talis caracterem indelebilem, ut sit de exercitu christiano. Hic videtur mihi indubie quod nullus prescitus est pars vel gerens officium tamquam de sancta matre ecclesia; habet tamen intra illam ecclesiam ad sui dampnacionem et ecclesie utilitatem certa officia ministrandi, ut patet de Scarioth et multis eius vicariis, et ad tantum Deus eligit tales dans eis ad tale officium potestatem. Nam Johannis VI°, 71 scribitur: Nonne ego duodecim vos elegi et unus ex vobis diabolus est?

[ENGLISH]

## ¶2 · 442.26–444.5

> [p. 442] Super quo Augustinus, Omelia XXVª, dubitat quomodo Christus elegit dyabolum, et respondet quod electus est iste de quo nolente et nesciente magnum aliquid boni fieret. Hoc, inquit, est proprium Dei, iniquis contrarium quod, sicut iniqui male utuntur [p. 443] bonis Dei operibus, sic econtra Deus bene utitur malis operibus iniquorum. Et ponendo multa exempla conclusionaliter sic concludit: Omnibus ergo bonis Dei, ne per singula currere longum sit, male utitur malus. Et hinc sepe dixi quod existens in mortali continue abutitur bonis Dei, et per consequens, quicquid sic fecerit peccat mortaliter; econtra de malis: malis malorum, inquit Augustinus, bene utitur bonus. Et quid tam bonum, ut Deus, de quo Marci X°, 18 dicitur: Nemo bonus nisi solus Deus? Quanto ergo ille melior tanto melius utitur malis nostris. Quid Iuda peius inter apostolos cui loculi commissi sunt et dispensacio pauperum distributa? Sed quia ingratus tanto beneficio et honori accepit pecuniam, perdidit iusticiam: mortuus tradidit vitam; quem ut discipulus secutus, ut inimicus persecutus est; toto hoc malo lude bene usus est dominus, cum prodicione eius dampnabili nos redemit. Sic ergo habuit ludas officium in ecclesia, non de illa, sicut stercus et apostemata habent officia in humano corpore, non de illo. Modo, inquit Augustinus, corpus Christi mixtum est tamquam area; sed novit Deus qui sunt eius, sicut tu nosti quid trituras, quia ibi est latens massa, nec consumit trituracio quod purgatura est ventilacio. Sed difficultas est utrum tales presciti habent caracterem ordinis, utrum sint sacerdotes episcopi vel prelati. Quoad primum est dissensio inter multos de quiditate caracteris. Aliqui enim dicunt quod est qualitas de secunda specie qualitatis sicut naturalis potencia. Alii autem dicunt quod non est per se in genere sed per reduccionem, sicut alie veritates consimiles extra genus, ita quod caracter sit deputacio [p. 444] passiva creature racionalis ad serviendum Deo et ecclesie secundum gradum ordinis dignitatis; nec contendo circa quiditatem talis caracteris, cum certus sum quod non sit res ut serta regis vel aliquod signum inpressum quod poterit per se esse.

[ENGLISH]

## ¶3 · 444.6–445.29

> [p. 444] Tenendo ergo secundam viam de quiditate caracteris dico ulterius quod alius est necessario delebilis, ut caracter ecclesiasticus in prescitis, eo quod non ultra diem iudicii durabit in eis officium dignitatis. In predestinatis autem oportet esse caracterem omnino indelebilem, cum dignitas sequendi agnum mutuo illuminandi conbeatum et percipiendi fructum vivificum non posset deleri in eis, et de tanto habent caracterem ordinis vel caracterem baptismalem. Et patet quod predestinati et presciti secundum diversitatem officii equivoce habent caracterem. Et correspondenter dicitur quod equivoce habent ordinem, episcopatum vel aliam ecclesiasticam prelaciam, quia presciti ascribuntur ad tale officium solummodo temporale, non ut mereantur beatitudinem, sed ut mitigando penam per accidens prosint ecclesie. Et ita conceditur quod Scarioth et eius vicarii erant apostoli, presbiteri, episcopi et prelati, habentes proporcionaliter ad suum officium potestatem, et ad tantum aput Deum sunt habiles. Quod autem ludas fuit apostolus, patet Matthei X°, ubi inter duodecim quos Christus elegerat computatur, et beatus Petrus testatur quod sortitus est sortem ministerii apostolatus et quod de illo scriptum est Psalmo CVIII°,: 8: Fiant dies eius pauci et episcopatum eius accipiat alter; et sic cum singulum istorum sit nomen officii, patet quod non sequitur: ludas est apostolus, episcopus vel sacerdos, ergo est membrum vel de sancta ecclesia. [p. 445] Sufficit quod sit in illa tamquam palea temporaliter ministrans finaliter comburenda. Unde non dicimus quod ad serviendum Deo in inferno perpetuo paciendo oportet servum indelebiliter habere caracterem, nisi forte equivocetur de caractere bestie quam meminit Johannis Apoc. XIX°, 20, ubi dicitur: Seduxit eos qui acceperunt caracterem bestie et qui adoraverunt ymaginem eius. Et de isto caractere fit mencio Apocalypsis XIII° et XIV°. Caracterem autem transferimus in bonum pro scriptura predestinacionis in libro vite (ut loquitur Christus Luce X°, 20 et Apocalypsis XIII°, 8). Quandoque vero accipitur caracter pro aggregato ex predestinacione et limitacione per signum sacramentale, et sic secundum limitacionem signi caracteris est varie respondendum. Nam caracter predestinatorum et caracter prescitorum qui sunt de synagoga sathane (ut loquitur scriptura Apoc. II°) est indelebilis, quia primus est calculus candidus vel nomen novum, quod nemo scit nisi qui accipit (ut loquitur scriptura Apoc. II°, 9). Sed secundus est nomen finalis impenitencie vel comitans caracter bestie, caracter autem temporalis quando est limitacio ad officium temporale; et in talibus terminis magistralibus oportet responsalem quoad significacionem et quiditatem in principio stabiliri. Caracter enim communiter in malum sumitur in scriptura, sed aliter loquimur hic de caractere agni quoad dignitatem activam ministerii ad quam assignantur predestinati differenter a servis dyaboli in ordine vel baptismo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 441.27: Whether the foreknown hold orders and offices in the Church.
- 442.18: None such is a part or officer of the Church, but he has a duty of ministering within the Church.
- 442.26: God uses the wicked for good.
- 443.26: The difficulty is whether the foreknown have "stamp" (caracter) of orders.
- 444.6: Predestinate and foreknown have the stamp in different ways.
- 445.3: Various senses in which the "stamp" is spoken of.
- 445.16: The "stamp" of the predestinate is a white stone with a new name: of the foreknown the mark of the beast; and there is the temporal "stamp" marking for a temporal office.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 441: *CAP. XIX.* [HEAD]
  - 442: *Vⁱ* [R4]
  - 442: *XIª* [R4]
  - 442: *Christus* [R3]
  - 442: *∅* (English side-note word (the); print has no word before Super) [INS?]
  - 442: *XXVª* [R4]
  - 442: *Christus* [R3]
  - 443: *18* [R3]
  - 444: *et* (alinea letter C glued) [R3]
  - 444: *necessario* (ri clear in print; shared misreading) [NW]
  - 444: *in* [R4]
  - 445: *indelebiliter* [R4]
  - 445: *habere* (line number 5 glued) [R3]
  - 445: *Christus* [R3]
  - 445: *II°* [R3]
  - 445: *II°* [R3]
  - 445: *∅* (second half of secun-dus; neighbour 144 already secundus) [DELX]
  - 445: *Sufficit* (190ª folio mark and margin letter dropped) [OVERRIDE-MARK]
  - 444: *X°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 441:
6. Incodd.: Enchiridion LXIV. 10. A in marg. : Nota. 11. B:
dormkns deest. 25. A: synagogam. Sequitur lingua Bohemica:
Hospodyne mylostywy, racz hrzyechy slare y nowe odpustyiy. Id est : Miseri-
cors domine, dimittcre digneris nobis peccata vetera nec non recentiora
:y. A in marg.: Utrum presciti gerant ordines et oflicia ecclesie.

p. 442:
4. A in marg.: Responsio. i3. 14. Codd.: huius potestatem. i8.Ain
marg.: Responsio. 26. A in marg. : Augustinus. 29. A in
marg.: Sicut mali bonis abuntuntur, sic boni malis bene utuntur.
8. Dec. sec. pars, causa XI, q. III. cap. I.X. 26. Aug.
In Joh. Evang. cap. VI, tract. XXVII. Opp. tom. III, pars II,
pag. 5o5.

p. 443:
7. 8. B: contra de bonis. 11. A A,: ille deest. 14. A A, :
sed quod. 22. In textu Aug. : tamquam in area. 26. Ainmarg. :
Utrum presciti habent caracterem ordinis (Below 189^ without mark of
reference). 27. A: utrum sit. 33. A B in marg. : quid est caracter.

p. 444:
4. serta sive sertum: corona ducalis, regalis sive imperialis. 6. A in
niarg. : Character ordinis est delebilis in prescitis, sed non sic in pre-
dcstinatis. 6. B : secundam vitam. 16. B: caractercm — habent
deest. 32. B: post quod.

p. 445:
8. B: adoraverint. Ainmarg.: Duplex caracter. 34. Codd. : et deest.
```
