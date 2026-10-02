# Translation brief: ecclesia 20-c–20-e

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-20-c.md chunks/ecclesia/wyc-ecclesia-20-d.md chunks/ecclesia/wyc-ecclesia-20-e.md` once and fix what it reports.
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

## Glossary (the 190 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
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
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
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
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| brachium seculare | the secular arm | Ruled 2026-09-28 (coordinator, delegated) (7 sites). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
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
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| cohabitacio | joint dwelling | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosina cartalis | charter alms | Alms granted by charter. Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinator | almsgiver | Agent noun beside *elemosinans* (same English); *elemosinatus* "almsman" (the 09-28 row governs; conformed 2026-10-02, *Eccl.* 16). Ruled 2026-10-02 (*Eccl.* 13). |
| elemosinacio | almsgiving | *Temporalis elemosinacio* "almsgiving from time to time" against perpetual alms. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| civilitas | civil standing | Kept apart from *dominium civile* "civil lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| Romanus pontifex | Roman pontiff | Kept apart from *papa* "pope". Ruled 2026-10-02 (*Eccl.* 16, 366.29). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| collegiatus | collegiate | Ruled 2026-10-02 (*Eccl.* 16, 16-d/16-e). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |

---

## Chunk 20-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-20-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-20-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "480.16–484.28"
divisions: "cap. 20 (heading 'CAP. XX.' at 471.13); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1065 words; 961 unanimous or majority-real; 96 settled by vote (R2 61, R3a 33, R3b 1, R5a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n517–n521 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 20, part 3: [TITLE]

## ¶1 · 480.16–484.28

> [p. 480] Sed quia matrona prudens considerans quod cibaria vie non sufficiunt homini in eternum, ideo quinto subditur: Consideravit agrum et emit illum, de fructu manuum suarum plantavit vineam. Ager ille secundum Augustinum est regnum celorum in quo sunt fructus semper virentes, ut patet Apoc. ultimo, et Psalmo XLIX°, 11 dicitur: Pulchritudo agri mecum est. Illam autem patriam fidelis discursu fidei infuse considerat, et ex fide scripture pro levi tribulacionis momentanee ipsum sperat, et sic illud quod non videtur modo sensibiliter pondus eterne glorie operatur in nobis et voluntariam persecucionis pacienciam propter iusticiam que secundum vocem veritatis Matthei VI° est precium huius agri. Unde quid propter exemplum martirum et iustorum sancte vivencium et quid propter virtutes theologicas infusas desuper mater nostra in spe boni futuri plantavit vineam, hoc est, superiorem cleri ecclesiam que residuum agri letificet? Et hoc merito tocius ecclesie quod est fructus [p. 481] sue potencie promerendi. Et utinam non propter ocium sive demeritum vinea ista transeat in ortum olerum. Unde quia ager iste in racione colendi et possidendi requirit laborem sollicitum et ordinatum, ideo sexto subditur de muliere forti predicta quod accinxit fortitudine lumbos suos et roboravit brachium suum. Nam ancilla apparate serviens tanto sponso nedum stringit carnales concupiscencias zona precepti dominici, sed cuncta opera sua facit ad regulam inter habundanciam et defectum, ne spiritualiter adulteretur cum viro alio, sic quod ad omne opus agendum in agro dominico sit parata; et ad ista requiritur fortitudo resistendi et prevalendi cunctis spiritualibus inimicis. Et videtur posse intelligi in predicacione secundum causam per agrum predictum ipsum caput ecclesie, cuius participacione omnes predestinati sunt regnum celorum; qui licet sint secundum naturam sensibiles, racio tamen qua sunt ecclesia et in potencia beatificabiles est insensibilis. Ad reducendum potenciam istam ad actum requiritur labor assiduus, et illud exercicium fortificat potenciam operandi; et ideo signanter dicitur quod roboravit brachium suum, nec est ista exercitacio nimium tediosa. Ideo septimo subditur: Gustavit et vidit quia bona est negociacio eius; non extinguetur in nocte lucerna eius. Quibus, inquit Augustinus, est palatum quo gustatur sic indulcoratum terrestribus, ut videatur laborem pro beatitudine esse amarum eis, non est celum carum. Rectificat autem gustum anime consciencia bona, que si pungitur peccato amara videntur omnia quibus anima nutriretur. Que ergo dulciter [p. 482] delectatur in domino, non solum exponit exercicio laudis divine sua omnia sed se ipsam; talis enim interim gustat in actibus quam suavis est dominus, quousque infima dulcedo timentibus Deum abscondita sit illapsa. Nec potest obici quod hec mulier non vidit quomodo operandum sit propter noctis tenebras in qua viat, quia lucerna ardebit continue, dum semper habet oculum et affeccionem, sperando in domino, verbo domini consolacionem scripture et continuacionem beneficencie tamquam oleum continue largiente, et ex ista luce cum oleo devocionis exhilarata. Unde octavo subiungitur: Manum suam misit ad forcia et digiti eius apprehenderunt fusum; ubi ista bona matrona lanifica per manum et digitum specificat expressius quam supra applicacionem potencie et prudencie ad sedule operandum. Nam manus et digiti sunt propiores quam brachium actui operandi; et potest opus huius femine dici forte, quia collectim procedit ex viribus universalis ecclesie resistente toto corpore dyaboli cum eius omnibus instrumentis. Sed quantum ad sensum habendum de fuso dicit magnus doctor Augustinus quod non tacebit caritati nostre quod magister suus inspirando donaverit. Primo ergo supponit quod christianus scit bene. quid fecerit in preteritum, sed ignorat quid aut qualiter faciet in futurum. Secundo supponitur quod pius christianus de futuro opere bono timet, de preterito gaudet, et ut perseveret in bonis operibus caute vigilat, ne forte negligens futurorum perdat preteritum, et sic habet firmam conscienciam de facto et non de fiendo. Tercio supponit quod in arte nendi lanifici involutum in colo nondum artificiatum est in forma fili, sed ab illo ad fusum trahitur, non econtra. [p. 483] Ex istis elicitur quod sancta mater ecclesia dum subtili operacione apprehendit opus suum preteritum ad sensum scripture, apprehendit digitis suis fusum, quia rem anteriorem posteriorat, ut contingit de nentibus; est tamen conneccio, quia in opere preterito debent firmari brachia, debet securari consciencia et fundari spes ad futura premia capienda: Quidquid, inquit, operaris tota firmitas animi sit ad fusum, quia quod pendet in colo ad fusum trahicitur, non econtra. Et secundum istam leccionem non sollicitaret fidelis nec aspiraret ad grandem statum seculi in futurum, sed instanter trahiceret opus meritorium in preteritum, confidens quod ut sic erit humilior ad futurum. Et istam sollicitudinem ad colum prohibet sponsus Matthei VI° capitulo. Jactemus ergo thesaurum meriti in memoriam sponsi nostri qui pendens in cruce noluit memoriam passionis in preteritum intranslate relinquere, quamvis Judei false dixerint: Si rex Israel est, descendat nunc de cruce et credimus ei Matthei XXVII°, 40. Et hinc conclusio sequitur pertinenter: Manum suam aperuit inopi et palmas suas extendit ad pauperem. Nam dicens beneficencie et communionis non oblivisci ex proposicione septima et sciens quod solum firma spes premii est de perfecta operacione plene preterita ex proposicione proxima dat operam pro ulteriori elemosina facienda. Sperans, inquit Augustinus, in domino sibi dicit: Da domine, quia dedi, dimitte, quia dimisi, fac mecum misericordiam, quia feci. Nam Jacobi II, 12 scribitur: Iudicium sine misericordia illi qui non fecit misericordiam. Habens, inquit, plenum sacellum apotecam vel orreum nendo salubriter a colo transferat ad fusum. Et multo magis operandum est instanter opus misericordie spirituale et notum ex textu quomodo ecclesia egenciori [p. 484] dat largius de eo quod indiget sed potestatem defensionis exercet in paupere. Ex istis decimo sequitur quod vir talis matrone non timebit domui sue a frigoribus nivis: omnes enim domestici eius vestiti sunt duplicibus. Quomodo, inquit Augustinus, timeret dominus de suis domesticis qui sunt membra talis matrone, cum Romanorum VIII°, 30 scribitur: Quos predestinavit ipsos vocavit et quos vocavit ipsos et iustificavit et quos iustificavit ipsos et glorificavit. Igitur nec Christus nec ecclesia timebit membris suis ex persecucione nivea in qua refrigescit caritas multorum (ut dicitur Matthei XXIV°, 12), cum omnes de domo ecclesie vestiti sunt duplicibus. Hoc vestimentum est preciosissimum, cum sit realiter ipse sponsus. Unde ad Galatos III°, 27 dicitur: Omnes qui in Christo baptizati estis Christum induistis. Illi ergo qui et predestinantur et virtuose superaddite operantur, digne laudantes Christum divinitus atque humanitus, sunt vestiti duplicibus. Heretici autem presciti qui baptizati sunt, habentes temporaneam graciam baptismalem, et post nude confitentur in Christo unam simplicem naturam (ut puta, solum divinitatem vel solum humanitatem, ut Fotiniani et Manichei) vestiti sunt tamquam servi ecclesie simplici vestimento, ne fingant se velle perseverare finaliter, si habuerint vestimentum. Sed mali secundum Augustinum vestiti sunt tantum forma sacramenti, boni vero opere et imitacione finali.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 480.16: Verse 16. The field that she buys is the Kingdom of Heaven.
- 481.6: Verse 17. The Church requires strength to contend with spiritual enemies.
- 481.24: Verse 18. The taste is purified by a good conscience.
- 482.12: Verse 19 tells of the Church's sedulous industry.
- 483.20: Verse 20. Her readiness to help those in need.
- 484.3: Verse 21. She is not afraid of persecution.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 480: *subditur* [R3]
  - 482: *ad* (8 is the bold argument numeral) [R4]
  - 482: *fusum* [R3]
  - 482: *fiendo* [NW]
  - 482: *Tercio* (3 is the bold argument numeral) [R4]
  - 484: *timebit* [R4]
  - 484: *30* (Rom. VIII°, 30: x-height 0 after 3) [R3]
  - 484: *III°* [R4]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 480:
1. In codd.: socios. 16. A A,: matrona — idco deest.
;ic idem. 29. In codd.: Matth. V. 32. A: boni fuci?

p. 481:
2. B: vinea est. 10. B: super habundanciam. Et sequencia in
sermone XXXVII Augustini de Proverb. cap. XXXI mutatis aliquot
verbis invenies. i5. Codd.: per dictum. i<). B: veriticabiles.

p. 482:
2 In codd.: se ipsum. 7- B: inde qua viat. 10. A A,:
oleum deest. n. In codd.: Ut octavo. A: Litera K in loco infer.
23. A in marg. : Triplex supposicio. 24. B: suppon.t quod pius

p. 483:
1. A: l.itera L decst. 18. B: dixerunt. 20. A in marg.
Conclusio. 34. B: Nota.

p. 484:
3. B : decimo dcest. 23. A: Fetiniani. 32. A A,: decebat deest.
```

---

## Chunk 20-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-20-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-20-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "484.29–490.4"
divisions: "cap. 20 (heading 'CAP. XX.' at 471.13); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1319 words; 1139 unanimous or majority-real; 159 settled by vote (INS 1, R2 100, R3a 50, R5a 6, R6a 2); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n521–n527 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 20, part 4: [TITLE]

## ¶1 · 484.29–490.4

> [p. 484] Unde pro declaracione ulteriori huius secte ecclesie undecimo subditur: Stragulatam vestem fecit sibi, byssus et purpura vestimentum eius. Non, inquit Augustinus, decebat matronam tanti viri nudam incedere vel pannosam, sed ornatam undique preciosis. Cum enim membra que Christus induit ex clero et [p. 485] laicis tamquam vestimento qualificato varie sint contexta et matrona ista vestimentum hoc varium in se contexuit, patet quod stragulatam vestem fecit sibi, et cum de utroque membro sint alii virginitate candidi sicut byssus, alii autem vernantes martirio tamquam purpura, Christus autem amictus sit utroque istorum luminum sicut vestimento, patet quod ipsa induens Christum habet byssum et purpuram vestimenta, sicut et habet de candida anima Christi et eius natura corporea rubricata. Ex istis sequitur duodecimo quod nobilis in portis vir eius, quando sederit cum senatoribus terre; oportet enim tam ex parte bonorum quam malorum quod iste cursus finem habeat, et per consequens, oportet (ut dicitur Isaie III°, 14) quod vir veniat ad iudicium cum senioribus populi sui. Unde et Matthei XXV°, 31 dicitur: Cum venerit filius hominis in maiestate sua et omnes angeli eius cum eo, tunc sedebit super sedem maiestatis sue et congregabuntur ante eum omnes gentes. Locus autem iudicii potest propter patenciam et introitum in civitatem duplicem dici porte. Tunc patebit Christi nobilitas primo in forma duplici quoad se ipsum, secundo in totali sua ecclesia sine macula vel ruga quoad suam familiam, et tercio in expulsione servi dampnabilis inhonesti, quia eius nobilitas non sinit cohabitacionem malefici talis perpetuam nec tantam iniuriam impunitam. Sed cognoscamus quod dictus paterfamilias posuit excrescenciam de corpore sue coniugis in cuiuslibet hominis libera potestate. Ideo terciodecimo subinfertur. Syndonem fecit et vendidit et cingulum tradidit Chananeo. Syndonem intelligo doctrinam evangelicam qua tamquam lineo vestimento purissimo et subtilissimo animus induatur. Vendidit autem spirituali vendicione, [p. 486] cum Luce XIX°, 23 dicitur: Huius coniugis pecuniam suam dedit ad usuram, et sic vendicio ista est satis gratuita, de qua dicitur Isaie LV°, 1: Venite et emite absque argento et absque ulla commutacione vinum et lac. In usura autem spirituali gratis precium est datum et donans querit fructum, et sic super excrescenciam, ut compossideat ad utilitatem datarii et honorem sui, ymmo (ut recitat Augustinus) cum evangelizans habeat temporalem mercedem pro sua evangelizacione, videtur quod sit racio dati mutui et accepti. Nam I Corinth. IX°, 11 dicit apostolus: Si nos vobis spiritualia seminavimus, non est magnum si carnalia vestra metamus. Sed non est contractus civilis, cum evangelizans principaliter querit salutem populi et non sua, ideo debentur stipendia evangelizantibus non pro commutacione civiliter possessorum. Oportet ergo quod recipientes hanc syndonem dent se ipsos, quia melius est ut pro frumento spirituali vendamus nos in servos perpetuos Joseph nostro quam pro fame spirituali sub dyabolo pereamus; cum enim das te carni, mundo sive dyabolo, tantum precium das pro voluptate transitoria et peccato quantum dares pro beatitudine et pro Deo. Ideo cum istis attento tedio patet quod in dampnatis est stulta mercacio. the Cingulum autem tradidit, quando precepta evangelica N gentibus predicavit; nam Cananei erant infideles ad literam et alienigene Israel et postquam sponsus dixit suis apostolis: Ite, docete omnes gentes, Luce ultimo, dicit apostolus Ephesiorum II°, 19: Iam non estis hospites et advene, sed estis cives sanctorum et domestici Dei, quod prefiguravit mulier Cananea de [p. 487] finibus suis egressa Matthei XV°. Nam ex predicacione fidei gentibus exeuntes de gentilitatis errore accincti sunt ad precepta domini adimplenda. Et quia hoc redundat ad profectum ecclesie, ideo decimo quarto subinfertur: Fortitudo et decor indumentum eius, et ridebit in die novissimo. Nam ex insercione gentilium induit ecclesia copiosius dominum Jesum Christum. Fortitudo secundum Augustinum signat constanciam passionis sanguinee et decor florem castitatis virginee iuxta dictum superius: Bissus et purpura indumentum eius. Nam hec due virtutes invaluerunt ultra Judeam in ecclesia gencium conversarum, et exhinc nimirum habebit hec matrona iubileum in die iudicii; nec miremur quid scriptura tam crebro precipit nos induere Isaac nostrum, quia notum est quod indumenta anime sunt virtutes, Christus autem Dei virtus et Dei sapiencia et forma exemplaris extrinseca efficiens et finis sine cuius illapsi informacione non est creatura aliqua virtuosa. Habitus autem qui sunt qualitates et forme intrinsece non sunt nisi consuetudines et promptitudines ad agendum. Unde Christus illapsus membro suo tamquam sibi accidente dicitur et ipsum induere et contexens virtutibus sapiencia perornare. Unde sequitur decimo quinto: Os suum aperuit sapiencie et lex clemencie in lingua eius. Virtus enim que est sapiencia patris illapsa ecclesie fecit eam ebullire sapiencia tam secundum actus quam habitus virtutis que sunt eius vestigia, et in lingua eius ordinate ponitur lex laudandi in suo ordine domini et quodlibet opus suum. Prestet nobis, inquit Augustinus, in illa constitutis, ipsam laudantibus, illi coherentibus, cum illa et in illa tamquam matre gloriam suam expectantibus, ut et nos in timore aperiamus os nostrum attente et caute et sollicite. Nam Iª Corinth. II°, 3 scribit Apostolus: Cum timore et tremore multo [p. 488] fui aput vos. Et sequitur: Os nostrum patet ad vos o Corinthi. Ordinem, inquit, posuit lingue sue, laudans creatorem et quamlibet creaturam in suo ordine, vel pulcrius hoc ordine quo homo amat quidlibet non ut aliud sed vere in ordine bonitatis quo Deus ipsum posuit. Tunc enim vere ipsum diligit ut se ipsum; unde signanter mater nostra Canticorum IIª 4 de sponso testatur: Ordinavit, inquit, in me caritatem. Sed quia ad illud requiritur noticia philosophica qua ordines bonitatum rerum secundum sapienciam cognoscuntur, ideo sexto decimo et ultimo ita subdit: Consideravit semitas domus sue et panem ociosum non comedit. Qui enim vigilanter considerat viam per quam sanctam matrem ecclesiam oportet in Deum ascendere, contemplando ipsum ordinate in suis effectibus, ocio culpabili non vacabit, cum oportet eum studiose vigilare ad fores sapiencie increate. Et in istis sedecim stat officium matris nostre. Quoad terciam partem Cantici qua declamatur huius matrone preconium, primo sic subditur: Surrexerunt filii eius et beatissimam predicaverunt et vir eius laudavit eam. Testimonium infallibile laudis huius domine capitur ascendendo a testibus expertis qui surrexerunt a miseriis huius vie usque ad testimonium viri sui. Ipse enim est veritas increata, Johannis XIV°; multi enim surrexerunt a purgatorio et a limbo qui communicarunt nobis noticiam de beatitudine et gloria ecclesie triumphantis, et veritas testatur in facto sue transfiguracionis et in verbis sue predicacionis laudem sponse Matthei XXV, 34: Venite benedicti patris mei, percipite paratum vobis regnum; et sequitur verbum laudis: Esurivi enim et dedistis mihi manducare; [p. 489] [et modo, inquit Augustinus, in paupertate vivimus et cum morimur in paupertate dormimus, sed surgemus et vere ditabimur. Unde quia pars beatitudinis est verorum bonorum possessio, ideo secundo subditur in preconium huius matris: Multe filie congregaverunt divicias, tu supergressa es universas. Nam omnia temporalia transeunt et decipiunt quoscunque qui ea preponderanter diligunt. Ideo Matthei VI°, 19 dicitur: Nolite thesaurizare vobis thesauros in terra, ubi erugo et tinea demolitur et ubi fures effodiunt et furantur, sed thesaurizate vobis thesauros in celo; et sequitur: Ubi est enim thesaurus tuus, ibi et cor tuum. Filie autem vocantur secundum Augustinum heretici presciti, ut finaliter ab ecclesia dividantur. Inter has filias splendet ecclesia sicut lilium inter spinas: Tales, inquit, spine habent florem sine fructu; nam existentes ad tempus in ecclesia percipiunt fallaciter fidem et ecclesiastica sacramenta, eo quod eis deficit caritas consummata. Unde quia tales persepe habundant mundana gloria et fama seculi propter eius divicias, ideo tercio subditur: Fallax gracia et vana pulchritudo: mulier timens dominum ipsa laudabitur. Nam gracia laudis humane, mundane glorie vel carnalis concupiscencie declinant homines a Deo ad hostem triplicem. Ideo necesse est ut ista sit fallax gracia, quia abducit a sponso, qui est plenus gracie et veritatis. Vana eciam est pulchritudo quecunque sensibilis, cum non sit pulchritudo nisi propter proporcionalem numerum insensibilem increatum, in quo est primo per se et proprie pulchritudo (ut patet cap. Multe). Ideo signanter dicitur vanitas talis pulchritudo sensibilis et potissime temporalis. Unde rectus et per se ordo iniciandi materiam vere laudis est timor domini; ex hoc [p. 490] enim quod caste filialiter timetur sponsus, operatur mulier predicta totum bonum narratum secundum dictum ordinem sponso suo, et certum est quod talis bona operacio non potest finaliter a laude deficere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 484.29: Verse 22. She is splendidly clothed, having put on Christ.
- 485.11: Verse 23. Christ will sit in the gate at the day of judgment,
- 485.30: Verse 24. The linen garment is evangelical teaching.
- 486.26: She gives the girdle in preaching to the heathen.
- 487.5: Verse 25. She gains in glory by the grafting in of the Gentiles.
- 487.24: Verse 26. The Church is full of the wisdom of the Father,
- 488.11: Verse 27. and is not given to idleness.
- 488.19: 3. Praise of the matron.
- 488.21: Verse 28. Her praise is attested by all the elect and by Christ.
- 489.5: Verse 20. The many daughters are the foreknown who are outwardly members of the Church.
- 489.21: Verse 30. Outward grace is of no avail.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 485: *laicis* (folio mark 195c glued) [THIN]
  - 485: *ut* (print (ut; 15 is the line number) [R3]
  - 485: *III°* [R4]
  - 485: *∅* (coordinator: joined/placed by OVERRIDE (part99)) [INS?]
  - 486: *11* [R3]
  - 486: *apostolus* [R4]
  - 486: *II°* [R3]
  - 486: *Iam* [NW]
  - 486: *estis* (30 is the line number) [R4]
  - 487: *Christus* [R3]
  - 487: *Christus* [R3]
  - 487: *Iª* [R3]
  - 487: *II°* (35 is the line number) [R3]
  - 488: *ultimo* (print: et ultimo (line end) before ita; main has no ultimo token) [INS?]
  - 488: *34* [R3]
  - 489: *diligunt* [R4]
  - 489: *Ideo* (30 is the line number) [R3]
  - 490: *enim* [THIN]
  - 488: *filii* (italic) [OVERRIDE-MARK]
  - 489: *et* (196ª folio mark dropped; et (italic) is missing from output) [OVERRIDE-MARK]
  - 485: *31* (verse 31 split 3|1 by the scan (agent 11)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 484:
3. B : decimo dcest. 23. A: Fetiniani. 32. A A,: decebat deest.

p. 485:
1. A A, : sunt. 4. A A, : sunt. 6. B : amicus. 12. B : quando
dederit. 28. 29. excrescenciam. A: exc"*m; B: existentibus. 34. B:
autem — ad decst.

p. 486:
20. 21. B: pereamus — tantum deest. 23. A A,:etdeest. 3o. li:
Iam non et advene sed ; A A,: et advene deest.
i. Verba Lucae: Et quare non dedisti pecuniam meam ad
mensam, ut ego veniens cum usuris utique exegissem illam?

p. 487:
13. Codd : iubilium. 19. In codd. : que sunt. 34. H : accinctcetcaute.

p. 488:
1. Codd. : apud vos. i3. Recte : ociosa. 17. A: ad fortes.
19. A in marg. : Tercia pars. 3i. percipite; in textu Matthaei : possidete.

p. 489:
1. E: eciam modo. 2. In codd.: dormivimus; correxi e textu
Aug. 6. A: universa. 26. B: Una eciam. 3o. In codd.:
ut patet 6. Multe.
1. Aug. 1. c. pag. 191. 29. Decr. sec. pars, causa~ I,
q. I, cap. XXXVIII.

p. 490:
2. secundum. In codd. sensum. 16. B in marg. : Nota quod beati
(in cod.: bene) danl dupliccm beatitudinem. 23. Codd.: merilorium.
33. A A,: Inter alia — legimus tale deest. 34- B: legius.
```

---

## Chunk 20-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-20-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-20-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "490.5–490.34"
divisions: "cap. 20 (heading 'CAP. XX.' at 471.13); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "224 words; 219 unanimous or majority-real; 5 settled by vote (R2 4, R3a 1); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n527–n527 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 20, part 5: [TITLE]

## ¶1 · 490.5–490.34

> [p. 490] Unde quia talem vitam laboriosam imperfectam oportet habere finaliter complementum, ideo quarto et ultimo sic infertur: Date ei de fructu manuum suarum: et laudent eam in portis. opera sua. Quia nunquam in cursu vie in qua oportuit matrem nostram de nocte consurgere, pannum texere, egentes pascere et cetera opera misericordie secundum vitam activam perficere, non potest esse talis successiva continuacio in eternum, ideo precipit sponsus pro die finalis iudicii ut filii ecclesie reciproce dent sibi in quiete perpetua de fructu operum; quod est premium beatificum meritorum. Nam Luce VI°, 38 scribitur: Mensuram bonam et confectam et coagitatam et supereffluentem dabunt in sinum vestrum. Beati enim dant beatitudinem essencialem in via iniciative ex vi communionis reciproce promerendo, etdant beatitudinem accidentalem in patria obiective de sua gloria reciproce congaudendo, et sic finaliter laus erit unicuique a Deo secundum numerum meritorum; proporcionaliter enim ut predestinatus ex maiori gracia plus proficit ecclesie, habebit in portis nedum in die iudicii sed toti mundo perpetuo patulo gloriam ampliorem. Sicut enim opera dampnatorum erunt in die iudicii et post patulo toti mundo ad sui confusionem, sic opera beatorum erunt perpetuo mundo patencia ad sui glorificacionem. Et patet in parte sentencia huius Cantici continentis viginti duas proposiciones secundum numerum literarum alphabeti ebraici, cuius primus binarius hic in quatuor est divisus. Inter alia interlocutoria aspersi quod in preceptis neutris christiane fidei legimus tale.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 490.6: Verse 31. Her labour in life shall be rewarded by rest in heaven.

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 490:
2. secundum. In codd. sensum. 16. B in marg. : Nota quod beati
(in cod.: bene) danl dupliccm beatitudinem. 23. Codd.: merilorium.
33. A A,: Inter alia — legimus tale deest. 34- B: legius.
```
