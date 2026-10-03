# Translation brief: ecclesia 23-j–23-l

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-23-j.md chunks/ecclesia/wyc-ecclesia-23-k.md chunks/ecclesia/wyc-ecclesia-23-l.md` once and fix what it reports.
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

## Glossary (the 216 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| descripcio | definition | Not "description" (T. p. 363). |
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
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| cataracta | trapdoor | "Floodgate" in a C note where the Genesis image is live. Ruled 2026-09-28. |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
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
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| acephala; incapitata | acephalous; unheaded | *Incapitata* pairs with *capitatus*. Ruled 2026-10-02 (*Eccl.* 18, 435.20–23). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| indulgere | to indulge | The etymology (*inde* + *algere*) turns on the verb. Ruled 2026-10-02 (*Eccl.* 23, 549). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| thesaurus ecclesie | treasury of the church | Ruled 2026-10-02 (*Eccl.* 23, 551.11). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| relaxare; relaxacio | to relax; relaxation | Ruled 2026-10-02 (*Eccl.* 23, 554.9). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| Romanus episcopus | the Roman bishop | Kept apart from *Romanus pontifex*. Ruled 2026-10-02 (*Eccl.* 23, 563.10). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| premium accidentale | accidental reward | Ruled 2026-10-02 (*Eccl.* 23, 565.6). |
| laxare | loose | Kept apart from *relaxare* "relax". Ruled 2026-10-02 (*Eccl.* 23, 571.29). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |

---

## Chunk 23-j: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-j.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-j
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "576.3–580.9"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 10 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1000 words; 958 unanimous or majority-real; 35 settled by vote (INS 2, R2 12, R3a 13, R3b 1, R5a 7); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n613–n617 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 10: [TITLE]

## ¶1 · 576.3–580.9

> [p. 576] nunquam incepisset ecclesia habere talem licenciam; similiter quilibet habens licenciam absolvendi habet licenciam commutandi penam temporalem pro pena perpetua quam confitens aliter supportaret, sed cum hoc sit indulgere, videtur quod quilibet sacerdos habet infinitam potenciam indulgendi. Non enim videtur racio quin in foro penitencie abscondito fiunt indulgencie, sicut fiunt extra in foro arbitrii per bullas publice proclamate. Nec est racio quin tantum valeant, cum fiunt utrimque devocius, humilius et legi Christi conformius; absolvens ergo preest ecclesie, et ad utilitatem ecclesie intendit efficaciter quod certa persona habeat remissionem grandis debiti pro parva satisfaccione. Sic enim potest diaconus, vel legatus secundum potestatem iurisdiccionis que est inferior potestate ordinis subditis indulgere. may Et ex istis tercio videtur quod quilibet de populo potest indulgere suo prelato, quia debita largissima sibi dimittere, et hoc est secundum modum loquendi scripture indulgere. Nam sicut apostolus dicit Rom. I, 14, quod Grecis vel Latinis est debitor, ita videtur quod dominus papa sit debitor ad serviendum et spiritualiter proficiendum cuilibet christiano, et illud debitum videtur eo maius quod Deus ad hoc obligat sub pena gravissima, et illud quod debetur foret preciosius debito corporali. Si igitur ille potest in debito isto deficere, et Christus docet Matthei VI, 12: Dimitte nobis debita nostra, sicut et nos dimittimus debitoribus nostris, videtur quod subditi possunt eciam pape copiosius indulgere. Ymmo videtur quod prelati maxime indigent indulgenciis laycorum, nec est indulgencia tantum sacramentum, quin laicis possit competere, [p. 577] quomodocunque fundabiliter terminus sit descriptus, quod laici possunt eis relaxare debitum spiritualiter ad utilitatem ecclesie, racione cuius relaxacionis Deus graciose coassistet, dimittendo peccatum et pene debitum, quod contingit Deum facere ad instanciam layci efficacius quam ad instanciam istius prelati qui blaspheme aut sacrilege vendicat aut vendit vel saltem pretendit se facere quod Deo non potest competere. Nam danti pecunias vel eis equivalens datur indulgencia quantumcunque laxa sive pro vivis sive pro mortuis quantumcunque incapacibus, sed egeno vel pauperi evangelice non dant indulgencias pro opere virtuoso, cum tamen quelibet virtus vel meritum sit infinitum prestancius quam totus thesaurus huius mundi et plus dignificat hominem ad habendum indulgencias quoad Deum, quia illa per se et alia solum per accidens. Item, videtur quod vel forma indulgenciarum est falsa vel indulgenti ambigua; nam indulgencie indifferenter conceduntur vivis et mortuis, sed sepe contingit quod non valeant illis vel non tantum valeant, eo quod sunt inhabiles quoad Deum. Ergo forma indulgenciarum sepe implicat falsum; et idem patet de impetrante indulgencias eciam plus quam centum millia annorum, quam largicionem vel oportet esse falsam vel diem iudicii adeo prorogari vel indulgencias valere in inferno post diem iudicii. Sed due posteriores partes sunt inopinabiles, ideo relinquitur prima pars, videlicet quod forma indulgenciarum sepe sit inutilis et falsa. Nec valet dicere quod subintelligende sunt condiciones capacitatis personarum quoad Deum pro quibus indultum est, quia talem promissionem posset quilibet de vulgo secure facere cuicunque, ut certum est quod omnis dampnatus habebit plenam remissionem [p. 578] si dignus fuerit et habilis ad tantam veniam quoad Deum, et aliter indubie propter concessionem Petri vicarii non habebit indulgencie plus vel minus. Ymmo videtur quod talis arroganter presumens dare tales indulgencias non sit procurator idoneus, ut ad sui peticionem Deus sit debitori magis propicius, quia in re concedit servus Dei, sepe sibi odibilis ex peccato quod Deus indulgebit suo affecto remittendo culpam et relaxando penam. Sed quomodo faceret Deus misericordiam ad tam luciferinam et tam infundabilem concessionem unius servi tam indigni? Revera melius foret quod vel doceret in hoc vicariam potestatem vel teneret se in limitibus sancti Petri. De Petro autem non plus sequitur: Quodcunque ligaveris super terram erit ligatum et in celo, ergo Petrus habuit potestatem ad taliter relaxandum penas tam in vivis quam mortuis in purgatorio vel dampnatis, quam sequitur: Christus dedit Petro illam potestatem ligandi et solvendi, ergo si Petrus voluisset insurgere contra Christum et membra sua, excommunicando eos et plene indulgendo membris dyaboli, ergo oportuit fuisse in celo apud Deum taliter diffinitum. Unde omnes fideles concedunt quod omnis potestas concessa Petro vel eius vicario limitata est quod humiliter et conformiter pareat Deo; ex cuius conformitate capit de tanto virtutem et ex eius deformitate capit tam prepositus quam subiectus seduccionem. Et hec racio quare Petrus et alii divinitus inspirati non magnificarunt potestatem suam ultra limites quos Deus instituit, sed precise ad tantum solverunt et ligarunt ad quantum docti sunt Deum solvere vel ligare. In ambiguis vero vel tacuerunt vel condicionem secundum quam oportet Deum principaliter [p. 579] solvere expresserunt. Unde sanctus Thomas conclusione secunda articuli tercii, d. XX, quarti libri movet dubium, utrum indulgencie tantum valent quantum pronunciantur, et arguendo ad partes recitat opinionem quadruplicem. Quarum prima dicit quod indulgencie non tantum valent quantum pronunciantur, sed ecclesia ad hoc ita pronunciat, ut quadam pia fraude homines ad beneficienciam et honorificenciam alliciat, sicut mater promittens false filio pomum vel aliud delectabile ad ambulandum provocat. Sed (ut dicit) periculosum est sic dicere, primo quia scola ista est patris mendacii, sed Job XIII°, 7 dicitur: Numquid Deus indiget mendacio vestro, ut pro eo loquamini? Item, sic dicens peccaret in se mortaliter et daret occasionem diffidendi de quocunque dicto vel facto prelati ecclesie. Nam Iª Corinth. XV°, 14 dicit Apostolus: Si inanis est predicacio nostra, inanis est et fides nostra. Talis autem falsum predicans dampnabiliter evacuat a se fidem. Et pro secunda parte beatus Augustinus epistola decima nona probat beato Jeronymo quod, si in scriptura sacra deprehenderetur aliquid falsitatis, robur auctoritatis scripture periret. Item, cum promittens donum spirituale magis obligatur ex promissione quam promissione corporalis pecunie, sequitur quod episcopus literatorie sic false promittens indulgencias obligat se ad solvendum thesaurum Deo. Caveat ergo episcopus de indiscreta et presumptuosa obligacione ad dandum thesaurum domini, quia hoc videtur magis dampnabile quam talentum Dei abscondere, [p. 580] quia sic false promittens superbe mentitur de Christo, cum Corinthiis dicit Apostolus: Si quid donavi in persona Christi. Quilibet ergo episcopus dicit in literis suarum indulgenciarum implicite quod Christus de thesauro domini tantum donat. Et patet ex dictis de mendacio quod non maior posset esse prelatorum defamacio vel ecclesie scandalizacio quam dicere quod in causa Dei ad seduccionem fidei populi prelati tam alti tam patule menciuntur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 576.19: The laity may give indulgence to the clergy.
- 577.5: God may pardon rather at the instance of a layman than of a wicked prelate.
- 577.31: If remission depends on worthiness, bulls are superfluous.
- 578.13: Even Peter could bind and loose only in accordance with Goa's will,
- 578.28: which he knew by divine inspiration.
- 579.1: St. Thomas enumerates four opinions as to the value of indulgences.
- 579.5: The first makes them a pious fraud,
- 579.12: and is to be rejected.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 576: *populo* (Q is a margin letter) [R4]
  - 576: *possit competere,* (main token covers two printed words; com- / petere, (top of p. 577, leaf zoom)) [THIN]
  - 577: *instanciam* (English side-note "at" glued) [R4]
  - 578: *Quodcunque* [R4]
  - 578: *solverunt* (30 is the line number) [R4]
  - 579: *Iª* [R4]
  - 579: *literatorie* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 576:
3. B: ecclesiam. 17. B : iurediccionis. 22. Ad Rom. I, 14
Grecis ac Barbaris. 34. totum sacramentum.

p. 577:
1?. 1'.: plus aignificat. 18 10. A: formn falsa vel.

p. 578:
26. B: et eius. 3o. solverant in codd.
i3. Cf. Hus. Adversus indulgencias papales Opp. I, fol.
CLXXXVl»

p. 579:
17. A B: Cor. XV. 2t. A in marg.: Augustinus ib. in codd.
epistola IX. Correxi. 28. A A, : thesaurum domini.
2. S. Thomae Summa theol. Supplem. tcrtiae partis, questio
XXVII. Opp. tom. VI, pag. 76. 21. Opp. Aug. tom. II,
pag. 190. Epistola LXXXII (alias XIX

p. 580:
V. quilibet; A: quilt. A, : qualiter. 21. penes; B pu'.
2. II Cor. II, i n: Si quid donavi, propter vos in persona Christi.
```

---

## Chunk 23-k: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-k.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-k
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "580.10–584.22"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 11 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1034 words; 977 unanimous or majority-real; 44 settled by vote (DEL 1, R2 20, R3a 17, R3b 1, R5a 4, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n617–n621 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 11: [TITLE]

## ¶1 · 580.10–584.22

> [p. 580] Ideo tres alie opiniones vere dicunt quod omnes indulgencie tantum valent quantum sunt rite promulgate. Sed una dicit quod valor earum attenditur penes fidem et devocionem indulti. Alia vero dicit quod valor indulgenciarum attenditur penes iustam estimacionem valoris rei date. Tercia autem dicit quod bonitas indulgencie cum predictis respicit causam pro qua datur indulgencia. Sed doctor dicit quod attenditur penes quantitatem meritorum ecclesie, que applicantur ad indulgenciam faciendum. Et sic oportet quod ex parte dantis sit auctoritas, ex parte recipientis caritas, et ex parte cause pietas, penes que omnia simul attenditur indulgencie quantitas, quia omnia ista respiciunt honorem Dei et utilitatem ecclesie. Et penes utrumque istorum attenditur valor indulgencie, et sic (ut dicit) nec per tales indulgencias peccatum remittitur nec pena remittitur, sed unius pena alteri commutatur. Sed contra ista dicta videtur primo quod non generaliter excusantur litere indulgenciarum a mendacio, quia sepe in causa et devocione omnino consimili, quantumcunque dispariter conceduntur indulgencie, ergo vel oportet concedere quod absolute valent indulgencie proporcionaliter ad intencionem concedentis, et sic mentiri [p. 581] non posset in istis ut Deus, vel aliter valor indulgenciarum non simul attenditur penes omnia ista tria, ymmo sepe, ubi causa est minus pia caritasque magis remissa, maior indulgencia est concessa; ut unus papa concedere posset indulgencias exercitantibus se in torneamentis, ubi alius papa prius excommunicavit omnes artem huiusmodi exercitantes. Nec oportet quod immineat sic varie necessitas ecclesiam Christi defendendi per gladium; patet factum in Extravagante Johannis XXIIⁱ Quia in futurorum eventibus. Item, videtur istam posicionem restringere potestatem pape in donando indulgencias, cum dacio dependet ex pietate cause et caritate persone cui sunt indulgencie conferende. Sed papa non regulariter rectificat istas causas sicut nec potest, ergo nec iustificat omnes suas indulgencias, et per consequens, ex timore excessus prodigi non foret tam laxus indulgencias concedendo. Non enim videtur racio quare Romanus pontifex posset concedere in generalibus indulgenciis centum millibus cuilibet septem annos, quin per idem uni persone tantum temporis simul, quia si noticia dignitatis requiritur, nunquam procederet talis indulgencia generalis. Ymmo videtur, cum merita triumphantis ecclesie sint connexa, quod omnia simul applicarentur ad penam tollendam, et specialiter meritum Christi in cuius virtute oportet alia operari; quod cum sit agens naturale, agit secundum ultimum sue potencie infinite; videtur quod tolleret generaliter omnem penam. Si dicitur quod Deus regulat, tunc stat quod papa indulgens non applicat, sed quod Deus ad rogatum unius laici egeni copiose penam dimittat. Item, si non dimittitur pena, sed commutatur (ut dicit sanctus doctor), tunc omnis pena que ante indulgencias [p. 582] foret debita est futura, quia data pena que non videtur, quod illa pena virtute indulgencie est dimissa. Ad istum enim sensum Deus dimittit penam, et per consequens, per indulgencias nec relaxatur pena nec alleviatur ille cui fit indulgencia. Nam si aliqua pena caret quam aliter haberet, tunc sibi dimitteretur illa pena, et cum pena individuatur a tempore et consistit in successione, videtur quod non est commutacio pene pro pena, tum quia quod non est non commutatur; pena autem pro qua fit indulgencia nec fuit nec est nec erit, et pena beati non est modo, nec potest subiectari in eo cui fit indulgencia. Videtur insuper, cum pena et peccatum sese inseparabiliter consequuntur, qui dimittit vel relaxat unum relaxat et reliquum, ut qui extinguit risibilitatem extinguit humanitatem; cum ergo papa extinguit penam extinguit et peccatum, quia aliter remaneret peccatum ineque punitum vel penitus inpunitum, vel aliter dans indulgenciam supplet satisfaccionem, quod non faceret nisi secundum racionem meriti, et sic oporteret omnem indulgentem esse in gracia, sicut oportet omnem cui facta est indulgencia quod leges impugnant. Alie autem sunt consideraciones de irracionabilitate legum multiplicatarum in ista materia, ut centum episcopi in dyocesi Petri non sufficiunt concedere Paulo de dyoecesi Petri nisi eosdem quadraginta dies quos Petrus diocesanus concedit, quia aliter (ut inquiunt) forent iurisdicciones permixte, et quilibet episcopus haberet potestatem super totalem ecclesiam sicut papa; sed Paulo vagante per illos centum episcopatus et deteriorato continue apud Deum accrescerent sibi de quadraginta diebus cum suis ratificacionibus quatuor millia dierum. [p. 583] Sed que racio (rogo) huius? vel que diversitas quod episcopus Nullatensis non sufficit concedere alicui indulgenciam quantumcunque digno apud Deum, episcopus autem dotatus sufficit concedere parem indulgenciam quantumcunque dispariter indispositis de sua dyocesi? Numquid talia dicta sonant quod indulgencia est pure ex arbitrio prepositi post dotacionem ecclesie adinventa et irracionabiliter ac fallaciter ad illusionem ecclesie sepe ficta? Et revera qui videntur defendere libertates, privilegia, honores ecclesie, ut amici, sunt ex adulacionis oleo inficiente mendacio et defensione fallaci in peccato diu abscondito eiusdem ecclesie nequissimi domestici inimici. Ideo premissa humili protestacione de ecclesie veneracione, de humili subieccione et de suarum libertatum constanti defensione dico primo quod nemo est capax indulgencie, nisi fuerit et de quanto fuerit dignus vel dispositus per graciam apud Deum. Patet ex hoc quod nemo si non Deus dat tales indulgencias qui non dat nisi caris suis quos sic prius habilitat. Dico secundo quod omnis recipiens tales indulgencias de tanto copiosius eas recipit, de quanto fuerit habilior quoad Deum. Patet ex hoc quod precise de tanto Deus dat sibi copiosius tales indulgencias, sed ipse facit quicquid facit ad regulam. Dico tercio quod nullius episcopi indulgencia prodest homini, nisi de quanto prius se disposuit apud Deum. Patet ex hoc quod Deus non dat sibi talem indulgenciam nisi ad tantum ex proposicione proxima, sed precise de tanto cuiuscunque episcopi indulgencia prodest. [p. 584] far Dico quarto quod episcopi indulgencia de tanto recipienti proderit, de quanto episcopus eum in fide Christi instruxerit, in devocionem et amorem Dei accenderit vel quomodocunque habilem ad indulgenciam Dei fecerit. Patet totum ex dictis. Dico quinto quod sacerdotes Christi non habent potestatem donandi indulgencias secundum quantitatem temporis, nisi eis specialiter fuerit revelatum. Patet ex illo morali Judith VIII°, 1: Posuistis vos tempus miseracionis domini, et in arbitrium vestrum diem constituistis ei. Ille ergo cui non fit ad hoc revelacio, qui spondet indigno apud Deum ex sibi dubio quod infra tantum tempus Deus miserebitur eius, donando sibi plenam remissionem, stulte pangit, cum non habet evidenciam quod Deus illud concesserit. Dico sexto quod ex fide scripture in qua est omnis veritas non fundabitur quod licet vicario Christi cui non fit ad hoc specialis revelacio, ut donet diurnas indulgencias vel annales. Patet ex hoc quod ex scriptura que non obviat sibi ipsi foret talis indulgencia temptacio Dei et seduccio populi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 580.10: The other three agree that their value depends on their being rightly given.
- 580.18: St. Thomas says that it depends on the amount of merit applied to them.
- 580.28: This does not account for different values arbitrarily assigned to indulgences.
- 581.18: The Pope's general indulgences cannot be given with regard to the capacity of the recipient.
- 582.1: If penalties are only commuted, they must still be to pay.
- 582.16: If the Pope destroys punishment, he must destroy sin.
- 582.23: Absurdities in the laws about indulgences.
- 583.14: Wyclif's final conclusions:
- 583.17: 1. God alone grants indulgences and only to those whom be has made worthy.
- 583.22: 2. Each receives according to his worthiness,
- 583.27: 3. No bishop's indulgence profits save as the recipient is worthy.
- 584.1: 4. And so far as the bishop's instruction has fitted him.
- 584.6: 5. Priests have no power to give indulgence for a specified time unless by revelation.
- 584.17: 6. Christ's vicar may not give indulgences of days or years.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 580: *∅* (ihree is the English side-note (The other three); Ideo already at pos 66) [INS?]
  - 580: *omnes* (T is a margin letter) [R4]
  - 580: *∅* (to is the English side-note (merit applied to); oportet already at pos 136) [INS?]
  - 581: *XXIIⁱ* [R3]
  - 581: *racio* [NW]
  - 582: *dyocesi* [NW]
  - 582: *diocesanus* [NW]
  - 583: *dyocesi?* [NW]
  - 584: *proderit,* [R3]
  - 584: *fide* (207c is the glued folio mark) [R4]
  - 584: *veritas* [R3]
  - 584: *vicario* [R3]
  - 584: *∅* (English side note (Christ's vicar)) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 580:
V. quilibet; A: quilt. A, : qualiter. 21. penes; B pu'.
2. II Cor. II, i n: Si quid donavi, propter vos in persona Christi.

p. 581:
2. penes; B pu'. 10. In codd. false: Equidem in futurorum
eventibus. Correxi. Vidc Iixtravag. Joann. XXII. tit. IX I)e Tornca-
mentis. 24. B: ecclesic couua. 29. Bi Si dicatur.

p. 582:
1. que: superfluum; recte: quia data pcna non videtur quod. 6. AA,:
quamalter. A in marg : aliter. 10. risibilitatem ; racionabilitatem (?)
ita codd. 17. A Bi extiguit. 28. 13: iurediccione- 3o. B:

p. 583:
[. B: rogo hoc. 2. cpiscopus Nullatensis, id est, episcopus qui
sedem episcopalem nonhabet. n. B: amici sint. 28. A A, : se deest.
16. Cf Hus adversus indulgcncias papales Opp. I, CLXXV'seqq.

p. 584:
io. In codd. : arbitrio vestro. Correxi e textu Iud. VIII, i3.
3o. Cleinentinarum lib. V, tit. IX, cap. II.
```

---

## Chunk 23-l: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-l.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-l
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "584.23–587.15"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 12 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "665 words; 638 unanimous or majority-real; 20 settled by vote (DEL 7, R2 3, R3a 7, R3b 1, R5a 1, R6a 1); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n621–n624 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 12: [TITLE]

## ¶1 · 584.23–586.17

> [p. 584] Dico septimo quod prelati ecclesie debent in ista veritate catholica subiectos instruere, ne laici infideliter occupati circa minus utilia attendant superbiam et avariciam sacerdotum? Patet in simili de lege questorum, quibus limitatum est quod non dicant populo nisi quod in literis episcoporum eis fuerit limitatum, ut patet libro septimo de Penitenciis et Remissionibus, capitulo Abusionibus. Multo magis ergo Christi vicarii debent docere populum secundum limites literarum spiritus sancti quas eis tradidit ad docendum. [p. 585] Dico octavo quod sacerdotes Christi, licet habeant potestatem ad absolvendum subditos a pena et culpa, non tamen debent absolvere sub hac forma nec subiecti illud expetere, nisi hoc eis specialiter fuerit revelatum. Prima pars patet ex hoc quod sacerdos potest sacramentaliter ostendere sibi confitentem taliter absolutum, qui ad tantum conteritur quod statim decedens sine pena purgatorii advolaret, et hoc est sacerdotem absolvere. Nec est potestas alicuius sacerdotis in casu ultime necessitatis sic ligata quin, quantum Deus revelans permiserit, possit absolvere; foret autem nimia presumpcio aliquem Christi vicarium absolucionem talem pretendere, nisi Deus hoc sibi revelaverit faciendum, ne forte incurrat blasphemum mendacium. Quid ergo valet subiectos inoportune absolucionem talem expetere, cum certe debent credere quod correspondenter ad sua merita vel demerita taxabuntur? Licet autem sufficiat apud Christum ubique presentem contricio, tamen sacramentum penitencie est valde necessarium, licet non proderit sine illa. Ideo foret stulticia sacerdotem cui non fit ad hoc revelacio diffinire quod penitencia vel aliud sacramentum suo suscipienti proderit ad salutem. Sic enim vetaret ut pro absoluto suo a pena et culpa in mortis articulo fieret suffragium ecclesie, sicut non facimus pro quocunque mortuo quem constat nobis iam esse beatum. Istam sentenciam de suffragiis et indulgenciis dixerim ad instruccionem inferiorum ecclesie, et exposicionem correccioni, supplecioni et approbacioni superiorum secundum regulas scripturarum et leges humanas ac decreta potentatuum precise ad tantum apprecior. Z Sed ad materiam de peccati purgacione quam tetigi in proximo argumento videtur mihi probabile quod quilibet purgandus tam diu habet peccatum [p. 586] in purgatorio, quam diu inibi subit penam. Nam sequitur: Hec est pena peccati, ergo est aliquid peccati, cum omnis pena sit res iusta per quam peccatum bonificatur, et per consequens illud peccatum est. Similiter, si quilibet in purgatorio purgatus est omnino sine peccato, tunc est ita mundus sicut beatus in celo, cum solum peccatum causat talem inmundiciam, et per consequens foret tam amabilis in purgatorio ab ecclesia triumphante, sicut ipso beato, quia tam pulcher. Similiter, quilibet existens in purgatorio propter peccatum suum preteritum deficit a plena dileccione Dei et ecclesie, ymmo a pleno profectu sibi et aliis quem debuit tunc habere. Ille ergo defectus purgandus est peccatum, ideo videtur penam purgare illum defectum et satisfacere pro defectu preterito, et quando lux amoris primo inducitur, tunc primo obscuritas peccati educitur.

[ENGLISH]

## ¶2 · 586.18–586.30

> [p. 586] Videtur ulterius quod pro quolibet peccato in quo decedit predestinatus Deus statuit certam penam, cum quo non poterit illo peccato supposito dispensare Nam per jdem posset dispensare cum quolibet peccato in purgatorio vel in inferno, et dimittere homini peccatum sine hoc quod voluerit converti ad dominum, sine amore faciendo ipsum beatum, cum nulla pena essencialiter consequeretur peccatum sed foret tantum per accidens arbitraria quoad Deum. Sicut ergo pena essencialis est per se iusta, sic est tanta iusticia in pena accidentali, sed meritum ecclesie facit esse aliud peccatum totale in purgatorio quam foret merito illo dimisso.

[ENGLISH]

## ¶3 · 586.31–587.15

> [p. 586] Videtur tercio quod sicut beati in celo merentur sibi continue usque ad diem iudicii premium accidentale, aliis autem utrumque, sed existentes in [p. 587] purgatorio merentur sibi premium utrumque continue, sic dampnati usque in finem continue demerentur. Prima pars videtur: Eo quod beati, sicut continue merentur aliis in via, sic merentur ut post habeant consorcium eorum in patria; purgati vero merentur sibi nedum remissionem peccaminum, sed beatitudinem tam essencialem quam accidentalem futuram, voluntarie gracia huius ex Dei gracia paciendo; licet autem peccent continue, quia tunc sunt in gracia sine mortali, non video quomodo proprie demerentur, sicut nec libere contradictorie tunc merentur. Dampnati vero cum sint peccato mortali in malivolencia sua continue peiorati, continue demerentur, licet prosint per accidens. De isto alibi. Explicit tractatus de sancta matre ecclesia.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 584.23: 7. The bishops should be careful to teach this to their flocks.
- 585.1: 8. Priests (unless by special revelation) ought not to give unconditional absolution.
- 585.18: The sacrament of penance is needful though useless without contrition.
- 586.1: Sin lasts as long as punishment.
- 586.18: For all sin there is an appointed punishment, with which God cannot dispense.
- 586.31: How the blessed gain reward for themselves and others,
- 587.1: and the souls in purgatory for themselves.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 586: *purgatorio,* [THIN]
  - 586: *bonificatur,* [NW]
  - 586: *Ille* [R3]
  - 586: *aliis* [NW]
  - 586: *in* [THIN]
  - 587: *finem* [NW]
  - 587: *peiorati,* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 584:
io. In codd. : arbitrio vestro. Correxi e textu Iud. VIII, i3.
3o. Cleinentinarum lib. V, tit. IX, cap. II.

p. 585:
18. B: autem afnciat. 33. B: inpurgacione.

p. 586:
1. A in marg. : Conclusio. 18. A in marg.: Conclusio. 21. B in
marg. : Apparet quod tcnet predcstinatum posse decedere in peccato.
23. B in marg. : Quam vocat penam essenci.ilem ct quam accidentalem ?
3i. A in marg.: Conclnsio.

p. 587:
9. A A,: quia tum. 14. B: licet profuit. i5. B : Explicit
A,: Continet viginti tria capilula et sic est finis.
```
