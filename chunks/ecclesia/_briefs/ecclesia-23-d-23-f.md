# Translation brief: ecclesia 23-d–23-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-23-d.md chunks/ecclesia/wyc-ecclesia-23-e.md chunks/ecclesia/wyc-ecclesia-23-f.md` once and fix what it reports.
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

## Glossary (the 208 rows these chunks use; the full file is GLOSSARY.md)

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
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| simonia | simony | Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| legii | lieges | Ruled 2026-10-02 (*Eccl.* 15, 343–344). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| copia / habundancia | plenty / abundance | Ruled 2026-10-02 (*Eccl.* 23, 553.15, 555.20). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |

---

## Chunk 23-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "558.24–561.18"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 4 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "703 words; 640 unanimous or majority-real; 52 settled by vote (R2 32, R3a 19, R6a 1); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n595–n598 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 4: [TITLE]

## ¶1 · 558.24–559.13

> [p. 558] ad salutem qui non vult iuvare Christum ad suam satisfaccionem, quia Psalmo LXI°, 13 dicitur: Tu reddes unicuique iuxta opera sua. Sic ergo tam militans quam triumphans satisfacit pro viatore indebitato quoad Deum, sed oportet ipsum indebitatum omnimode se ipsum iuvare, quia aliter ipse non solveret quod debebat, et per consequens non fuit [p. 559] apud Deum illo debito exoneratus, sed unus alius a quo Deus debitum illud exigit, non ab illo. Ideo videat homo si potest esse beatus pure per procuratorem, et tunc concipiet si potest satisfacere pure per procuratorem; oportet enim percipientem premium persolvere meritum. Unde non foret onus meum, ad quod supportandum alius me iuvat nisi ego debeam satisfacere pro illo. Ideo dicit Apostolus: Unusquisque onus suum portabit Gal. VI°, 5. Sic ergo ex vi communionis sanctorum habemus reciproce adiutores, in tantum quod Dei adiutores sumus secundum Apostolum Iª, Corinth. 111°, 9 seu oportet quod cum adiutorio isto simus cooperatores.

[ENGLISH]

## ¶2 · 559.14–560.5

> [p. 559] Ad secundum argumentum patet quod conclus est concedenda, sed nunquam potest unus dampnare alium quoad Deum, nisi ipse superaddat proprium delictum, ut patet in materia de originali peccato, et ideo canit fidelis ecclesia quod nulla ei nocebit adversitas, si nulla dominetur iniquitas. Quomodo, queso, posset Deus dampnare non reum et per consequens non dampnabilem? Et patet bonitas Dei in hoc quod neminem salvat, nisi quem prevenit adiuvando, nec aliquem dampnat, nisi a quo preveniente occasionem accipit ex peccato. Et patet quod licet brachium se exponat pro capite, tamen oportet caput quodammodo se iuvare. Ideo quamvis quodlibet membrum iuvet aliud ad agendum, tamen nullum membrum supplet omnino alterius membri officium, sed iuvando satisfacit; et sic est de corpore Christi mistico, quia aliter posset Deus omnino eximere hominem a debito servitutis quoad Deum, quod notum est claudere repugnanciam formalem. Ideo sicut Deus in opere creacionis non potest habere naturam coadiuvantem [p. 560] propter solitudinem sue supereminencie, sic creatura non potest opus quodcunque perficere nisi cum iuvamine alterius nature propter per se subieccionem servitutis et essencialem dependenciam a suo principio. Et per hec patet responsio.

[ENGLISH]

## ¶3 · 560.6–561.18

> [p. 560] Ad tercium dicitur negando minorem, nam oportet F Deum in omni satisfaccione creature sue concurrere et est in racione debiti hominis ad hominem ac in racione debiti hominis ad Deum neganda differencia. Homo enim potest omnino solvi a corporali debito sui ad hominem, quia non est essencialiter debitor sui pro omni bono quod possidet, quia tunc alius foret Deus suus, sed nemo potest omnino eximi a debito Dei sui, quia tunc non teneretur Deo pro esse suo, sed foret Deus simpliciter par cum illo. Ideo ista est condicio obligacionis hominis ad Deum, quod de quanto copiosius et complecius solvit sibi debitum de tanto est obligacior quoad eum, quia de tanto plus boni ab eo recipit. Et hec racio quare homo potest recipere satisfaccionem debitoris sui in vita vel morte eius per procuratorem ipso non cooperante ad hoc. Deus autem non potest recipere a servo suo satisfaccionem pro debito nisi ipse in persona propria satisfaciat adiutus per Deum, et hoc testatur immensitatem libertatis Dei et excellenciam sui dominii, ut non oportet, si homo potest libere ac meritorie exuere se a dominio servi sui subiciendo se sue servituti, quod deitas sic potest quoad servum simpliciter; homo potest relinquere domini superioris vindictam offense non vindicando in persona propria, ergo Deus sic potest; homo potest dimittere culpam non expetendo sibi emendam satisfactoriam, ergo Deus sic potest, et sic de infinitis exemplis attestantibus infirmitatem humani dominii et invincibilitatem dominii divini. Et patet [p. 561] quod ista sentencia est pia fidelibus sese consolantibus in domino et non blaspheme exigentibus honorem debitum soli Deo, unde qui putat peccatum commutari vel vendi pro nudo numismate implicat quod Deus vendit a se dominium parificans sibi creaturam a qua non exigit servitutem, et per consequens Deus venderet se ipsum, quia insuperabilem iusticiam, pro vili precio proprio, ut puta, pro minuta, cum pro qualibet parte precii venderet indivisibilem iusticiam que est Deus. Sed quid rogo blasfemius? Ideo si quis peccat in Deum, oportet quod ipse in persona propria expectat satisfaccionem vel satispassionem ab eadem persona, qui in eum peccaverit. Et patet quod primum assumptum est falsum, videlicet quod Deus potest peccata sine satisfaccione dimittere vel communicare vicario suo potenciam vel peccata taliter remittendi vel contra peccata taliter dispensandi. Hoc enim est de regalia propria deitati.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 559.14: As to the second argument one man's sin cannot cause another's damnation without fault of his own.
- 560.6: As to the third argument a debt to man is different in nature from our debts to God,
- 560.17: which increases the more we pay.
- 561.5: The pardon of sin for money would imply that God sells righteousness,
- 561.10: 1. e. himself.
- 561.15: God cannot remit sin without satisfaction.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 558: *illius* (print: debito / illius ad salutem) [INS?]
  - 558: *∅* (duplicate INS? at same pos 158 (ilhus = illius), given on the illius row) [INS?]
  - 559: *procuratorem* (main token holds whole word (procu- / ratorem); 204c folio mark on next line) [R4]
  - 559: *Iª* [R3]
  - 560: *dependenciam* [NW]
  - 560: *tanto* (English side-note "we" in slot of Latin tanto) [R3]
  - 560: *est* (print: tanto est obligacior) [INS?]
  - 561: *quod* (204c is the glued folio mark) [THIN]
  - 561: *parificans* [NW]
  - 561: *sibi* (English side-note "The" glued) [NW]
  - 561: *blasfemius?* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 558:
2. contento; in codd. A: co"> (cotitato? cf. partem cotam p. 5io, 1- 6);
B: to">. 3. B: totalem satisfaccionem. 4- B inmarg.: Satisfaocio
pro alio tripliciter fit. 6. B in marg.: Christus assumpsit naturam
nostramin athomo. io. confratrum; B: consivium (src). 18. B m
marg.: Apparet quod si infans discedens absque baptismo flamims admdi-
cabitur eternc pene propter culpam primorum parenfum ipso in persona
propria non demerente: pcr idem posset bcatus pro pcccantc satisfacere
peccatore, pro commisso nullatenus satisfacicnte. 25. In codd. LXXXl.

p. 559:
14. B in marg. : Istud ut videtur obviat eis qui ponunt infantcm discc-
dentcm absque baptismo flaminis forc inevitabilitcr dampnatum. 20. A in
marg. : Solnciones utiles arfjumentorum supra positorum (Abovc 204«
without mark of refcrence).

p. 560:
3. B: alterius nec. 8. B in marg. : Raciones debitorum hominis
ad hominem et hominis ad Deum differunt.

p. 561:
i. B: de se consolantibus. 5. A in marg. : Nota de usurpata
auctoritate pape. 18. B in marg.:Quid per hoc intelligit, cum dicit:
Hoc enim est de regalia propria deitati ? cum prius fit responsio de potencia
dispensandi contra peccata per satisfaceionem altcrius non per sentcnciam
suam cst tenendum quod Deus ipse aut papa aliquis potest contra pcc-
catum aliquod dispensarc nisi persona delinquens satisfaciat in persona
propria? Quid ergo est illud quod cst de rcgalia propria deitati ?
19. Cf. pag. 356, 9.
```

---

## Chunk 23-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "561.19–564.31"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 5 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "765 words; 730 unanimous or majority-real; 26 settled by vote (INS 1, R2 11, R3a 10, R3b 1, R5a 2, R6a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n598–n601 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 5: [TITLE]

## ¶1 · 561.19–563.6

> [p. 561] Et per hec patet responsio ad primum argumentum quo suadetur dominum papam de facto sic facere; non enim pretendit vicarius Christi aut Petri vel sic se posse facere, nisi forte blasphemet et postea resipiscat. Unde signum infallibile foret homini quod sit extra regulam quam Christus suis instituit, nec sit de numero illorum pro quibus Christus tunc oravit, si potestatem talem sibi usurpaverit, nec sollicitor circa facta talia particularia dominum papam vel confratres suos temere accusando, sed scio quod si finaliter consummat in ista sentencia, nec fuit Christi vicarius nec eciam christianus, quia non intravit [p. 562] humiliter per ostium Christum ad tale officium, sed ascendit aliunde violente per tractum regis superbie, et per consequens est, si factum suum sic se habuerit, fur et latro. Ad secundum argumentum captum ex dicto Christi Matthei XVI° patet ex sepe dictis quod quicunque sic extollitur, vel ad eum de potestate data Petro et eius vicarii) ideo necesse est papas addiscere scolam Petri specialiter in humilitate et ministerio spirituali, quia aliter non est ille qui sic pretenditur, ut patet quadragesima distinccione. Oportet ergo dominum papam circumspicere ut teneat se in limitibus sancti Petri, et specialiter quod notet verba scripture sacre, non usurpando quod ligat et solvit in purgatorio subter terram nec ascendit in celum imperciendo premia beatorum, cum sint insolubiliter limitata, sed oportet quod teneat se virtuose in medio super terram. Et patet quod minor argumenti est falsa, nam unus apostata potest pretendere se sic solvere vel ligare, sed non exhinc sequitur quod sic facit. Ideo (ut sepe dixi) oportet dominum papam cavere de modis sophisticis. of Ad tercium argumentum dicitur quod minor est falsa, cum deitas Christi, scriptura sacra et beatus Petrus relicti sunt in ecclesia militante ad ipsam regulandum et eius dubia decidendum, que tria secundum singulum non sunt vicarii sancti Petri. Christus enim in ascensione sua dereliquit humanitus deitatem suam in terris, sed non divisit, cum copulatus [p. 563] est sibi ypostatice, ubicunque fuerit humanitus, et ipsa deitas est caput ecclesie. Christus autem humanitus reliquit testamentum suum in terris per quod voluit suam ecclesiam regulari, nec voluit quod crederetur alicui Petri vicario, nisi de quanto vivit et docet conformiter illi legi.

[ENGLISH]

## ¶2 · 563.7–564.6

> [p. 563] Unde quicunque sacerdos ecclesie post mortem Petri vivens et docens testamento illi conformiter potest racionabiliter dici Petri vicarius, sed specialiter ille qui vivit Petro conformius et ad istam doctrinam testamenti Christi similius; et ille supponitur esse Romanus episcopus, sed in synodis pro dubiis decidendis non est credendum cuicunque vianti, nisi de quanto dictum suum fundaverit in scriptura. Unde non est credendum quod fides catholica vel in veritate que creditur vel in habitu ecclesie catholice dependet ab ista persona, cum sit errabilis et de possibili non membrum ecclesie. Ego autem non sollicitor quid papa facit vel loquitur, cum scio quod nec sibi nec alicui istorum doctorum credendum est nisi de quanto se in scriptura fundaverit, cum in ipsa sit omnis veritas proporcionaliter, ut est necessarium ipsam nosci (ut patet secundo De Doctrina Christiana in fine). Unde sepe miratus sum quomodo aliquis istorum trium doctorum fundaret supradictam sentenciam in scriptura. Scimus autem quod papa cum cetu cardinalium eciam in materia fidei sepe errat, sed supponendum est quod scriptores bullarum papalium vel examinatores aut falsi suggestores sepe falsificant bullas suas, sicut noverunt auctores scripture de multis indulgenciis, de multis collacionibus [p. 564] prefecturarum et de multis privilegiis et terroribus censurarum; ideo tales apud Deum incurrunt penam falsarii et sunt apud potentes, scientes et ordinate volentes notabiliter renotandi. Caput ergo ecclesie Christus cum scriptura sua et sanctis doctoribus debet esse regula ecclesie in dubiis decidendis.

[ENGLISH]

## ¶3 · 564.7–564.22

> [p. 564] Secundo principaliter restat obicere contra fictas indulgencias, et primo contra sentenciam que imponitur sancto Thome, quia in ista materia concordant doctores alii, tam decretiste quam theologi. of Primo (inquam) videtur quod supererogata meritai Christi et membrorum suorum olim transierunt, et per consequens vel non sunt vel, si sunt pro suo tempore, sunt extra potestatem ordinariam iam superstitis Romani pontificis. Quid (queso) valet fingere quod iste Gregorius XI. ordinavit et instituit ut ymmolacio Ysaac et cetera merita patrum tantum precedencium in utroque testamento valeret ad ordinacionem suam cognato suo iam mortuo? Non enim valet fingere mendacia infundabilia propter extollenciam potestatis. Quomodo (rogo) est copia meritorum que non sunt, aut quomodo tam determinate lapsa in preteritum

[ENGLISH]

## ¶4 · 564.23–564.31

> [p. 564] cum omnibus suis appendiciis sunt in potestate nostra, cum omnis actus quem nos ipsi fecimus preteriit potestatem nostram? Quomodo ergo distribuit ipse ista opera que non sunt in potestate sua? Nec valet fingere quod distribuit fructus istorum operum, quia illi non sunt nisi premia que sunt beatitudines quas non est in potestate sua a beatis auferre vel peccatoribus donare, quia tunc bonificaret eos, quod foret deliramentum asserere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 561.19: Certainly then the Pope cannot,
- 561.27: and he cannot be a Christian if he claims such a power.
- 562.5: To have Peter's power the popes must follow Peter in humility and service.
- 562.23: The head of the Church is Christ's divinity;
- 563.3: and Christ has left his testament to guide us.
- 563.12: In things doubtful the only authority is Scripture.
- 563.26: The Pope and Curia err, and their bulls are often falsified.
- 564.11: The merits of Christ and his Saints are things past,
- 564.22: and so beyond our power.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 562: *humiliter* [THIN]
  - 562: *Christum* [THIN]
  - 562: *fur et latro.* (print line is "fur et latro." only; tr*k is noise) [GAP]
  - 562: *et eius* (print: Petro / et eius vicariis,) [INS?]
  - 563: *et ipsa deitas est caput ecclesie. Christus autem humanitus reliquit testamentum suum in terris per* (two print lines; rehquit = reliquit, m = in on the ink) [GAP]
  - 563: *non* (205a is the glued folio mark) [R4]
  - 564: *multis* [R3]
  - 564: *cum omnibus* (print: cum omnibus suis; cum has no main-scan token, appended here) [R4]
  - 564: *bonificaret* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 561:
i. B: de se consolantibus. 5. A in marg. : Nota de usurpata
auctoritate pape. 18. B in marg.:Quid per hoc intelligit, cum dicit:
Hoc enim est de regalia propria deitati ? cum prius fit responsio de potencia
dispensandi contra peccata per satisfaceionem altcrius non per sentcnciam
suam cst tenendum quod Deus ipse aut papa aliquis potest contra pcc-
catum aliquod dispensarc nisi persona delinquens satisfaciat in persona
propria? Quid ergo est illud quod cst de rcgalia propria deitati ?
19. Cf. pag. 356, 9.

p. 562:
1. Per ostium Christum; conferas Johannis X, 7. B in marg. : Ex hns
verbis innoscit (sic) quis dicendus sit Christi vicarius secundum eum.
8. et eius vicariis. Hoc loco aliquot verba excidisse videntur. 8. addiscere ;
B addicere. 21. A A,: Ideo - sophisticis deest. 23. A m
marg.: Nota quis debet dubia ecclesie decidere? 27. singulum;
A B: singlm. 28. B in marg.: Christus in sua ascensione dereliquit
humanitus deitatem suam in terris sed non divisit.
5. Cf. pag. 556, 22. n. Decreti prima pars, dist. XL,
capp. VI et VII. 23. Compare pag. 556, 3o.

p. 563:
i3. B in marg. : Quale est premium accibile bonorum? 24. A in
marg. : Augustinus. 24. A A,: sepe deest. 25. B in marg. :
Sanctus Thomas, doctor Bonaventura ct Wilhelmus de reliquiis et vene-
racione sanctorum. 27. B : cum cet.
24. Aug. Opp. tom. III, p. [, pag. 44.

p. 564:
1. A (ut saepius): pravilegiis. 5. A A, : sciencia docloribus.
7. A in marg. : Secundum principale. 11. A in marg. : Hic arguitur
contra fictas et falsas indulgencias. 12. 11 : iransierant. 18. B: ad
ordinacionem — propter deest. 32. A Ai : districtum est a Dco.
```

---

## Chunk 23-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "564.32–568.24"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 6 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "915 words; 859 unanimous or majority-real; 45 settled by vote (R2 21, R3a 21, R3b 1, R5a 2); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n601–n605 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 6: [TITLE]

## ¶1 · 564.32–566.25

> [p. 564] Item, omnibus beatis diffinitum est a Deo premium beatitudinis correspondenter ad omnia merita sua, [p. 565] que adhuc manent in fructu, sed aliqua merita, requisita ad beatitudinem patriarcharum, non subiacent potestati huius Gregorii sic distribuere racione premii ex eis limitati; ergo nec alia. Assumptum patet, tum quia nihil est ociosum in meritis beatorum, tum quia beati habent gaudium et sic premium accidentale de quocunque bono quod fecerint. Minor autem sic ostenditur: In facta distribucione meriti stricte requisiti ad beatitudinem essencialem diminueretur de illa beatitudine correspondenter, quam iniuriam non potest papa facere, sicut nec Christus potest concives suos sic depauperare. Sed dicitur quod meritum beatorum, cum sit spirituale, non excommunicacione tali minuitur sed pocius perficitur. Sed (rogo) ad quid limitantur tunc merita supererogata ultra mensuram debitorum suorum vel superhabundanciam meritorum, cum merita stricte ad beatitudinem requisita eque sufficerent ad distribucionem huius faciendam, aut quomodo est necessarium ponere nunc tantam copiam talium meritorum? Videtur multis fidelibus quod non est modo numerus talium meritorum, vel aliter omnia illa et longe plura si fierent non -sufficerent ad aliquem gradum beatitudinis promerentis, nisi quod Deus ex infinitate gracie sue acceptat merita illa de congruo. Item, iuxta istam sentenciam sequitur quod potestas iudiciaria cuiuscunque pape se extendit ad omnes animas Jn purgatorio et omnes beatos in celo; consequens impossibile, et consequencia sic probatur: papa eciam prescitus habet potestatem ad imperciendum merita bonorum cuicunque et quandocunque voluerit, ut dicit posicio; sed longe minor potestas sufficit ad fundandum iudiciariam potestatem, ergo papa habet iudiciariam potestatem super beatos eciam super Christum. Potest enim facere quod beatus [p. 566] mereatur cuicunque affecto suo quantumcunque voluerit, quia potest dare sibi meritum alterius, quod est idem. Ille enim qui habet potestatem super tam secretum thesaurum anime habet potestatem super personam quoad inferius corporale; in cuius signum Deus dedit dyabolo potestatem primo super substanciam beati Job, secundo super corpus. Verumptamen, inquit, animam eius serva, Job II°, 6. Et multo evidencius sequeretur quod papa preest cuicunque spiritui in purgatorio vel dampnato, et hoc videtur doctorem intendere, cum dicit quod bona communia multitudinis distribuuntur singulis de illa multitudine secundum arbitrium eius qui illi multitudini preest, et multo evidencius sequitur quod papa preest dampnatis, cum preest personis dignioribus, ut puta, purgandis spiritibus et beatis; qui enim habet potestatem cassandi opus dyaboli et tollendi ab eo predam quam tantum appetit, habet potestatem in eum, sed papa habet potestatem ad dandum quantamlibet indulgenciam captivo dyaboli, ne sufficiat amplius valere in eum, ut dicitur. Dicitur et Luce IX° quod Christus dedit discipulis potestatem super omnia demonia, sed nimis ampla foret pape iurisdiccio, qui instar Christi habet potestatem super multitudinem celestium, terrestrium et infernorum.

[ENGLISH]

## ¶2 · 566.26–566.33

> [p. 566] Ex istis colligitur, cum tot inconveniencia sequuntur ex dicta palliacione potestatis papalis, quod radix istorum inconveniencium foret fidelibus venenosum. Quod autem ista sint inconveniencia, patet primo ex hoc quod secundum apostolum Roman. XIII°, 1 non est potestas nisi a Deo. Ipse autem non reliquit in lege sua papis huiusmodi potestatem, ergo non est fingenda, nam per idem foret infinitum amplianda.

[ENGLISH]

## ¶3 · 566.34–567.13

> [p. 566] Secundo per hoc quod pape singuli citra Christum sunt paris potestatis; cum ergo par in parem non [p. 567] habet imperium, videtur quod papa superstes non habet potestatem super omnes papas in purgatorio et in celo. Illi enim sunt excellenciores quia Deo propiores et cariores. Ideo oportet quod papa superstes serviat eis et non imperatorie concedat quod Petrus vel alius beatus mereatur amico suo quantumcunque sibi placuerit limitare. Et tercio per hoc quod papa superstes non habet tantam potestatem super corpus vel opus proprium, ergo multo magis non super opus Dei tam sibi alienum; homo enim quadam naturalitate dominatur super actibus et operibus propriis, nec autor nature dedit pape potestatem adversantem ordini naturali.

[ENGLISH]

## ¶4 · 567.14–568.4

> [p. 567] Assumptum patet ex hoc quod tunc posset facere opus suum esse quantumcunque meritorium sibi placuerit, quia limitare beatis quod sibi assisterent quantumcunque voluerit promerendo. Stultus enim foret qui propter fastum vel questum plus benefaceret alteri minus digno, quam eciam benefaceret sibi ipsi, et si dicatur quod potestas non datur ut sic benefaciat sibi ipsi, patet quod Deus dat potestatem solum ad bonum suo predestinato. Ideo daret suo vicario potestatem, ut sibi retribuat tantum bonum. Sed Hostiensis (ut recitavi superius) horrebat istam ficticiam, quia certum videtur quod, si haberet tantam potestatem super demonia et super cunctos subditos suos quoad corpus et animam, haberet eciam potestatem super eorum substanciam, et tunc multi pape (ut creditur) fecissent miracula, mandando spiritibus afferre sibi thesauros absconditos et acquisivissent sibi dominia adeo affectata. Sed (ut innuitur Act. 111,6), quia Petrus non habuit possessionem auri vel argenti, ideo habuit potestatem sanandi [p. 568] infirmum, sed Simon, quia affectabat temporalia, caruit apostolica potestate (ut patet Act. VIII°). Apostoli enim denudati ab affeccione temporalium habuerunt super eis spiritualem potestatem atque dominium.

[ENGLISH]

## ¶5 · 568.5–568.24

> [p. 568] Item, secundum doctorem beati non fecerunt determinate huiusmodi superhabundancia opera satisfactoria pro isto vel isto qui remissione indiget, ideo restat ut Deus derelinquat vicario suo in terris distributivam potestatem illius thesauri egenis ecclesie; sed illud videtur multipliciter palliatum, ergo posicioni deficit fundamentum. Minor probatur primo, per hoc quod eque probabiliter contingit sompniare quod tales beati determinate fecerunt ista opera supererogacionis pro illo qui eis participet, sicut quod reliquit papam, quod ipsa distribuat; ideo videtur peti ignotum per ignocius. Secundo quia dicti sancti fecerunt opera sua ex maiori gracia quam fuit illa in qua communiter vivunt pape, ideo verisimile est quod fecerunt ipsa principaliter pro ecclesia, relinquendo distribucionem divino arbitrio; hoc enim est habilitatis, sapiencie et necessitatis. Sed tunc fecissent determinate pro illis ad quos Deus limitat, ergo verisimile est quod meruerunt determinate pro illis, et hoc est certum quoad determinacionem divinam cui oportet stare.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 565.1: God has rewarded the Saints according to their merits.
- 565.9: To distribute the merits would be to diminish the rewards.
- 565.21: Merits would not suffice to the Saint himself but for God's grace.
- 565.26: The power claimed makes the Pope judge of all souls, even in purgatory and heaven;
- 566.10: much more in hell.
- 566.30: All powers are of God, who has left no such power to the Pope.
- 567.2: An undue power is claimed for the actual Pope over his predecessors.
- 567.10: The Pope might appropriate all merits to himself;
- 567.26: and would have demons at his service.
- 568.5: We do not know that these merits have not been assigned;
- 568.20: as indeed they probably have been by God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 565: *que* (margin letter H and 205a folio mark glued) [THIN]
  - 565: *in* [THIN]
  - 565: *fructu,* [THIN]
  - 565: *merita,* (English "God" follows in side-note) [THIN]
  - 565: *meritorum,* [R3]
  - 566: *II°* (comma dropped per superscript rule) [R3]
  - 566: *1* (print: Roman. XIII°, 1 (verse); leaf zoom: short old-style 1, lower than the capitals) [INS?]
  - 567: *habet* (205b is the glued folio mark) [THIN]
  - 567: *Illi* [R3]
  - 567: *cariores.* [R3]
  - 565: *∅* (second half of subia-cent; neighbour 13 already subiacent) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 564:
1. A (ut saepius): pravilegiis. 5. A A, : sciencia docloribus.
7. A in marg. : Secundum principale. 11. A in marg. : Hic arguitur
contra fictas et falsas indulgencias. 12. 11 : iransierant. 18. B: ad
ordinacionem — propter deest. 32. A Ai : districtum est a Dco.

p. 565:
">.. B: requisita — potestati deest.

p. 566:
8. In codd.: Job primo. Correxi. M. B: Et Luce IX» dicitur.

p. 567:
10. B in marg. : Item, difficile videtur dicere quod talia mcrita bonorum
in patria que dominus papa prctcndit sc imperliri sccundum votum
suum adhuc remancant irrcmunerata, saltem cum dominus premiat
ultra condignum ct punit cilra.

p. 568:
6. and 3.. huius in codd.
```
