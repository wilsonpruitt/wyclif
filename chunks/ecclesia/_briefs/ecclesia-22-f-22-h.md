# Translation brief: ecclesia 22-f–22-h

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-22-f.md chunks/ecclesia/wyc-ecclesia-22-g.md chunks/ecclesia/wyc-ecclesia-22-h.md` once and fix what it reports.
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

## Glossary (the 210 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
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
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
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
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| cohabitacio | joint dwelling | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
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
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| cantaria | chantry | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | damnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| sacerdotes annales | annual priests | Priests hired to say masses for a year. Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |

---

## Chunk 22-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "535.3–538.13"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 6 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "755 words; 699 unanimous or majority-real; 51 settled by vote (R2 25, R3a 20, R3b 1, R5a 4, R6a 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n572–n575 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 6: [TITLE]

## ¶1 · 535.3–538.2

> [p. 535] Ad terciam confirmacionem negetur assumptum, cum multe oraciones tollunt mala de bestiis pro quibus non orant homines Deum suum. Ymmo si fiat oracio pro omnibus melioratis occasione illius, tunc oraciones sanctorum pro adventu Christi in carne fierent pro toto mundo, nedum pro omnibus bestiis et dampnatis, ymmo pro cunctis inanimatis et singulis creaturis. Omnia enim ista recipiunt perfeccionem et melioracionem, ymmo et ipsum peccatum virtute passionis Christi, et tamen theologi non tam extense loquuntur sicut nec scriptura sacra, ut dicant orandum esse pro talibus ut percipientibus fructum oracionis intentum, licet posset dici eos orare pro talibus tamquam per accidens consequentibus ad fructum per se intentum. Conceditur ergo quod dyabolus et omnes dampnati recipiunt quoddam bonum ex merito ecclesie; videtur tamen mihi quod non sit bonum eis expediens vel utile, sed bonum tollens eis fugibile; dampnacio enim tollit quodlibet bonum honestum et utile in dampnato. Conceditur tamen (ut tangitur in secundo commento mendacii) quod Deus misericorditer punit dampnatos. Et notat Augustinus XXI°, De Civitate Dei, cap. XXIV°. Sic enim secundum Augustinum Deus non continet in ira sua miseraciones suas eciam dampnatis, sed facit eos non tanta quanta digni sunt penarum atrocitate puniri, non ut eas penas vel nunquam subeant vel ante finiant, sed ut eas miciores quam merita sunt eorum levioresque paciantur; sic enim ira Dei manebit et in ipsa ira sua miseraciones [p. 536] suas non continebit. Sed quia dixit sacrum Psalmum intelligere de membris suis predestinatis in quibus peccatum est mutacio dextere excelsi, ideo prosequitur dicens: Hoc quidem non ideo confirmo, quoniam non resisto. Hoc autem utrobique detestatur iste sanctus cum aliis quod vel pena membrorum dyaboli pro instanti temporis finiatur, vel postquam fuit intensior per ecclesie suffragia remittatur, licet credi posset probabiliter quod omne peccatum est minus malum et minus punibile propter meritum Jesu Christi. Unde quia Augustinus, cap. XVII°, libri XXIⁱ, recitat quomodo quidam commendant istam sentenciam, quia pia, sed (ut arguit, cum non habet auctoritatem ex scriptura sed eius oppositum), tunc foret melior et verior, si misericordior. Extendatur ergo fons huius misericordie ad dampnatos quoslibet quod punientur pena solummodo temporali, vel dicatur misericordius quod pena illa erit brevissima, vel tercio misericordissime quod omnino non erit alia pena post mortem, sed tota scriptura est in ista parte conminatoria sed non vera. Si quis, inquit, audeat ista asserere, tanto invenitur errare deformius et contra recta Dei verba perversius, quanto videtur sentire sibi clemencius. Non seducat nos ergo ceca pietas que, cum sit veritati et fonti iusticie ac pietatis contraria, est blasphema impietas; nam per eius oppositum fides catholica integratur, conversacio militantis ecclesie timore pene melioratur et spes maioris beatitudinis confirmatur; et correspondenter illi qui videntur magis placere dyabolo magis nocent, et hinc indubie possunt expectare amplius nocumentum. Non ergo oramus pro dyabolo vel sibi [p. 537] proficimus quamvis per accidens facimus sibi bonum; nec valet fingere quod nulli christiani sencient istam penam, quia (ut dixi secundum sentenciam beati Gregorii) illi sunt pessimi. Unde Augustinus, XXI° De Civitate Dei, XXV° cap. dicit quod a sana doctrina foret nimis contrarium ut heresiarche qui receperunt in ecclesia baptismum, eucaristiam et alia carismata, post vero ingrate acucius impugnant ecclesiam quam alii infideles, quia non adeo sunt ingrati. Peior, inquit, est desertor fidei et ex desertore obpugnator eius effectus, quam ille qui non deseruit quam nunquam tenuit. Ex istis potest colligi alius sensus dictorum beati Augustini Enchiridion CX°, que ponuntur in decretis XIIIª, q. II. Tempus. Ponit enim primo quod in hoc meditulio temporis inter mortem hominis et diem iudicii contingit mereri vel iuvare spiritus defunctorum. Ponit secundo quod eis prosunt suffragia qui, cum viverent hec sibi ut postea possent prodesse meruerunt. Tercio dicit quod de quatuor generibus mortuorum merita superstitum sunt pro valde bonis graciarum acciones, pro mediocriter bonis propiciaciones, pro valde malis sunt vivencium consolaciones, sed mediocriter malis faciunt dampnaciones tollerabiliores, sic quod utrobique valent pie oraciones intente pro mortuis, quia beatis vertuntur in graciarum acciones, purgandis in propiciaciones, dampnatis vero licet non sint adiumenta, prosunt tamen ecclesie militanti et dampnatis qui [p. 538] superstites per bona opera meruerunt sunt causa quare micius puniuntur (ut tetigi ultimo capitulo libri Vᵗⁱ).

[ENGLISH]

## ¶2 · 538.3–538.13

> [p. 538] Ex istis potest colligi quantum mundus decipituro in elemosinis perpetuis et exequiis ac ritibus solempnibus mortuorum de perpetuacione elemosine; dictum est hoc cap. XVI° et XXII° cap. libri V. Ymmo cum debet esse certum catholico quod modus quo Christus fecit et fieri precepit elemosinas sit quocunque alio modo elemosinandi perfeccior, et est undiquaque facilior, patet quod non mediocriter peccant sed ex superbia et negligencia se accusant qui contempnunt sermonem Christi et adherent prudencie proprie et opinioni seculi. De exequiis vero et

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 535.3: Prayer may profit those for whose intention it was not made.
- 535.25: Augustine says that God punishes the damned mercifully,
- 536.5: but he abhorred the notion that there would be an end to the punishment of the damned.
- 537.1: Christians will be punished more severely than others.
- 538.3: We may see how the world is deceived,
- 538.8: as to perpetual alms,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 535: *ante* (print: ante finiant, ; finiant, was main pos 216 (iiniant), DEL-accepted) [R4]
  - 537: *sensus* (202a is the glued folio mark) [R4]
  - 537: *XIIIª* [R4]
  - 538: *Vᵗⁱ* (print: Vti). ; punctuation dropped per superscript rule) [R4]
  - 535: *finiant,* (print: ante finiant, (was DEL-accepted) (agent 12)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 535:
17. B: Qua ergo. 23. A in marg.: Huius contrarium habetur in
decalogo. 25. A in marg. : Augustinus. A: civitate cap. 3o. AA,:
antea finiant; in Augustino: aliquando.
2 5. Aug. Opp. tom VII, pag. 640.

p. 536:
12. A in marg. : Contra sentenciam que ponit nullum perpetue dampnari.
20. alia; A: aliter; A, : alicui; B: alie; Correxi. 23. B: contra recia.
24. B: sibi sor (sequitur lacuna).

p. 537:
4. A in marg.: Augustinus. In codd. cap. XXIV Correxi. 8. A:
inpungnant. i3. A A^: sensus doctorum. i3. A in marg.:
Augustinus. 22. Hic locus in decr. sic habelur: Cum sacriticia
altaris sive quarumcunque elemosinarum pro haptizatis omnibus offerunter,
pro valde bonis graciarum acciones sunt, pro non valde malis propicia-
ciones sunt, pro valde malis, eciamsi nulla sunt adiumenta mortuorum,
tamen vivorum consolaciones sunt. A in marg : Nota quomodo et qui-
bus mortuis prosunt suffragia (Abovc 202" witliout mark of reference).
11. pag. 646. 14 Decreti sec. pars, causa XIII, q. II,
c. XXIII.

p. 538:
4. A in marg.: Exequie pro mortuis quomodo prosunt et quomodo
nocent illis. 6. A A, : Dictum est hoc cap et 22. 17- B:
et neutra — unde deest.
29. Decr. sec. pars, causa XIII, q. II, cap. XIX.
```

---

## Chunk 22-g: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-g
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "538.14–542.18"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 7 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "918 words; 852 unanimous or majority-real; 51 settled by vote (R2 19, R3a 22, R5a 10); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n575–n579 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 7: [TITLE]

## ¶1 · 538.14–540.16

> [p. 538] aliis ritibus factis pro mortuis patet quod vel sunt purgandis COntraria vel neutra vel minus utilia; contraria si sapiunt peccatum, minus utilia si in istis omissis contraria magis profecerint, et neutra supposito quod neque sint bona neque mala moraliter. Primum et tercium fiunt communius, unde prima particula ex hoc patet quod, sicut omnia meritorie facta pro mortuis capacibus eis prosunt, sic omnia demeritoria pretensa pro ipsis fieri profectui suo obsunt; non enim prodest corpori mortuo talis solempnitas, cum deficiat sibi sensus, nec prodest anime nisi sub racione qua meritum; aliter enim foret profectui suo indifferens, sicut est indifferens utilitati dyaboli vel beati. Illud ergo suppono ut maximam, et patet per Augustinum inDeCura agenda pro mortuis, et ponitur in decretis XIIIª, q. IIª: Non estimemus, inquit, ad mortuos pro quibus curam agimus pervenire nisi quod pro eis sive altaris sive oracionis sive elemosinarum sacrificiis supplicamus. [p. 539] Et sequitur: Corpori autem humando quidquid inpenditur, non est presidium salutis sed humanitatis officium. Sed et idem videtur per se notorium considerando quomodo proveniret profectus corpori mortuo vel spiritui separato. Et ex isto sequitur vivorum stulticia qui magis dolent pro morte corporali quam pro morte anime per peccatum, magis solicitantur pro solempnitate exequiarum proximi vel amici quam pro assiduitate conversacionum meritoriarum per quas solum suffragia insunt sibi. Unde decretum beati Gregorii XIIIª q. IIª, Anime defunctorum. Curacio, inquit, funeris, condicio sepulture, pompa exequiarum magis sunt vivorum solacia quam subsidia mortuorum. Si aliquid prodest impio sepultura preciosa, oberit pio vilis aut nulla. Crisostomus super epistolam ad Hebreos, ut ibi exponitur: Ubicunque sepeliamur, domini est terra et plenitudo eius; secundum quod oportet fieri efficiatur. Lugere autem, deplorare et lamentari eos qui de hac vita decedunt ex pusillanimitate contingit. Hoc autem ex desperacione future resurreccionis intelligitur. Unde Apostolus non simpliciter ait: Nolumus vos ignorare de dormientibus, ut non contristemini, sed addit: Sicut et ceteri qui spem non habent. Et eadem sentencia patet in duobus capitulis sequentibus. Item, videtur quod murmur tale sit contra dominum quem debemus credere omnem hominem velle mori, sed voluntati Dei non est licitum taliter contrariare. Si enim scio quod est de Dei beneplacito et sic iustum, faciens ad ordinem [p. 540] et pulchritudinem universi quod Petrus nunc per dominum occidatur, quomodo licet mihi remurmurare contra istam iusticiam et pulchritudinem que adeo placet Deo. Unde XIIIª q. IIª sub auctoritate Cypriani sic scribitur: Quam preposterum est, quamque perversum, ut cum Dei voluntatem fieri postulemus, quando evocat nos et accersit de hoc mundo, non statim voluntatis eius imperio pareamus et pervicacium more servorum ad conspectum domini cum tristicia et merore perducimur, exeuntes isthinc necessitatis vinculo, non voluntatis obsequio, quomodo volumus ab eo premiis celestibus honorari ad quem venimus inviti. Preceptum est, inquit, a domino ut contester assidue et publice predicarem fratres non esse lugendos accersione divina de seculo liberatos, cum sciamus non amitti sed premitti, recedentes de seculo.

[ENGLISH]

## ¶2 · 540.17–542.18

> [p. 540] In isto dicto videtur innuere triplicem racionem: Prima ex hoc quod nemo debet orare sibi ipsi contrarie, sed oramus Deum: Fiat voluntas tua undique, ideo non debemus velle huic contrarie. Secunda racio est ex hoc quod oportet salvandum meritorie et per consequens voluntarie pati mortem. Tercia racio stat in isto quod diligens se vel alterum debet gaudenter acceptare accessum eius proprium, sicut est mors cuilibet salvando, et prescito eciam est ad bonum, cum continue plus nocet ecclesie et amplius demeretur. In oppositum sunt consuetudo et leges ecclesie de cura agenda pro mortuis et ecclesiastica sepultura, unde oblaciones Jude Machabei laudat ecclesia, Machabeorum XII°, et sepultura mortuorum computatur inter opera misericordie, pro [p. 541] quo laudatur Tobias Tobie. Unde decretum recitat Augustinus De Cura agenda pro mortuis sub hiis verbis: Quamvis cure pro mortuis non pro omnibus pro quibus fiunt prosint, sed hiis tantum pro quibus dum viverent ut prosint meruerant; sed quia non discernimus qui sint illi, oportet illa pro regeneratis omnibus facere. Et assignat causam eius triplicem: Prima est profectus mortuorum capacium, secunda est excitacio affectus superstitum, et tercia est naturalis instinctus et meritorius, dum fuerit caritate formatus curam talem agencium. Pro prima sic scribit: Melius enim supererunt ista hiis quibus nec obsunt nec prosunt, quam eis deerunt quibus prosunt. Vult dicere quod oportet intendere orare generaliter pro cunctis fidelibus, subintelligendo et Deo limitante suffragium capacibus. Pro secunda causa patet quod ex hoc excitatur devocio superstitum et provocatur occupacio circa actum meritorium. Unde Augustinus: Diligencius facit hoc quisque pro amicis suis, ut pro illo fiat similiter. Et quoad terciam causam patet, cum necesse sit evacuare cadavera bestiarum, multo magis cadavera hominum, magis carorum et plus inficiencium. Unde Augustinus: Humanitatis, inquit, hoc est officium secundum affectum quo nemo unquam carnem suam odio habet. Unde oportet ut quam potest pro carne proximi curam gerat, cum spiritus inde recesserit qui hoc gerebat. Et si hoc faciunt qui carnis resurreccionem non credunt, quanto magis [p. 542] debent facere qui credunt ut corpori resurrecturo et eternaliter mansuro impensum officium sit quodammodo evidens eiusdem fidei testimonium. Et patet cum talis operacio non sit per se virtuosa, sed valde per accidens quod contingit eam nunc bene nunc male fieri. Cavere autem debemus de malicia ne fastui seculi principaliter intendamus, nec magis necessarium omittamus; nichil enim est magis necessarium obsequium agendum pro mortuis quam vivere virtuose. Ille ergo inordinate agit curam corporalem pro suo mortuo qui plus attendit ad illam quam ad superhabundanciam virtutis in animo. Vis ergo affectuose proficere anime defunctorum, exercita te ipsum in scola virtutum; quod quanto plus feceris, tanto cum paribus facis mortuis plus profectum; oportet ergo iuxta caritatis regulas quod superstes misereatur anime proprie placens Deo, et ad illud consequitur efficacissime suffragium mortuorum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 538.14: and as to funeral ceremonies.
- 538.21: False works injure the dead as good works profit them.
- 539.6: Hence the folly of those who care more for solemn rites than true prayers.
- 540.5: Cyprian tells us that we ought not to mourn for those who have gone before.
- 540.26: Yet the Church teaches us to care for the dead,
- 541.13: and to pray for all the faithful.
- 542.3: Burial of the dead may be done in a wrong way,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 538: *et* (print: vero / et aliis ritibus) [INS?]
  - 538: *XIIIª* [R4]
  - 538: *IIª* [R4]
  - 539: *XIIIª* (coordinator: XIIIª split X|111|a; 73-74 were DEL (agent 12)) [R4]
  - 539: *IIª* [R3]
  - 540: *XIIIª* (coordinator: XIIIª split XII|Iª (agent 12)) [R3]
  - 540: *∅* (coordinator: joined at 23 (agent 12)) [DEL]
  - 540: *IIª* [R4]
  - 540: *racionem:* (margin letter Q follows) [R4]
  - 541: *quo* (202b is the glued folio mark) [THIN]
  - 541: *∅* (previous page's closing text at page top; laudatur already at pos 1) [INS?]
  - 542: *debent* [THIN]
  - 540: *XII°,* [OVERRIDE-VERSE]
  - 539: *∅* (joined at 72 (agent 12)) [OVERRIDE]
  - 539: *∅* (joined at 72 (agent 12)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 538:
4. A in marg.: Exequie pro mortuis quomodo prosunt et quomodo
nocent illis. 6. A A, : Dictum est hoc cap et 22. 17- B:
et neutra — unde deest.
29. Decr. sec. pars, causa XIII, q. II, cap. XIX.

p. 539:
2. A A,: liumanitatis — corpori deest. 6. A in marg. : Correlarium.
II. Codd.: XII». i3. A: pompe. ly. B: efficaciter. 29. B:
1 1. Decr. sec. pars, causaXIII, q. II, cap. XXII. 1 2—16. Cura-
cio — nulla is a quotation from Augustine De Cura agenda pro
mortuis Cap. II. 17. ibid. cap. XXVI. 23. Cap. XXVII.
Habent forsitan and XXVIII. Qui divina.

p. 540:
7. A: accerscit: scil. Deus ut habet decret. II. In decretali: et
volumus. i3. In decr. preceptum cst ut contestarer assidue ut.
16. In decret.: recedentes precedere ... 19. A B in marg. : Nota
contra lugentes mortuos. 3o. A: XII. deest.
4. Cap. XXV.

p. 541:
i. Num. cap. deest in codd. 3. A: quamvis cura .... prosunt.
4. In decret. : Quibus dum vivunt cooperantur ut prosint. (i. A A,:
decemimus; B: decrevimus ; in codd.: qui sunt. 18. A in marg. :
Augustinus. 24. A in marg. : Nota pro sepultura proximi si et
quomodo obligamur.
3. Decreti sec. pars, causa XIII, q. II, cap. XIX et Aug.
in libro De Agenda Cura pro mortuis cap. XVIII. Opp. tom. VI,
pag. 53o.

p. 542:
i3. A in marg. : Nota efficacissimum suffragium mortuorum. 20. A in
marg.: Nota pro exequiis et sepultura circa ecclesias. 25. B: salu-
briter dimittitur. 28. diligentiaeque persolvitur in decret.
23. Decret. sec. pars, causa XIII, q. II, cap. XXII.
```

---

## Chunk 22-h: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-22-h.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-22-h
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "542.20–548.35"
divisions: "cap. 22 (heading 'CAP. XXII.' at 517.27); part 8 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1455 words; 1350 unanimous or majority-real; 94 settled by vote (R2 53, R3a 32, R3b 1, R5a 7, R6a 1); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n579–n585 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 22, part 8: [TITLE]

## ¶1 · 542.20–548.35

> [p. 542] Ad primum obiectum patet quod beatus Gregorius intendit quod talia obsequia non prosunt mortuis nisi forte per accidens. Unde sequitur in textu Gregorii: Nec ideo tamen contempnenda et abicienda sunt corpora defunctorum maximeque iustorum, ex quo illud salubriter discitur quanta possit esse remuneracio pro elemosinis; quas viventibus et sencientibus exibemus, sed neque hoc apud Deum perit quod ex animis hominum membris officii diligencia persolvatur. Ex quo videtur quod racione elemosine prosunt defunctis talia obsequia, et obsunt eis de quanto excitant affectantes ad affectandum splendenciam in mundi gloria, accusantque mortuos, de [p. 543] quanto ostendunt illos affectos ad secularia desideria. Et quoad dictum Crisostomi, patet quod ipse intendit istam eandem sentenciam, unde sequitur in textu suo: Pietatis namque affectu et humanitatis intuitu mortuos lugere non prohibemur, sicut nonnullos sanctorum aliorum exequiis legimus pias lacrimas impendisse. Unde quod quis sepelitur iuxta martirem in ecclesia vel ubicunque solempniter, nunc obest et nunc prodest, sed tantum per accidens obest, si accumulant peccata originata ex mortuo decedente in mortali. Prodest, si sit occasio diligencius orandi pro mortuo in gracia decedente, unde decretum (ubi supra) sub auctoritate sanctorum Augustini et Gregorii sic loquitur: Quibus peccata dimissa non sunt, a sacris locis post mortem adiuvari non possunt, quia quos peccata graviora deprimunt, si in sacris locis sepeliri se faciunt, restat ut de sua presumpcione iudicentur, quia eos sacra loca non liberant, sed culpa temeritatis accusat. Et quoad secundum partem sequitur decretum beati Gregorii: Cum gravia peccata dimissa sunt et non deprimunt, tunc prodest mortuis si in ecclesia sepeliantur, quia eorum proximi, quociens ad eadem loca veniunt, suorum quoque sepulturam aspiciunt, recordantur et pro eis domino preces fundunt. Nam quos peccata gravia deprimunt, ad maiorem cumulum dampnacionis pocius quam absolucionem eorum corpora in ecclesiis reponuntur. Quantum ad racionem terciam, quomodocunque glossamus, non dubium quin murmuraciones plurime pro mortuis sunt inique; [p. 544] dicitur enim quod alius est amor vel affeccio naturalis, quali Christus voluit vivere et non mori, cum Matthei XXVI° dicit: Verumptamen non sicut ego volo, sed sicut tu vis. Et tali affeccione naturali doluit mater eius pro morte filii naturalis. Nec evidens quod in hoc peccavit, sicut nec Christus, quando pro Lazaro ploravit. Alia autem est affeccio deliberativa qua non est dolendum sed gaudendum de mortibus propinquorum. Sic enim Christus, sic Paulus et ceteri martires gaudebant de pena et morte propria, et sic oportet omnem salvandum gaudere. Ideo necessarium est christianis discere quomodo debent mori; quando ergo quis plus dolet propter amissionem boni utilis vel boni delectabilis temporalis in morte proximi quam propter amissionem boni utilis anime defuncti et utilitatis ecclesie, tunc peccat indubie plus vel minus, sicut ille peccat gravius qui propter amissionem amoris quem habet ad seculum dolet de morte propria. Et patet quod debemus secundum racionem superare impetum anime naturalem, sicut est mihi verisimile quod mater domini mitigavit ex integro, et Christus non directe ploravit pro morte Lazari quem necessitavit ad gloriam suam mori, sed doluit pro peccato humani generis, pro quo oportuit talia et tot pati. Unde ex concilio Toletano Qui divina sic scribitur: Prohibet nos sanctus Apostolus dicens: De dormientibus nolo vos contristari sicut et ceteri qui spem non habent. Et dominus Joh. XI° non flevit Lazarum mortuum, sed ad huius vite erumpnas ploravit resuscitandum. Si autem potest hoc episcopus omnibus christianis prohibere, non moretur. [p. 545] Ex istis colligo conclusionem triplicem mihi notabilem: Prima quomodo ista sentencia est a prepositis populo predicanda, eo quod instruit eum in moribus, evacuat errorem fidei et precipitur ab ecclesia fieri. Quod si multiplicamus leges de sepulturis et eas solempnizamus atque pro porcionibus et substancia defuncti contendimus et illud cum aliis suffragiis defunctorum omittimus, quis dubitat quin Deus huius seculi usque ad infidelitatem cecavit oculos mentis nostre? Et cum in vigilia Pentecostes post communionem concinimus quod Deus per os omnium prophetarum docuit nos temporalia relinquere, et alibi cantantes oramus ut Deus doceat nos terrena despicere, quia certum est quod spiritus sanctus effugit cohabitare cum spiritu hominis sic affeccione temporalium deturpato. Ad probandum autem si sumus huiusmodi, sollicitudines nostre cum actibus sequentibus iudicabunt. Nam pater spiritualis qui animo preponderat oracionis suffragia et elemosinas providas faciendas pro mortuis plus quam lucri temporalis commoda, manifeste demonstrat quod plus amat temporalia defuncti quam anime sue spirituale suffragium. Secunda conclusio: Nullus ritus ecclesie ab eius capite approbatus de suffragiis vel memoriis faciendis pro mortuis repugnat sentencie supradicte. Patet ex hoc quod nulla veritas repugnat veritati. Procuret ergo homo, quantum prudenter sufficit, per se vel alium, remedium animarum in purgatorio oblacionibus vel stipendiis annalibus sacerdotum aut precibus sanctorum, aut carorum elemosinis aut ieiunio cognatorum et secundum supradictam Dei sentenciam approbatur. [p. 546] Et hiis quatuor modis secundum decretum beati Gregorii, XIIIª q. II, Anime defunctorum, contingit animabus in purgatorio suffragari, ymmo (ut sepe dixi) per omnem vitam vel operam meritoriam viatoris. Unde ritus quem approbat beatus Ambrosius in De Officiis, positus in conclusione predicta, plurimum est laudandus. Quia, inquit, alii tercium diem, alii septimum diem, alii tricesimum, alii quadragesimum observare consueverunt in officiis mortuorum, quid doceat leccio consideremus. Defuncto quidem Jacob precipit Joseph pueris suis ut sepelirent eum et sepelierunt sepultores Israel, et completi sunt quadraginta dies luctus, ut patet Genesis L°. Sed eciam in Deuteronomio, capitulo ultimo, et Numeri XX scriptum est: Quia planxerunt filii Israel Moysen triginta diebus et consummati sunt dies luctus. Illi autem qui servant diem tercium respiciunt trinitatem vel triduum resurreccionis Christi; qui autem observant septimum observant perpetuam quietem anime, que est tercia cum copulacione corporis, quod est quatuor; ex quibus autem constant septem; qui autem observant trigenarium considerant quomodo ex duobus quindenariis secundum corpus et animam ille constat, quindenarius autem resultat ex septenario patrum legis veteris et octonario legis nove: Nam hos duos numeros quadam proprietate colunt specialiter isti patres. Qui autem observant quadrigenarium expectant fructum resurreccionis per mortem Christi qui totidem horis dicitur fuisse mortuus, licet arca triginta sex horas iacuit in sepulcro, et sic de quinquagenario, centenario vel anniversario secundum racionem cui devocio populi est affecta. [p. 547] Omnes enim affectant suis mortuis beatitudinem circularem, ut notat Hostiensis in Summa (ubi supra). V Tercia conclusio: Dimissis istis ritibus foret purgandis animabus utilius, populo superstite dante sollicitudinem et operam ex integro ad virtutes. Patet ex hoc quod ista variacio rituum fuit omissa a Christo et suis apostolis; ymmo precepit Matthei VIII°, 22: Dimitte mortuos sepelire mortuos suos et in moribus sequi ipsum. Ista autem variacio introducit sectas et gildas et consequenter errores multiplices, mundialibus infideliter opinantibus quod proporcionaliter habent ipsi suffragia singulariter a se ipsis et beatis in patria, sicut ipsi coniunguntur federe temporali, et sic credunt de suis mortuis quoad ipsa suffragia que impendunt. Illud autem improbatum est hic et capitulo ultimo libri quinti. Omnes enim predestinati vivi vel mortui citra beatitudinem constituti participant suffragiis utriusque ecclesie precise secundum quod digni sunt meritis quoad Deum. Tales ergo lige superfluunt et periculose seminant dogma falsum sepeque gignunt sedicionem in populo. Nec moveat quod sepe bonum ex ipsis evenit, quia Deus non sineret dyabolos vel aliud nefandum collegium congregari, nisi exinde disponeret utilitatem ecclesie provenire. Et sic dicitur de sepulcris et aliis construccionibus sumptuosis quod bonum exinde evenit, ut puta, devocio confluencium, sustentacio egenorum et multa bona similia; malum eciam communius, ut puta, distraccio et ocium sensus hominis dissoluti et inordinata conglobacio tam temporalium quam eciam personarum, et difficile foret iudicare quid istorum foret matri nostre utilius, si facta et dicta Christi et [p. 548] apostolorum suorum non darent fidem de inutilitate fundamenti. Non enim est causa evidens: Si Symon, summus sacerdos construxit sibi et suis edificium altum super sepulchrum eorum et mirabiliter sumptuosum (ut patet I Macchabeorum XIII°), ergo bene, sicut est evidens: Si Christus et eius apostoli illud omiserant, ergo bene; nam regimen illorum sacerdotum fuit presagium destruccionis synagoge que fuit ecclesia Judeorum; et fundamentum aliud cum suis domesticis fuit indefectivum principium perpetue ecclesie christiane; nichil ergo valet nobis fidelibus nisi de quanto fuerit fundabile ex lege Christi; sed cum ex lege Christi et lege ecclesie patet quod observancie de quanto plus accedunt ad statum innocencie et minus intricantur cum mundo, imitantes voluntatem Dei, direccius preponderantes in amore bonum communius, patet quod observancia opposita ritui quem mundus in istis exigit est ipso melior. Unde (ut tetigi) talia memorialia post mortuos derelicta vel nocent eis vel minus eis proficiunt quam purgandis pauperibus in gracia ampliori, ymmo minus quam ceteris paribus eorum destruccio. Si enim tales mortui sunt presciti, tunc talia memorialia derelicta sunt fructus peccati sui in spiritum sanctum; si sunt predestinati, tunc sunt fructus sue affeccionis proprietarie expurgande, et indubie pauper decedens in maiori gracia, cum melius usus fuit temporalibus istis quibus verius dominatus est, plus participabit in purgatorio eorum fructu, dominio devoluto ab utroque ad dominum, aput quem non potest esse accepcio personarum. Quomodo excusatur peccatum quo propter affeccionem mundialem vel affeccionem proprietariam carnalem ritus talis preponitur et modus faciendi exproprietarie vivencium, et bonum communius plus diligencium stulte postponitur?

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 542.29: as by too much care for show.
- 543.7: Solemn burial in holy places may do good or harm.
- 544.1: As to grief for the dead we must distinguish between natural affection and deliberate judgment.
- 544.19: Natural grief should be controlled by reason.
- 545.2: 1. The clergy should thus teach about funeral rites.
- 545.18: They must not let the desire of gain outweigh the desire to benefit souls.
- 545.23: 2. All rites approved by the Church agree with this rule.
- 546.6: Reasons for various observances.
- 547.3: 3. It would be better to aim wholly at a virtuous life and give up these ceremonies,
- 547.10: which bring in gilds and other causes of mischief.
- 548.2: The example of Simon Maccabeus cannot outweigh that of Christ.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 542: *Gregorius* (a is a margin letter) [R4]
  - 544: *Verumptamen* [R4]
  - 544: *ego* [R3]
  - 545: *animo* (203a is the glued folio mark) [R4]
  - 546: *XIIIª* (coordinator: XIIIª split XI|IIª (agent 12)) [R3]
  - 546: *∅* (coordinator: joined at 8 (agent 12)) [R4]
  - 546: *plurimum* [NW]
  - 546: *alii* [R3]
  - 547: *purgandis* (main token holds whole word (pur- / gandis)) [R4]
  - 547: *lige* [NW]
  - 548: *edificium* [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 542:
i3. A in marg. : Nota efficacissimum suffragium mortuorum. 20. A in
marg.: Nota pro exequiis et sepultura circa ecclesias. 25. B: salu-
briter dimittitur. 28. diligentiaeque persolvitur in decret.
23. Decret. sec. pars, causa XIII, q. II, cap. XXII.

p. 543:
5. A A,: nonnullorum. 7. A: sp sepelitur. A,: semper sepelitur.
Errorem scribentis A imitatus cst A,. 18. In decret. : qtioniam eos.
22. ibid.: in ecclesiis. 28. A in marg. : Nota quomodo licet de-
plangere (superscriptum est: flere scil. deflere) mortuum et quomodo
3. Causa XIII, q. II, cap. XXVI. i3. Causa XIII, q. II,
capp. XVI and XVII.

p. 544:
1. A: quod aliquis. n. A: et sicut. 22. A B in raarg.: Nota
de fletu Christi. 23. 24. A: nunciavit ad gloriam. 3i. agere
non moretur in decret.
26. Causa XIII, q. II, cap. XXVIII.

p. 545:
i. A in marg. : Contra avariciam cleri. 1'rima conclusio. 23. A in
marg. : Sccunda conclusio. De variis ritibus approbatis in suflragiis ct
memoriis mortuorum.
6. porcio i. e. pensio annua.

p. 546:
5. A in marg.: Ambrosius. 12. A B: sepultores deest; luctus ut
patet Gen. L deest in decret. i5. cap. ult. et Num. XX deest in
2. Decr. sec. pars, Causa XIII, q. II, cap. XXII Animae dc-
/nnctorum and cap. XXIV Qiiia alii.

p. 547:
3. A in marg.: Tercia conclusio. Contra ritus supra positos.
7. Matth. VIII, 22: Sequere me et dimitte ... i3. B: lidere.
iG. A in marg.: De solcmpni sepultura ct sumptuosis sepulcris (Above
2o3b wilhout mark of rcfcrcnce). iR. precise; A: p" ; A,: pe.

p. 548:
2. B : tam evidens. 5. B : ergo — omiserant deest. 7. B:regnum
illorum fuit. 12. ex deest in codd. 26. B: expurgande — fuit deest.
```
