# Translation brief: ecclesia 19-e–19-g

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-19-e.md chunks/ecclesia/wyc-ecclesia-19-f.md chunks/ecclesia/wyc-ecclesia-19-g.md` once and fix what it reports.
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

## Glossary (the 203 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| apocrifa; apocrifus | apocrypha; apocryphal | Wyclif applies it to the saints' chronicles as well as to books outside the canon. Ruled 2026-09-28 (6 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |

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
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| summi pontifices | highest pontiffs (of popes); high priests (of the Jewish priesthood) | Split by referent. Ruled 2026-10-02 (*Eccl.* 18, 424.19, 425.20). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |

---

## Chunk 19-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "457.30–460.25"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "675 words; 579 unanimous or majority-real; 78 settled by vote (INS 1, R2 43, R3a 30, R3b 1, R5a 3); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n494–n497 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 5: [TITLE]

## ¶1 · 457.30–460.25

> [p. 457] absolvendo, sine ipso rite ministerialiter concurrente; [p. 458] nec sequitur ex isto quod debemus credere Christum sic concurrere in pretensione ministerii laycalis, nam nullum tale de communi cursu absolute credere debemus explicite sed vivere in fide filii Dei que est universalis sive catholica. Unde Encheridion LX°, quando dyabolus corporis sensus fallit, mentem vero non movet a vera rectaque sciencia qua quisque vitam fidelem gerit, nullum est in religione periculum; vel cum se bonum fingens ea facit sive dicit que bonis angelis congruunt, eciamsi credatur bonus, non est error christiane fidei periculosus aut morbidus. Cum vero per hec aliena ad sua incipit ducere, tunc eum dinoscere nec ire post eum magna et necessaria vigilancia est. Vult iste sanctus dicere quod multa sunt que fidelis neque tenetur plene et particulariter credere neque discredere, sed stat sine mortali cum formidine falsum credere, ut patet de opinantibus vel reputantibus multa bona et religiosa de membris dyaboli licet falsa; sed oportet cavere ne affectus per consensum ad vetitum seducatur. Omnis autem error in veritate videtur mihi sapere peccatum ad minimum veniale. Sed redeundo notandum est quod non sequitur ex isto quod haberetur quoad sacramentum eukaristie devocio laicorum, quia potest contingere quod efficacius et meritorius accipiat laicus corpus Christi, credendo in ipsum in celo et credendo generaliter sacramentum universalis ecclesie, quam datus laicus vel sacerdos qui sub actibus sacramentalibus corporalibus accipit corpus Christi. Nam ritus talis non proficit nisi de quanto disponit ad accepcionem et manducacionem corporis Christi secundum animam in fide et caritate (de qua manducacione Joh. VI° loquitur Jesus noster). Non enim nego quin [p. 459] necesse sit nos in vita intendere signis sensibilibus in quibus stat modo suo christiana religio, cum debemus credere quod omnia sacramenta sensibilia rite ministrata habent efficaciam salutarem. Sed in isto stat periculum militantis ecclesie quod iudaizando secundum sensum carnalem signa illa cum tradicionibus humanis plus suis signatis preponderet vel eciam legem Dei plus attendat iudicio sensus corporei quam oculo mentis vel eciam lumini fidei. Et correspondenter ad istos motus anime opera consecuntur, unde ad elidendum istum errorem Christus ordinavit nos in fide vivere et membra matris nostre particulariter ignorare, ne quis presumat se extollere vel exigendo temporalia gentiliter a lege scripture recedere, sciendo quod nulla solempnitas vel tradicio humana facit hominem caput vel membrum sancte matris ecclesie aut Christi vicarium nisi specialis Christi gracia et imitacio Christi in moribus. Ulterius videtur quod non licet pure clerico in causa et persona propria fratres suos corporaliter pro temporalibus ecclesie expugnare. Patet sic: Clero minus elongatum a vita apostolica est omnino illicitum, et magis elongatum est magis illicitum, sed iuxta conclusionem primam clerum contendere in foro ecclesiastico pro patrimonio Christi est omnino illicitum, ergo multo magis ipsum bellando pro temporalibus invadere fratrem suum, nam cum sit a vita et doctrina Christi magis extraneum, foret sacerdoti Christi magis illicitum. Ille ergo qui pateretur iniurias, antequam cum fratre suo contenderet, pateretur iniurias, antequam spoliando bona nature fratrem suum invaderet. Unde magnus videtur defectus in nostris doctoribus qui dimissa scola Christi in sequendo ipsum et paciendo iniurias [p. 460] consulunt nedum laicis sed pontificibus ad pugnandum, palliantes per sompnia et scripta apocrifa quomodo pugne tales eciam in Romano pontifice per signa que vocant miracula sunt laudate (ut tetigi XVII° cap. libri quarti). Rogamus itaque in verbis ut habeamus Christi et sue paciencie documenta, sed tamquam ypocrite adversamur in factis, nitendo totis viribus quomodo habeamus de factis hostibus temporales victorias et fastuosa ac huic vite voluptuosa delectamenta, et ad hoc applicamus triplicem sapienciam huius mundi, de qua Jacobi III°, 15 dicitur quod est terrena, animalis et dyabolica. Necessarius ergo foret cogitare cogitaciones pacis, rogare et predicare que ad pacem sunt, quam adducere fucos sophisticos ad palliandum quod nedum mundi principibus sed eciam summis pontificibus licitum est bellare. Ad tantum enim cecati sunt eciam professores scripture quod dicunt tam necessariam esse clero hodie possessionem temporalium, quam necessaria fuit in primitiva ecclesia potestas faciendi miracula, et intelligunt necessarium pro utili (ut oportet), quia aliter concederent quod tam necessaria ecclesie foret sua predicacio, ymmo sua decepcio sicut fuit Christi passio, cum sit sub eodem gradu contingens necessitas utrobique.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 458.1: while we have no reason to suppose he will do so with lay ministrations.
- 458.23: The sensible sacrament profits only so far as it helps to the spiritual acceptance of Christ.
- 459.1: Yet we must not neglect the Sacraments,
- 459.5: The danger is that more attention is paid to the signs than to the things signified.
- 459.19: No cleric may fight tor temporalities.
- 460.1: False teaching on this point is common.
- 460.17: It is even said that temporal possessions are as needful now as was the power of miracles at first.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 457: *ministerialiter* [THIN]
  - 458: *pretensione* (print spelling) [NW]
  - 458: *laycalis* [R4]
  - 459: *modo* [R4]
  - 459: *iudaizando* (margin numeral 1 glued) [R4]
  - 459: *vel* (margin numeral 2 glued) [R4]
  - 459: *consecuntur* (print con-/secuntur; main token holds whole word; print spelling) [NW]
  - 459: *Christi* [R3]
  - 459: *Christi* [R3]
  - 459: *nam* [R3]
  - 459: *Christi* [R3]
  - 459: *Christi* [R3]
  - 460: *XVII°* [R3]
  - 460: *∅* (other scans split XVII° (xui + 1); print has no word before cap.) [INS?]
  - 460: *III°* [R4]
  - 460: *15* (main token i covers printed 15) [R3]
  - 460: *necessaria* [R3]
  - 459: *quod* (English side-note "The" glued on (agent 10)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 457:
2. 3. Decr. sec. pars, q. I., cap. LXXXIV. 7. ib. cap. LXXVIII.
ib. cap. LXXXIII.

p. 458:
5. A in marg.: Augustinus; in codd. Encheridion l.XVIII, recte LX
vid. Aug. Opp. tom. VI, pag. 218. 9. A A, : vel si. i3. B: magna
et multa. 20. A A, : autem deest; 21. A A,: in veritate deest.
22. A in marg. : Conclusio notanda. 23. B: habetur.

p. 459:
5. A in marg.: Periculum. 9. B: lumini decst. 14. A in marg. :
Conclusio. 18. A in marg. : Quinta conclusio. Non licet purc clerico
invadere fratrem suum propter temporalia nec licct sibi ut pro illis pugnei.
21. Codd. : cxpungnare. lbid. : Clero cui. 26. In codd : talibus j Correxi.

p. 460:
3. A: pungne. 16. A in marg. : Conclusio falsa. 21. B: quod
aliter. 26. A in marg.: Nota contra possessionem et dominium
ecclesie, quod sic necessarium nunc reputatur, sicut in primitiva ecclesia
potestas faciendi miracula (Above 192* without mark of reference).
26. 27. B: dedisset preter naturalia.
```

---

## Chunk 19-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "460.26–464.30"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "996 words; 848 unanimous or majority-real; 136 settled by vote (R2 90, R3a 42, R3b 1, R5a 2, R6a 1); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n497–n501 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 6: [TITLE]

## ¶1 · 460.26–462.21

> [p. 460] Primo ergo videtur quod cesar dedisset principaliter naturalia bona clero tam utilia sicut Christus, et iterum tam perfecta fuisset temporalis possessio, sicut carismata supernaturalia concessa a Christo, quia si potestas quam Christus concessit suis apostolis fuit cesareo dono perfeccior, fuit ecclesie Christi necessarior, quod fuit patulum ex fructu et cremento [p. 461] ecclesie. Et iterum proporcionaliter ut membrum ecclesie habet plus de talibus possessionibus foret perfeccior et ecclesie necessarior, et sic fratres et viri contemplativi forent sub non gradu necessitatis ecclesie et persone mundo divites maxime necessarie, quia nullius possessio est necessarior ecclesie quam est ipse. Sed quid plus repugnaret scripture sacre vel sacris legibus de status minoritate? Ideo consulerem fratribus quod omnino resisterent isti sentencie, quia nedum derogaret perfeccioni sue retrahendo seculares, ne accipiant ordinem evangelice paupertatis, sed animaret divites seculi ne faciliter imperciantur eis elemosinas corporales. Possent enim seculares dicere (ut audivi quosdam. instructos ex ista sentencia): Tu dicis quod tam necessaria est modo possessio temporalium quam necessaria fuit in primitiva ecclesia potestas faciendi miracula, sed possessio temporalium est ecclesie utilior et congruencior in secularibus quam in clero. Ideo quam necessaria fuit in clero potestas faciendi miracula in primitiva ecclesia, tam necessaria est hodie in secularibus possessio terrena. Sed nemo in primitiva ecclesia diminueret de potestate sua faciendi miracula propter communionem cum fratribus, ergo nec secularis debet communicare cum fratribus de possessione temporalium, ne diminuatur perfeccio sibi necessaria; et sic frater qui ad hoc hortatur vel consulit, deficit a caritate, nitens dampnificare gracia questus temporalium fratrem suum. Sed quis temptaret taliter membrum Christi? Si dicitur quod propter dispersionem temporalium accresceret elemosinanti donum spirituale perfeccius, hoc repugnat sentencie propter duo: Primo quia tunc foret expediens cuicunque clerico possessionato plus [p. 462] de possessione sua egenis tribuere et sic usque ad non gradum, et sic renunciando cunctis que possidet sequi Christum in evangelica paupertate. Secundo, quia tam necessaria est clero modo temporalium possessio, sicut fuit alia potestas concessa a Christo ad faciendum miracula, sed notum est quod propter nullas corporales elemosinas dat Deus meliora carismata quam fuit potestas faciendi miracula; ergo propter tales elemosinas non recipiet distribuens carismata pociora. Ymmo cum necessarior sit modo temporalium possessio quam potestas faciendi miracula, et quelibet partis possessionis particio perderet illam possessionem, cum sit res inanimata, videtur sequi ex principio quod fatuum foret clero possessionato possessionem suam perdere. Nec valet egenti allegare possessionato quod de superfluo vel principaliter necessario debet tribuere, quia (ut sequitur ex principio sapiencie dyabolice) nichil est clerico possessionato superfluum, sed de quanto plus possidet, de tanto quod possidet est sibi magis necessarium, quia complet unam possessionem magnam necessariorem ecclesie.

[ENGLISH]

## ¶2 · 462.22–463.31

> [p. 462] Ideo detestando hoc porisma de scola dyaboli dico quod necessarior fuit in clero dominacio temporalium in primitiva ecclesia militante quam est modo. Patet ex hoc quod tunc fuit utilior et meritorior et per consequens necessarior. Tunc enim fuit pure evangelica civili dominio impermixta. Ulterius dico secundo quod potestas faciendi miracula fuit necessarior ecclesie, quam unquam fuit temporalium possessio quodammodo infinite, quia potestas illa est natura superior, sicut virtus excedit civile dominium. Unde Symon magus non fuit tam fatuus quin libenter voluerit commutasse pecuniam pro potestate faciendi miracula, [p. 463] ymmo affeccione commodi hoc censuit fore lucrum; patet Act. VIII°. Multo magis fidelis sciens quod potestas faciendi miracula plus lucrefaciendo pacificaret ecclesiam quam quelibet divicie temporales- Et ex istis patet tercio quod seminans illud dogma in populo non roret ut sic utilis procurator vel minister pauperum sed egenis Christi ex doctrina sibi contraria subdolus inimicus. Nam gracia et caritas sunt precipua potestas faciendi miracula, quia illa sunt per se bona per que docetur homo mundum et peccata relinquere et Deum diligere; quod est opus excellentissimum viatoris. Ideo si illud porisma per impossibile foret verum, tunc sicut nemo tenetur alienare a se caritatemvelspiritum sanctum, sic nemo teneretur temporalia pauperibus impertiri. Suppono autem de logica quod sicut confundit, ut si temporalia sint tam necessaria sicut aliqua potestas faciendi miracula, tunc nulla talis potestas est necessarior; quod est falsum de potestate quam Joh. 1°, 12 exprimit: Dedit eis potestatem filios Dei fieri. Illa enim est infinitum melior quam possessio temporalis, nam ex illa potestate legitur Evangelistam mutasse silvestres frondes in aurum et litoria saxa in gemmas. Ex quo patet quod illa potestas fuit infinitum validior quam illa possessio et plus fecit ad profectum ecclesie. Aliter enim Christus infinitum potencior cesare, habens discipulos prudenciores ad ministrandum bona fortune, foret notabiliter increpandus quod non dotasset ecclesiam plus quam cesar. Hoc enim propter minorem mundi avariciam fuisset tunc melius, et per consequens ex dictis tam bonum sicut potestas quam Christus habuit.

[ENGLISH]

## ¶3 · 463.32–464.30

> [p. 463] Sexto videtur quod nullus clericus contenderet circa maioritatem sui ad subditos in ecclesiastica ierarchia, [p. 464] nara homine habente revelacionem ad hoc non contenderet circa illud, sed sentiret humiliter de se ipso, si non habeat revelacionem de hoc; cum tunc ignorat si sit de sancta matre ecclesia, in vanum contenderet si sit maior de illa ecclesia, cum deest sibi probacio si sit de illa ecclesia (ut tactum est in conclusione prima). Maioritas autem in ecclesia et non de illa foret contendenti inutilis et ecclesie tamquam impertinens sive contrarium contemptibilis. Et ex istis videtur quod nimis magna demencia foret urgere ecclesiam ut credat quemlibet Romanum pontificem esse caput sue ecclesie, nam iuxta dicta quilibet talis posset esse episcopus in ecclesia sine hoc quod sit de illa. Sicut ergo non est de fide quod omnis Romanus pontifex sit predestinatus sic non est de substancia fidei quod sit caput vel membrum sancte matris ecclesie. Et patet quod non sequitur perire in laicis fides de recto sacramentali ministerio sacerdotis, quia sufficit fideli credere fidem catholicam et quod Deus propter nullum errorem spiritualis prepositi dampnificat subditum nisi suum demeritum sit in causa. Non ergo debet subditus desperare de peccato prepositi, quia, quantumcunque malus sacerdos fuerit, dummodo subditus in Christum crediderit, salvus erit, et dampnabile ministerium sacramenti sui curati sibi proderit, ut ostendit decretum sub auctoritate Augustini, in De Consecracione, dist. IV: Quomodo ipsum, inquit, caracterem multi lupi eciam lupis infigunt qui videntur esse intus, verumptamen ad illam ovem que ex multis una est non pertinent.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 461.9: Friars should oppose such teaching,
- 461.14: or it may be turned against them.
- 462.22: I say that possession was more needed in the primitive Church than now.
- 462.31: Simon Magus was wiser than these teachers,
- 463.5: whose teaching if received would stop all alms to the poor.
- 464.1: There should be no contention for high place in the Church,
- 464.14: since we cannot tell whether even the highest are members.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 461: *iterum* [THIN]
  - 461: *∅* (s is line number 5; print has no extra word) [INS?]
  - 462: *de* [THIN]
  - 462: *possessione* [THIN]
  - 462: *fuit* [R3]
  - 462: *fuit* [R3]
  - 463: *ymmo* (folio mark 192ᶜ glued) [THIN]
  - 463: *populo* (print has populo whole on the line (not hyphenated)) [R4]
  - 463: *Christi* [R3]
  - 464: *si* [R3]
  - 464: *probacio* (line number 5 glued) [R4]
  - 464: *ergo* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 460:
3. A: pungne. 16. A in marg. : Conclusio falsa. 21. B: quod
aliter. 26. A in marg.: Nota contra possessionem et dominium
ecclesie, quod sic necessarium nunc reputatur, sicut in primitiva ecclesia
potestas faciendi miracula (Above 192* without mark of reference).
26. 27. B: dedisset preter naturalia.

p. 461:
4. A, corrigere vult: sub uno gcnere. 8. A in marg. : Consilium.
11. 12. B: si animarct. 22. diminucret in codd.: An diminucreiur ?
24. B: ideo nec. s5. B: ne deest. 3o. A B in marg. : Responsio
quedam.

p. 462:
3. 4. B: tam multa est. 12. A in marg. : Responsio quedam.
16. B: vel principio. 22. AB inmarg. : Responsio propria. l'otestas
faciendi miracula semper fuit utilior ecclesie quam bona temporalia.
27. A A, : impermixti. A in marg.: Conclusio. 32. A A,: voluit.

p. 463:
4. A in marg.: Conclusio. 6. B: utilis procreator. 14. A:
sicut nemo. 24. B: valior. 32. Sexta conclusio. Nullus
clcricus debet contenderc pro maioritatc ad subditos in ecclesiastica
ierarchia.

p. 464:
7. Codd.: Minoritas. 9. B : impertis. 9. A in marg.: Non
tenemur credere Romanum pontificem csse caput nostre ecclesie.
16. B : vel deest. 24. A in marg. : Augustinus.
27. Decreti III pars, De Consecr. dist. IV, cap. XI. I.
```

---

## Chunk 19-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "464.31–468.31"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "930 words; 817 unanimous or majority-real; 99 settled by vote (R2 62, R3a 28, R5a 8, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n501–n505 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 7: [TITLE]

## ¶1 · 464.31–465.13

> [p. 464] Nec sequitur ex isto confusio policie ecclesie, quia ecclesia militans operibus sui curati debet credere, et [p. 465] non nudo nomini vel prefecture in facie ecclesie, quia talis foret evidencia nimis fallax. Obediendum est tamen tali pretenso preposito salva semper obediencia legi Christi; et in ista cecitate tantum turbatur ecclesia quod quidam plus credunt signis mortis factis in vestigio mortuorum defunctorum quam operibus vivacibus superstitum quantumcunque conformiter legi Christi vivencium. Et credo quod illusio diaboli in talibus signis excecat populum; post illum ergo in quo claruit viva vite sanctitas probabiliter credi potest ad ostendendum eius sanctitatem signorum claritas, sed adhuc non tam evidenter sicut in uno opere fructuoso.

[ENGLISH]

## ¶2 · 465.14–468.31

> [p. 465] Unde talis culpanda cecitas, inordinatus ac cupidus cultus circa reliquias faciunt in penam peccati populum multum falli. Unde in multis patriis cupido pecunie facit in multis ecclesiis quod pars persone empte, ut canonizetur pro confessore vel martire, plus honoretur peregrinacione, sumptuosa oblacione et sepulcri ornacione auro et lapidibus preciosis quam corpus matris Dei, apostolorum Petri et Pauli vel alterius notorie beati. Et evidencia talium stat in isto quod talia possunt fieri vere ac meritorie, et prelati quibus hoc est incognitum approbant quod sit ita; nullum tale factum reprobo et pauca vel nulla approbo, quia peregrinantes, reliquias adorantes et pecunias congregantes nedum possent occupari utilius hoc dimisso, sed ex factis in lege Christi et scriptura videtur sequi quod omnes sic colentes debent protunc melius occupari et per consequens peccant graviter melius omittendo. Dimitto peccata que contingunt altrinsecus in hoc facto et quomodo ipsum est factum pharisaicum patrum veteris testamenti, sed non ex lege [p. 466] nova efficaciter nobis fundatum, sed ut plurimum ambiguum et vel ex parte colencium vel ex parte occupancium reliquias viciatum. Sicut enim in lege veteri Judeis declinantibus a cultu insensibilium invaluerunt signa generacionis adultere, sic in nova lege torpente affeccione celestium oportet tradiciones humanas et ritus ceremoniarum sensibilium dimissa religione et affeccione insensibilium prevalere, et ad hoc movent tres hostes anime. Nam necesse est dyabolum illusionibus signorum sensibilium seducere ypocritas sub specie sanctitatis, quia peccata facta in populo hoc requirunt, et dyabolus videt quod populus ad seduccionem illam est pronior. Sic enim legitur I° Regum XXVIIIᵛᵒ quod Saul consuluit phitonissam que arte diaboli suscitavit sibi dyabolum pretendentem effigiem Samuel, qui dyabolus multas veritates commiscuit, ut Saulem in desperacionem induceret et caucius in aliis erroribus seduceret post et ante. Declarat autem Augustinus libro II° De Mirabilibus Sacre Scripture, cap. X°, quod fuit dyabolus, non spiritus Samuelis, primo quia mulier tam malifica non haberet arte diaboli potestatem ad imperandum tam sancte anime; secundo quia tyrannus Saul non meruit tantam illustracionem et ministracionem a bono spiritu inquietato per duos homines tam indignos, et tercio quia dicit ille spiritus: Cras tu et filii tui mecum eritis. Saul autem et filii eius creduntur fuisse reprobi et sic cum diabolo et non cum spiritu Samuelis. Ista movent hunc sanctum [p. 467] ad credendum hoc totum factum fuisse illusione diaboli, et credo quod nemo faciet evidenciam quin licet fidelibus opinari quod feretrum pape bellantis translatum fuit in ecclesiam arte dyaboli. Nec sequitur ex sentencia Augustini quod scriptura 1° Regum XXVIIIᵛ° sit falsa, quia dicit quod nomen Samuelis signat translative dyabolum figurantem; sic enim dicitur I Johannis V°, 8 quod spiritus, aqua et sanguis unum sunt in officio, designando trinitatem divine essencie, et in communi modo loquendi pretendens personam alterius vocatur nomine illius cuius vicem pretendit. Sic enim Johannes dicitur Helyas, et angelus vicarius Dei loquitur in lege veteri in persona Dei cuius sentenciam representat. Redeundo ergo ad propositum, patet quod necesse est sacerdotes Lhnsti dimittere ritus gentiles de maioritate civili et omnino attendere quomodo copiosius atque humilius fructuose servient in ecclesia sancta Dei scientes ex fide quod secundum hoc laus et maioritas sunt a Deo. Ideo secundum Crisostomum sicut membra humani corporis nobiliora non impugnant minus nobilia sed iuvando se reciproce complent sua officia, sic debet esse de membris sancte matris ecclesie: unusquisque sine pompa maioritatis vel eius solicitudine debet iuvando et amando quemlibet operari in sua vocacione subducta contenciosa adversacione. X Septimo videtur quod nullus prescitus recipit rite baptismum quo deleatur simpliciter suum originale peccatum; patet ex dictis XXVII° capitulo libri V. Nam omnis prescitus manet perpetuo in defectu finalis perseverancie, quod est peccatum gravissimum et indelebile, et per consequens non tollitur simpliciter per baptismum. Verumptamen sicut aliqua est gracia predestinacionis [p. 468] et aliqua gracia secundum presentem iusti- ciam, sic aliquod est peccatum presciencie vel finalis impenitencie, et aliquod peccatum secundum presentem iniusticiam, et quia termini videntur multis extranei et preter significacionem verbalem, ideo alias illos exposui, declarans quomodo ista dicuntur gracie et peccata equivoce et quomodo ista sunt alternatim sibi opposita. Nam omnis prescitus habet perpetuum et originalem defectum, ille tamen ad tempus in malicia sua suspenditur per graciam secundum presentem iusticiam, ut graciam baptismalem et alias, et ideo dixi quod peccatum originale non deletur simpliciter. Et si queratur quid meretur prescitus existens in gracia secundum presentem iusticiam, dicitur quod aput rectiloquos et non equivocantes nunquam meretur beatitudinem, quia nunquam est dignus beatitudine sed meretur perpetuam mitigacionem pene eterne cum aliis bonis temporalibus; et sic Deus redemit prescitum non ad beatitudinem sed ad pene eterne miticiam, sicut redemit omnes dampnatos. Et correspondenter prescitus absolvitur a peccato, non ut omnino non perpetuo puniatur sed ne tam graviter perpetuo puniatur. Et sic (ut dicit Lincolniensis) peccata redemit non actus sed defectus quorum malicia per temporalem graciam est suspensa. Et sic presciti, sive seculares sive clerici, quantumcunque iuste videantur prefici bonis Dei, hoc est, dumtaxat secundum quid dum sunt in gracia temporali et iniuste simpliciter dum carent omnino momentanea caritate. Ex quo patet quod iudices tam seculares quam ecclesiastici deficiunt persepe in suis iudiciis a regulis

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 465.5: Excessive trust in miracles.
- 465.14: Evil of relic worship.
- 466.10: The devil has always drawn men to hypocrisy by means of sensible signs.
- 467.14: Christ's priests should care only to do service to the Church.
- 467.27: Baptism does not altogether destroy original Sin in the foreknown.
- 468.13: The profit of present righteousness to the foreknown is that they lessen their punishment,
- 468.26: and gain a qualified right to temporal goods.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 464: *quia* (alinea letter c and margin T glued) [R4]
  - 465: *non* (folio mark 192ᵈ glued) [THIN]
  - 465: *operibus* [NW]
  - 466: *efficaciter* [THIN]
  - 466: *∅* (has is from the English side-note "The devil has"; print has Nam (main token pos 61)) [INS?]
  - 466: *∅* (boxed item is the alinea letter V at the right edge) [R4]
  - 466: *sensibilium* [DEL]
  - 466: *I°* (tall capital I, same height as R) [R3]
  - 466: *XXVIIIᵛᵒ* (superscript vo) [R4]
  - 466: *II°* (tall capitals) [R3]
  - 466: *quia* (trailing 1 is a note/margin mark, not text) [NW]
  - 467: *ad* (folio mark 193a glued) [THIN]
  - 468: *∅* (previous page closing text (est gracia predestinacionis); p468 line starts destinacionis et aliqua gracia) [INS?]
  - 466: *∅* (duplicate: torpente already at 37) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 464:
7. Codd.: Minoritas. 9. B : impertis. 9. A in marg.: Non
tenemur credere Romanum pontificem csse caput nostre ecclesie.
16. B : vel deest. 24. A in marg. : Augustinus.
27. Decreti III pars, De Consecr. dist. IV, cap. XI. I.

p. 465:
5. B: quod quidem. 6. B : mortuorum decst. [4. Ainmarg. :
Nota de pcregrinacionc. 19. A in marg. : Nota de colentibus reliquias
sanctorum (liclow ig2<t without mark of reference).

p. 466:
10. A in marg.: Diabolus sepe seducit horaines per corpora mortu-
orum et de Samuele, an ipse fuisset suscitatus (Above ip3» without
mark of reference). 16. A A, : pretendem. 20. B in marg. :
Nota secundum Augustinum quod phitonissa suscitavit diabolum Sauli.
21. A in marg. : Samuel; ibid : Augustinus.
21. Aug. Opp. tom. III, pars II, pag. 18 Appendicis. 27. !. Reg.
XXVIII, 19.

p. 467:
7. B in marg. : Nota de papa bellatore. 19. B: Ideo deest. A in
marg: Crisostomus. 27. A in marg. : Scptima conclusio. Nullus
prescitus recipit rite baptismum quo deleretur pcccatum originale.
28. AA,: quomodo dcleatur.

p. 468:
2 A A,: sicut aliquod. 2. A in margine: Nota quid meretur
prevcitus pcr temporalem iniusticiam (Above i93» without mark ot
reference). 5. preter; in codd.: p«. H. alias, scil. gracias.
,3. A in marg.: > Nota. 23. A in marg.: Lincolniensis.
24. B: peccata redeunt. 3o. A in marg. : Conclusio. De iudiciis
sepe dubiis iudicancium.
```
