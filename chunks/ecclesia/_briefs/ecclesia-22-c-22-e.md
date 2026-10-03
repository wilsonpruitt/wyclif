# Translation brief: ecclesia 22-c–22-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-22-c.md chunks/ecclesia/wyc-ecclesia-22-d.md chunks/ecclesia/wyc-ecclesia-22-e.md` once and fix what it reports.
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
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

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
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
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
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| forisfactura | forfeiture | Noun beside *forisfacere* "forfeit". Ruled 2026-10-02 (*Eccl.* 15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| cantaria | chantry | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| acephala; incapitata | acephalous; unheaded | *Incapitata* pairs with *capitatus*. Ruled 2026-10-02 (*Eccl.* 18, 435.20–23). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| habilis / habilitas | qualified / qualification | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |

---

## Chunk 22-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "524.18–528.17"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "959 words; 894 unanimous or majority-real; 52 settled by vote (R2 28, R3a 15, R3b 2, R5a 6, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n561–n565 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 3: [TITLE]

## ¶1 · 524.18–526.31

> [p. 524] Item, Augustinus XXI° De Civitate Dei, capitulo XXIV°, tractans istam eandem materiam ponit primo evidencias discipulorum Origenis arguencium si ex precepto domini homines debent in via diligere et orare pro inimicis (ut patet Mathei V°): multo magis beati in maiori caritate plus exaudibiles orabant pro illis continue, et per consequens oportet quod sint finaliter exauditi. Unde totam scripturam de dampnacione perpetua glossant quod homines digni sunt pati talia, si non assit Dei misericordia, non (inquiunt) quod passuri sunt talia, sed sicut nemo sane fidei hoc dixit, sic nec dicturus est. Alioquin, inquit, nulla foret nunc causa, cur non eciam nunc pro dyabolo [p. 525] et angelis eius oret ecclesia. Hec ergo causa qua fit ut nunc ecclesia non oret pro malis angelis quos suos novit esse inimicos; eadem ipsa causa est qua fiet ut in illo tunc iudicio eciam pro hominibus eterno igni cruciandis, quamvis homo perfecta sit sanctitate, non oret. Nunc enim propterea pro eis orat quos in genere humano habet inimicos, quia tempus est penitencie fructuose. Unde orat (sicut dicit Apostolus), ut Deus det illis penitenciam et resipiscant de dyaboli laqueis a quo captivi tenentur secundum ipsius voluntatem. Denique, inquit, de aliquibus ita certa esset, ut qui sint illi nosset, qui licet in hac vita constituti sunt, tamen predestinati ire in ignem eternum cum dyabolo; tam pro eis non oraret quam nec pro ipso. Ex istis patet quod nemo oraret pro illo specialiter quem scit perpetualiter ante tempus oracionis esse dampnatum perpetuo. Item, beatus Gregorius XXXIV° Moralium capitulo— dicit eandem sentenciam cum Augustino: Ubi est, inquiunt, quod sunt sancti, si pro inimicis suis quos ardere viderint non orabunt. Sed respondemus: Orant pro inimicis suis eo tempore quo possunt ad fructuosam penitenciam eorum corda convertere. Sed quomodo tunc pro illis orabitur, quando iam non possunt ab iniquitate ad iusticie opera conmutari? Eadem itaque causa est, cur tunc non oretur pro hominibus istis dampnatis, que causa est nunc ut non oretur pro ipso dyabolo. Et multa similia ibi infert. Racio autem omnium istorum sanctorum doctorum stat in isto: Nemo debet orare Deum specialiter pro [p. 526] aliquo impetrando, quod scit tunc fore irracionabile Deum sibi concedere et impossibile sibi ipsum adquirere, sed sic foret de quolibet scienter orante pro beatificacione hominis quem scit Deum ad dampnacionem perpetuam ordinasse; ergo conclusio. Minor patet ex hoc quod orans nedum sciret oracionem huiusmodi fore frustra, sed foret scienter contrarius voluntati divine, et per consequens ineptus ad dicendum ex animo oracionem quam Christus docuit Matthei VI°, 10: Fiat voluntas tua in celo et in terra. Quomodo queso subicit ipse humiliter voluntatem suam voluntati divine qui videt clare quod sit pulchrum et utile ut sic fiat ex ordinacione divina, et oppositum foret dampnosum et turpe, et tamen instat ut Deus faciat illud quod de facto foret irracionabile. Nam proinde foret ac si rogaret Deum mutare suum propositum et ordinacionem eternam vel meliorare mundum in infinitum ultra quam decrevit, vel orare ut Deus non permittat aliquod malum fieri quod iam est preteritum. Sed Petrus Matthei XVI°, 23 propter talem adversam peticionem vocatus est Sathanas ab illo qui Johannis XVII°, 9 dicit: Non pro mundo rogo (hoc est, pro prescitis quorum dampnacio est cum mundo), et a quo Johannes dicit: Est peccatum ad mortem, non pro eo dico, ut roget quis, Iª Johannis ultimo 16. Et hec racio, quare beati non rogant nisi pro dignis quos intuentur Deum velle iuvare; aliter enim forent miserrimi vel languide a peticione sua frustrati, vel aliter orarent frustra contra voluntatem suam pro illo quod de appetunt; quod foret in eis magna duplicitas.

[ENGLISH]

## ¶2 · 526.32–528.17

> [p. 526] Ideo patet quod quidquid fidelis rite oraverit effectualiter ad hoc tendit quod Deus faciat in omnibus illud quod sibi videbitur expedire. Et sic omnes [p. 527] G2oo°debite oraciones sunt realiter graciarum acciones quibus confitentes inmensitatem sue misericordis benevolencie dicimus: Fiat voluntas tua undique. Nec aliud licet nobis petere nisi si et quatenus tibi placuerit. Et hec racio, quare bona vita est optima oracio; Deus enim non potest expergisci vel precibus nostris flecti, ideo necessarium est orare pro vivis et mortuis, ut ex caritate mereamur nobis ipsis et dignificemur communicare meritum nostrum aliis. Deus autem distribuit secundum capacitatem eorum et non secundum limitacionem nostram, cum sepe oratur pro mortuis non ex hoc suffragium participantibus sed punitis, ut patet de multis prepositis ecclesie legem sacerdotum vetantibus, sicut innuit decretum, XXIª, q. IIIa, Ciprianus, ubi sic dicitur: Si hoc fecisset quis, non oretur pro eo, nec sacrificium pro dormicione eius celebretur. Neque enim ante altare Dei merentur nominari in sacerdotum prece qui ab altari sacerdotes et ministros volunt advocare. Nec valet glossa dicens: hoc esse dictum tantummodo ad terrorem, quia sic diceretur ad omnem legem que in penam sonuerit. Ideo caveant episcopi et domini qui vel omissione correpcionis vel commissione continuacionis trahunt sacerdotes a vita clericali ad seculum, cum decedentes sine satisfaccione non debent redimi, eciamsi habuerint quotlibet cantarias, dicente decreto Jeronymi XIIª, q. IIª, In presenti seculo: Cum, inquit, ante tribunal Christi venerimus, nec Job nec Daniel nec Noe rogare posse pro quoquam sed unumquemque oportet portare onus suum. [p. 528] Sed ut clarius pateant sanctorum sentencie in parte, obicitur multipliciter quod orandum est specialiter pro dampnatis. Primo quia orandum est pro istis viventibus prescitis, sive sint amici in gracia secundum presentem iusticiam sive inimici secundum iniusticiam presentem dampnabiles. Cum ergo illi pro suo tempore sunt dampnati, videtur quod oportet orare pro dampnatis, eciam licet scitur eos esse tales, tum quia orans scit omnia in communi, tum eciam quia scit in particulari pro suo tempore quod prescitus huiusmodi est dampnatus. Sed illud sophisma non solvit difficultatem qua queritur utrum viator orans pro mortuis debet pro eodem tempore orare pro dampnato pro quo tempore scit particulariter et distincte quod ille tunc sit dampnatus ad penam perpetuam. Et contra hoc vadunt raciones et sophisticantur evidencie ad eiusdem oppositum colorandum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 524.18: Augustine asks if we are to pray for the damned, why not for the devil?
- 526.1: We ought not to pray for what we know God will not grant.
- 526.32: All right prayers are for the fulfilment of God's will,
- 527.1: and are really thanksgivings.
- 527.10: God distributes our suffrages as he sees fit.
- 528.1: We pray for the foreknown while alive, but this is quite different from praying for the damned.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 524: *∅* (asks is the English side-note; Item, already present at pos 132) [INS?]
  - 524: *assit* [NW]
  - 524: *dyabolo* (coordinator: print has dyabolo whole at line end; every scan truncated (agent 12)) [NW]
  - 525: *fit* [R3]
  - 526: *foret* [R3]
  - 526: *Iª* [R3]
  - 526: *illud* [R3]
  - 527: *tua* [R3]
  - 527: *placuerit.* (5 is the line number) [R4]
  - 527: *XXIª* [R4]
  - 527: *XIIª* [R3]
  - 527: *IIª* [R4]
  - 528: *in* (200d folio mark and margin letter G glued) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 524:
2. In codd.: tale in quid. 3. In codd.: glossa. Est evidens.
Correxi e textu glossae (Pro impiis) ad caus. XIII, q. II. Pro obeuntibus.
ibid.: suspendat. Correxi e textu glossae. Vide Decretum Gratiani una cum
glossis (Venet. iCo5) pag. 97! 18. A in marg.: Argumentum pro
salvacione omnium. 18. In codd.: XXII de civitate Dei cap. XXIII.
23. In codd.: orabat.
18. Aug. Opp. tom. VII, pag. 641, 642.

p. 525:
18. A in marg. : Gregorius. 18. capitulo; sequitur lacuna in codd.
19. B: quod — suis decst. 24. In codd.: qui iam non. Corrcxi c
tcxtu b. Greg. 29. A in marg. : Racio. Non cst orandum pro
dampnatis pcrpetuc, modicum supra vidc (Abovc 2ooc witliout mark of
refcrcncc).
11. II. Timotli. II, 26. 18. Gregoiii Moral. XXXIV,
cap. XIX [vet. XIII] in cap. XLI. b. Job. Opp. tom. I, pag. n 33.

p. 526:
o. A A,s dicendum quod animo. 22. zUB: Johannes didicit.
3i. de appetunt; Verbum excidisse videtur.

p. 527:
ii. B: nam nostram. 16. In decretali: non offeretur. 19. Bi
volunt avocare. 2G. A A,: etsi habuerint. A in marg. : Arguitur
quod orandum est pro dampnatis et dissolvitur. 29. B rogare
posset.
i5. Dec. sec. pars, causa XXI, q. III, c. IV. 27. ib.
causa XIII, q. II, cap. XX.

p. 528:
2. A in marg.: Obiectus. 10. A A,: scit impertiri. 12. B:
salutat solvit; A: salutat correxit in solvit ; A, : salutat. 28. morientis.
Conieci. A: iam mori. I.ocus rasura corruptus. H : utor iam mori.
A,: vita sine moritis. 3o. B: ergo orare.
```

---

## Chunk 22-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "528.18–532.20"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1015 words; 934 unanimous or majority-real; 68 settled by vote (INS 1, R2 44, R3a 15, R3b 4, R5a 3, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n565–n569 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 4: [TITLE]

## ¶1 · 528.18–530.1

> [p. 528] Sed secundo arguitur quod oportet orare pro dampnatis perpetuo, quia de dampnatis temporaliter ad penam purgatorii non dubium quin debemus pro eis specialiter exorare, nam debemus orare pro omnibus christianis conviventibus nobiscum, et multi eorum sunt dampnati perpetuo quoad Deum; ergo conclusio. Aliter enim nullus oraret pro aliquo fratre suo, cum ignorat utrum sit predestinatus vel prescitus. Et eadem est consideracio de defunctis. Nam recepcio sacramentorum, manifestacio signorum et testificacio astancium in fine vite iam morientis, non faciunt nisi levem evidenciam topicam quod decessit in gracia. Quomodo ergo orarent sacerdotes annales pro suis mortuis vel religiosi possessionati pro suis patronis, si non liceret orare pro dampnatis? Unde Augustinus, XXI° De Civitate Dei, capit. XXIII° [p. 529] (ubi supra) sic loquitur: Quia ecclesia de nullo certa est, orat pro omnibus; sic enim orat in die Parasceues pro perfidis Iudeis, paganis et aliis cunctis barbaris. Hic dico supponendo sensum proximo limitatum quod trimembris est distinccio oracionis ad propositum. Alia enim est oracio confusa et alia distincta, quod oportet mensurare penes suum primum subiectum, vel secundarium pro quo oratur; ut orando distincte pro cunctis animabus in purgatorio oratur confuse pro Petro vel alio inibi ignorato; et sic dicunt logici quod eadem oracio est respectu diversorum simul confusa et distincta. Secunda distinccio oracionis est quod alia est absoluta et alia condicionata. Absoluta qua beati petunt illud quod intuentur in verbo esse ab eis petendum et a domino concedendum, nam sic Christus et angeli necessitati sunt petere pro membris Christi viantibus et sunt regulariter exauditi. Oracio autem condicionata est oracio qua nos ignari petimus quod reputamus esse nobis utile subintelligendo condicionem, si Deo placeat. Tercia distinccio oracionis capitur penes illud pro quo oratur, ut alia est oracio pro beatitudine et alia oracio pro bono aliquo citra ipsam, sive fuerit perpetuum, sicut est remissio pene eterne, sive bonum aliquod temporale; sed oracio pro homine quoad Deum sumitur communiter pro primo membro famosiori. Istis premissis dico quod orare debemus isto ultimo modo pro prescitis nobiscum conviventibus, intendendo illis bonum in communi, quod secundum illum modum ultimum contingit nos eis mereri, cum contingit nos inorare eorum demeritum et, sic quoad eos nec nostra racio nec nostra correpcio foret cassa; verum tamen scito a nobis distincte ante oracionem quod forent [p. 530] knewtunc mortui eternis ignibus deputati cessaret pro tunc

[ENGLISH]

## ¶2 · 530.2–532.20

> [p. 530] efficacia deprecandi, et ita, sicut ignoramus qualiter oremus pro vivis ex ignorancia qualitatis sui exitus, sic ignoramus qualiter oremus pro iam mortuis propter ignoranciam conformem. Ideo optimum est nobis sacerdotibus vivendo sancte porrigere Deo oraciones generales et condicionales pro nostris benefactoribus, quia tales ex maiori caritate plus eis proderunt si capaces fuerint (ut patet in De Consecratione d. Vª Non mediocriter); et supposita eorum incapacitate plus proderunt ecclesie et oranti. Nec est licitum orare pro vivis vel mortuis, specialiter condicione orandi exposita pretermissa. Ille ergo qui orat specialiter absolute pro beatificacione patroni sui iam mortui cum hoc quod iam revelatum sit sibi ipsum iam eternis ignibus mancipari, et hoc propter cupidinem temporalium, debet eis privari tamquam orator inutilis, cum debet congaudere cum Deo et beatis in celo de iusto Dei iudicio et materiali gaudio beatorum, eciamsi fuerit alter parentum carnalium vel specialissimus amicorum, quia, sicut non rogamus Deum ut revocet tempus preteritum, sic nec rogamus eum ut revocet tale iudicium. Et quantum ad dictum Augustini, patet quod intelligitur ecclesiam rite orare pro omnibus capacibus, de quanto sunt tales. Unde iste textus suus orat pro omnibus dumtaxat hominibus, inimicis suis in hoc corpore constitutis, nec tamen pro omnibus exauditur; pro hiis enim solis exauditur qui etsi adversantur ecclesie, ita sunt tamen predestinati ut filii efficiantur ecclesie. Si qui autem usque ad mortem habebunt cor impenitens nec ex inimicis convertentur in filios, non pro talium defunctorum spiritibus orat ecclesia, quia in parte iam diaboli [p. 531] computatur, qui cum esset in corpore non est translatus ad Christum. Eadem itaque causa est cur non oretur tunc pro hominibus eternaliter puniendis, que causa est ut non oretur neque nunc neque tunc pro malis spiritibus. Sed tercio principaliter arguitur per hoc quod homo potest meritorie orare generaliter pro defunctis, immiscendo intencionem orandi specialiter pro patrono vel alio amico cum hoc quod ipse sit dampnatus, in quo casu orat licite pro dampnato, ergo hoc licet. Confirmatur tripliciter: Primo per hoc quod oracio condicionata est oracio qualem oportet concedere esse licitam pro dampnato, cum sit ex gracia, et per consequens necessitat ad orandum pro talibus. Secundo confirmatur per hoc quod beatus Gregorius oravit specialiter pro Traiano quem scivit esse dampnatum, quia Johannis III°, 18: Qui non credit iam iudicatus est. Imperator autem Traianus fuit infidelis decedens in mortali, ergo cum beatus Gregorius fuit pro illo exauditus a domino, videtur quod pro talibus licitum est orare; ergo sanctus potest mereri ut tales resuscitentur, potest mereri ut salventur. Tercio confirmatur per hoc quod licet orare pro quolibet cui oracio foret utilis vel malum tolleret, sed sic est de omni merito militantis ecclesie quoad dampnatos, ergo licet orare pro illis saltem tollendo magis malum quod eis aliter eveniret. Nam sepe dictum est quod totus mundus adquirit perfeccionem secundam ex merito Christi, cum aliter forent dyaboli penalius cruciati, eo quod aliter haberent maius consorcium conpunitum, plus demerentur amplius seducendo, et careret perfeccione secunda, qua modo consolacione sanctorum misericorditer [p. 532] sunt puniti. Bonum ergo quod dyabolus facit predestinatis per accidens fit in virtute meriti Christi; quod videtur de tanto illis proficere. Et per idem videtur quod viator de quanto victoriose resistit dyabolo, confortando fratres ecclesie, mitigat de eius malo, et per consequens facit ut tolleracior sit eius dampnacio et de tanto effectualiter orat pro illo; membra enim sua maxime nocent sibi, quia sicut timentibus Deum omnia cooperantur in bonum, sic prescitis omnia cedunt in malum, et potissime que videntur eis magis utilia. Hic dico quod minor est falsa, nam in casu posito homo intendit orare pro dato mortuo, sed non orat pro eo ex eius incapaci- tate, sed intencio sicut oracio generalis est in casu meritoria. Unde ad hoc quod quis oret Deum pro aliquo requiritur eius capacitas, ut puta, quod sit creatura racionalis, capax boni pro quo racionabiliter oratur. are Et ad primam confirmacionem dico quod contingit intelligere oracionem condicionatam dupliciter; vel quoad

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 528.18: It is argued that our prayers must cease if we may not pray for the damned.
- 529.4: Distinctions In prayer:
- 529.7: 1. general or distinct;
- 529.12: 2. absolute or conditioned;
- 529.20: 3. for bliss or for less good.
- 529.27: We may pray for good less than bliss on behalf of the foreknown;
- 530.1: but if we knew they were in hell our prayers would be useless.
- 530.7: We do best to pray generally and conditionally.
- 530.23: The Church prays for all men, but her prayers are effectual only for the elect.
- 531.6: It is said that we may pray generally but with a special intention for a friend, who may be damned.
- 531.15: The example of Gregory and Trajan is cited,
- 531.23: and it is urged that even the devils profit by Christ's merit.
- 532.12: I reply that in the case put the intention is for the man if he is capable.
- 532.19: All prayers are conditioned by the divine will and the capacity of the subject.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 528: *pro* (b and margin letter H glued) [R4]
  - 529: *(ubi* (200d is the glued folio mark) [THIN]
  - 529: *trimembris* (5 is the line number) [R4]
  - 529: *petimus* (201a is the glued folio mark) [R4]
  - 529: *illum* [R3]
  - 530: *Deo* (English side-note "to" glued) [R4]
  - 530: *Vª* [R4]
  - 531: *specialiter* [NW]
  - 531: *sit* (English side-note "may be damned" glued in other scans) [R4]
  - 531: *III°* [R4]
  - 531: *18:* [R3]
  - 531: *Qui* [R4]
  - 532: *incapaci-* (hyphen half; tate, follows at pos 106) [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 528:
2. A in marg.: Obiectus. 10. A A,: scit impertiri. 12. B:
salutat solvit; A: salutat correxit in solvit ; A, : salutat. 28. morientis.
Conieci. A: iam mori. I.ocus rasura corruptus. H : utor iam mori.
A,: vita sine moritis. 3o. B: ergo orare.

p. 529:
5. A in marg.: Responsio. Nota trimembrem distinccionem oracionis.
27. A in marg. : Quomodo est orandum pro mortuis continuc infra (Above
2010 without mark of reference). 3o. B: cum continue. 33. B:

p. 530:
i5. B: cum hoc — mancipari deest. 19. In codd.: gaudii.
27. A: in hoc in hoc. 29. B: isti sunt tamen.
to. Decreti tercia pars, dist. V, cap. XXIV.

p. 531:
3. A A,: etcrnaliter promercndis 19. B: inlidelis deest.
22. in codd. : resuscitnr. 27. A in marg.: Nota causam. Christi
passio perficit omnia. 32. B: careret scil. mundus; sunt puniti
scil. diaboli. Locus iste haud dubic corruptus est.

p. 532:
1. A A,: quod deest. 4. B: de quarto viatori. 10. 11. A A,:
qui videntur. A in marg. : Responsio.
9. Rom. VIII, 28.
```

---

## Chunk 22-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "532.21–535.2"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 5 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "624 words; 575 unanimous or majority-real; 33 settled by vote (INS 2, R2 19, R3a 11, R5a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n569–n572 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 5: [TITLE]

## ¶1 · 532.21–533.23

> [p. 532] voluntatem divinam, ponendo in eius voluntate quid et qualiter decreverit succurrendum, et talis debet esse oracio viatorum; vel secundo quoad capacitatem subiecti pro quo orare intenditur, et sic supposita eius incapacitate ipsum subiectum non est persona pro qua sic oratur, sed vel ipse orans vel alia capax persona ecclesie. Quod autem vulgariter dicitur orari pro tali intento suffragari, licet sit inhabilis, equivocatur in nominetenus oracione, sicut forte oracio indigni non est aput Deum univoce oracio pro quocunque; licet ergo orare pro viatore prescito, cum sit capax meriti ut micius puniatur, sicut est de prescitis qui ad oracionem alterius faciunt nedum [p. 533] multa bona de genere, sed meritoria secundum presentem iusticiam, racione cuius micius dampnabuntur et interim ecclesie merebuntur. Sed cum certum sit quod dampnati sunt, amplius orare pro illis foret omnino inutile, ymmo oracio catholici non est pro illis, cum impossibile sit ipsam illis proficere; contendens vero quod ipse orat pro tali mortuo potest mortificare oracionem propriam contendendo. Nec contendo contra volentem defendere quod licet particulariter orare pro dampnato, dum tamen orator hoc ignoraverit, quia talis oracio nonnisi equivoce est pro illo, sed intendens quod sit pro illo faciliter meretur veniam; nec valet iuramentum oratoris, quo obligat se ad orandum annaliter temporaliter pro defuncto, sed amici defuncti debent appetere quod generaliter oretur pro mortuis in purgatorio, et talis oracio tantum vel plus sibi valet sicut oracio specialis, supposito quod sit ibi; et nulla oracio valet sibi dummodo sit dampnatus. Ideo utrimque non mediocriter peccant qui errando postponunt melius et eligunt minus bonum. Quando ergo dicitur quod oratur pro dampnato, intelligitur quod pretenditur orare pro eo, quod fit nunc licite et nunc male.

[ENGLISH]

## ¶2 · 533.24–534.9

> [p. 533] Ad secundum confirmacionem admitto cronicam et dico quod nec beatus Gregorius nec Deus ipse scivit Traianum fuisse dampnatum ad penam perpetuam, quia Deus eternaliter predestinavit Traianum ad gloriam; et sicut eternaliter ordinavit eum ad penam purgatoriam, sic eternaliter ordinavit quod mediante intercessione beati Gregorii salvaretur, quia debemus credere quod nec beatus Gregorius nec beatus in celo potest mutare divinum consilium vel per preces mutare vel flectere suum propositum (ut dicit decretum beati Jeronimi [p. 534] ubi supra). Et patet quod Traianus decessit in gracia predestinacionis, nec audivi suasum quod non decessit in gracia secundum presentem iusticiam. Multi enim extra iudaismum erant catholici (ut patet de Job, de Nabugodonosor et eis similibus), et sic est de multis quos propter solempnitatem ritus nostri decernimus esse foris. Nam corde creditur ad iusticiam, et in tali iusticia decedens est vere ecclesie filius et flamine baptizatus.

[ENGLISH]

## ¶3 · 534.10–535.2

> [p. 534] Nec vidi suasum quod beatus Gregorius peccavit M in quantum hoc peciit, cum factum Dei in concedendo ostendit hoc fuisse iustum et Deo beneplacitum. Ideo si sanctus papa peccavit in sic orando, hoc fuit quia defecit in modo, ut puta, affeccione singulari suum studium occupando, suffragia ecclesie magis utilia dimittendo, vel in alia tali circumstancia, propter quod ad sui meritum temporaliter est punitus. Unde sepe contigit hominem mereri in volendo et orando pro illo quod Deus non vult fieri, ut patet de stimulo carnis pro cuius decessu apostolus rogavit ter dominum (ut patet IIª Cor. XII°), et sepe contingit hominem laborare, orare et facere illud quod Deus vult fieri, et tamen peccare graviter propter defectum modi agendi, sicut meminit Augustinus, XXII° De Civitate Dei, capit. II°: Multa, inquit, volunt fieri sancti eius ab illo inspirata sancta voluntate, nec fiunt; sicut orant pro quibusdam pie sancteque, et quod orant non facit, cum ipse in eis hanc orandi voluntatem sancto spiritu suo fecerit. Et videtur equivocando de velle, Deum velle in aliis quod non vult in se ipso. Movet ergo Deus corda hominum ad nunc modeste orandum pro illo quod ipse vult fieri, et nunc pro illo quod ipse non vult fieri; [p. 535] semper tamen talis oracio habet fructum suum et est peticio racionalis ac voluntati divine conformis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 533.14: Prayers should be said generally for the souls in purgatory and the special intention would profit no less.
- 533.24: As to the example I say that Trajan was predestined to be saved by the intercession of Gregory.
- 534.4: Men may be Catholics whom we judge to be outside.
- 534.18: It may be right for a man to ask what God will not grant.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 532: *oracio* (30 is the line number) [NW]
  - 533: *multa* (201b is the glued folio mark) [THIN]
  - 533: *omnino* (5 is the line number) [R4]
  - 533: *obligat* (201c is the glued folio mark) [R4]
  - 533: *generaliter* [R4]
  - 533: *Gregorius* [R3]
  - 533: *∅* (coordinator: joined at 186 (agent 12)) [R5]
  - 533: *fuisse* [R3]
  - 533: *Traianum* (coordinator: Traianum split T|raianum (198 was DEL) (agent 12)) [R4]
  - 534: *gracia* (201c folio mark and margin letter L glued) [R4]
  - 534: *de* [R4]
  - 534: *IIª* [R4]
  - 534: *II°* (colon dropped per superscript rule) [R3]
  - 535: *semper* (201c is the glued folio mark) [THIN]
  - 533: *Traianum* (Traianum split 1|raianum (agent 12)) [OVERRIDE]
  - 533: *∅* (joined at 197 (agent 12)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 532:
1. A A,: quod deest. 4. B: de quarto viatori. 10. 11. A A,:
qui videntur. A in marg. : Responsio.
9. Rom. VIII, 28.

p. 533:
5. 6. B: non pro illis. 12. Codd. : quo sit. 24. A in marg. :
Nota dc Traiano quem Dcus per oracionem Grcgorii de dampnacione
liberavit. 28. A B : sic eternaliter.

p. 534:
21. B: II deest. 28. B: non faciunt. 25. A in marg.: Augustinus.
25. Aug. Opp. tom. VII, pag. 656.

p. 535:
17. B: Qua ergo. 23. A in marg.: Huius contrarium habetur in
decalogo. 25. A in marg. : Augustinus. A: civitate cap. 3o. AA,:
antea finiant; in Augustino: aliquando.
2 5. Aug. Opp. tom VII, pag. 640.
```
