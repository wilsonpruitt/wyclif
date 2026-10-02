# Translation brief: ecclesia 21-a–21-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-21-a.md chunks/ecclesia/wyc-ecclesia-21-b.md chunks/ecclesia/wyc-ecclesia-21-c.md` once and fix what it reports.
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

## Glossary (the 180 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
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
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
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
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| ablatarius | the one from whom it is taken | Beside *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 15, 343.7). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |

---

## Chunk 21-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "491.2–494.12"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 1 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "805 words; 728 unanimous or majority-real; 63 settled by vote (R2 37, R3a 22, R3b 2, R5a 2); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n528–n531 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 1: [TITLE]

## ¶1 · 491.2–492.10

> [p. 491] Fortuna non tantum arridet mihi ut valeam facere aliquod argumentum quod visum est in oculis doctoris valere in materia de rectiiicacione elemosine occupate a clero per dominos temporales, sed breviter quodcunque argumentum quod feceram dicit generaliter deficere tam in materia quam in forma. Sed revera sic dicere non est solvere, quia sic pica posset solvere quelibet argumenta. Quesivi autem si rex Anglie potest auferre licite atque legitime temporalia a clero suo legio delinquente, et dimissa forma illius questionis vecorditer insoluta, convertit more matrone respondentis querenti quantum distat Lincolnia quod sacculum plenum prunis. Rex (inquit) non potest auferre simpliciter aliqua temporalia a clero suo legio delinquente, et quia sensus quem habet de signo isto simpliciter est multis incognitus, ideo specificat eius sensum. Solum (inquit) aufert simpliciter qui auctoritate propria aufert; et quia oportet dicere quod rex habet auctoritatem propriam ad hoc datam sibi a Romano pontifice vel a Deo, ideo oportet ipsum dicere quod solum ille auctoritate propria facit qui non capit illam ab alio. Auctoritas enim que subiectatur appropriate in rege est auctoritas propria, quia aliter nihil sufficeret facere auctoritate propria. Sic (inquit) ille aufert simpliciter bona ab ecclesia qui aufert ab ea omnia bona sua. Rogo videamus primo quam remote dimittitur questio insoluta et videamus secundo quam infundabiliter et extranee fingitur signacio huic signo simpliciter. Nam iuxta hunc sensum nichil potest facere quicquam simpliciter nisi Deus, sed solum secundum quid. Sed cum non sequitur: Creatura facit opus solum secundum quid, ergo facit illud, sed [p. 492] sequitur evidenter oppositum propter fallaciam secundum quid, et simpliciter videtur quod non est possibile creaturam facere quicquam bonum vel malum, et per consequens, nullus dominus temporalis dedit ecclesie dominium temporale, et per idem non habet quodvis dominium, quia solum daretur sibi, ut haberet illud secundum quid. Nec valet fingere quod iste terminus simpliciter habet sensum predictum, ubi doctor limitaverit, et alibi habet sensum alium, quia non valeret significacio huismodi solum fundabilis ex tali auctore.

[ENGLISH]

## ¶2 · 492.11–494.12

> [p. 492] Item, iuxta fidem scripture ante ascensionem fuit verum quod auferetur ab apostolis Christus qui est sponsus ecclesie (ut patet Marci 11°, 20); ex quo oportet consequenter concedere quod Deus pater abstulit simpliciter ab apostolis Christum suum, quia auctoritate propria. Quod videtur nimis extraneum, cum solum ad tempus abstulit eis Christum et solum secundum humanitatem vel partes eius, cum mansit cum apostolis perpetuo non ablatus secundum divinitatem que est tota personalitas sua; ideo secundum modos loquendi philosophorum talis foret ablacio secundum quid, licet fuit vera ablacio. Item, iuxta, istam descripcionem nec homo nec Deus posset auferre simpliciter aliquod bonum ab homine; homo non, quia tunc auctoritate propria et non auctoritate Dei sic faceret? quod esse non potest, sicut nemo potest habere auctoritatem ad peccandum. Deus autem si auferret ab homine omnia bona sua, tunc illa ablacione annichilaret ablatarium, quia remanente eo oporteret remanere aliquod bonum suum. Quomodo ergo bonitatem essencialem posset Deus auferre a bono? Per illam Deus ergo non posset auferre bona ab ecclesia [p. 493] vel alia creatura; et revera fingere talem significacionem infundabilem ad cecandum regem et regnum quod non possunt quicquam auferre a subditis, foret nimis supina stulticia, nam ignorancia est percepta. Sic enim dicerent domini quod non auferunt simpliciter sed secundum quid, proporcionaliter ut dederunt, nec foret alicubi periculum, quia illa bona non fuerunt sua sed solum secundum quid. Melius ergo fuisset descripsisse veritatem catholicam et defensionem pertinacem, ut declaretur si poterit quod non verificatur de rege et regno descripcio predicta de heresi, sed ad tedium scole fugitur per ambages. Melius tamen foret studere logicam et dicere quomodo debet intelligi iste articulus fidei catholice ecclesiam sanctam catholicam, tunc enim non dicerentur tot sentencie heretice et sibi ipsis contrarie, ut puta, quod ecclesia que ante mortem Christi fuit synagoga cepit post mortem Christi. Ista enim non est logica huius mundi quod ante mortem Christi non fuit ecclesia et sic de multis aliis erroribus. O quam gloriosa foret conclus quod nemo potest quicquam auferre a clerico nisi iuste, nemo enim potest quicquam auferre a clerico nisi auferat illud simpliciter, sed nemo potest quidquam auferre simpliciter nisi iuste, ergo conclusio. Si enim quis aufert aliquid auctoritate propria, cum nemo potest habere auctoritatem ad peccandum, sequitur quod nemo potest auferre quidquam auctoritate propria nisi iuste. Sed ulterius multiplicando inconveniencia dicitur quod clericus sciens patronum suum esse dampnatum debet orare pro eo, ut mitiget eius penam, et allegantur ad hoc dicta doctorum Prepositivi, Altissidorensis, [p. 494] Hostiensis in Summa, et specialiter doctoris Bonaventure super IV° Sentenciarum, et ita (ut prius dogmatizatum est) quod privilegia et possessiones ecclesie debent in casu defendi per mendacia, ita modo dicitur quod debet eorum possessio continuari per suffragia dyabolica. Constat quidem ex fide evangelii quod ludas est dyabolus, et per idem quilibet perpetuo dampnatus. Sicut ergo suffragia specialiter facta pro mortuis sunt suffragia mortuorum, sic suffragia facta specialiter pro dyabolis sunt suffragia dyabolorum. Unde percipiatis quomodo mendax allegacio induxit ad interpellandum pro dyabolo dampnato speciali suffragio.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 491.2: My opponent says all my arguments fail in matter and form, but he will not meet them.
- 491.13: He says that the King cannot"simply" take away goods from a delinquent clergy; and by "simply" he means: a) the authority must be original;
- 491.25: b) the taking must be complete.
- 491.28: α) According to this only God can do anything simply,
- 492.2: and no one can have made gifts to the Church.
- 492.11: β) God took Christ from the disciples, but not altogether.
- 492.23: Even God can take nothing from man since he must take everything and destroy man.
- 493.4: Rulers may take away "secundum quid", as the goods were given;
- 493.19: indeed we may come to the logical conclusion, that all taking from the clergy is right.
- 493.28: My opponent says that a priest may pray for a patron whom he knows to be damned.
- 494.5: This would be praying for a devil.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 491: *CAP. XXI.* [HEAD]
  - 491: *habet* [R4]
  - 491: *signo* [R3]
  - 491: *specificat* [R4]
  - 491: *fingitur* [R4]
  - 492: *evidenter* [THIN]
  - 492: *oppositum* [THIN]
  - 492: *secundum* (print secun-|dum; main token holds the whole word (no separate dum token)) [THIN]
  - 492: *∅* (coordinator: joined/placed by OVERRIDE (part99)) [THIN]
  - 492: *facere* [R3]
  - 492: *habet* (5 is the line number) [R4]
  - 492: *sic* (print: sic faceret; main has no sic token) [INS?]
  - 492: *faceret* [R3]
  - 492: *quid,* (quid split qui|d (agent 11)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 491:
14. 15: plcnum pravis. 21. A in marg.: l)e ablacionc temporaliuni.
21. B: tens oportct. 26. A A,: qui aufcrrct. 3i. 32. A A,: sed
bonum bccundum.

p. 492:
6. B: vel haberet. 9. 10. B: valeret signacio. 10. A: ex tali
ex auctore; A: ex tali exactore. 11. A in marg.: De ablacione tem-
poralium (Below io6b without mark of reference). 16. A in marg.:
De illa diccione simpliciter quomodo debet intelligi (Above 196« without
mark of reference). 19. 20. B : secundum deitatem.

p. 493:
1. B: signacionem. 24. A A,: quis deest. 3i. In codd. :
preposiiivi Altisiodorensis.
3i. Praepositivus, natione Lombardus, cancellarius universitatis
Parisiensis anno 1207. cf. Fabricii Biblioth. med. et inf. aetatis VI,
3 1 5. Altissidorensis, cognomen nonnullorum dccrelistarum et
theologorum. cf. PYanklin Dictionnaire I. c. p. 5i.

p. 494:
11. A in marg.: SnfTragia pro mortuis si et quomodo prosunt (Above
io6d without mark of reference). i3. B: Beneventure. 16. A in
marg. : Quadruplex opinio. 2t. In Codd.: istum.
16. Verba Bonaventurae ; cf. Bonaventura, Liber IV Senten-
ciarum, dist. XLVI, Art. I, q. I (Opp. [Ed. Venet. 1764] IV,
```

---

## Chunk 21-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "494.13–498.29"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 2 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1039 words; 926 unanimous or majority-real; 96 settled by vote (INS 1, R2 61, R3a 30, R5a 4); 17 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n531–n535 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 2: [TITLE]

## ¶1 · 494.13–496.12

> [p. 494] Rogo notetis quomodo allegatur doctor Bonaventura super IV° Sentenciarum procurasse effectualiter pro hac parte; scribit enim super distinccionem XLVIᵃᵐ libri quarti sub hac forma: Videtur, inquit, quod per suffragia aliqua mitigacio fiat dampnatis et faciendo quinque raciones pro parte illa recitat tres responsiones quas reprobat. Prima dicit quod suffragia ecclesie prosunt dampnatis, non tamen omnibus, quia non valde malis, et istam dicit fuisse magistri Prepositivi. Sed ista dimissio pene est solum ad tempus (ut quidam dicunt quod omni diei Pasche habent omnes dampnati remissionem pene). Secundi dicunt quod fit remissio simpliciter non secundum proporcionem arismetricam sed geometricam (ut dicitur de indulgenciis), ita quod non quelibet operacio eque meritoria eque diminuit de pena eterna, sed quelibet operacio ecclesie eque meritoria diminuit proporcionaliter de pena quam invenit, ut si meritum ecclesie, ut quatuor diminuit centesimam partem [p. 495] qualitativam pene, tunc quodcunque meritum domini diminuit proporcionaliter centesimam partem pene quam invenit, et ita superest semper divitibus occasio impetrandi indulgencias, tam pro vivis quam mortuis, tam existentibus in purgatorio quam dampnatis. Tercia opinio dicit quod suffragia ecclesie non prosunt dampnatis vel ad liberacionem totalis pene nec ad ablacionem partis pene diminuendo vel mitigando, puniens ne tantum puniatur, sed fortificando punitum ut melius et tollerabilius sustineat. Sed reprobatis hiis tribus opinionibus sequitur doctoris sentencia in hec verba: Ideo, inquit, est aliorum opinio communior et verior quod suffragia dampnatis non prosunt, nec ecclesia intendit orare pro eis. Et si sophista instet quod quelibet istarum opinionum est tunc vera, patet quod doctor intelligit quod quelibet aliarum est vera secundum partem, vel negative non est vera. Ista vero eis contradictoria est vera totaliter. Et consequenter respondet ad quinque argumenta facta in ppositum: Primum est ex dicto beati Augustini, Enchiridion CX°, dicentis quod quibus mortuis prosunt suffragia ecclesie vel prosunt ut plena fiat remissio vel ut tolleracior fiat eis dampnacio. Ex quo videtur quod pena dampnati poterit mitigari. Dicendum, inquit, quod non intelligitur de dampnacione facta in inferno, ubi nulla est redempcio, sed in purgatorio, ubi dupliciter illis prosunt: vel statim liberando, ut eos qui parum habent de cremabili vel mitigando quoad eos qui gravius peccaverunt. Et eandem responsionem tenet sanctus Thomas super [p. 496] IV°, distinccione XLVIª, questione prima. Dampnacio, inquit, quandoque large accipitur pro deputacione ad penam quancunque, ut Luce XXIII°, 40 dicit beatus Latro, tu in eadem dampnacione es; quandoque vero accipitur stricte pro deputacione ad penam perpetuam, ut Matthei XXV°, 46: Ibunt hii in supplicium eternum; et ista significacio est famosior. Et istam responsionem tenet Ostiensis in Summa sua, libro quinto, De Penitenciis et Remissionibus, secundum quod anime defunctorum, et exponitur dictum Augustini, XIIIª, q. IIª Tempus. Glossa autem que dicit quod papa dispensat contra Deum male exponit contrarie Hostiensi.

[ENGLISH]

## ¶2 · 496.13–498.7

> [p. 496] Secundo arguit doctor ex alio dicto beati Augustini dicentis de pena Arrii quod non est determinata, quia augetur secundum quod peccatores suo errore multiplicantur, sed Deus pronior est ad miserendum quam ad puniendum. Ergo si in statu dampnacionis potest eorum pena augeri, potest et minui. Dicendum, inquit, quod non est simile, quia remissio debet fundari in fundamento caritatis, sed Arrius continue habet malam voluntatem sed non caritatem. Tercio arguit sic: Impossibile est multorum preces non exaudiri, sed ecclesia orat pro omnibus fidelibus qui moriuntur; de quibus constat multos dampnari. Ergo si ecclesia non frustra orat, oportet omnes fideles salvari. Dicendum, inquit, quod si constaret ecclesie aliquem esse dampnatum, non oraret pro eo. Et quantum ad formam ac materiam ulteriorem istius argumenti patet inferius. Quarto arguit doctor sic: Plus placet Deo pena quam quis sustinet voluntarius quam alia [p. 497] quam quis sustinet invitus, sed dampnatus penam sustinet invitus. Sed vir iustus in casu penam sustinet voluntarius pro dampnato, ergo vir iustus superstes plus solvit Deo pro dampnato voluntarie paciendo, quam dampnatus sufficeret solvere pro se ipso. Ergo si Dei iusticie satisfactum est pro eo quod minus placet, Dei misericordia acquiretur pro eo quod magis placet. Dicendum, inquit, quod verum est, cum Deus remunerat virum iustum qui pie et condicionaliter orat pro defuncto dampnato. Sed (ut dicam posterius) talis orat realiter pro se ipso et solum pro capacibus. Ideo dicit doctor, eo quod pena voluntaria non potest assumi nec acceptari pro eo qui non habet caritatem. Quinto arguit doctor sic: Talis iustus punit se meritorie pro dampnato, ergo Deus acceptat hanc penam pro illo. Sed Deus non bis punit in id ipsum, ergo oportet quod dampnatus habeat mitigacionem pene. Patet ex significacione proximi argumenti quod iustus punit se pro merito suo atque ecclesie et non pro salvacione talis dampnati. Sed ulterius querit doctor utrum fiat mitigac pene dampnatorum ex pietate misericordie divine. Et larguit primo quod sic per illud Psalmi LXXVI, io: Numquid obliviscetur misereri Deus aut continebit 2in ira sua misericordias suas? Secundo per hoc quod peccans mortaliter offendit Deum a quo est omne bonum, ergo meretur amittere omne bonum; cum ergo Deus non adnichilat eum, videtur quod Deus misericorditer punit eum. Tercio per hoc quod, eo ipso quo quis peccat offendit in ordinem, et per consequens meretur statim ordinari ad penam, cum ergo Deus expectat eius conversionem et non statim [p. 498] dampnat eum, videtur quod pietas Dei se extendit ad dampnabilem. Quarto per hoc quod peccans offendit in infinitum bonum, ergo meretur infinitam penam, quam cum Deus non infligit, sequitur quod Deus misericorditer punit quemlibet peccatorem. Sed doctor respondet concedendo consequens: Dicendum, inquit, quod mitigacio pene dampnatorum dupliciter

[ENGLISH]

## ¶3 · 498.8–498.29

> [p. 498] potest intelligi, aut quantum ad taxacionem et infliccionem pene; et sic indubie est pene mitigacio in inferno, quia illa mitigacio non est nisi mitis et misericors perpetue pene deputacio. Sed secundo modo potest intelligi mitigacio post pene taxacionem et infliccionem, et hoc modo nulla cadit mitigacio a divina misericordia. Et rogo scolam hic vigilanter attendere si non sit fictum mendacium adducendo testimonium huius doctoris in aliquo, cum tam manifeste contrariatur dicenti quod ecclesia debet orare pro dampnatis in inferno, ut pena eorum fiat remissior. Unde sanctus Thomas (ubi supra) recitando tres opiniones erroneas imponit terciam Altissidorensi dicenti quod dampnati non suffragantur per diminucionem vel interrupcionem pene, sed per confortacionem pacientis, sicut si homo portaret grave onus et facies sua perfunderetur aqua, confortaretur, licet onus in nullo sit levius. Est, inquit sanctus, predicta opinio presumptuosa, ut puta, sanctorum dictis contraria et vana, nulla auctoritate fulcita et nihilominus irracionabilis, quia dampnati in inferno sunt extra vinculum caritatis, secundum quam opera vivorum continuantur defunctis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 494.13: He alleges the authority of Bonaventura, who is against him.
- 495.25: Damnation is used in two senses and may be only to pain in purgatory,
- 496.13: Argument from a saying of Augustine's;
- 496.23: from the Church's praying for all the departed.
- 497.1: 4. Voluntary atonement is better than involuntary; so the suffrages of the pious atone more than the pains of hell.
- 497.14: 5. God accepts the atonement.
- 497.17: Answer: The profit is to the Church, not to the damned.
- 497.21: The doctor argues that God's mercy extends to the damned.
- 498.6: God's mercy works in fixing their punishment, not in lessening it afterwards.
- 498.19: St. Thomas also declares the damned to be beyond our aid.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 494: *∅* (the is from the English side-note "He alleges the"; print has Rogo) [INS?]
  - 494: *hac* [R4]
  - 494: *XLVIᵃᵐ* (superscript am) [R4]
  - 495: *qualitativam* (folio mark 196d glued) [THIN]
  - 495: *CX°* [R4]
  - 496: *XLVIª* [R5]
  - 496: *XIIIª* (10 is the line number) [R4]
  - 496: *IIª* [R4]
  - 497: *quam* (folio mark 197a glued) [THIN]
  - 497: *iustus* [NW]
  - 497: *sufficeret* [R4]
  - 497: *Ergo* [R4]
  - 497: *Et* [R3]
  - 498: *dupliciter* [THIN]
  - 498: *potest intelligi* (print: potest intelligi; main has no potest token, appended in print order) [THIN]
  - 498: *ubi* (print (ubi supra)) [R4]
  - 498: *Dicendum,* (italic; 1 is a margin numeral) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 494:
11. A in marg.: SnfTragia pro mortuis si et quomodo prosunt (Above
io6d without mark of reference). i3. B: Beneventure. 16. A in
marg. : Quadruplex opinio. 2t. In Codd.: istum.
16. Verba Bonaventurae ; cf. Bonaventura, Liber IV Senten-
ciarum, dist. XLVI, Art. I, q. I (Opp. [Ed. Venet. 1764] IV,

p. 495:
8. A A, : diminuende vel mitigande. 21. In codd.: Euch. CXII.
25. A in marg.: Responsio. 28. A: ut eis. A in marg. : Dampnacio
capitur dupliciter.
21. Aug. Enchir. cap. CX. Opp. tom. VI, pag. 238. Cf. Bona-
ventura 1. c. Opp. IV, 1019. 25. Bonaventura 1. c. Opp. IV,

p. 496:
7. B: ista signacio. 18. A in marg.: Responsio. Argumenta quod
omnes salvabuntur et soluciones (Above 197» vvithout mark of reference).
26. A in marg.: Responsio. 3o. A: quis tinet.
1. Thomae in IV. librum Sentenciarum dist. XLVI, q. II.
Opp. tom. X (Edit. Paris. 1660), pag. 707. 10. Decr. sec.
pars, causa XIII, q. II, cap. XXIII. 18. 26. Bonaventura I. c.

p. 497:
i. A: quis tinet. 8. A inmarg. : Responsio. i8. B: signa-
cione. 19. A in marg.: Responsio. 21. A in marg. : Questio bona.
8. Bonaventura I. c. pag. 1021. 21. Ronavcntura I. c.
2?. Et sequencia ibidem in secunda quaestione (pagg. 1021, 1022)
mutatis aliquot verbis invcnies.

p. 498:
4. B: sequitur Oeus. 5. A B in marg.: Mitigacio pene dampna-
torum dupliciter accipitur. 7. A in marg. : Responsio. 20. In
codd.: Altissiodorensi.
6. Bonaventura 1. c pag. 1021, 1022.
```

---

## Chunk 21-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "498.30–502.9"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 3 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "741 words; 689 unanimous or majority-real; 44 settled by vote (INS 1, R2 29, R3a 13, R5a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n535–n539 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 3: [TITLE]

## ¶1 · 498.30–500.2

> [p. 498] Et post respondet ad quintuplex argumentum per quod probaretur ficta sentencia, et patet primum commentum mendacii et repugnancia testium adductorum. [p. 499] Si (inquam) liceret de testibus mendacibus colare commentum in quo erraverint, patet quod sentencia summe heretica posset colligi nedum ex sentencia dyaboli et membrorum suorum, sed ex sentencia doctorum catholicorum. Dyabolus enim ex arte mendacii inmiscet sepe cum mendaciis veritatem, igitur quando rite capitur unus doctor in testem, supponi debet quod non sit contrarius illi in eodem libro et eadem materia cuius sentenciam testaretur, etsi arguatur quod ego sim in eadem dampnacione, cum allego pro una supposicione quam supposui totum mundum, et constat quod mundus est mendax et proditor. Talia autem argumenta non sunt digna ut remittantur in vicum scolarum examinanda sophistis, sicut conclusio supradicta que ponit quod eadem ecclesia in numero que ante mortem Christi fuit synagoga incepit post mortem Christi, sed brasiatricibus Oxoniensibus mittenda est ista argucia examini concludens ex particularibus particulare eis impertinens, sicut replicacio qua dictum est quod non valet fingere hoc vel illud mitti debet grammaticis. Ego, inquit, valeo hoc fingere (nam sicut sunt multi mundi, sic valet) est equivocum iuxta grammaticos sic loquentes: Qui valet ille potest, et qui valet hic validus est; impersonale nunc personale notatur. Quid ergo totum genus hominum iudicare potest de istis arguciis? Secundum commentum mendacii est de caractere ordinis quod solum sacerdotibus imprimatur, et allegatur in testimonium huius ficticie Bonaventura super ?odist. XXIVª quarti Sentenciarum; et per illud mendacium dicit se tollere supposicionem quam supposui [p. 500] describendo clericum. Ostenditur autem illud mendacium ex veritate scripture doctorum.

[ENGLISH]

## ¶2 · 500.3–500.25

> [p. 500] Querit autem primo utrum in omnibus ordinibus caracter imprimitur et, probando quod sic, per quadruplex argumentum recitat duas opiniones quas reprobat; quarum prima dicit quod caracter in solo ordine sacerdotali imprimitur, in ordinibus autem inferioribus solum fit disposicio ad sacerdotalem caracterem, sed hoc dicit esse falsum. Cum in ordinibus sacris inferioribus fiat segregacio perpetua clericorum a laycis, ideo manifestum est quod limitacio in illis ordinibus est vel requirit clericalem caracterem. Secunda opinio quam reprobat est quod caracter imprimitur in omnibus ordinibus sacris, sed non in inferioribus, quia isti et non alii possunt laicis commisceri; sed cum nullus ordo sit iterabilis et quilibet habeat aliquid de racione sacramenti, videtur quod in quolibet sit aliquid quod habeat racionem rei et signi perpetui; hoc autem caracterem dicimus. Ideo est tercia opinio probabilior quod in omnibus ordinibus caracter imprimitur sicut raciones ostendunt expresse. Cum enim caracter sit signaculum expressum, distinctivum et perpetuum et Christo configurativum, et hoc est in omnibus ordinibus, non dubitandum est in omnibus caracterem imprimi.

[ENGLISH]

## ¶3 · 500.26–502.9

> [p. 500] Et consequenter respondet ad obiectum quadruplicem. Ad primum quo sic arguitur: Caracter est signaculum spirituale, ergo in illis solis imprimitur in quibus datur aliqua potestas nova et spiritualis, sed potestas omnium ordinum inferior est corporalis, ut aperire ostium vel custodire, prophetias dicere, candelabra [p. 501] deferre, ergo in istis nullo modo imprimitur caracter. Dicendum, inquit, quod omnibus ordinibus datur potestas vel spiritualis de se vel ad spiritualem ordinans. Unde potestas hostiarii est ad admittendum homines ad divinum sacrificium, potestas lectoris non solum ad excitandum auditorem exteriorem, verum eciam interiorem, et sic de aliis. Secundo sic arguitur: Caracter est signaculum quod respicit vel habet imprimi in ymagine ad configurandum ipsam Deo; sed actus quorundam ordinum solum sunt circa ministeria inferiora, ergo cum talia non spectant ad configuracionem huius, videtur quod in illis nullus caracter imprimitur. Dicendum, inquit, quod caracter ordinis ut conservativus animam configurat Deo secundum ymaginem quasi assimilatam Deo, quod potissime fit in ordine supremo, vel dicendum quod magis proprie configuratur tale signaculum Christo. Unde cum Christus triplex habuerit officium, scilicet ministri in agendo, pugilis in paciendo, redemptoris in moriendo, triplex fuit sacramentum secundum quod homo configuratur sic Christo tripliciter; unde tantum est triplex sacramentum in quo fit caracteris impressio. Nam baptismus configuratur morienti et redimenti, unde sepelitur homo in mortem. Confirmacio vero configuratur pacienti et pugnanti, ideo signum crucis fit in fronte. Sed ordo configuratur ministranti et operanti, sicut magister ostendit in litera, et quia in omnibus ordinibus configuratur clericus Christo secundum plus et minus, ideo in omnibus illis caracter imprimitur. Tercio sic [p. 502] arguitur: Caracter est signum indelebile; ergo si collocat hominem in aliquo statu, impossibile est ab illo statu recedere, quin fiat contumelia sacramento, sed in minoribus ordinibus constituti possunt licite redire ad laycum, ergo in eis caracter non imprimitur. Dicendum, inquit, quod caracter omnium ordinum manet in anima sive revertentis ad laicatum sive morientis ut signaculum distinctivum et hoc vel ad gloriam si bene usus est, vel ad ignominiam si male.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 499.12: My opponent's arguments are frivolous.
- 499.27: He alleges the authority of Bonaventura as to the "stamp" of priesthood.
- 500.3: But Bonaventura rejects two forms of his theory as to orders,
- 500.19: and favours a contrary view.
- 500.26: Bonaventura's opinions shown by quotations.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 498: *adductorum* (print adduc-|torum; main token holds the whole word with folio mark 197b glued) [THIN]
  - 499: *commentum* [R3]
  - 499: *eadem* [R4]
  - 499: *∅* (coordinator: joined/placed by OVERRIDE (part99)) [NW]
  - 500: *∅* (print men-|dacium; main has mendacium whole at pos 5) [INS?]
  - 500: *fit* [R3]
  - 500: *Caracter* [R4]
  - 499: *ordinis* (ordinis split ordi|nis (agent 11)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 498:
4. B: sequitur Oeus. 5. A B in marg.: Mitigacio pene dampna-
torum dupliciter accipitur. 7. A in marg. : Responsio. 20. In
codd.: Altissiodorensi.
6. Bonaventura 1. c pag. 1021, 1022.

p. 499:
18. In codd. : Oxon. 21. In codd. : in quia. 24. A A, : va-
lidus sit; li: validus (it. 27. A in marg. : Secundum commentum.
27. Comp. cap. XIX, p. 441. 3o. Cp. Bonaventura Lib. IV.
Sent. dist. XXIV, pars II, Art. I, q. I. Opp. IV, pag. 65o.

p. 500:
5. A in marg.: Duplex opinio. 6. A in marg.: De caractere
ordinis (Below 197»» without mark of reference). 9. A in marg.:
Bonaventura. 22. Codd.: distinctum . . . conliguratum. 26. A B m
marg. : Quadruplcx argumentum.
6. Seqq. e Bonaventurae libro IV. Sent. deprompta sunt. Cf.

p. 501:
2. A in marg. : Responsio. i5. A in marg.: Responsio. 18. In
codd. : habuit. 22. A in marg. : Tanlum in iribus sacramentis caracter
imprimitur. 28. A in marg. : Utrum in singulis ordinibus caracter
imprimitur (liclow 197« witliout mark of rcference).
14. Honaventura 1. c. ul est conservnntis animam. 27. 28 ma-
gister ostendit. Bonav. I. c: sicut recte ostendit.

p. 502:
6. A in marg.: Responsio. 8. A A,: signaculum destitulum :
B: distinctum. i3. B: ministralis. 14. A in marg.: Responsio.
17. A in marg.: Opinio. 18. B: diversis imprimuntur. 23. A in
marg.: Duplex opinio. .25. A in marg.: Prima.
25. Bonav. 1. c: minorem complexionem.
```
