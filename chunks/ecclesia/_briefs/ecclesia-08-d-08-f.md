# Translation brief: ecclesia 08-d–08-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-08-d.md chunks/ecclesia/wyc-ecclesia-08-e.md chunks/ecclesia/wyc-ecclesia-08-f.md` once and fix what it reports.
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

## Glossary (the 150 rows these chunks use; the full file is GLOSSARY.md)

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
| viare; vians | to be a wayfarer; [one] on the way | The verb of *viator*; tag `g:viator`. Ruled 2026-09-28 (8 sites). |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| familia | household | A great man's retinue. Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| prelatus | prelate | |
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
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| castra caynitica | Caim's castles | The friars' houses; the Wycliffite English name (CAIM = the four mendicant orders' initials). Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| graduacio; graduati | graduation; graduates | Academic. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). Ruled 2026-10-02 (*Eccl.* 72.24). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| practizare | to put into practice | Ruled 2026-09-28 (coordinator, delegated) (4 sites). With *contra* + person, "practise against" (plot), *Dial.* ch. 17. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
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
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii | the propertyless | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| penaliter | in hardship | The adverb of *penalitas*. Ruled 2026-10-02 (76.29, 76.34). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| indoles | promise | The natural promise of a thing (the midwives' argument, *Eccl.* 163.18, 164.1–12; Comestor reads *de dolo*). Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| globus | band | Derogatory collective (*globus reprobus*, *globos claustralium*). Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| penalitas | hardship | "penalty". Ruled 2026-09-28. |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 08-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-08-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-08-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "168.4–172.24"
divisions: "cap. 8 (heading 'CAP. VIII.' at 157.25); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1105 words; 980 unanimous or majority-real; 93 settled by vote (INS 1, R2 52, R3a 32, R3b 2, R5a 4, R6a 2); 32 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n205–n209 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 8, part 4: [TITLE]

## ¶1 · 168.4–169.28

> [p. 168] Ex istis patet primo non equivocantibus quod proprietates que naturaliter competunt trinitati non sunt earum privilegia, cum omne privilegium principaliter ab extrinseco pro utilitate inest privilegiato, et sic solum creatura racionalis est capax privilegii. Patet secundo quod privilegiante aut privilegiato decepto in credendo privilegium vergere privilegiando ad commodum, dum tamen concessum privilegiando cedat ad dampnum tamquam utilitati sue contrarium, non est privilegium sed pocius corruptela. Patet ex hoc quod privilegium (in quantum huiusmodi) est bonum utile, ut non est privilegium infidelibus quod liberati a iusticia exonerati sunt a iugo domini et effrenes ad peccandum subiecti iugo diaboli, nisi forte equivocetur, vocando privilegium quodlibet privans legem. Tercio sequitur quod non est aliquod privilegium, nisi quod princeps pacis concessent, caput universalis ecclesie, dominus Jesus Christus. Patet ex hoc quod non potest esse bonum ecclesie, nisi primo venerit per derivacionem a capite. Si enim primas privatus concedit aliquid et Deus illud non concedit, tunc vel oportet concedere quod Deus non prevenit ipsum in agendo, et per consequens non est causa essencialis cuiuslibet creature, vel aliter quod non est bonum vel rationale quod privilegiatus illud habeat, quia si esset sapiencia Dei, eternaliter ordinaret ut habeat, et cum clemencia spiritus sancti graciose illud donaret; cum Johannis XV°, 5, 4, dicit caput: Sine me nichil potestis facere, sicut palmes non potest facere fructum, nisi manserit in vite, sic [p. 169] [enim privilegium concessum domesticis non est ratum, dum tamen ab essenciali patrefamilias omnipotente et omnisciente indultum non fuerit et optenta eius licencia confirmatum. Ex istis colligitur quod summum privilegium concessum christiano pro via foret quod, exproprietarie vivendo, Christo similius foret anterior in exercitu christiano. Patet primo sic: Iuxta proximum corellarium nullum est privilegium nisi concessum a Christo, ipse autem non potest concedere maius privilegium quam plus assimilando subditum sibi ipsi, ergo etc. Unde Matthei XVIII°, 1, quando discipuli quesierunt a Christo: Quis putas maior est in regno celorum, ipse advocans parvulum sine malicia statuit eum in medio illorum dixitque re et sermone quod qui sic plus se humiliaverit hic maior est in ecclesia militante. Item, cuicunque militi pro statu milicie foret aptacius quod armatus decencius et adiutus specialius ponatur in acie belli, ubi forcior est conflictus, in hoc enim consistit militaris strenuitas. Sed ut dicitur Job VII°, 1: Milicia est tota vita hominis super terram, et iuxta Apostolum Eph. VI°, 12: Non est nobis colluctacio adversus carnem et sanguinem, sed adversus principes et potestates, adversus mundi rectores tenebrarum harum, contra spiritualia nequicie. Ideo patet quod, quanto quis fuerit sic positus anterius in dicto exercitu, indultum est sibi privilegium eo maius quo amplius coronabitur. Et patet ista sentencia de matre

[ENGLISH]

## ¶2 · 169.29–170.4

> [p. 169] filiorum Zebedei que ex instigacione filiorum petebat privilegium a Christo, ut hii sederent in regno suo unus ad dexteram et alius ad sinistram (ut patet Matthei XX°, 22). Sed pueri petentes illud implicite audierunt divinum responsum: Nescitis quid petatis. Potestis bibere calicem quem ego bibiturus sum [p. 170] Quo concesso concessit cis privilegium consequenter Calicem, inquit, meum bibetis, sedere autem ad dexteram meam vel sinistram non est meum dare vobis, sed quibus paratum est a patre meo.

[ENGLISH]

## ¶3 · 170.5–170.20

> [p. 170] Super quo Crisostomus, Omelia XXXV° Operis In-, perfecti notat primo quod diabolus qui seduxit primum virum per feminam movit ut dicti apostoli seducerentur per feminam. Notat secundo quomodo Christus dirigens sermonem ad illos discipulos docet quod illi ex ceca presumpcione atque superba primatum culpabiliter pecierunt, aliter enim non direxisset omnisciens increpativum sermonem ad illos discipulos dimissa femina procurante: Nescitis, inquit, quid petatis. Ideo dicit Cristostomus: O error salutaris qui tocius mundi solvit errorem. Si enim apostoli non sic errassent, unde nos cognoscere poteramus quod non omne quod videtur bonum desiderare bonum est? Cum enim scimus quod aliud est opus bonum et aliud primatus honoris. Et opus quidem bonum desiderare bonum est, primatum autem honoris vanitas est,

[ENGLISH]

## ¶4 · 170.21–172.7

> [p. 170] Tercio notandum quod sive apostoli errore seductic pecierunt primatum in regno temporali sive in regno celorum, sicut videtur ex textu convinci, stulta fuit eorum peticio, cum debuerunt laborem certaminis humiliter petivisse, et ad hoc sine iactancia primatus honor beatitudinis secutus fuisset; honor enim fugientem se sequitur et refugit affectantem. Unde dicit Crisostomus: Desiderium primatus ex iactancia nascitur cordis; qui, inquit, humilis est indigniorem se aliis arbitratur [p. 171] iuxta apostolicum preceptum: Alter alterum existimans superiorem. Et hec racio (ut tactum est superius), quare membra ecclesie et gradus quibus Deus ipsos diligit sunt nobis abscondita. Quarto notandum quod Christus videns alienum spiritum in cordibus templi sui, non more conquirencium castra sua corporalia, disrupit muros castri, sed hostem expulit alliciens eos ad humilitatem qua ipsimet superent tyrannum qui eos turpiter superavit. Potestis, inquit, bibere calicem quem ego bibiturus sum? Ex qua interrogacione mulcente docemur, primo quod oportet victoriam esse voluntariam, si debet esse meritoria, ideo querit Christus ab eis modeste, si possunt pati voluntarie instar sui. Secundo docentur ceteri apostoli non indignari contra duos fratres, cum dominus eorum, contra quem principaliter usurpata fuit iniuria, tam urbane optulit eis idem medium quo ipse meruit dignitatem. Tercio docentur omnes christiani quod pati propter iusticiam sit necessarium cuilibet volenti beatifice premiari, cum dominus incessit per summum gradum illius medii; ideo vocat Christus hoc singulariter suum calicem. e Quinto docemur quomodo Christus non potest suis deficere in concedendo privilegia, et consequenter mercedem ex eorum usu sequentem, cum statim post humilem consensum fraternum quo dixerunt possumus, statim concessit: calicem quidem meum bibetis, ubi non licet fideli ambigere quin concessit duobus fratribus quos prius gratificavit privilegium singulare. Si enim terreni patres noverunt bona data dare filiis suis, quanto plus pater primus post tam gloriosam victoriam quam per alios fecit in principem huius mundi? Lex ergo privata quam princeps pacis, et per consequens tocius ecclesie concessit hiis fratribus ad commodum eorum maximum [p. 172] quod possint regnum celorum rapere armis suis, fuit privilegium singulare. Et ex isto eliciunt doctores quod est dare duplex genus martirii, scilicet affeccione et corporali passione; cum beatus Evangelista non fuit sic passus corporaliter usque ad mortem ut Jacobus, sed uterque iuxta vocem predicti Christi veridicam bibit calicem passionis.

[ENGLISH]

## ¶5 · 172.8–172.24

> [p. 172] Sexto docentur omnes fideles et specialiter prelati f non pompare vel alta sapere de gradus excellencia vel primatu, cum Christus coniungit: Sedere autem ad dexteram vel ad sinistram non est meum dare vobis, sed quibus paratum est a patre meo. Quamvis enim Christus sit omnipotens et eiusdem auctoritatis et operacionis cum patre, pater ex se et ipse per se, tamen Christus more suo loquens humanitus prefert patrem, dicens quod nullum membrum ecclesie habebit mansionem in celo, nisi qui ex auctoritate patris eternaliter inscribitur libro vite; quod licet eleccione eterna sit factum per filium, quia tamen discipuli considerarunt Christum secundum humanitatem, ideo univocando cum eis fuit pertinens Christum vere atque humiliter ostendere minoritatem suam secundum humanitatem, cum non sit menciendum propter devocionem.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 168.4: Only a creature can have privilege;
- 168.9: a true privilege must really benefit the grantee:
- 168.19: Consequently there is no privilege except what is granted by Christ.
- 169.5: The highest privilege is to be allowed to follow Christ in poverty.
- 169.28: Instance of the mother of Zebedee's children.
- 170.21: Primacy is to be desired in labour, not in honour.
- 171.5: Christ's treatment of bis disciples' ambition.
- 171.23: He refused their request but granted that they should drink his cup.
- 172.3: Two kinds of martyrdom.
- 172.8: Lesson of humility.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 168: *quod* (glued I is the bold argument numeral 1) [R3]
  - 168: *proprietates* [NW]
  - 168: *non* (glued 1 is a margin numeral, not text) [R3]
  - 168: *princeps* [NW]
  - 168: *Christus* [R3]
  - 169: *corellarium* (corella-/rium; main token holds the whole word) [NW]
  - 169: *Item* (glued 2 is the bold argument numeral) [R3]
  - 169: *VII°* [R4]
  - 169: *1* (x-height old-style arabic 1 (Job VII°, 1)) [R3]
  - 169: *tenebrarum* (tenebra-/rum; main token holds the whole word) [R3]
  - 169: *amplius* (glued 3 is the bold argument numeral) [R4]
  - 169: *filiorum* (print: filiorum Zebedei) [R3]
  - 169: *filiorum* [R4]
  - 169: *Matthei* (152b is the folio mark) [R4]
  - 170: *Crisostomus* (round C, not G) [R4]
  - 170: *In-* (first half of In-/perfecti; main token is In- plus margin M) [R4]
  - 170: *perfecti* (second half of In-/perfecti at start of next line, before notat; missing from main scan) [INS?]
  - 170: *primum* (trailing a is the margin letter) [R4]
  - 170: *Christus* (trailing b is the margin letter) [R4]
  - 170: *∅* (be is English side-note text (Primacy is to be desired)) [INS?]
  - 171: *Christus* [R3]
  - 171: *corporalia* [NW]
  - 171: *disrupit* [NW]
  - 171: *filiis* [R3]
  - 172: *martirii* [R4]
  - 172: *∅* (Sexto already at pos 50; nothing between it and docentur) [INS?]
  - 169: *enim* (152a folio mark glued) [THIN]
  - 170: *concessit* [THIN]
  - 172: *regnum* [THIN]
  - 172: *armis* (152c folio mark glued) [THIN]
  - 172: *privilegium* [THIN]
  - 172: *∅* (box is English side-note word of (Two kinds of martyrdom)) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 168:
1. B: et fruendi. Codd.: usibili. 2. A A, patet deest. 7. A
in marg. : Nota de privilegiis ecclesie continue infra (Abovc i52° withont
mark of reference). i5. B: ut deest. 16. A: et ss. (literae ss.
extinct.). 28. Racionale sive racionabile; codd.: racio'".

p. 169:
5. A in marg. : Prima conclnsio. 7. A: anteterior. 17. A:
optacius. 18. A A,: specialiter. 28. 13: patct ex ista. 29. A:
Zebei. 33. A: Noscitis.

p. 170:
1. B: consessit illis privilegium in. 5. A in marg. : Cluisoslomus.
M. Litera L. dcest in cod. ib. In codd. Omelia XXVIII. <j. 13 : illos
deest. 10. supcrba scil. presunipcione. 10. In codd.: poterimus.
Corr. cx Op. Imperf. 1. c. 17. In codd.: omne bonum. Correxi e
tcxtu Opcris lmp. 19. In codd. : Et opus quidcm desiderare bonum est.
Correxi c tcxtu Operis Imperfecti. I. c. 27. A in marg.: Crisostomus
5. Opus Imperf. in Matthacuni Hom. XXXV, 1. c, CLII. E.
Cf. Richardi Armachani, Defensio curatorum, Goldast, Monarchia
tom. II, pars II, pag. 1403.

p. 171:
g. A A,: turpitcr supcrant. 2(3. A A, : assensum.

p. 172:
marg. : Martir <T affeccione „ m marg. man. alt. :
passione corporali.
Martirium. 9. A in marg. : humilitas. B in marg. man. alt. : Pri-
matus est fructus humilitatis. 19. tamen; tum in codd. 23. B
in marg. man. alt. : Mcnciendum non est in causa devocionis. 3o. A
in marg. : Crisostomus.
3o. Opus Imperfectum 1. c , pag. CLIII. C.
```

---

## Chunk 08-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-08-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-08-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "172.25–177.30"
divisions: "cap. 8 (heading 'CAP. VIII.' at 157.25); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1213 words; 1076 unanimous or majority-real; 121 settled by vote (DEL 1, R2 73, R3a 33, R3b 1, R5a 10, R6a 3); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n209–n214 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 8, part 5: [TITLE]

## ¶1 · 172.25–177.30

> [p. 172] Unde ad pacificandum discipulos et instruendum eos quale privilegium et prioritatem eligerent, dicit quod qui voluerit inter eos prior vel maior fieri in celis, oportet quod sit servus humilior atque diligencior hic in terris (ut alias ostendi modo opposito) quoad primatum vel honorem seculi. Ideo dicit Crisostomus: Fructum humilitatis posuit primatum [p. 173] celestem, ut quicunque desiderat primatum celestem, sequatur hic humilitatem celestem; quicunque autem desiderant primatum in terra invenient confusionem in celo. Ergo, inquit, iam non sit inter servos Christi de primatu certamen, nec festinet unusquisque eorum quomodo alio maior appareat, sed quomodo omnibus inferior videatur. Et ista doctrina sufficeret toti ecclesie ad eleccionem privilegii vel primatus, nec est possibile quod vere pacificetur ecclesia, antequam ista regula practice sit edocta. Ex istis elicitur quod nullum est verum privilegium ecclesie, nisi de quanto fundatur, docetur vel elicitur ex scriptura. Patet sic: Omnis lex utilis sancte matri ecclesie docetur explicite vel implicite in scriptura, domne privilegium est huiusmodi ex dictis: ergo conclusio. Confirmatur ex sepe dictis: Omnis veritas est in scriptura sacra, omne privilegium est veritas quia lex, ergo conclusio. Unde Augustinus, II° De Doctrina Christiana, in fine: Quicquid homo extra scripturam sacram didicerit, si noxium est ibi dampnatur, si utile est ibi invenitur; et idem dicit epistola quarta ad Volusianum (ut alibi diffuse exposui). Sequitur ergo, si quis quidquid utile extra scripturam sacram didicerit, ibi invenitur, omne privilegium concessum in cartis vel bullis est quiddam utile (ut patet ex diffinicione), ergo omne privilegium ecclesie est in scriptura sacra; ideo cum illa sit maioris auctoritatis et accepcionis quam bulle vel carte (ut dixi alias), ille ut plurimum in clero superfluunt. Nam illis ablatis inniteretur privilegiatus ministerio ecclesie quod est per se causa privilegii, et non sic confideret in [p. 174] cartis dimisso officio. Talis enim securitas confundit ecclesiam, cum telis sophisticis super equivocacione que est ypocrisis et mendacium, diabolus et membra sua concludunt ecclesie. Quis queso non decipitur hodie in adherendo parti ecclesie malignancium et colendo ipsam ut membrum ecclesie? Quis insupera non aspirat ad fastum seculi vel primatum vel privilegium, cum tamen sit sceleratissima corruptela, in tantum quod sepe incidimus in illud ve propheticum Ysaie V°, 20: Ve qui dicitis bonum malum et malum bonum. Nonne diligencia nostra ostendit quod plusb appreciamus cartas et privilegia humana quam scripturam sacram et privilegia que Christus suis instituit? Et indubie ut sic cadimus a quibuscunque veris privilegiis per abusum, quia iuxta beatum Gregorium (et ponitur in decretis XI, q. III. Privilegium) privilegium debet amittere qui sua abutitur potestate. Cum ergo omne racionabile vel utile ecclesie Christi prius ab ipso conceditur et in carta vel libro suo inscribitur, patet quod scrutinio illius libri et condicioni sub qua privilegiavit debemus primo attendere. Non enim sequitur: Datus potentatus seculi concessit hoc ut privilegium date ecclesie, ergo hoc est rationabile sive verum. Ideo oportet ultra concessionem scrutari regulam per quam racio privilegii debeat iudicari. to Esto, inquam, quod Petrus potentatus seculi concedat privilegium Westmonasterio sub hac forma quod quicunque quantumcunque maleficus intraverit septa sua habebit immunitatem omnimodam, sic tamen quod in prima conclusione in qua post introitum a preposito loci [p. 175] sibi opponitur dicat verum. Casus autem videtur possibilis et honestus, cum pro mendacio et pro quocunque scelere posset uti privilegio ad hoc sibi donato, ut dicitur; ergo multo magis pro confessione humili veritatis. Pono insuper quod Petrus maleficus intrans Westmonasterium pro immunitate habenda sit primo interrogatus a preposito Westmonasterii si habebit immunitatem in dicta ecclesia et pono quod Petrus conscius sibi ex dignitate contracta de crimine dicat desperando de venia vel vere reputando se dignum morte temporali, quod non habebit immunitatem in dicta ecclesia; tunc isto casu deducto ad placitum, patet quod ex casu et aliis circumstanciis positis et ponendis utraque pars contradiccionis sequitur, ut noverunt sophiste in materia insolubilium. Et revera quilibet intrans limina ecclesie, ut foveatur in crimine, incidit culpabilius in materia insolubili cuiusmodi est peccatum, quam sequitur Petrum incidere. Unde ego nescio aliter solvere nec credo alium quemquam scire, nisi quod dictum vocatum privilegium non est privilegium, quia non est fundabile in scriptura; et ita generaliter omnis lex privata non fundabilis in scriptura non est privilegium, quia non cedit ad utilitatem ecclesie, cum (ut dicit Augustinus) quicquid utile est ibi invenitur. Et si claudit contradiccionem quod hoc sit privilegium, multo magis omnis casus in quo ponitur dari privilegium loco, ut quicunque intraverit cum quocunque crimine, gaudeat immunitate date ecclesie; illud enim est impossibile plus elongatum ab apparencia quam precedens. Cum multi intrant sanctuarium cum illo peccato, racione cuius tenentur amittere libertatem, ymo cum principium Gregorii sit verum quod omnis et specialiter prescitus [p. 176] privilegium tenetur amittere qui sua abutitur potestate, et omnis criminosus ut sic sua abutitur potestate, cum racione mortalis peccati inficientis abutitur bonis nature: sequitur quod omnis criminose intrans septa ecclesie tenetur ut sic privilegiis ecclesie pro illo tempore non gaudere. Et hoc est notum illis qui sciunt quod quicquid criminosus fecerit racione peccati inficientis peccat mortaliter. Fundet ergo homo racionabilitatem privilegii ex scriptura et aliter nichil valet. Illa autem privilegia que debemus magis attendere plus relucent in speculo scripture, et- minus necessaria plus confuse, quia Deus qui non potuit in privilegiis et scriptis ipsa testantibus sponse sue deficere, scivit quod palea plus diverteret ad terrena quam celestia, ideo ut gradus notificacionis scripture sit nobis pro regula, expressit privilegia spiritualia de corporalibus que adducerentur confusam adiciens disciplinam. of Ex istis tercio colligitur quod summum privilegium pro statu vie foret ecclesiam esse exoneratam possessione civili temporalium, currendo libere post Christum in evangelica paupertate. Patet ex duabus conclusionibus precedentibus, nam ut sic disponitur fidelis Christo similius et paracius ad conquirendum regnum celorum. Unde et hoc privilegium notatur in ecclesia expressius, alcius et crebrius carioribus Christi discipulis (ut patet Matthei X°, Luce XIV° et Iª, Thymotei VI°); ad hoc enim copiosius sequebantur bona gracie. Confirmatur primo sic: Christus posuita vicarios suos in maxima libertate et privilegio in hoc quod regulam illam iniunxit singulariter suis apostolis, ergo conclusio. Non enim licet negare quin Christus privilegiavit suum collegium, cum dedit eis leges singulares, [p. 177] ut consilia evangelica ad maximam utilitatem sui atque ecclesie, sicut patet ex indole que inde provenerat. Ergo ex diffinicione privilegii in hoc privilegiavit suam ecclesiam. Confirmatur secundo: Ille status est perfectissimus, ut patet in VI° decretalium, cap. Exiit qui seminat, per Nicolaum III., et omne ponere viatorem in statu tam alto est proporcionaliter privilegiare ipsum, ergo conclusio. Si enim dare bona fortune que sunt abiectissima sit privilegiare datarium, multo magis dare sibi bona gracie. Item, quicunque vians exoneratus fuerit sarcina temporalium, ad propinquius, paracius atque laudabilius sequendum hynnulum cervorum salientem in montibus, ut sic est privilegiatus uberius, sed sic fuit de apostolis renunciantibus quoad civilitatem omnibus bonis suis, ergo conclusio. Non enim negabit fidelis quin possessio talis temporalium sit pondus anime, ut docet beatus Gregorius XXXI° Moralium (sicut declaravi XII° cap. huius). Unde apostoli vere reputarunt eis magnum privilegium, quod exonerati fuerunt a ministerio cotidiano in mensis fidelium (ut patet Actorum VI°), ergo multo magis exonerare eos a statu seculari plus abiecto. In hoc enim consistit excellencia status cleri super dominos seculares (ut hic supponitur), non autem in caractere ordinis, cum stat cum illo servitus abiectissima (ut patet de Scarioth), sed in hoc quod deputati sunt ut milites plus strenui ad plus meritorie peragendum bella domini et conquirendum regnum celorum. Nam Matthei V°, 3 dicitur: Beati pauperes spiritu, quoniam ipsorum est regnum celorum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 173.11: The Church has no true privilege except what is founded in Scripture.
- 174.1: Corruptions of the Church.
- 174.27: A case as to privilege.
- 175.21: The Westminster privilege is a false one.
- 176.19: Divestment of all temporal possession would be the greatest privilege the Church could have.
- 177.5: Poverty is the most perfect state, therefore it is a privilege to be placed in it.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 173: *fundatur* [R3]
  - 173: *II°* [R3]
  - 174: *bonum* [R3]
  - 174: *Christus* [R3]
  - 175: *in* [R3]
  - 176: *ecclesie* [R3]
  - 176: *privilegium* (trailing R is the margin letter) [R4]
  - 176: *Iª* [R3]
  - 176: *Christus* [R3]
  - 176: *Christus* [R3]
  - 177: *per* [R3]
  - 177: *ut hic* (one scan token covers two printed words) [R3]
  - 173: *in* [THIN]
  - 174: *preposito loci* (prepo- here, 152d sito loci at top of p.175; main token covers both words) [THIN]
  - 176: *amittere* [THIN]
  - 176: *qui* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 172:
marg. : Martir <T affeccione „ m marg. man. alt. :
passione corporali.
Martirium. 9. A in marg. : humilitas. B in marg. man. alt. : Pri-
matus est fructus humilitatis. 19. tamen; tum in codd. 23. B
in marg. man. alt. : Mcnciendum non est in causa devocionis. 3o. A
in marg. : Crisostomus.
3o. Opus Imperfectum 1. c , pag. CLIII. C.

p. 173:
4. R inter deest. i3- A in marg. : Honor scripturc, quia omnis
vcritas in ca continetur. 16. A in marg. : Secunda conclnsio.
18. A in marg. : Augustinns. ih. B: si quis est, qttis est, quid utile.
28. B: acceptacionis ; A in marg. : Corrclarium.
18. cnp. XI. II. Opp. III, 1, 44. Epistolam ad Vol. vid. Opp.

p. 174:
1. A inmarg.: Conclusio. 4. ecclesic? Fortasse legendum : con-
fundnnt ecclesiam. 8. B: Cum tamen scit. i5. A in marg.:
Conclusio. 20. 21. In codd.: Condicione. 22. A in marg.:
De privilcgiis monastcriorum ct ccclcsiarum. (Relow i52'i witltout mark
of reference.) 27. A in marg. : Casus.
16. Dec. sec. pars, causa XI, q. III, c. LXIIl.

p. 175:
0. A, corrigere vult: ex gravitate contracta. i3. A A,: ca-u et
dcest. 17. In matcria involubili: supcrfluum esse ct e marg. in tex-
tum incidissc videtur. 1S. B: peccatum incidere. 23. A in
marg. : Conclusio. 28. 3o. B: immunitate — clongatum deest.

p. 176:
4. A, corrigcrc vult: criminosus. 4. A in man;: Rcsponsin. S. A
in marg. : Nota. i5. A A,: Non ut. 17. A A,: adicereniur.
iq. A in marg : Tercia conclusio. 22. A in marg. : Rcsponsio. Pau-
pertas clcri.

p. 177:
5. A in marg.: Optimum privilegium ecclesie est paupcrtas cleri.
(Above i53b without mark of referencc.) 7. 8. alto est': alto ut in
codd. n. A in marg. : Sequela Christi. iS. A in marg.: Gregorius.
XII. cap. rectius: III. 22. B: a dccst. 28. B: belli domini et
conquirendo.
7. Lib. V. tit. XII, cap. III. i3. Cant. II, 17. 18. caP.
XIII. Opp. tom. I, 1006. Vide supra pag. 5o — 54.
```

---

## Chunk 08-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-08-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-08-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "178.1–182.5"
divisions: "cap. 8 (heading 'CAP. VIII.' at 157.25); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "978 words; 851 unanimous or majority-real; 105 settled by vote (R2 55, R3a 38, R3b 1, R5a 9, R6a 2); 22 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n215–n219 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 8, part 6: [TITLE]

## ¶1 · 178.1–178.16

> [p. 178] Item, proporcionaliter ut dominus est potencior, prudencior et plus affectus sue ecclesie, tribueret eis privilegia pociora, sed iste condiciones autonomatice reperte sunt in Christo in comparacione ad Cesarem, ergo et privilegiacio proporcionaliter correspondens. Nemo ergo dicet quod Cesar plus privilegiavit ecclesiam quam dominus Jesus Christus, nec licet fingere quin Christus fuit potencior ad donandum eis temporalia, sicut et apostoli potuerunt ea copiosius recepisse, ut patet in vitis eorum. Unde Symon magus voluit dedisse Petro multam pecuniam pro privilegio apostolico (ut patet Act. VIII°), et indubie foret melius quam quantalibet pecunia vel omnia temporalia huius mundi. Nos ergo non erimus magis degeneres dicto Symone, plus appreciantes privilegium Cesaris quam privilegium domini Jesu Christi.

[ENGLISH]

## ¶2 · 178.17–178.23

> [p. 178] Nec valet dicere quod ista privilegia dicuntur equivoce voce et ideo non sunt comparabilia, nam Deus est melior diabolo, bona gracie sunt meliora bonis fortune, et iuxta sanctos melius est seculariter carere temporalibus quam habere. Si ergo ista tam disparia sunt conparabilia in bono analogo, a pari vel maiori bona minus disparia.

[ENGLISH]

## ¶3 · 178.24–178.30

> [p. 178] Et preter hoc aliqua temporalia donavit Deus suis que quoad quantitatem et modum habendi sunt comparabilia dono Cesaris vel alterius domini secularis; in hoc ergo quod dicta privilegia dicuntur tam equivoce, oportet concedere quod unum infinitum excedit reliquum in perfeccione, sicut spiritus excedit naturam corpoream.

[ENGLISH]

## ¶4 · 178.31–182.5

> [p. 178] Item, iuxta hic dicta in correlariis descripcionis privilegii, nemo potest dare privilegium, nisi Christus principaliter] illud dederit, et cum non decet dominum dare per servum donum perfeccius quam ipse dat [p. 179] singulariter per se ipsum, sequitur quod privilegium datum appropriate per Christum excedit privilegium quod ipse dedit per Constantinum, potissime cum videtur privilegia illa fuisse contraria. Ergo uno existente bono aliud saperet in parte maliciam venenosam, et per consequens, non foret privilegium pocius quam fuisset, quod filiorum Zebedei unus sedisset ad dexteram Christi et alius ad sinistram in regno temporali. Confirmatur ex sepe dictis, privilegium est filium patrisfamilias domus poni in loco digniori ad premium et in loco tuciori ad evadendum periculum, nec fas est dubitare quin Christus vocavit apostolos suos ad talem locum, in quo eciam secundum quandam prerogativam fuit Baptista, dicente Christo Matthei XI°, 1 i: Inter natos mulierum qui ceciderant per peccatum non surrexit maior Johanne Baptista. Cum ergo hec diffinicio Christi necessario sit vera, patet quod nec Petrus nec alius citra Christum fuit maior Baptista quoad Deum, cuius maioritas non attenditur penes possessionem secularem, cum Baptista fuit citra Christum pauperrimus, sed penes gradum evangelice paupertatis que consistit in vera humiliacione et in meritoria penalitate et in ecclesie edificacione. In hoc ergo fuit Baptista positus securius ad cavendum periculum et alcius ad querendum premium. Cum ergo quicunque status sit alcior quem Deus plus acceptat, sequitur quod status in quo Christus posuit apostolos et docuit ecclesiam sit status alcior statu secularis glorie in quo positi sunt Christi vicarii et dotati per Cesarem. Nec valet dicere quod ille status fuit tunc perfeccior, nunc autem status iste est perfeccior, tum quia fructus status ostendit oppositum de intricacione et detrimento ecclesie, tum eciam quia racio fidei scripture contradicit, [p. 180] nam lex consiliorum est perpetua, non habens contrarium, cum ponit hominem in statu, statui utriusque innocencie propinquiori, statum autem magnitudinis secularis oportet deserere propter eius repugnanciam statui beatitudinis. Quomodo ergo non est al statu inperfeccior, cum respicit magnitudinem temporalem quam oportet deserere, alius autem magnitudinem virtutis quam oportet semper habere? Ex istis colligitur quod domini temporales possent maxime zelando pro privilegiis ecclesie exonerare clerum suum ab occupacione temporalium que sunt preter necessaria ad faciendum opus evangelicum; nam possent sic faciendo reducere ecclesiam cleri ad perfecciorem statum ex dictis, sed cum impossibile sit hominem posse facere bonum de genere, nisi posset facere illud bene, sequitur quod domini temporales possent facere illud bene. Absit, inquam, credere quod status in quoa Cesar posuit clerum non posset solvi licite propter habitudinem sacerdotum Christi ad globum temporalium. Et cum status in quo Christus posuit clerum suum dissolvi posset licite propter inperfeccionem habitudinis vite eorum ad paupertatem evangelicam et alia carismata in quibus Christus dotavit ecclesiam, nonne foret suspectum verbum, accusans proprietarios de: affeccione inordinata temporalibus, dicendo quod lex Dei et eius consilium sunt temporalia sub dispensacione cadencia, sed non ordinacio Cesaris quoad donacionem temporalium? Numquid credimus quod excommunicacio vel malediccionisinterpretacio plus ligat dissolventem ordinacionem dominorum temporalium, quam excommunicacio Christi, Johannis et Pauli ligat dissolventem Christi consilium? Nonne dicit Paulus Galat. 1°, 9: Si quis aliud evangelizaverit preter illud quod evangelizatum est, anathema sit, et cum ipse [p. 181] instruxit coapostolum Thymoteum Iª Thymotei VI°, 8: Habentes ergo alimenta et quibus tegamur dhiis contenti simus? Numquid est contrarium isti contencioni aspirari inordinate ad habendum perpetuo et indissolubiliter quantumlibet seculariter dominium? V Nonne dicit beatus Gregorius (ut recitavi superius, III° cap.) quod labor querendi et defendendi temporalia et dolor amittendi eadem, si superat laborem et dolorem circa bona spiritualia quesita vel perdita, indicat terrenorum affeccionem inordinate in animo presidere Nonne beatus Augustinus in libro De Vera Religione, XCII° cap., dicit idem? Ubi postquam ostenderat quid est adherere Deo et quibus profluit affluencia temporalium etc, respondet: Cum, inquit, mutabilium bonorum adest copia, non eis confidit, sed cum subtrahuntur, agnoscit utrum eum non ceperint, quia plerumque cum assunt nobis, putamus quod non ea diligimus, sed cum abesse ceperint, invenimus qui simus; hoc enim sine amore nostro aderat quod sine dolore discedit. Si ergo clerus aliquis sit mundo deditus quod plus dolet pro amissione temporalium quam virtutis, plus insistit circa adquisicionem vel defensionem eorum quam boni spiritualis, ut sic inhabilitat se ad habendum hec temporalia et per consequens dignificat se ut perdat illa. Nec est ille cui hec sunt donata qui in isto animo finaliter perseverat, quia est membrum diaboli et non pars ecclesie (ut patet in solutione VIⁱ argumenti de VI° cap. huius). Nam vera religio stat in recta dileccione beatorum, ut in libro De Vera [p. 182] Religione XCIII.: Et hec est perfecta iusticia qua pocius pociora et minus minora diligimus. Vana ergo est religio facientis oppositum, privilegium ciresorum iniectorum puris certantibus est medicinaliter removendum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 178.1: Christ, who gives poverty, is far greater than Caesar, who gives riches.
- 178.31: All privileges come from Christ directly or indirectly.
- 179.1: Those coming directly are the greatest.
- 179.15: Baptist, than whom none was greater, was very poor.
- 179.31: It is futile to say that the state of poverty was more perfect, but is so no longer.
- 180.1: Poverty is nearer to the state of innocence.
- 180.10: Hence rulers may relieve the clergy of useless wealth.
- 181.6: Opinions of Gregory
- 181.11: and Augustine.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 178: *∅* (the boxed item is the folio asterisk (153c); no word there) [DEL]
  - 178: *principaliter* (prin-/cipaliter; main token princjpa spans the hyphen) [THIN]
  - 178: *∅* (tcr is the rest of cipaliter, already in pos 224) [THIN]
  - 178: *illud* [THIN]
  - 179: *singulariter* (153c folio mark, S margin letter) [R3]
  - 179: *1* (leaf zoom: print has XI°, 11 (two old-style 1s); main splits them, this token is the first, pos 106 the second) [R3]
  - 179: *perfeccior* [R3]
  - 181: *Iª* (153d folio mark; print Iª Thymotei) [R3]
  - 181: *Gregorius* (g with lower bowl, not c) [R4]
  - 181: *III°* [R4]
  - 181: *assunt* (print spelling) [NW]
  - 178: *proporcionaliter* [THIN]
  - 178: *est* [THIN]
  - 178: *potencior* [THIN]
  - 178: *prudencior* [THIN]
  - 178: *sue* [THIN]
  - 178: *ecclesie* [THIN]
  - 178: *tribueret* [THIN]
  - 179: *eciam* [R4]
  - 179: *scripture* [THIN]
  - 182: *Religione* [THIN]
  - 182: *pociora* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 178:
3. P. : antonomastice. 17. A in marg. : Responsio. 23. sc.
sunt comparabilia. 3i. A in marg. : Nota hoc argumentum.

p. 179:
20.21. A A,: posscssioncm pcncs dcest. 3l. A in marg.: Rc-
sponsin. 33. A in marg.: Corrclarium. Ablacio temporalium nota supra.

p. 180:
14. Duo verba: sicut patet (sicut patct cx dictis) huic loco dcesse
videtltur. 16. A A,: possttnt tacere. 32. B: consilium Chrisli.

p. 181:
(i. A in marg. : Gregorius; XII. cap. recte. III. 7. Codd. 12° cap.
Correxi. n. A in marg. Amor temporalium occultus quomodo indi-
catur. 12. A in marg. : Augustinus. Pomny, giossa tschechica :
Memento. 12. A: ostenderit. i5. A in marg. : Nota. In codd.:
non cis conlicit. Corr. cx Aug. I. c. 16. In codd. : separent corr.
e textu Augustini. 25. A in marg. : Conclusio.
6. V. supra pag. 52 — 54. 12. Aug. cap. XCIl, libri De
Vera Relig. Opp. I, pag. 781. 28. V. supra pag. 1 36 — 1 38.

p. 182:
1. B: religione quoque. in codd. : est hec; corr. c tcxtu Aug.
6. Cap. IX; A: Tit. vacat in A; solum in marg. ib. Prima obicccio. A:
sic deest: B: primo deest. it. A in marg.: Responsio. 19. B:
attcndat. ii. A: habuocia. 3i. B: quibus habet.
```
