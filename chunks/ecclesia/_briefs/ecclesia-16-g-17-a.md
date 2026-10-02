# Translation brief: ecclesia 16-g–17-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-16-g.md chunks/ecclesia/wyc-ecclesia-16-h.md chunks/ecclesia/wyc-ecclesia-17-a.md` once and fix what it reports.
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

## Glossary (the 202 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
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
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
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
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| subdominans | holding lordship under | Beside *dominari*. Ruled 2026-10-02 (*Eccl.* 15, 339.6). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |

---

## Chunk 16-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "380.31–384.33"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1010 words; 871 unanimous or majority-real; 123 settled by vote (DEL 1, INS 1, R2 86, R3a 29, R3b 3, R5a 2, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n417–n421 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 7: [TITLE]

## ¶1 · 380.31–381.26

> [p. 380] Item, iuxta tacta papa videns dissensionem oriri ex occupacione civilis dominii, et sibi ac clero suo per seculares posse procurari subsidium in casu quo illis dominacionem illam relinqueret, non foret plenus et [p. 381] perfectus dominus eorum nisi posset ad relevamen sui et sui generis de suis subsidium procurare, ut tactum est de milite captivo, sed papa est utilius, plenius et perfeccius dominus patrimonii Crucifixi quam alius secularis: ergo licet sibi in casu sic facere; ymmo si credit vel credere debet verisimiliter quod status ille foret sibi et toti suo generi perfeccior, securior atque tranquillior, videtur quod sub pena peccati gravis debet sic facere, nam sic utilius possiderentur a sancta matre ecclesia. Item, religio quam Christus instituit de nolendo possidere pecuniam fuit perfeccior, solempnior: et obligacior quam privilegiacio cesarea, ergo cum ad dispensacionem unius non apostoli licuit religionem ,5priorem deserere, et licet privilegium secundum relinquere. Sic enim ex causa potest celebrari divorcium inter virum et uxorem; ymmo (ut fingitur) licet clero separare animam a corpore in quocunque, qui dominacioni sue restiterit; et sic hoc luciferinum vinculum foret forcius quam vinculum gracie vel nature, et tunc indubie Deus malus superat Deum bonum. Dicunt enim quod verbum nedum humanitatem assumptam sed totam ecclesiam potest dimittere, sed clerus possessionatus non potest dominacionem deserere, sed abrasio capillorum nostrorum testatur quod non debet esse tam fortis nexus inter nos et bona fortune.

[ENGLISH]

## ¶2 · 381.27–382.7

> [p. 381] Ex quibus videtur quod propter ingratitudines secundum quas volumus de dominorum elemosinis in secularitate superare ipsos dominos et propter hereses quas in materia de dominio nostro defendimus, ex una parte abutententes elemosinis et ex alia parte subtrahentes debitum de spiritualibus elemosinis rependendis, videtur quod patroni elemosinarum debent ipsas a nobis subtrahere et vere ecclesie Christi restituere, cum totus finis laudabilis sit eversus, et [p. 382] specialiter si peccamus subdole pretermisso ordine correpcionis evangelice inconsultis episcopis, ut aput nominetenus papam et cardinales, inimicos regni nostri precipuos, leges regni nostri et regaliam regis tamquam hereticam condempnamus. Iste enim videretur contemptus notabilis indiscreti doctoris cum suis complicibus.

[ENGLISH]

## ¶3 · 382.8–382.13

> [p. 382] Octavo et ultimo arguitur per hoc quod cuilibet domino temporali non solum est licitum sed mentonum emere hereditatem et bona eterna pro bonis temporalibus, et cum maius bonum temporale sit dignius maius bono spirituali, sequitur quod amplius et diucius dotans ecclesiam intensius meretur beatitudinem.

[ENGLISH]

## ¶4 · 382.15–382.16

> [p. 382] Ad istud argumentum dixi superius quod quilibet dives seculi tenetur sub pena peccati mortalis emere

[ENGLISH]

## ¶5 · 382.17–383.34

> [p. 382] sibi beatitudinem per suas divicias, non quod cuilibet beatificando sit precium illud necessarium sed quod habens terrenam potestatem atque divicias utatur eis ad utilitatem ecclesie, et sic episcopi et religiosi possessionati tenentur precipue emere sibi beatitudinem per dispensacionem prudentem elemosinarum dandarum pauperibus. Verumptamen non oportet ut altera pars ecclesie vendat vel emat regnum illud civiliter, nec quod dominus secularis det dominacionem suam clericis, sed quod caveat ut faciat elemosinam suam in abscondito cum nesciencia manus sinistre quid faciat dextera, non dampnificando proximum dando sibi occasionem relinquendi perfeccionem suam primevam, nec ut onerosus factus subditis iniuste detineat eis debitum, que omnia fiunt hodie occasione dotacionis perpetue. Nam exhinc prelati dicuntur sompniferi vel ignari, subditis in equis, familia et exaccionibus onerosi. Unde non est credendum quod cesar proporcionaliter ad quantitatem bonorum que dicitur dedisse ecclesie [p. 383] cleri sic meruit, tum quia magnitudo elemosine ex dictis non taliter mensuratur, tum eciam quia iuxta adversarios non fuit nisi nimis stricta restitucio alieni. Sed quomodocunque sit de istis, verisimile est quia Cesar cecatus tumebat superbia, et sic tam elemosinantes quam elemosinati peccant communiter, sicut quilibet viator sciens vel probabiliter credens quod religio vel conversacio alia sibi faciliter adquiribilis esset sibi melior, et tamen quiescit torpide in vita quam reputat sibi minus meritoriam vel minus utilem sancte matri ecclesie, ut sic peccat; et ad arbitrandum hoc requiritur mentis purgacio, status et circumstanciarum discrecio sed omnino scripture sacre consulcio. Contingit enim quod rex vel alius seculi potentatus videns obstinaciam cleri et populi tantum invalescere in contemptu Christi et sue ecclesie quod foret sibi ex tali supposicione meritorius conversari seculariter, ut per gladium datum sibi a Deo coherceat potenter adversarios legis Christi, quam foret sibi istum statum deserere et vitam exproprietariam clerici vel heremite assumere. Vita tamen communis exproprietaria, nec in magna terrenorum affluencia nec in magna eorum carencia, videtur communiter illustratis securior, ut docet Solomon Prov. XXX°, 8, aliis autem illustratis eminencius est vita arcior vel in cura alcior, debite proficienti perfeccior; quod si propter ypocrisim vel primatum status talis appetitur, nullus est periculosior, quia Sapiencie VIª, 6, dicitur: Districtum iudicium hiis qui presunt fiet; a talibus enim archiservis Deus requiret striccius compotum talenti traditi et fructum ministerii, et patet de primatibus utriusque partis ecclesie, sicut inferius ostendetur de regibus. Unde videtur mihi quod rex Anglie annuatim vel per vices congruas faceret diligenter et perfecte inquiri

[ENGLISH]

## ¶6 · 384.1–384.33

> [p. 384] de bonis regni, qua condicione et quando sit in omnibus et singulis cleri sui ad manum mortuam devolutum. Secundo quod notetur numerus, qualitas et armatura spiritualis cleri qui occupat ista bona, et tercio quod faciat inquiri si in quantitate vel qualitate cleri in comparacione ad has elemosinas sit defectus, quem inventum faciat omnimode celeriter emendari. Probatur huius racionabilitas in exemplo: Nam supposito quod rex dedisset capitaneo cum suo exercitu thesaurum regni notabilem ad hostes corporaliter debellandum, nonne in monstracione exercitus sui ydonea faceret similia inquiri proporcionabiliter ad thesaurum pugnatoribus ministratum? Cum ergo pugna spiritualis milicie sit quoad causam clarior, quoad regem et regnum utilior et quoad exigenciam, iudicis preponderancior, quomodo non per locum a maiori faceret fidelis rex illud diligencius inquiri? Non restat fideli admittenti principia fidei medium excusandi. Illius enim est ydoneitatem militum suorum inquirere cuius est stipendium reddere. have Nec valet fingere exempcionem vel privilegium ad tollendum illud stante rata solucione stipendii; nec mirum si regnum nostrum habeat consuetudinem (cum hoc quod non sit legi scripture contraria), eciam aliam quam habent alia regna mundi, quia al modo et alio pondere stipendii conduxit rex clerum Anglie quam cleri in regnis aliis sunt conducti. Unde cum maximus contemptus quoad Deum et hominem et specialiter quoad periculum regni staret in fraude illius milicie, videtur quod rex et regnum debent de istis eo magis diligenter inquirere et proporcionaliter ad defectum in quantitate vel qualitate de stipendio deficienti subtrahere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 380.31: So may the Pope,
- 381.5: and should, if he thinks the Church will be the better for his action.
- 381.11: The Church left Christ's privilege for Caesar's; it has now the right to leave Caesar's.
- 381.27: We make so bad use of alms that patrons should withdraw them and restore them to the true Church.
- 382.8: Objection: 8. It is good to give temporal gilts for spiritual, and the more is given the more is received.
- 382.15: Answer: The rich man should use his wealth so as to obtain blessedness;
- 382.24: but this does not mean that he is to give up his duties to the clergy.
- 383.14: A King may see that it is his duty to reign rather than to enter into religion.
- 384.1: The King should enquire into Church property; how got and how used, and correct what is wrong.
- 384.21: The clergy have no exemption from such an enquiry.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 381: *verisimiliter* [R4]
  - 381: *foret* [R3]
  - 381: *Christus* [R3]
  - 381: *fuit* [R3]
  - 381: *perfeccior* [R3]
  - 381: *hereses* (English side-note "draw" glued) [R4]
  - 381: *quas* (30 is the line number) [R4]
  - 381: *Christi* [R3]
  - 382: *seculi* [R4]
  - 382: *mortalis* (clear li) [NW]
  - 382: *nesciencia* (italic) [NW]
  - 383: *cleri* (alinea T and 182a folio mark glued) [THIN]
  - 383: *Cesar* (clear C) [R4]
  - 383: *VIª* [R3]
  - 383: *iudicium* (italic) [R3]
  - 384: *mortuam devolutum* (print mor-/tuam devolutum.; main token mordevolutum covers both words, p.384 pos 17 is Secundo) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 380:
1. A in marg.: Nota. 6. 7. B: tcrrenorum non abicio. 25. A:
proporcionabiter.

p. 381:
5. B: quod alius. 27. A in marg.: Conclusio. Dc ablacione.

p. 382:
8. A in marg. : Octava racio. i5. A inmarg. : Responsio. Dotacio.

p. 383:
5. A in marg. : Conclusio. 10. B: vel minus utilem deest.
2S. Durissimum iudicium in lib. Sap. 3i. Codd.: ut post de
primatibus. 33. A n in marg. : Nota consilium

p. 384:
9. Ain marg.: Exemplum. M. A B in marg.: Prima liccio.
3 1 . A B in marg.: Sccunda liccio.
```

---

## Chunk 16-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-16-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-16-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "384.34–387.31"
divisions: "cap. 16 (heading 'CAP. XVI.' at 359.5); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "697 words; 609 unanimous or majority-real; 80 settled by vote (R2 50, R3a 22, R3b 3, R5a 4, R6a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n421–n424 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 16, part 8: [TITLE]

## ¶1 · 384.34–385.5

> [p. 384] Nec cadit excusacio quod nemo luet defectum alterius, quia oppositum est fides catholica, specialiter [p. 385] quando unus omissione vel commissione participat peccato alterius; si enim prepositus spiritualis exercitus vel capit stipendium pro militibus quos non habet vel pro indignis quos debet corrigere, quomodo non est dignum elemosinam proporcionalem ab illo subtrahere?

[ENGLISH]

## ¶2 · 385.7–386.14

> [p. 385] Nec valet infidelis ficcio qua dicitur quod absque condicione fuit facta collacio, quomodocunque religiosus voluerit donatum expendere, quia hoc accusaret patronos ex blasphemia et extingueret spem de suo spirituali suffragio; ideo non minus propter mortuorum suffragium quam vivorum subsidium debet fieri diligens inquisicio in hac parte; tunc enim haberemus pauciores milites, sed potenciores contra dyabolum. Y Nec valet infundabilis ficcio qua dicitur quod nemo aufert quicquam simpliciter ab alio nisi auferat quolibet sibi simili in natura, quia tunc nemo posset quicquam auferre ab alio, cum omne ablatum ab impio tribuitur iusto. Sic enim iusti tulerunt spolia impiorum et omni habenti dabitur, ab eo autem qui non habet et quod videtur habere auferetur; et sic de modis loquendi scripture, sanctorum doctorum et legis ecclesie. Nam XXXVIIª epistola Augustini ad Macedonium dicitur quod non dimittitur peccatum nisi restituatur ablatum, et idem ponitur in canone, XIVª, q. VI. Si res. Ista tria nesciverunt sompniare quod non est ablacio nisi iusta, nec quod est iusta ablacio nisi fuerit auctorizata a pontifice Romano. Nam omnem ablacionem vel collacionem sicut et omnem [p. 386] operacionem quoad eius substanciam oportet auctorizari a Deo; et cum omnis talis operacio non est sic secundum quid sed operacio simpliciter, eo quod aliter nulla creatura foret simpliciter activa, sicut Commentator recitat quosdam dicere, quos dicit non habere cerebrum dispositum ad philosophandum, sequitur cum veris quod stat esse ablacionem simpliciter cum hoc quod non a papa fuerit approbata. Si ergo ablacio vel alia talis iniusta operacio non dependet ex approbacione divina quoad mores quin sit simpliciter ablacio et alterius generis operacio, quomodo blasphematur quod nulla est ablacio simpliciter nisi papa decreverit? Sic enim extolleretur super omne quod dicitur Deus.

[ENGLISH]

## ¶3 · 386.15–386.33

> [p. 386] Nec minus blasphemum est dicere quod nulla est iusta ablacio, collacio vel alia operacio ecclesie nisi auctorizetur ab ipso, quia antequam ipse habuerit primatum huiusmodi erant multe operaciones ecclesie satis iuste, sicut operacio sua est iusta ex pura acceptacione divina. Ymmo pro tempore mortis sue, sicut et ipso superstite ignorante sunt multe ablaciones, collaciones et operaciones elemosinarie satis iuste, sicut patet de dotacione ecclesie Anglicane, que non emanavit ex eius auctoritate, sicut nec percepcio elemosine cesaree vel elemosina Anglie cesari non subiecte. Aliter enim non faceret Anglicus elemosinam clero suo nisi ostensa ad hoc auctoritate papali singularissima; quod non est fingendum, cum tempus et infinite alie circumstancie variarent operacionem elemosine. Et sic cum auctorizacio generalis non sufficit, frustraretur ex defectu auctoritatis papalis et ignorancia revocacionis licencie prioris omnis elemosina facienda egenis.

[ENGLISH]

## ¶4 · 386.34–387.31

> [p. 386] Ex istis demum colligitur quod ficticia subdola recentissima qua maior pars nostrorum sacerdotum [p. 387] dotatorum fingit infideliter quod, cum papa dominatur civiliter et capitaliter super singulos reges terre, non licet eis auferre quicquam a clero, iudicare de cleri conversacione vel cleri officio, nec ipsum corripere vel iuvare nisi ex eius auctoritate previe requisita. Sic enim extolleretur super Petrum et omnem Christi vicarium, cum Petro ignorante et non approbante nisi forte confuse, sicut benevolus approbat omne bonum, Paulus nuda auctoritate Christi fecit magnum profectum ecclesie (sicut patet Act. IX° et infra). Secundo fingens hoc dogma nephandum daret occasionem populo, laicali subtrahere beneficienciam suam egenis, tam clericis quam laicis, eo quod non expresse docetur satis singularis papalis auctoritas vel interim revocacio auctoritatis ostense, ut tangitur in destruccione proxime ficcionis. Tercio tolleretur omnis regalia et primatus secularis principum terrenorum, cum non liceret seculari iudicare de nequicia clerici sibi iniuriantis quantumcunque notorie nec exterrere clerum freneticum ab attemptato facinore, et multo magis non liceret seculari domino amerciare clericum vel eius familiam insolentem nisi prius consulto papa ad hoc licenciante, quia aliter liceret auferre a clero per viam multacionis temporalia sua mobilia et in foro civili iniuste. occupata, papa qui est capitalis dominus inconsulto. Talia deliramenta nedum ex scriptura sacra infundabilia sed sibi contraria que hodie plus solito sunt emuncta dabunt finem, si Deus voluerit, ne post istum virum sterilem succedat alius tyrannice sic blasphemans, sed Danielis IX°, 27, dicitur quod abhominacio desolacionis perseverabit usque in finem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 385.7: It is vain to plead that the gifts were made without conditions.
- 385.15: Vain too is the fiction that all true taking away is from like by like;
- 386.15: or that every gift or withdrawal of gifts needs the Pope's sanction.
- 387.11: If this were true the laity might withdraw all gifts that had not been sanctioned by the Pope, while the clergy would be out of all control.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 385: *quando* (alinea X and 182c folio mark glued) [THIN]
  - 385: *XXXVIIª* [R4]
  - 385: *XIVª* [R4]
  - 387: *occasionem populo* (print: daret occa-/sionem populo laicali; main token occaH and line 11 starts laicah, so sionem populo has no main token; whole word plus populo given here) [THIN]
  - 387: *laicali* [THIN]
  - 387: *auctoritatis* (15 is the line number) [NW]
  - 387: *proxime* (3 is a margin argument numeral) [R4]
  - 386: *∅* (duplicate: iusta already at 107) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 384:
9. Ain marg.: Exemplum. M. A B in marg.: Prima liccio.
3 1 . A B in marg.: Sccunda liccio.

p. 385:
7. A B in marg.: Tercia ficcio. 8. In codd.: quandocunque.
i5. A B: Quarta ficcio. A in marg.: Nota ficticias pro dominacione cleri
(Above i82c without mark of reference). 23. A m marg. : Augusrinus.
B in marg.: Nota Augustinum quod non dimittitur peccatum nisi resti-
tuatur etc. 29. A in marg. : Stat esse ablacionem iustam preter
hoc quod papa ipsam approbaret.
26. Vide Decr. II pars, causa XIV, q. VI, cap. I. De illa
epistola Augustini vide supra pag. 304.

p. 386:
i5. A H in marg. : Quinta ficcio. 17. B: ipse — operacio sua
deest. 34. A in marg. : Nota. A B in marg.: Sexta ficcio.

p. 387:
i5. A A,: ostense deest.
```

---

## Chunk 17-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-17-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-17-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "388.2–390.11"
divisions: "cap. 17 (heading 'CAP. XVII.' at 388.1); part 1 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "534 words; 472 unanimous or majority-real; 50 settled by vote (INS 1, R2 38, R3a 8, R3b 1, R5a 2); 12 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n425–n427 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 17, part 1: [TITLE]

## ¶1 · 388.2–388.6

> [p. 388] Pro ulteriori declaracione christiane fidei de quiditate ac unitate sancte matris ecclesie discurrendum est per illas decem raciunculas quas feci superius in fine Vⁱ capituli de ista materia, et recitabo responsiones cuiusdam doctoris, ut veritas fidei concertacione scolastica magis appareat.

[ENGLISH]

## ¶2 · 388.7–388.10

> [p. 388] Assumpsi autem in primo argumento quod, si ante incarnacionem Christi non fuit ecclesia et extra ecclesiam catholicam non est salus, tunc nullus patrum veteris testamenti salvabitur.

[ENGLISH]

## ¶3 · 388.11–390.11

> [p. 388] Hic negatur consequencia, cum antecedens sit verum et consequens falsum vel, inquit ante incarnacionem erat ecclesia catholica. Hic insto primo contra falsitatem impositam consequenti, et quia est argumentum ad hominem, suppono primo quod nihil est quod fuit ante hoc instans quod est presens, et erit post illud nisi quod est in illo eodem instanti. Patet supposicio scole dicenti quod nichil est nisi quod est in hoc instanti temporis quod est presens, et tunc arguo sic contra concessum, scilicet quod aliquis patrum veteris testamenti salvabitur. Si sic, tunc vel qui est aliquis patrum veteris testamenti salvabitur, vel qui erit aliquis patrum veteris testamenti salvabitur consequens falsum secundum istam scolam. quia nec est nec erit aliquis patrum veteris testamenti, cum non sit vetus testamentum nec reincipiet in die iudicii vel ante. Nec est verisimile quod vetus testamentum sit novum testamentum de quo scriptura facit distinccionem cum lege veteri, quia tunc non foret distinccio inter vetus testamentum et novum [p. 389] per descripciones eorum congruas exprimenda, sed omnia cerimonialia et legalia veteris testamenti essent pro tempore legis gracie ab ecclesia observanda, consequens contra sanctos doctores tractantes de cessacione legalium. Et quantum ad conclusionem ex fundacione Augustini, scilicet quod ecclesia fuit antequam fuit ecclesia, patet quod iste sanctus horruit sic sophisticari in fide de sancta ecclesia, nec sequitur ex textu suo, III, De Doctrina Christiana VI°, supradicta sentencia. Nam iste est textus Augustini: Qui crediderunt ex quibus facta est prima ecclesia Jerosolimitana, satis ostenderunt quanta utilitas fuerit eo modo sub pedagogo custodiri. Modo non sequitur, ex illis facta est prima ecclesia Jerosolimitana, ergo nec ante illos nec ante incarnacionem fuit ecclesia Jerosolimitana, et multo magis non sequitur quod ante illos non fuit ecclesia. Unde logice dicitur quod ex illis facta est particulariter ecclesia catholica que fuit a principio mundi et fuit continue per generacionem membrorum suorum usque ad finem mundi, et facta est in magno anno mundi. Sed pertinencius sensui huius sancti dicitur quod intendit ex illis factam primam Jerosolimitanam particularem ecclesiam sub nomine Jerosolimitane ecclesie, quamvis ante fuerit ecclesia tam pro tempore legis veteris quam nove. Iste autem sanctus fuit mirabiliter subtilis logicus, relinquens nobis ex verbis suis diversa puncta logicalia capienda. Unde utramque istarum responsionum approbo, cum inutile est scole dare responsionem que non valet. Et conformiter dicitur ad illud Augustini, I Retraccionum cap. XIII°, [p. 390] ubi sic loquitur: quod dixi, ea est nostris temporibus christiana religio quam cognoscere ac sequi securissima ac certissima salus est; secundum hoc nomen dictum est, non secundum ipsam rem cuius hoc nomen est. Nam res ipsa que nunc christiana religio nuncupatur, erat et aput antiquos nec defuit ab inicio generis humani, quousque ipse Christus veniret in carne. Unde vera religio que iam erat cepit appellari christiana. Et sequitur exposicio: Hec est nostris temporibus religio christiana, non quia prioribus temporibus non fuit, sed quia posterioribus hoc nomen accepit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 388.2: We must go through the ten arguments given in Chap. V. with our opponent's answer.
- 388.11: 1. Our opponent denies our right to conclude from his premisses that the O. T. fathers will not be saved.
- 388.20: Answer: On his own nominalist theories it must be so.
- 389.5: Augustine did not say that the Church existed before it was the Church;

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 388: *CAP. XVII.* [HEAD]
  - 388: *∅* (go is the English side-note (We must go)) [INS?]
  - 388: *doctoris* (clear ri) [NW]
  - 389: *per* (alinea A and 183a folio mark glued) [THIN]
  - 389: *∅* (inserted run is p.388 text; p.389 begins per descripciones) [INS?]
  - 389: *fuit* [R3]
  - 389: *fuit* [R3]
  - 389: *Jerosolimitanam* (capital J as printed) [R4]
  - 388: *∅* (duplicate: capituli already at 26) [DELX]
  - 388: *Vⁱ* (print: in fine Vⁱ capituli (agent 13)) [OVERRIDE]
  - 388: *∅* (scan split; capituli at 27) [OVERRIDE]
  - 388: *capituli* (print: capituli) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 388:
1. A in marg. cam XVII (in red ink). 4. V. cap. ; codd.: XV.
6. A A,: contncacione. 7. B: autem deest. 11. A in marg.:
Prima responsio. 18. A in marg. : Ante Christi incarnacionem fuit
ecclesia; hoc probatur continue (Below i82d without mark of reference).
iq. B : quod est prius.
7. Compare pag. 112, 1. 18.

p. 389:
5. 6. B: ex fundamento. 12. In codd.: inutilatas. Correxi e textu
Aug. I. c. 22. A A,: huiusmodi sancti. 3l. A: Augustini 11
in textu ; in marg. : correxit I. In codd.: cap. XII. correxi. B in marg. :
Christiana religio est securissima.
9. Aug. Opp. tom. III, pars I, pag. 48. 3i. Ibid. tom. I,
pag. 19.

p. 390:
II. A in marg.: Nota. 20. A in marg. : Ecclesia incepit habere
nomen ecclesie in novo testamento, sed utique ipsa prius fuit (Below
i83»without mark of reference). 26. B: vel fuit. 28. A A, :
quia — ecclesia deest. 32. A in marg. : Augustinus.
18. Decret. sec. pars, causa XXXII, q. IV, cap. II.
```
