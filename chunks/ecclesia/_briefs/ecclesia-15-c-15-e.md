# Translation brief: ecclesia 15-c–15-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-15-c.md chunks/ecclesia/wyc-ecclesia-15-d.md chunks/ecclesia/wyc-ecclesia-15-e.md` once and fix what it reports.
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

## Glossary (the 171 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
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
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
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
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "one given alms". Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |

---

## Chunk 15-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "336.17–340.16"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "904 words; 814 unanimous or majority-real; 72 settled by vote (INS 2, R2 36, R3a 32, R6a 2); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n373–n377 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 3: [TITLE]

## ¶1 · 336.17–338.11

> [p. 336] Ex istis secundo arguitur quod nedum potuit sed decuit eum sic dotasse ecclesiam, ut licite posset subtrahere elemosinas suas in casu quo earum abusus vergat ad detrimentum regni et subtraccionem evangelii; et scimus pro tempore antequam Britones et Saxones dotarunt ecclesiam vel enim fuit ecclesia nostra dotata, et interim tempore Saxonum ante adventum Augustini fuit fides Christi infideliter pretermissa, tunc isti principes primo dotantes ecclesiam nostram non erant moti nisi titulo misericordie donare plus vel minus nostre ecclesie ut nec cesar. Potuerunt ergo dedisse clero nostro quantum decreverint, adiciendo quamcunque condicionem honestam voluerint, sed potuerant cum donacione sua primeva adiecisse condicionem honestam quod elemosinarii non contempnant [p. 337] insurgentes in regem ad sui populi detrimentum. Omnia ista suppono ex cronicis et tamquam proxima per se notis. Non enim tenebantur reges sub pena excommunicacionis dotare suam ecclesiam dotacione perpetua plus vel minus, ut patet ex dictis; tunc enim tenerentur sub pena dampnacionis dedisse clero suum totale dominium, cuius oppositum suppono. Et ex istis sic arguitur: Si secundum istam formam dotassent nostram ecclesiam, licite potuissent pro contemptu regis suam elemosinam subtraxisse, sed cum ista condicione potuerunt dotasse nostram ecclesiam, ergo potuerunt pro contemptu cleri datam elemosinam licite subtraxisse. Cum ergo illa condicio fuisset licita et honesta, consuetudoque regis et regni docent in facto condicionem illam fuisse adiectam, videtur nimis presumptuosa assercio quod principes nostri non potuerunt ab eis auferre temporalia quantumcunque deliquerint; ymmo cum absolute necessario potuerunt talem condicionem adicere, et iterum absolute necessario elemosinarii possent tantum delinquere, patet (ut sepe dixi) quod principes nostri absolute necessario potuerunt suas elemosinas subtrahere, periculo possibili imminente. Et per idem sequitur quod potuerunt cum possibilibus paribus subtrahere in futurum, quod sonat directe contra terciam conclusionem doctoris que dicit quod reges Anglie temporalia a clero suo nunquam legitime abstulerunt, sicut nec datis paribus legitime potuerunt in futurum. Et notate verba si, inquam, nec datis paribus potuerunt auferre legitime, tunc nec datis aliquibus paribus potuerunt auferre legitime, et per consequens in quantumcunque magnam [p. 338] prodicionem regni nostri clerus possessionatus conspiraverit vel quantumcunque magna necessitas regno nostro contigerit, non liceret regi ad defensionem regni bona appropriata clero suo accipere; nec dubitat vel cecus logicus quin si liceret regi bona cleri in tali casu possibili qui tam sepe contigit, tunc poterit cum paribus sic auferre. Sed supponendo istam potenciam tamquam absolute necessariam, accedendoque ad licenciam et debitum, probo primo racionabilitatem condicionis superius recitate: Nam rex Anglie dotans ecclesiam suam nec debuit nec potuit ipsam dotare

[ENGLISH]

## ¶2 · 338.12–340.16

> [p. 338] ad enervacionem vel deterioracionem regni sui. Cum omnis potestas sit a Deo qui non potest dare potenciam ad hunc finem, sed sic contingeret supposito quod rex absolute dotasset suam ecclesiam non subintelligendo condicionem illam, ergo oportuit condicionem jllam subintelligi et per consequens, quando contemptus cleri accidit, rex capiendo temporalia in manus suas non facit clero illi iniuriam, cum condicio ex defectu cleri dissolvitur. no Minor autem argumenti sic ostenditur: Si omnia illa bona quibus dotatur nostra ecclesia immediate et directe pertinerent ad papam, sic quod rex non habeat interesse in possessionibus vel personis, cum plus quam quarta pars regni sit devoluta ad manum mortuam, sequitur quod rex noster non sit rex tocius Anglie, cum plus quam quarta pars in manu mortua est decisa. Stat enim aliquid esse in [p. 339] regno et non de illo, sed quomodo contingeret hoc planius quam quod omnia temporalia cleri Anglie non forent sub regis regimine sed pape, cum enim dicunt quod papa dominatur civiliter, nec est possibile quod due tam disparate persone dominentur ex equo simul civiliter super eodem, relinquitur eis dicere quod rex noster sit quoad omnia mortificata in regno nostro vel exclusus simpliciter vel pape subdominans. Sibi enim non licet (ut inquiunt) interponere de Clero vel possessionibus suis quantumcunque deliquerint, nec regi licet subtrahere temporalia eorum, quantumcunque abusus vergat ad regni periculum, quia (ut inquiunt) exempti sunt a iurisdiccione regis, tam in corpore quam in bonis, et inmediate subiecti pape vel suis ballivis, collectoribus vel ministris. In cuius signum papa habet post mortes multorum prelatorum et abbatum in Anglia primos fructus secundum nephandum abusum infundabiliter presumptum et a regibus culpabiliter toleratum. Unde (ut alias dixi) quicunque pertinaciter dogmatizaverint istam sentenciam nituntur proditorie subvertere regnum nostrum. Oportet ergo de integritate regalie regis nostri quod habet potestatem ad confiscandum suas elemosinas pro contemptu, quia, cum religiosi possessionati non sunt confirmati sed peccabiles sicut vulgus, patet, cum plus elongatur a rege punire eos tam in personis quam in temporalibus, si rex non posset punire eos in temporalibus, cessaret quoad eos omnis regalis cohercio, et tunc sicut angeli non sunt subiecti seculariter regi Anglie nec boni nec mali, sic nec illi. Nam persona vel populus existens in regno et non subiecta legibus regis et regni, non dicitur esse de illo regno, ut patet de comitivis depopulatricibus [p. 340] regnorura et de dominiis alienorum regum infra alia regna contentis. Sed ut meminerunt recencius iuris regis, optentum est privilegio laudabili regni nostri quod in mortibus multorum sacerdotum qui de rege tenent in feodo temporalia cedant regi. Unde ex iure patronatus confert beneficia interim vacancia, et licenciato capitulo ad novam eleccionem presentato sibi electo approbat vel reprobat sicut placet. Unde cum rex preter istas regalias aufert sepe temporalia a capitulis eciam jnvitis, vel oportet dicere quod omnia ista licet sibi facere vel si non potest tunc cum facto foret hereticus, et per consequens illi ex vecordi taciturnitate et redempcione temporalium que capitaliter tenerent, de tanto heretici forent heresis sue participes. Cur ergo ex fundamento scripture sacre vel iuris canonici hoc non docent?

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 336.25: These endowments were first made after the coming of Augustine.
- 337.4: and may have had conditions attached to them; such as forfeiture by contempt.
- 337.14: The customs of the realm show that such conditions were attached;
- 337.22: so our princes may on sufficient occasion withdraw alms.
- 338.11: Such a condition is reasonable,
- 338.14: for without it the King would damage his kingdom by giving endowments.
- 338.21: If he had no power over the possessions of the clergy he would not be King of all England,
- 339.1: since a fourth part of the realm would be under the Pope,
- 339.9: who is said to be the only ruler the clergy should acknowledge.
- 339.21: So the royal power would be maimed.
- 340.1: Customs proving the King's rights,
- 340.9: acquiesced in by the clergy.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 336: *et* (176a folio mark follows) [R3]
  - 337: *regis* [R3]
  - 337: *imminente* [R4]
  - 338: *bona* (5 after it is the line number) [R3]
  - 338: *sui* [R3]
  - 338: *∅* (of is the English side-note (possessions of); print: illa bona) [INS?]
  - 338: *cum* [R3]
  - 339: *Anglie* [R4]
  - 339: *forent* [R3]
  - 339: *Oportet* [R4]
  - 339: *cohercio* [NW]
  - 339: *regno* (176b folio mark glued) [THIN]
  - 338: *∅* (fragment of subintelligi; JOIN 116 subi + 117 n + 118 te + 119 lli + 120 gi -> subintelligi) [DELX]
  - 338: *subintelligi* (print: subintelligi (agent 13); scan cut it in five) [OVERRIDE]
  - 338: *∅* (joined at 116) [OVERRIDE]
  - 338: *∅* (joined at 116) [OVERRIDE]
  - 338: *∅* (joined at 116) [OVERRIDE]
  - 338: *∅* (joined at 116) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 336:
1. A in marg. : Ficcio. 17. A in marg. : Secunda racio. 21. In
codd : simus. 29. A: adiciendo quantumcunque ; volucrint —
honestam deest.
17. Comp. Hus, De ablacione bonorum temporalium I. c. fol.
cxxir.

p. 337:
8. A in marg.: Dotanda cst ecclesia sub condicionc (Abovc iy6n without
mark of referencc). 23. B: quod cum potuerunt. 2S. A in
marg.: Conclusio falsa. 20. A A,: paribus potuerunt. Codd.: in
qnantum. 3i. A A,: quantamcunque.
12. Comp. Hus I. c. fol. CXXIII".

p. 338:
10. A in marg.: Racio. 21. A in marg. : Dc ablacione (Above
176* without mark of reference). 28. B: Est vel decisa.
10. Hus: Item rex Boem i e dotans ecclesiam suam nec debuit . . .
27. Hus 1. c: sequitur quod rex noster non sit rex tocius Roemie,
cum plus quam quarta pars pro clericis in manu mortua est
decisa . . . Comp. Loserth, Hus und Wiclif, Zur Genesis der
husitischen Lehre, p. 199—208. (Wiclif and Hus, transl. by
Evans pag. 225—235.)

p. 339:
5. B: dcsparate. 19. A in marg.: Conclusio. 29. B:
sicut Angli.
33. Comitivis. Cf. Wulsingham I, 3o2.

p. 340:
7. B: licento. 14. B: de tanto heretico. 19. A in marg. :
Tercia racio. 21. B : omniquam. 26. A: XXII. cap., corrcxit XIII.
A, : XXII. 32. A in marg. : Ficcio.
```

---

## Chunk 15-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "340.17–342.12"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "451 words; 399 unanimous or majority-real; 45 settled by vote (INS 1, R2 25, R3a 19); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n377–n379 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 4: [TITLE]

## ¶1 · 340.17–342.12

> [p. 340] Tercio principaliter arguitur de lege Dei atque ecclesie quod rex debet in casu subtrahere suas elemosinas a nominetenus clericis et restituere eas sancte matri ecclesie. Nam hoc foret complementum iusticie, prodessens altrinsecus omniquaque; cum ergo ad regem maxime pertinet facere iusticiam in rebus subiectis suo dominio, sequitur quod ad regem pertinentissime spectat complementum talis justicie. Antecedens patet ex hoc quod omnis sic pertinaciter abutens bonis ecclesie est hereticus (ut patet in fine XIIIⁱ cap.). Sed cum omnis hereticus iniuste occupans bona regni nostri est spoliandus, et bona restituenda veris dominis, videtur quod bona illa quibus rex tam principaliter dominatur, sunt per regem confiscanda et veris dominis restituenda, specialiter in tam pertinaci desidia spiritualis prepositi. Nec valet dicere quod ad regem non pertinet cognoscere super heretica pravitate; quia [p. 341] ad regem pertinet cognoscere quod elemosinarius suus vivat clericaliter, tum quia sub illa condicione sunt elemosine sibi date, tum eciam quia degenerando ab ista vita foret monstrum maxime proditorie faciens ad destruccionem regni, et per consequens incurrens contemptum regis gravissimum. Ideo idem foret cecare regem et regnum per istum fucum sophisticum et dicere illis quod non pertinet eis cognoscere quid foret saluti anime eorum et gubernacioni regni necessarium. Et revera quicunque hoc imposuerit regi nostro, imponit sibi implicite quod non sit habilis ad regnandum. Rex ergo tenetur scire per se vel suum executivum consilium quid vergeret ad sui ac regni maius periculum, quod indubie foret omissio corrigendi quia secundum beatum Gregorium et leges quotlibet: Qui emendare potest et negligit absque dubio participem delicti se ipsum constituit. Consideret ergo de cleri crimine rex vel suum consilium secundum racionem qua est ipsius regni cuius rex accepit gubernacula destructivum, sicut docet beatus Gregorius in Registro lib. XI°, cap. XXIX° (ut superius allegavi). Confirmatur tripliciter, primo per hoc quod iuxta decretum beati Gregorii positum XIª, q. IIIª, ,Privilegium Privilegium omnino debet amittere qui sibi permissa abutitur potestate. Sed omnis clericus abutens elemosinis regis sibi permissa abutitur potestate, cum ergo illa dotacio sit privilegium, sequitur quod illud omnino debet amittere. Sed per quem nisi per regem privilegiantem? Illius enim est privilegium interpretari et defendere cuius est condere. Confirmatur ex illo Matthei, XIII° 12: Omni habenti dabitur et habundabit, [p. 342] ab eo autem qui non habet et quod videtur habere auferetur ab eo. Cum ergo rex tenetur sic habundare ex titulo iusticie, videtur quod ab eo debet causari ablacio sui elemosinarii, supposito quod contingat eum videri habere elemosinas quas non habet; et propter talem abusum habitualem dixi dominos temporales posse auferre bona sua a clericis micius quam loquitur beatus Gregorius cum canone, quia ipsi dicunt confuse quod privilegium omnino debet amittere propter abusum. Ego autem specifico abusum pertinacem qui inducit pravitatem hereticam, et tunc nulli dubium debet elemosinator subtrahere patrimonium Crucifixi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 340.17: Again, we assert that the King's duty is to take from false clergymen and restore to the Church.
- 341.1: It is objected that heresy does not come within the King's cognisance;
- 341.12: but the King is bound to guard against all dangers to the kingdom.
- 341.23: Confirmation: 1. The decretals say that abuse of a privilege forfeits it.
- 342.4: This forfeiture; must be enforced by the King.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 341: *ad* (176c is the folio mark, I the alinea letter) [R3]
  - 341: *foret* [R3]
  - 341: *lib* (print: Registro lib. XI°) [NW]
  - 342: *elemosinarii* [R3]
  - 342: *videri* [R3]
  - 342: *propter* (5 after it is the line number) [R3]
  - 341: *XIª, q. IIIª,* (output XI^, covers XIª, q. IIIª, (pos 170 absent); box on q. IIIª,) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 340:
7. B: licento. 14. B: de tanto heretico. 19. A in marg. :
Tercia racio. 21. B : omniquam. 26. A: XXII. cap., corrcxit XIII.
A, : XXII. 32. A in marg. : Ficcio.

p. 341:
5. Ii: dctraccionem. 10. B: hoc imponit. lS. B inmarg. :
Nota quoniodo rex sccundum Grcgorium habet interessc ad defectus clcri-
corum corrigcndos. A in marg.: Gregorius. 22. A in mari;.: Rez
peccat, si non corrigit clericum elemosinis abutcntem (Below 170 witliout
mark of rcfcrence). 28. A in marg. : Triplex conlirmacio.
22. et 25. Hus I. c. fol. CXXIII'.

p. 342:
6. B: clerum abusum. i3. A in marg.: Nota. 19. A in
marg.: Nota. 2S. 29. B: aJitcr enim. 32. A: suis suis.
```

---

## Chunk 15-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-15-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-15-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "342.13–348.23"
divisions: "cap. 15 (heading 'CAP. XV.' at 328.26); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1445 words; 1286 unanimous or majority-real; 137 settled by vote (R2 79, R3a 49, R3b 1, R5a 5, R6a 3); 22 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n379–n385 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 15, part 5: [TITLE]

## ¶1 · 342.13–348.23

> [p. 342] Secundo confirmatur ex hoc quod rex (in quantum huiusmodi) habet privilegium concessum a Deo et acceptum a populo ad regnandum; si ergo abutitur sua potestate in desidia correccionis, que maxime spectaret ad regis officium, quis dubitat quin secundum legem premissam rex teneretur amittere regnum suum? Unde inter alia peccata regum videtur quod omissio correccionis et auctorizacio curati inhabilis sit peccatum periculosissimum a regibus absconditum, cum ut sic sunt reges socii defensorum. Et ad illud potest adduci illud dictum Christi Matthei XXI°, 43: Auferetur a vobis regnum et dabitur genti facienti fructus eius. Non enim posset esse maior contemptus domini quam de suo patrimonio contra ipsum defendere hostem suum. Et ad hoc sunt multe concordancie legum (ut dixi in materia De Symonia); taliter enim meretur tam rex quam symoniacus ut ab eis tamquam ab hereticis dominus auferatur, ut loquitur propheta Osee V°, 6, sacerdotibus et regibus: In armentis suis vadent ad querendum dominum et non invenient: ablatus est ab eis. Talis ergo thesauri ablacio depauperaret regnum ad sui maximum detrimentum. [p. 343] Unde solebam dicere quod ablacio quedam est utrimque bona, ut Marci II°, 20, dicit Christus quod auferetur a discipulis suis sponsus, quandoque tantum alterutrum bona (ut Osee V°), quandoque vero utrimque mala, ut quando criminosi spoliant sese reciproce, semper autem est ablacio passiva bona ablatario permanente in caritativa paciencia. Tercio confirmatur ex lege debiti elemosine spiritualis. Nam rex tenetur tam ex iure Dei quam lure regni servare quantum sufficit legiis suis iusticiam et debitum opus spiritualis misericordie (ut patet superius tractatu De Privilegiis), sed precipuum opus talis misericordie regi pertinens foret castigacio coactiva ad continuandum suas elemosinas; ergo illud debet impendere. Unde qui offenduntur maxime ad verbum de ablacione temporalium vendicant quod seculares defendant elemosinas suorum progenitorum in suo robore permanentes, quod non fit (iuxta dicta XIII° cap.) nisi dum ecclesia habet profectum ex modo elemosinandi, sic quod collata remaneant in racione privilegii vel elemosine, quod extinguitur dum elemosinarii collatis elemosinis abutuntur; quamvis enim remaneat pie donantis voluntas, cum donum corporale perdit racionem elemosine per abusum, et fuisset meritum donatoris extensius, supposito quod sui elemosinarii proficerent magis ecclesie, quia in ipsis elemosinantes magis proficerent. Sic enim secundum beatum Bernardum peccatum Petri Abellardi est adhuc incertum, antequam noscatur quod homines ex sua heresi seducentur. Unde solet dici communiter quod elemosina habet perfeccionem essencialem que attenditur penes fervorem [p. 344] caritatis, secundum quam elemosinans miseretur, et perfeccionem accidentalem que capitur penes quantitatem fructus ex illa occasionata posterius. Ego autem credo quod aliud est genus elemosinandi in predestinatis et aliud in prescitis. Nam tota elemosina quam facit predestinatus limitat sibi gradum beatitudinis ad quem parcialiter proficiunt singule partes eius. Elemosina autem totalis presciti concurrit secundum se totam ad mitigandum penam perpetuam. Si domini temporales (ut elemosinati vendicant) tenentur continuare elemosinas patrum quorum sunt heredes, tunc tenentur ad omne inde sequens formaliter, quia aliter contra possibilitatem obligacionis divine forent ad contradictoria obligati, scilicet ad faciendum ipsas esse elemosinas et ad defendendum earum abusum in discolis, secundum quam racionem carent forma elemosine. Ergo cum reges Anglie tenentur servare elemosinas suorum progenitorum in sua perpetuitate, tenentur insuper ex lege spiritualis elemosine suos legios castigare, tenentur tercio ex obligacione qua tenentur facere legiis suis iusticiam et extinguere iniurias que vergunt periculosissime ad sui populi detrimentum; patet quod tenentur in casu bona sua ecclesie sancte restituere et a comtemptoribus Dei sui et regni auferre. Hoc enim fuit pactum dotacionis primeve. Ideo audenter assero, si cum istis paribus rex noster non habet potestatem ad faciendum in clero suo opus misericorditer castigandi, non habet sufficienciam super totali regno nostro politice dominandi, ymmo si bene attendimus ad scripturam sacram et dicta de privilegiis ecclesie, et sonat in privilegium regis quod habeat potenciam taliter clericos cohercendi, et clerici habent [p. 345] privilegium eo quod habent talem prepositum cui sic meritorie possunt subdi. Illi ergo qui dicunt quod rex habet potestatem incomprehensibilem castigando leones et faciendo corporales sanaciones cum aliis que vocant miracula, laxarent porcionem sue potencie ad regulandum regnum suum in clero, cum hoc et eius actus foret excellencius et plus fundabile ex scriptura. Nonne foret excellencius castigare freneticos, peccatores et discolos scole Christi quam domare feras que non tantum nocent ecclesie? Nonne iterum foret opus maioris virtutis gignere virtutes in mente disciplinabili occasione castigacionis salubris, qua ablata ab ecclesia virtutes ab indomito subtrahuntur, quam inducere virtualiter corpoream sanitatem? Utrobique namque est rex nudum instrumentum Dei qui dans regi virtutem subautenticam principaliter operatur. Et sic (ut sepe dixi) rex nedum faceret opus maioris virtutis in castigando subditos quam faciendo quoscunque actus mirabiles corporales, sed eciam quam accumulando quotlibet temporalia cleri Christi, nam tales virtutes faciendi sanitates corporeas possunt inesse bestiis, terre nascentibus atque lapidibus sed non virtus correccionis salubris. Et iterum adieccio temporalium communiter non est ita propinqua ultime necessitati salvacionis presentis corporee, sicut subtraccio abusi est propinqua ultime necessitati salvacionis perpetue tam corporis quam anime. Sicut enim est opus maioris misericordie auferre gladium a frenetico volente se ipsum occidere quam dare gladium persecuto ad defendendum se a volente eum occidere, quia peius foret hominem occidi sic a se ipso quam occidi ab alio, quia primum est dampnabile et secundum semper meritorium sive [p. 346] iustum; et ad hoc sunt multe leges ecclesie, ut allegavi superius XI° cap. huius ex dictis Augustini positis XXIIIª, q. IVª, Nimium, et Ipsa pietas, et Quid faciet; et illud patet Vᵗᵃ, q. Vᵗᵃ, ubi sub auctoritate Augustini scribitur: Non vos iudicetis malivolos esse, quando crimen alterius indicatis; magis quippe nocentes non indicando crimen estis, quam si fratres vestros quos indicando corrigere potestis tacendo crimen perire permittitis. Si enim frater tuus habet vulnus in corpore quod velit occultari, dum timet secari, nonne crudeliter a te siletur et misericorditer indicatur? Quanto ergo pocius debes manifestare ne deterius putrescat in corde? Et sequitur: Non omnis qui parcit amicus est, nec omnis qui verberat inimicus; meliora enim sunt vulnera amici quam fraudulenta oscula inimici; melius est cum severitate diligere quam cum lenitate decipere. Et sequitur ad propositum: Utilius esurienti panis tollitur, si de cibo securus negligat iusticiam, quam esurienti panis frangitur, ut iniusticie seductus acquiescat. Et qui freneticum ligat et qui litargicum excitat ambobus molestus ambos amat. Quis non potest amplius amare quam Deus, et tamen nos non solum docere suaviter, verum eciam salubriter terrere non cessat, ut docet Apostolus Hebreorum XII°. Fomentis lenibus quibus Deus omnes consolatur, sepe eciam mordacissimum medicamentum tribulaminis adiungit, exercet fame patriarchas, pios et religiosos, populum autem contumacem penis gravioribus agitat, non aufert ab apostolo stimulum carnis, tercio rogatus ut virtutem in infirmitate perficiat. Ex quotquot [p. 347] dictis sanctorum exponencium fidem scripture patet quod de lege caritatis et spiritualis elemosine sub pena dampnabilis consensus tenetur prepositus subiectos corripere. Unde inter omnia peccata de quibus magis timeo in superioribus regni nostri, sunt ceca pietas, falsa misericordia et consentanea omissio, sive ex negligencia sive (quod maxime horrendum est), quando venditur consensus criminis et iniuste ac proditorie per patrimonium Christi defenditur eius hostis. Unde Augustinus epistola XXXVII ad Macedonium: Misericordius opem nostram talibus subtrahimus quam impendimus. Non enim opem fert qui ad peccandum iuvat ac non pocius subvertit et opprimit. Sed contra dicta primo obicitur per hoc quod nemo debet defamare proximum et specialiter christos Dei. Illi autem qui illud obiciunt parum considerant quomodo mendax (in quantum huiusmodi) defamat se ipsum, et iterum quomodo ex verbis istis generalibus legis domini se putans defamatum indicat ut sic se esse legis Dei adversarium, et iterum parum considerat quomodo prophete veteris testamenti, Christus et leges ecclesie acutissime instant contra solum nomine sacerdotes; et racio est, quia in eorum subversione imminet maius periculum matri ecclesie. Et illud meminit decretum, LXXXIIIª dist., ubi sic scribitur: Nemo quippe in ecclesia amplius nocet quam qui perverse agens nomen vel ordinem sanctitatis vel sacerdotis habet. Delinquentem namque hunc redarguere nullus presumit, et in exemplum culpa [p. 348] vehementer extenditur, quando peccator pro reverencia ordinis honoratur. Episcopus itaque qui talium crimina non corrigit magis dicendus est canis impudicus quam episcopus. Ista, inquam, iura sanctorum ideo incorporata sunt in canone, non ut palea perpetuo taceantur, sed ut ad laudem bonorum cum modestia detegantur. Et dico cum modestia, quia contingit hominem in dicendo veritatem modum excedere, ut notatur in decretis Vª, q. Vª, Qui ambulat, ubi solvendo apparenciam repugnancie in ista materia sic scribitur: Aliud est ex caritate aliorum crimina deferre, ut quos secreta ammonicione corrigere non possumus, convictos iudicis sentencia corripiat, atque aliud est insidiando falsa obicere vel insultando vera facile exprobare. Illud vero caritatis, hoc autem est impietatis officium. Unde Proverb. XII, 6, dicitur: Verba impiorum insidiantur sanguini, os iustorum liberat eos. Et infra: Qui quod novit loquitur iudex iusticie est, qui autem mentitur testis est fraudulentus. Oportet ergo accusatorem servare integritatem veritatis et rectitudinem intencionis. Ego autem preservo me a descensu ad singularia quiescens more philosophorum in communi sentencia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 342.13: 2. By the same decretal the King loses his privilege of rule if he is slothful in correction.
- 343.8: 3. The King is bound to see that his subjects are not deprived of spiritual aid.
- 344.1: Double merit of alms; a) essential, from the charity of the giver; b) accidental, from the fruit of the gift.
- 345.3: Just rule is a more excellent privilege than so called miraculous powers.
- 345.24: The gift of alms is a less good than the suppression of abuses;
- 346.4: and so Augustine teaches.
- 347.15: Objection: 1. We have no right to speak ill of our neighbour.
- 347.21: Answer: We deal in general terms which apply only to those who deserve them.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 342: *regnandum* [R4]
  - 342: *43* (print: Matthei XXI°, 43: Auferetur; voted Auferetur twice at 172-173) [R3]
  - 342: *detrimentum* (print detri- / mentum; main token holds the whole word) [R4]
  - 343: *est* (1 is the margin argument numeral) [R3]
  - 343: *II°* [R3]
  - 343: *lege* [R4]
  - 343: *legiis* [NW]
  - 344: *capitur* (p clear) [R3]
  - 344: *legiis* [NW]
  - 345: *Illi* (M is the alinea letter) [R3]
  - 346: *XXIIIª* [R4]
  - 346: *IVª* [R4]
  - 346: *Vᵗᵃ* [R4]
  - 346: *Vᵗᵃ* [R4]
  - 347: *dictis* (177b folio mark and N alinea letter are not text) [R3]
  - 347: *legis* [R3]
  - 347: *LXXXIIIª* [R4]
  - 348: *Vª* [R4]
  - 348: *Vª* [R4]
  - 344: *posterius* (clear ri in print) [NW]
  - 346: *et* [R5]
  - 346: *perficiat* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 342:
6. B: clerum abusum. i3. A in marg.: Nota. 19. A in
marg.: Nota. 2S. 29. B: aJitcr enim. 32. A: suis suis.

p. 343:
4. A A(: quando decst. i5. Hus: Unde clerici qui. 18. A in
textu: XXII. cap.; corrcxit in marg. 23. Voluntas dcest in A et
B; A, add. in marg. 23. B: tum donum. 2S. B: est adhuc
meritum, antequam. 3o. A B in marg. : Nota de duplici perfcccionc
Q. Hus 1. c.

p. 344:
8. B: concurribilis. 12. Hus: sequens formari. 14. li: scilicct
deest. 29. politicc. In codd: polelice.

p. 345:
23. B: sed nec virtus. 25. li: prescntis — salvacionis dccsl.
3o. A in marg. : Nota. li in marg. : Nota non intelligo.
3. Hus 1. c. 24. IIus 1. c. fol. CXXXIll\

p. 346:
2. B: supcrius XX cap. 6. In dccrct.: malivolos, quoniam crimcn.
16. 17. B: cum sccuritate diligere. 24. A in marg. : De correccione pcr
ablacionem nota benc (Above i77b without marl; of rcfercnce). 27. In
dccret. : tribulacionis. 3i. Codd: in firmitatc; corrcxi c dccrct.
4. Decreti sec. pars, causa V, q. V, c. I et II.

p. 347:
6. A in marg. : Nota. 10. A in marg. : Augustinus. 12. In
codd. : Num cnim. Correxi e tcxtu Aug. 17. A in marg. : Obicccio.
18. A in marg.: Responsio. 20. 15: sc reputans. 20. A in
marg.: S3 dist. 26. B: ut sic scribitur.
4. — 11. Hus 1. c. 10. Aug. Opp. tom. II, pag. 532.
26. Dec. I pars, dist. LXXXIII, c. II.

p. 348:
i. in decret: quoniam peccator. 2. B: Episcopus in quantum. A in
marg. : Nota decrctum quantum nocet malus episcopus, papa ctc. (Bclow
I77b without mark ot' refercnce). 4. A B: Ista itaque iura. B in
marg. : Episcopus omittens subditos corrigere dicendus est canis impu-
dicus. 9. A in marg. : Accusator quomodo dcbet se habcrc.
22. singularia. A, addit: nomina.
9. Dec. II pars, causa V, q. V, c. V.
```
