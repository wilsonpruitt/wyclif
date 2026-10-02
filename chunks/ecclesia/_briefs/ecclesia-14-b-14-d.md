# Translation brief: ecclesia 14-b–14-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-14-b.md chunks/ecclesia/wyc-ecclesia-14-c.md chunks/ecclesia/wyc-ecclesia-14-d.md` once and fix what it reports.
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

## Glossary (the 176 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |
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
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Ruled 2026-10-02 (*Eccl.* 13). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
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
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "one given alms". Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |

---

## Chunk 14-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "302.3–306.14"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1094 words; 971 unanimous or majority-real; 108 settled by vote (R2 53, R3a 49, R3b 1, R5a 4, R6a 1); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n339–n343 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 2: [TITLE]

## ¶1 · 302.3–305.28

> [p. 302] Ideo (ut sepe diffuse exposui) Christus non potuit dominari civiliter, quomodo ergo doceret servos imitatores precipuos taliter dominari? Nonne dicit Apostolus, IIª Corinthiorum, VIII°, 9, quod pro nobis inops et egenus factus est? — Nonne recitat apostolus Thymotheo suo coepiscopo I, Tim. VI°, 8: Habentes, inquit, alimenta et quibus tegamur hiis contenti simus? Si ergo sit blasphemia imponere Christo quod sibi non potest conpetere, et (ut sepe ostendit dominus Ardmacanus) non potest competere Christo dominacio civilis, cum trahit secum de natura rei peccatum veniale, qua fronte presumeret fidelis imponere redemptori suo istam blasphemiam, specialiter cum nec ex scriptura veteris testamenti nec novi sit fundabilis talis dominacio cleri Christi? Si enim sit fundabilis dicas ubi? Et cum non sit contradiccio in scriptura sacra, oportet tollere leges veteris testamenti et novi que sonant in oppositum, ut patet de illis legibus allegatis hic et proximo capitulo. Ymmo cum leges ut plus necessarie sunt in scriptura sacra clarius expressate (ut patet IV°, De Doctrina Christiana), magnum defectum imponeret sic opinans auctori scripture quod nullibi exprimit dominacionem illam tam necessariam sue ecclesie. Item, Christus non potuit dominari civiliter secundum deitatem nec secundum humanitatem, ergo non potuit dominari civiliter quoad deitatem. Non est dubium fideli, cum secundum illam non potest esse activus viator proprietarius vel pars populi nec secundum suam humanitatem, sive solus fuerit homo, sive in puro statu innocencie cum toto suo genere, sive post lapsum ipso posito capite ecclesie ut est modo, duobus modis prioribus non foret civilitas, nec tercio modo foret ipse tam proprietarius. Pro cuius [p. 303] declaracione suppono dictum beati Gregorii, XXXIII° Moralium, cap° primo, super illo Job XIX°, 25: Scio quod redemptor meus vivit. Sciendum, inquit, est quod redemptor unam personam se cum sua ecclesia quam assumpsit exibuit; de ipso enim dicitur: Qui est caput Christus. Rursumque de eius ecclesia scriptum est: Et corpus Christi quod est ecclesia. Et sequitur quod Christum et ecclesiam unam personam credimus, hoc eciam unius persone actibus signari videamus. Ista fide supposita arguo sic: Non est possibile quod Christus, sponsus ecclesie, faciat vel habeat quicquam humanitus nisi secundum communicacionem tocius sue ecclesie, quia aliter esset sponsus ingratus sponse sue, cum sit personaliter sibi ydemptificatus, sed quelibet tanta communicacio excludet proprietatem civilem; ergo non est possibile quod Christus sponsus ecclesie vivat secundum proprietatem civilem. Et hec est racio quare Christus amavit bona communia et Apostolus tantum reprobat eos qui querunt que sua sunt. Unde Christus nunquam comedit, dormivit vel quomodolibet se habuit humanitus, nisi prius intendendo profectum tocius ecclesie militantis, dormientis et triumphantis, eciam plus quam profectum proprium sue humanitatis. Sed quis diceret personam hominis ut sic proprietarium civilem? Et istum articulum fidei ignorarunt primo apostoli, quando dixerunt: Magister manduca, et ille: Ego cibum habeo manducare quem vos nescitis, Johannis IV°, 31, 32. Et super ista racione fundata est primeva apostolorum religio, vivendo exproprietarie, postposita vita et occupacione seculari vel civili. Item, supposita veritate opinionis predicte, sequitur cum veris quod Constantinus post dotacionem ecclesie remansit hereticus sicut et omnes succedentes domini seculares; quod repugnat approbacioni ecclesie. Et [p. 304] consequencia probatur, supponendo tamquam datum falsigraphi quod de iure debetur pape, Christi vicario et clero suo tota civilis dominacio huius mundi. Et arguo sic: Ad hoc quod debitor vel iniuste aliena detinens sit absolutus quoad Deum, oportet quod plene satisfaciat, sed sic non fecit Constantinus, cum medietatem imperii sibi retinuit. Cum ergo illa medietas fuit tantum debita sicut medietas occidua restituta, videtur quod remansit in debito sicut prius, nam secundum Augustinum, Epistola XXXVII non dimittitur peccatum nisi restituatur ablatum. Unde (sicut dixi in materia De Privilegiis) Deus non potest remittere vel licenciare debitorem, ne satisfaciat, et hinc dixi periculosum esse quod quis auctorizet vel foveat sufficientem fugitivum, ne solvat creditori debitum corporale, dicente Augustino in supradicta epistola ad Macedonium: Illud, inquit, fidentissime dixerim, eum qui pro homine ad hoc intervenit, ne mala oblata restituat, et qui ad se fugientem, quantum honeste potest, ad restituendum non compellit, socium esse fraudis et criminis. Numquid credimus prepositum loci refugii posse honeste compellere fugitivum sufficientem, ut vel exeat locum tamquam eius violator, vel quod satisfaciat secundum quantitatem apportati vel sufficienciam fugitivi? Illa enim foret honestas legi Dei consona, sed applausus movens ad detencionem iniustam, et specialiter gracia participii foret diabolica facesia. Ideo (ut sepe dixi) vel oportet negare fidem scripture, racionem et sanctos doctores, vel dicere quod talis defensio sapit hereticam pravitatem. Et idem videtur supposita opinione predicta de dominio cleri Christi; cum enim taciturnitas [p. 305] huius sit consensus, consensus autem talis est cum facilitate eque dampnabilis, videtur quod sic opinantes, ex hoc quod sic tacent dicere ius suum et iniuriam in qua dampnabiliter indurantur domini temporales, peccant mortaliter. Nec valet eis fingere quod beatus Silvester remisit Constantino residuum, quia (ut ista secta credit tamquam principium) non licet Christi vicario vel clero suo vel alienare vel cedere iuri patrimonii crucifixi, sic videlicet quod tam illud quam sibi equivalens sit simpliciter extra possessionem civilem cleri Christi. Item, nec est privilegium nec dos nec possess adquisita Christi vicario nisi pro qua caput Christus fuerat crucifixus, sed Christus non fuit tanta passus pro dotacione civili vel seculari sue ecclesie clericorum, ergo talis dotacio vel dominacio civilis non est pure clero Christi conveniens. Assumptum patet ex hoc quod Christus meruit humano generi totam graciam et omnia ad ipsam consequencia que haberet, sed iuxta alibi dicta sine gracia et caritate non est simpliciter iusta possessio; ergo nec dos nec privilegium inest clero Christi, nisi quod Christus sibi meruit paciendo; nec credo fidelem contradicere huic sentencie: nam omnes patres veteris testamenti, omnes gentiles post et ante qui vel erant iustificati vel salvati, hoc obtinuerant merito fidei et passionis Christi, cum aliter fuissent dampnati nec unquam ab originali peccato purgati et per consequens nunquam iustificati moraliter.

[ENGLISH]

## ¶2 · 305.29–306.14

> [p. 305] Nec dubium theologo qui noscit quomodo homo intendit, meretur vel emit aliqua principaliter et aliqua secundarie, accessorie vel confuse, quin Christus, sicut passus est pro redempcione tocius ecclesie, sic et pro redempcione cuiuslibet membri sui et pro quolibet bono sibi utili ad hunc finem. Si enim dicimus [p. 306] quod iustus amat omnia, quod sacerdos rite excommunicat pro decimis et quod homo emendo equum emat quamlibet partem eius emibilem, Christus ergo omnisciens emendo a patre totum genus humanum emit accessorie omne bonum sibi utile vel privilegium citra Christum. Sic enim dicit Apostolus, Romanorum VIII°, 32, quod proprio filio Deus non pepercit, sed pro nobis omnibus tradidit illum: quomodo ergo non cum ipso omnia nobis donavit? Ideo audenter assero quod vel dominacio cleri moderni est illicita, vel non licet excommunicare pro decimis, vel Christus crucifixus est pro dominacione illa sue ecclesie adquirenda; nec aliter est presumibile quod sponsa Christi vocaret dotem cesaream patrimonium crucifixi.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 302.3: If Christ could not rule civilly, how can his servants do so?
- 302.26: Christ could not rule either in his godhead or his manhood: not as to his godhead, which cannot be involved in active life;
- 303.1: not as to his manhood, since he is one with his spouse, the Church, with whom all would be shared.
- 303.32: If the prelates are right, Constantine and all later emperors were heretics,
- 304.4: since they only handed over a part of what was due and kept back the rest.
- 305.1: and the Popes have by consent shared in their sin.
- 305.11: Christ did not die for worldly gain, but all the clergy receive from him was won by his passion;
- 306.9: so unless civil rule was the object of his crucifixion the clergy have not received it.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 302: *civiliter* [R4]
  - 302: *IIª* [R4]
  - 302: *Thymotheo* (Thy-/motheo; main token holds whole word; print has y) [R4]
  - 303: *Scio* (italic Scio; side-note text follows) [R4]
  - 303: *quam* (5 is the line number) [R4]
  - 304: *∅* (only is the English side-note) [NW]
  - 305: *huius sit* (main token covers 171d huius sit; folio mark dropped) [R3]
  - 305: *accessorie* [NW]
  - 306: *∅* (print ex-/communicat; main already holds excommunicat whole at pos 7) [INS?]
  - 306: *accessorie* [NW]
  - 306: *Deus* [R3]
  - 306: *cleri* [R3]
  - 306: *illicita* [R4]
  - 303: *ecclesie* [THIN]
  - 303: *XIX°, 25:* (print has verse 25 followed by colon) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 302:
8. A:adTim. 27. A: deitatem deitatem ; A, : divinitatem dcitatem.

p. 303:
2. A in marg. : Christus et sua ecelesia sunt una persona.

p. 304:
8. A A,: fuit — medietas: deest. 10. A in marg. : Augtistinus.
28. A: facessia. A in marg. : Tcnentur male ablata restitui (Above 171*
without mark of reference).
10. Epistola (CLIII) ad Macedonium Opp. tom. II, pag. 532.

p. 305:
16. A B in marg. : Nota pro quibus Christns passus est. 27. 28. li:
iustilicati mortaliter.

p. 306:
9. A in marg.: Conclusio. Christus non ad hoc est passus, ut acquirat
dominia clero (Above 172" withont mark of refcrence). i5. A B in
```

---

## Chunk 14-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "306.15–310.29"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1039 words; 950 unanimous or majority-real; 76 settled by vote (R2 44, R3a 29, R3b 1, R5a 1, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n343–n347 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 3: [TITLE]

## ¶1 · 306.15–307.2

> [p. 306] Nec valet fingere quod dominacio illa non sit privilegium sed lex communis, quia est lex privata diu post fundacionem ecclesie Christi concessa singulariter clero suo. Ideo patet ex descripcione privilegii quod sit sibi privilegium notabile pro hac vita. Sic enim purgacio mortuorum est privilegium sancte ecclesie quam tamen multi non appetunt. Minor autem argumenti sic ostenditur: Non fuit in Christo falsitas, dolus sive duplicitas, cum secundum Apostolum, II Corinth. 1°, 18, non fuit in ipso Est et non, sed fuisset cum paribus, si fuisset crucifixus, ut post clericatum sui imitatores seculariter dominentur. Ergo hoc non intenderat paciendo; ipse enim non potuit dominari seculariter sed vixit pauperem vitam summe exproprietarie; quod et docuit suos precipuos apostolos quos voluit esse exemplaria imitanda future ecclesie. Ipsis enim dixit quod haberent nolicionem possidendi aurum vel argentum, quod non diligerent mundum nec mundialia, sed quod omnino relinquerent cuncta [p. 307] que possident et tollentes crucem sequantur eum (ut patet Matthei X°, Luce XIV° et sepe alibi in evangelio).

[ENGLISH]

## ¶2 · 307.3–307.33

> [p. 307] Cum ergo in facto movit apostolos suos ad facto et conversacione interpretandum hec mandata secundum vitam exproprietariam et penalem, nec unquam innuit eis dominacionem civilem, fuisset nimis magnus seductor, si cum istis paribus dominacionem civilem pro statu cleri moderni intendebat ipsis adicere. Nam capitalibus exemplaribus in quibus dedit nobis potestatem et regulam vivendi precipit et monuit exemplando oppositum, nec est credibile quod desereret clerum suum, tacens omnino necessarium ad conversacionem ipsorum secundum suum beneplacitum regulandam; tunc enim fuisset omnino negligens et subdolus, sic quod omnes defectus nostros possemus in suam negligenciam racionabiliter retorquere; quod cum sit nefas dicere, credamus ex fide scripture et testimonio sanctorum doctorum quod in apostolis docuit totum genus cleri sequentis vivere pure exproprietarie de elemosinis corporalibus laicorum et pro mutuo nexu caritatis habendo, non minus obligavit clerum suum ad retribucionem elemosine spiritualis, sic quod clerici sint necessariores et digniores in ecclesia quam econtra, et plus indigent seculares clericis quam econtra, sicut spiritualis elemosina est prestancior corporali, et sic oportet quod laici mendicent elemosinas spirituales a clericis ad quarum retribucionem clerici amplius obligantur, sicut oportet ut clerici mendicent elemosinas corporales a laicis ad quarum re tribucionem multum valde sed non adeo laici sunt astricti, nec graviter feramus maioritatem obligacionis huiusmodi, quia hoc redundat in excellenciam clericorum.

[ENGLISH]

## ¶3 · 308.1–309.7

> [p. 308] Christus enim est plus obligatus creature sue quam econtra, cum ex lege sua eterna et titulo gracie prevenientis constituit se debitorem suis servis fidelibus, non ut solum daret eis bonum aliquod temporale, sed ut daret eis se ipsum in premium sempiternum, tantum autem non potest creatura beata domino obligari, et sic tenetur sacerdos rependere subditis spirituales elemosinas. Ideo (ut dixi proximo capitulo) deficiens a satisfaccione illius debiti gravius excommunicatur a domino, et per consequens periculosius cadit in heresim in tantum quod, si Deus per impossibile deficeret a debito ad quod se obligavit, graciose promittendo et meritum proficiendo, ipse foret summus hereticus. Nec feramus graviter quod quantumcunque nobiles quoad mundum ad tantum se humilient pro Christo quod deveniant elemosinarii pauperum subditorum, tum quia Christus nobilissimus recepit ad sui egenciam relevandam tam a viris secularibus quam a devotis feminis elemosinas corporales, tum eciam quia ex tali humiliacione et ministerii complecione crescit prepositi maioritas quoad Deum. be Sic ergo non est quoad hoc distinccio inter fratres, inter possessionatos et inter curatos, viventes de decimis et oblacionibus, quin omnes debemus vivere expropnetane de elemosinis laicorum et omnes debemus esse procuratores, non civiles possessores bonorum pauperum, iuxta preceptum Christi Matthei X°, nec potest conventualis conversacio vel solitaria aut prelacia maior vel minor tollere hoc debitum, sed omnes tenemur esse fideles dispensatores thesauri spiritualis vel corporalis domini secundum-mensuram donacionis Christi; illi autem sunt superiores quoad Deum qui instar apostolorum plus deserentes mundum seminant efficacius verbum Dei. Unde ritus moderni [p. 309] isti maxime religioni supperadditi alios iuvando facilitant et alios retardando difficultant, sed utrobique qui ex maiori caritate plus defenderit et docuerit legem domini accepcior erit illi; non enim est personarum accepcio apud Deum, sed quicunque ex maiori caritate pro illo plus passus fuerit, magis penaliter vixerit et sponse sue magis profecerit, sibi accepcior erit.

[ENGLISH]

## ¶4 · 309.8–310.13

> [p. 309] Ex istis potest speculator perpendere quomodo perversa est elemosinancium intencio, et per consequens religio Christiana, nam ubi donata sunt clero temporalia non ut civiliter dominentur, sed ut ecclesiastica elemosina serviliter dispensetur; non ut proprietarie splendidi vel seculariter conversetur; sed ut sine personarum accepcione, postposito affectu carnis et sanguinis, elemosina divitum magis egentibus ministretur; non ut clerus deses in spirituali servicio contendat seculariter pro primatu, sed ut vigilancius ex maiori beneficio intendat humilius quomodo se et suos subditos liberet a reatu. Sed iudicet considerans statum seculi, que istarum parcium est pocior hns diebus; nam ad tantum invaluit oleum peccatoris quod, ubi dicerentur christiani ex oleo gracie et humili imitacione regis justicie, iam nimis multi sunt Antichristi ex diffusione olei regis superbie ad cuius probacionem a nominetenus sanctuario Christi incipite. Nonne vendicat antipapa, vicarius Luciferi, quod debet super omnes imperatores, reges et principes seculariter dominari, et ob reverenciam ordinis sibi debet undique secundum modum seculi magis splendide ministrari; et ad hoc intorquet scripturam sacram et dicta sanctorum. Et idem vendicant multi eius discipuli, verecundantes vocari subditorum elemosinarii [p. 310] sive servi, sed conversando excessive seculariter introducunt se dominos reciproce nominari. Nam in primitiva ecclesia dixerunt se regulariter esse servos, tempore vero Augustini propter dominacionem insolencium destruendo vicia vocati sunt domini. Sed hodie plane nituntur omissione et commissione in conversacione ostendere quod pretendunt se esse dominos seculares; quod cum repugnat legi Dei et ordini, patet quanta monstruositas foret ex heresi circa fidem scripture sacre in ecclesiam introducta. Corrigendi ergo sunt blasphemi qui denigrant (quantum in eis est) causam Christi martirii, scilicet quod mortuus est pro dominacione seculari suis clericis adquirenda.

[ENGLISH]

## ¶5 · 310.14–310.29

> [p. 310] Et sic fingunt ingrati quod sanctus Thomas Can- tuariensis obiit pro dominacione seculari ablata clero Anglie restituenda et dominacione civili habita confirmanda. -Christus enim econtra mortuus est pro salvacione humani generis et ad docendum suos discipulos et specialiter clerum secularia desideria abnegare (ut dicit Apostolus ad Titum II°). Et sanctus Thomas mortuus est ad constanter corripiendum reges et dominos, ne precipitent clerum in officio seculari nec impediant quominus corripiatur a suo episcopo, et per consequens ad docendum episcopos nostre provincie ne ab ista correpcione, et per consequens a defensione privilegiorum et iuris ecclesie timore servili de amissione temporalium retrahantur. Et utinam sacerdotes superiores nostri regni addiscerent intellectu et affectu istam geminam leccionem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 306.15: It is a mere fiction to say that such rule by the clergy is not a privilege, but common law.
- 307.3: Christ did not contradict himself, and he taught his apostles to live without properly,
- 307.20: and to distribute spiritual alms.
- 308.22: There should be no distinction of secular and regular, but all the clergy should live only on alms.
- 309.8: Religion itself, like alms, has been perverted,
- 309.19: and pride has taken the place of serviceable humility.
- 310.1: How ecclesiastical rule grew up.
- 310.14: St. Thomas died to maintain the right of rebuking kings and enforcing discipline in the clergy.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 306: *privilegii* [R3]
  - 307: *ergo* [R3]
  - 307: *nimis* [R4]
  - 309: *et* (15 is the line number) [R4]
  - 309: *Nonne* (172c folio mark) [R4]
  - 310: *Nam* [R3]
  - 310: *Can-* (Can-/tuariensis; main token holds first half) [R4]
  - 310: *tuariensis* (second half of Can-/tuariensis) [R6]
  - 310: *obiit* [R5]
  - 310: *II°* [R3]
  - 307: *excellenciam* (excel- / lenciam on next line; main token holds whole word) [THIN]
  - 309: *isti* (alinea G and 172b folio mark glued) [THIN]
  - 308: *X°,* (line-final; next line starts nec, no verse) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 306:
9. A in marg.: Conclusio. Christus non ad hoc est passus, ut acquirat
dominia clero (Above 172" withont mark of refcrence). i5. A B in

p. 307:
21. A A,: motuo ncxu. 22. spiritalis in codd. sic et in pluribus locis
sequentibus. 29. A B in marg.: Christus plus obligatur creature sue
quam econtra et similiter saccrdos laico quam econtra (Above 172'' withom
mark of reference). 3o. A A,: non deest.

p. 308:
1. A in marg. : Conclusio. 22. A in marg. : Conclusio.
8. Vide supra pag. ao,6 et seq.

p. 309:
8. A in marg. : Clerus dehet esse fidelis dispensator elemosinarum ct
non debct dominari pompatice super illis (Below iy2b without mark of
refcrence). 22. B: ex eo gracie. 23. A Aj: nam nimis.
26. sc. Roberlus Gebenensis (Clemens VII.).

p. 310:
2. A in marg.: tlnde prelati ecclesic vocantur domini. 14. A in
marg. : Ficcio. 3o. A A, : obicitur; A in marg. : Contra. Obieccio.
```

---

## Chunk 14-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-14-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-14-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "310.30–314.27"
divisions: "cap. 14 (heading 'CAP. XIV.' at 299.9); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "924 words; 815 unanimous or majority-real; 95 settled by vote (R2 59, R3a 27, R3b 1, R5a 7, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n347–n351 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 14, part 4: [TITLE]

## ¶1 · 310.30–312.13

> [p. 310] Sed contra dicta arguitur per hoc quod omnia bona mundi sunt patrimonium crucifixi, sed totum suum patrimonium concessit Petro et eius vicariis. ergo illorum sunt omnia bona mundi, licet ergo eis super suo patrimonio dominari. [p. 311] Hic concedenda est conclusio (ut alias diffuse exposui), nam lusti sunt omnia lure poli (ut docet Apostolus, Romanorum VIII°, et Augustinus, epistola XXXVIIª ad Macedonium). Unde clerici debent sequi patrem suum abiciendo dominacionem civilem, dominando pure evangelice ex titulo caritatis. Hoc enim habent exemplatum a Christo et aliud usurpant a cesare; quod si plus appreciantur imitari cesarem quam Christum, quis dubitat quin ex degeneracione perdunt utrumque? Potest ergo clerus habere quotlibet bona ex titulo elemosine ad supplendum suum officium et distribuendum pauperibus, et in hoc imitarentur Christum et eius apostolos, non autem in dominando civiliter, cum hoc foret oppositum in adiecto, et secundum istam racionem foret eis patrimonium crucifixi. Unde consideraremus ne blaspheme nominemus occupacionem bonorum Christi abutendo eis heretice (ut dictum est in fine proximi capituli) vel ne nominemus divicias secundum illam racionem patrimonium crucifixi. Si, inquam, sit patrimonium crucifixi, faciamus ut utendo eis ad similitudinem crucifixi imperciamur ea fideliter membris pauperibus crucifixi, ut demum participemus merito crucifixi, unde abusus noster foret maxime revocabilis considerando attente de nomine patrimonii crucifixi. Contra ista arguo, primo quod omnia bona ecclesie, sive in laicis sive in clero, sunt de patrimonio crucifixi, ipse enim est heres habens in capite omnia bona mundi, et nos titulo adopcionis filialis participamus [p. 312] corum. Nam Psalmo VIII°, 8, de illo dicitur: Omnia subiecisti sub pedibus eius, et Luce X°, 22, dicit iste primogenitus ex multis fratribus: Omnia mihi tradita sunt a patre meo, et Psalmo II° alloquitur pater eum: Postula a me et dabo tibi gentes hereditatem tuam, et possessionem tuam terminos terre. Ex istis sic arguo: Nemo vere possidet quicquam in terra nisi vel Christus vel eius filius, sed quicquid talis possederit; est patrimonium crucifixi, ergo nemo de iure quidquam possidet nisi titulo patrimonii crucifixi, et per consequens superiores filii, cuiusmodi sunt clerici et specialiter eius vicarii, prius et excellencius debent possidere de eius patrimonio quam alii seculares.

[ENGLISH]

## ¶2 · 312.14–312.33

> [p. 312] Hic dicitur quod utraque conclusio est concedenda. Nam iure altissimo habet ipse tam secundum deitatem quam secundum humanitatem omnia bona mundi, et secundum derivacionem ab ipso fonte iusticie, secundum gradus dignitatum participant alii bonis suis, in tantum quod si ipse non fuisset incarnatus, non fuisset in toto genere humano lapso simpliciter iusta possessio, sic quod omnes patres veteris testamenti quibus Deus disposuit regnum, sive gentiles ut Job, Nabuchodonosor et similes, sive Hebrei tempore utriusque legis, omnes, inquam, receperunt possessiones iure Christi; qui passione sua rectificavit titulos omnium membrorum suorum, ymmo quodammodo profuit toti mundo, cum omnes dampnati, omnia inanimata, et breviter tota universitas creata recipit quandam perfeccionem secundam ex vita Christi, cum totus mundus secundum quamlibet partem sui racione meriti Christi perfeccius servit Deo, cum aliter mundus foret colobon, et partes inordinate forent perpetuo sibi ipsis contrarie.

[ENGLISH]

## ¶3 · 313.1–314.9

> [p. 313] Ideo creditur probabiliter quod Christus necessitatus fuit lapsu supposito ad suam fabricam reparandam. Ideo dicit Luce ultimo quod oportuit Christum pati. Omnes ergo domini seculares et breviter omnia membra ecclesie titulo illius domini utuntur patrimonio crucifixi, et ideo oportet quod omnes eius filii, tam clerici quam laici, caveant de abusu. Et ita concedendum est quod clerici et specialiter Christi vicarii habeant prius et perfeccius patrimonium crucifixi; sed tunc oportet quod imitentur modum suum habendi et utendi quantum sufficiunt. Ipse enim habuit hec in via puro titulo gracie et humane elemosine et precise sub illa mensura sub qua fuit exproprietarie necessarium ad edificacionem ecclesie et medium ad supportandum ministerium spirituale, et idem genus modi habendi reliquit appropriate clericis sortis sue, ut patet XII, q. Iª, Clericus. Iste autem est modus habendi perfeccior, quia a modo mundano distraccior et modo habendi beatorum similior. Quando enim triumphantes vitam eternam possidebunt, Deus eos constituit super omnia bona sua, et tunc non habebunt usum vescendi vel corporalem imperfectum ut modo, sed usum spiritualem per intencionem in verbo, et de quanto viator ceteris paribus plus ad talem usum accesserit, de tanto perfeccius procedit; quod faciunt hii qui plus laborant ad edificacionem ecclesie et stricte, humiliter et immundialiter accipiunt graciam necessitatis nature, quantum requiritur pro hoc fine. Sed secundo obicitur per hoc quod Christus fuit simul rex et sacerdos humanitus, sed omne privilegium quod habuit humanitus concessit Petro et eius vicariis, ergo ipsi debent esse simul reges et sacerdotes, [p. 314] habentes utrumque gladium. Sic enim legitur apostolos habuisse tempore capcionis Christi duos gladios, et Petro precepit Christus quod poneret gladium suum in vaginam. Ex quo verbo innuitur quod ecclesia Christi et navicula Petri debent habere utrumque gladium, ut notat beatus Bernardus et quotlibet iura canonica cum concordanciis doctorum. Et hoc videtur beatum Petrum innuere Ia Petri II°, 9, quando dicit: Vos estis genus electum, regale sacerdocium etc.

[ENGLISH]

## ¶4 · 314.10–314.21

> [p. 314] Hic respondeo concedendo maiorem, sed nego minorem tamquam summe hereticam. Christus enim habuit humanitus ius primogeniture nomine redemptoris humani generis et nomine capitis universalis ecclesie cum multis aliis singularibus privilegiis, que nec quanta potuit facere inesse Petro vel alicui vicar Christi formaliter, sicut Augustinus recitat super Joh., Omelia VIª. Verumtamen Augustinus recitat super Joh., Omelia Vª, Christus potuit communicasse Petro, Johanni vel alteri potestatem, ut christiani baptizarentur in nomine eorum, si sic voluisset, sed nec voluit nec docuit, quod implicat quod non sic potuit voluisse.

[ENGLISH]

## ¶5 · 314.22–314.27

> [p. 314] Sed ulterius concedo (ut sepe alias) quod nedum ecclesia sed clerus Christi habet utrumque gladium. Ecclesia quidem cum habeat duas partes, scilicet clerum et laycos, quarum prior pars habet gladium spiritualem in se formaliter et pars laycalis secundum principes seculi habet gladium corporalem in se formaliter.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 310.30: Objection: All things belong to Christ and he has given all to his vicars.
- 311.1: Answer: It is true that the righteous have all things, but to use them in Christ's service.
- 311.26: Objection: 1. All things are Christ's,
- 312.7: therefore his chief followers have a special right to possession.
- 312.14: Answer: This also is true;
- 313.4: but that special possession binds them all the more to use and not to abuse.
- 313.30: Objection: 2. Christ was both king and priest, so the Popes should be the same.
- 314.10: Answer: Christ had rights which he did not give to Peter.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 310: *vicariis* [R3]
  - 311: *a* (print has 'usurpant a' at line end before cesare; main lacks this a) [INS?]
  - 311: *arguo* [R3]
  - 312: *II°* [R3]
  - 312: *Christus* [R3]
  - 313: *patrimonio* [NW]
  - 313: *filii* [R4]
  - 313: *Iª* [R3]
  - 313: *vicariis* [R3]
  - 314: *II°* [R3]
  - 314: *nego* [R3]
  - 314: *VIª* [R3]
  - 314: *Vª* [R4]
  - 311: *VIII°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 310:
2. A in marg.: tlnde prelati ecclesic vocantur domini. 14. A in
marg. : Ficcio. 3o. A A, : obicitur; A in marg. : Contra. Obieccio.

p. 311:
i. A in marg.: Responsio. Iusti sunt omnia. 10. B in marg. :
Clerici titulo elemosine possunt habcrc quotlibet bona. 12. A in
marg. : Nota de patrimonio crucihxi. Nota quomodo sacerdotes debent
dominari evangelice toti mundo et non secularitcr cesarem imitando
(Below i72c without mark of reference). 26. Prima racio. Color pro
dominacionc civili cleri. 29. B: adopcionis linalis.
4. Ep. CLIII in the modern Editions. 18. Vide supra
pag. 297.

p. 312:
9. A A,: ergo — crucifici deest. 14. A in marg. : Responsio. Omnis
dominacio ct iusta poss^ssio est instituta cx vita Christi ct sua passione.
21. Ainmarg.: Conclusio. 24. Codd.: omnes tn quantum. 29. A:
et vita. 32. colobon in codd. rcctc colobos id est: truncatus.

p. 313:
17. B in marg. : Nota titulum Christi ad habendum tcmporalia.
21. A A,: constituet. 3o. A in marg : Secunda racio.
17. Decret. II pars, causa XII, q. I, c. V.

p. 314:
10. A in marg. : Responsio. 12. B: ius deest. 14. B in marg. :
Si Christus habuit potestatem cohercendi homines corporali racione sue
regalie, unde est quod sibi competere dominari civiliter denegatur.
22. A B in marg. : Nota qualiter ecclesia habct duos gladios (A: Below
173» without mark of reference). 28. B in marg. : Quid signant duo
gladii ecclesie. B: ad sensum — gladium potestatem deest.
18. Aug. In Joh. Ev. cap. I, tract. V. Opp. tom. III, pars II,
pag. 323.
```
