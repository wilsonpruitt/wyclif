# Translation brief: ecclesia 23-a–23-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-23-a.md chunks/ecclesia/wyc-ecclesia-23-b.md chunks/ecclesia/wyc-ecclesia-23-c.md` once and fix what it reports.
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

## Glossary (the 195 rows these chunks use; the full file is GLOSSARY.md)

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
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
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
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
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
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |

---

## Chunk 23-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "549.2–550.23"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 1 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "348 words; 326 unanimous or majority-real; 17 settled by vote (R2 9, R3a 5, R5a 3); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n586–n587 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 1: [TITLE]

## ¶1 · 549.2–550.23

> [p. 549] Restat consequenter tractare de indulgenciis et absolucionibus a pena et culpa, in quibus videtur esse error apud simplices istam materiam ignorantes. In primis ergo suppono significacionem quid nominis huius signi indulgencia. Est enim omnis indulgencia actus indulgentis, ita quod indulgencia non sit aliud nisi habentem ad hoc potenciam indulgere, et est indulgere gratis concedere, operam dare sive remittere, et componitur de inde et algere (quod est frigere vel mortificari), sicut est de commissis oblivioni traditis quoad expeticionem vindicte. Et sic loquitur scriptura Judith VIII°, 14: Indulgenciam domini cum lacrimis postulemus, et sic sumitur Isaie XXVI°, LXI° et LXIII°. Sic autem indulgere peccatoribus est Deo proprium, sicut et peccata dimittere (ut patet capitulo ultimo quinti libri); sed ab istis sensibus extractus est terminus et baptizatus in sensum alium partim per doctores theologie et partim per canonistas; quandoque enim secundum eos connotat remissionem pene, ut secunda questione tercio capitulo Indulgencie, ut notat Archidiaconus, quod quandoque signat active concessionem, ut dominus papa indulsit subdito hoc vel illud, id est, concessit; aliquando autem signat dispensacionem, aliquando ius, ut notat Johannes, XXXIII, q. IIª. Interfectores; et aliquando accipitur pro remittere vel condonare, in De Penitenciis [p. 550] et Remissionibus, cap. Indulgencie in princip per Archidiaconum; unde omnes istas indulgencias trahunt et limitant ad prelatos ecclesie. Unde statuunt sibi pro regula quod solus papa potest dare quoad locum et tempus indulgencias generales, episcopi autem habent potestatem limitatam faciendi indulgencias. Nam cum dedicant ecclesias, non extenditur eorum indulgencia ultra annum, eciamsi a pluribus episcopis dedicetur. In aliis autem ultra numerum quadraginta dierum non potest episcopus indulgere, verumptamen episcopus confirmatus antequam sit sacerdos, sicut et legati non sacerdotes faciunt indulgencias, quia hec potestas magis eis ex iurisdiccione quam ex ordine. Inferiores autem ut abbates et presbiteri non possunt indulgencias tales concedere publice ex auctoritate iurisdicionis, sed private in foro penitencie (ut patet in De Penitenciis et Remissionibus, capitulo Indulgencie); super vero conceduntur per Innocentem et Archidiaconum: licet, inquit, restricta sit potestas de indulgenciis que fiunt publice, non tamen in foro penitenciali in quo sacerdos potest indulgere annos et dies dummodo discrete faciat et penitenciam iniunctam per superiorem non remittat.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 549.2: Indulgence to sinners belongs to God alone.
- 549.15: The canonists have given it another sense: of remission of punishment.
- 550.1: Such indulgences are reserved to prelates under certain limitations.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 549: *CAP. XXIII.* [HEAD]
  - 549: *consequenter* [THIN]
  - 549: *Deo* (203c is the glued folio mark) [R3]
  - 549: *IIª* [R4]
  - 550: *∅* (previous page's closing text at page top) [INS?]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 549:
1. A: Cap. XXII. 2. A in marg. : De indulgcnciis (Below 2o3b
without mark of referencc). 5. B: signacionem. y. B in marg. :
Qiiid cst indulgcncia? 9. xo. B: remittere componitur. 18. B:
baptizatus deest. 20. B: convocat. ' 20. A: Nota quid est indulgere
vel indulgencia ; supra vide. 21. ut sec. q. III. cap. Indulgencie. Recte:
Sexti decretalium, lib. V, tit. X, cap. III. 25. 26. Johannes; sic in
codd. Legcndum: Nicolaus papa.
5. Cf. Hus, Opp. tom. I, 175". Losertli, Hus u. Wiclif, p. 209.
21. Sexti Decret., lib. V. De Penitenciis et Remissionibus, cap. III,
Glossa. 26. Decr. sec. pars, causa XXXIII, q. II, cap. V.

p. 550:
3. A in marg. " Indulgencia <~ paPe >3. potestas; A, in
marg. addit: convenit. 14. B: Inserentes autem. 14. B in
marg. : Potestas indulgendi est ex iurisdiccione et non cx ordine, ut hic
patet. 22. A: discreta. 24. A B in marg. : Nota quid sonat
(B: hoc): Remitto tibi tantum tempus indulgencie pro peccatis. 25. B:
Remitto tibi tempus.
```

---

## Chunk 23-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "550.24–554.22"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 2 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "805 words; 758 unanimous or majority-real; 38 settled by vote (R2 18, R3a 15, R3b 3, R5a 1, R6a 1); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n587–n591 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 2: [TITLE]

## ¶1 · 550.24–554.4

> [p. 550] Istis premissis restat videre expressius quid sonat verbum prelati: Remitto tibi tantum tempus indulgencie pro peccatis, et dicitur communiter quod virtute talis indulgencie per tantum tempus minus pacieris in purgatorio, et hoc intelligi potest dupliciter, vel quod indulgencia habeat efficaciam tantam, quantam tantum temporis pro penitencia huius vie quoad statum purgatorii, vel secundo quod de tanto [p. 551] brevius pacieris secundum penam purgatorii, et ista glossa est sentencie decretistarum pertinencior et dictis eorum conformior ut patet in De Penitenciis et Remissionibus; cap. Quod autem) in verbo, sed queres quid sonat? Sumitur autem fundamentum huius sentencie ex ista ymaginacione fantastica: Ponitur enim primo quod sunt supererogata merita sanctorum et specialiter Christi in celis infinita numero et valore, ultra quam requiritur ad eorum beatitudinem, et omnia ista vocantur spiritualis thesaurus ecclesie in capite eius reconditus. Ponitur secundo quod dominus papa, cum sit vicarius Christi in terris, habet plenam potestatem distribuendi thesaurum illum fidelibus, sed quod libuerit plus vel minus, nec licet diffidere quin potestas imperciendi ista spiritualia suffragia remaneat continue inexhausta, quia aliter deficeret Christus dando potestatem clavium suo vicario hic in terris. Tercio dicitur quod quando papa vel suus episcopus dispensat subditis de isto thesauro, commutando meritum beati loco meriti quo peccator mereretur remissionem peccati, tunc concedit indulgenciam plus vel minus. Et ex isto fundamento dicuntur hii vendere peccata sua et isti emere eciam pro pecunia et seductus est populus de cambio impossibili et infundabili propter fastum et questum adquisibilem sacerdoti. Et isti sentencie videtur sanctum Thomam annuere, super Quarto Sentenciarum, distinccione vicesima, questione [p. 552] tercia: Ab omnibus, inquit, conceditur indulgencias aliquid valere, quia impium esset dicere quod ecclesia aliquid vane faceret. Sed quidam dicunt quod non valent ad absolvendum a reatu pene quam quis in purgatorio secundum iudicium Dei meretur, sed valent ad solvendum ab obligacione qua sacerdos obligavit penitentem ad penam aliquam vel ad quam eciam ordinatur ex canonum statutis. Sed hec opinio non videtur vera; primo quia est expresse contra privilegium Petro datum, ut quod in terra remitteret et in celo remitteretur, unde remissio que fit quoad forum ecclesie, valet eciam quantum ad forum Dei. Item, ecclesia huiusmodi indulgenciam faciens magis dampnificaret quam adiuvaret, quia remitteret ad graviores penas, scilicet purgatorii, absolvendo a penitenciis iniunctis. Et manifeste patet deduccio, eo quod iuxta opinionem indulgencia non facit ad remissionem in purgatorio, sed subducta indulgencia in pleno penitencie faceret ad remissionem in purgatorio, quod foret infinitum prestancius quam aliqua penitencie vie remissio. Ideo iuxta hanc viam omnis indulgencia foret impeditiva fructus penitencie et nociva, ideo prudenter dicunt canoniste quod propter indulgencias non est dimittenda iniuncta penitencia [p. 553] pro peccato, nec haberent colorem indulgencie de multis millibus annorum quoad nudam mitigacionem penitencie hic pro via, cum certi sumus quod non subibitur eciam a Matussale tanta penitencia hic in via. Ideo, inquit doctor, aliter est dicendum quod valent indulgencie et quantum ad forum ecclesie et quantum ad iudicium Dei et quantum ad remissionem pene residue post contricionem, confessionem, absolucionem, sive sit iniuncta sive non. Racio autem quare valere possunt est unitas corporis mistici in qua multi in operibus penitencie supererogaverunt ad mensuram debitorum suorum et eciam multas tribulaciones iniuste sustinuerunt pacienter, per quas multitudo penarum poterat expiari, si eis deberetur. Quorum meritorum tanta est copia quod omnem penam debitam nunc viventibus excedunt et precipue propter meritum Christi; quod et si in sacramentis operatur, non tamen efficacia eius in sacramentis includitur, sed sua infinitate sacramentorum efficaciam excedit. Ideo cum unus pro alio satisfacere potest, sancti autem in quibus superhabundancia operum satisfaccionis invenitur, non determinate pro isto qui non remissionem indiget, huiusmodi opera fecerunt (quia alias absque omni indulgencia remissionem consequeretur) vel communiter fierent pro tota ecclesia, sicut apostolus dicit se implere ea que desunt passioni Christi in corpore suo pro ecclesia, ad quam scribit Corinth. I°. Et sic predicta merita quamvis sint communia tocius ecclesie, tamen papa distribuit ea dispariter, sicut ea que sunt communia alicuius multitudinis distribuuntur singulis de multitudine secundum arbitrium [p. 554] eius qui multitudini preest. Unde si quis consequeretur remissionem pene ac si alius pro eo satisfecisset ita quod satisfaccio alterius sibi per eum qui potest distribuatur; sic de indulgenciis est censendum.

[ENGLISH]

## ¶2 · 554.6–554.22

> [p. 554] Item, doctor Bonaventura super eadem distinccione, questione secunda, primo reprobat opinionem de indulgenciis dicentem quod tantum valent ad forum ecclesie militantis sic quod non ad forum ecclesie triumphantis. Si, inquit, prelatus relaxat et Deus non relaxat, tunc est pocius decepcio quam relaxacio, pocius crudelitas quam pietas. Et patet quod non foret dispensacio sed rebellio. Ideo ad excludendum ab ecclesia Christi fallaciam dicit quod indulgencia sic potest fieri: Obtinemus, inquit, bonum ex triplici merito, scilicet ex merito proprio, ex merito capitis et ex merito ecclesiastice unitatis. Et correspondenter ad istud triplex meritum bonum obtinendi est triplex meritum a malo liberandi, scilicet meritum proprium, ut puta, meritum contricionis, quo meremur liberari pena eterna et ascribi ad gaudia sempiterna, sic quod hec duo sunt simul, sicut in angelis gracia et gloria.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 550.24: So much time of indulgence may mean a) the equivalent of so much temporal penance; b) so much shortening of time in Purgatory.
- 551.1: The latter meaning is favoured by the decretists.
- 551.6: The opinion rests on an invention which supposes a) a store oft supererogatory merits;
- 551.13: b) that the store is inexhaustible and is at the disposal of the Pope;
- 551.20: c) that when the Pope makes over a share in such merit, he gives an indulgence,
- 552.1: St. Thomas says that indulgences are not simply remissions of temporal penance but avail in purgatory.
- 554.6: Bonaventura's opinion.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 550: *∅* (time is English side-note (So much time); Istis already at pos 158) [INS?]
  - 551: *Quod* [R3]
  - 551: *meritum* [R3]
  - 553: *pro* (203d is the glued folio mark) [THIN]
  - 553: *meritorum* (15 is the line number) [R4]
  - 553: *sua* [R3]
  - 553: *I°* (italic capital I, full height; period dropped per superscript rule) [R3]
  - 554: *eius* [THIN]
  - 551: *∅* (duplicate: glossa already present (tok pos 6 second entry)) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 550:
3. A in marg. " Indulgencia <~ paPe >3. potestas; A, in
marg. addit: convenit. 14. B: Inserentes autem. 14. B in
marg. : Potestas indulgendi est ex iurisdiccione et non cx ordine, ut hic
patet. 22. A: discreta. 24. A B in marg. : Nota quid sonat
(B: hoc): Remitto tibi tantum tempus indulgencie pro peccatis. 25. B:
Remitto tibi tempus.

p. 551:
i. B: Brevius paciens. 4. In verbo (?); in codd. A B: in v.
6. A in marg.: Fundamentum indulgenciarum secundum communem
opinionem. 9. A: numero et valere. 11. B in marg. : Spiritualis
thesaurus ecclesie. 14. A: in terra. 17. A: remaneant.
4. Decret. Greg. IX, lib. V, tit. XXXVIII, cap. IV. 3o. Thom.
Aq. Comment. in lib. IV. Sent. Opp. tom. IX, pag. 374.

p. 552:
1. indulgencias ; in codd.: indulgencia. Correxi. 2. B in marg. :
Sentencia sancti Thome et Bonaventure super materia indulgenciarum hec
est: Concipiunt aulem quod dominus papa ad votum suum potest distri-
buere et impertiri viatoribus de peccatis saltem suis conterentibus merita
Christi et suorum sanctorum, que vocant opera supererogata et thesaurum
ecclesie, sic quod potest illa merita loco meritorum rudorum (sic) ponere
ad remissionem peccati rudi, et quia illa merita excedunt omnem penam
viantibus debitam, ideo habent efficaciam delendi omne peccatum et
tollendi omnem penam debitam pro peccato magno. Ergo et mirabilis est
petentis (sic) dominus papa, qui potest hec merita taliter impertiri et gracia
illorum peccata remittere, penas tollere et ea loco plurimorum aliorum
commutare. Sed revera non video quomodo sanctorum communio tantum
dependet ex pape voto, cum magnam habuit illa communio efficaciam
ante adinvencionem istius distribucionis aut imperticionis papalis preas-
sumpte. 4. A in marg. : Opinio falsa. B: a reatu — solvcndum
deest. 6. B : ab deest. 8. A in marg. : Arguitur contra com-
munem opinionem indulgenciarum. 16. B: quod deduccio.

p. 553:
10. n. In textu s. Thomae: multi operibus. 23. huius in codd.
sic et in pluribus locis scqq. 25. A: niliil communiter. 27. A, :
II. Cor. I. 3l. A A,: singularia.
6. Thomae Aquinat super IV. Sent. I. c. pag. 374. 26. Ad
Coloss. I, 24.

p. 554:
6. B in marg.: Nota quomodo percipias teriam (sic) indulgenciarum
secundum fautores earum. Numerus distinccionis deest in codd. i5. A in
marg.: Bonum obtinemus ex merito proprio, ex merito capitis, ex merito
ecclesie unitatis. 17. A in marg.: Bonaventura de indulgenciis (Below
2o3d without mark of reference).
10. Lib. IV. Sentenciarum dist. XX, pars II, art. I, quaestio II.
Conclusio. Sancti Bonaventurae Opp. tom. IV, pag. 556 (ed.
Ven. 1734).
```

---

## Chunk 23-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-23-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-23-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "554.23–558.23"
divisions: "cap. 23 (heading 'CAP. XXIII.' at 549.1); part 3 of 12, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "896 words; 821 unanimous or majority-real; 67 settled by vote (INS 4, R2 36, R3a 24, R3b 1, R5a 2); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n591–n595 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 23, part 3: [TITLE]

## ¶1 · 554.23–555.15

> [p. 554] Secundo modo meritum Christi cooperatur in sacramentis et potestate clavium, et per hoc remittitur pars pene. Et tercio modo fit meritum ad fugiendum malum ex vi unitatis ecclesiastice. Et correspondenter fit triplex pene condonacio, ut sic currat misericordia cum iusticia. Et in qualibet tali condonacione est commutacio maioris in minus, unde pena eterna primo [p. 555] mutatur in temporalem in remissione pene et culpe. Secundo pena temporalis magna et supra vires mutatur in penam viribus competentem in sacerdotis absolucione. Tercio vero commutatur pena ad quam pertinet iudicio ecclesie in minorem relaxacionem in virtute residui meritorum ecclesie. Et omnia ista originantur ex merito passionis et satisfaccionis Christi, nullibi preiudicando iusticie. Et ita dicit quod indulgencie fiunt de meritis supererogacionis membrorum ecclesie, quem thesaurum pertinet ad solos episcopos saltem publice dispensare, quia illi sunt vicarii succedentes in loco Christi fratris senioris mortui, ut suscitent semen suum generando sibi filios spirituales. Et uterque istorum doctorum respondet ad obiectus in contrarium.

[ENGLISH]

## ¶2 · 555.16–556.4

> [p. 555] Et illam sentenciam sepe inculcant doctores decretorum ponentes quod indulgencia est liberalis et graciosa donacio de thesauro ecclesie, facta per vicarium Christi peccatoribus pro suis penis ad quas de iusticia obligantur. Thesaurus iste, inquiunt, est habundancia meritorum que multi sancti ultra mensuram debitorum erogaverunt et tribulaciones quas iniuste sustinuerunt; quorum meritorum tanta est copia quod excedit omnem penam debitam viventibus, et precipue passio et meritum Christi, cuius minima gutta sanguinis vel sudoris sufficeret ad expiacionem omnium peccatorum, hec et cetera bona supererogat, que omnia ponuntur in scrinio pectoris Christi tamquam thesaurus ecclesie. Ista sentencia patet per Willielmum in De Reliquiis et Veneracione Sanctorum, capitulo V°. Et patet [p. 556] quomodo a theologis decretiste sumpserunt istam sentenciam que, si sit infundabilis et principium erroris fidelium, patet gravedo peccati in auctoribus illius ficticie.

[ENGLISH]

## ¶3 · 556.5–556.8

> [p. 556] In ista materia sic procedam: Primo fundabo vel colorabo possibilitatem et probabilitatem illius sentencie, secundo obiciam multipliciter contra illam et tercio dicam quid videtur mihi probabiliter sustinendum.

[ENGLISH]

## ¶4 · 556.9–556.21

> [p. 556] Quantum ad primum sic arguo: Deus nedum potest de sua absoluta potestate quecunque peccata eciam sine satisfaccione remittere, sed unus potest de communi cursu pro alio satisfacere, et per consequens, Deus potest committere suo vicario potenciam contra quecunque peccata taliter dispensandi. Quo habito suadetur tripliciter quod sic facit, primo quia caput ecclesie pro quo Christus oravit Luce XXII°, 32, ut non deficiat fides sua, sic pretendit se facere de facto; sed foret error intollerabilis si in isto a fide exorbitet, sicut maxime dampnabilis fatuitas foret membris ecclesie hoc sibi imponere, ergo presumendum est factum istud esse catholicum.

[ENGLISH]

## ¶5 · 556.22–556.29

> [p. 556] Item, Matthei XVI°, 19 concessit Christus Petro et cuilibet eius vicario singulariter plenitudinem potestatis dicens: Quodcunque ligaveris super terram erit ligatum et in celis, et quodcunque solveris super terram erit solutum et in celis. Cum ergo dominus papa sic solvit et ligat in terris, videtur ex evangelio quod proporcionaliter fit in celis; aliter enim titubaret fides ecclesie.

[ENGLISH]

## ¶6 · 556.30–557.2

> [p. 556] Item, Deus reliquit unum caput in ecclesia pro dubiis decidendis, quod non potest poni nisi Petri vicarius; ergo sibi restat difficultatem istam decidere; sed cum factum suum sit manifestissimus interpres sensus sui, videtur quod in facto docet hoc esse [p. 557] catholicum. Quis rogo iudicaret papam cum conventu suo errare?

[ENGLISH]

## ¶7 · 557.3–557.32

> [p. 557] Assumptum ergo primi argumenti sic docetur: Oportet ex fide credere quod Christus satisfecit pro omnibus membris suis, sicut ex vi communionis sanctorum quodlibet membrum ecclesie satisfecit pro altero, cum apostolus dicat Gallatis VI°, 2°: Alter alterius onera portate; ergo per idem contingit ecclesiam beatam satisfacere pro viante. Item, contingit unum condempnare alterum, ut patet de primis parentibus et multis aliis ex suis capitibus et consociis accusatis. Cum ergo Deus sit pronior ad premiandum quam puniendum, videtur quod contingit unum satisfacere pro alio. Sic enim brachium naturaliter se exponit pro capite; multo magis in corpore Christi mistico, ubi est ligatum forcius, videtur quod unum membrum debet satisfaciendo supportare pondus alterius iuxta istud Apostoli IIª Corinth. XI°, 29: Quis infirmatur et ego non infirmor? Item, Deus est liberior ad recipiendum satisfaccionem de suis debitoribus quam servus suus de debitoribus suis, sed homo sepe racionabiliter recipit debitum unius per puram satisfaccionem alterius, ergo contingit Deum liberrimum hoc facere. Si ergo creditor benigne accipit talentum debitum a Petro ex pura satisfaccione Pauli hoc solventis pro eo, multo magis Deus misericors. Si ergo unus in gracia impetrat alteri remissionem culpe, quod maius est, ipse evidencius potest impetrare sibi remissionem pene, quod minus est. Pia ergo consolativa fidelium et honorificativa cleri est ista posicio.

[ENGLISH]

## ¶8 · 557.33–558.21

> [p. 557] Primo ergo concedenda est ista conclusio quod contingit unum satisfacere pro alio. Sed notandum [p. 558] ofquod hoc intelligi potest tripliciter, primo participative satisfacien do pro suo contento, secundo iuvative concausando totam satisfaccionem in omnino altero et tercio per se sine concursu alterius satisfaciendo pro toto debito. Exemplum primi est in assumpcione nature humane per Christum in attomo et complecione primiciarum tocius debiti humani generis pro peccato. Exemplum secundi est quomodo nedum Christus sed alia membra iuvant ad plenam satisfaccionem confratrum; et tercio modo unus satisfacit pro debito particulari alterius particulari creditori. In utraque primarum satisfaccionum oportet debitorem concurrere, ut quamvis Christus fecit se naturam humanam que debuit Deo satisfaccionem pro peccato primi hominis, tamen illa satisfaccio non potuit membris proficere, nisi ex adiutorio capitis se disponentibus active ad suscipiendum medicinam vel saltem ad consolvendum ministracionem debitam, in tantum quod infans unius diei decedens in gracia primo baptizatur flamine, secundo servit Deo meritorie et sic tercio participat fructum celestis medicine.

[ENGLISH]

## ¶9 · 558.22–558.22

> [p. 558] Et patet ad primum quod concedenda est conclusio, sed

[ENGLISH]

## ¶10 · 558.23–558.23

> [p. 558] non credamus quod Christus satisfecit pro debito illius

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 555.1: The commutation of punishment is due to the satisfaction made by Christ.
- 555.9: Indulgences are to be dispensed only by bishops.
- 555.18: Other decretists maintain this opinion of a treasure doled out by Christ's vicar.
- 556.5: I propose to give 1. Arguments in its favour; 2. Arguments against it; 3. My own judgment.
- 556.9: 3, My own judgment.
- 556.11: In its favour:
- 556.13: a) One man may make satisfaction for another.
- 556.22: b) Christ gave to Peter full power of binding and loosing.
- 556.30: c) The Pope's acts shew that he declares it catholic.
- 557.3: We believe that Christ made satisfaction for all his members.
- 557.10: Since one man's sin may hurt another, one may atone for another.
- 557.21: Even men let one man acquit another's debt, much more will God
- 558.1: Three kinds of satisfaction: 1. Where one does his separate share. 2. Where one helps another to do his part. 3. Where one satisfies entirely for another.
- 558.22: Christ made satisfaction, but to the profit only of those who join in his work.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 555: *pertinet* (5 is the line number) [R4]
  - 556: *a* [THIN]
  - 556: *et* (b is a margin letter) [R4]
  - 557: *IIª* [R4]
  - 557: *ipse* (30 is the line number) [R4]
  - 557: *notandum* [THIN]
  - 555: *habundancia* (italic; out is English side-note) [OVERRIDE-MARK]
  - 557: *portate;* (italic) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 554:
6. B in marg.: Nota quomodo percipias teriam (sic) indulgenciarum
secundum fautores earum. Numerus distinccionis deest in codd. i5. A in
marg.: Bonum obtinemus ex merito proprio, ex merito capitis, ex merito
ecclesie unitatis. 17. A in marg.: Bonaventura de indulgenciis (Below
2o3d without mark of reference).
10. Lib. IV. Sentenciarum dist. XX, pars II, art. I, quaestio II.
Conclusio. Sancti Bonaventurae Opp. tom. IV, pag. 556 (ed.
Ven. 1734).

p. 555:
4. commutatur ; in codd.: commutacio; Fortasse legendum: commu-
tacio pene. 16. B in marg.: Indulgencia quid sit. 20. B in
marg. : Thesaurus ecclesie. 27. supererogata in codd.
8. Dist. XX, pars II, quaest. III (pag. 558). 29. An Wilhelmus
Autissidorensis, W. de Montc Laudano, Durantis, de St. Amore,
alterve, non video.

p. 556:
5. A in marg.: Arguitur pro possibilitate indulgenciarum. 9. A m
marg. : Racio. 10. B: absolutus. 17. sic; sicut(>).

p. 557:
10. B : contingir c. i3. A : quam ad ; ad extinctum cst. 32. A in
marg. : Responsio conclusio. 33. A in marg. : Quomodo contingit
unum satisfacere pro alio. Conclusio conccdenda.

p. 558:
2. contento; in codd. A: co"> (cotitato? cf. partem cotam p. 5io, 1- 6);
B: to">. 3. B: totalem satisfaccionem. 4- B inmarg.: Satisfaocio
pro alio tripliciter fit. 6. B in marg.: Christus assumpsit naturam
nostramin athomo. io. confratrum; B: consivium (src). 18. B m
marg.: Apparet quod si infans discedens absque baptismo flamims admdi-
cabitur eternc pene propter culpam primorum parenfum ipso in persona
propria non demerente: pcr idem posset bcatus pro pcccantc satisfacere
peccatore, pro commisso nullatenus satisfacicnte. 25. In codd. LXXXl.
```
