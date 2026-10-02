# Translation brief: ecclesia 11-a–11-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-11-a.md chunks/ecclesia/wyc-ecclesia-11-b.md chunks/ecclesia/wyc-ecclesia-11-c.md` once and fix what it reports.
6. Final message: per chunk, the ledger rows (table: id | chunk / note | claim | status | how / next step),
   glossary proposals, Latin doubts, and a one-line note of anything the coordinator must decide.


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

## Glossary (the 158 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
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
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| conducentes | those who hire them | Ruled 2026-09-28. |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
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
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| inobedienciarius | disobedient man | The negative of *obedienciarius*. Ruled 2026-10-02 (146.11). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| indebitare se | to make oneself a debtor | Sense doubtful; C note (*Dial.* 85.15). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 11-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-11-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-11-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "227.20–232.33"
divisions: "cap. 11 (heading 'CAP. XI.' at 227.19); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1243 words; 1142 unanimous or majority-real; 80 settled by vote (R2 44, R3a 23, R5a 10, R6a 3); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n264–n269 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 11, part 1: [TITLE]

## ¶1 · 227.20–232.33

> [p. 227] Cum elemosina tantorum principum non debet omnino extingui propter sinistram interpretacionem abutencium, sicut nec veritas scripture sacre frustrari debet a suo lumine propter hereticos qui sinistrum sensum occasione male accepta ex ipsa eliciunt, videndum est ad quem sensum dictum privilegium debet concipi, ut remaneat tam re quam nomine privilegium utrobique. Igitur inprimis, cum illius sit interpretari leges ac privilegia cuius est condere (ut patet XXVª lq. I, Ideo permittente, et V° Decretalium, De Sentencia [p. 228] Excomunicacionis, Inter alia), rex autem Anglie debet concedere et condere leges tales privatas de suo regali dominio ad edificacionem ecclesie: ideo capiendum est tamquam per se notum quod regis est illas leges privatas ac elemosinas interpretari et in rectitudine sua defendere. Romanus autem pontifex super isto consultus, et sacerdos suus legius requisitus de interpretacione sensus catholici, tenentur de lege evangelii quantum sciunt humiliter declarare; quibus non est parendum nisi de quanto sentenciam suam fundaverint in scriptura sacra. Unde secundo oportet supponere quod sacram theologiam necesse sit omnem talem scienciam principaliter regulare; patet ex hoc quod illa sola principaliter docet viam qua celeste coniugium honoratur, sed iuxta hunc finem regulandum est omne factum viatoris legitimum; ergo conclusio. Et ista est sentencia XXª dist. De quibus, ubi Innocencius papa docet quinque gradus procedendi in dubiis discernendis, primo in quantum recurrendum est ad scripture auctoritatem quam episcopi et specialiter papa usque ad sanguinem tenentur defendere, ut patet XXVª, q. I. Sunt quidam. Secundo si ex scriptura sacra in lingua latina solucio dubii non clare eluceat, recurratur ad scripta greca, ut vel sic divina sentencia habeatur. Tercio si nec sic lux veritatis appareat, ad ecclesiasticas historias catholicas congregatas a sanctis doctoribus, mitte manum. Quarto si nec illis eluceat difficultas que queritur, sanctorum exempla perspicaciter recordare, exempla enim vite sanctorum debent esse nobis speculum conversandi. [p. 229] Quinto si omnibus istis inspectis questionis qualitas non lucescat, per decretum seniorum provincie ad hoc congregatorum mediante Dei assistencia qui non potest suis deficere, decidatur. Tercio suppono: Cum dictum privilegium non fundatur m iure canonico vel civili, sed specialiter in legibus regni nostri et cartis illius ecclesie superius recitatis, quod notetur forma et finis gracia cuius hec privilegia sunt concessa (finis enim ex secundo Phisycorum mensurat omnia media ad eundem), in privilegiis autem regis Edgari triplex finis exprimitur, scilicet reverencia Dei in reliquiis sui apostoli, quies monachorum ibi degencium et honor sanctitatis illius peculiaris basilice in qua degant speciales oratores pro rege et regno de quorum elemosinis ad hoc specialiter sustentantur. Unde in bulla Nicolai III sic habetur: Monachi ibidem nulli omnino persone subdantur nisi regi. Ex quo videtur quod incole illius loci, non solum quia legii homines regis, nec solum quia speciales eius elemosinarii sed ex mandato pape regi suo specialiter sunt subiecti; nam secundum beatum Gregorium multiplicitas beneficiorum auget obligacionem beneficiati ad suum datarium. Ex quo videtur, cum monachi illius loci regi tam singulariter sunt subiecti, nec hospites vel fugitivi sui debent esse plus exempti vel privilegiati quam monachi a quibus emanat privilegium, videtur quod omnes profugi, de quanto sunt in illo loco, regi Anglie quadam preeminencia sunt subiecti ex hoc quod ab eo ibi recipiunt beneficium singulare; nec consonat fidei religionis Christi quod monachus, si per possibile occiderit hominem in dicto loco, erit post liberior et plus percipiens de fructu privilegii, quam quando fuit immunis quoad Deum et [p. 230] hominem magis capax. Nec videtur racionabile quin, supposita capacitate in monacho vel quocunque famulo illius loci, habebit fructum privilegii post delictum eciam pocius quam unus extraneus; aliter enim omnis contumaciter ibi quiescens in crimine ut sic indisponeret se ad habendum privilegium supradictum. is Istis premissis videtur mihi (ut alias) quod, licet per totam Angliam indulgeri debet omnimoda remissio, de quanto sonat in misericordiam et non ultra, tamen pro loco Westmonasterii servari debet generalis talis remissio virtute singularis privilegii pie concessi a regibus illi loco. Prima pars patet ex hoc quod privilegia cum (in quantum huiusmodi) sonant per se bonum, sunt racionabiliter amplexanda; nam melius esset quod tota ecclesia haberet privilegium, hoc est, legem ad sui commodum quam quod aliqua pars ecclesie a privilegio vero deficiat, quia de tanto peccat vel punitur de quanto deficit a plenis privilegiis beatorum. Et patet quod nullum est privilegium, nisi de quanto sonat in elemosinam vel opus misericordie, quia non est privilegium, nisi de quanto misericorditer datur a Deo, vergens homini ad profectum. Et secunda pars patet ex hoc quod oportet concessionem regis habere specialem efficaciam ibi diligencius observandam, nam aliter foret frustra. Et ex istis patet quod nullum privilegium est iuri communi contrarium, nam si foret, tunc esset contra iusticiam et per consequens lex iniqua et non privilegium. Unde videtur mihi omnino insipidum dictum quorundam dicencium quod non esset privilegium nisi foret iuri communi contrarium. Nam licita variacio ritus pro loco et tempore non est contrarium veritati et per consequens nulli legi. Ideo oportet privilegiantes omnino attendere, [p. 231] ne subtrahant iusticiam vel inferant iniuriam alicui. Unde XXVª q. II, Quod vero, dicit Gregorius: Absit hoc a me ut statuta maiorum cum sacerdotibus meis in qualibet ecclesia infringam, quia mihi iniuriam facio, si fratrum meorum iura perturbo. Et indubie idem foret iudicium de quolibet viatore, quod si privilegiando precludit cuicunque iusticiam, dampnificat tam se quam privilegiandum; quod non licet vel Deo facere. Ex istis secundo sequitur quod fugitivi privilegiati in Westmonasterio non ex hinc libertantur, ut non satisfaciant debitori vel quod ibidem maneant pro suo perpetuo sine pena correccionis salubris, sed aliquam defensionem singularem habent ibidem que sonat eis in commodum et non in dampnum vel iniuriam alicui. Prima pars patet, tum quia hoc non sequitur ex tenore verborum privilegii, tum eciam quia hoc non foret libertas vel privilegium sed pravissima corruptela. Nam mandatum apostoli et sic Dei est Rom. XIII° 8: Nemini quidquam debeatis nisi ut invicem diligatis. Quomodo ergo licet creature licenciare aliquem, ut remaneat in debito fratris, non satisfaciens, eciam quoad Deum? Tales itaque hereses si pullulaverint eciam per dominos regni nostri, tenentur prelati destruere. Unde XXVª, q. I, Omne quod, sic scribitur: Iniustum iudicium et diffinicio iniusta regio metu vel iussu a iudicibus ordinata non valeat, nequaquam enim quod contra evangelicam vel propheticam vel apostolicam doctrinam constitucionemve eorum sive sanctorum patrum actum fuerit, stabit. Unde istam doctrinam dicitur Romanos [p. 232] pontifices debere usque ad animam et sanguinem confirmare (ut capitulo proximo precedente). Quomodo ergo stant simul: nulli liceat quidquam debere alteri extra caritativam dileccionem, et tamen fugitivus licenciatur in dicto loco perpetuo debere tam debitum corporale quam spirituale sine hoc quod rependat satisfaccionem. Revera in istam blasphemiam usurpatam Deus non potest, cum non licenciat hominem ad aliquid pro quo dampnat. Secunda autem pars conclusionis patet ex hoc quod oportet aliquod privilegium ex concessione regis dari talibus fugitivis ex conclusione proxima. Et ista sentencia notabiliter docetur XXVª, q. I. Ideo permittente domino, ubi dicitur quod quandocunque Romana ecclesia concedit privilegium, exprimit vel subintelligit, nisi aliter decreverit ordinandum. Unde, inquit, in nonnullis capitulis conciliorum, cum aliquid observandum decernitur, statim subinfertur, nisi auctoritas Romane ecclesie aliter fieri imperaverit vel salvo semper in omnibus iure Romane ecclesie vel salva in omnibus apostolica auctoritate. Cum ergo alia privilegia ab apostolico aliquibus conceduntur, et si contra generalem legem aliquid sonare videantur, non tamen contra ipsam aliquid concedere intelliguntur. Privilegia, inquit, dicuntur quasi privata legia; et concludit finaliter: Valet ergo Romana ecclesia extra generalia decreta quedam speciali beneficio indulgere, considerata tamen racionis equitate, ut mater iusticie in nullo ab ea dissentire inveniatur, ut videlicet privilegia que ob religionis vel necessitatis vel exhibiti obsequii graciam conceduntur, neminem relevando ita divitem faciant, ut multorum detrimenta non circumspiciendo in paupertatis miseriam nonnullos deiciant.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 227.20: The real use of the privilege.
- 228.2: The interpretation of it lies with the King,
- 228.12: who is to be guided by sound theology.
- 229.5: We must consider the purposes of the Charter,
- 229.10: which are: a) respect to the relics of St. Peter,
- 229.15: b) quiet for the monks,
- 229.17: c) honour to the Church in which the King Is Specially prayed for.
- 229.23: Monks of the royal foundation are bound to obey the King; so must be their guests or fugitives.
- 229.31: Crime cannot free from the duty of obedience.
- 230.7: Forgiveness is good so far as it tends to true mercy,
- 230.12: and a special privilege of forgiveness should be left to Westminster,
- 230.23: out of regard for the royal grant.
- 230.28: No privilege may be contrary to common law.
- 231.10: Hence fugitives are not made altogether free of debt or of punishment,
- 231.17: since this would be mischievous.
- 232.3: It is contrary to charily to encourage a man not to pay his debts.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 227: *CAP. XI.* [HEAD]
  - 228: *XXª* [R4]
  - 228: *XXVª* (italic) [R4]
  - 229: *Cum* (B 3 are the alinea letter and argument numeral) [R4]
  - 229: *iure* [R3]
  - 229: *superius* [NW]
  - 229: *Edgari* (letterspaced) [R4]
  - 229: *scilicet* (glued 'the' is the English side-note) [R4]
  - 229: *apostoli* [NW]
  - 229: *rege* (15 is the line number) [R4]
  - 229: *legii* [R4]
  - 229: *singulare* (30 is the line number) [R4]
  - 229: *Christi* [R3]
  - 230: *per* (C is the alinea letter) [R4]
  - 230: *Angliam* [R4]
  - 230: *attendere* (atten-/dere hyphenated; main token holds whole word) [R4]
  - 231: *XXVª* (25 is the line number) [R4]
  - 232: *∅* (print has sangui-/nem; main already holds sanguinem whole at pos 6) [INS?]
  - 232: *licenciatur* [NW]
  - 232: *XXVª* [R4]
  - 232: *legia* (italic; print legia;) [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 227:
1. A B in marg. : Duplex privilegium. 8. A in marg. : Nota.
18. B: vires. 20. A in marg. : (black ink and red ink): Cap. nm.
28. B concedere.
28. Decr. II pars, causa XXV, q. I, c. XVI et Decr. Greg. IX,
Iib. V, tit. XXXIX, cap. XXXI.

p. 228:
7. B: suus deest. 9. B: humiliter declinare. 17. A ln marg. :
Nota quomodo est dubium discernendum. 17. In cod. dist. XXI.
25. B in marg. : Ad quem quis debet recurrere pro dubiis discrete deci-
dendis. 27. B alia manu corr.: mittere.
17. Quae autor hic diffuse explicat, mutatis aliquot verbis
deprompta sunt e Decreti I parte, dist. XX, c. III, et Decr. II
parte, causa XXV, q. I, cap. VI.

p. 229:
16. B in marg.: Bulla Nicolai III. 18. A in marg.: Conclusio.
Nota quomodo sunt privilegia intelligenda. (Above i6od without mark of
reference.) 28. A: preminencia. 3i. B: per deest.
9. Arist. Physic. Ausc. II, 3.

p. 230:
7. A in marg. : Prima conclusio. 12. A A^: hoc cum pr ivilegia.
ig. A in marg. : Cor rclarium. 20. A: sonant. 25. A in
marg. : Correlarium. 26. B in marg. : Privilegium non est communi
ruri cot.trarium.

p. 231:
io. A in marg. : Secunda conclusio. 20. In codd.: Rom. XII.
28. B in marg. : Est hic manifeste elicibile quod non licet contra apo-
stolum dispensare;
2. Decr. sec. pars, causa XXV, q. II, cap. X. 25. Dec.
sec. pars, causa XXV, q. I, c. VIII.

p. 232:
4. A Aj : extra caritatem. 8. Deus non potest: verbum deesse
videtur. 19. B: vel salva — conceduntur deest. 3o. A: que vel.
33. In codd.: pauperis; correxi e decret. sup. mcm.
```

---

## Chunk 11-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-11-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-11-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "233.1–237.33"
divisions: "cap. 11 (heading 'CAP. XI.' at 227.19); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1138 words; 1046 unanimous or majority-real; 84 settled by vote (R2 50, R3a 28, R3b 1, R5a 4, R6a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n270–n274 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 11, part 2: [TITLE]

## ¶1 · 233.1–237.33

> [p. 233] Ex istis patet triplex correlarium: primum declaracio et confirmacio descripcionis supradicti privilegii; secundo patet, cum actus privilegiandi regum terre exemplari debet a privilegiacione sancte Romane ecclesie, quam oportet subintelligere condicionem sicut oportet et Deum a quo est omnis privilegiacio exemplata: necesse est reges terre subintelligere racionabilitatem privilegii, sic quod non sonet in alicuis iniuriam; quod si ignoranter fecerit, error perceptus debet statim ex mandato Christi et eius pura licencia revocari. Et patet tercio stultum esse ex nudis verbis privilegii aliqua vocata privilegia que sunt manifesti errores concludere, quia (ut patet V° Ethicorum cap. ultimo De Epykeya) necesse est in talibus subintelligere condicionem captam a fine; aliter enim preter triplex inconveniens (deductum in proximo capitulo) sequeretur manifesta blasphemia, ut puta, rex Anglie concedit cuilibet tali fugitivo omnimodam libertatem, sed libertas a peccato est maxima, sine qua non est aliqua vera libertas, ergo rex concedit cuilibet tali ipsum esse liberum a peccato. Quod cum sonat blasphemiam, manifestum est quod hec non fuit regis intencio sed quod haberent quodcunque terrenum privilegium tam in bonis nature quam in bonis fortune quod sue subiacet potestati. Ex istis tercio colligitur quod virtute dicti privilegii multi fugitivi ad dictum locum debent in casu acute puniri, bonis ahenis que occupant privari et aliis medicinis tam corporalibus quam spiritualibus ad salutem anime sue tendentibus expurgari. Patet ex hoc quod ibi virtute privilegii habebunt quod [p. 234] nocius vergit ad sui commodum, sed hoc foret in casu huiusmodi medicina; ergo conclusio. Unde movet ad hoc privilegiacio regis, finis, gracia cuius privilegium conceditur illi loco, et utilitas quam caritative rex debet intendere fugitivo. Si enim rex erranter intenderit finem illi oppositum, tunc si ab illo errore purgatus non fuerit, pena sua ex quacunque malicia que directe exinde sequitur, aggravatur, et nedum hoc sed peccatum regum dominorum et prelatorum superstitum, qui correpcionem illam quam debent ex accidia pretermittunt. Nam LXXXIIIª distinccione sic scribitur: Error cui non resistitur approbatur, et veritas cum minime defensatur opprimitur. Negligere quippe, cum possis perturbare perversos, non est aliud quam fovere. Nec caret scrupu societatis occulte qui manifesto facinori desinit obviare. Et utinam nostri domini, nostri prelati et nostri scolastici attenderent illud dictum; nam totus labor scolasticus debet tendere ad hunc finem propter zelum ad dominum veritatis in quem offenditur. Et ad idem sonat quies monachorum ibi degencium; cum enim omnis nociva perturbacio trahit originem a peccato, patet quod monachi non quietarentur sed turbarentur ex favore et assistencia peccatorum. Et si dicitur quod est eis lucrum, cum fugitivi condividunt temporalia que apportant, superadditur accusans gravacio quod tam sancti viri, tam alienati a mundo, sint socii furum, communicantes cum excommunicatis, impedientibus suam contemplacionem et quietem in domino, quia Isaie IX°, 5, scribitur: Omnis violenta predacio cum tumultu. Ymmo cum loci sanctitas [p. 235] precipue trahitur ab inhabitantibus illum locum, patet quod talis monachorum infeccio derogat sanctitati et reverencie loci quam rex privilegians intendebat. Nec valet dicere (ut audivi quosdam fingere) quod infra locum haberent iniuriati contra profugos respondentes ibidem iusticie complementum. Primo quia ritus regni laudabilis in habendo forum contenciosum in loco prophano non debet in domum oracionis vel locum sanctum propter tale maleficium transmutari. Secundo quia monachis pro quorum quiete rex tam tenere procuravit inferretur dampnum anime, quia inquietacio a contemplacione distrahens cuius oppositum privilegians intendebat. Tercio quia contra ius divinum et ius ecclesie est violare sponsam Christi vel locum eius. Unde VI° Decretalium, De immunitate ecclesie, cap. Decet, postquam ostenditur ex scriptura quod multipliciter decet sanctitas domum Dei, sic infertur: Nullus in locis eisdem in quibus cum pace ac quiete vota convenit celebrari, sedicionem excitet, conclamacionem moveat, impetumve committat; cessent in illis universitatum et societatum quelibet consilia, concertaciones et publica parliamenta; cessent vana et multo forcius feda et prophana colloquia, cessent confabulaciones quelibet, sed postremo quecunque alia que divinum possent turbare officium aut oculos divine maiestatis offendere sint ab ipsis prorsus extranea, ne ubi peccatorum est venia postulanda, ibi peccandi detur occasio aut deprehendantur peccata committi. cessent in ecclesiis earumque cimiteriis negociaciones et precipue nundinarum ac fori cuiuscunque [p. 236] tumultus. Omnis in eis secularium iudiciorum strepitus conquiescat. Nulla inibi causa per laycos criminalis maxime agitetur; sint loca eadem a laicorum congregacionibus aliena. Hec ibi. Quomodo queso foret ecclesia fomentum criminum? vel quoscunque in ipsam committentes defenderet? Unde super verbo Sedicionem dicit glossa quod committens furtum in ecclesia non habebit inmunitatem in ea et hoc tenet Hostiensis, et bene, cum frustra invocat loci suffragium qui fedat eundem. Cum ergo quicunque offendit in uno factus est omnium reus, manifestum est quod omnis peccans mortaliter intra ecclesiam furatur spirituale suffragium, quo Deus plus offenditur quam pro furto temporalium, ymmo cum omnis occupans temporalia in mortali, deficit a iure utendi quocunque, pro tunc manifestum est quod furatur bona ecclesie in qua pausat. Si ergo ille sit prevaricator precepti decimi: quicunque iniuste cupierit aliena, multo magis ille est prevaricator decalogi qui fraudulenter et iniuste detinet aliena. Si ergo non licet alicui dispensare cum aliquo preceptorum domini, manifestum videtur quod non subiacet potestati humane privilegiare locum vel hominem, ut liceat sibi vivere contra mandatum dominicum. Et hic mirantur nonnulli, cum sit ad privilegium locis sanctis quod eximantur a quocunque tumultu secularis negocii, quomodo superiores prepositi ecclesie, scilicet episcopi, priores et abbates nedum permittunt sed vendicant ut privilegium et pertinaciter defendunt, quod in ecclesiis suis ac cimiteriis suis sint nundine et secularia negocia que nunquam sine dolo et crimine multiplici exercentur. Cum autem non est possibile ut duo contraria sint simul privilegium eidem ecclesie, manifestum est quod vel oportet negare privilegium iuris divini ac iuris canonici de exempcione [p. 237] ecclesie a tumultu negocii secularis vel concedere hoc esse privilegium impediens bonos mores. Et credo quod nostri ecclesiastici isti sentencie annuerent, si non essent lucro temporalium excecati, cuius probacio foret, si princeps tolleret questum, renunciaretur privilegium; sed sceleratissimum videtur atque sacrilegum pro pecuniis vendere divinum privilegium. Et per idem tollitur quod leges Anglie non mutarentur pretextu erroris in hoc privilegio, introducendo bancum regis, eius iudicem vel placitum seculare in domum domini; tunc enim foret novissimus error peior priore, cum error ignorancie factus in Deum augeretur supplecius per supinum contemptum; nam unum peccatum illaqueando profundius trahit ad aliud. Quoad terciam personam, scilicet fugientes, patet quod privilegians intendit commodum fugitivi, quia aliter non esset sibi elemosina vel opus misericordie sed omnino contrarium, si intenderet dampnificare proximum. Quod autem esset in casu fugitivo privilegium sic puniri, patet supponendo aliquos occasione male accepta ex securitate talis refugii iniuriari proximis et sic dampnificare animas proprias per peccatum. Suppono secundo quod maius opus misericordie foret impedire occidentem sic animam propriam quam occidere volentem nudum corpus. Et ex istis tercio sic arguitur: Omne maius bonum opus misericordie est pocius inpendendum, sed maius bonum opus misericordie est subtrahere bonum a tali in casu signato et castigare freneticos ad salutem eorum perpetuam, quam egentem solum in bonis corporalibus taliter relevare; ergo illam elemosinam potens pocius debet inpendere. Supposito ergo casu de fugitivis, sic alibi nocentibus, patet conclusio.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 233.1: All privileges must be reasonable and not injurious,
- 233.11: and this condition must always be understood, however the words of the privilege run,
- 233.26: By virtue of this very privilege many fugitives should be punished;
- 234.1: since it would be to their advantage.
- 234.7: If the King had a wrong purpose his mistake should be corrected.
- 234.14: Not to punish the wicked is to support them.
- 234.24: The monks cannot have quiet, if they are disturbed by sin.
- 235.4: Redress cannot be had within the Sanctuary; a) because it is not a proper court of justice;
- 235.10: b) to hold trials there would disturb the monks;
- 235.13: c) to use a church as a court of law is to violate it.
- 236.10: Whoever sins mortally in a Church steals its protection.
- 236.26: Church dignitaries should not allow fairs etc. to be held in Churchyards;
- 237.8: nor the King's court to sit in the house of the Lord.
- 237.15: As to the fugitives it is not a privilege to them to be encouraged in their sin.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 234: *et* (161 is the folio mark) [R4]
  - 234: *LXXXIIIª* [R4]
  - 234: *violenta* (italic; c is the alinea letter) [NW]
  - 235: *∅* (G is the alinea letter; Nec is pos 21) [R4]
  - 235: *iniuriati* [NW]
  - 235: *forum* (f) [R3]
  - 237: *∅* (print has nothing between ecclesie and a; the inserted run is the end of p.236) [INS?]
  - 235: *precipue* (161c folio mark glued) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 233:
I. A in marg.: Triplex Corrclariuni. 2. A A, : supradictc.
8. B: nobilitatem privilegii. t(i. B: quadruplex. 17. A
in marg. : Nota. 26. A in marg. : Tcrcia conclusio. 27. A in
i3. Vict. Ethicorum Nicomacheorum. V, c. 14.

p. 234:
2. A B in marg. : Triplex mocio. n. A in marg. : LXXXIII, q.
Nota, Nota. B in marg. man. alt. : Error cui non resistitur approbatui.
i3. B: opprimit. 25. A A, : dicitur quod cum eis lucrum fugitivi.
3o. In codd. : violencia; correxi ex Is. IX, 5.
ii. Dec. I pars, dist. LXXXIII, c. III.

p. 235:
4. A B in marg. : Responsio ficta. 11. In codd.: infereretur.
i5. A in marg. : Nota pro immunitate ecclesiarum. 20.21. Decr. habet:
locis illis universitatum et socictatum quarumlibet concilia, conciones et . . .
28. A A, : peccata quieta. 29. A in marg. : Nota contra nundinas
et secularia negacia in locis sacris. B in marg. : Que prohibentur lieri in
ecclesiis et earum cimiteriis.
i5. Sexti decret. Hb. III, tit. XXIII, cap. II.

p. 236:
11. B in niarg. man. alt. : Furtum in ecclesia. 17. B : sit privile-
giator. 3i. A in marg. : Conclusio.

p. 237:
i5. B: scilicet deest. 16. B: quod rex privilegians. 17. A
in marg: Conclusio. 21. A: privilegii refugii. 24. A in marg. :
Nota contra pretensam immunitatem ecclesiarum. 26. A in marg. :
Tercio racio. 27.28. B: Maius opus. 32. A A, : supposito casu.
```

---

## Chunk 11-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-11-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-11-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "238.1–242.18"
divisions: "cap. 11 (heading 'CAP. XI.' at 227.19); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1024 words; 921 unanimous or majority-real; 77 settled by vote (R2 47, R3a 18, R5a 12); 26 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n275–n279 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 11, part 3: [TITLE]

## ¶1 · 238.1–238.27

> [p. 238] Confirmatur primo ex hoc quod Christus medicus sapientissimus et clementissimus ita facit cum suis discipulis quos plus amat (ut declarat beatus Gregorius XXI° Moralium, et recitatum est proximo capitulo). Unde Apoc. III°, 19, dicit is medicus: Ego quos amo arguo et castigo, et Hebr. XII°, 16, 19, dicitur: Flagellat autem Deus omnem filium quem recipit. Secundo confirmatur ex testimonio Augustini posito in decretis XXIIIª q. IV. Ipsa pietas, ubi sic scribitur: Molestus est medicus furenti frenetico et pater indisciplinato filio: ille ligando iste cedendo, sed ambo diligendo. Si autem illos negligant et perire permittant, ista falsa mansuetudo foret crudelitas, Vª, q. IVª. Non vos, et Non omnis. Et ponit post exemplum quomodo existentibus pluribus amicis in domo certissime ruitura, si nollent credere narracioni periculi, flagellaremus vel invite extraheremus aliquem, licet credamus quod aliquis se stulte precipitet. Multo magis in maiori periculo spirituali. Unde XXIII°, q. IVª. Quid faciet, dicitur quod ad hoc datur ecclesie medicina, ut inter freneticos atque litargicos eciam contempnentes non debet desistere sic quod perseveret diligencia caritatis, ligando freneticum et litargicum stimulando. Quotlibet tales sunt leges que idem sentenciant. Si ergo tantum sit peccatum in omittentibus habentibus potestatem, manifestius et inexcusabilius est peccatum in speculatore qui ommittendo proderit veritatem.

[ENGLISH]

## ¶2 · 238.28–239.31

> [p. 238] Cum ergo (ut tactum est superius) non stat duo contraria esse simul privilegia eidem, et secundum idem patet cum casu limitato, foret privilegium fugitivo [p. 239] ligari et pungi, non foret tunc idem privilegium in facultatibus et pena relaxari, quia revera omnis taliter cupidus fastus et questus est furens freneticus et soporatus litargicus ex fumo temporalium inficiencium cerebrum racionis. Et patet per modum epilogi quomodo oportet privilegium sic interpretari quod fugitivi ad locum sic privilegiatum pro quocunque commisso habeant libertatem vel immunitatem omnimodam secundum regulas caritatis et misericordie a rege et regno cum paribus eis dandam, sic quod omne dandum sonet tam eis quam dantibus bonum utile. De diversitate vero inter crimen, facinus atque flagicium dictum est XXV° cap., libri VIⁱ quomodo facinus sonat in proximi iniuriam; de quiditate autem privilegii dictum est superius, VIII° cap. huius libri; et cum oportet ut intelligatur libertas a peccato (ut loquitur Apostolus Rom. VI°, 22); patet quod immunitas pertinenter est indignitas criminis ad tormentum (ut loquitur scriptura Jeremie XXV° et Ecclesiasticus VII° cap.). Communiter autem intelligitur de mundicia a facinore quod in Anglia dicitur felonia, et est quedam species libertatis quam quidam vocant franchisiam et sumitur nunc extensius et nunc striccius. Unde immunis dicitur ab in et munium tributum, quasi liber a reddicione tributi, ut est expers vel alienus a reatu et vere loquendo solum insons, dum non est dignus sic puniri. Dicitur inmunis sic quod immunitas opponatur reatui, ad quem sensum ex nullo humano privilegio sequitur in criminoso immunitas aput Deum, sed ex privilegiacione sequitur irreatus pene quoad principem libertantem.

[ENGLISH]

## ¶3 · 239.32–240.22

> [p. 239] Contra dicta obicitur primo per hoc quod, si quilibet criminosus sit indignus habere suffragium ecclesie, tunc [p. 240] lex illud exprimeret, sed facit oppositum cum servum eciam existentem in gracia docet extrahere et alios criminosos docet libertate gaudere. Hic dicitur quod plus peccans est de racione plus elongatus a suffragio ecclesie, licet ecclesia ex ignorancia gravedinis peccati vel ex percepcione planiori iniurie vel alia causa culpabili hoc dispariter prosequatur. Nam si secundum iura humana et ecclesiastica licitum racionabile atque legitimum est extrahere servum atque libertum de ecclesia pro debito operis impendendo domino temporali (ut patet capitulo De hiis qui ad ecclesiam fugiunt, le. fi.), si omnis indebitatus proximo in pecunia vel quocunque debet servicium satisfaccionis sub pena dampnacionis domino dominorum, ergo multo magis licet eum extrahere de ecclesia, si exhinc pauset inobediens ad reddendum servicium regi regum. Minor patet ex hoc quod omnis homo est magis servus Deo, plus debitor et prius quam aliquis servus est debitor domino temporali. Unde Apostolus Ephes. VI°, 5°, docet servos obedire dominis carnalibus cum timore et tremore, sicut Christo, servientes sicut domino non hominibus.

[ENGLISH]

## ¶4 · 240.23–242.3

> [p. 240] Confirmatur primo per hoc quod, sicut homo tenetur plus Deum diligere quam se ipsum, sic tenetur plus odire Dei iniuriam, unde XXIIIª, q. IV sic scribitur: Si ea de quibus vehementer Deus offenditur, insequi vel ulcisci deferimus, ad irascendum utique divinitatis pacienciam provocamus. Secundo confirmatur ex hoc quod secundum leges humanas lesis et non [p. 241] ledentibus debent privilegia ecclesie suffragari (ut patet collacione tercia) sed omnis profugus, iniuste detinens alienum debitum pretextu profugii ad quamcunque ecclesiam iniuriatur Deo et omnibus sanctis leditque se ipsum et quemlibet proximum mortalis peccati comparticipem. Ergo non est iustum ut sic ledens gaudeat taliter immunitate ecclesie. Et ad idem vadunt quotlibet iuris principia, ut III° Decretalium, De rerum permutacione, cap°. Cum universorum: Deceptis et non decipientibus iura subveniunt; aliter enim ordinarentur leges ad fovendum iniurias. Sed Isaie X°, 1, dicitur: Ve qui condunt leges iniquas; non enim est lex humana vel divina nisi ad continuandum iusticias et expurgandum iniurias. Tercio confirmatur ex hoc quod homo est obligacior ad vindicandum iniuriam Dei quam propriam, cum suam debet remittere, nisi de quanto sapit divinam iniuriam, sicut patet de Christo, de Moyse et ceteris Christi membris, que omnia debent exponere se pro capite; sed omne ad cuius complecionem est obligacior debet magis attendere: ergo debet magis attendere vindicacionem divine iniurie; unde omnes facientes oppositum sunt culpabiliter se ipsos amantes (ut loquitur Apostolus, II°, Thymothei Et istam sentenciam docet Augustinus, libro primo ad Cresconium grammaticum ut recitatur in decretis, XXXIIIª, q. IVᵗᵃ): Quisquis christianus iniquum non persequitur, Christi est inimicus. Verum dicis, si non hoc in illo persequitur quod Christo est inimicum. Neque enim dominus in servo, pater in filio, maritus [p. 242] in coniuge, cum sint utrique christiani, non debent persequi nisi vicia christiane contraria veritati; que si non persequuntur, rei negligencie merito tenebuntur.

[ENGLISH]

## ¶5 · 242.5–242.18

> [p. 242] Et ista sentencia rectificaret multum ecclesiam, quia desidia et deformitas correpcionis perturbant ecclesiam, cum multi non correptores, sed corruptores zelo vindicte amant peccatum et odiunt personam, querunt pecuniam, non correpti iusticiam, et ideo correpciones propter ordinem preposterum non habent efficaciam. Conceditur ergo assumptum in obiecto, cum oportet Deum dignificare fugitivum per graciam, et post redditur dignior ad habendum matris sue suffragium; nec possunt aliqua iura exprimere huius oppositum. Racionabile autem est servum fugientem a servicio debito domino suo extrahere, cum ut sic delinquit in Deum; quod autem homines illud maioribus peccatis preponderant, accusant proprietarie se amantes.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 238.1: Christ chastises those whom he loves.
- 239.6: To sum up: The fugitives should have all liberty that is good tor themselves and for others.
- 240.1: Objections: 1. It is said that the law would express these limitations, if they were intended.
- 240.12: Answer: It does in a way express them.
- 241.1: The Church should help the injured, not those who do wrong.
- 241.15: A man is more bound to revenge an injury to God than to himself.
- 241.25: Augustine teaches the duty of punishing the wicked.
- 242.5: The performance of this duty would do much to set the Church right.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 238: *Christus* [R3]
  - 238: *suis* (1 is the argument numeral) [NW]
  - 238: *III°* [R4]
  - 238: *amo* (the 5 after it is the line number) [NW]
  - 238: *Vª* [R4]
  - 238: *IVª* [R4]
  - 238: *IVª* [R4]
  - 239: *ligari* (H 162ª in margin is alinea letter + folio mark) [R3]
  - 239: *VIⁱ* (small superscript i after VI, as Edwardi IIIⁱ) [R4]
  - 240: *gaudere* [R3]
  - 240: *XXIIIª* [R3]
  - 241: *ledentibus* (K 162ᶜ in margin is alinea + folio mark) [R3]
  - 241: *suffragari* [R4]
  - 241: *ut* (opening paren is punctuation) [R3]
  - 241: *III°* [R4]
  - 241: *1* (old-style arabic 1 (verse number), x-height) [R3]
  - 241: *Augustinus* [R4]
  - 241: *ut* (opening paren is punctuation) [R3]
  - 241: *IVᵗᵃ* (superscript ta) [R3]
  - 242: *odiunt* [NW]
  - 242: *servicio* (5 after it is the line number) [NW]
  - 239: *suffragium* [THIN]
  - 240: *exprimeret* [THIN]
  - 240: *oppositum* [THIN]
  - 241: *privilegia* [THIN]
  - 241: *XXXIIIª,* [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 238:
1. A in marg. : Confirmacio triplex. 8. Ainmarg.: Augustinus.
12. A A,: nec ligant. i3. In codd.: V q. vel IV. 14. ponit sc.
August. 1. c. 23. B in marg. man. alt. : Correccio est medicina.
4. Cap. IV. 9. Dec. sec. pars, causa XXIII, q. IV,
cap. XXIV. i3. ib. causa V, q. V, c. I et c. II. 19. ib.
causa XXIII, q. IV, cap. XXV.

p. 239:
4. B: et se portatus. C. A in marg. : Epilogus. Nec omnia valent
pro correccione peccancium. li. B: omnino dandum. 18. B in
marg. : Immunitas quid sit, nota. 22. 2'). B: quedam franchisia.
24. B: et buium. 32. Contra. Prima obieccio.

p. 240:
3. A in marg.: Responsio. 6. B: in iure; A culpali. II. A B:
patet Coj ibid. le. fi. id est Iege fine (lege in tine) ib. sed omnis.
i3. B: quocunque alio. 25. A A, : Unde deest.
ii. Decret Gregorii IX, lib. III., tit. XLIX, cap. VI.: Si vero
servus fuerit qui confugerit ad ecclesiam, postquam de impunitate
sua dominus eius clericis iuramentum praestiterit, ad servicium
domini sui redire compellitur etiam invitus. s5. Dec. II
pars, causa XXIII, cap. L.

p. 241:
4. B: ledit se. 12. B: qui comcdunt. 17. B: debent re-
mittcre. 24. A in marg. : Nota. 2O. A B: Cresconicum; A,
Crescencium. A in marg.: Augustinus. 27. Ainmarg. : Correpcio.
In decrct. legcs : Quisquis shristianus iniquum persequitur.
8. Dec. Greg. IX, lib. III, tit. XIX, cap. VIII. 26. Decr.
II pars, causa XXIII, q. IV, Cap. LII.

p. 242:
1. In codd.: utique. 7. 8. B: ze vindicte. i3. B: digni; A cor-
rexit: dignior. iS. B: accusat. 19. A in marg. : Contra. Se-
cunda obieccio. 24. A in marg. : Responsio. 25. A in marg. :
Nota, qui fugitivi debent gaudere de immunitate ecclesiarum, quia peni-
tentes etc (Above K)2J without mark of reference). 3i. 32. B: sed
quantum.
```
