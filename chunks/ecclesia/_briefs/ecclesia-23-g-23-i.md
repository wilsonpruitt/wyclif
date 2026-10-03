# Translation brief: ecclesia 23-g–23-i

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-23-g.md chunks/ecclesia/wyc-ecclesia-23-h.md chunks/ecclesia/wyc-ecclesia-23-i.md` once and fix what it reports.
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

## Glossary (the 200 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| claustrales | cloisterers | Ruled 2026-09-28 (20 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
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
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| preconium | commendation | Ruled 2026-10-02 (*Eccl.* 20, 488.20). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| taxacio (pene) | assessment | Ruled 2026-10-02 (*Eccl.* 21, 498.8). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |

---

## Chunk 23-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "568.25–570.27"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 7 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "497 words; 475 unanimous or majority-real; 15 settled by vote (R2 6, R3a 7, R3b 1, R5a 1); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n605–n607 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 7: [TITLE]

## ¶1 · 568.25–570.27

> [p. 568] Tercio, quia beati vident continue in verbo quibus merita sua proficient, sicut eternaliter Deus necessario limitavit quibus proficient. Sed Deus nichil facit superfluum sive inconsonum, ergo non reliquit potestatem suis vicariis ad ista suffragia distribuendum. Superfluum dico, quia eo ipso quo Deus ordinat vel limitat quod isti vel isti proficiet sancti suffragium, eo ipso sic proficiet et aliter non, quomodocunque papa decreverit. Ideo foret omnino superfluum relinquere pape huiusmodi distributivam potestatem; non enim sapit quod super decreto pape [p. 569] in talibus dependet ordinacio Dei eterna, intuicio benefica vel premiacio Dei iusta; superflua itaque foret potestas propter cuius officium nec maius nec minus contingeret. Item, Deus propter nullam magnificenciam papalis potencie preiudicat sue iusticie, sed hoc contingeret data ista potencia, ergo illa non est fingenda. Minor sic probatur: Papa sicut tota ecclesia militans errat in multis que concernunt divinum iudicium et statum ecclesie triumphantis, sed inter alia archana huiusmodi hoc est unum, quis quante sit dignus ecclesiastico suffragio quoad Deum, ergo stat papam communiter errare in talibus. Ideo ergo oportet concedere quod eo ipso quo papa concedit alicui tantam indulgenciam eo ipso sic habebit, vel aliter non obstante concessione pape precise tantum participabit quantum dignus fuerit aput Deum, vel aliter quod papa generaliter intelligit istam condicionem in concessione sua qualibet, ut oportet. Prima pars est omnino impossibilis, implicans papam illum non posse peccare vel errare, et sic papa per se habilitaret et iustificaret subditum quoad Deum; quod foret blasphemum dicere. Ideo restant secunda via et tercia concedende; sed constat non oportere sumptuose acquirere tales bullas, quia illis subductis homo precise tantum participabit de merito quantum fuerit habilis apud Deum. Et quantum ad clausulam positam in bullis, quod datur tantum spirituale suffragium vere contritis et dignis apud Deum, vel de tanto absolvitur de quanto claves ecclesie non errantes permiserunt, videtur quod quilibet fidelis in haberet hoc privilegium sine bulla, et quod quilibet sacerdos posset tante absolvere, et sic absolucio a [p. 570] pena et culpa introducta in opinione populi foret simplicium seductiva, et sequeretur utraque conclusio quam doctor reliquit ut inconveniens, scilicet quod absque omni tali indulgencia dignus apud Deum remissionem proporcionaliter sequeretur et indulgencie communiter fierent pro tota ecclesia. Profectum enim tocius ecclesie debet papa primo intendere et distribucionem premii iudicio divino relinquere, ut oportet. Ex quibus videtur quod non est altrinsecus valde meritorium instare penes papam pro indulgenciis huius acquirendis, quia vel oportet dicere quod racione huius occupacionis fit homo dignior apud Deum, quam foret omittendo talem instanciam, vel aliter quod ad habendum affectatam indulgenciam foret concessio vel bulla papalis indifferens. Primum non dabitur propter tria: Primo quia apostoli, quos spiritus sanctus docuit omnem veritatem, culpabiliter omisissent occupacionem tam meritoriam pro indulgenciis impetrandis; secundo quia tunc papa prorogaret concessiones huiusmodi, ut subditus diucius continuet in vita tam meritoria; et tercio facta tota diligencia tantum valeret petenti nec habere concessionem pape vel bullam sicut papam concedere vel bullare, et sequeretur tercium membrum quod multa officia clericorum papalium condempnarent. Tales multas evidencias cogitare possumus per quarum obiecciones et soluciones veritas catholica declaretur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 568.25: God has preordained who is to profit by them, so the Pope's decree is superfluous.
- 569.4: The Pope cannot judge worthiness in God's sight; therefore either
- 569.13: a) his indulgences take effect without worthiness in the recipient;
- 569.16: b) the recipient profits simply according to his worthiness;
- 569.21: c) this condition is implied in the indulgence.
- 569.24: a) is blasphemous b) and c) make indulgences useless.
- 569.29: So the conditional clause in bulls makes them merely superfluous.
- 570.9: It follows that a man is not the better for soliciting indulgences.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 569: *in* (205c is the glued folio mark) [THIN]
  - 569: *archana* [NW]
  - 569: *generaliter* [R4]
  - 569: *haberet* [R4]
  - 570: *valde* (M is a margin letter) [R4]
  - 570: *vel* [R3]
  - 568: *quibus* (L is a margin letter) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 568:
6. and 3.. huius in codd.

p. 569:
io. huius in codd. 14. sic habebit sc. si dignus sit ecclesiastico
suffragio quoad Deum. i5. non non tn codd. 18. B: in conccsso
est sua. 23. Codd. : concedenda. 32. B: caute absolvere.
4. Cf. Hus, Opp. tom. I., i83b.

p. 570:
li. B: hius. 27. B: obiecciones soluciones.
```

---

## Chunk 23-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "570.28–574.32"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 8 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "987 words; 940 unanimous or majority-real; 43 settled by vote (R2 23, R3a 17, R5a 2, R6a 1); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n607–n611 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 8: [TITLE]

## ¶1 · 570.28–574.22

> [p. 570] Ulterius fiunt argumenta communia contra omnem theologorum et decretistarum sentenciam in hac parte. Videtur enim, primo quod potestas pape sit potencia infinita; nam papa habet potestatem ad concedendum indulgencias infinitis personis per infinitum tempus duraturas, ergo infinitum maioris potencie est quam episcopus, qui solum quadraginta dies solum finitis subditis potest concedere. [p. 571] Consequencia patet ex hoc quod penes hoc est potestas maior, cum omnes ille sint univoce consimilis speciei; et antecedens videtur, tum quia super totum thesaurum ecclesie dominatur papa, qui thesaurus est quodammodo infinitus, tum quia non est dare quot personis potest papa thesaurum illum distribuere nec ad quantum. Item, videtur quod papa debet ex consciencia facere generaliter illud opus misericordie spiritualis, nam potens relevare fratrem suum et inexcusabiliter differens usque ad mortem corporalem fratris sui est reus homicidii, ergo multo magis differens liberare fratrem a morte spirituali, cuiusmodi est quicunque papa avarus de indulgencia generali; nec valet dicere quod potestas prelati in isto vilesceret, quia generaliter potentatus ex beneficii percepcione fit carior. Quam ergo excusacionem haberet qui a dampnacione perpetua posset proximum liberare quem debet diligere ut se ipsum, et tamen sine racione omittit? Numquid ille cui preceptum est eciam in sabbato extrahere bovem fratris de puteo non incurret prevaricacionem, si negligit liberare animam proximi ab inferno? Si ignorancia voluntatis divine excusat, quomodo alicui concedere talem indulgenciam papa temptat? Item, posito quod dictus papa Gregorius laxet ad tantum plenitudinem potestatis quantum Deus permiserit, et potestas sibi data suffecerit ad iuvandum spiritus in inferno, in purgatorio et hoc mundo, et sic concedat cuicunque presbitero plenitudinem vicarie potestatis ad absolvendum et indulgendum generaliter tam vivos quam mortuos, quantumcunque claves ecclesie permiserint, casus non videtur negandus, [p. 572] quia tunc dictus Gregorius non foret precise tante potestatis quante foret papa alius post vel ante, ymmo non precise tante potestatis quante ipsemet foret, quia non foret dare in eo maximam potestatem nec aliquam parcialem potestatem (ut patet in materia De Maximo et Minimo). Admisso ergo casu videtur quod omnes spiritus liberarentur de inferno et purgatorio, et omnes viantes forent in gracia finalis perseverancie confirmati. Nam thesaurus ecclesie cuius accepit plenam dispensacionem est infinitum plus bonus quam habitus sibi oppositus est malus, et limitatur secundum sui ultimum ad agendum; ergo extingueret totum malum. Quis ergo argueret talem papam de imprudencia qui destrueret totam mundi maliciam, restituendo seculum aureum, ut in statu innocencie? Et cum quo Deus tam efficaciter concurreret approbando? Excitandus ergo foret papa ad tam instanter proficiendum ecclesie, si non diffidit, sed confidit in plenitudine potencie quam pretendit. can Item, dominus papa potest remittere medietatem Vel terciam partem tocius penitencie aut quamcunque partem eius aliquotam (ut dicit ista posicio et perdoniste preconizant) in patria, sed si hoc potest tunc potest totalem penitenciam omnino remittere, et sicut de una persona, sic de totali ecclesia; ergo potest preservare totalem ecclesiam ab omni pena purgatorii vel inferni. Hic dicunt decretiste communiter quod papa non remittit regulariter secundum partem quantam sed quotam, ut tetigi per Hostiensem superius et recitat glossa in decretis, XIIIª q. IIª super capitulo Tempus; et ista scola videtur [p. 573] sompniata ut populus habeat continue aliquid redimendum. Contra istud queritur, primo utrum papa potest de plenitudine potestatis sue pro quocunque opere eque meritorio in persona habente tantum de culpa et eque capaci venie tantum peccatum remittere? Si potest, pono quod concedat cuicunque vere confesso et contrito facienti elemosinam ut quatuor, remissionem peccati ut quatuor, et indulgenciam ut quatuor, et pono insuper quod quilibet peccator iam militantis ecclesie multiplicet elemosinas, quousque totum peccatum suum sit dimissum et pena remissa, sicut faciliter hoc ordinato posset contingere. Illo ergo statuto pro lege perpetua faciliter excluderetur dyabolus a punicione hominum in inferno et tolleretur omnis punicio in purgatorio, et per idem liberarentur per tales indulgencias mortui puniti vel in purgatorio vel inferno. Si dicatur quod papa non potest statuere talem legem, sed oportet ipsum proporcionaliter semper remittere, videtur primo quod hoc derogat potestati divine, quod Deus personis eque dignis non potest tantam mercedem tribuere pro meritis paribus, ut Petro habenti peccatum ut octo in purgatorio vel inferno potest dare remissionem pene et culpe ut quatuor pro elemosina viatoris dantis pro eo denarium. Paulo autem ibi detento pro peccato ut quatuor non posset dare cum illis paribus remissionem pene et culpe ut quatuor pro tanta elemosina in via facta pro ipso, quia tunc posset Deus communicare potestatem talem eius vicario, ut omnino absolveret a pena et culpa tam vivos quam mortuos. Sed constat quod primum assumptum sequi ex opinione claudit contradiccionem; secundo videtur istam sentenciam derogare potestati papali, quia, si lex ligat papam [p. 574] quod potest facere maius et non minus, quomodo concederetur legi sue, quod taxat ad votum pro quantumcunque parva elemosina remitti quamcunque partem aliquotam pene vel culpe: Numquid eo ipso quo ipse dicit terciam vel quartam aut quamcunque aliam partem penitencie indultam pro denario sequitur quod sit ita? Numquid oporteret quod previe subsit racio apud Deum? Ubi ergo est evidencia maioris racionis laxandi, est evidencia maioris potestatis ad hoc et econtra de irracionabilitate, ut repugnat prime racioni, per quam oportet omnes indulgencias fieri, quod hic sint infiniti puniti; quorum primus est aliqualiter capax venie secundum dignitatem habitam a Deo, secundus vero in duplo capacior et sic in infinitum, et tamen proporcionaliter ut fit maior elemosina pro magis capaci quoad Deum, habet ex taxacione pape minorem efficaciam ad peccatum vel penitenciam remittendum. Tales multe conclusiones impossibiles sequuntur ex potestate pape taxandi penas et peccata hominis suffragandi ad suum placitum et ex casibus calculatoriis quos ista scola habet admittere.

[ENGLISH]

## ¶2 · 574.23–574.32

> [p. 574] Tercio videtur quod subiacet potestati pape omnino absolvere tam vivos quem mortuos a pena et a culpa, et pono quod sint infiniti homines et infiniti denarii sive simul sive successive creati et adnichilati de Dei potencia absoluta, et iniungat papa primo illorum quod det primum denarium pro delenda prima parte penitencie Petri; secundo autem iniungat quod secundus det secundum denarium pro delenda secunda parte sue penitencie, et sic in infinitum. Et patet quod in fine foret tota penitencia Petri deleta.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 570.28: The power ascribed to the Pope is infinite.
- 571.8: He should use it freely or he is guilty of the death of those whom he might save.
- 572.7: with full use of his power he might restore the golden age.
- 572.21: If the Pope can excuse a part of penance he can excuse all.
- 573.18: To say that the remission must always be partial derogates from the divine power.
- 574.1: The Pope cannot assign arbitrary value to certain alms.
- 574.23: If each indulgence can remit a part, a succession must remit the whole.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 572: *tunc* [THIN]
  - 572: *forent* [R3]
  - 573: *sompniata* (margin letter N and 206a folio mark precede) [THIN]
  - 573: *populus* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 570:
li. B: hius. 27. B: obiecciones soluciones.

p. 571:
8. B in marg.: Quid sonat vcrbum lcgistarum, scilicet quod dominus
papa non remittit regulariter secundum partcm quantam sed quotam.
vid. pag. 752, I. 3o. i3. B: fratrcm dcest. 29. B: Et dic.
8. Cf. Hus, Opp. I, 184»

p. 572:
8. A A,: forent magna. i3. Quis ; codd . : quia. 17. approbando (?) ;
A B: app'ndo. 28. A B in marg. : Rcsponsio decretistarum.
3l. 32. Decreti sec. pars, causa XIII, q. II, cap. XXIII.

p. 573:
I. A: habcant. 2. A in marg. : Questio. iK. A in marg.
Rcsponsio quedam.

p. 574:
2. A A,: crederetur. 7. 8. B: prime subsit. 33. B: casus
sunt ymaginum.
```

---

## Chunk 23-i: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-i.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-i
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "574.33–576.2"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 9 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "285 words; 277 unanimous or majority-real; 3 settled by vote (R2 2, R3a 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n611–n613 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 9: [TITLE]

## ¶1 · 574.33–575.13

> [p. 574] Et si dicatur quod tales casus sunt ymaginarii solum possibiles de Dei potencia absoluta, revera sic potestas ficta de concessione indulgenciarum est [p. 575] imaginaria non colorabilis, nisi Deus specialiter assistat iuvando iuxta suam potenciam absolutam, et sibi foret facile dare potenciam vel subito vel successive laxandi peccata vel penam capacibus pro merito maiori vel minori; nec est viator cercior de uno quam reliquo, ut si Deus statuat quod per primam partem proporcionalem dati meriti remittatur prima pars proporcionalis pene date vel peccati, et per secundam secunda, et sic infinitum, tunc papa faciens isti conformiter ex sciencia et potestate sibi data posset absolvere quemcunque peccatorem a pena et culpa, et eque probabiliter posset unum fingi ut reliquum, cum toti isti materie deficit fundamentum.

[ENGLISH]

## ¶2 · 575.14–575.32

> [p. 575] Item, videtur quod quilibet sacerdos potest facere indulgencias, nam quilibet sacerdos habet parem potestatem ordinis cum quolibet et ipso existente in gracia habet potestatem super thesaurum ecclesie. Ergo cum aliter populo digno preest, videtur quod ipse et ex parte sui et ex dignitate potest eis aliquam indulgenciam impertiri. Nam quadraginta dies quos dat episcopus non limitant minimum gradum indulgencie, quare ergo non posset inferior curatus dare unus viginti dies et alius decem vel varie secundum quod Deus decreverit? Confirmatur primo ex hoc quod ante publicacionem huius materie habuerunt ecclesiastici potestatem ut modo, sed tunc non fuit racio, quare papa potest pro infinitum magno tempore indulgere; quicunque autem episcopus pro anno vel quadraginta diebus et non aliter; ergo nec modo subest racio quoad Deum, nec potest fundari racio huius variacionis nec est vicarius Petri istius potestatis ut generaliter sit dignus dicere:

[ENGLISH]

## ¶3 · 575.33–575.33

> [p. 575] Sic volo, sic iubeo; sit pro racione voluntas.

[ENGLISH]

## ¶4 · 576.1–576.1

> [p. 576] Non ergo sequitur: Ecclesia non decrevit tali curato licenciam

[ENGLISH]

## ¶5 · 576.2–576.2

> [p. 576] indulgendi, ergo non habet licenciam, quia tunc

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 575.1: Our cases are said to be fanciful, but all this papal power is a mere fancy.
- 575.14: Every priest should have power of indulgence.
- 575.25: Formerly the Pope did not claim this excessive power.
- 576.1: The power of absolution implies the power of indulgence.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 574: *ymaginarii* (P is a margin letter) [R4]
  - 575: *foret* [R3]
  - 575: *merito* [R3]
  - 575: *ut* (English side-note "claim" glued in other scans) [R4]
  - 576: *licenciam* (English "power" dropped; print: curato / licenciam indulgendi,) [INS?]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 574:
2. A A,: crederetur. 7. 8. B: prime subsit. 33. B: casus
sunt ymaginum.

p. 575:
10. B : possent. 33. B in marg. : Vcrsus. 33. Rectc: Hoc
volo, sic iubeo.
?4. luvenal. Sat. VI, 223.

p. 576:
3. B: ecclesiam. 17. B : iurediccionis. 22. Ad Rom. I, 14
Grecis ac Barbaris. 34. totum sacramentum.
```
