# Translation brief: ecclesia 21-d–21-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-21-d.md chunks/ecclesia/wyc-ecclesia-21-e.md chunks/ecclesia/wyc-ecclesia-21-f.md` once and fix what it reports.
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

## Glossary (the 218 rows these chunks use; the full file is GLOSSARY.md)

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
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). Where privileges or law, not prayers, do the aiding: "to aid" (*Eccl.* 241.1; cf. *suffragium* "aid"), 2026-10-02. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| castra caynitica | Caim's castles | The friars' houses; the Wycliffite English name (CAIM = the four mendicant orders' initials). Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
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
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
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
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| carecter, caracter (sensibilis) | (perceptible) character | "reputation". The mark of orders. Ruled 2026-09-28 (*Dial.* 5.7). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| pseudomonachus | false monk | Kept apart from *pseudofrater* if it appears. Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| clericatus | clerical state | Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| pseudoprepositi | false superiors | Ruled 2026-10-02 (*Eccl.* 15, 358.24). |
| clerimonia | learning | The clergy's lettered state (ME "clergy"). Ruled 2026-10-02 (*Eccl.* 16, 373–374). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| ficcio | fiction | As *ficticia*; Wyclif numbers six *ficciones*. Ruled 2026-10-02 (*Eccl.* 16, 385.7). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable | Ruled 2026-10-02 (*Eccl.* 17, 398.29). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
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
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| pseudocardinales | pseudo-cardinals | Ruled 2026-10-02 (*Eccl.* 18, 426.32). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| deputacio | deputation | Ruled 2026-10-02 (*Eccl.* 19, 443.34). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |

---

## Chunk 21-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "502.10–506.30"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 4 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1075 words; 973 unanimous or majority-real; 91 settled by vote (INS 1, R2 67, R3a 22, R6a 1); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n539–n543 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 4: [TITLE]

## ¶1 · 502.10–503.31

> [p. 502] Quarto arguitur per hoc quod caracter est signaculum perpetuum, manens in anima separata, ergo non debet imprimi nisi ad actum perpetuum; sed actus ministerialis istorum ordinum inferiorum non est perpetuus. Ergo etc. Dicitur, inquit, quod non oportet ut maneat semper quantum ad usum ministerii quod iste usus vel abusus convertitur in premium vel mercedem. Unde secundo querit et tenet quod in diversis ordinibus diversi imprimuntur caracteres distincti, et hoc specifice, sicut ordines, ut oportet eum dicere, et arguendo quadrupliciter ad oppositum respondet. Dicendum, inquit, quod inter opinantes in omnibus ordinibus esse caracterem duplex opinio esse consuevit. Quidam enim dicere volunt quod omnes ordines in uno caractere uniuntur; differunt tamen secundum maiorem implecionem et minorem, sicut si sigillum imprimatur in cera tenui, deinde forcius vel amplius, paulative procedendo secundum plus et plus quousque perveniatur ad statum perfectum. Si autem queras que sit racio talis impressionis, respondeo breviter quod hoc est propter [p. 503] caracteris imperfeccionem; et tripliciter reprobat istam opinionem satis vivaciter. Primo, inquit, si hoc esset, tunc esset impossibile promoveri ad sequentem ordinem dimisso priori; quod est contra iura. Item, tunc non esset differencia inter ordines nisi secundum maius et minus; quod est manifeste falsum, cum potestates in diversis ordinibus sunt ad diversa ordinate. Et tercio, si caracter sic susciperet magis, per idem posset suscipere minus, et per consequens foret delebilis, et per idem caracteres aliquorum sacramentorum magis et minus reciperent, ut dicatur baptizatus vel confirmatus magis et minus; quod est domnino inconveniens. Ergo et posicio. Alia possunt fieri argumenta quod per idem caracter baptismi crescere posset ad qualemcunque caracterem. Oportet enim in casu concedere quod duorum acolitorum caracter sacerdotalis fuit impressus in uno, et in alio non, posito quod alter cresceret in posterum in sacerdotem et alter maneat tantum acolitus, et foret confusio in sacerdocio secundum magis et minus. Ideo dicit secunda opinio melius quod in diversis ordinibus imprimuntur diversi caracteres, eo quod non solum qui ad Dei cultum assumuntur, distinguuntur ab aliis, ymmo inter ministrantes est ordo atque distinccio, et ulterius gradus illi et potestates ministrandi, si simul dantur, nunquam auferuntur, eciamsi ad alcius ministerium elevatur qui in minori ministraverat; et ideo in diversis ordinibus diversa sigilla debent imprimi secundum que nobis diversitas potestatum ministrandi et perpetuitas innotescat; tale autem signaculum est caracter.

[ENGLISH]

## ¶2 · 504.1–506.12

> [p. 504] Ideo in diversis ordinibus imprimuntur diversi caracteres, et concedende sunt raciones hoc ostendentes. Ad primum in oppositum quo sic arguitur in sacramento baptismi non imprimitur nisi unus caracter; similiter in sacramento confirmacionis, ergo pari racione in sacramento ordinis. Dicendum, inquit, quod non est simile pro eo quod non ponit ita diversitatem, sicut ponit ordinis sacramentum quod de sui racione implicat diversitatem graduum. Ad secundum quo sic arguitur sacramentum ordinis essencialius respicit caracterem quam aliquod aliud sacramentum in quo caracter imprimitur; si ergo ordo unum est sacramentum quantumcunque plurificetur, videtur quod unus caracter in eo imprimitur. Dicendum quod verum est, sed nonnisi prout comparatur ad ulterius signaculum. Sicut ergo una litera est scripta et due et tres et quattuor et tamen multarum literarum aggregacio ad unam sentenciam exprimendam non est nisi una scriptura: sic in proposito intelligitur quod omnis talis figuracio ordinatur ad hoc quod ei inscribatur signaculum secundum quod homo Dei minister perfectus esse iudicatur, et cum sacramentum dicat quid ad alterum, et eciam caracteres uniuntur secundum quid ad alterum, ideo plures caracteres unum faciunt sacramentum. Tercio sic arguitur: Si plures caracteres in eadem anima imprimuntur, aut ergo differunt specie vel solum numero; non secundo modo, quia oportet recipiens denudari a natura rei recepte, nec primo modo, quia ex diversis secundum formam et speciem manentibus non fit unum nisi unum materiale. Ad illud dicendum, inquit, quod dupliciter est loqui de [p. 505] caracteribus vel in se vel prout uniuntur in unitate et integritate subiecti. Si in se, sic differunt, sicut diverse species numeri, si secundo modo, tunc sicut binarius et quaternarius constituunt senarium et habent racionem partis constitutive et complementum ponitur in senario, sic intelligendum est in proposito suo modo, licet non sit omnino simile. Quarto arguitur per hoc quod natura non facit per plura quod facere potest per unum, ergo autor nature non imprimit in ordinato multos caracteres, cum solum unus sufficit, sicut evenit in baptismo. Que ergo necessitas ponendi in ordine tam distinctos caracteres? Dicendum, inquit, quod hoc verum est, quando aliquid potest per unum ita complete fieri ut per plura; hoc autem non fit in proposito pro eo quod oportet ordinatos non solum distingui ab aliis, sicut fit caracter baptismi, sed oportet ipsos distingui plus quam materiali differencia in se ipsis. Expergiscat rogo auditorium et consideret si iste locus et sermo doctorum dat efficax testimonium ad rantasiandum quod solum in ordine sacerdotali caracter imprimitur, cum tam spissim manifeste testatur oppositum. Et revera homo cui ars menciendi non foret laudabilis verecundaretur de tam patente mendacio. Ille autem qui vel intenderit omnia dicta sua capi yronice vel mendacium sibi ascriberet ad honorem, daret occasionem ut non credatur amplius allegacioni vel testimonio suo eciam quicquid iuraverit. Ex primo igitur commento colligitur quod doctor iste vel falsificat multipliciter testem suum, vel quod testificacio sequens sit omnino mendosa et nimis inutilis, cum ipse et testis suus tam crebro et tam patule contradicunt. Quomodo queso invocarem racionabiliter suffragium testimonii [p. 506] doctoris in eadem opinione et eodem libro quem in eadem opinione implico cencies esse mendacem? per inde quidem foret allegandus dyabolus in testem sentencie, cum notum sit quod ex cautela et subtilitate ingenii plurima vera dicit. Et hec racio quare quietor in allegacione scripture que mentiri non poterit et sanctorum doctorum quorum sentenciam volo ex integro sustinere. Alios autem doctores nolo sic allegare nisi arguendo ad hominem, cui foret talis doctoris testificacio argumentum, et sic allegarem contra mendacem oratorem dyaboli ipsum patrem mendacii, sed non ut sit mihi testis ydoneus.

[ENGLISH]

## ¶3 · 506.13–506.20

> [p. 506] In isto autem secundo commento absque tergiversacione patet primo mendacium allegantis; patet secundo quod non solvitur argumentum quod feci supponendo descripcionem clerici, per hoc quod mendaciter allegatur quod solum in sacerdocio caracter ordinis imprimatur; et tercio quod ista sentencia conviccionis mendacii foret medium doctori isti mihi et aliis cavendi caucius de mendosis allegacionibus in futurum.

[ENGLISH]

## ¶4 · 506.21–506.30

> [p. 506] Scola quidem mendacii est per se a Deo et tota ecclesia detestanda dicente venerabili Anshelmo primo: Cur Deus homo cap. XII°: Non, inquit, sequitur si Deus vult mentiri, iustum est mentiri (supple si non ex possibili), sed pocius sequitur dominum illum non esse. Nam nequaquam potest velle mentiri voluntas, nisi in qua corrupta est veritas, ymmo que deserendo veritatem corrupta est. Quid ergo sequitur ex ista responsione mendacii? Revera mendacium mendacio cumulatum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 505.19: These quotations enable us to estimate our Opponent's power of lying.
- 505.28: Bonaventura either contradicts himself; or is falsely alleged.
- 506.1: In either case he is valueless as an authority.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 502: *Quidam* [R4]
  - 503: *caracteris* (folio mark 197d glued) [THIN]
  - 503: *imperfeccionem* [THIN]
  - 504: *arguitur* [R3]
  - 504: *figuracio* (20 is the line number) [R4]
  - 505: *quaternarius* [R4]
  - 505: *rogo* [R3]
  - 505: *locus* (20 is the line number) [R4]
  - 505: *suffragium* [THIN]
  - 506: *quorum* [R4]
  - 506: *∅* (print tergiver-|sacione; main has tergiversacione whole at pos 96) [INS?]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 502:
6. A in marg.: Responsio. 8. A A,: signaculum destitulum :
B: distinctum. i3. B: ministralis. 14. A in marg.: Responsio.
17. A in marg.: Opinio. 18. B: diversis imprimuntur. 23. A in
marg.: Duplex opinio. .25. A in marg.: Prima.
25. Bonav. 1. c: minorem complexionem.

p. 503:
2. A A,: satis vivaciter deest. 11. B: recipercnt — minus dcest.
21. A in marg.: Secunda opinio. 26. B: sed simul. A A, : licct
semel. Ibidem codd. : eciamsi alterius. Correxi. So. B: peccatum
23. Bonav. 1. c. pag. 602 seqq.

p. 504:
6. A in marg. : Responsio. i3. 14. B: purificetur. i5. A in
marg. : Responsio. 16. Operatur in codd. Jbid. si ergo in codd.
20. sciencie figuracio in codd. 23. A A,: Sed quidcm secundum
quid — caracteres deest ; ibid. Sed quidem ad alterum in codd. 27. A A, :
ac ergo difierunt. 3i. B: unum sit. 3i. 32. Ad aliud in codd.
32. A in marg. : Responsio.

p. 505:
i\. ln codd.: tcrnarius. 6. A A,: sicut intelligendum. i3. A in
marg.: Rcsponsio. 16. In codd.: distigui 20. A A,: logicus
ct scrmo. 28. B: primo crgo.

p. 506:
22. A in marg. : Anselmus; in codd. cap. X. 24. 25. Recte: si
ex non possibili. 32. A in marg.: S. Thomas.
22. Anselmi Opp. tom. I, pag. 80. 32. Thomae lib. IV.
Sent. Opp. tom. X, pag. 442.
```

---

## Chunk 21-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "506.31–510.26"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 5 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "932 words; 868 unanimous or majority-real; 55 settled by vote (INS 1, R2 28, R3a 21, R3b 3, R5a 2); 9 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n543–n547 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 5: [TITLE]

## ¶1 · 506.31–510.8

> [p. 506] Tercium commentum est ficcio testimonii sancti Thome quod in solo ordine sacerdocii vel suo subdito [p. 507] caracter ordinis est impressus, et limitatur locus super distinccione XXIVª quarti Sentenciarum; et indubie tractat istam sentenciam ibidem, questione secunda, articulo tercio, recitandoque tres opiniones, ut doctor Bonaventura; quarum prima dicit quod in solo ordine sacerdotali caracter inprimitur; secunda quod in solis sacris ordinibus, sed hoc, inquit, iterum nichil est. Unde, inquit, cum caracter sit signum distinctivum ab aliis, oportet quod in omnibus ordinibus imprimatur, cuius eciam signum est quod oportet quod caracteres perpetuo maneant et nunquam revertentur. Et respondet ad tria argumenta in oppositum, sicut supra. Et patet quod nec hoc est conveniens testimonium ad probandum solum in ordine sacerdotali caracterem esse impressum, cum militat directe in oppositum; et revera cum mendacium in castris armorum corporalium tamquam eis contrarium sit oditum, (ut patet Machabeorum VII°), multo magis in castris scolasticis in quibus militarent solum pugiles veritatis. Sed instatur tripliciter: Videtur enim primo quod uterque istorum doctorum ponat caracterem omnino indelebilem, ego autem dixi superius quod caracter aliquis est tantummodo temporalis. Hic dico quod neuter eorum est mihi autenticus. Ideo non allego eos nisi arguendo ad hominem. Dico tamen quod glossari possunt intelligendo per caracterem esse vel fuisse deputatum ad aliquod sacrum ministerium in sancta ecclesia, et hoc non potest desinere esse, et ideo dicit prior doctor quod caracter manet perpetuo in officio vel premio; nam in predestinatis manet post miliciam quod illi fuerunt deputati ad officium [p. 508] temporale propter cuius complecionem perpetuo premiantur, sicut in prescitis manet perpetuo quod ipsi perpetuo puniuntur propter abusum sui officii, et ad istum sensum omnis caracter manet perpetuo in officio vel mercede. Ego autem loquebar de caractere ut dicit simpliciter deputacionem ad officium, nec credo quod ex scriptura vel racione improbabitur sensus iste. Non enim est caracter talis una res que poterit per se esse, sed subiectum taliter se habere. Sed secundo videtur quod in omni homine, et per consequens in omni ordine caracter imprimitur, et sic reges et milites haberent gloriosum caracterem correspondenter ad suum ordinem. Hic dico quod extense loquendo de caractere (ut supra) est conclusio concedenda, nam omni homini deputat Deus officium ad profectum ecclesie. Ideo cum oportet omnem hominem esse servum Christi vel agendo vel paciendo, omnem hominem oportet portare de secta sua uno modo vel alio. Nec credo aliquem infringere quin, sicut milites spirituales Christi habent caracterem sui officii, sic et reges ac milites corporales (ut patet inferius). In tribus tamen sacramentis specialiter caracter imprimitur, scilicet baptismo, confirmacione et ordine, que tria sacramenta sunt initerabilia ut officia caracterum indelebilia quoad effectum vel fructum. Nam in baptismo recipit servus Christi distinccionem ab omnino infidelibus, in confirmacione roboracionem sue milicie, in ordine vero recipit singularem limitacionem supra laicos ad ministerium sacramenti. Et ita doctores palliant descripciones et applicant scripturam ad sensum quem asserunt, ut patet de caractere, de ordine et ceteris que vix habent corticem apparencie ex scriptura, ut ordinem militarem dicunt non habere caracterem, quia ille ordo non limitatur ad differenter a laicis ministrandum ecclesiastica sacramenta (de quo alibi). [p. 509] Sed tercio dubitatur quomodo illi caracteres ordinum unum constituunt. Et dicunt doctores predicti, quod nec sunt partes quantitative ordinis nec partes subiective sed partes potestative, ut patet prioris doctoris super d. XXIV°, ita quod ordines inferiores habent potestatem a sacerdocio ad quod finaliter ordinantur. Sicut ergo senarius constat ex partibus suis aliquotis que non sunt partes eius quantitative, sic sacramentum ordinis constat ex suis partibus, sed illud latinum videtur multis difficile. Nam signato Petro qui vicissim assumpsit septem ordines et maneat modo cum illis omnibus, patet quod si quilibet eorum fuit sacramentum quia ordo, per idem quilibet eorum est modo sacramentum quia ordo. Nam eiusdem racionis est quilibet eorum cuius foret quilibet huiusmodi per se sumptus, sed tunc foret ordo et sacramentum, ergo et modo. Si enim quilibet eorum sit ordo, ergo vel idem ordo in numero qui posterior, vel alius non idem in numero, quia sic foret ydemptificacio numeralis, et si alius, tunc forent septem ordines, et per consequens, cum quelibet multitudo priorum constituit unum ordinem, forent quatuordecim vel plures ordines distincti specifice. Nam sicut ordo inferior et ordo superior sunt disparis speciei, sic ordo sacerdocii constans ex sex ordinibus precedentibus et ordo sacerdocii simplex non habens partes vel causas huiusmodi forent disparis speciei, sicut simplex et compositum. In isto videtur mihi primo notandum quod ordo sumi potest tripliciter satis equivoce. Primo analogice pro gradu in quo Deus ordinat quicquam constitui ad pulchritudinem universi, et sic quelibet res habet suum ordinem in tantum quod necesse est [p. 510] peccatores ex hoc quod dissolvunt ordinem debitum ad quem ex institucione primaria ordinantur subire ordinem puniendi, sic quod (ut multis videtur) peccatum in quantum bonum habet racionem ordinis quoad penam, quia ordo et bonum quoad consequenciam convertuntur, unde congregaciones hominum in quibus ordinacior est unio vocantur ordines secundum quandam excellenciam inferioribus exemplarem (ut dixi alias).

[ENGLISH]

## ¶2 · 510.9–510.26

> [p. 510] Secundo modo accipitur ordo pro gradu a Deo limitato clerico ad differenter a laycis sacramentaliter ministrandum, et sic sunt septem ordines scilicet hostiarius, ceroferius, lector, exorcista, subdyaconus, dyaconus et sacerdos de quibus dixi superius). Illi autem ordines quandoque sumuntur limitate pro caracteribus subiectatis in anima et quandoque respiciunt signacula sensibilia extrinsecus distincta, cuiusmodi sunt rasio capitis et barbe cum similibus signis humanitus institutis. Isti autem sensibiles caracteres non sunt ordo clericalis, quia sic continue variarentur ordines ad crementum, decrementum vel aliam variacionem istorum signorum, et barbitonsor vel alius laycus frequencius conferret ordines; quod foret ridiculum. Ideo necessitantur loquentes ponere ordines subiectari in anima. Ex quo patet quod anima est persona que est ordinatus, ut puta, diaconus vel sacerdos. Iste ergo ordo manet quietus in anima corrupto episcopo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 507.1: Again my opponent quotes St. Thomas who is also adverse to him.
- 507.20: These doctors are alleged against me, but I do not admit their authority.
- 508.7: The "stamp" or character is not a thing, but a relation. Every rank has its character.
- 508.21: Yet three sacraments: baptism, confirmation and orders imprint the character in a special way.
- 509.1: Difficulties as to the grades of orders.
- 509.13: Either all orders are identical, or there are numerous orders specifically distinct.
- 509.25: I think orders may be taken in three senses; a) as the position which God assigns to each thing.
- 510.9: b) as a rank assigned by God to clerics for ministering sacramentally;
- 510.22: and such orders are in the soul.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 506: *subdito* (print sub-|dito; main token holds the whole word with folio mark 198b glued (no separate dito token)) [THIN]
  - 507: *∅* (coordinator: joined/placed by OVERRIDE (part99)) [R4]
  - 507: *indubie* [NW]
  - 507: *oditum* [NW]
  - 508: *vel agendo* (one main token covers two printed words) [R5]
  - 508: *imprimitur* [THIN]
  - 508: *scilicet* [THIN]
  - 508: *∅* (English side-note word "confirmation"; print text line has baptismo, confirmacione (pos 170-171)) [THIN]
  - 507: *XXIVª* (XXIVª split XXI|Vª (agent 11)) [OVERRIDE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 506:
22. A in marg. : Anselmus; in codd. cap. X. 24. 25. Recte: si
ex non possibili. 32. A in marg.: S. Thomas.
22. Anselmi Opp. tom. I, pag. 80. 32. Thomae lib. IV.
Sent. Opp. tom. X, pag. 442.

p. 507:
10. AA,: quod careat; careat extinctum. 20. A in marg.: Triplcx
obicccio. Responsio. Auctoris sentencia.
8. Bonaventura lib. IV. Sent. dist. VI, pars II, art. I, quaest. IV
et dist. XXIV, pars II, art. I, quaest. I, Conclusio Opp. tom. IV,
pag. 65 1.

p. 508:
i3. A in marg.: Responsio. 21. A in marg.: In tribus sacramcntis
caracter imponitur. 24. A: indclibilia.

p. 509:
4. A A, : ut — potestatem deest. 7. A in marg. : Hcc cst sen-
tencia auctoris de potestate et caractere ordinis continue infra (Above
108° without mark of rcfercnce). 10. A in marg. : Casus. 29.A B in
marg. : Nota quod ordo tripliciter accipitur. 3|. B: habet ordinem.
5. Cf. Thomae Lib. IV. Sent. 1. c. pag. 424.

p. 510:
i. B: primaria obligantnr. 34- circumcisione; ita codd. Rectins
et intercisione. cf. pag. 5n. I. 29. 3i.
```

---

## Chunk 21-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-21-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-21-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "510.27–514.34"
divisions: "cap. 21 (heading 'CAP. XXI.' at 491.1); part 6 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "981 words; 918 unanimous or majority-real; 58 settled by vote (INS 2, R2 35, R3a 18, R3b 1, R5a 1, R6a 1); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n547–n551 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 21, part 6: [TITLE]

## ¶1 · 510.27–512.25

> [p. 510] Sed tercio modo sumitur ordo pro sacramento sensibili quod est ordinancia episcopi ad sacrum officium supra laycos jn ecclesia ministrandi, et si res abscondita huius sensibilis sacramenti est ordo vel caracter insensibiliter subiectatus in anima, et ordo est opus sensibile ab episcopo celebratum quod in verborum sacramentalium prolacione, in ritus, tactus aut unccionis ministracione et in circumcisione extrinsece, ut loci, [p. 511] temporis, persone ordinande et superiorum licencie attencione. Unde dicitur communiter quod regulariter in celebracione ordinum rite facta Deus graciose coassistit dando graciam. Et ideo necesse est peccatorem ordinandum conteri de peccatis. Deus enim dans potestatem ad ministrandum dat eciam graciam ad officium exequendum nisi indisposicio ordinati prepediat. Unde in baptismo et quocunque alio sacramento subducta assistencia Christi dantis graciam, que sit res sacramenti, fit ex indisposicione suscipientis sacramentum equivoce. Verumptamen Deus post sacracionem episcopi sepe facit ordinem reminiscere, ipse enim dat regulariter rem sacramenti, et sic facit sepe ordines nobis incognite. Unde vacuum videtur mihi quod sollicitemur ad querendum quando, qualiter et quibus verbis Deus ordinavit apostolos vel beatum Paulum aut alios discipulos. Cavere tamen debemus solicite ne pseudoclerici fingant se esse ordinatos a Deo ad tale officium clericatus. Ad hoc enim ordinatur ordinandi examinacio, episcopi celebracio et signorum sensibilium figuracio, ut sic innotescat ecclesie discolorum exclusio; utrobique tamen sepe contingit illusio. Et (ut sepe dixi) credendum est precipue operi legitimo ordinati. Istis premissis videtur mihi quantum ad primam conclusionem quod, sicut ordo acceptus tercio modo est aggregatum ex multis signis sensibilibus, eciam paulatim in diversis et intercisis temporibus celebratis: sic ordo superior acceptus secundo modo est aggregatum ex diversis caracteribus sive signaculis; quos Deus dat appropriate simul vel intercise, et sunt eius partes quantitative non quoad molem, sed quoad potestatem, ita quod, quotquot actus legitimos quis sufficit facere, tot caracteres habet datos a Deo compositos [p. 512] proporcionaliter cum se ipsis. Sed ne subditus diffidat de potestate sui prepositi, cum in cessacione cuiuscunque officii unus caracter extinguitur, Deus dedit caracterem superiorem, qui est limitacio ad sufficienciam dati generis ministerii indistincte, et talem caracterem non potest ordinatus deserere, quamdiu manet in eo potencia ad signa sensibilia ministrandum. Suspendi tamen potest a superiori propter causam racionabilem, ne ordinatus ponat tunc caracterem in effectum. of Et si queratur necessitas ponendi tot caracteres, dicitur quod admissa significacione quid nominis, et supposita ordinacione divina de dividendo diversis hominibus diversas gracias officii gratis datas, sequitur inevitabiliter predicta diversitas caracterum. Unde ad fundandum istam sentenciam oportet primo supponere fidem scripture Iª Cor. XII°, 4— 7: Divisiones graciarum sunt, idem autem spiritus; et divisiones ministracionum sunt, idem autem dominus, et divisiones operacionum sunt, idem autem Deus qui operatur omnia in omnibus. Unicuique autem datur manifestacio spiritus ad utilitatem. Et post in corpore ecclesie explicat novem gradus. Nec licet denegare talem ordinem concedendo corpus ecclesie vel eius ministros secundum iura canonica.

[ENGLISH]

## ¶2 · 512.26–513.21

> [p. 512] Unde notanda est trimembris divisio textus apostoli. Aliqua enim donat Deus predestinatis que vocat gracias a spiritu sancto datas, quia predestinatis timentibus Deum omnia cooperantur in bonum. Unde quia cum istis donis stat mortale secundum presentem iusticiam, ideo vocantur gracie gratis date ex benevolencia spiritus predestinantis. Ministraciones autem sunt in qualibet creatura racionali predestinata [p. 513] vel prescita, quam oportet servire domino libere vel coacte; ideo adiungit apostolus illud secundum membrum ad dominum. Sed tercio omnis natura creata saltem per se existens habet apud creatorem suum officium operandi. Ideo notat illud tercium generale sub habitudine ad Deum creantem. Istis suppositis patet quod omnis clericus habet a Deo secundum suum gradum limitacionem officii ministrandi, et illam voco ego caracterem quem oportet omnem fidelem admittere cuicunque membro ecclesie et nullum alium. Quod autem alii capiunt terminum striccius in uno sensu et alii largius in alio, non est magna vis, cum sit terminus magistralis, verumptamen loquendum est (ut plures loquentes scripture et racioni conformius), et patet responsio quomodo aliquis caracter cessat completo officio, et talis dividitur proporcionaliter ut eius officium. Et ille vocatur caracter in actu, et alius caracter dicit potestatem ad confuse faciendum ministerium, sive sequatur sive non, et ille non dependet ab opere sed a sufficiencia operis quoad speciem terminantis, et iste modus loquendi videtur facilior.

[ENGLISH]

## ¶3 · 513.22–514.20

> [p. 513] Ulterius patet quod est dare septem ordines secundo modo dictos, distinctos specifice, sed nullus eorum est sensibile sacramentum, sed res vel fructus eius. Sacramentum autem ordinis quod sacerdos celebrat est quodammodo unum secundum magnam partem sui subiectatum in ordinante, quia finis a quo capitur eius unitas est totum sacerdocium tocius sacerdotis ecclesie, nec resisto quin sunt diversi ordines distincti specifice tam sacramenta quam res sacramenti; omnes tamen illi ordines sunt unus ordo, et sic sunt tantum septem sacramenta, licet sit tantum unum sacramentum, sicut Crisostomus, Omelia prima, dicit de septem ecclesiis. [p. 514] Et patet primo quod ordinans hominem primo et immediate in sacerdotem eo ipso dat sibi vel ministerialiter signo sacramentali ostendit quod habet septem ordines sive caracteres. Patet ex hoc quod eo ipso limitatur ad potestatem septemplicem quod est ordo. Non enim foret sacerdos univoce nisi haberet potestatem ad ministrandum quamcunque speciem spiritualis ministerii quo sufficit ministrare clericus graduatus inferior. Immo quot sunt species officii in quas graduatus potestative sufficit, tot sunt ordines sive caracteres. Omnes tamen sunt unus ordo cuius partes integrales vocari possunt partes potestative, sicut pars senarius communis ad quamcunque unitatem eius vocatur prima pars eius aliquota, et pars eius communis ad quemcunque eius binarium vel ternarium vocatur secunda et tercia pars eius aliquota, ex quibus adequate constat senarius. Unde si Deus per impossibile daret clerico potestatem conficiendi et non absolvendi, ille non foret sacerdos, si non equivoce, et patet secundo quod

[ENGLISH]

## ¶4 · 514.21–514.23

> [p. 514] sicut res sacramenti ordinis, sic res diversorum sacramentorum sese essencialiter consequuntur. Nam oportet

[ENGLISH]

## ¶5 · 514.24–514.31

> [p. 514] recipientem efficaciter ordinem prius baptizari baptismo flaminis, sicut oportet eum confirmari aliquo gradu divine confirmacionis, sponsari capiti ecclesie, habere fructum penitencie, unionem eucaristie et unccionem gracie consummate. Verumptamen in sacramentis nostris sensibilibus est ordo per accidens ex institucione ecclesie, ad quem ordinem magis appreciando

[ENGLISH]

## ¶6 · 514.32–514.34

> [p. 514] intendimus quam ad rem vel fructum appreciando sacramenti sensibilis, et ista irregularitas qua magis attendimus

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 510.27: c) as the sensible sacrament of ordination by the bishop.
- 511.5: God gives the grace of the sacrament unless hindered by unworthiness in the recipient.
- 511.18: The purpose of formal ordination is to exclude unworthy pretenders.
- 511.26: As outward orders are conferred by several rites, but are finally one, so spiritual orders are such powers as are gradually or at once given by God;
- 512.2: who also gives a power which makes the ministration of the ordained effectual.
- 512.11: This variety of characters is declared in Scripture.
- 513.6: Every cleric has a duty assigned by God according to his degree,
- 513.12: and this is what I call his "character".
- 513.22: There are seven orders, but they all combine to make one order.
- 514.1: Ordination to the priesthood confers the power of performing all spiritual ministrations.
- 514.20: As the various orders are combined in one, so the grace of each sacrament combines with the rest.
- 514.31: We are apt to attend too much to the outward sign.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 511: *temporis* (folio mark 198c glued) [THIN]
  - 511: *officium* [R4]
  - 512: *Iª* [R3]
  - 514: *appreciando* [THIN]
  - 514: *∅* (duplicate: baptismo already at 161) [DELX]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 510:
i. B: primaria obligantnr. 34- circumcisione; ita codd. Rectins
et intercisione. cf. pag. 5n. I. 29. 3i.

p. 511:
i5. A in marg. : Nota. 26. A in marg.: Rcsponsio.

p. 512:
7. B: in ea. II. A in marg.: Questio. 12. B: signacione.
29. Rom. VIII, 28.

p. 513:
7. A I? in marg. : Quid cst caracter. 8. p. B : ministrandi deest ;
ibid A A,: ego deest.

p. 514:
1 A in marg.: Crisostomus. Prima conclusio. 7- 8. B : quarn-
cunque pem. «■ A in marg. : Nota. M- A b. marg. : Secunda
coSsioP 22. B. consequentur. 26. A A». fructum finem.
27. B: gracie confirmate.
24. baptismo flaminis; cf. Trial. p. 2
```
