# Translation brief: ecclesia 12-e–13-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-12-e.md chunks/ecclesia/wyc-ecclesia-12-f.md chunks/ecclesia/wyc-ecclesia-13-a.md` once and fix what it reports.
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

## Glossary (the 162 rows these chunks use; the full file is GLOSSARY.md)

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
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
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
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |

---

## Chunk 12-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-12-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-12-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "268.1–272.21"
divisions: "cap. 12 (heading 'CAP. XII.' at 250.17); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1082 words; 972 unanimous or majority-real; 85 settled by vote (DEL 1, INS 1, R2 46, R3a 29, R3b 1, R5a 7); 25 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n305–n309 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 12, part 5: [TITLE]

## ¶1 · 268.1–268.19

> [p. 268] Mala autem consuetudo propter maioritatem periculi est pocius extirpanda, dicente decreto d. VIIIª: Mala consuetudo non minus quam perniciosa corruptela est abicienda; que nisi cicius radicitus evellatur in privilegiorum ius ab impiis assumitur, et incipiunt prevaricaciones et varie presumpciones, celeberrime non compresse, pro legibus venerari et privilegiorum more perpetuo celebrari. Et sentencia huius decreti verificata est nimium hiis diebus, unde ad interpretandum rectitudinem consuetudinis et privilegii subiungit decretum sub auctoritate Augustini: Veritate manifestata cedat consuetudo veritati. Nemo consuetudinem racioni et veritati preponat, quia consuetudinem racio et veritas semper excludunt. Cum ergo racio naturalis et veritas scripture patenter convincunt quod dictum privilegium non debet intelligi nude ad literam, sed racione et veritate limitante condicionem sepe expositam, aptari debet singulare pertinens secundum distribucionem accomodam.

[ENGLISH]

## ¶2 · 268.20–269.11

> [p. 268] Per hec patet quod forma argumenti quod primo innuitur non procedit, tum quia multi sancti potuerunt consuetudinem predictam improvide approbasse et post penituisse, vel potuit fuisse tunc consuetudo laudabilis propter usum modestum, sed modo versum fuisse in corruptelam fidei contrariam propter malam consuetudinem superadditam gracia cupidinis usurpatam. Unde si racio ista procederet, nunquam impugnaret catholicus malum usum, sed ex consuetudine peccandi prescriberet membrum diaboli contra Deum, cuius oppositum docuit Christus consuetudines phariseicas acutissime reprobando, mundana vero prosperitas tam in personis quam in regnis est sepe kalende preparatorie ad ruinam. [p. 269] Quantum ad violacionem sancte matris ecclesie, dictum est quod ipsa non violatur nisi per defectum observancie legis sponsi; unde non est maior ydolatria credere truncum putridum esse dominum Jesum Christum quam credere domum:,: materialem sive basilicam esse sanctam matrem ecclesiam, sponsam Christi. Unde quia in festis dedicacionis basilice per episcopum laudat ecclesia Deum in hoc quod ecclesiam suam sponsam vocare dignatus est, instruendi sunt simplices sacerdotes ne credant infideliter quod illa basilica sit ecclesia sponsa Christi.

[ENGLISH]

## ¶3 · 269.12–270.15

> [p. 269] Ulterius quantum ad remissionem debiti satisfaccionis, dicitur quod nec temporalis dominus nec Deus ipse potest ipsum omnino remittere, tunc enim Christus frustra fuisset mortuus ad satisfaciendum pro peccato humani generis. Necesse est ergo quod pro quocunque crimine satisfiat in virtute meriti Jesu Christi, vel quod illud crimen eternaliter puniatur. Deus autem non potest concedere licenciam alicui ut eternaliter duret in crimine, et per consequens non potest concedere criminoso licenciam ut non satisfaciat pro delicto. Verumptamen homo potest cum circumspeccione sagaci remittere fratri iniuriam et debitum corporale et Deus remittet culpam postquam misericorditer invenerit peccatorem satisfacere pro debito. Nemo enim posset satisfacere pro minima offensa in tantum dominum, nisi ipse misericorditer levem penitenciam, baptismum vel aliquod opus penale acceptaverit graciose: iusticia, inquam, sua requirit quod solum premiet promerentem. Et patet quantum periculum est occasionare debitoribus fugitivis audaciam, ut non satisfaciant Deo vel homini, cum secundum principia Augustini et iuris [p. 270] canonici non dimittitur peccatum nisi restituatur ablatum, non quod oportet spoliantem restituere idem in numero fratri suo, sed quod satisfaciat omnimode domino capitali. Ipse autem vult ex inflexibilitate sue iusticie quod debitor satisfaciat servo suo debitum corporale, aut sibi equivalens restituendo, vel in pena inferni perpetuo serviendo. Illud autem servicium non est meritorium, sicut meritum quo impotens satisfacit creditori in via, sed est demeritorium prodessens creditori beato, et crucians perpetuo creditorem dampnatum; ideo non satisfaccio sed satispassio nominatur. Ulterius non oportet theologum omnes leges hominum de servitute et manucapcione discutere, sed satis est dicere quod precise de tanto sunt racionabiles de quanto consonant cum sacra scriptura.

[ENGLISH]

## ¶4 · 270.16–272.5

> [p. 270] Quinto et ultimo accusamur a vulgo per sompnia; fingunt enim filii patris mendacii quomodo revelatum est regnum Anglie transire impune, quousque sub quodam rege Ricardo basilica Westmonasterii sit polluta. Alias autem variaciones quas false fabricant non oportet hic recitare, cum mendacium dissonat sibi ipsi. Unde quicquid infortunii regno nostro acciderit applicant ad vindictam Dei de illo homicidio in sanctuario perpetrato, sed nesciunt applicare sequelam nisi per mendacia sompniorum. have Hic non contendo si fuerit tale sompnium, quia scimus ex fide scripture quod pater mendacn agitat fantasias fidelium in sompnis, ut eos subvertat vel impediat profectum ecclesie. Nam Matthei XXVII°, 69, legitur uxorem Pilati fuisse illusam a sathana ad impediendum profectum ecclesie ex merito mortis Christi. Nichil, inquit, tibi et iusto illi: multa enim passa sum hodie per visum propter eum. Ulterius [p. 271] videtur multis verisimile quod regnum nostrum pacietur in brevi; sed cum non sum propheta cui facta est illa visio, non presumo illud sompnium revelare. Credo autem quod in occisione istorum hominum commissa erant horrenda facinora, sed comparacionem gravedinis ipsorum ad aha dilncile est taxare, cum verisimile est quod alie polluciones per occisiones et verberaciones sacerdotum ibi et alibi in Anglia induxerunt in regnum crimina graviora. Ideo vellem quod omnia illa crimina sint correcta, quia certus sum ex fide scripture quod purgato regno a crimine et reconciliato Deo suo non est compossibilis tribulacio ab extrinseco vel intrinseco nisi sibi cesserit ad profectum, quia in oracione ecclesie sic habetur: Nulla ei nocebit adversitas, si nulla dominetur iniquitas. Ulterius tamen plus credendum est vive voci spiritus sancti, quam verbis vel sompniis patris mendacii, cum quandoque inmiscet verum, ut magis fraudulenter decipiat. Videndum est ex verbis scripture pro quibus peccatis contingit regnorum destruccio, et patet ex dicto sapientis Ecclesiastici X° quod iniusticie quoad Deum et iniurie quoad proximum sunt causa precipua. Et cum ad regem pertinet in regno suo utrumque extinguere, patet quod omissio regis in corrigendo clerum suis elemosinis abutentem et in corrigendo secularem miliciam pacem ecclesie perturbantem, est in rege causa precipua. Sed ve speculatoribus qui illud dicerent regi suo; ipsi enim sicut sacerdotes Judee sunt causa precipua persecucionis nostre ecclesie, si contingat, cum in quorum profectu stat regni prosperitas, in eorum defectu stat regni adversitas. Sacerdotes autem Dei debent autonomatice esse induti iusticiam, ideo declinantes ad iniusticiam gravius inficiunt se et suos, [p. 272] nam per absenciam vite in membris mors eorum inducitur. Et de isto conqueritur Isaie LVI°, cap. X°: Speculatores eius ceci omnes. Quod si fuerit, credenda est consequencia Christi Matthei XV°, 14°: Cecus si ceco ducatum prestet, ambo in foveam cadunt.

[ENGLISH]

## ¶5 · 272.6–272.14

> [p. 272] Et quoad correccionem brachii secularis, patet quod perturbacio perturbacio qua iniuste perturbant forinsecus, evidencia topica prenosticat perturbacionem futuram illis per quos staret eorum correccio; Matthei VII°, 2, scribitur: Eadem mensura qua mensi fueritis, remecietur vobis. Et ista est causa quare Salomon ad pacificacionem regni sui ex mandato patris fecit Joab occidi ad cornu altaris, ut patet III°, Regum II° cap., quia Isaie XXXIII° 1, scribitur: Ve qui predaris nonne et ipse predaberis?

[ENGLISH]

## ¶6 · 272.15–272.21

> [p. 272] Non autem intendo quod milites regis occidi debeant, sed arguebam per locum a maiori: Si pro tempore veteris testamenti licuit militem ad cornu altaris occidere, multo magis licet maleficum pro pacificacione regni et mundacione ecclesie salvatum in vita et membris extrahere (ut patet in primo argumento capituli septimi).

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 268.1: Evil customs should be rooted out at once.
- 268.12: Truth is of more weight than custom,
- 268.21: and makes it an insufficient plea.
- 269.1: It is mere idolatry to suppose a building to be the Church, the spouse of Christ.
- 269.12: For every crime satisfaction must be made;
- 269.31: so it is wrong to encourage debtors not to make amends,
- 270.6: as the satisfaction may have to be made in hell.
- 270.16: 5. The last charge against us rests on an absurd dream,
- 270.26: which may have occurred and have been instigated by the devil.
- 271.3: A great crime was committed, but others worse have taken place there, and all ought to be punished.
- 272.10: Justice should be done, even at the horns of the altar.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 268: *periculi* (hyphenated peri-/culi; main token holds whole word; 166ᵉ M is folio mark + alinea) [R4]
  - 268: *∅* ('insufficient' is English side-note text (and makes it an insufficient plea)) [R4]
  - 268: *quam* [R4]
  - 269: *Nemo* [R3]
  - 269: *fugitivis* [R4]
  - 270: *non* [R3]
  - 270: *inferni* [R4]
  - 270: *fingunt* [R3]
  - 270: *filii* [NW]
  - 270: *fidelium* [R4]
  - 270: *sathana* (30 after ad is the line number) [NW]
  - 270: *Nichil* [R3]
  - 271: *videtur* (P alinea + 167ª folio mark in margin) [R3]
  - 271: *hominum* (5 is the line number) [R3]
  - 272: *Christi* [R3]
  - 272: *14°* [R3]
  - 272: *perturbacio* [R4]
  - 272: *III°* [R4]
  - 272: *1* (old-style arabic 1, x-height (Isaie XXXIII° 1)) [R3]
  - 272: *et* [R3]
  - 268: *VIIIª* [R4]
  - 269: *iuris* [THIN]
  - 270: *dimittitur* [THIN]
  - 272: *absenciam* [THIN]
  - 272: *∅* (second half of in-ducitur; neighbour 8 already inducitur.) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 268:
1. A in marg. : Mala consuetudo. B in marg. : De consuetudinibus
abiciendis nota bene. n. A in marg.: Augustinus. 12. i3. B:
consuetudinem — quia deest. 20. A in marg.: Ad primum. 23. AA,:
Tunc — versum fuisse deest.
2. Decreti I pars, Dist. VIII, c. III. 11. ib. c. IV.

p. 269:
/\. A in marg. : Conclusio. Ecclcsia materialis sive basilica non est
sponsa Christi. 10. A: nec crcdant. A, correxit. 25. A A,:
invenit. 31. A in marg. : Spoliator tcnetur restituere ctc.

p. 270:
4. A,: Ipse enim. n. B in marg. man. altera: Satispassio.
i3. A, corr. in marg. : mancipacione. 16. A in marg. : Quinta obicc-
cio. Contra. 26. A in marg. : Responsio. 33. B: propter

p. 271:
10. Ainmarg. : Conclusio. 12. Codd.: reconsiliato. 20. A
in marg.: (niusticie quoad Detim et inmric quoad proximuni sunt
causc dcstruccionis regni (Abovc 167* without mark of reference).
32. Codd.: autonomastice.

p. 272:
1. B: et membris. 6. A in marg. : Correccio perturbancium pacem.
i3. A in marg. : Isaie XXXIII. Racio. B in marg. man. alt. : Non occides.
22. A in marg. : Responsio quedam.
```

---

## Chunk 12-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-12-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-12-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "272.22–274.24"
divisions: "cap. 12 (heading 'CAP. XII.' at 250.17); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "489 words; 455 unanimous or majority-real; 24 settled by vote (R2 13, R3a 8, R3b 1, R5a 2); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n309–n311 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 12, part 6: [TITLE]

## ¶1 · 272.22–273.3

> [p. 272] Unde audivi quemdam doctorem negare consequenciam, eo quod dicta ecclesia fuit miraculose consecrata, sed nec templum nec altare in quo occisus est Joab fuit taliter consecratum. Illud autem duplex sompnium nichil movet. Dico autem duplex sompnium, quia non docetur quin illud templum Salomonis fuit per inhabitacionem sanctorum prophetarum, sapientis et sancti regis in suis floribus, cum alio devoto populo, locus a domino per talem populum consecratus; plus enim valet ad sanctificacionem loci populus sanctus inhabitans cuius spiritus perungitur oleo gracie a spiritu sancto, quam valet corporalis linicio parietum secundum cerimonias sacerdotum. Nam illa sanctificacio [p. 273] est plus fundabilis ex scriptura, ut patet II° Machabeorum V°, et Exodi XXXII° dicit propheta: Consecrastis manus vestras hodie.

[ENGLISH]

## ¶2 · 273.4–274.4

> [p. 273] Secundum sompnium est de quodam piscatore qui sompniavit se locutum fuisse cum beato Petro dicente se ipsum velle dictam basilicam manibus propriis consecrare. Unde vidit consequenter in nocte vehemens lumen in basilica illa splendescere cum assistencia aliorum signorum consecracionem illam testancium. Sed da utrumque sompnium, et videamus quid obest loco sancto extraccionem legitimam ac meritoriam, preceptam a rege ibi perficere specialiter tantum opus misericordie quod vergeret ad basilice purgamentum. Unde consuluissem dicto abbati et eius conventui quod equanimiter tollerassent illatam iniuriam sanctificando se ipsos et celebrando devocius pro rege et suis progenitoribus. In illa autem paciencia facilius superassent quam insurgendo frontose per excommunicacionem in privatam regis familiam. Sicut enim privilegium ecclesie quesitum est per pacienciam Christi et suorum membrorum, sic est conformiter defendendum. Unde Christus dedit privilegia facillima ad querendum pro quibus docuit non esse corporaliter contendendum, sed in eorum defensionem esse humiliter paciendum, ut docetur XXIIIª, q. I, in principio. Privilegia autem humana sunt condicionis opposite, cum in sua impetracione sunt sumptuosa, in sua defensione sunt laboriosa, et in sua retribucione sunt dampnosa, sicut est de superbia et suis singulis filiabus. Quis, inquam, contenderet circa privilegium nolendi possidere aurum vel argentum, et sic de aliis privilegiis Christi superius memoratis? Ipsa enim donantur per apercionem oris [p. 274] anime et continuantur per pacienciam persecucionis atque iniurie et demum augmentantur usque ad summum gradum libertatis in requie.

[ENGLISH]

## ¶3 · 274.5–274.24

> [p. 274] Stulticia ergo est fastidiando certa privilegia secularia ista contempnere. Etista doctrina docetur Baruch 1°, 1 ex consilio Jeremie et captivitatis sapiencia sub hiis verbis: Orate pro vita Nabugodonosor, regis Babilonis, et pro vita Baltazar, filii eius, ut sint dies eorum sicut dies celi super terram. Si ergo tempore veteris testamenti, quando nondum perfecte docta est scola paciencie per Christum, non excommunicaret populus Dei regem infidelem qui destruxit templum, civitatem et gentem, et insuper ecclesiam eorum spoliavit cunctis suis insigniis et ministros ecclesie captivavit, sed e contrario benedixit, quanto magis tempore paciencie legis evangelice non excommunicaret vicarius Christi patronum suum vel eius familiam propter eius legitimum factum ad regni ac ecclesie fulcimentum vel propter opus unius persone nepharium, preter voluntatem regis vel sui consilii perpetratum, specialiter cum Christus Luce IX° docuit non sic maledicere eciam infideli. Erubescerent, inquam, interim recipere corporales elemosinas et defensionem corporis et bonorum a peculiari patrono cui taliter maledicunt.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 272.22: Another story of a dream.
- 273.10: Let the dreams be true, still justice should be enforced in the abbey.
- 273.17: More devotion is the right way for the convent to defend its privileges.
- 274.17: They ought not to excommunicate the household of their patron.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 273: *II°* [R3]
  - 273: *manus* [R3]
  - 273: *qui* (R is the alinea letter) [R4]
  - 273: *perficere* [NW]
  - 273: *∅* (print has in-/surgendo; main already holds insurgendo whole at pos 118) [INS?]
  - 273: *Christus* [R3]
  - 273: *XXIIIª* [R3]
  - 274: *1* (old-style arabic 1, x-height (Baruch I°, 1); the 5 after it is the line number) [R3]
  - 274: *scola* (167ᶜ folio mark glued) [R4]
  - 273: *V°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 272:
1. B: et membris. 6. A in marg. : Correccio perturbancium pacem.
i3. A in marg. : Isaie XXXIII. Racio. B in marg. man. alt. : Non occides.
22. A in marg. : Responsio quedam.

p. 273:
2. In ccdd. Exod. XXII. 14. Ainmarg. : Consilium. B: consiluissem.
23. A in marg. : Defcnsio privilcgiorum ecclesie. 33. B: per apcioncm.
26. Decr. sec. pars, causa XXIII, q. I, cap. I. Nisi bella.

p. 274:
5. A A,: doctrina deest. 6. loc. corrupt. in codd. Fortassc legen-
dum: captivitatis paciencia. 25. cm XIII in marg. (in red ink); ib. :
cm xUlm (in black ink. 26. A in marg. : TJtrum elemosina humana
corporalis perpetua sit fundanda. 28. A in marg. : Conclusio.
3o. A A,: plus secatur.
```

---

## Chunk 13-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-13-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-13-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "274.26–278.32"
divisions: "cap. 13 (heading 'CAP. XIII.' at 274.25); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "987 words; 902 unanimous or majority-real; 75 settled by vote (R2 45, R3a 27, R3b 1, R5a 1, R6a 1); 10 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n311–n315 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 13, part 1: [TITLE]

## ¶1 · 274.26–276.17

> [p. 274] Ex istis incidit declarare sentenciam quam dixi superius scilicet quod humana elemosina temporalis foret elemosina humana perpetua tam clero quam elemosinanti cum paribus magis autentica, magis meritoria et altrinsecus plus secura. [p. 275] Et ne equivocetur in termino, supponatur quod humana elemosina perpetua sit elemosina corporalis, data ab homine simpliciter sub nomine elemosine perpetue, sicut in cartis regum Anglie sepe fit mencio. Elemosina enim humana temporalis est elemosina data ab homine sine tali titulo expressata, sicut dantur bona vocata mobilia communitatibus vel personis egentibus. Prima autem elemosina fit communiter de redditibus secularibus, de proventibus ecclesiarum vel de impensionibus annuis ad perpetuitatem secundum traditiones humanas signo sensibili obligatorio limitatis. Suppono secundo positivum cuiuscunque partis conclusionis proposite; nam contingit secularem existentem in gracia pie dare tales elemosinas perpetuas, ergo contingit eas esse elemosinas autenticas, meritorias et securas; nec contendet amicus vel adversarius circa probacionem huius, cum leges ecclesie approbant dotaciones, fundaciones et appropriaciones perpetuas factas clero. Non autem sic approbarent factum illud, nisi fuerit autenticum, meritorium et securum; ergo conclusio. Unde adversarii clamant quod iustissime, necessariissime et decentissime ecclesia taliter est dotata, in tantum quod non licuit dominis temporalibus sine excommunicacione et dampnacione perpetua taliter non dotasse. Istis suppositis probatur conclusio per hoc quod Christus expresse facto exemplavit et verbo docuit temporalem elemosinam, non autem dictam elemosinam perpetuam; ergo conclusio. Illud autem quod docetur expressius in scriptura, quod procedit signancius a persona magis autentica et in quo plus crescit ecclesia, habet tres condiciones superius recitatas. Nam negligencia vel fatuitas fuisset in Christo, si dedisset legem ad gubernandum suam ecclesiam, et regulam abiectam [p. 276] vel minus necessariam expressius declarasset, regulam autem plus necessariam occultasset; ideo antiqui doctores ceperunt ex fide scripture quod testamentum Ghristi datum est ecclesie, tam in materia quam in forma, secundum quod est necessarium et expedicius, ut dirigat viantes per artam viam ducentem ad patriam, et per consequens, ut doceat quomodo viator est disposicior ad beatitudinem acquirendam. Illa autem que scriptura tacet, ut de nomine canis Tobie, de die iudicii et de futuris persecucionibus seculi, expedit particulariter ignorare. Cum ergo Christus et eius apostoli ceperunt ab homine dumtaxat elemosinas temporales et docuit suos discipulos precise tales recipere, ut patet Matthei X° et Luce Xª ut dictum est XI° capitulo de privilegiis, manifestum videtur quod Christus preponderavit in ecclesia sua altrinsecus illum modum dandi et recipiendi elemosinas creature.

[ENGLISH]

## ¶2 · 276.18–276.23

> [p. 276] Et confirmacio huius est quod per illas elemosinas trecentis annis et amplius plus viguit ecclesia christiana. Privilegia ergo tam singulariter et signanter concessa a principe pacis pro quibus noluit suos contendere (ut dictum est in fine proximi capituli) sunt secularibus privilegiis pociora.

[ENGLISH]

## ¶3 · 276.24–278.6

> [p. 276] Sed particularius descendendo probatur specialius particulatim conclusio, et primo quod elemosina temporalis foret seculari elemosinanti magis autentica, nam talis elemosinacio foret tam operi quam doctrine verbali regis regum similior; cum ergo operacio membri ecclesie sit eo magis autentica quo est capiti similior, quia de tanto est ab auctore approbacior, sequitur conclusio. Loquor autem de opere cum suis circumstanciis secundum quod plus sonant in moralem iusticiam (in quantum huiusmodi), sic quod de se habet plus rectitudinis operis boni de genere; et hoc intelligo [p. 277] per istam particulam cum paribus. Contingit autem per accidens occisionem hominis vel eius punicionem esse magis autenticam, quia plus Deo placentem quam data liberacio a morte vel restitucio ad prosperitatem in bonis nature vel fortune, supposito quod precedat ex maiori caritate. Verumptamen cum operacio que secundum se et secundum suas circumstancias est exemplari suo in Christo similior, debet correspondenter esse caritativior, suppono quod loquamur de autenticacione operis (in quantum huiusmodi), et cum omnis autenticacio operis nostri correspondet proporcionaliter approbacioni Christi, patet conclusio. Nemo enim debet facere opus misericordie nisi secundum doctrinam quam didicit a Christo, sed cum Christus docuit nos dare temporalem elemosinam et non sic perpetuam, sequitur quod temporalis elemosinacio sit magis autentica. Item, proporcionaliter ut operacio meritoria sapit maiorem humilitatem, est Deo placencior, et per consequens plus autentica apud magistrum qui est mitis et humilis corde; sed sic est de elemosinacione temporali respectu elemosinacionis perpetue. Ergo illa est magis autentica. Minor probatur ex hoc quod solius domini temporis qui est Deus est per se concedere donum perpetuum, unde (ut alias declaravi) non subiacet potestati hominis concedere donum pro aliquo tempore, nisi pro tempore quo ipse potest habere vel dominari eidem, cum Deus non potest concedere ius extensius sive uberius quam ipsemet potest habere. Cum ergo non sit in potestate secularis domini habere perpetuo tale donum, videtur quod non sufficit per se tam extense quicquam concedere. Et confirmacio huius est quod homo non potest ratificare perpetuitatem dominii suo heredi naturali cui magis afficitur tamquam magis capaci. Quomodo ergo rectificabit elemosinam ab approbacione Christi magis extraneam? Sicut ergo Edgarus et sanctus Edwardus [p. 278] non habuerunt potestatem ad dandum suis heredibus naturalibus dominium regni nostri, sicut patet ex conquestu sequente, sic videtur quod non suffecerunt donare accessorium persone tam extranee, ymmo sicut Willielmus conquestor non tenebatur restituere principale sic nec accessorium.

[ENGLISH]

## ¶4 · 278.7–278.11

> [p. 278] Et confirmacio est ex hoc quod multas tales elemosinas Saxonum transmutavit et monachos Normanie introduxit; quod si omnino fuisset illicitum, maior pars cleri possessionati in Anglia alienum bonum sine titulo usurparet.

[ENGLISH]

## ¶5 · 278.12–278.32

> [p. 278] Item, videtur quod multe carte perpetue elemosine sapiunt ex parte elemosinantis et male interpretantis blasphemiam et superbiam, cum multi domini seculares presumunt quod est in potestate eorum dare simpliciter in perpetuam elemosinam signatum redditum, qualibet condicione elemosinarii pretermissa; quod declaratum est proximo capitulo Deo non posse competere, cum 1° Regum II° legitur quod Deus condicionem Hely notaverat, sic quod non obstante quacunque promissione non tenet concessio, nisi servicium Dei virtuose peragat. Si ergo Deus qui potest iustificare impium et scit condiciones ac dignitates tocius generis succedencium subintellegit condicionem, ceca presumpcio videretur in homine qui nec potest donare per tantam periodum nec iustificare aliquem eius datarium, ut asserat se concedere datam elemosinam cuilibet illius generis absolute; in hoc enim implicat se sic concedere, sive Deus voluerit sive noluerit; quod non potest, cum nemo potest quicquam concedere, nisi prius Deus ipsum concesserit: ideo racione talis mendacii dissolvuntur multe elemosine vocate perpetue.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 274.26: Temporary alms are better than perpetual.
- 275.1: Definition of each.
- 275.12: Let us suppose perpetual alms in themselves to be good;
- 275.26: still temporary are better, since they have Christ's sanction,
- 276.18: and were practised in the primitive church.
- 276.24: 1. Temporary alms are more in God's way of working, and are so far, better.
- 277.18: 2. Temporary alms imply more humility.
- 277.24: Man's power over things is temporary and he cannot give rights that he does not possess.
- 278.15: Many perpetual alms are given without conditions as to the character of the grantee.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 275: *Christus* [R3]
  - 276: *Christus* [R3]
  - 276: *a* (print: concessa a principe; main lacks a) [INS?]
  - 276: *foret* (hooked ascender = f) [R3]
  - 277: *Contingit* [R4]
  - 277: *sufficit* (hyphenated suf-/ficit; main token holds whole word) [NW]
  - 278: *II°* [R3]
  - 277: *per* (alinea B and 167d folio mark glued) [THIN]
  - 277: *et* [THIN]
  - 278: *potestatem* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 274:
5. A A,: doctrina deest. 6. loc. corrupt. in codd. Fortassc legen-
dum: captivitatis paciencia. 25. cm XIII in marg. (in red ink); ib. :
cm xUlm (in black ink. 26. A in marg. : TJtrum elemosina humana
corporalis perpetua sit fundanda. 28. A in marg. : Conclusio.
3o. A A,: plus secatur.

p. 275:
10. B: dc pcncionibus. 12. i3. A, commentatur in marg. : possibili-
tatcm vel posicionem. 14. A A,: perpetuas dcest. 26. A in
marg. : Racio.

p. 276:
5. AA,: necessarius. i(5. B: XX. cap. 24. A in marg.:
Confirmacio. 3o. AB: approba"'. A, : approbabilior; B: de tanlo ab.

p. 277:
(none)

p. 278:
4. B: extranie. 9. B: fuisset — titulo deest. 21. Aj corr. :
teneret. 21. B: servicio. 22. Ainmarg.: racio. 24. A At:
subintellexit. 25. 26. A A, : durare per tantam.
```
