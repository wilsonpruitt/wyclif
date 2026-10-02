# Translation brief: ecclesia 16-a–16-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-16-a.md chunks/ecclesia/wyc-ecclesia-16-b.md chunks/ecclesia/wyc-ecclesia-16-c.md` once and fix what it reports.
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

## Glossary (the 175 rows these chunks use; the full file is GLOSSARY.md)

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
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
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
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
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
| dotacio | endowment | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| claustrales | cloisterers | Ruled 2026-09-28 (20 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| illabi | to flow into | Ruled 2026-09-28. |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "one given alms". Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |

---

## Chunk 16-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "359.6–363.12"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "890 words; 798 unanimous or majority-real; 80 settled by vote (R2 49, R3a 23, R5a 6, R6a 2); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n396–n400 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 1: [TITLE]

## ¶1 · 359.6–359.13

> [p. 359] Post hec dubia respondendum est ad magistrales argucias quas doctores obiciunt contra dicta. Arguitur primo quod beatus Silvester, recipiendo dotacionem perpetuam ecclesie pro se et suis successoribus nullo modo peccavit, et libenter acceptarem argumenta ad istam partem, quia quamvis neutram partem asseram, pars tamen isti opposita est mihi credibilior.

[ENGLISH]

## ¶2 · 359.14–360.2

> [p. 359] Prima itaque racio sic formatur: quam licite recipiunt sancti elemosinas pro relevandis indigenciis presentis vite, tam licite ipsas elemosinas servant idem sancti distribuendas indigentibus in perpetuum. Non enim videtur racio diversitatis quin, si licet recipere elemosinas propter indigenciam propriam relevandam, a pari erit licitum ipsas elemosinas sic collatas propter indigenciam futuram perpetuo conservare; ergo si licet indigenti recipere elemosinas propter se relevandum et hoc absque peccato, a pari licet conservare elemosinas sic receptas in perpetuum ad usus pauperum absque peccato. Sed beatus Silvester in faciendo sibi licitum simpliciter nullo modo verisimiliter peccavit; ergo beatus Silvester in retinendo dotacionem [p. 360] perpetuam ecclesie nullo modo verisimiliter peccavit.

[ENGLISH]

## ¶3 · 360.3–362.27

> [p. 360] Quantum ad istud argumentum, non oportet respondere ad formam, nec vidi probacionem assumpti, cum Ghristus recepit elemosinas temporales, sicut etapostoli ab ipso receperant pro temporali indigencia pauperum relevanda (ut patet Joh. VI°), et tamen non legitur apostolos recepisse elemosinas pro pauperibus perpetue conservandas. Et quantum ad illud brogardicum, ergo per idem vel questionem vagam que est ultimum refugium simplicis arguentis qua queritur que sit racio diversitatis, retorqueo utrumque in arguentem. us Si Christus docuit nos in suis apostolis non solicitari in crastinum, quia sufficit diei malicia Matthei VI° et non videtur racio, quare non preciperet eis providere de elemosinacione perpetua, per idem preciperet eis providere de elemosinacione perpetua; vel racio diversitatis confirmatur ex hoc quod tempore apostolorum fuerunt homines devociores et ad elemosinas prompciores et post avariores, ergo fuisset congruum quod ipsi obligassent suos heredes ad elemosinas perpetuas. Si dicatur quod voluntas Christi est racio diversitatis sufficiens, revera sic doctrina Christi exemplata future ecclesie est racio diversitatis, et forma sufficiens ad movendum nos clericos ritum gentilem deserere et omnem solicitudinem nostram inpresenciarum proicientes in ipso confidere. Non solicitemur ergo quomodo providebitur nunc ad mille annos Lhnsti pauperibus de pabulo corporali, sed permittentes mortuos sepelire mortuos suos sequamur Christum attencius et sic christianis futuris ad mille annos magis proficimus, et ita (ut dixi superius) perpetua elemosinacio est dotanti inductivumblasphemesuperbie et elemosinatofomentum mundane confidencie et vigilanter requirendi divinum [p. 361] Bauxilium aversive desidie, et utrumque istorum per elemosinacionem temporalem excluditur. Et istam racionem assignant doctores, quare Deus non particulariter premunivit primos parentes, ut caveant de calliditate serpentis promissa eius fallacia detestando. Nam dixit illis illabendo generale principium, cui innitentes, prudenter confidendo in domino et consulendo ipsum in ambiguis, amplius meruissent, et sic negata penultima consequencia negatur assumptum sequens, scilicet quod beatus Silvester in faciendo sibi licitum simpliciter nullo modo verisimiliter peccavit. Nam omnis conversacio secularis est inseparabiliter cum peccato, sicut dicit fides scripture et Augustinus persepe commemorat; et cum multe conversaciones seculares sint licite ac meritorie, patet quod beatus Silvester in faciendo sibi licitum sepe peccavit, sicut de se confitetur beatus Evangelista qui fuit Silvestro sanccior. Unde notet homo formam dotacionis, XCVIª dist. Constantinus, quomodo imperator tribuit Silvestro potestatem, vigorem et honorificenciam imperialem, decernendo quod habeat primatum super quatuor sedes et princeps sacerdotibus tocius mundi existat. Consideret secundo quomodo tradidit beato Silvestro et successoribus suis Lateranense palacium, diadema et frigium, superhumerale, clamidem purpuream et tunicam coccineam cum aliis insigniis et potestatibus imperialibus, et breviter cum omnibus dignitatibus quas papa vendicat non fundabilibus ex scriptura, ut puta, quod equitet super equum candidum cuius frenum cesar tenuit et alias reverencias quas mundo cecati in ipsis preponderant sibi exhibuit. Nam illud [p. 362] affeccione ceca quis tribuit quod in se reputat preciosum. Consideret ergo evangelicus attente ordinem predicte carte, et miror si excuset beatum Silvestrum ab omni elacione, ab omissione contemptus mundi et defectu informacionis imperatoris et populi. Unde exhinc irreligiose accepta fuit occasio faciendo scisma in ecclesia instinctu dyaboli, ut notat decretalis, XCVª dist., Olim, ex dicto Jeronimi. Et hec creditur racio, quare ecclesia orientalis remanens in sua pauperie detestata est monstruosam superbiam occidentalis ecclesie. Unde legitur quod ecclesia Grecorum misit domino Johanni pape XXII magnam epistolam ad exhortacionem suam qua suadebat eos sue coactive iurisdiccioni subici plenarie responsivam et in fine inseruisse talem clausulam: Potenciam tuam summam super tuos subditos firmiter credimus, superbiam tuam summam tollerare non possumus, avariciam tuam summam saciare non intendimus, dominus tecum, quia dominus nobiscum est. Consideret ergo procurator Romane ecclesie cum approbabili: beatus Augustinus fuit sciencior, religiosior et sanccior beato Silvestro; ipse autem asserit irrevocabiliter cum aliis sanctis eum sequentibus. si quid utile est, in scriptura sacra invenitur, et moneat ut fautores illius dotacionis dicentes quod fuit omnino sine peccato ipsam fundent clarius ex scriptura, quod nulli usque hodie potuerunt.

[ENGLISH]

## ¶4 · 362.28–363.12

> [p. 362] Et si obicitur quod eque evidenter credendum est errori cuiuscunque hominis in scriptis sicut in factis, et sic periret testificacio ex scripturis. Sed quod falsum assumitur (ut beatus Augustinus declarat epistola VIIIª ad Jeronynum), cum ex veritate scripture [p. 363] credimus quod propheta David peccavit cum uxore Urie et quod Petrus peccavit tempore passionis et post ascensionem, tamen scripta eorum credimus esse summe autentica, et sic maiori probabilitate credimus scriptis famosorum doctorum quam nudis factis, tum quia communiter ex maiori deliberacione, ex minori temptacione et pro ulteriori explanacione scribunt personis gravibus nec posterius revocant. Sed alii multi sancti post et ante in sentenciam illam concordant, sed (ut reor) nec ex scriptura nec racione fundabitur quod beatus Silvester non peccavit recipiendo dotacionem cesaream.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 359.6: The doctors object:
- 359.8: 1. that Silvester did not sin at all in accepting endowment;
- 359.14: for if it lawful to receive alms, they may be kept without sin.
- 360.3: Answer: This is a mere begging of the question.
- 360.13: Christ bade us not to be careful for the morrow;
- 360.27: What business have we with providing 1000 years in advance?
- 361.1: An act may be forbidden by a general precept as much as by a special prohibition.
- 361.19: The form of the gift to Silvester shews that it was tainted with worldliness,
- 362.2: and makes it impossible to free Silvester from blame.
- 362.8: His acceptance became the occasion of schism.
- 362.28: It is objected that men err also in their writings,
- 363.1: but we accept the writings of David and Peter although they sinned.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 359: *CAP. XVI.* [HEAD]
  - 360: *VI°* (print: Matthei VI°, 34) [R3]
  - 360: *mille annos* (main token covers two printed words) [R5]
  - 361: *Et* (capital E; 179b is the folio mark) [R4]
  - 361: *XCVIª* (C 1 are alinea letter and argument numeral) [R3]
  - 362: *affeccione* [R3]
  - 362: *XCVª* [R4]
  - 362: *Et* [R3]
  - 362: *VIIIª* [R4]
  - 362: *quis* [THIN]
  - 363: *et* (David is in the English side-note (writings of David and Peter), not the Latin line) [R4]
  - 361: *seculares* (secu-/lares; output holds both halves) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 359:
2. B : subtraccio et suscepcio. 4. scriptura sacra ; A : Scquuntur lingua
Boliemica aliquot verba: Lecz na kawczye horze v Prahy est fundata
newyem. Id est: Si in monte apud Pragam est fundata nescio. 6. A in
marg. : Nota bene istam totam columpnam, quia ponuntur fundamenta pro
dominacion ecivili cleri (Below iy8d without mark of reference). i5. A in
marg.: Prima racio. Nota argumenta pro dominacione cum solucionibus
(Above 179" without mark of reference). 14. B : qui licite. i5. AA, :
pro — elemosinas deest. 20. Codd.: quin a pari.

p. 360:
3. A in marg. : Responsio. 4. 5. B: assumpti Christus. 9. bro-
gardi cum in codd. 10. B in marg : Questio vaga que est ultimum
refugium simplicis arguentis. Hic notatur. 23. 24. B: exemplativa.

p. 361:
19. A in marg.: Nota formam dotacionis per Constantinum.
19. Vid. Decret. I pars, dist. XCVI, c. XIV. Et sequencia ex
hac decretali deprompta sunt.

p. 362:
3. B: minor. i5. A B in marg.: Nota epislolam Grecorum.
20. B: procreator Romane. 21. A Ax: et sanccior deest. 32. In
codd.: nona. Vide Aug. Opp. II, pag. .(5.
7. ib. dist. XCV, cap. V.

p. 363:
i3. A in marg. : Secunda racio. 18. A in marg.: Responsio.
```

---

## Chunk 16-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "363.13–365.6"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "452 words; 400 unanimous or majority-real; 48 settled by vote (R2 30, R3a 12, R3b 2, R5a 3, R6a 1); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n400–n402 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 2: [TITLE]

## ¶1 · 363.13–364.6

> [p. 363] Secundo sic arguitur: Quidquid fuerit meritorium beato Silvestro, nullo modo fuit sibi demeritorium, cum iste denominaciones ex opposito distinguuntur, sed fuit meritorium beato Silvestro recipere temporalia distribuenda pauperibus in perpetuum, hoc idem nullo modo fuit sibi demeritorium. Hic dicitur quod theologus logicus ponit calumpniam in maiori, cum idem opus successive est prius meritorium, et post demeritorium vel econtra; et sic conversacio beati Silvestri que ante baptizacionem vel conversionem fuit sibi demeritoria postea fuit sibi meritoria. Sic enim dicimus motum difformem quoad tempus vel subiectum, licet maior pars eius quantitativa fuerit uniformis. Minor autem non probatur, sed sub verbis illis capit calumpniam, quia nimis onerosum foret tali sancto recipere tale perpetuum officium, sive in se sive in suis ministris; nec probatur minor ista per hoc quod relevare pauperes indigentes est simpliciter meritorium cuicunque, tum quia multi sunt quibus hoc non convenit, tum secundo quia multis infidelibus et ypocritis in hoc demerentibus hoc convenit, tum tercio quia hoc dato non exhinc sequitur quod meritorium fuerat beato Silvestro recipere elemosinas [p. 364] distribuendas pauperibus in perpetuum. Sed finaliter, dato quod hoc fuit meritorium, sic quod nullo modo demeritorium beato Silvestro, non exhinc sequitur quod beatus Silvester nullo modo peccavit sic faciendo. Homo enim peccat venialiter merendo continue et non demerendo sed remissius promerendo.

[ENGLISH]

## ¶2 · 364.7–365.6

> [p. 364] Tercio sic arguitur: Quicquid potuit Silvester papa licite et absque peccato in usum suum recipere,; potuit sic recipere in usus aliorum; sic enim absque peccato recipiunt domini temporales predia, redditus et huiusmodi, tam sibi quam aliis, sed licite et absque peccato eciam veniali recepit Silvester temporalia privilegia pro se ipso; ergo sic fecit vel potuit pro aliis.: Hic respondeo concedendo asumptum et conclusionem illatam, sed non credo aliquos sanctos asserere dominos temporales absque peccato recipere redditus temporales, cum vivens activam vitam peccat continue mortaliter vel venialiter; et sic non credo quod absque peccato veniali recepit Silvester temporalia privilegia pro se ipso. Credo tamen quod potuit taliter recepisse, cum potuit fuisse in puro statu innocencie cum toto suo genere, et sic iure status innocencie recepisse immediate a domino usum et dominium temporalium. Sed ulterius pro materia argumenti concedo, primo quod omnis predestinatus habet tituluml et dominium super omnia temporalia privilegia cuiuscunque, cum pro tempore suo constituitur super omnia bona Dei; hoc tamen est impertinens doctori, cum post hanc vitam immediate a Deo ad usum poli recipitur tale dominium. Secundo notandum quod domini temporales recipiunt licite et meritorie pro se et heredibus suis in perpetuum civili titulo redditus et proventus, tam propriorum dominorum quam filiorum [p. 365] nobilium subditorum quorum custodia est in manus dominorum capitalium devoluta, sed sicut non vivunt hanc vitam sine peccato, sic non exercent actus tales civiles sine veniali, illud tamen quod foret in domino seculari licitum et meritorium foret in sacerdote Christi dampnabile.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 363.13: Objection: 2. Silvester did right in accepting a gift for the poor and an act cannot be both right and wrong.
- 363.24: Answer: The same act may be now right and now wrong.
- 363.30: Moreover we do not allow that Silvester did right.
- 364.1: and even if right on the whole, the act might be accompanied by sin.
- 364.7: Objection: 3. Silvester might receive a gift for himself without sin; why not for others?
- 364.15: Answer: Sin accompanies all active life;
- 364.29: and, although lords may rightly perform civil acts,
- 365.2: yet such acts may be damnable in a priest.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 364: *papa* (E is the alinea letter) [R3]
  - 364: *licite* [R3]
  - 365: *licitum* [R3]
  - 365: *Christi* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 363:
i3. A in marg. : Secunda racio. 18. A in marg.: Responsio.

p. 364:
7. A in marg.: Tercia racio. Domini temporales continue vivunt vitam
non sinc peccato. i5. A in marg.: Responsio.

p. 365:
7. A in marg. : Contra dominacionem cleri (Above 1794 without mark
of reference). ir. A A, : utrumquc inquam. 14. A Aj : civilis
ditacio. 21. A in marg.: Nota clerus habet dominacionem cvange-
licam a Christo super omnibus rebus mundi. 23. Codd. usum-
fructum. 28. B: aliis sancti.
```

---

## Chunk 16-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "365.7–368.28"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "821 words; 705 unanimous or majority-real; 103 settled by vote (R2 71, R3a 29, R3b 1, R5a 2); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n402–n405 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 3: [TITLE]

## ¶1 · 365.7–368.28

> [p. 365] Unde minus remotum est a sacerdocio Christi recipere a dominis temporalibus alternatum usum uxorum suarum secundum copulam carnalem (quod credidit Nicolaus dyaconus fuisse licitum), quam quod recipiant a seculari domino dominacionem civilem; utrumque enim istorum foret horribile, sed secundum horribilius, cum carnalis procreacio stat cum sacerdocio, non autem civilis dominacio. Ideo inniti ad dotacionem civilem cleri Christi non foret sui vel sacerdotum eius honoracio, sed detestanda turpacio, quia de clero qui prius fui-t nude de sorte domini, faceret apostatam de sorte seculi. Ideo domini temporales dant clero titulo elemosine quidquid et quantumcunque voluerint et non deturpant eos dominacione civili. Tercio notandum quod Deus dedit beato Petro et toti generi suo secundum spiritualem imitacionem dominacionem evangelicam et usufructum super omnia bona mundi, non autem dominacionem vel usum civilem, quia illa proprie consummatur ab homine, prima autem donacio non consummatur ab aliquo preter dominum, cum solius Dei sit illa generacio; quamvis enim apostolus et alii sancti predicatores genuerunt filios Dei ex semine verbi sui, tamen primogenito iam mortuo tribuenda est generacio cuius semen suscitat frater iunior, de quanto participative dicitur ipse Christus. Sed circa talem genituram filialem vel sucessionem [p. 366] vicariam non sit contencio, cum quotquot receperunt cum caritate consummata dedit eis potestatem filios Dei fieri; illos autem non constituit humana eleccio, cum ubicunque terrarum clericus vel laycus post ascensionem edificat ecclesiam sanctam cuius est membrum, ipse est tam Christi quam Petri vicarius. Et stat quod aliquis solempnitate, ritu et reputacione humana sit reputatus Christi vicarius, cum hoc quod sit horrendus dyabolus, ut non est incredibile de Gregorio XI. et multis ei similibus. Nam si maritavit Raymundum nepotem suum cum herede Bolonie mediantibus decimis et bonis pauperum ecclesie Anglicane, si sustentavit iuxta fastum seculi multas parentum suorum familias, si redemit dignam captivitatem fratris sui et fecerit occidi multa millia hominum pocius propter secularem questum quam propter salutem eorum per patrimonium crucifixi, si insuper catholicaverit quod secundum potestates clavium errare non poterit, nec finaliter fructuose penituerit, quis dubitat quin fuit perpetuus hereticus, nunquam caput vel membrum sancte matris ecclesie, quia secundum Augustinum in libello De Decem Cordis vir finaliter infidelis non est caput mulieris membri ecclesie? Hec autem non impono sibi, sicut faciunt superiores persone ecclesie, sed dico quod nec ipse nec alius est Christi vel Petri vicarius nisi relinquens mundanum ritum imitetur eos in moribus, et sic stat quod pretensus Romanus pontifex sit caput membrorum dyaboli, et in hoc iacet periculum humane dotacionis perpetue, cum sepe occasione illius cadit distribucio fertilior bonorum pauperum super membra diaboli. [p. 367] Quarto arguitur ponderancius propter gravedinem argumenti sic: Nullus obligatus sub pena peccati mortalis ad recipiendum temporalia pro se et suis successoribus in perpetuum in hoc peccat, sed Silvester fuit obligatus sub pena peccati mortalis sic recipere elemosinas a Constantino, ergo in hoc nullo modo peccavit. Hic dicitur quod utraque pars antecedentis capit calumpniam, nam multi sunt actus ad quorum obligacionem homines inducuntur, eciam sub pena peccati mortalis occasione precedencium peccatorum, quos actus faciendo peccant vel mortaliter vel venialiter. Sic enim peccatum illaqueat multos insolubiliter ad peccandum, et hinc (ut notat Augustinus) Psalmista rogat de necessitatibus liberari, sed quamvis homo sit in multis casibus necessitatus ad peccandum, tamen et poterit faciliter non peccare, et non a Deo sed a peccato capit necessitatem ut peccet, non tamen debet vel tenetur peccare. Ut autem ista sentencia palpabilius videatur, pono primum exemplum in quo quis sub pena mortalis teneatur reddere debitum uxori pro excusanda utriusque libidine, et in reddicione peccet mortaliter aut venialiter; nulli dubium quin casus sit possibilis et sepe accidens. Pono secundum exemplum in quo abbas teneatur sub pena mortalis recipere onus sue ecclesie ad regulandum religiose suum capitulum, ad dispensandum fideliter egenis elemosinas quas recipit ad hunc usum, et ad vivendum in se et suo capitulo inseculariter secundum regulam traditam a patrono. Et pono de [p. 368] possibili quod electus ad illud officium peccet, inor-i8o°H dinate aspirando ad honorem et cultum seculi et imprudenter dispensando bona pauperum; et patet contradictorium maioris assumpte. Pono tercium exemplum in quo quis tenetur accipere eukaristiam et eam indigne accipiat, et patet quod in faciendo illud quod debet facere peccat mortaliter propter defectum modi faciendi, sicut in maiori parte accidit in accipiendo ecclesiasticum beneficium. Sed longe aliud est dicere, Petrus obligatus sub pena mortalis recipere datum onus in hoc peccat, et in quantum recipit illud onus in tantum peccat; nam prior proposicio dicit in reduplicacionem concomitanciam et secunda dicit reduplicacionem causalem. Minor eciam argumenti est falsa, quia non est deducibile quod Deus vel scriptura sacra obligavit beatum Silvestrum sub pena mortalis recipere elemosinas secundum illam formam a cesare sed religiosius fecisset, informando cesarem quod caput ecclesie Christus in cuius virtute sanatus est aufugit honores mundanos et proprietatem civilem. Ideo superioribus sacerdotibus suis non incumbit tam grave officium ministrandi pauperibus, sed inferioribus dyaconis et laycis quibus incumbit abiectum sed in gradu suo meritorium ministerium, nec alium primatum docuit Christus apostolos suos appetere nisi ex veritate prima sequentem maioritatem quoad Deum racione humilioris ministerii (ut docetur Luce XXII°).

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 365.7: Civil dominion is more inconsistent with priesthood than is fornication.
- 365.21: God gave Peter an evangelical dominion over all things but no civil dominion.
- 366.6: A man may be reputed Christ's vicar and yet be a devil, as is not incredible of Gregory XI.
- 367.1: Objection: 4. Silvester could not refuse Constantine's alms without mortal sin.
- 367.10: Answer: A man may so involve himself that he cannot excape sin.
- 367.19: Examples.
- 368.15: There is no evidence that Silvester would have sinned in refusing.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 365: *licitum* (print: licitum),) [R3]
  - 365: *utrumque enim* (main token covers two printed words) [R4]
  - 365: *cum* [R3]
  - 365: *imitacionem* [NW]
  - 366: *aliquis* [NW]
  - 367: *in* [R4]
  - 367: *mortaliter* [NW]
  - 367: *venialiter* (print veni- / aliter; main token holds the whole word) [R4]
  - 367: *∅* (aliter is the tail of veni-aliter (pos 77); print: aliter. Sic) [INS?]
  - 367: *secundum* (30 is the line number) [R4]
  - 368: *dinate* (second half of inor-/dinate (pos 7)) [NW]
  - 368: *Christus* [R3]
  - 368: *XXII°* (print: Luce XXII°).) [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 365:
7. A in marg. : Contra dominacionem cleri (Above 1794 without mark
of reference). ir. A A, : utrumquc inquam. 14. A Aj : civilis
ditacio. 21. A in marg.: Nota clerus habet dominacionem cvange-
licam a Christo super omnibus rebus mundi. 23. Codd. usum-
fructum. 28. B: aliis sancti.

p. 366:
6. A in marg.: Nota de papa. 21. A: num caput. A,: non caput.
22. A in marg. : Augustinus. 26. A in marg. : Quarta racio. Nota
quis est vicarius Cliristi vel Petri (Above 180" without mark of reference).
22. Sermo IX De Decem Chordis Opp. tom. V, pag. 5o.

p. 367:
7. A in marg. : Responsio. B in marg. : Multi sunt actus quos obligamur
perlicere sub magna pena, quos implendo peccamus mortaliter. i3. B:
hic ut notat. 19. A in marg. : Nota. 22. A: libine.
i3. Aug. De Natura et Gracia contra Pelagium cap. LXVI.
Opp. tom. X, pag. 161, De Perfeccione iustitiae hominis ibid.
tom. X, pag. 170 etc.

p. 368:
i3. A: reduplicacione sive reduplicative. 21. B: mundanos in
proprietatem. 29. A in marg. : Nota defectus beati Silvestri (Above
iSob without mark of reference).
```
