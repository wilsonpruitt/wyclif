# Translation brief: ecclesia 19-h–20-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-19-h.md chunks/ecclesia/wyc-ecclesia-20-a.md chunks/ecclesia/wyc-ecclesia-20-b.md` once and fix what it reports.
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
| presciencia | foreknowledge | |
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| adolescentula | young maiden | Song 1:2, 6:7 (DR "young maidens"). Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
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
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
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
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| legalia | the legal precepts | Of the old law, beside *cerimonialia* "ceremonial precepts". Ruled 2026-10-02 (*Eccl.* 17, 389.2–3). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |

---

## Chunk 19-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "469.1–471.12"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "546 words; 501 unanimous or majority-real; 36 settled by vote (R2 17, R3a 7, R3b 1, R5a 9, R6a 2); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n506–n508 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 8: [TITLE]

## ¶1 · 469.1–471.12

> [p. 469] iudiciis prime iusticie. Si enim secundum leges hominum iudex iudicans seculare dominium vel ecclesiasticum officium pro procreato extra matrimonium quem vocat filium populi et illegitimum, quantumcunque predestinatus et habilis fuerit quoad Deum, multo magis iudex iudicans pro prescito quem Deus decrevit inhabilem iniuste iudicat, quia contrarie iusticie legis Dei. Nec valet ficta excusacio qua dicitur quod iudex facit suam diligenciam iudicando secundum suam noticiam, et nisi forent talia iudicia, maius malum contingeret. Nam quoad primum constat quod in talibus ambiguis, utrum iniusta fuerint, debet homo dubium illud dimittere et partem securam eligere. Hoc enim docuerunt Christus et sui apostoli tam scripto quam opere. Et quantum ad secundam partem, patet quod non est peccandum vel venialiter propter aliquod bonum signabile acquirendum vel malum culpe aut pene persone vel perpetuo precavendum. Y Et ex istis patet veritas conclusionis beati Augustini Epistola XXXVIIª ad Bonifacium quod leges hominum quas sanctus vocat iura civilia communiter sunt iniuste. Nam supposito quod Petrus sit predestinatus, carnaliter illegitimus, vendicans hereditatem vel ecclesiasticum officium, et supposito quod Paulus prescitus sit legitimus, vendicans illud idem beneficium, Petrus tamen habilis et Paulus inhabilis quoad Deum, et sint duo iudices quorum primus iudicet pro Paulo secundum leges hominum allegatas et testificaciones legalis testimonii plane depositas et iudicet secundus iudex pro Petro ex revelacione qua noscit Deum iudicare Petrum habilem ad datum beneficium et Paulum inhabilem, [p. 470] et patet quod secundus iudex iudicat iustum iudicium, et per consequens primus iudicando sibi contrarie iudicat secundum faciem et iniustum iudicium; et talis perplexitas est communiter in humano iudicio. Et patet possibilitas casus ex sentencia Augustini super Johannis, Sermone XI°, super illud Johannis III°, 1: Erat homo ex phariseis, ubi notat scripturam Exodi 111°, quare Deus signanter dicit: Ego sum Deus Abraham, Deus Isaac, cum Noe, Job, Moyses et alii multi erant patres veteres nominandi, et respondet quod in istis tribus patriarchis qui erant principia generis Hebreorum, Israelitarum et Judeorum figuratum est genus populi christiani. Nam illi tres habuerunt prolem de liberis et ancillis secundum divisionem quadruplicem; et sic est in populo christiano. Nam sicut Abraham genuit ex Sara libera Isaac bonum, sic ex Agar ancilla figurans malos (ut notat Apostolus Galatis IV°, 30) peperit Ysmahelem. Iterum Rebeca uxor Isaac nedum peperit Jacob bonum sed Esau malum tam nomine quam figura, et Jacob de liberis et ancillis peperit duodecim patriarchas. Sic ergo habemus bonos procreatos ex bonis, ut Ysaac de Sara, malos de malis, ut Ysmael de Agar ancilla, malos de bonis, ut Esau de Rebeca, bonos de malis, ut sunt filii Jacob quibus datur hereditas de ancillis. Correspondenter (ut dixi superius) inter christianos quicunque servaverint semen fidei patris nostri Jesu, de quantumcunque malis processerint quoad carnem, de quantumcunque malis sacramenta et legem Dei receperint, si perseveranciam finalem servaverint, sunt finaliter premiandi. [p. 471] 193° Ex quibus patet quod natale vicium sanari potest per viam morum tam quoad celeste beneficium quam terrenum, nec dubium quin dimisso affectu primatus vel data prepositura amovibili iuxta testimonium digni operis vel indigni foret melius in ecclesia quam est modo. Leges ergo secundum quas iudicatur contra magis habilem quoad Deum pro minus habili vel indigno sunt omnino iniuste vel, si non sic iudicatur secundum leges illas nec ille sufficiant habilitatem hominis ad talia edocere, stultum foret legibus illis in iudiciis cecis intendere et evidenciam operis quam Deus dedit relinquere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 469.1: Judges decide wrongly from not knowing who is predestinate.
- 469.19: Augustine said that civil laws are mostly unjust,
- 470.13: Fourfold division of Christians.
- 471.4: Prelates should be removable for bad behaviour.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 469: *XXXVIIª* [R4]
  - 470: *et* [THIN]
  - 470: *patet* [THIN]
  - 470: *III°* [R4]
  - 470: *1* (x-height old-style arabic 1 (shorter than III capitals), leaf zoomed) [R3]
  - 471: *foret* [NW]
  - 471: *melius* [R3]
  - 471: *in* [R3]
  - 471: *iudicatur* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 469:
8. Ainmarg. : Ficcio. 19. A in marg.: Augustinus. 19. B: quod
veritas; beati deest. Non in Aug. Ep. CLXXXV. Opp. tom. II, pag. 643
seqq. sed pocius in epistola ad Macedonium hanc sentenciam invenies:
Quaedam intcr eos iura constituuntur quae appellantur civilia, non quod
hinc fiat, ut bcne utentcs sint. . . . Opp. tom. II, pag. 534. 22. A in

p. 470:
1. A A,: patet deest. 6. Johannis; scil. cvangelium. 9. Isaac;
et Ucus Jacob deest in codd. 17. A A,: sic deest. 18. In codd.
Gal. 111. A in marg. : Nota nativitatem bonorum ex malis et econtra.
6. Aug. In Joh. Ev. cap. III, tract. XI, Opp. tom. III, pars II,
pag. 378.

p. 471:
1. A in marg. : Conclusio. 10. B: legibus vel in. 12. relin-
querc;A. Seq. glossa Bohcmica : Jako czynyc nassy pravilegistc. Id est: ut
faciunt nostri iuris legiste. 17. 18. B: ad regnandum. tg. In codd.:
Sponsus ct sponsa dicunt. Corrcxi e tcxtu Apoc. XXII, 17. 20. A:
quilibet librum.
```

---

## Chunk 20-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-20-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-20-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "471.14–475.31"
divisions: "cap. 20 (heading 'CAP. XX.' at 471.13); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1071 words; 961 unanimous or majority-real; 95 settled by vote (INS 1, R2 55, R3a 35, R5a 2, R6a 2); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n508–n512 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 20, part 1: [TITLE]

## ¶1 · 471.14–472.25

> [p. 471] Fructus huius longe contencionis de nostra sancta matre ecclesia roret sequens noticia scripture sacre, et per consequens dileccio sponsi et sponse inducens laborantes in ista fide fideliter in domum domini ad regulandum, ita quod illi applicetur illud Apoc. ultimo: Spiritus et sponsa dicunt: Veni. Quamvis autem quilibet liber scripture requirit pro eius sensu noticiam istius articuli fidei de ecclesia sancta catholica, specialiter tamen liber Apocalypsis, canticum ecclesie Proverbiorum XXXI° et Cantica canticorum. Quando enim partes ecclesie turbantur erga plurima, vocantur adolescentule non habentes ubera, quarum Salomon dicit non esse numerum propter volubilem affeccionem animi circa multa; sed quando Martha dimissa vita activa induit figuram Marie, intendens incomplete tamen uni necessario contemplando, inducta [p. 472] in thalamum, secundum numerum octogenarium dicitur concubina; sed tercio plus accedens ad unitatem que est omnia in omnibus notatur sub nomine regine et sub numero sexagenario post miliciam triumphalem; sed quarto quando cessabit omnis exaccio, area tocius ecclesie plene purgata a palea per ventilabrum finalis iudicii, non derelicta in corpore tocius ecclesie macula sive ruga, tunc dicitur una columba adepto fine unitatis caritative, secundum quam tota ecclesia est Christus. Patet ista sentencia Canticorum VI° et sparsim alibi in processu. Intendo ergo illam partem mediam scilicet canticum de muliere forti succincte transcurrere et difficultates profundas tam expositorias quam scolasticas superioribus meis relinquere. Video tamen (licet obscure) quomodo omnis difficultas logica, philosophica vel methaphisica includitur in scriptura de sancta matre ecclesia, ymmo (ut habundancius loquar) si quid subtilitatis repertum est a nobis in aliqua istarum arcium, eius sentenciam innuit nobis spiritus sanctus in cantico sapientissimi Salomonis de sancta matre ecclesia, Proverbiorum XXXI°, 10, Mulierem fortem quis inveniet; quod potest dividi in tres partes, in quarum prima narratur ecclesie sancte coniugium, in secunda describitur eius officium et in tercia concluditur eius preconium.

[ENGLISH]

## ¶2 · 472.26–475.31

> [p. 472] Primo autem supponitur esse unum primum coniugium iugium quod sit metrum omnium aliorum inter fortissimum virorum et mulierem sibi proporcionalem faciendum, nam secundum philosophos in omni genere est reperibile tale primum. In genere ergo coniugii supposita incarnacione verbi (quod est Deus fortis et potens in prelio) oportet invenire sibi coniugem bene fortem. Ideo primo de illa queritur: Mulierem fortem [p. 473] quis inveniet, ubi secundum sanctos doctores concorditer oportet per mulierem tortem intelligere sanctam matrem ecclesiam, quia quamvis sexaginta sint regine et octoginta concubine adolescentularumque non est numerus (ut dicitur Canticorum VI°, 7), tamen ex omnibus illis constat una columba (ut dicitur ibidem). Quis ergo inveniet dignam coniugem tanto sponso? Et videtur quod nullus hominum nisi ipse, nam in constitucione primi carnalis coniugii primus coniux concurrebat materialiter ad causandum suam coniugem (ut patet Genesis III°): ergo multo magis in illo coniugio celesti oportet coniugem concurrere in causa triplici ad causandum suam coniugem ex natura angelica et humana. Primo ergo opere creacionis secundum raciones exemplares in verbo, secundo vero opere ministracionis secundum raciones seminales in genere humano, et tercio opere recreacionis in Christo facto circulariter ista duo inventa est mulier ista fortis. Nam secundum illam partem lapsa in devium erravit, sicut ovis que periit in vepribus peccatorum, et (ut dicitur Matthei XVIII°, 12) pastor et sponsus dimissis nonaginta novem ovibus in pascuis semper virentibus in celo perditam ovem invenit et humeris suis labore et penalitate debita reportavit. Nec moveat quod beatus Augustinus in tractatu huius cantici dicit quod hec mulier est civitas supra montem posita quam difficile est nescire. Videmus enim modo per fidem secundum quam tamquam lucem secundam illuminat mundum, faciens nos luscos tenebra ignorancie obfuscatos videre eam speculariter et obscure, sic quod ignoramus quoad noticiam distinctam partes ecclesie, sicut videns civitatem longinque, confuse et [p. 474] indistincte videt domos eius et alia ornamenta. Nec sufficeremus sic cernere, nisi dicta mulier a sponso prius in racionibus exemplaribus et visceribus misericordie sit inventa. Unde post conclusionem propositam supponendo quod ille invenit hanc mulierem qui secundum divinitatem est immensus, a cuius oculis nichil potest esse absconditum et secundum humanitatem ascendit super omnes celos, subditur inventorem illum quoad naturam et quoad tempus respectu patrum veterum esse procul, sicut et mulier illa procul erat localiter a Iudeis, partim in celo secundum angelos et partim in terra secundum gentes pro tempore gracie convertendas, sicut procul erat a Deo per culpam, cum non sit possibile quicquam esse a Deo distancius quam peccatum. Inventa itaque muliere forti copulanda in primo coniugio videndum est secundo de suis passionibus, utrum sit apta nubere tanto sponso; et respondet litera consequenter quod de ultimis finibus precium eius. Quod videtur sic posse intelligi: causa finalis quare ecclesia est valida, ut Christo matrimonialiter coniungatur, sunt predestinaciones suorum membrorum. Nam causa celestis particularis coniugii est opus meritorium viatoris, et causa operis meritorii est gracia infusa, et causa gracie infuse est predestinacio que quasi ultimus finis citra Deum dignificat ecclesiam ad illud coniugium, quia (ut dicitur Johannis 1°, 16), de eius plenitudine nos omnes accepimus graciam pro gracia. Nam ex caritate eterna dedit nobis caritatem subiectivam secundum quam cum opere meritorio simus digni vel (ut habet litera Augustini) preciosiorem preciosis lapidibus que eiuscemodi est; cum quo verbo innuit eiusmodi [p. 475] mulierem in mente habere dileccionem usque ad finem; que Canticorum VIII°, 6 fortis ut mors dicitur. Ex quo sequitur quod mulier habens membra dileccione sic forcia sit sponsa racione consumate fortitudinis preciosa, quia usque ad finem diligit sponsum suum. Alii autem lapides scilicet caritates horales finaliter excidentes (ut fuit in Donato et aliis prescitis) non sunt tanti precii, ut subiecta sua sponso ecclesie coniungantur; vel tercio intelligitur non contrarie supradictis quod de ultimis finibus celorum et seculorum est precium, unde est dignitas huius sponse; vel quarto de divinitate ac humanitate in Christo qui sunt ultimi fines circuli intelligibilis est precium huius mulieris, ut patet ex fide, quia sicut verbum creat, ita dignificat sponsam suam. Et de ipso dicitur Psalmo XVIII°, 7: A summo celo egressio eius, et in ultima etate seculi consummata est gracia unionis virtute cuius originatur tota dignitas huius coniugii; Ia Cor. X°, 11 scribitur: Nos sumus in quos fines seculorum devenerunt. Inventa ergo coniuge et inventa eius dignitate ex precio vel valore, cum sponsus sit totum per se dignificans opus suum non restat quid tardaret illud coniugium. Ideo innuitur tercio affidacio celestis, dum subditur: Confidit in ea cor viri sui. Plane, inquit Augustinus, confidit et ut confidamus in eum edocuit. Prescius predestinacionis proprie confidit qui falli non poterit. Mulier autem cum filiis suis potest in ipsum confidere, eo quod mentiri non poterit nec sponse vel membris suis deficere, sed totus timor huius affidacionis stat in nostra desidia quod per nos non sit precium vel dos huius coniugii consummata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 471.14: This discussion should lead to knowledge of Scripture, especially the Apocalypse, the Song of the Church (Prov. XXXI) and the Canticles.
- 472.11: A short exposition of the Song of the virtuous woman.
- 472.21: It is in three parts: a) telling of the marriage of the Church b) of its office c) of its praise.
- 473.1: Verse Io. By the virtuous woman we understand the Church.
- 473.11: Christ has part in the making of his spouse, as Adam of Eve.
- 474.19: The Church is fit to espouse Christ because of the predestination of her members,
- 475.4: which makes her love to the end.
- 475.24: Verse II. The husband's trust in his spouse.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 471: *CAP. XX.* [HEAD]
  - 471: *illi* [NW]
  - 471: *dicunt* [R4]
  - 472: *thalamum* [THIN]
  - 472: *difficultates* [R4]
  - 472: *coniugium* (main token holds the whole hyphenated con-iugium) [R4]
  - 473: *mulierem* [NW]
  - 473: *III°* [R4]
  - 473: *angelica* (bold argument numeral 1 glued) [R4]
  - 473: *dicit* (folio mark 194a glued) [R4]
  - 474: *indistincte* [THIN]
  - 474: *angelos* (print ange-|los; main token anges covers both halves (no separate los token)) [R3]
  - 474: *distancius* [NW]
  - 474: *est* (trailing 1 is a margin mark, not text) [NW]
  - 474: *de* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 471:
1. A in marg. : Conclusio. 10. B: legibus vel in. 12. relin-
querc;A. Seq. glossa Bohcmica : Jako czynyc nassy pravilegistc. Id est: ut
faciunt nostri iuris legiste. 17. 18. B: ad regnandum. tg. In codd.:
Sponsus ct sponsa dicunt. Corrcxi e tcxtu Apoc. XXII, 17. 20. A:
quilibet librum.

p. 472:
1. A in marg. : De adolescentulis, concubinis et reginis Salomonis
(Above iy34 withoul mark of reference). 2. B : si tercio. 22. A in
marg.: Exposicio illius: Mulierein fortem quis inveniet. 26. A in
marg.: Supposicio. B: omne unum. 3i. B: quod est dominus.

p. 473:
14. A in marg. : Nota dc coniugio (superscriptum : matrimonio) Christi
et sponsa ecclesie (Below kj3j without mark of reference).
25. Aug. Sermo XXXVII de Prov. cap. XXXI, Opp. tom. V,
pag. 181.

p. 474:
7. A in marg. : Solus Chrisius poluit talem mulierem fortem invenire,
que est sua sponsa (Above 194» without mark of reference).
3i. Aug. L c. cap. III.

p. 475:
5. A in marg.: Nota de passionibus ecclesie, an posset nubcre Christo
6. B: licet caritates. 8. 9. A A,: sponsa ecclesia. B: sponso ecclesia.
i5. B: Eciam de. 18. B: erigitur tota. 19. Nos sumus deest in
textu apostoli citato. 22. 23. B: dictum couiugium. 26. B: pre-
scitus. Aug. : Prescius conlidit, falli non potest qui confidit. 3o. dosidia ;
```

---

## Chunk 20-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-20-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-20-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "476.1–480.15"
divisions: "cap. 20 (heading 'CAP. XX.' at 471.13); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1113 words; 963 unanimous or majority-real; 132 settled by vote (INS 2, R2 79, R3a 40, R3b 2, R5a 7, R6a 2); 18 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n513–n517 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 20, part 2: [TITLE]

## ¶1 · 476.1–476.11

> [p. 476] Quarto infertur quod uxor tanti domini cuius sunt omnia et ipsa cum eo una persona (ut docetur Matthei XIX°, 5), erit sicut vitis habundans in lateribus domus sue, ideo subditur quod spoliis non indigebit. Non, inquit Augustinus, quia non querit spolia, cum diffusa per mundum eius trophea accipit tamquam sua, quia Sapiencie X°, 19 scribitur: Iusti tulerunt spolia impiorum. Et hinc nimirum dicit sponsa, Psalmo CXVIII°, 162: Letabor ego super eloquia tua, sicut qui invenit spolia multa. Et sic ista quadruplex proposicio declarat in parte predictum coniugium.

[ENGLISH]

## ¶2 · 476.12–476.14

> [p. 476] Quoad secundam partem cantici in qua declaratur mulieris huius officium primo in generali premittitur quod sponsa tam grata, tam fida et tam fertiliter dotata

[ENGLISH]

## ¶3 · 476.15–477.25

> [p. 476] a viro reddet ei bonum et non malum omnibus diebus vite sue. Operatur, inquit Augustinus, viro suo bona eterna continue, quia (ut mihi videtur) omnes predestinati semper prosunt ecclesie sine dampnacionis sue demerito vel ecclesie detrimento. In hoc enim differt peccatum predestinati a peccato presciti quod primum est necessario remissibile et secundum dampnabile. Primum per accidens prodest ecclesie et peccanti (ut patet de peccato Petri) et secundum licet per accidens faciat ad bonum ecclesie, tamen continue sibi nocet, quia sicut quicquid predestinatus hic fecerit tendit ad sui salvacionem, sic quicquid prescitus hic fecerit tendit ad sui dampnacionem. Quod autem quidam dicunt peccatum predestinati dampnabile, equivocatur in nomine dampnabile sumpto large vel proprie. Large dicitur dampnabile culpandum quod perpetuo dampnaretur, si non foret Christi gracia [p. 477] preservatum, et sic omnis peccator foret dampnabilis. Sed proprie solum illud dicitur dampnabile ad quod est Dei ordinacio, ut dampnetur, et sic nunquam hec mulier vel aliquod eius membrum fecit malum dampnabile sponso suo. Et (ut notat Augustinus) hec mulier fecit non sibi principaliter, sed sponso bonum quodcunque fecerit tamquam viro et capiti modo quo loquitur Apostolus IIª, Cor. V°, 15: Qui vivit iam non sibi vivat, sed ei qui mortuus est pro omnibus et resurrexit, sic quod ecclesia et quodlibet eius membrum quicquid operatum fuerit hoc facit, ut ei placeat cui se probavit. Omnes enim alii querunt que sua sunt, non que domini Jesu Christi. Et hec est racio (ut dixi superius), quare Christus non usus est proprietate civili in se nec in suis apostolis. Nec moveat quod nemo debet bonum reddere huic viro propter hoc quod omnis homo est servus sibi inutilis, cum fecerit omnia que rector iste precepit, ut dicitur Luce XVII°, 10; et Psalmo XV°, 2 dicitur: Dixi domino: Deus meus es tu, quoniam bonorum meorum non eges. Verum est quod Christus in persona propria non eget modo humanitus neque divinitus, sed nos egemus ut faciamus omnia nostra opera primo sibi, hoc est ad honorem suum et utilitatem sui corporis in quo eget.

[ENGLISH]

## ¶4 · 477.26–478.18

> [p. 477] Habita solicitudine generali huius matrisfamilias, specificat secundo opus suum, cum subditur: Quesivit lanam et linum et operata est consilio manuum suarum. Secundum Augustinum lana est habitus collectus ex campo scripture ad regulandum vitam laudabilem corporalem et linum est habitus ad conversacionem spiritualem ducendam. Sic enim in ordine vestimentorum nostrorum corporalium interiora sunt linea, sed vestimenta exteriora sunt lanea. Correspondenter in vestibus anime que secundum fidem scripture sunt virtutes: [p. 478] quidquid carne operamur, est a dextra sensibile: quidquid spiritu, in secreto. Oportet ergo hanc feminam cum sua familia indui hoc geminum vestimentum. Operari autem carne et non spiritu quamvis bonum videatur, utile tamen non est. Operari vero spiritu et non carne pigrorum est; nam dans elemosinam pro laude hominum nudam vestem videtur indui, sicut dicens sibi sufficere in consciencia sua Deum colere, nec quod debet ad ecclesiam ire vel ceteris christianis actibus sensibilibus immisceri. Talis, inquit Augustinus, nudam vestem lineam vult habere. Non sic docet hec mulier, sed instituit simul secundum praxim et theoricam operari, nam ad hoc colligere debemus hos habitus, ut consilio manuum operemur. Virtus enim secundum philosophos est propter opera, et hinc felicitas consistit in actu vel opere, et melior est virtute. Omnem autem virtutem moralem oportet prudenciam regulari, et ideo signanter dicitur quod hec mater operata est consilio manuum suarum,

[ENGLISH]

## ¶5 · 478.19–480.15

> [p. 478] Unde ad denotandum varietatem operacionum huius matrone subiungit tercio: Facta est quasi navis institoris de longe portans panem suum. Notum est ex tractantibus de archa Noe et navicula Petri quomodo ecclesia similatur navi in qua divicie et diversa mercimonia congerunter habetque intra se mercantes tam venditores quam eciam institores, et cum per totam habitabilem nostram saltem potestative diffunditur, ymmo per purgatorium atque celos, patet quod de longe portat panem quo pascitur. Navis autem nedum in figura tendit ad similitudinem matrone sed ligna levigata ad imitacionem ligni crucis composita evehunt navigantem in seculo, ne procellis undarum [p. 479] et aliis maris periculis submergatur. Mercimonia et divicie huius navis sunt omnia genera virtutum et merita quibus bona patrie comparantur; sic pascitur anima viatrix per effluxum longinquum a triumphante ecclesia, sed anima purganda recipit panem ab ecclesia militante. Divicie, inquit Augustinus, in quibus pascitur et mercatur ecclesia sunt largiflue laudes sponsi, de quibus Psalmo CXII° dicitur: A solis ortu usque ad occasum laudabile nomen domini. Non enim pascitur nec solicitatur membrum ecclesie nisi in laude domini. Sed quia nec navis dicta nec sui incole debent ab operibus ociari, ideo quarto subiungitur huius matrone provida prudencia operando. De nocte, inquit, surrexit deditque predam domesticis suis et cibaria ancillis suis. Nox secundum Augustinum est tempus quo tortores dyaboli persequuntur christicolas, in qua involuti peccatorum tenebris videntur nocere fidelibus, sed eis surgentibus ad vitam plus prosperam nocent realiter sibi ipsis. Unde quia in talibus tribulacionibus claruit et profecit ecclesia, sicut granum trituracione separatum a palea, ideo signanter dicit sapiens quod de nocte surrexit. Aporiamur, inquit apostolus, et non defecimus, IIª Corinth. IV°, 8 et Ysaie XXVI°, 9: Anima mea desideravit te in nocte, et Job XXXVI°, 20: Ne protrahas noctem ut ascendant populi. Dedit autem predam domesticis suis, quando viris evangelicis domesticis fidei dedit ex vi communionis sanctorum populum conversum ad Christum, quem dyabolus ante captivavit, et dedit cibaria ancillis suis, quando christianis inferioribus esurientibus et sicientibus iusticiam dedit pastum legis domini et potum in complemento iusticie delectandi. Et sic de matre nostra verificata est doctrina matrone Anne, Tobie X°, [p. 480] ubi ducta est a parentibus honorare soceros, diligere maritum, regere familiam, gubernare domum et se ipsam irreprehensibilem exhibere. Nec moveat quod filii ecclesie sunt ancille, cum vir tocius ecclesie sit eius dominus; quod figuratum est in Sara Genesis XVIII°, 12, vocante Abraham dominum suum (ut notat beatus Petrus Iª Petri III°, 6). Non timeat, inquit Augustinus, condicionem, sed speret miseracionem, quia revera si Deo servire sit regnare, ancilla domini est regina. Et hinc vere ac meritorie profitetur Psalmista Psalmo CXV°, 16: Ego, inquit, servus tuus et filius ancille tue. Oportet enim membra ecclesie precipue cavere ocium et servire continue, quia aliter non datur eis spirituale cibarium. Unde IIª Thessal. III°, 10 dicit Apostolus: Qui non laborat non manducet.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 476.12: The office of the Church.
- 476.14: Verse 12. All the works of the predestinate are profitable to the Church.
- 477.26: Verse 13 specifies the work of the Church, in giving a law both for our outward and inward life.
- 478.4: Both laws require observance.
- 478.19: Verse 14. The Church is like a ship.
- 479.11: Verse 15. The Church gives the "prey" of converted peoples, and distributes ''a portion" of the law of God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 476: *Iusti* [R3]
  - 477: *IIª* [R3]
  - 477: *15* [R3]
  - 477: *10* [R3]
  - 479: *usque* [R3]
  - 479: *suis* (15 is the line number) [R4]
  - 479: *∅* (coordinator: joined/placed by OVERRIDE (part99)) [GAP]
  - 479: *non* [R3]
  - 479: *defecimus* [DEL]
  - 480: *Iª* [R3]
  - 480: *III°* [R4]
  - 480: *filius* [NW]
  - 480: *IIª* [R4]
  - 480: *III°* [R4]
  - 477: *specificat* (spe-/cificat; output holds both halves; 194ᶜ folio mark dropped) [OVERRIDE-MARK]
  - 479: *IIª* (citation printed "et non defecimus, IIª Corinth. IV°, 8" (agent 11); wrongly dropped as DEL) [OVERRIDE]
  - 479: *Corinth.* (as above) [OVERRIDE]
  - 479: *IV°, 8* (as above) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 476:
1. B: Quarto infert. 2. A A,: una deest. 5. In codd.: quia
querit. Corr. e textu' Aug., ubi sic habetur: Non quia non querit spolia,
ideo non indigebit, sed quia multis abundabit ... 12. A in marg. :
Secunda pars. i5. A A, : a deest. 17. continue; Aug. : in omni tempore.
20. A in marg. : Differencie inter peccatum presciti et predestinati.
22. B: Peccatum per accidens. 23. B: et secundum — tamen deest.
29. A A,: equivocatur — dampnabile deest.

p. 477:
(none)

p. 478:
1. B: carne deest. ibid: ad extra. 4. Aug. 1. c. Et sequencia ex
illo texto (mutatis aliquot verbis) deprompta sunt. lO. 17. B: moralem
et potenciam oportet enim et ideo. 26. B : habitatem. 3i. incodd.:
1. Aug. Quidquid carne operamur, in promptu est: quidquid
spiritu, in secreto.

p. 479:
6. Aug. mutatis verbis. 8. In codd.: CXXII.
22. 23. "Aporiamur sed non tlestituimur." Vulgate.

p. 480:
1. In codd.: socios. 16. A A,: matrona — idco deest.
;ic idem. 29. In codd.: Matth. V. 32. A: boni fuci?
```
