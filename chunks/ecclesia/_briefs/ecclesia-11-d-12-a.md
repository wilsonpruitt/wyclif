# Translation brief: ecclesia 11-d–12-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-11-d.md chunks/ecclesia/wyc-ecclesia-11-e.md chunks/ecclesia/wyc-ecclesia-12-a.md` once and fix what it reports.
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

## Glossary (the 156 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| vulgares | the common people | The third estate. Not "the vulgar". Pilot. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| facinus | misdeed | Wyclif equates it with "felony" (239.13, 239.21). Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
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
| descripcio | definition | Not "description" (T. p. 363). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 11-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-11-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-11-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "242.19–246.25"
divisions: "cap. 11 (heading 'CAP. XI.' at 227.19); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "998 words; 898 unanimous or majority-real; 80 settled by vote (R2 39, R3a 28, R3b 4, R5a 9); 20 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n279–n283 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 11, part 4: [TITLE]

## ¶1 · 242.19–243.10

> [p. 242] Secundo obicitur per hoc quod iuxta istam senten- ciam excluderetur libertas privilegii, eo quod nemo sciret qui essent digni aut indigni, qui puniendi aut qui dimittendi, aut qualis vel quanta debet esse remissio. In ampliacione ergo privilegii est via securior Hic dicitur negando assumptum et consequenciam sequentem; nam locus potest ex effectu probabiliter COgnoscere qui fugitivi sunt fructuose penitentes, et solum tales prius criminosi debent ex lege Dei et iuris ecclesie habere in illa refugium. Nam fugientes illuc cum ere alieno et negantes restitucionem quantumcunque habundant ostendunt se incapaces refugii, et sic de cunctis facinorosis qui non disponunt se quantum sufficiunt ad emendam. Et si obicitur quod [p. 243] ex talibus signis sensibilibus non fit demonstracio, cum potest esse sensus illusio vel aliunde decepcio, dicitur quod obieccio est inutilis, cum non requiritur talis infallibilis noticia ad elemosinas faciendas. Tunc enim periret omnis correccio et omnis sentenciacio secundum leges humanas et omnis elemosina, cum perinde homo dubitaret, si ille cui faceret elemosinam sit diabolus incorporatus vel membrum eius; cuius defensio foret contra voluntatem Dei, cedens ad perturbacionem ecclesie.

[ENGLISH]

## ¶2 · 243.11–245.25

> [p. 243] Unde cum dilatacio talis non foret ampliacio privilegii sed perversio privilegii, pars securior foret tenenda, innitendo iuri communi in cuius execucione exclusa est undequaque iniuria. Ulterius, si queratur de limitibus remissionis talium profugorum, videtur mihi quod pium esset, quoad debitum pecuniarum, docto quod fugitivi sine suo demerito sint casualiter impotentes, ut ex naufragio, incendio vel rapina, quod a suis creditoribus et specialiter a mundi divitibus et clericis dimittantur liberi, vel totaliter vel in parte; egenis autem creditoribus satisfaciant suo laboricio paulative. Unde mirum est pluribus quomodo extortus fuit sensus privilegii ad debitum pecuniarum, cum ante XXVᵘᵐ annum Edwardi IIIⁱ non esset pro tali debito ad ecclesiam fugiendum, privilegiantes autem per multos annos ante illud tempus non intenderant, sicut nec poterant, ut nullus debitor illuc fugiens teneatur satisfacere creditori. Nam XIª q. IIIª ex auctoritate beati Isidori sic habetur: Qui consentit peccantibus et defendit aliquem delinquentem maledictus erit aput Deum et homines et corripietur increpacione severissima. Hinc eciam quidam sanctissimus [p. 244] pater ait: Si quis peccantem defenderit, acrius quam ille qui peccavit coherceatur. Hinc eciam alius pater ait: Si quis alterius errori consenserit, sciat se cum illo simili modo culpabilem iudicandum. Sufficit ergo prepositis peccatum proprium etsi non cumulent alienum. Insuper aliud mirum est quomodo extortus est sensus nephandus ex dicto privilegio quod licet sceleratissimis cubare ibidem in suo crimine sine correpcione penali pro tota suo periodo, cum nec verba privilegii illud annuerint. Nam potissime extorqueretur de isto verbo quod habeant ibidem omnimodam libertatem. Sed revera ex istis verbis patenter infertur oppositum, cum libertas ad pausandum in peccatis non foret libertas, eo quod tunc spiritus infernales forent liberrimi. of Et si queratur quantam libertatem habebunt ibidem, dicitur quod magna libertas est concessa a regibus ecclesie Anglicane, ultra hoc quodhabent regna alia vel exprimunt iura canonica, scilicet quod quilibet fugitivus ad quamcunque ecclesiam in Anglia pro qualibet felonia habeat ibidem tempus quadraginta dierum instar Ninivitarum et penitencium in Quadragesima quibus tot tempora penitencie sunt concessa. Pro illo tamen loco excedit illud privilegium in duobus: primo in hoc quod, ubi in aliis locis restringitur situs ad basilicam Vel paucos passus extra ecclesiam, ibi possunt secure quiescere per totum precinctum Westmonasterii, ubi eciam in aliis ecclesiis limitatur causa fuge ad feloniam, ibi extenditur ad quodcunque facinus vel delictum, cum quo stat regni prosperitas et integritas regalie. autem placeret regi et suo consilio concedere fugitivis illius loci libertatem maiorem, gauderem et assidue procurarem, sed (si non fallor) ex debito sensu verborum privilegii non potest homo convincere ampliorem. [p. 245] Et si arguitur quod privilegium de immunitate ecclesie Anglicane repugnat iuribus canonicis supradictis, dicitur quod non, quia omnes ille leges sunt locales, obligantes tantum eos qui ipsas acceptant, tam in materia quam in forma. Anglia autem quia prius habuit consuetudinem misericordius libertantem ecclesiam, ideo dimissa martirizacione sui populi venit coronanus ad fugitivum, querens causam sui aufugii; quod si pro alio delicto quam felonia aufugerit, libertas ecclesie non ad eum. Si autem pro felonia, dum tamen non repugnat provido statui regni, licet sibi per quadraginta dies libere ibi quiescere et in fine unum ex tribus eligere. vel per stratam regiam tamquam exulans exire provinciam, vel publice exire, stando tamquam indigena iuri regni, vel tercio remanere infra basilicam sine hoc quod ultra de cibariis provincie sustentetur. Et ut mihi videtur) privilegium illud foret misericordius et racionabilius quam privilegium notans casus in quibus salvandi in Anglia extracti sunt alibi et occisi. Ideo laudemus nostros principes, non vendicantes alieno iure, quod consuetudo Anglie non permittit; nam Angliam non obligant aliena privilegia alleganda, sed sufficit nobis fructus ulterioris privilegii, nec est aliqua lex fundabilis pro ambobus.

[ENGLISH]

## ¶3 · 245.26–245.33

> [p. 245] Tercio principaliter arguitur contra dicta de descripcione privilegii: videtur enim primo quod omnis lex sit privilegium, cum omnis lex individua sit lex privata, concessa ad utilitatem ecclesie vel persone. Videtur secundo quod non subiacet potestati dominorum temporalium statuere ecclesiam in privilegiis que Christus instituit, quia illa erant dona gracie que solius Dei est concedere.

[ENGLISH]

## ¶4 · 246.1–246.25

> [p. 246] Tercio videtur quod omnis infirmitas vel peccatum sit privilegium, quia cedit ad utilitatem sancte matris ecclesie. Hic dicitur negando assumptum, quia lex communissima non est privilegium, nisi equivocando in predicacione secundum essenciam vocetur omne quod obiective terminat utilitatem privatam, vel privilegiat melioratum privilegium, sicut Deus dicitur gaudium et premium beatorum. Loquendo autem formaliter de privilegio, patet supra dicta descripcio in iure canonico; nam XXVª, q. I, Ideo permittente domino, exprimitur supradictum genus privilegii sub hiis verbis: Privilegia enim dicuntur quasi privata legia, eo quod privatam legem singulis generent. Quam diffinicionem Gregorius innuens ait: Si hoc neque consuetudine generali neque privilegio speciali vendicas, restat te usurpare quod fecisti. Et patet ex iure canonico genus privilegii supradictum. Superaddidi eciam differenciam pro explanacione maiori quod est concessa a principe ad utilitatem ecclesie vel persone, et potest ista differencia pertinenter capi de iure canonico XIXª, q. II, Due sunt, ubi distinguens inter legem publicam et privatam dicit quod lex privata est que instinctu spiritus sancti in corde scribitur, sicut de quibusdam loquitur Apostolus: Qui habent legem Dei scriptam in cordibus suis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 242.19: Objection: 2. It cannot be known who are fit to be protected by the privilege.
- 242.24: Answer: We must judge by acts, as in almsgiving.
- 243.14: Debtors should not be protected, except those who cannot pay through misfortune.
- 243.22: The privilege was not intended for debtors.
- 244.16: The period of immunity should be limited, as in other Churches, to 40 days.
- 244.25: Two points in which Westminster exceeds other Churches.
- 245.7: Coroner's office as to fugitives in sanctuary,
- 245.13: Liberties given to the fugitive.
- 245.26: Third principal argument against us. a) All law is privilege.
- 245.30: b) Secular lords cannot appoint Church privileges, which rest with God.
- 246.1: c) All weakness or sin is a privilege since it brings good to the Church. Answer: a) Such use of the word privilege is an equivocation.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 242: *securior* (hyphenated secu-/rior; main token holds whole word) [R4]
  - 243: *ex* (162ᵈ folio mark glued in main token) [R3]
  - 243: *demerito* [R3]
  - 243: *casualiter* [NW]
  - 243: *IIIⁱ* (small superscript i after III) [R4]
  - 243: *XIª* [R4]
  - 243: *IIIª* [R4]
  - 244: *magna* [R3]
  - 244: *regibus* [R4]
  - 244: *regna* [R4]
  - 244: *restringitur* [R4]
  - 245: *descripcione* (hyphenated descrip-/cione; main token holds whole word) [R4]
  - 245: *privilegiis* [R4]
  - 246: *Tercio* [R3]
  - 246: *melioratum* [NW]
  - 246: *XXVª* [R4]
  - 246: *legia* [NW]
  - 246: *XIXª* [R4]
  - 244: *pater* [THIN]
  - 243: *XXVᵘᵐ* (superscript um) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 242:
1. In codd.: utique. 7. 8. B: ze vindicte. i3. B: digni; A cor-
rexit: dignior. iS. B: accusat. 19. A in marg. : Contra. Se-
cunda obieccio. 24. A in marg. : Responsio. 25. A in marg. :
Nota, qui fugitivi debent gaudere de immunitate ecclesiarum, quia peni-
tentes etc (Above K)2J without mark of reference). 3i. 32. B: sed
quantum.

p. 243:
16. A: esset csset. 22. B in marg. man. alt. : Pena furum.
27. A in marg. : Contra defcnsores peccancium. 29. A in marg. :
Ysidorus. ^o. Incodd.: maledictus est ; correxi e decr. supra mem.
29. Dec. I! pars, causa XI, q. III, Cap. C.

p. 244:
[. In decret.: defendit. 3l. A A,: fupitivi. 34 A A, : homo
deest; A,: committere. A B: convicere; correxi.

p. 245:
g. A B: felononia. u. B in marg.: Pcna raalcdicti; A A,: dum
tamen repugnat. 12. A in marg.: Nota. 26. A in marg. : Contra.
Tercia obieccio. Arguitur contra dcscripcionem privilegii (Above i63b
without marli of reference). 29. A A,: privata et concessa.

p. 246:
l. ad lit. Q. Lit. P decst in cod. 2. B: quia concessit ad.
3. A in marg. : Responsio. 4. B in marg. : Ethymologia privilegii.
10. A in marg.: Gregorius. In codd. XXV, q. II. Correxi. 12. i3. B:
privatam legem; legia — iegem: deest. 23. B in marg. man. alt. :
Lex privata est instinctu spiritus sancti. 25. B in marg. : Lex com-
munis dupliciter- A in marg. : Lex dicitur communis dupliciter.
10. Dec. II pars, causa XXV, q. I, c. XVI. 2i. ib. causa
XIX, q. II, c. II.
```

---

## Chunk 11-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-11-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-11-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "246.26–250.16"
divisions: "cap. 11 (heading 'CAP. XI.' at 227.19); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "858 words; 767 unanimous or majority-real; 77 settled by vote (R2 46, R3a 22, R3b 2, R5a 6, R6a 1); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n283–n287 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 11, part 5: [TITLE]

## ¶1 · 246.26–248.20

> [p. 246] Sed quia videtur per verba decreti quod membra coincidunt, licet racio non sit diversa, ideo notandum quod lex potest dici communis dupliciter, scilicet obiectiva obligacione vel formali predicacione; primo [p. 247] modo est lex communissima quod Deus est super omnia appetendus, cum nedum omnem creaturam racionalem sed omnem creatam substanciam semper obligat. Nam Deus est bonum quod omnia appetunt, et sic omnia alia mandata decalogi sunt leges communes obiective, cum necessario omnes homines obligant. Leges autem communes predicacione sunt species vel genera legum que in suis individuis sunt fundata, ut clericum curare de sua fama et genera similia, sive accepta pro legum privatarum multitudine, sive pro universalibus quiditative predicatis de sua specie. Et sic iste due maneries legum non sunt contrarie in suo analogo, cum canon describit legem publicam que a sanctis patribus scriptis est confirmata; quod notum est competere cuilibet vero privilegio, sicut et descripcio privilegii competit legi communi. Unde illa lex que est communis private parti ecclesie est privilegium respectu sui tocius, ut lex que est communis singulis personis dati monasterii monachorum est privilegium toti domui, et dotacio in temporalibus, si est lex communis toti clero possessionato et singulis personis eiusdem, tunc est privilegium respectu persone cleri dotate, eo quod persone cleri exproprietarie viventi non convenit sed privatim persone priori. Cum ergo iuxta decretum omnis lex privata a spiritu sancto inscribitur, manifestum est quod omnis lex privata concessa est a principe ad utilitatem ecclesie vel persone, eo quod opera trinitatis sunt indivisa ad extra. Deus autem nescit docere vel dare nisi utilia, et sic omnis lex creata individua est privilegium. Et patet quomodo loquendum est logice de privilegiis, detecta equivocacione termini, ut oportet. Ad secundam instanciam negatur assumptum, cum Christus dedit ecclesie duplex genus privilegii, quoddam [p. 248] extrinsecum, affirmativum, negativum vel privativum, ut Matthei X°, 9, dicitur quomodo privilegiavit discipulos, quando misit illos ad predicandum: Nolite, inquit, possidere aurum neque argentum neque pecuniam in zonis vestris. Privilegia autem corporalia positiva concedit eis, ut patet Luce X°, 7: In eadem, inquit, domo manete edentes et bibentes que aput illos sunt; dignus est enim operarius mercede sua. Talia autem privilegia instrumentaliter et ministratorie concedi possunt a domino temporali; sed est dare spiritualia privilegia pociora que Christus prius concessit suis discipulis, ut patet Matthei X, 8: Infirmos, inquit, curate, mortuos suscitate, leprosos mundate, demones eicite, Talia autem potestativa privilegia appropriate conceduntur a domino, que licet princeps terrenus non posset concedere, tamen concedendo temporalia privilegia propriatorie potest disponere ut Deus concedat privilegia pociora, sicutaperiens fenestram vel removens prohibens est occasio, unde lumen solis per domum infunditur.

[ENGLISH]

## ¶2 · 248.21–249.2

> [p. 248] Ritus ergo sensibiles quos Christus instituit tamquam signa efficacia spiritualis privilegii sunt diligencius observandi, cum impossibile sit, ut rite observans hec privilegia sensibilia non privilegietur a Deo intrinsecus per privilegia pociora. Ideo (ut dixi proximo capitulo) sunt diligencius quam humanitus adinventa privilegia observanda, sicut patet in parabola domini de Recabitis a vino abstinentibus ex precepto patris sui Recab (ut exponit: Jeremie XXXV, 8). Et hec racio quare Christi privilegia sunt diligencius audienda, reccius exponenda et solicicius defendenda, quia ut illa spernuntur innitendo ad alia, perit religio christiana; et sic domini temporales tenentur privilegia [p. 249] Christi tam positiva quam privativa defendere et omnes ritus illis contrarios animose destruere.

[ENGLISH]

## ¶3 · 249.3–249.34

> [p. 249] Unde videtur mihi quod collegium predicte abbathie primo attenderet, si vendicatum privilegium sit privilegiis Christi contrarium. Secundo quod lucrum reportabit ex privilegio sic defenso, quia indubie si non meritum quoad Deum sed nude mundi gloriam ex privilegio reportat anime detrimentum. Tercio, supposito quod reportet ex operibus misericordie indultis profugis salutem anime, attenderet cum suis fautoribus quod pro veris privilegiis plus necessariis defendendis diligenciam tantam apponerent vel maiorem. Sepe nempe mundo decepti cece preponderant folia fructui, umbram luci, ymmo venenum pruriens temporale perpetue saluti. Ad tercium dicitur quod falsum assumitur, nam peccatum cum non sit privata lex nec concessum principe non est privilegium. Quamvis enim princeps huius mundi excitat ad peccandum, non tamen potest concedere, sicut nec Deus, ad illud licenciam, et si per impossibile concederet ad hoc vel pretense licenciam, hoc non faceret ad privilegiandi commodum sed ad dampnum. Conceditur tamen ex immensitate potestatis veri principis quod racione cuiuscunque peccati occasionatur ecclesie Christi verum privilegium, cum timentibus Deum omnia cooperantur in bonum Rom. VIII°, 28; non quod peccatum sit eis privilegium, sed quod profectus de peccato occasionaliter ortus cedat eis in privilegium. Et hoc est verum non solum de alienis peccatis sed de peccatis propriis que predestinati perpetrant. Conceditur tamen quod pena cedit filiis in privilegium, cum stimulus carnis a Deo datus apostolo cessit sibi ad virtutis exercicium, ut patet IIa Cor. XII°.

[ENGLISH]

## ¶4 · 250.1–250.16

> [p. 250] Unde sancti plus contentantur de tribulacione quam de mundana prosperitate propter securitatem et fructum meriti ampliorem, dampnati autem habent quoddam bonum ultra bonum nature ex merito Christi et sua punicione iusta; quod bonum, licet sit bonum utile beatis et honestum domino punienti, non tamen videtur mihi quod illud bonum sit eis privilegium utile vel honestum sed bonum mitigativum malicie vel quomodocunque aliter apcius nominetur. Unde licet sit privata lex concessa a principe, non tamen ad utilitatem persone cui inest formaliter, nec contendo sed concedo ad sensum equivocum quod illa dampnacio est privilegium beatis, cum racione iuste punicionis suorum hostium qui serviunt eis perpetuo suum gaudium quodam-, modo maioratur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 246.26: Law is common in two senses; of obligation and assertion.
- 247.17: A law may be common as to a part, yet a privilege in respect of the whole.
- 248.1: b) It is true that the highest privileges are the gift of God only,
- 248.13: yet the ruler may so employ earthly privileges as to make the Church apt to receive higher gifts.
- 248.21: Rites or privileges instituted by Christ are to be specially observed.
- 250.1: although God uses it for good, even to the wicked.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 247: *modo* (Q alinea letter + 163ᵇ folio mark glued) [R3]
  - 247: *monasterii* [R4]
  - 247: *vel* (bold argument numeral 1 glued) [R4]
  - 248: *∅* (print has pri-/vativum; main already holds privativum whole at pos 4) [INS?]
  - 248: *∅* (print has Matthei X°, 9 once; main pos 6 already covers Matthei X° (glued), 9 at pos 7) [INS?]
  - 248: *zonis* (z-form ʒ in italic zonis; print spelling) [NW]
  - 248: *corporalia* (5 after it is the line number) [R4]
  - 248: *Talia* [R4]
  - 248: *proximo* (25 after it is the line number) [R3]
  - 249: *Christi* (163ᵈ folio mark in margin) [R3]
  - 249: *cum* [R3]
  - 250: *Christi* [R3]
  - 248: *negativum* [THIN]
  - 248: *Matthei X°,* (token covers two words; X read as \) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 246:
l. ad lit. Q. Lit. P decst in cod. 2. B: quia concessit ad.
3. A in marg. : Responsio. 4. B in marg. : Ethymologia privilegii.
10. A in marg.: Gregorius. In codd. XXV, q. II. Correxi. 12. i3. B:
privatam legem; legia — iegem: deest. 23. B in marg. man. alt. :
Lex privata est instinctu spiritus sancti. 25. B in marg. : Lex com-
munis dupliciter- A in marg. : Lex dicitur communis dupliciter.
10. Dec. II pars, causa XXV, q. I, c. XVI. 2i. ib. causa
XIX, q. II, c. II.

p. 247:
4. B: Deus bonum. 9. A A, : clericum creare. 19. B:
dati — personis deest.

p. 248:
15. A: appropriata correxit in: appropriate. 17. AA^: preparatoric.
21. A in marg.: Conclusio. Ritus. 24. B in marg.: Ritus sensibiles
a Christo instituti sunt obscrvandi plus quam alii. 28. A: Racabitis
correxit in Recabitis; B in marg.: de Recabitis.

p. 249:
3. A in marg.: Nota tria 8. B: detrimentum — salutem deest.
lb. A: perpctuo. 34. A in marg.: Nota.

p. 250:
16. maioratur. A: Sequuntur diio versus Bohemici:
W Anglii wyerna dwa knyezy
pro slowo bozye w zalarzy wyezye.
Id est : In Anglia duos fidelcs presbyteros
pro sermone divino in carcere incarcerant.
18. A in marg. : Prima obieccio. 24. A: defensioni predicti privilegii
impcdire. Aj defensionem . . . impedire.
```

---

## Chunk 12-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-12-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-12-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "250.18–254.23"
divisions: "cap. 12 (heading 'CAP. XII.' at 250.17); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "929 words; 834 unanimous or majority-real; 80 settled by vote (R2 45, R3a 23, R3b 2, R5a 6, R6a 4); 15 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n287–n291 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 12, part 1: [TITLE]

## ¶1 · 250.18–252.25

> [p. 250] Ex istis colligi potest solucio tam vulgarium obiectuum quam scolasticorum quos quidam seminant, quando deficiunt eis efficacia argumenta. Sic enim declinant quidam ad commenta mendacii, dicentes quod nos nitimur destruere privilegia sancte matris ecclesie, unde et commovent milites et alios quos credunt ex sperato lucro defensioni privilegii predicti intendere quomodo defenderent ipsum, destruendo eius adversarios, sub obtentu eterni premii ex operibus pietatis. [p. 251] Sed tales attenderent ad scolam et fructum mendacii, Nam XXIIª q. ultima, ex auctoritate beati Ambrosii sic habetur; Cavete fratres mendacium, quia omnes qui ipsum amant filii diaboli sunt, Nec solum in falsis verbis sed eciam in simulatis operibus mendacium est. Mendacium quippe est christianum se dicere et opera Christi non facere. Mendacium est episcopum, sacerdotem vel clericum se profiteri et contraria huic ordini operari. Et tales leges ecclesie predicari debenttam clericis maioribus quam minoribus, cum sint precipua lex eorum, nec non et laicis, cum pater mendacii cum suis sophistis infecit mendaciis magnam partem vocate ecclesie. Nam pretendentes se esse sacerdotes vel clericos et non facientes quod incumbit illi officio, falso nomine, mendacio et ypocrisi decipiunt plebem Dei. Debent enim exproprietarie vivere tamquam humiles et utiles procuratores pauperum, quorum bona custodiunt. Unde beatus Ysidorus, III° libro, De Summo Bono c. XLII°: Agnoscat, inquit, episcopus servum se esse plebis, non dominum. Verum hoc caritas, non condicio exigit. Et XVIª, q. I, sub auctoritate Jeronymi Damaso pape scribitur quod quicquid habent clerici pauperum est. Pretendere ergo dominacionem secularem eciam plus quam laici super tam alienis bonis pauperum est horrendum mendacium. Non ergo debet fidelis propter talia mendacia non predicare populo periculum ex declinacione [p. 252] a lege domini, quia ut dicitur XIª, q. IIIª, inter verba: Sufficit christiano invocare in testimonium operis purgatam conscienciam atque Deum. Habemus, inquit Gregorius, Paulum dicentem: Gloria nostra hec est, testimonium consciencie nostre. Job quoque dicit: Ecce in celo testis meus. Si, inquit, est nobis testis in celo, testis in corde, dimittamus stultos foris loqui quod volunt. Quid enim aliud detrahentes faciunt nisi quod in pulverem sufflant et in oculos suos terram excitant, ut unde plus detraccionis perflant, inde magis, nichil veritatis videant. Si, inquam, publicarem istam sentenciam quam predico principaliter propter lucrum seculi vel laudem hominum, ego essem me ipso stulcior, lavans laterem, quia scio quod fama vel favor populi est valde flexibilis et vertibilis propter timorem, favorem vel odium instar venti. Sed cum veritas domini manet semper, non movet dicta infidelis commocio fidelem servum Christi, ut omnino taceat, quia Act. XVII° et XIX° legitur quomodo synagoga Judeorum et principes sacerdotum concitaverunt vulgum, Demetrium et artifices facientes edes argenteas Diane, ex quibus quesierunt questum non modicum, commovere populum clamare constanter: Magna Diana Ephesiorum, sed post conversi cognoverunt quod doctrina apostoli fuit eis utilior.

[ENGLISH]

## ¶2 · 252.26–253.7

> [p. 252] Detestamur autem occisionem hominum nedum in Westmonasterio sed altrinsecus inter regna, sed distinguimus inter extraccionem pro tutela regni, et castigacione hominum salubri hominum legiorum de quo facta fuit nobis questio, et inter occisionem que facta fuit preter preceptum aut voluntatem regis vel sui consilii. Unde hominibus armorum plus optamus prosperitatem [p. 253] et requiem quam adversarii quorum falsa exheredacione et ceca excitacione tot prelia oriuntur. Unde testis sit mihi Deus: Ego vellem si Deo placeret quod nedum illa ecclesia sed quelibet ecclesia Anglicana haberet per precinctum viginti milliarium plenam libertatem pro omnibus fugitivis, unde plenam libertatem sancte matris ecclesie sicio modo meo.

[ENGLISH]

## ¶3 · 253.8–254.23

> [p. 253] Secundo principaliter arguitur per hoc quod dicta de potestate privilegiandi nedum sonant in Dei blasphemiam sed derogant potestati pape et regalie regum seculi. Dictum est enim quod Deus non potest auferre quicquam ab homine stante iure suo, nisi satisfaciat aliunde; quod repugnat potencie adnichilandi, et multo magis dominus papa non potest licite auferre beneficium a digno nisi deliquerit. Nec rex habet super omnibus bonis sui regni plenum dominium; que videntur sonare blasphemiam et sacrilegium. Hic negatur conclusio, cum Deus absolute necessario habet summam potestatem privilegiandi, et illa est infinitum maior quam aliqua potestas creata. Quantum ad primam instanciam, concedi debet conclusio: nam si Deus aufert quidquam ab homine stante iure suo sine hoc quod recompenset aliunde, tunc iniuriatur illi homini, quod non potest. Nam iustum est quod haberet ablatum, cum stat ius primum, ut ponitur, sed nemo est causa quare ius illud tollitur nisi Deus, ut ponitur; ergo solus Deus est causa illius iniurie. Et per consequens, cum iusticia sit constans et perpetua voluntas divina, tribuens unicuique quod suum est, patet cum veris sequi quod Deus est contrarius sibi ipsi, quia simul vult quod habent datum bonum, cum sit iustum, et vult quod nunc non habeat, cum aufert. Loquimur enim de habere opposito ablacioni [p. 254] qua Deus aufert, et de iure ad sic habendum pro eadem mensura. Similiter vel est ablatarius contentatus de ablacione Dei vel remurmurat vel est neuter. Sed si contentatus, meretur a Deo meritum vel augmentum meriti, quod est valencius quam foret abicio oblati, et per consequens, Deus per commutacionem vel recompensacionem super remunerat. Si ablatarius remurmurat, perit propter peccatum suum ius habendi, et sumus extra casum conclusionis, sicut Egipcii forisfacientes in capitalem dominum exciderunt a iure bonorum a quibus ex mandato domini habentis ipsa in fisco fuerant spoliati. Cui, inquam, debuit iustus iudex dare bona sic confiscata nisi servis suis qui prius ipsa meruerant? Si autem ablatarius sit neuter quoad actum explicitum, equanimiter tollerat ipsum eventum, et quicquid Deus decreverit faciendum, et per consequens, accrescit in merito; talem enim actum vel habitum confusum oportet inesse omni iusto; et patet conclusio. Unde ista fides de absolute necessaria iusticia et misericordia Dei facit christianos gaudenter pati et gratulanter acceptare quicquid prosperitatis vel pene eis acciderit, quia sciunt demonstrative quod Deus non potest eis humiliter pacientibus deficere, quin loco ablati tribuat pociora.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 250.18: Objections: 1. We are charged with wishing to overthrow the privileges of the Church. Answer: This charge is false.
- 251.1: Falsehood may consist in act or in word.
- 251.14: Those who say they are priests should live in poverty;
- 251.21: and if they claim secular rule it is a horrible falsehood.
- 252.1: We must not let fear of detraction keep us from our duty.
- 252.26: We detest homicide at Westminster or elsewhere.
- 253.8: 2. We are charged with derogating from the power of the Pope.
- 253.18: God cannot take anything from the righteous without compensation.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 250: *CAP. XII.* [HEAD]
  - 250: *deficiunt* [R3]
  - 250: *Sic* [R4]
  - 250: *∅* ('is' is English side-note text (This charge is); print: dicentes quod nos, main has quod at 136) [INS?]
  - 251: *tales* [NW]
  - 251: *profiteri* [R4]
  - 251: *ypocrisi* [R4]
  - 252: *XIª* [R4]
  - 252: *IIIª* (164ª A after it is folio mark + alinea) [R3]
  - 252: *regna* [R3]
  - 252: *legiorum* (print: hominum legiorum) [R4]
  - 253: *illa* [R3]
  - 254: *gratulanter* [NW]
  - 252: *lege* [THIN]
  - 254: *aufert* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 250:
16. maioratur. A: Sequuntur diio versus Bohemici:
W Anglii wyerna dwa knyezy
pro slowo bozye w zalarzy wyezye.
Id est : In Anglia duos fidelcs presbyteros
pro sermone divino in carcere incarcerant.
18. A in marg. : Prima obieccio. 24. A: defensioni predicti privilegii
impcdire. Aj defensionem . . . impedire.

p. 251:
1. A in marg. : Rcsponsio. Malus episcopus, saccrdos vcl clerius non
cst talis (Above 164», without mark of rcference). '}. A in marg. :
Contra mendacium. 9. A: legcs deest. B in marg. : Lcx pungnans
(sic) contra mcndaces opere vel sermone. Mcndacium duplex. 18. A
in marg. : Ysidorus. 21. A in marg.: Jcronymus. 21. In codd.
2. Dec. II pars, causa XXII, q. V, 0 XX. 18. Isidori
De Summo Bono lib. III, cap. XLII: Agnoscat episcopus se
esse conservum ... 23. Dec. II pars. causa XVI, q. I, c.
LXVIII.

p. 252:
2. A B in marg.: Nota. 4. B in marg. man. alt. : Tcstes duo.
9. 11. A At: et in — perflant dcest. 14. A: laudans laterem.
1. Ib. causa XI, q. III, c. LV et LVL 3. Greg. Epp.
Lib. XI. Ep. II.

p. 253:
5. milliarium in codd. rectius: milliariorum. 8. A in marg. :
Contra. Sccunda obieccio. iR. B: Hic ncgetur; A in marg.: Re-
sponsio. 20. A in marg. : Conclusio. 27. A in marg.: Dif-
ferencic iusticie. 33. A A, : enim decst.

p. 254:
6. B: Vel per. i3. A A,: confiscancia. i5. equininiiter in
codd. 19. A in marg. : Conclusio. 23. tribuet in codd.
24. A in marg. : Deus non potest iniuste auferre nec potest annichilare
(Above 164' without mark of reference).
```
