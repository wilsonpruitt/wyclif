# Translation brief: ecclesia 19-b–19-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-19-b.md chunks/ecclesia/wyc-ecclesia-19-c.md chunks/ecclesia/wyc-ecclesia-19-d.md` once and fix what it reports.
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

## Glossary (the 201 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
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
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
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
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

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
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| cohabitacio | joint dwelling | Ruled 2026-09-28 (coordinator, delegated). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| ditarius | almsman | The one enriched by the alms (cf. *ditare*, §B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| usufructus | usufruct | Beside *dominacio evangelica*. Ruled 2026-10-02 (*Eccl.* 16, 365.23). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| presbiteri conducticii | hired presbyters | Ruled 2026-10-02 (*Eccl.* 16, 374). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
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
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |

---

## Chunk 19-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "445.31–449.15"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 2 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "849 words; 770 unanimous or majority-real; 65 settled by vote (R2 35, R3a 22, R5a 7, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n482–n486 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 2: [TITLE]

## ¶1 · 445.31–448.13

> [p. 445] Unde videtur mihi quod nomina recitati officii eciam in predestinatis exhinc merentibus beatitudinem sunt quedam specialia, ut apostolatus et episcopatus. Nam missio ad evangelizandum et superintendencia solicita ad custodiendum videntur tantum pro statu [p. 446] vie officiariis sponsi competere. Sed sacerdocium videtur esse eternum, cum beati dant et docent sacra illuminando suos socios in eternum, et ad illud potest applicari illud Apoc. 1°, 6: Fecisti nos Deo nostro regnum et sacerdotes; et sic predestinati qui dignes presunt subiectis videntur mihi esse eis in beatitudine preferendi, et sic in celesti ierarchia eis in perpetuo sacerdocio sunt prelati, ut innuit beatus Gregorius, Omelia XVIIª super illo Luce X°, 1: Post hec designavit dominus alios septuaginta, et Crisostomus expressius, Omelia XXXIV Operis Imperfecti Melior, inquit, est laicus qui in prima facie profitetur vitam secularem sed studet spiritualem, quam sacerdos profitens vitam spiritualem sed amplectitur vitam carnalem, et melior est laicus ante Deum penitenciam agens quam clericus permanens in peccatis. Laicus enim in die iudicii stolam sacerdotalem accipiet, dum eciam crismate omnes sic unguentur in sacerdocio; sacerdos autem peccator spoliatur sacerdocii dignitate quam habuit; et tunc erit inter infideles et ypocritas (ut dicit veritas Matthei XXIV°, 51). Omnes eciam beati erunt virgines spiritualiter (ut patet Apocalypsis XIV°, 4). Et omnes erunt martyres modo suo, cum Luce XIV°, 27, dicitur: Qui non baiulat crucem suam et venit post me, non potest meus esse discipulus. Omnes (inquam) erunt sacerdotes in patria, quia dantes sacra beatitudinis accidentalia conbeatis. Et hinc Abel a quo cepit humana ecclesia in triumpho, fuit expresse virgo, martir et sacerdos, ut notat Augustinus in De [p. 447] Mirabilibus Scripture Sacre, III° capitulo. Tota, inquit, iusticia, hec est virginitas, sacerdocium et martirium. Que triplex iusticia in Abel primo fuit qui et munera Deo placita obtulit, prosapiam generis in seculo non dereliquit et martirii coronam sanguinis effusione ipromeruit. Quilibet ergo salvandus debet esse spiritualiter virgo in hoc quod declinans a malo sequitur agnum sponsum ecclesie; debet secundo esse sacerdos, offerens Deo fructum meriti, et debet tercio connectendo hec duo ad invicem in istis perseverare finaliter tamquam martir. Et ideo signanter notat Christus Matthei XXIII°, 35 quomodo ecclesia dicitur cepisse ab Abel iusto cui secundum Augustinum Jesus commisit primatum iusticie. In hoc, inquit, quod non nominat Zachariam iustum, ut Abel iustum, hereditatem iusticie Abel tenere Zachariam ostendit, sicut in genealogia Christi scribitur primo et solitarie David fuisse regem, dum dicitur: Gesse autem genuit David regem; Salomoni autem et aliis non additur nomen regis, cum alii patres regnum iure hereditario tenuerunt. Sed notanda est alia causa (quam dixi superius) quod Abel fuit primus veteranus ecclesie triumphantis qui spe felici spiritualis nectaris missus est in locum refrigerii expurgandus. Et patet ad formam argumenti quod Deus quidquid creature racionali dederit, eam igocprius ad ipsum habilitat; et quantum ad decretum beati Gregorii, patet quod intelligitur abutentem potestate sua ut sic privare se illa, quantum ad racionem sibi merendi, dum tamen maneat potestas secundum racionem aliis promerendi. Et sic Deus dedit potestatem lude propter causam multiplicem; ipse autem non fuit inhabilis ad recipiendum illam potestatem, licet [p. 448] ex culpa propria fuerit inhabilis ad sibi merendum beatitudinem; nec Christus ordinavit eum sic demereri sed permisit ordinando eum in hoc per accidens sponse sue proficere. Unde talis mixcio atque prefeccio prodest ex gracia ordinantis sancte matri ecclesie eciam plus quam si solum membrum ecclesie in ipsa preficeret. Prodest enim strenuo militi ad exercitum quod habeat rebellantem. Nec contradico sed assencio quod sepe evenit, ut pontifex fingat vel putet se signare sacerdotem caractere, ubi propter inhabilitatem ad ordines vel negligenciam ordinarii manet laycus non signatus (de quo alibi).

[ENGLISH]

## ¶2 · 448.14–449.3

> [p. 448] Videtur autem mihi quod prescitus eciam in mortali peccato actuali ministrat fidelibus, licet sibi dampnabiliter, tamen subiectis utiliter sacramenta. Sic enim Balaam, Num. XXIII°, Cayphas, Joh. XI°, prophetarunt, et dyaboli sepe deiecti per Christum a personis quas obsederant confessi sunt publice dominum Jesum Christum. Et istam sentenciam diffinivit Salvator Matthei VII°, 22: Multi, inquit, dicent mihi in illa die: Domine, domine, nonne in nomine tuo prophetavimus et in nomine tuo demonia eiecimus et virtutes multas fecimus? Et tunc confitebor illis: Quia nunquam novi vos, ut patet de uno Marci IX° et Luce IX° quem apostoli increparunt, quia fecit miracula et non secutus fuit eos. Sed Christus approbavit quantum ad substanciam miraculi, ut non per se ex signis huiusmodi iudicemus filium Dei vel filium diaboli. Sic ergo sacerdotes mali iniuriantur sed non nocent piis fidelibus non demerentibus ministrando eis ecclesiastica sacramenta, ut patet in [p. 449] decretis Ia, q. I, Sifuerit, ex testimonio Augustini, et XVª, questione ultima, cap. ultimo, et III° Decretalium, De Cohabitacione clericorum et mulierum, Vestra.

[ENGLISH]

## ¶3 · 449.4–449.15

> [p. 449] Ex istis videtur primo quod cessaret in clero omnis contencio circa temporalia que sub titulo cause ecclesiastice est tractata. Feci autem ad hoc raciones multiplices et allegavi ad hoc auctoritates scripture.Nam posita licencia taliter contendendi via paciendi iniurias foret securior, ergo generaliter sub pena peccati foret via illa eligenda; patet consequencia ex hoc quod via meritorior et facilior est generaliter eligenda, et ideo dicit Gregorius Omelia XVIIª: Qui locum predicacionis suscipit mala inferre non debet sed tolerare, ut ex ipsa sua mansuetudine iram seviencium mitiget et peccatorum vulnera in aliis ipse affliccionibus vulneratus sanet,

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 445.31: Some offices in the Church are temporal.
- 446.1: some eternal.
- 446.21: All the blessed will be virgins, martyrs and priests.
- 447.22: God fits the creature for the power given to him,
- 447.29: but, it may be, only for the benefit of others,
- 448.14: The foreknown even when in actual sin minister the sacraments with profit to others.
- 449.4: All the litigation in ecclesiastical causes ought to cease.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 445: *eciam* (folio mark 190ᵇ glued) [R4]
  - 445: *Nam* [R3]
  - 446: *XVIIª* [R4]
  - 446: *permanens* [THIN]
  - 446: *in* [THIN]
  - 446: *peccatis* [THIN]
  - 447: *III°* [R5]
  - 447: *offerens* (margin numeral 3 glued) [R4]
  - 449: *et XVª* (main token covers two printed words) [R4]
  - 449: *III°* [R4]
  - 449: *XVIIª* [R3]
  - 448: *∅* (G is margin alinea letter; 'tali' is second half of mor-tali, neighbour 95 already mortali) [DELX]
  - 448: *XXIII°,* [OVERRIDE-VERSE]
  - 448: *XI°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 445:
8. B: adoraverint. Ainmarg.: Duplex caracter. 34. Codd. : et deest.

p. 446:
I. B: sacerdocium vestrum. 4- A in marg.: Quilibet sanctorum
in patria erit sacerdos. 8. A in marg.: Gregorius. 10. A in
marg. : Crisostomus. 12. B : laicis. i3. A in marg. : Laycus
melior quam sacerdos. 29. A in marg.: Augustinus.
II. Opus Imperfectum 1. c. pag. CXLV. 29. Aug. Opp.
tom. III, App. pag. 5.

p. 447:
i. In codd.: IV" cap. Correxi. n. B : signanter nota. i5. B in
marg.: Nota quomodo abutens sua potcstate ca privatur. 24. B: qui
sepe felici. 24. B: iussus est in locum. 28. A in marg.:
Sacerdos quomodo se privat saccrdocio et quomodo manet sacerdos.

p. 448:
3. A A, : promisit. 8. A in marg. : Episcopus non semper quando
pretendit ordinare ordinat. B in marg.: Presciti ministrant sacramenta.
14. A in marg. : Nota conclusionem bonam : Sacerdos malus est sacerdos
et ministrat. 17. 18. A A, : prophetavit. 25. novi vos; sequencia
excidisse videntur: discedite a me. 3o. A in marg.: Nota.

p. 449:
3. A in marg. : Clericus vel sacerdos non debet Iitigarc pro tempo-
ralibus. Prima conclnsio. 9. Codd.: elicienda. i3. Ainmarg. :
Nota Gregorius. 14 A A,: scviciencium. 16. A in marg. : Iudex
ecclesiasticus non debet iudicare inter litigantes pro temporalibus.
1. Decr. II pars, causa I, q. I, cap. XXX et causa XV, q. VIII,
c. V. 2. Decret. Greg. IX, lib. III, tit. II, c. VII. 12. Greg. XL
Hom. lib. I, Hom. XVII, 4.
```

---

## Chunk 19-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "449.16–453.28"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 3 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "993 words; 852 unanimous or majority-real; 125 settled by vote (INS 1, R2 73, R3a 41, R3b 4, R5a 5, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n486–n490 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 3: [TITLE]

## ¶1 · 449.16–450.4

> [p. 449] Item, iudex generaliter ignorat que sit voluntas Dei quoad partes contendentes, que occuparet temporalia vendicata; sed nullus iudex ecclesiasticus iudicare debet pro parte nisi pro qua scit Deum discernere, quia aliter foret Deo contrarius iudicando. Ergo nullus iudex ecclesiasticus iudicaret in foro cleri contencioso nisi forte quod utraque pars cessaret a lite, intendens circa officium a domino limitatum. Illi enim quibus Christus limitat non portare saculum neque peram, sed, propter preponderanciam spiritualis officii ad quod primo accelerant, neque calciamenta ferre neque hominem per viam salutare neque quomodolibet occupari unde gravius officium discipuli Christi prepediat (ut docetur Luce X°, 4), valde alieni sunt, ut circa contenciones temporalium occupentur. Salutaciones [p. 450] enim per viam sunt nimis periculose et nimis a predicacione evangelii tardative. Nec valet ficcio qua dicitur temporalia pro quibus contenditur esse Christi discipulo pro suo officio necessaria

[ENGLISH]

## ¶2 · 450.5–450.16

> [p. 450] instrumenta, quia exequatur suum officium sine retrospeccione ad temporalia, et non est compossibile Deum sibi deficere in temporalibus necessariis non ad onus. Ideo dicit Apostolus Heb. ultimo: Sint mores sine avaricia, contenti presentibus. Ipse enim dixit: Non te deseram neque derelinquam, ita ut confidenter dicamus: Dominus mihi adiutor, non timebo quid faciat mihi homo. Ideo dicit beatus Gregorius Omelia XVIIª Predicatori tanta debet esse in Deo fiducia ut presentis vite sumptus quamvis non provideat, tamen hos non sibi deesse certissime sciat, ne dum mens eius occupetur ad temporalia, minus aliis provideat eterna.

[ENGLISH]

## ¶3 · 450.17–450.28

> [p. 450] Item, eo ipso quo quis est non membrum sancte matris ecclesie est indignus habere patrimonium Crucifixi titulo vel iure viri ecclesiastici, sed omnino iudex ecclesiasticus cui non sit de hoc specialis revelacio ignorat si dicta persona contendens sit membrum sancte matris ecclesie, ergo ignorat si sit dignus habere patrimonium vendicatum. Assumptum patet eo quod nullius alterius ecclesie persona nisi persona sancte matris ecclesia habet titulo illius ecclesie colorem aliquid vendicandi, cum sit de civitate et corpore dyaboli, contrarius prime iusticie. Et maior patet ex hoc quod nullus iudex ecclesiasticus subducta revelacione predicta

[ENGLISH]

## ¶4 · 450.29–450.34

> [p. 450] scit si alius sit predestinatus, et per consequens, si sit membrum sancte matris ecclesie. Cum ergo fundamentum tocius iuris contencionis foret incorporacio qua contendens foret de sancta matre ecclesia, quod nec contendens scit docere nec iudex

[ENGLISH]

## ¶5 · 451.1–451.3

> [p. 451] quacunque probacione humana discernere, videtur quod propter ambiguitatem offendendi in Dei iusticiam cessaret omnis talis contencio.

[ENGLISH]

## ¶6 · 451.4–453.8

> [p. 451] Nam si fundamentum tituli foret mendacium, quomodo non foret omne iudicium innitens illi fundamento iniquum? Aliter enim sufficeret cuicunque layco vel mechanico habere pretensionem vel apparenciam iuris ad iuste vendicandum et obtinendum quamcunque possessionem ecclesiasticam vel civilem; ex quo absurdissima sequerentur. Cum ergo pars Antichristi non sufficit probare quod sit vir ecclesiasticus, et iudex debet cavere omnino ne discrepet a divino iudicio, cum nullum nisi illud sit iustum simpliciter, videtur quod debet cessare omnino tale iudicium; et qui nituntur generaliter excusare curias ecclesiasticas in talibus iudiciis a peccatis lavant lateres et proditorie inpinguant inimicos iusticie oleo peccatoris. Nam Christus cum suis apostolis renuit talia placita secularia atque iudicia, et sic omnes curati vel clerici non cecati possessione et lege cesarea, de quibus loquitur Gregorius Omelia XVII: Multi, inquit, cum regiminis iura suscipiunt, ad lacerandum subditos inardescunt, terrorem potestatis exhibent, et quibus prodesse debuerant nocent, et quia caritatis viscera non habent, domini appetunt videri, patres se esse mimine recognoscunt, humilitatis locum in elacionem dominacionis immutant, et si quandoque extrinsecus blandiuntur, intrinsecus seviunt. De quibus veritas dicit: Veniunt ad vos in vestimentis ovium, intrinsecus autem sunt lupi rapaces. Et forte sicut in tempore sancti Gregorii, sic sunt hodie in ecclesia quidam tales, et [p. 452] cum leges ecclesie Licet sopite cum suis doctoribus illud dicunt concorditer, (ut patet III° Decretalium, cap. Fraternitatem), nec aliter possumus excusari de tanta occupacione temporalium differenter a Christo et suis apostolis, nisi quod sumus ministri eorum et procuratores pauperum quorum sunt bona que servamus non ut domini seculares, et tamen servare illam racionem in facto vel audire loqui de illa in verbo contempnimus ut venenum, sed tam sermone quam opere aspiramus ad dominium seculare. Item, ad repellendum tale humanum iudicium confert quod iudex ut plurimum ignorat si exactor interim cecidit a iure suo propter omissionem spiritualis ministerii subditis rependendum, sed stante illa iniusticia iniuste ferretur pro tali iudicium: ergo temerarium foret dare pro tali iudicium. Minor patet pro eo quod continuatim creatorum spirituale ministerium est magis debitum quam aliquod debitum corporale, ergo illis subtrahentibus magis debitum iniuste exigerent minus debitum et sub condicione quod retribuant magis debitum. Ymmo videtur quod excedunt in malicia servum nequam qui post magnam misericordiam factam maioris debiti minus sibi debitum exegit crudeliter (ut patet Matthei XVIII°). Talis enim curatus exigit a subditis sibi indebitum et hoc horribiliter per censuras et quomodocunque clerici circa prelacias contenderint, demum temporalia exigunt a viduis, a subiectis. Unde et istam iniuriam tangit Decretum, XIIª, q. II. Sepe fit, ubi ex decreto septimi Tolnensis concilii sic habetur: Si quis clericorum stipendium de rebus ecclesie cuiuscunque episcopi perceperit largitate, [p. 453] sub precarie nomine debeat professionem scribere, ne per retencionem diuturnam preiudicium afferat ecclesie, et quicunque in usu perceperit debet utiliter laborare, ut nec res divini iuris videantur aliqua occasione negligi et ut subsidium ab ecclesia cui deserviunt percipere possint clerici. Quod si quis eorum contempserit facere, ipse se stipendio suo videbitur privare.

[ENGLISH]

## ¶7 · 453.9–453.28

> [p. 453] Iura autem nature, iura scripture et iura ecclesie contestantur quod ecclesiasticus omnino omittens laborare pertinenter ad suum officium non debet accipere a subditis quibus non proficit sed officit temporale stipendium, quia tunc deberent laici conducere apostatas ad eis nocendum. Sed (ut sepe tetigi) contencio est quis exequeretur subtraccionem talem iustam, et videtur mihi non esse tantum sacramentum, quin illi qui stipendium ministrandi conferrent vacanti subtraherent, nec nocet fidelibus excommunicacio vel censura alia in hac parte (ut patet XIª, q. III. Quomodo sacerdos). Sumitur precaria nunc stricte pro dono vel stipendio temporali ad preces hominis pro tempore limitato, et nunc large pro quacunque donacione gratuita, eciam perpetua quoad usufructum donatore reservante penes se dominium, et sic in primitiva ecclesia tota dotacio censebatur precaria, ne elemosinarius prescriberet contra patronum; in defectu vero officii non cadit prescripcio sicut nec fit prescripcio contra Deum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 449.16: The clergy should not act as judges.
- 450.3: It is a mere pretence to say that the clergy need temporal possessions for their duties .
- 450.17: None can rightly hold the patrimony of 1 the Crucified but members of the Church,
- 451.1: but the judge cannot know who is such,
- 451.6: Since the ground of just judgments cannot be reached, it were better to give up such trials.
- 452.11: A claimant may have forfeited his right to dues by not ministering,
- 453.9: in which case all laws shew that he should not be paid.
- 453.15: The real question is who should withdraw the stipend? I say the patron.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 449: *Christus* [R3]
  - 449: *Christi* [R3]
  - 450: *a* (print has a predicacione at line start) [INS?]
  - 450: *necessaria* (print has necessaria before instrumenta; main scan lacks it) [INS?]
  - 450: *officium* (line number 5 glued) [R4]
  - 450: *XVIIª* (print has lia XVIIª: before Predicatori; main scan lacks it) [INS?]
  - 450: *ut presentis* (main token covers two printed words) [R5]
  - 450: *Crucifixi* (print Cruci-/fixi; main token holds whole word) [R4]
  - 450: *iudex* [THIN]
  - 451: *pretensionem* (print spelling) [NW]
  - 452: *III°* [R4]
  - 452: *XIIª* [R3]
  - 453: *Quod* [R3]
  - 453: *Iura* [R3]
  - 453: *XIª* [R4]
  - 450: *∅* ('in-' (of in-corporacio, 229 already incorporacio) glued to ergo (222 present)) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 449:
3. A in marg. : Clericus vel sacerdos non debet Iitigarc pro tempo-
ralibus. Prima conclnsio. 9. Codd.: elicienda. i3. Ainmarg. :
Nota Gregorius. 14 A A,: scviciencium. 16. A in marg. : Iudex
ecclesiasticus non debet iudicare inter litigantes pro temporalibus.
1. Decr. II pars, causa I, q. I, cap. XXX et causa XV, q. VIII,
c. V. 2. Decret. Greg. IX, lib. III, tit. II, c. VII. 12. Greg. XL
Hom. lib. I, Hom. XVII, 4.

p. 450:
3. A in marg.: Ficcio. «o. B: te deest. «. A n. marg.:
Gregorius. Nota qualem spem debet habere predicator ad De»m.
12. Greg. XL. Hom. lib. I, Hom. XVII, 5.

p. 451:
21. A in marg. : Gregorius. Contra malos rectores ecclesiasticos. In codd.
Omelia nona supra; 9 s"» = pro : /Au> = XVII. 25. In codd.: patres
esse minime. Correxi c textu Gregorii.
16. 'lavant lateres', id est, operam inanem adhibent; cf. Erasmi
Adagia, Chil. I, 370. He says itis used by Terence in Phormio (186).

p. 452:
3.AA1:Firmitatem;vid.Decret. Greg. IX, lib. III, tit. XXVIII, cap. III.
11 12 A in textu: constat; in marg. correxit: confert. A, : constat; B:
confert. .5. A: fereretur; A, : feretur. 17. A A, : creatons.
,9. A A,: exigeret. 24. In codd. Ma.th. XVI. 29. A: Tolnens.s;
recte Toletanensis ; vid. Decreti sec. part. c. XII, q. U, cap. LXXH-
3i. In decr. : percipit.

p. 453:
5. In decret.: negligi et subsidiurrt. 6. deservit in codd. Correxi
e decretali supra memorata. 21. A in marg. : Precaria accipitur
dupliciter < \ 28. B: Sicut — prescripcio deest. 29. A B in
marg. : Primus error.
20. Decr. sec. pars, caus. XI, q. III, cap. XLIV.
```

---

## Chunk 19-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-19-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-19-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "453.29–457.29"
divisions: "cap. 19 (heading 'CAP. XIX.' at 441.26); part 4 of 8, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "921 words; 814 unanimous or majority-real; 94 settled by vote (R2 59, R3a 25, R3b 4, R5a 3, R6a 3); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n490–n494 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 19, part 4: [TITLE]

## ¶1 · 453.29–454.8

> [p. 453] Et ex istis patent errores multi: Quidam enim fingunt quod si secundum leges humanas testificatum [p. 454] fuerit quod tali debeatur datum beneficium, debet iudicari pro illo quomodocunque secundum mores secum fuerit quoad Deum, quia certum est quod Deus in superatis excipit contra illum nisi habuerit rectificacionem secundum veritatem iusticie. Ideo iura civilia que non per se attendunt ad habilitaciones virtutum ut plurimum sunt iniusta (ut dicit Augustinus, Epistola XXXVIII ad Macedonium).

[ENGLISH]

## ¶2 · 454.9–454.14

> [p. 454] Patet secundo destruccio fuci sophistici quo fingunt contendentes se exequi pro iure suo atque ecclesie; nam per execucionem talem et omissionem divini consilii ac debiti ministerii ius quod prius habuerunt extinguitur, ymmo haberent ius et dominum ulterius faciendo opus evangeliste sine contencione huiusmodi.

[ENGLISH]

## ¶3 · 454.15–456.19

> [p. 454] Item, tales iudices communiter exigunt absolutum iuramentum in tali casu a testibus, cuius iuramenti veritatem cognoscunt testes ut plurimum ignorare; quod cum sit magnum periculum sicut iudicare sine sufficiencia probacionis, videtur quod debent omnino iudicium tale dimittere. Nam sine ritu tali crevit et stetit mater nostra prospere, quando scilicet quilibet sacerdos vel curatus habuit ex evidencia sui ministerii suffragium temporale; tunc enim fuit cura diligencior, profectus ecclesie maior, concordia extensior, ministracio ac veneracio sacerdotis complecior et omnino progressus ecclesie legi Christi conformior. Ideo status iste et eius antecedencia, licet ritus introductos interimant, sunt racionabiliter admittenda. Quis rogo sacerdos vel laycus cognoscit si dictus sacerdos advena fuit rite in sacris ordinibus constitutus? Nam litere ordinum, quid propter variacionem impressionis sigilli, quid propter mutacionem nominis literati et quid propter latentem defectum in ordinante vel ordinato, non dant vel evidenciam topicam alteri qui [p. 455] super testificacione ordinum dati presbiteri fuerit requisitus? Sic enim facta apostolorum ostenderant se esse sacerdotes, licet nesciamus quando et qua forma fuerint a domino ordinati. Confirmatur, si ordinans vel ordinatus vel uterque fuerit pro tempore ordinacionis simpliciter infidelis, aut ordinanti deest intencio cum verbis sacramenti ordinis que profert, tunc cum paribus non fit ordinacio legitima, sed hoc ex tibi dubio contigit de quocunque sacerdote cui debes testimonium prohibere: ergo ex tibi dubio non fuit legitime ordinatus. Assumptum videtur eo quod nemo accipit baptismum quod est sacramentum necessariissimum sine fide, ergo a pari nec alia minus necessaria sacramenta, et per idem videtur quod omnino infidelis non ministrat fidelibus sacramenta. Sic enim paganus, iudeus vel omnino hereticus deridendo et intendendo oppositum ministraret in casu fidelibus sacramenta, et per idem in casu avis, bestia vel res inanimata infundens aquam et formans vocem, quod videtur ridiculum et contra decreta ecclesie. Nam Ia, q. I scribitur sub auctoritate beati Gregorii: Quicunque sacros ordines vendunt aut emunt sacerdotes esse non possunt. Unde scriptum est anathema danti et anathema accipienti, hoc est symoniaca heresis. Quomodo ergo, si anathema sunt et sancti non sunt, sanctificare alios possunt? Et cum in Christo corpore non sunt, quomodo corpus Christi tradere vel accipere possunt? Qui maledictus est benedicere quomodo potest? Talia sunt multa decreta, ut IX, q. I, et sepe alibi. Et quicquid doctores dixerint, ignoratur de alio utrum sit perpetuo infidelis excommunicatus [p. 456] sive hereticus, et tunc secundum decretum IXª q. I. Sed excommunicati, non ministrat ecclesiastica sacramenta. Ideo patet quod est dare indisposicionem in ministro que vetaret confeccionem vel ministerium sacramenti, est dare aliam indisposicionem que ministrantem dampnificet et habili recipienti proficeret; qui gradus sunt Deo absconditi. Ex istis videtur quod, sicut laicus de quocunque sacerdote suo in casu dubitat utrum sit sacerdos de sancta matre ecclesie, sic est sibi evidens dubitare utrum sit sacerdos rite ordinatus secundum formam statutam in iam militante ecclesia vel sub aliquo gradu clericus secundum presentem iusticiam in ministerio temporali. Probatur ex hoc quod ignoratur error fidei in ordinante vel in ordinato, sicut ignoratur utrum sit perpetuo hereticus et infidelis, sicut est de quolibet prescito, et ita de infinitis illusionibus que possent contingere in verbis sacramentalibus in intencione consecrantis.

[ENGLISH]

## ¶4 · 456.20–457.29

> [p. 456] Ulterius videtur quod fides non titubaret in laicis, licet ignorent in particulari disposicionem sui presbiteri, nam nichil quod est supra potestatem eorum faceret in eis fidem deficere, sed certitudo talis circumstancie sacerdotis est supra potestatem eorum. Ideo non faceret in eis fidem deficere, nam sensus laici non iudicat de verbis vel intencione presbiteri consecrantis, nec est aliqua particula fidei catholice quod ipse rite consecrat; et sic de testificacione, de racione vel quocunque alio loco evidencie assignando, ita quod vita sacerdotis (ut mihi videtur) est maxima naturalis evidencia per quam crederetur in talibus [p. 457] sacerdoti. Notandum tamen quod stultum est laicum de talibus nimium dubitare, dicente decreto Iª q. I, sub auctoritate Gregorii: Multi secularium hominum cum plus sacerdotum vitam quam suam discuciunt, magnum contempcionis divinorum sacramentorum crimen incurrunt, quia sicut paulo ante recitatur ex dicto beati Augustini: Omnia sacramenta cum obsunt indigne tractantibus, prosunt tamen per eos digne sumentibus sicut et verbum Dei. Unde dictum est: Que dicunt facite, que autem faciunt facere nolite. Et infra sub auctoritate beati Ambrosii Cum scriptura testatur quod ad preces Jeroboam ignis descendit de celo et rursus precante Helia ignis missus est de celo qui sacramenta consumeret ut patet 111° Regum XII° et XVIII°), datur intelligi quod Deus non merita personarum considerat sed officia sacerdotum. Requiritur tamen laicum habere aliquam evidenciam de presbitero citra suam fidem Ulterius videtur quod sine sacramentis nostris sensibilibus de possibili servatur fides in nostra ecclesia servata in nobis cum caritate fide catholica. Nam articuli fidei catholice sunt generales et non implicant quod iste sit sacerdos, quod hic sit corpus Christi et sic de aliis nisi de quanto veritas est substrata Nec tenetur christianus nisi subintellecta tali condicione credere quidquam tale; opinionem tamen habet de ministerio diffamati presbiteri ultra consimile ministerium laicorum, sicut credibile est quod Christus sepe supplet defectum presbiteri, ordinando, conficiendo vel

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 454.1: Some pretend f we have only to, consider human 1 law.
- 454.9: Others, that the claimant acts for the Church.
- 454.15: Ecclesiastical judges make witnesses swear to things they cannot know.
- 454.20: Once a man was curate because he did the work.
- 455.5: Doubts as to the legitimacy of ordinations.
- 456.1: Unfitness may go so far as to prevent ministration or only so far that a man ministers to his own damnation.
- 456.20: It does not affect the layman's faith that he cannot tell whether the priest is qualified;

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 454: *∅* (English side-note word (the); print has no word before Patet) [INS?]
  - 454: *iure* [NW]
  - 455: *fuerit* [R3]
  - 456: *sive* [THIN]
  - 457: *tamen* [THIN]
  - 457: *est* [THIN]
  - 457: *de* [THIN]
  - 457: *talibus* [THIN]
  - 457: *nimium* [THIN]
  - 457: *Iª* (English side-note text glued) [R4]
  - 457: *ut* (line number 15 glued) [R4]
  - 457: *Christi* [R3]
  - 457: *Christus* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 453:
5. In decret.: negligi et subsidiurrt. 6. deservit in codd. Correxi
e decretali supra memorata. 21. A in marg. : Precaria accipitur
dupliciter < \ 28. B: Sicut — prescripcio deest. 29. A B in
marg. : Primus error.
20. Decr. sec. pars, caus. XI, q. III, cap. XLIV.

p. 454:
9. A in marg. Secundus error. 14. B: contencione huius.
28. A : intimant. 29. B : si dulus.

p. 455:
4. A Aj : fuerunt. 5. A in marg. : Confirmacio. 14. B : per illud.
18. B: per illud. 21. A in marg.: Nota. Dubitatur an qui pretenduntur
esse sacerdotes sint sacerdotes cum motivis (Above 191° wliitout mark
of referencc). 24. In decrct. dandi . . . accipiendi.
21. Decr. sec. pars, causa I, q. I, cap. XII.

p. 456:
8. A in marg. : Secunda conclusio. 14. i5. B : inordinate. 20. Ain
marg.: Tercia conclusio. 20. B: tutubaret. 23. 24. A: circum-
stancia; hoc verbum rasura laesum, propter quod in A^j talis circum —
sacerdotis. 27. A in marg. : Conclusio.
2. Decr. sec. pars, causa IX, q. I, cap. III.

p. 457:
2. 3. Decr. sec. pars, q. I., cap. LXXXIV. 7. ib. cap. LXXVIII.
ib. cap. LXXXIII.
```
