# Translation brief: ecclesia 13-e–14-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-13-e.md chunks/ecclesia/wyc-ecclesia-13-f.md chunks/ecclesia/wyc-ecclesia-14-a.md` once and fix what it reports.
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

## Glossary (the 168 rows these chunks use; the full file is GLOSSARY.md)

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
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |
| elemosinans | almsgiver | The participle of *elemosinare*: the donor. Ruled 2026-10-02 (*Eccl.* 13). |

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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Ruled 2026-10-02 (*Eccl.* 13). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
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
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| zizania | cockle | Douay–Rheims (Matt. 13:25). Ruled 2026-09-28. |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |

---

## Chunk 13-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-13-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-13-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "290.20–294.10"
divisions: "cap. 13 (heading 'CAP. XIII.' at 274.25); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "852 words; 773 unanimous or majority-real; 71 settled by vote (DEL 2, R2 50, R3a 18, R5a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n327–n331 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 13, part 5: [TITLE]

## ¶1 · 290.20–292.1

> [p. 290] Immo ut probabiliter creditur tota dissensio inter regna et gentes diversarum sectarum exoritur propter omissionem culpabilem consiliorum ac privilegiorum que Christus instituit clero suo. Nam si omnes redditus quibus in christianismo dotatur ecclesia, forent inter seculares dominos distributi et clerus ostenderet in se concorditer ac efficaciter contemptum seculi ac tercio predicaret laicis vigilanter de fallaci affeccione temporalium pro momento quo peregrinamur a domino, et quomodo instantaneum seculare desiderium inducit dampnacionem perpetuam, brevis autem mundi contemptus preparat efficaciter ad beatitudinem consequendam, [p. 291] tunc cessarent bella in christianismo, vel simpliciter vel in parte, et disponeretur ecclesia Christi ad conquirendum armis virtutum populum infidelem. Sic enim fuit tempore apostolorum, quando exproprietarie pure secundum Christi consilia vixit clerus, sed commixtus sinistris tradicionibus humanis cum dexteris Christi consiliis, vinum in quo inebriaretur ecclesia est limphatum et genus nervorum caritatis ecclesie debilitatum et sine custode zizannium discordie undique seminatum. Cum enim corpus ecclesie sit limitatum a Deo, quibus cibis et qualiter secundum partes dispares pasceretur, Deus sicut tribuit commensurale alimentum spirituale per prelatos distribuendum fidelibus, sic dat escam corporalem parciendam per activos tam predicatoribus in agro quam contemplatoribus in lecto. Ideo usurpantibus illis violentis officium et consumentibus inordinate eorum pabulum necesse est totum corpus ecclesie esse inordinatum ex defectu observacionis ordinis suarum parcium. Si enim fit bolismus in homine et breviter quocunque membro secundum appetitum caninum contra regulas virtutis regitive trahente alterius nutrimentum vel occupante alterius membri officium, fit in toto corpore discrasia. Si enim viator haberet vermem in stomacho qui nutrimentum membrorum, quomodo servaretur sanitas et valitudo eorum? Sic si sacerdotes Baal cum uxoribus et filiis consumunt mendaciter per meatus nocturnos et subterraneos bona plebis, patet littera Danielis XIV°: sic autem est in corpore ecclesie cuius virtus regitiva est patris sapiencia; et leges eius, ut mandata atque consilia, sunt privilegia singulariter membris ecclesie officium operandi et nutrimentum limitancia, ut membra superiora debent pasci precipue spiritu animali et regere ac movere membra supposita; [p. 292] quod si dislocantur et innaturaliter pascuntur, necesse est ut in aliis membris fiat discordia.

[ENGLISH]

## ¶2 · 292.2–292.17

> [p. 292] Unde credo quod nunquam in corpore ecclesie cessabit simpliciter bellum, dolus atque contencio, antequam cleri dislocacio, secularis officii usurpacio, et per consequens officii speculatoris omissio sit per virtutem regitivam ecclesie restituta; in tanta namque armonia constituta est pars mundi superior quod secundum Commentatorem una stella addita celo vel moveret cum fatigacione et pena, vel simpliciter non moveret; et multo magis in regno celorum quod est ecclesia contrariacio superiorum suo motori facit quod tota ecclesia fatigabiliter sit turbata. Tota autem contrariacio stat in hoc quod bona temporalia plus bonis perpetuis sunt amata. Ideo ve illis qui stulte faciunt in affeccione pastorum temporalia spiritualibus anteponi.

[ENGLISH]

## ¶3 · 292.18–292.28

> [p. 292] Si autem prelati sint magis avari, honoris mundani plus cupidi, plus viventes secundum fastum seculi, per bella excitata de bonis pauperum ad vindicandum proprias iniurias amplius secularibus insistentes, et (quod periculosissimum est) sub pallio sanctitatis quicquid perpetraverint fuco adulterandi verbum Dei sophistice defendentes, quomodo cum isto circulo quinarii stabit regnum? Scio quod in ista rota currus diaboli seducerentur (si fieri potest) eciam electi, et non sic preparatur ad hic augendum populum domini sed satellitum Antichristi.

[ENGLISH]

## ¶4 · 292.29–294.10

> [p. 292] Et quantum ad secundam partem assumpti, patet quod infideliter vendicatur a clericis in talibus dotacionibus a mundo securitas; nam carta evangelii quam Christus concessit non potest deficere. Unde Matthei VI°, 25, precipit clero suo ne sit sollicitus [p. 293] quid manducabit vel bibet, aut quomodo induatur, sicut solliciti sunt viventes gentiliter, quia, ut arguit per locum a maiori: Si Deus providet pastum volucribus celi et tegumentum liliis agri, quanto magis domesticis fidei? Si enim tempore legis veteris quando minus suadebatur elemosina, Psalmista dicat, Psalmo XXXVI°, 26: Junior fui, etenim senui et non vidi iustum derelictum nec semen eius querens panem, quanto plus hodie? Tollat ergo clerus offensam domini non declinando a lege sua, sicut communiter facimus affectando inordinate voluptatem et curiositatem, et non est compossibile quod ad deterioriacionem desint nobis necessaria vite nostre, quia Matthei VI°, 33, dicit veritas: Querite ergo primum regnum Dei et iusticiam eius, et hec omnia adicientur vobis. Privilegium autem Christi concessum Luce X°, suis discipulis est securius quam carta vel concessio mundana, cum dominus mundi qui mentiri non poterit sic precipit: In quamcunque domum intraveritis ibi manete edentes et bibentes que apud illos sunt. Sed debemus cavere sollicite ne amittamus hoc privilegium per abusum, quod fit quando contra regulam et vitam apostoli sumus hospitibus onerosi. Quomodo ergo stat cum fide et religione christiana quod clerus confederatus et obligatus mundo per cartas plus confidit in dotacione cesarea quam divina, cum Luce XXI°, 34, precipiat ut caveamus a crapula et curis seculi. Et patet ex fide scripture quomodo observantes ordinem illum preposterum sunt insecurissimi quoad homines et quoad Deum. Oportet enim primo quod originetur in Deo securitas que non potest fundari nisi in observancia legis sue. Et [p. 294] hec racio quare Deus ad abstergendum cecitatem mundanam ab oculis mentis nostre ordinat nunc translacionem regnorum in qua extinguitur cleri mundana securitas, nunc permittit predones, fures, incendium vel alium eventum fortuitum evenire. Unde tollantur temporalia in quibus seculares clerici prepostere confidebant, et nunc tercio permittit dissensiones oriri inter partes, tollens seculi potentes de medio per quod coniectura providencie humane eciam in superioribus ecclesie sepius est cassata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 290.20: Quarrels and wars would end if the Church kept Christ's privilege of poverty.
- 291.11: The Church is disordered when the clergy encroaches upon the work and reward assigned by God to the laity.
- 292.2: All the evils in the Church spring from worldliness.
- 292.18: The security that comes of endowments is a false one.
- 293.1: The true security depends on the promise of Christ who commanded us not to be careful for these things.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 290: *inter* (20 is the line number) [R3]
  - 290: *Christus* [R3]
  - 291: *Christi* [R3]
  - 292: *cleri* [R3]
  - 292: *plus* [R3]
  - 293: *quid* (170a folio mark) [R3]
  - 293: *Christi* [R3]
  - 293: *X°,* (line-final; next line starts suis, no verse) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 290:
11. A in marg. : Nota. 20. A in marg. : Conclusio.
IX. Sergius III. (897 — 904). Comp. Gregorovius, Gesch. der
Stadt Rom im Mittelalter III, 242 hodie; id est, 1378; per duos
pseudomonachos scil. per Urbanum VI et Clementem VII.

p. 291:
i3. A in marg. : Nota. 17. Violentis; rccte: violcnter. 24. B: discrusia.

p. 292:
3. A in marg. : Nota. iR. A in marg. : Nola quinque. 21. 22. B:
et per quod. 27. B: hoc augendum ; A,: sic agendum. 29. B:
terciam partem.

p. 293:
9. A in marg. : Conclusio. 16. A in marg.: Nota privilegia a
Christo concessa. 27. A in marg.: Conclusio. 29. A A^:
servantes ordinem.
3. Matth. VI, 26—28. 19. Luc. IX, 4.

p. 294:
11. A in marg. : Nola honas considcracioncs. Nota contra securitatem
dotacionis. 3j. A Aj : odium.
```

---

## Chunk 13-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-13-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-13-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "294.11–299.8"
divisions: "cap. 13 (heading 'CAP. XIII.' at 274.25); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1107 words; 985 unanimous or majority-real; 94 settled by vote (DEL 1, R2 55, R3a 22, R5a 15, R6a 1); 28 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n331–n336 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 13, part 6: [TITLE]

## ¶1 · 294.11–295.8

> [p. 294] Ulterius consideret Christi discipulus si ista vocata mundana securitas assecurat altrinsecus elemosmatores ac elemosinatos de accepcione operum misericordie quoad Deum. Nonne ista mundialitas retardat Christi presbiteros, ut ascendant ad speculam scripture in qua possent omnia pericula ecclesie a mundi principio usque in finem premuniendo ecclesiam speculari (ut notat scriptura Jeremie XXXI° et Ezechiel XXXIII°)? Notet secundo si ista copiosa mundana securitas facit istos speculatores sompniferos et ignaros ad ista pericula ecclesie previdendum, illos autem facit timidos ad pericula dampnacionis populi predicendum, et alios qui forent altilia facit reptilia, indispositos ad orandum pro subditorum salute, inter Deum et populum mediando, vel ad merendum sibi et aliis sacramenta ministrando vel evangelium predicando. Unde notaremus parabolam Christi, Luce XII°, ubi precipit cavere ab omni avaricia, quia non in diviciis cuiusquam vita eius est, sicut probat de quodam divite, sollicitante se circa inhorreacionem bonorum suorum, et eadem nocte fuit anima eius rapta per demones. Cogitaremus insuper illud Ezechielis XVI°, 49: Hec fuit iniquitas Sodome, sororis tue, superbia, saturitas panis et habundancia et ocium, que quatuor [p. 295] si sint in clero occasione dotacionis, imminet exinde periculum. Si autem occasio sit data vel accepta per accidens ex tali dotacione perpetua, ubi temporalis elemosinacio foret securior, patet periculum tam in elemosinante quam elemosinato isti seculari ritui innitendo. Deus autem necessitat divites huius seculi, ut continue ministrent clero in vite necessariis, quantum de clero est necessarium ecclesie militanti.

[ENGLISH]

## ¶2 · 295.9–296.6

> [p. 295] Et patet quod non est securitas domino seculari elemosinam suam taliter impertiri, cum veritas precipit sibi Luce XVI, 9, ut faciat sibi amicos de mammona iniquitatis, non autem spirituales et periculosissimos inimicos. Sed Matthei X, 36, dicit Christus: Inimici eius, domestici eius. Nulli enim plus subdole faciunt scisma in sancta matre ecclesia tamquam magis periculosi heretici quam illi qui videntur esse capitales ecclesie induti vestibus ovium. Unde quamvis tam de laicis quam de clero sint multi heretici, ut patet de tribus personis prescitis que relinquentur in finali iudicio (de quibus Matthei XXIV, 1), periculosior et communior heresis pululat in clero, cuius (ut alias exposui) sunt tres gradus. p Primus est quando in clero quis aspirat ad dignitatem ecclesiasticam symoniace pocius propter questum et fastum cum eis sequentibus quam meritorium officium spiritualiter serviendi. De ista heresi loquitur decretum Ia, q. I, sub auctoritate Gregorii sic dicentis: Fertur symoniaca heresis que prima contra ecclesiam Dei diabolica supplantacione surrepsit et in ipso ortu suo zelo apostolice ulcionis percussa atque dampnata est, in regni nostri finibus dominari. [p. 296] Tales enim hereticos debet superior in ecclesia et precipue verus Christi vicarius extirpare; omnis enim symoniacus est hereticus (ut patet Iª, q. I. Quisquis). Nec videtur apcior destruccio huius heresis quam tollere proprietatem temporalium gracia cuius est talis dignitas symoniace affectata.

[ENGLISH]

## ¶3 · 296.7–298.24

> [p. 296] Secundus gradus heresis a prelatis venandus et ab utroque brachio destruendus est, cum persona dotata ecclesie, que debet esse procurator, non dominus elemosinarum datarum pauperibus, ut patet in principio capituli huius et libro III Decretalium, De Donacionibus, cap°: Fraternitatem, cum, inquam, talis expendit bona ecclesie prodigaliter in pompa seculi vel consumit ipsa in cognacione vel affeccione carnali, aut tercio detinet thesaurum pauperum avare affeccione terreni commodi, tunc est periculosus hereticus sed periculosissimus persona conventualis istis condicionibus heresis maculata. Patet ista heresis, ymmo antechristiana vesania ex dicto beati Gregorii posito in decretis XVIª, q. VII, sic dicentis: Pervenit ad nos fama sinistra quod quidam episcoporum non sacerdotibus proprie diocesis decimas atque christianorum oblaciones conferant, sed pocius laicalibus personis, militum videlicet sive servitorum vel( quod gravius est) eciam consanguineis. Unde si quis amodo episcopus inventus fuerit huius divini precepti transgressor, inter maximos hereticos et pessimos antichristos non minimus habeatur, et sicut Nicena synodus de simoniacis censuit, et qui dat episcopus [p. 297] et qui recipiunt ab eo laici, sive pacto sive beneficio, eterni incendii ignibus deputentur. Et multo magis communitas que debet esse religiosior et est in isto peccato pertinacior et antichristus profundior, cuiusmodi forent religiosi, viventes seculariter, distribuentes bona pauperum cognacioni sue, ut fiat mundo inclitus, militaribus atque iuridicis, ut defendant suos redditus, et (quod foret pessimum) si darent cognacioni sue carnalibus et famulis inhabilibus presentacionem ad beneficia ecclesiastica virtute iuris patronatus. Et omnia ista innuit beatus Gregorius. Tercius gradus clericalis heresis est, cum sacerdos occupat statum et bona ecclesie sine hoc quod rependat debitum ministerium ad quod pretextu elemosine et acceptacionis solempnis officii obligatur; talis autem ut sic excommunicatur a domino, quia si laicus excommunicatur ab homine, eo quod iniuste detinet decimas vel elemosinas debitas sacerdoti, multo plus sacerdos excommunicatur a domino qui iniuste post maiorem obligacionem detinet spirituales elemosinas subditorum. Obligacio, inquam, est maior, cum non licet sibi elemosinas spirituales subtrahere eciam subdito subtrahente elemosinas corporales. Sacerdotes enim Christi debent benefacere persequentibus et diligere inimicos, et iterum subtraccio spiritualis elemosine est periculosior, cum minatur perpetuam perdicionem corporis et anime, sed neutrum tam evidenter subtraccio elemosine corporalis. Unde Jeremie XLVIII°, 10 dicitur: Maledictus qui facit opus domini fraudulenter; et multo magis est maledictus qui recipit onus ducatus gregis dominici, quem vel proditorie ducit in precipicium, vel fraudulenter omnino subtrahit ministerium, de quo dictum est libro VI°, [p. 298] cap. XX° et tribus sequentibus. Omnis autem excommunicatus eciam rite ab homine est hereticus, et evidencius omnis excommunicatus a Deo. Unde IVª, q. I Quod autem, sub auctoritate secunde synodi Nicolaus papa sic loquitur: Hereticos, inquiunt, dicimus tam eos qui ab ecclesia olim proiecti sunt, quam qui post hec a nobis anathematizati sunt. Porro si adhuc nec sic credatis, audite. Preter hos autem aiunt et eos qui fidem simulant confiteri scismaticos esse et eos qui seorsum a comunicantibus nobis episcopis collectas faciunt. Demum vero, et si quidam ab ecclesia super causis quibusdam reprehensi sunt et proiecti et excommunicati, sive ex clero sive ex laicali ordine. Dicimus omnes huiusmodi hereticos atque scismaticos. Unde glosa dicit ibidem quod omnis excommunicatus est hereticus, et allegat decretum, XXIIIª, q. IVª, Ipsa pietas, et XXIVª q. III, Illi. Et concordant dicta de heresi libro VI°. Omnis enim vel peccans mortaliter est ut sic divisus a communione sancte matris ecclesie quod sonat hereticus. to Item, omnis qui nititur auferre privilegium Romane ecclesie est ut sic hereticus; quod dissipantes legem de sacerdotum officio maxime faciunt in effectu.

[ENGLISH]

## ¶4 · 298.25–299.8

> [p. 298] Item, tales penun sunt nedum, quia negant fidem quam Christo promiserant in baptismo, in recepcione sacerdotalis ordinis et in recepcione illius officii, sed iurati sunt specialiter ad defendendum et retinendum (quantum sufficiunt) iura Romane ecclesie et regulas sanctorum patrum (ut patet III° Decretalium De Iure [p. 299] Iurando. Ego episcopus). Quod si in isto contra Romanam ecclesiam incurrunt periurium, quomodo non papa primus divideret eos a sua ecclesia cui tam proditorie sic illudunt? Heresis ergo symoniacorum in ingressu non per hostium, in progressu quo prodigaliter consumunt bona pauperum, et maxime in omissione debiti officii curatorum videtur inficere tam ecclesiam quam Romanum imperium.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 294.11: This false security hinders Christ's priests from warning the people.
- 295.17: The most dangerous heresy is common among the clergy and in three degrees:
- 295.24: 1. Clerks aspire to office in the Church for worldly ends;
- 296.7: 2. The clergy spend money wrongfully or hoard it;
- 297.12: 3, Priests receive the endowments but do not repay them with service.
- 298.22: It is heretical to infringe the privileges of the Roman Church and lawbreakers do this.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 294: *ad* (20 is the line number) [R3]
  - 295: *∅* (170c is a folio mark) [R3]
  - 295: *1* (x-height old-style 1) [R3]
  - 295: *zelo* (italic z clear) [NW]
  - 296: *Christi* [R3]
  - 296: *Iª* [R3]
  - 296: *diocesis* [NW]
  - 297: *∅* (coordinator: the main scan already has et qui recipiunt at pos 0-2 (the other scans voted p.296's dat there; OVERRIDE in part99)) [GAP]
  - 297: *gradus* [R4]
  - 297: *ut sic* (main token covers 170d ut * sic; folio mark and * dropped) [R4]
  - 298: *excommunicatus* (ex-/communicatus; main token holds whole word) [R4]
  - 298: *∅* (print ex-/communicatus; main already holds excommunicatus whole at pos 7) [INS?]
  - 298: *IVª* [R4]
  - 298: *XXIIIª* [R4]
  - 298: *IVª* [R4]
  - 298: *officio* [R3]
  - 298: *in* [R3]
  - 298: *effectu* [R3]
  - 298: *fidem* (25 is the line number) [R4]
  - 298: *Christo* [R4]
  - 299: *Iurando* (italic capital I; 170d folio mark) [R4]
  - 294: *ocium* [THIN]
  - 296: *enim* [THIN]
  - 298: *III°* (degree sign visible) [THIN]
  - 294: *superbia,* (4 is a margin numeral) [OVERRIDE-MARK]
  - 294: *quatuor* (qua- at foot of p.294, tuor at head of p.295 (leaf n0332); output token holds both) [OVERRIDE-MARK]
  - 294: *XII°,* (no verse; the 3 at line end is a margin numeral) [OVERRIDE-VERSE]
  - 297: *recipiunt* (print: et qui recipiunt ab eo (plate, agent 6); the other scans aligned p.296 dat here) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 294:
11. A in marg. : Nola honas considcracioncs. Nota contra securitatem
dotacionis. 3j. A Aj : odium.

p. 295:
9. A in marg.: Conclusio. i3. Ainmarg.: Conclusio. i5. A
in marg.: Conclusio. 21. A A^: XXIV: deest. 24. A in marg. :
In clero. A B in marg. : Nota tres gradus lieresis.
28. Decr. II pars, caus. I, q. I, cap. XXVIII.

p. 296:
7. A in marg.: Secundus gradus.
3. Decr. II pars, caus. I, q. I, cap. V. 11. Decretal. Greg. IX
lib. III, tit. XXIV, c. II. 19. Non ex dicto beati Gregorii
sed pocius Gregorii VII, vide Decret. II p., caus. I, q. III, c. XIII
et XVI, q. VII, c. III. Vide notam Friedbergii, corp. i. c. I, 417.
Hunc errorem et Johannes Hus (Opp. I, 194") recepit.

p. 297:
1. In decrct. leges: sive precio sive benclicio. 4. A A,: pertina-
cior — vivente deest. 5. A A, : particulariter distribuentes. 12. A B
in marg. : Torcius gradus.

p. 298:
1. A in marg. : Conclusio. i. A in marg. : Omnis rite cxcom-
municatus cciam ab homine cst hcreticus. 5. A A, : Hereticos
inquam; B: inquit; rccte inquiunt, sicut in decrct. supra memorata ct
infra: prcter hos "aiunt". 8. Jn decret. : audite quod subditur.
14. B: dicamus omnes.
3.4. Decr. II pars, c. IV, q. I, cap. II. 3o. Decr. Greg. IX,
lib. II, tit. XXIV, c. IV.

p. 299:
8. imperium; in cod. A sequitur: Myly Czechowe, id cst: Carissimi
Bohcmi. 10. A in marg.: Matcria pro dotacionc ecclcsie (Abovc
171" without mark 01 rcfcrencc). 16. A ui marg.: Rcsponsio.
```

---

## Chunk 14-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "299.10–302.2"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "617 words; 549 unanimous or majority-real; 54 settled by vote (R2 29, R3a 15, R3b 1, R5a 7, R6a 2); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n336–n339 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 1: [TITLE]

## ¶1 · 299.10–300.6

> [p. 299] Antequam respondeam ad magistrales obiectus, sunt duo dubia breviter transcurrenda. Primo, quomodo stat cum fide scripture dotacio Romane ecclesie. Videtur enim ex multis dictis superius expresse innui quod non sine gravi peccato altrinsecus potest tale privilegium temporale contra Christi privilegia introduci. Sed videtur probabile (ut alias sepe dixi) quod illa dotacio sicut et particularium ecclesiarum possunt sic racionabiliter colorari, quod seculares domini videntes quod vita exproprietaria qualem Christus et sui apostoli vixerant est seculari ac civili conversacione perfeccior, et sic ad exonerandum eos, ad accumulandum eis meritum, ad multiplicandum milites Christi qui distrahant mundum a vita mundana, cum talis sit ad multiplicandum religionem Christi habilior, dederunt titulo elemosine suum seculare dominium, non ut sacerdotes Christi civiliter aut seculariter dominentur, sed ut servantes humilitatem, paupertatem et penalitatem priorem fideliter ministrent pauperibus elemosinas ad hoc datas, ut vel sic distraheretur mundus a conversacione civili et ritu quem [p. 300] ante Christum observaverant mundiales. Nec credo quod ista condicione dimissa nec secularium dotacio nec cleri Christi admissio cum religione Christi sit compossibiliter sustinenda; talis autem dotacio, sonans in puram et perpetuam elemosinam, utrimque est tota trinitate auctorizabilis et fundabilis in scriptura.

[ENGLISH]

## ¶2 · 300.7–300.17

> [p. 300] Sed hic recalcitrant moderni prepositi, dicentes quod licet eis civiliter ac seculariter dominari, et quod secularis dominacio fuit iurepoli debita Christi vicariis, cum Christus dominatus fuit seculariter toti mundo. Unde (ut inquiunt) Constantinus non dotavit ecclesiam, sed illud dominium quod ipse ac predecessores sic occuparunt tyrannice, humiliter et debite diviserunt, unde Christus, Petrus, Clemens et alii precedentes beatum Silvestrum habuerunt ius plenum ad totum imperium, sed non erant in possessione ante concessionem humilem Constantini.

[ENGLISH]

## ¶3 · 300.18–302.2

> [p. 300] Et inter omnes hereses dissipantes religionem christianam et fidem scripture hec est una precipua. Primo, inquam, claudicat in hoc quod dicit Christum habuisse ius ad dominandum civiliter, cum conversacione et sermone secundum testimonia sanctorum doctorum exponencium fidem evangelii docebat oppositum. Ipse enim dicit Luce, IX°, 58: Vulpes foveas habent et volucres celi nidos, filius autem hominis non habet ubi caput suum reclinet. Super quo dicit venerabilis Beda super Lucam lib. II°, c. IV°: Quid me propter divicias et seculi lucra cupis sequi, cum tante sim paupertatis ut nec hospiciolum quidem habeam et non meo utar tecto? Et ad istum sensum illud exponitur a beato Jeronymo nec contrarie ab aliquo sancto (ut alias explanavi). [p. 301] Item, si Ghristus et sui apostoli habuissent ius ad civiliter dominandum, et faciliter ex oblacione mundi potentum possent fuisse positi in possessione pacifica, ut patet de Evangelista et aliis sanctis: sequitur quod ex desidia fuissent valde culpabiles, cum possent ita faciliter quesivisse ius sibi et sue ecclesie et excusasse sibi iniuriantes a sua intrusione. Hoc autem est contra evangelium Luce XXII°, ubi decidens questionem de maioritate inter apostolos dicit quod opposito modo se habet ad ritum gentilem, cum maioritas inter eos attenditur penes maioritatem servicii ex humilitate maiori. Ex quo Iª Petri V°, 3, capit ipse pro principio quod sui clerici non sint dominantes in clero. Item, illud est expresse contra iura canonica, cum sub auctoritate Augustini, distinccione VIIIª canon sic loquitur: Quo iure defendis villas ecclesie divino vel humano? Divinum ius in divinis scripturis habemus, humanum ius in legibus regum. Unde quisquis possidet quod possidet? Nonne jure humano? Nam iure divino domini est terra et plenitudo eius. Pauperes et divites una terra supportat. lure ergo humano dicitur: Villa hec mea est. Tolle, inquit, iura imperatoris et quis audet dicere: Villa hec mea est, meus est iste servus, mea est hec domus? Si autem ut teneantur ista ab hominibus, regum iura fecerunt, vultis reticeamus leges ut gaudeatis? Unde infra, XCVIª distinccione, Constantinus, incorporat ecclesia cartam cesaris sub forma qua dotavit ecclesiam. Cum ergo lege scripture, lege sanctorum doctorum et iuris canonici non sit fundabilis secularis dominacio cleri [p. 302] Christi, qua temeritate sompniarent discoli istam blasphemiam?

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 299.10: Two doubts to be solved: 1. Whether the endowment of the Roman Church is consistent with the faith.
- 299.22: Probably in its first intention it was directed to help the clergy to minister more effectually;
- 300.1: and otherwise it is certainly not consistent with Christ's religion,
- 300.7: Modern prelates say that Christ was ruler over the world and they inherit his rights (as vicars).
- 300.18: This is a great heresy:
- 300.21: I. as contrary to Christ's teaching;
- 301.1: He and his apostles refused all civil power.
- 301.15: 2. It is against the canons.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 299: *CAP. XIV.* [HEAD]
  - 300: *credo* (171a folio mark and A margin letter) [R3]
  - 300: *cleri* [R3]
  - 300: *quod* ('ruler' is English side-note) [R4]
  - 300: *cum* [R3]
  - 300: *filius* (italic f clear) [NW]
  - 300: *lib* [NW]
  - 300: *II°* [R3]
  - 301: *Iª* [R3]
  - 301: *XCVIª* [R3]
  - 302: *Christi* [R3]
  - 300: *Christum* [THIN]
  - 300: *Christi* [R4]
  - 301: *XXII°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 299:
8. imperium; in cod. A sequitur: Myly Czechowe, id cst: Carissimi
Bohcmi. 10. A in marg.: Matcria pro dotacionc ecclcsie (Abovc
171" without mark 01 rcfcrencc). 16. A ui marg.: Rcsponsio.

p. 300:
1. A in marg. : Contra dominacionem civilem clcri (Bclow 171» without
mark of referencc). 7. A B in marg. : Opinio heretica. 24. In
codd.: Luce VIII. 27. A in marg. : Beda. 29- A: ut nec;
sequitur lacuna. A,: meum hospiciolum.
27. Beda in Lucae evangelium Opp. tom. V, pag. 262.

p. 301:
]S. 19. A Ax: scriptumhabemus ; B: scriptis; Corr. e canone.
20. A A,: possideret.
16. Decr. I pars, dist. VIII, c. I. 28. Dec. I pars, dist.
XCVI, c. XIV.

p. 302:
8. A:adTim. 27. A: deitatem deitatem ; A, : divinitatem dcitatem.
```
