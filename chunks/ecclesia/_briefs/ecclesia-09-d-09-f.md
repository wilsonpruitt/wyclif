# Translation brief: ecclesia 09-d–09-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-09-d.md chunks/ecclesia/wyc-ecclesia-09-e.md chunks/ecclesia/wyc-ecclesia-09-f.md` once and fix what it reports.
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

## Glossary (the 149 rows these chunks use; the full file is GLOSSARY.md)

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
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| orator | CONTEXTUAL: bedesman / advocate | Plural *oratores* "bedesmen" (Dialogus ruling); of one who pleads the church's cause (*orator ecclesie*, *Eccl.* 165.25, 166.4) "advocate", with a **C** note. Ruled 2026-10-02. |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
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
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| oratores | bedesmen | Those bound or paid to pray for a benefactor; Pollard's side-note word. Not "those who pray". Ruled 2026-09-28 (5 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| satrapa | satrap | Derogatory: church-court officials wielding delegated power (T. p. 378 n. 58). Keep the word; note it at first occurrence per work. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
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
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| zizania | cockle | Douay–Rheims (Matt. 13:25). Ruled 2026-09-28. |
| cautela | wile | Not "caution"; *cautela diaboli*, the devil's wile. Ruled 2026-09-28 (8 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| vecors; vecorditer; vecordia | faint-hearted; faint-heartedly; faint-heartedness | The medieval sense, not classical "senseless". Ruled 2026-09-28 (5 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| perplexus | perplexed | The moral-theology sense: bound to sin whichever way one turns. Ruled 2026-09-28. |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 09-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-09-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-09-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "194.26–198.24"
divisions: "cap. 9 (heading 'CAP. IX.' at 182.6); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "930 words; 809 unanimous or majority-real; 96 settled by vote (DEL 1, R2 64, R3a 28, R5a 2, R6a 1); 25 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n231–n235 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 9, part 4: [TITLE]

## ¶1 · 194.26–195.22

> [p. 194] Sed da quod ista fuissent compossibilia cum dotacione ecclesie et da minorem principalis argumenti, adhuc non sequitur conclusio, cum stat cum toto isto quod ecclesia perdat perfeccionem aliunde maiorem quam fuit perfeccio ex acquisicione temporalium perquisita; quod ego credo nedum fuisse verum sed necessarium, supposita declinacione a religione quam Christus instituit. Et videtur mihi stultum fore omnino excusare beatum Silvestrum et Cesarem a peccato [p. 195] sic quod unus fuisset omnino inmunis ab affeccione inordinata ad temporalia, et ut sic aliquantulum venialiter nocens sibi, et occasione male accepta plene superbiendi, plus nocens suo generi succedenti. Potuit enim renuisse, sicut beatus Evangelista et ceteri apostoli qui possent in tanta quiete assumpsisse sibi et successoribus suis tantam copiam temporalium quam prudencius reliquerunt. Nec repugnat isti quod sancti canonizantur in ecclesia et beatificantur in celo, cum possunt hic penitere et in purgatorio emendari. Quis, inquam, sanctus a sancto sanctorum exclusive usque ad novissimum sanctum non peccavit eciam mortaliter? Ideo (ut sepe dixi) cecitas magna foret nobis superstitibus allegare tales argucias: Iste sanctus sic fecit, ergo nobis licet sic faciendo quodcunque opus consimile approbando defendere et augere. Hoc enim privilegium specialiter reservatum est Christo qui non potuit peccare, ut nitamur sequi ipsum in omnibus quantum sufficimus et nullum alium nisi de quanto ipsum sequitur; sed propter formidinem mentiendi neutram partem assero, vel quod sancti meruerunt in dicta dotacione vel quod demeruerunt.

[ENGLISH]

## ¶2 · 195.23–198.24

> [p. 195] Sed scio quod prior status fuit perfeccior, et scio quod donacio si fuit privilegium fuit facta a Christo, et scio quod nos debemus uti hiis temporalibus sicut illi usi sunt, quia aliter excidimus a privilegio per abusum. Si ergo volumus sequi sanctos confessores, arguamus per locum a sufficienti similitudine sequendo eos in affeccione et usu temporalium concessorum, et conformiter videtur probabile in republica de Cesare et ceteris mundi principibus quod laborarunt peccato superbie, volentes in republica solempnitate sacerdotes [p. 196] suos excellere et nomen suum in mundo extollere. Et sic potuerunt melius fecisse defendendo religionem quam Christus instituit. Christus enim ne sponsa sua adulteretur cum mundo, prohibuit sibi communicacionem cum mundo et iniunxit contemptum sue glorie, et hec fides scripture docuit sanctos pro amore sponsi zelotis vincere istum mundum; Iª Joh. II°, 1 precipit Johannes dileccione speciali privilegiatus a Christo: Nolite diligere mundum neque que in mundo sunt; et magister noster Christus dicit Iª Joh. III°, 1: Nolite mirari si odit vos mundus et Joh. XVI°, 33: Confidite, quia ego vici mundum, et: Sufficit discipulo ut sit sicut magister eius. Hec cum quotlibet eis similibus fecerunt sanctos mundum cum condicionibus suis contempnere et sponso qui hec fecit et docuit moribus adherere, cum ex testimonio suo Matthei VI°, 24: Non possumus Deo servire et mammone. Si ergo servamus usum et ritum ecclesie per accidens introductum in dicendo divinum servicium et conversando secundum tradiciones hominum, ne parva declinacio tracta in consequenciam inducat maiorem defectum, quanto magis debemus striccius servare usum et mandatum dominicum de incommunicanter odiendo mundum? Revera declinacio ad oppositum posset paulative inducere clerum nostrum, ut vivat secularius quam laici colentes seculum, et sic olim vinea domini transiret in ortum olerum; et probando si blaspheme excusaciones nostre sintvere de non diligendo seculum, sed ad roborandum amorem Dei, capiendo licitum eius usum, utamur regula tacta in fine proximi capituli, videndo si dicta nostra operibus compensamus. [p. 197] 56° Constat quidem ex testimonio scripture Ysaie V°, 1, 2, quomodo ecclesia Dei est vinea, dum stillat a botris plenis vino sapiencie doctrinam fidei scripture ad nutriendam vitam fidelium, ut patet ex processu Cantici canticorum, quod si ab isto officio declinat ad seculum, tunc soror nostra parvula, non habens ubera, versa est in ortum olerum. Olera enim (ut tangit Augustinus super Psalmum XXXVIᵘᵐ) virescunt in hyeme, in estate autem propter defectum radicum marcescunt; et cum secundum naturales caules sunt herbe nimis melancolice, generantes humorem terrestrem, propter quod a bestiis melancolicis ut bobus, leporibus et similibus adeo sunt amate, signanter signant mundo deditos qui virescunt in yeme peregrinacionis, refrigescente caritate multorum, sed in estate diei novissime propter defectum radicacionis in Christo ex ardore solis iusticie evanescunt; sed tunc fideles in caritate fundati quorum vita abscondita est cum Christo, cum pastor eorum apparuerit, evirescunt. Canticorum II°, i, scribitur: Jam enimyemps transiit, ymber abiit et recessit, flores apparuerunt in terra nostra, tempus putacionis advenit, vox turturis audita est in terra nostra, ficus protulit grossos suos, vinee florentes dederunt odorem suum. Quamvis autem illud epitalamium verificatum est ad literam pro tempore incarnacionis sponsi ecclesie, tamen pertinenter et vere dici potest pro estate diei iudicii. Primo enim tempore processit tempus vernum ecclesie, quando apparuit gracia et caritas solis iusticie, fugato frigore brumali ab ecclesia, instructa a sponso ponere animam [p. 198] pro amicis; tunc enim yemps transiit et ymber tribulacionis abiit, mollificans fideles, ut patet de Petro et ceteris fugientibus a sponso, qui postea usque ad mortem permanserant, quia Canticorum VIII° scribitur: Aque multe non potuerunt extinguere caritatem. Sermones Christi erant flores, fructus virtutum prenostici, et quando misit discipulos ad metendum fructus et evellendum actus superfluos (ut notat Christus Johannis IV°), tunc advenit tempus putacionis. Nonne fuit Baptista turtur qui Johannis 111°, 29, dicitur gaudere propter vocem sponsi; ipse enim fuit vox clamantis in deserto, simul cantans penitenciam et gaudium sicut turtur; tunc enim cetus apostolorum protulit rudimenta fidei sicut ficus, et discipuli christiani? florentes virtutibus ut palmites vitis vere dederunt adoramenta sancte matri ecclesie, IIª Corinthiorum II° i 5, scribitur: Christi bonus odor sumus Deo. Sed sole occidente ab affeccionibus generata melancolia propter esum olerum yemps rediit, faciens refrigescere caritatem multorum; et iterum oportet ut fiat nova appropinquacio ad perpendiculare, quodque fiat directe post diem iudicii solsticium sempiternum (ut patet Apocalypsis ultimo), tunc enim invariabiliter coincident radius incidens et reflexus.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 194.26: Even if we grant it, the gain is less than the loss.
- 195.1: The example of Silvester and other Saints is insufficient.
- 195.16: Our only safe model in all things is Christ.
- 195.27: If we follow saints in possessing properly, we must follow them in our use of it.
- 196.14: They despised the world.
- 196.28: We should show by our works that we do so.
- 197.2: How the Church is God's vineyard.
- 197.27: The spring time of the early Church
- 198.17: has passed into winter,

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 195: *sic* (155ᵈ is the folio mark) [R3]
  - 195: *assumpsisse* [R4]
  - 195: *Christo* (side-note things follows) [R4]
  - 195: *ergo* [R3]
  - 195: *Cesare* (capital C) [R4]
  - 196: *sue* (156ª is the folio mark) [R3]
  - 196: *Iª* [R3]
  - 196: *II°* [R3]
  - 196: *Iª* [R3]
  - 196: *III°* [R4]
  - 196: *24* (print: Matthei VI°, 24) [DEL]
  - 196: *declinacio* (20 is the line number) [R4]
  - 197: *1* (old-style arabic 1, short like the following 2 (Ysaie V°, 1, 2)) [R3]
  - 197: *vinea* (italic v) [R3]
  - 197: *II°* (Canticorum II°, 11) [R3]
  - 197: *et* (margin 1 is the argument numeral) [R3]
  - 197: *pro* [R3]
  - 198: *tribulacionis* (tri-/bulacionis hyphenated; main token holds whole word; 156ᵇ O are folio mark and margin letter) [R4]
  - 198: *∅* (bulacionis is the tail of tribulacionis held whole at pos 8; no separate word) [NW]
  - 198: *Christi* [R3]
  - 198: *clamantis* (6 is the argument numeral) [R4]
  - 198: *IIª* [R4]
  - 198: *II°* ('into' is the English side-note) [R4]
  - 195: *fuisset* [THIN]
  - 195: *sacerdotes* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 194:
12. A in marg. : Rcsponsio. 14; A in marg. : Nota quattior.
iS. A,: calcata. 24. cprrel'" in codd. 33. A in marg. :
Conclusio.

p. 195:
9. B: beatificentur. i3. A in marg.: Arsucia. 31. A in
marg.: Hotantcs ct dotacioncs rccipicntcs si et quomodo peccavcrunf.
23. B: quod pcior status; A in marg. : Sciencia trium 25. 13: uli
dccst. 3o. AA,: dc Cesare deest; B: probabile de Cesare ctcclcris
33. in codd.: solempnic".

p. 196:
7. A B: .loh. III. A, corr. I Joll. III. II. In codd. Joh. XVII.
i3. In codd. ActB: hec requiritur cum; A,: requiritur; hoc verhnm sine
dubio superfluum et fortasse error in archetypo. 14. B: sanctos
deest. 21. B: tracta deest. 24. A in marg. : Conclusio.

p. 197:
1. A in marg.: Quomodo ecclesia dicitur vinca ct quomodo convertltur
111 ortum olerura. A: Is. IV. 7. A in marg. : Augustiiuis. 7. A
in marg.: Olus; U in marg man. alt.: Olerum proprietatcs. A, in marg.:
Olus est hcrba melancolica quc signat mundo deditos, ct ideo Theotunici
pre aliis geutibus comcdunt olus, quia plus sunt mundo et avaricie dediti.
11. A: malencolice. 19. A A,: apparuit.
5. Cant. Cantic. VIII, 8. 8. Sermo I. Opp. IV, 1, p. 2q.

p. 198:
17. A A,: Dco decst 18. A: malencolica. 21. In codd.
quosque. 27. A: Reg. 21 cap. B: 12 cap.
```

---

## Chunk 09-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-09-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-09-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "198.25–202.29"
divisions: "cap. 9 (heading 'CAP. IX.' at 182.6); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "956 words; 814 unanimous or majority-real; 113 settled by vote (DEL 1, R2 84, R3a 20, R5a 4, R6a 4); 29 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n235–n239 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 9, part 5: [TITLE]

## ¶1 · 198.25–199.10

> [p. 198] Sicut ergo Naboth noluit vel vendere regi vineam hereditariam, ut transferatur in ortum olerum (ut patet III, Regum XXI°, cap. I°), sic clerus pure accipiens Christum, vitem veram in porcionem hereditariam, non venderet illud privilegium paternum, sic quod ortus deliciarum in ortum olerum transferatur. Sed heu Jesabel, hoc est, effeminati et lubrici, voluptati dediti, dominantes satrapis primevum privilegium subverterunt; ideo caveant de malediccione et pena minata Achab et Jesabel. Istam moralitatem tangit venerabilis [p. 199] Beda super epistolam Jacobi. Insuper, si vitis noluit deserere vinum suum quo dii letificantur et homines, ut imperet ceteris lignis silve (ut patet Iudicum IX° et expositum est IV° cap. libri VIⁱ), quanto magis clerus non desereret primevum privilegium quod Christus instituit propter libidinem civiliter dominandi; ita solutio sathane regis superbie post mille annos (de quibus Apocalypsis XX°) retardat quod ecclesia non sit ad privilegium primevum restituta. Et ista causa rectificavit gloriosum martirium sancti Thome, cum de eo canit ecclesia:

[ENGLISH]

## ¶2 · 199.11–199.11

> [p. 199] Nec in agnos sustinet

[ENGLISH]

## ¶3 · 199.12–199.12

> [p. 199] Lupos desevire

[ENGLISH]

## ¶4 · 199.13–199.13

> [p. 199] Nec in ortum olerum

[ENGLISH]

## ¶5 · 199.14–199.27

> [p. 199] Vineam transire. Nec credo quod est causa verior vel alia qua fuit martir nisi resistendo lupis sevientibus in agnos gregis dominici et impediendo ne vinea inebrians transferatur in ortum olerum; herba quidem melancolica preservat ab ebrietate ex amissione temporalium gignens vecordiam. Sexto arguitur contra dicta per hoc quod iuxta predicta nichil sonat in privilegium hominis, nisi de quanto sapit graciam vel virtutem; sed hoc nullus preter Christum potest concedere, ergo nec privilegium, et sic nullus prescitus haberet privilegium, ymmo sciencia cum inflat et omnia bona citra virtutes non forent privilegia abutenti, que videntur legibus et modo loquendi vulgari contraria.

[ENGLISH]

## ¶6 · 199.28–202.29

> [p. 199] Hic dicitur quod prima consequencia non procedit, cum prescitus habet privilegium, dum est in gracia. [p. 200] Ideo signanter additur in descripcione privilegii quod est bonum concessum ecclesie vel persone. Datur enim quandoque temporale privilegium persone prescite que non est membrum ecclesie, verumptamen predestinatus habet excellenciori modo privilegium, quia ad maiorem utilitatem, scilicet ad beatitudinem, percipit donum Dei (ut patet in fine capituli VIⁱ). Prodest autem privilegium prescito quoad commodum temporale et quoad mitigacionem pene perpetue, sed manifestum videtur ex fide quod nulli prescito est privilegium bonum quod habet, dum est iniustus, quia ut sic abutitur dato ad sui incommodum; abutitur, inquam, quia debet uti dato in caritate honorando Deum et merendo sibi ac sancte matri ecclesie, et facit omnino oppositum deteriorando se ipsum. Ideo patet ex diffinicione privilegii quod peccatum facit prius privilegium desinere esse privilegium, quod quidam vocant mortificacionem privilegii. Et sic verum dicit beatus Gregorius (ut recitatur XIª, q. III): Privilegium omnino meretur amittere qui sibi permissa abutitur potestate. Et patet (ut ostendit glosa) quod non exinde debet sancta ecclesia privari privilegio, sed in privilegio innovari. Nam privilegium foret clericum in casu privari bonis fortune tam sibi quam ecclesie; privilegium eciam foret in casu ecclesie quod heretici sibi molesti subtrahantur morte civili ecclesiastica, naturali vel violenta. Et hec racio quare oportet consulere regulas scripture sacre in dando privilegia positiva vel privativa ecclesie. Nunquam enim debet quis punire personam in ecclesia, nisi sub intento privilegiandi ecclesiam; quod quia Apostolus fecit inconsulta scriptura (ut patet Act. IX°), ideo blasphemavit; et sepe contingit hodie quod seculares putantes se privilegiare [p. 201] ecclesiam perturbant et retardant eam, fortificando inimicos ecclesie et specialiter in concedendo elemosinas perpetuas, cum necesse est discolos subintrare in tales elemosinas, propter necessitatem ignorancie quam oportet nos hinc habere de membris ecclesie. Ideo dicit decretum sub auctoritate Gregorii XXIIIª q. IV: Hec autem, quod sicut habitacio ecclesie militantis est inter celum et terram, sic utrarumque parcium cives recipit, sed in finali iudicio discernentur. r Ethecracio quare regula Christi precipit benefaciendo diligere tam amicos quameciam inimicos (ut patet Luce VI°, 27, et ad Romanos VIII°). Omnis, inquit, iniquus bonorum est inimicus. Omnis enim amicus huius seculi inimicus est Dei, inimicus autem Dei bonitatis et iusticie est inimicus. Racionabile itaque et securum est diligere inimicos, quia necesse est dileccionem illam premiari in retribucione finali; odium autem extra caritatem necesse est sequi demeritum. Et hec racio quare Christus voluit hic filios suos atque diaboli esse permixtim nobis absconditos. Nam Matthei XXIV°, 40, loquens de die iudicii dicit confuse: In illa die erunt duo in agro uno, unus assumetur et alter relinquetur, due erunt molentes in una mola, una assumetur et altera relinquetur, duo in lecto uno, unus assumetur et alter relinquetur. Illud autem exponit Augustinus super Psalmum XXXVIᵘᵐ de tribus statibus ecclesie militantis, qui sunt pastores, laboratores et ociatores. Pastores sunt prepositi ovibus Christi, quia instar floris campi et suorum agricultorum debent evellere, destruere, edificare et plantare, ut patet Jeremie I° et Ia Cor. 111°, 6, dicit Apostolus: Ego plantavi, Apollo [p. 202] rigavit, sed Deus incrementum dedit, et sequitur: Dei adiutores sumus, Dei agricultura estis. Illud autem genus pastorum dividitur in duas personas quorum filius Dei assumetur ad beatitudinem et filius diaboli relinquetur ad dampnacionem. Ista autem logica est rectissima sed confusa, quia ignoramus quot et qui descendent ad inferos vel ascendent. Secundum iugum, signans infirmiores activam vitam ducentes, signanter exprimitur per terminos feminini generis; molaris inferior est terra quam colimus, recipiens undique constanter secundum variacionem anguli incidentalis et reflexionis influenciam celestium radiorum. Molaris autem superior qui pigre circumducitur est spera celestium; cui activi molentes preparant terre nascencia et alia mixta inanimata sive artificialia sive naturalia de quibus est negociacio activorum. Celum enim sua circulacione ministrat illis tempus et auram ac unicuique sui generis complementum; cum autem gracia hominis celum circumducitur, signanter dicitur activus molere in pistrino. Tercium vero iugum est quiescencium ab istis duobus officiis, sive sint clerici contemplantes, sive promiscui deprecantes, sive seculares domini imperantes omnes enim tales quiescunt in lecto (ut patet Canticorum 111°), et sunt ambo iuga, ut primum secundum predestinacionem et prescienciam ac finalem perseveranciam et finalem inpenitenciam bipertiti, cum ibunt Iiii in supplicium eternum, iusti autem in vitam eternam (ut dicitur Matthei XXV°, 46).

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 199.9: Example of St. Thomas.
- 199.20: 6. It is objected that on our showing privileges could be held only in grace.
- 200.4: The predestinate holds privilege in a more excellent way,
- 200.10: yet a privilege may be of some avail to the foreknown.
- 200.21: Privileges that are abused should be changed in form.
- 201.4: We cannot recognise the members of the Church.
- 201.10: Hence the rule that we are to love our enemies.
- 201.20: Exposition of Matthew XXIV,
- 201.29: Those in the field are the clergy;
- 202.8: those at the mill, the laity engaged in active life;
- 202.21: those in the bed, those who are tree from active duties.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 198: *vineam* (P is the alinea letter) [R4]
  - 198: *I°* (cap. I°)) [R3]
  - 199: *Beda* (156ᵇ is the folio mark) [R3]
  - 199: *gloriosum* [R4]
  - 199: *privilegium* [R4]
  - 200: *∅* (print has nothing between Ideo and signanter; the inserted run is text from the end of p.199) [INS?]
  - 200: *VIⁱ* (superscript i after VI) [R4]
  - 200: *XIª* [R4]
  - 200: *Nam* [R3]
  - 200: *foret* [R3]
  - 201: *quam* (5 is the line number) [THIN]
  - 201: *oportet* [THIN]
  - 201: *nos hinc* (main token covers two printed words) [THIN]
  - 201: *habere* [THIN]
  - 201: *et iusticie* (main token covers two printed words) [THIN]
  - 201: *est* (15 is the line number) [THIN]
  - 201: *edificare* (f clear) [NW]
  - 201: *∅* (print has 'Jeremie I° et' once; main already has I° (225) and et (226)) [INS?]
  - 201: *I°* [R3]
  - 202: *∅* ('the' is the English side-note (those at the mill)) [R4]
  - 202: *signans* [R4]
  - 202: *ducentes* (glued 'ac' is the English side-note (ac-tive life)) [R4]
  - 202: *signanter* [NW]
  - 202: *influenciam* [NW]
  - 202: *iugum* [R4]
  - 199: *est* [R5]
  - 200: *Ideo* [THIN]
  - 200: *privilegiare* [THIN]
  - 201: *XXIV°, 40,* (print has verse 40 after chapter (old-style 4)) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 198:
17. A A,: Dco decst 18. A: malencolica. 21. In codd.
quosque. 27. A: Reg. 21 cap. B: 12 cap.

p. 199:
i. A in marg. : Beda. 2. B: disscreie. 6. A At: itaque
solucio. n. A in marg. : Conclnsio. Recte: obieccio. iS. A:
malencolica. 20. A in marg. : Sexta conclusio. 28. A in marg.:
Responsio.
r. Venerabilis Bedae Opp. tom. V, pag. 676. 11. This is
thc Antiphon in the second nocturn on the feast of S. Thomas
Archbishop (Sarum Breviary, Procter and Wordsworth, vol. I.
col. CCLI.)

p. 200:
21. A in marg. : Correlarium. 22. A A,: scd privilegio. 2j. A
in marg.: Uuplcx mors. 29. A in marg. : Conclusio.

p. 201:
19. 20. B : permixtum. 21. A: loquens dc Dei iudicii. 26. A
111 marg : Augustinus. 29. agricultorum : A, addit: id cst apostolorum.
6. Decr. II. p., causa XXIII, q. IV, c. XV. 12. The pas-
sage occurs neither in I.uke, nor in the Ep. to the Romans.
25. I.uke, XVII, 35. 26. See Aug. Enarr. in Ps. XXXVI,
Serm. I, Opp. IV, I, p 258.

p. 202:
9. AB: Exprimit. 14. spcra i. e. sphacra. 19. A: circum-
ciditur corrcxit in circumducitur. so. A: lit. d in marg. dccst.
3i. Numerus capituli in codd. deest. In codd.: lacuna. 3i. B: Nam
decretum.
```

---

## Chunk 09-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-09-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-09-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "202.30–204.26"
divisions: "cap. 9 (heading 'CAP. IX.' at 182.6); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "450 words; 404 unanimous or majority-real; 39 settled by vote (R2 26, R3a 12, R5a 1); 7 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n239–n241 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 9, part 6: [TITLE]

## ¶1 · 202.30–204.26

> [p. 202] Et raciones omnium istorum sunt nobis abscondite, (ut dictum est.... capitulo). Nam secretum divine ordinacionis dies nostre mortis et dies finalis divisionis ideo sunt a mortalibus occultati, ut nec presumamus [p. 203] nec despiciamus, sed timentes senciamus humiliter et amemus generaliter; et quoad duo sequencia, ut vigilemus a peccato continue et obviam sponso cum oleo et lumine sollicitissime nos paremus. Et ista ignorancia est racionalis et salubris. Ideo pertinenter dicit canon sub auctoritate Augustini XXIIIª, q. IV: Quantus arrogancie tumor est, quanta humilitatis et lenitatis oblivio quantaque arrogancie iactancia, ut quis se credat posse facere quod nec apostolis concessit dominus, ut zizannia videlicet a frumento posse se putet discernere. Ex istis formari potest talis racio: Quilibet christianus debet in ambiguis viam perplexam abicere et viam securam eligere, sed omnis dominus secularis dotans vel privilegians ecclesiam est christianus cui talis duplex via exponitur, ergo debet eligere viam certam: sed certum est quod dare elemosinas temporales est via certa, dare autem elemosinas perpetuas est via ambigua, ergo prima via facilior et cercior est eligenda, neglecta alia. Quis queso presumeret viam eligere per quam verisimiliter credere posset Deum offendere? Quis insuper dubitat quin ex perpetuacione elemosinarum fundantur lites et bella per que subtrahitur religio christiana, originantur utrimque superbia et cetera vicia, in tantum quod elemosinarius insurgit saltem contencione cauterizante contra elemosinantem, et (quod est pessimum) surrepentibus multis discolis loco veri cleri cui donata sunt temporalia, aspiratur ad statum propter temporale lucrum, contempto vero officio? Omnia autem ista vel extinguerentur vel mitigarentur data elemosina temporaliter probabiliter egenis qui fideliter peragerent incumbens ministerium, et non data cece ad securandum [p. 204] discolos futuros quos datarius ignorat. Hoc enim plus consonat legi Christi qui nec suscepit nec docuit elemosinas tales fieri, sed pocius oppositum. Nec dubium quin temporalis elemosina de decimis, de oblacionibus et sponte oblatis sufficeret ad numerum tanti cleri quanto eget ecclesia. Non ergo ex veteri testamento vel novo fundari potest tanta et talis dotacio. Unde sophisma diaboli procedens nunc ex equivocis, nunc per locum ab insufficiente similitudine conturbat ecclesiam dicentem Canticorum VI°, ii°, Anima mea turbata est propter currus Aminadab. Nunc enim ecclesiastici procedunt currati cum multitudine cliencium quasi reges et reputant privilegium quod ceci et inhabiles et ignari preficiantur in altis statibus quoad mundum (de qua materia patet alibi). Sed redeundo ad difficultatem dicitur quod potentatuum seculi est privilegia terrena (quantum in eis est) concedere, et Dei virtute et gracia confirmare sine quibus non recipit privilegium ultimum complementum. Unde si hoc moveret, tunc nullus sacerdos posset conficere vel dare sacramenta, nullus fidelis posset facere opera meritoria, nec aliquis homo preter Christum dare alteri quevis dona. Omnia enim ista implicant graciam Dei, ideo non fiunt, nisi Deus approbando preveniat et det graciam; quod solus Deus potest facere.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 203.12: A christian is bound: to take the sure way.
- 203.17: Giving temporal alms is sure; giving perpetual alms uncertain,
- 203.23: since it leads to quarrels,
- 203.27: and induces unfit men to take clerical office.
- 204.16: To sum up: rulers have the power of giving privileges so far as they are confirmed by God.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 203: *nec* (157ª is the folio mark) [R3]
  - 203: *putet* (italic) [R3]
  - 203: *offendere* [R3]
  - 204: *Christi* [R3]
  - 204: *preficiantur* [NW]
  - 204: *eis* [R3]
  - 203: *XXIIIª,* [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 202:
9. AB: Exprimit. 14. spcra i. e. sphacra. 19. A: circum-
ciditur corrcxit in circumducitur. so. A: lit. d in marg. dccst.
3i. Numerus capituli in codd. deest. In codd.: lacuna. 3i. B: Nam
decretum.

p. 203:
4. Codd. : solitissime. 12. A in marg. : Racio. ij. A in
matg.: Nota contra perpetuacioiicm elemosinc. 20. B: conteiiciose.
6. Dccr. II. p., causa XXII, q. IV, cap. XV.

p. 204:
n. Propter quadrigas in Cant. Canticor. VI, n. 14. i5. B: altis
stautibus. 28. A in marg. : Nota de privilcgio Westermonasterii
(Above 15;1 witliout mark of rcfcrcncc).
```
