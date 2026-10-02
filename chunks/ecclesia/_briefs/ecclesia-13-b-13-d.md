# Translation brief: ecclesia 13-b–13-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-13-b.md chunks/ecclesia/wyc-ecclesia-13-c.md chunks/ecclesia/wyc-ecclesia-13-d.md` once and fix what it reports.
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

## Glossary (the 172 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |
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
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| ditare | to enrich | Kept apart from *dotare*, endow. Ruled 2026-09-28 (coordinator, delegated) (21 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| dotacio | endowment | |
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
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| privilegiandus | the one to be privileged | Ruled 2026-10-02 (*Eccl.* 12). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Ruled 2026-10-02 (*Eccl.* 13). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| propositio copulativa / disiunctiva | conjunction / disjunction | Not "copulative proposition" (T. p. 365). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| philargiria | love of money | 1 Tim. 6:10 *radix omnium malorum cupiditas*. Ruled 2026-10-02. |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten | Provisional; the sense (lighten rents / refine) is doubtful; C note (*Dial.* 67.19, 68.11). Ruled 2026-09-28 (coordinator, delegated). |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| irreligiositas | irreligion | Ruled 2026-10-02. |

---

## Chunk 13-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-13-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-13-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "278.33–282.34"
divisions: "cap. 13 (heading 'CAP. XIII.' at 274.25); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "929 words; 842 unanimous or majority-real; 74 settled by vote (R2 47, R3a 21, R3b 1, R5a 4, R6a 1); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n315–n319 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 13, part 2: [TITLE]

## ¶1 · 278.33–279.27

> [p. 278] Religiosior ergo foret concessio expressa condicione quod persone sint habiles et quod Deo sit placitum; [p. 279] quam condicionem licet oportet intelligere, tamen illa expressa foret contencionum plurium sedativa et disposicionis plus vigilis causativa et sic racione humilitatis foret magis autentica et racione declinacionis a ritu gentili ad religionem Christi foret plus meritoria et racione pluris adiutorii plus secura. Et ita videtur presumpcio quod quis obliget heredes suos simpliciter ad continuacionem talis elemosine, cum non subiacet potestati sue dignificare quoscunque taleselemosinarios, nec potest obligare se ipsum vel alium ad premiandum indignos, cum heres plus obligatur veritati a qua per se capit hereditatem, quam patri carnali a quo capit solum per accidens. Et hec est racio quare catholice dicitur regem Anglie semper esse infra etatem, cum debet corrigere errores tam sui quam progenitorum suorum, sive ex ignorancia sive ex inadvertencia deceptus fuerit; aliter enim attemptaret defendere iniusticias contra Deum. Ideo absit nos inponere regi et regno tantam demenciam ut inveteratus dierum malorum defenderet antiquum errorem tractum in consuetudinem, cum secundum decretum, allegatum XI° cap°, error cui non resistitur approbatur. Et patet consideranti attencius quomodo omnis elemosina humana vocata perpetua est realiter ex lege Dei invincibili temporalis, cum oportet omnino condicionem quam Deus apponit subintelligi, quamdiu ditarius manserit dignus participare elemosina quoad Deum.

[ENGLISH]

## ¶2 · 279.28–280.10

> [p. 279] Unde talis attencio et expressio hominis elemosinantis ex maiori humiliacione, ex maiori Deo confirmacione, et maiori errorum exclusione magis disponeret ad perpetuacionem elemosine per Christum quam elemosina humana irreligiose vocata perpetua. [p. 280] Nam perpetuare elemosinas est Christo proprium, eo quod est dominus, simpliciter assistens omni tempori, potens iustificare elemosinarium, a qua iustificacione (iuxta dicta proximo capitulo) dependet humana donacio; et sic est de successione hereditaria de qua minus videtur. Deo enim est proprium heredes in perpetuitate successionis hereditarie limitare. Unde creditur quod multi fundantes elemosinas nominetenus perpetuas in penam sue superbie a perpetuitate generis hereditarie defecerunt.

[ENGLISH]

## ¶3 · 280.11–280.16

> [p. 280] In talibus ergo elemosinis unus princeps concedit pro suo tempore subintellecta supradicta condicione et imprecatur suum heredem sic facere, et ex meritoriis donis multorum sibi succedencium cum graciosa disposicione materie facit Deus unam elemosinam perpetuam, si sibi sit placitum.

[ENGLISH]

## ¶4 · 280.17–280.33

> [p. 280] Unde hic instatur sophistice quod temporalis dominus meritorie facit elemosinam perpetuam, cum meritorie faciat partem eius. Sed iste obiectus non vadit contra sensum expositum, ymmo si procedit de faccione elemosine- perpetue secundum partem, eque probaret quod una vidua paupercula plus faceret in casu elemosinam talem perpetuam, posito quod plus mereatur ut Deus elemosinam utrimque perficiat; nam 1° Corinthiorum III°, 6, scribitur: Ego plantavi, Apollo rigavit, sed Deus incrementum dedit. not Unde patet consideranti subtiliter quod nullus heres procedens post progenitorem dotantem ecclesiam tenetur approbare fundatam elemosinam nisi ex libera voluntate. Patet primo sic: Non tenetur facere aliquodl opus meritorium nisi ex libera voluntate, non tenetur sic approbare nisi secundum racionem operis meritorii, ergo non tenetur sic approbare nisi ex libera voluntate.

[ENGLISH]

## ¶5 · 281.1–281.28

> [p. 281] hoc est notum intelligentibus textum Apostoli Philipp. IIIo, 3, et Gal. VI°, 14°, dicentis: Michi autem absit gloriari nisi in cruce domini Jesu Christi. Item, ex precepto Dei et eius successione hereditaria filii adoptivi non tenetur heres continuare aliquod bonum opus nisi ex libera voluntate; sed Deus, pater heredis plus obligat quam pater suus carnalis, ergo multo magis ex obligacione patris carnalis non tenetur sic facere nisi ex libera voluntate. Deus enim posuit hominem in tanta libertate, quod non potest sibi quicquam absolute precipere nisi meritorium, et per consequens adiecta condicione, ut libere illud perficiat. Unde Augustinus super Psalmum CXLVIIIᵘᵐ: In tuo, inquit, arbitrio Deus te esse voluit, cui pares locum, Deo aut diabolo, cum paraveris, qui possidebit ipse imperabit. Sed absit ut aliquis reportet me quod dem occasionem dominis temporalibus ad spoliandum sanctam ecclesiam vel ad continuandum elemosinas quas progenitores eorum inceperant, cum ex conclusione sequatur formaliter quod tenentur elemosinas tales perficere. Scit enim logicus quod si non sic elemosinare nisi libere tunc tenentur, quis queso urgeret regem Anglie coaccione civili continuare elemosinas patris sui? Non rex preteritus, tum quia par in parem non habet imperium, tum eciam quia ipsis in regno incompossibilibus est plenum ius ad regem posterum derivatum, nec imperatori pertinet, cum regnum nostrum non sit imperio sic subiugatum.

[ENGLISH]

## ¶6 · 281.29–282.34

> [p. 281] Ex quibus sequitur quod non pertinet ad papam propter obligacionem regis et regni antiquis temporibus [p. 282] pensionem vel elemosinam annualem ab istis requirere, nam in lege Christi talis perpetuus redditus non habetur nec ex lege imperiali post dotacionem factam a cesare, quia integrum imperium non habet ius, unde liceat sibi exaccionem huiusmodi vendicare. Requireretur ergo ut papa in hoc humilis elemosinarius regis petat ratificacionem talis elemosine, cum omnia que habet in Anglia tenet de rege, tum quia dominium regni nostri non est subiectum imperio, et per consequens non parti imperii decise ad Romanum pontificem, tum eciam quia sic regnum nostrum foret per mortificacionem temporalium nimium diminutum et per consequens virtute brevis regii; ad quod dampnum rex statim revocaret quod tam improvide est concessum. is Rex vero ex vocali promissione, ex scripti personali obligacione, vel ex paternali affeccione potest esse obligacior ad progenitorum suorum elemosinas gratis continuandum, sed potissime racione obligacionis qua Christo tenetur sub obtentu beatitudinis impertiri opera misericordie membris suis (ut patet Matthei XX V°); et cum maius opus misericordie sit fraterna coreccio, patet quod heredes sunt secundum leges Dei et hominum ad ipsam amplius obligati. Unde (ut dixi superius) plus faceret in casu ad continuacionem elemosine progenitorum, auferendo ipsam a discolis et convertendo eam in alios pios usus quam quantumlibet multiplicando collacionem temporalium minus provide. Et ex talibus operibus misericordie sibi succedentibus eciam diversis in genere fit unum opus misericordie successivum, cum tota ecclesia a principio mundi usque ad novissimum electum habet unum opus misericordie secundum quod ecclesia plene complacet sponso suo.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 279.1: Such conditions must be always understood, but would be better expressed.
- 279.28: Temporary alms would probably endure longer than those called perpetual.
- 280.11: The giver's example would be followed and the succession of gifts kept up.
- 280.27: An heir is not bound to approve of his ancestor's gifts.
- 281.9: God ordains all good works to be done of free will.
- 281.16: (I must not be supposed to mean that lords should cease their payments to the Church.)
- 282.1: The Pope has no power to enforce payments from the King,
- 282.16: but the King is bound to continue his ancestor's alms,
- 282.26: though he may vary their application.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 279: *confirmacione* (hyphenated confir-/macione; main token holds whole word) [R4]
  - 280: *facere* (hooked ascender = f) [R3]
  - 280: *III°* [R4]
  - 280: *Deus* [R3]
  - 281: *14°* [R3]
  - 281: *in* [R3]
  - 281: *meritorium* [R3]
  - 282: *Christi* [R3]
  - 282: *obligacione* [R4]
  - 282: *paternali* [NW]
  - 279: *quam* (alinea C and 168a folio mark glued) [THIN]
  - 280: *perpetuare* [THIN]
  - 282: *pensionem* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 278:
4. B: extranie. 9. B: fuisset — titulo deest. 21. Aj corr. :
teneret. 21. B: servicio. 22. Ainmarg.: racio. 24. A At:
subintellexit. 25. 26. A A, : durare per tantam.

p. 279:
b. A in marg. : Conclusio. i3. A Aj: Et hec racio; A in marg.:
Conclusio. 28. 29. B: elemosinant.
21. Dec. I pars, dist. LXXXIII, c. III. Vide supra pag. 235.

p. 280:
1. Ainmarg.: Conclusio. 7. Ainmarg.: Conclusio. i3. B:
ct interpretatur suum. 14. B: graciose. 17. A B in marg. :
Instancia. 21. B: cx faccionc. 27. A in marg.: Conclusio.
3i. B: nisi — meritorii deest.

p. 281:
j. Philipp; In codd. sequitur lacuna. Addidi: III, '}■ 16. A in
marg. : Nota solucionem obiectus. 18. discontinuandum (?). 21. AA,:
quod si non tenentur. 22. 23. B: urget. A in marg. : Non tcnetur
filius continuare dotacionem elemosine patris sui. 28. B: non sit
imperatori. 29. A in marg. : Conclusio.
i3. Opp. tom. IV, p. II, pag. 1671

p. 282:
7. B : artificacionem. Ai n marg. : Conclusio. 12. i3. A A, : dirimitum.
i3. A A,: regie; B: regei; recte: regii. 16. A in marg. : Conclusio.
```

---

## Chunk 13-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-13-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-13-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "283.1–287.20"
divisions: "cap. 13 (heading 'CAP. XIII.' at 274.25); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1090 words; 948 unanimous or majority-real; 128 settled by vote (R2 69, R3a 48, R3b 1, R5a 7, R6a 3); 14 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n320–n324 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 13, part 3: [TITLE]

## ¶1 · 283.1–283.10

> [p. 283] Contra dicta obicitur primo per hoc quod in veteri testamento erant multe tales elemosine, religiones et ritus perpetui approbati, cum ergo tante auctoritatis sit vetus testamentum ut novum, sequitur quod licitum est fundare tales elemosinas perpetuas auctoritate veteris testamenti. Nam ex hinc sumitur solucio decimarum, ut dictum est libro III° cap.... ex testimonio Henrici de Gandano et sancti Thome; et assumptum patet Levitici VI° et VII° Exodi XXVII° et sepe alibi in scriptura.

[ENGLISH]

## ¶2 · 283.11–284.21

> [p. 283] Hic patet quod obieccio ista non impugnat predicta, cum conclusio sit concedenda. Sed utinam sic arguentes attenderent ad sufficientem similitudinem utrobique, primo quomodo in veteri testamento ordinata est talis perpetuitas, singulariter a Deo et non ab homine. Unde libri legales et prophetales sic inchoant talia privilegia perpetua: Hec dicit dominus; et tunc cum auctor utriusque testamenti expressit voluntatem suam sufficienter in evangelio, non usurparent superaddere ordinacionem que videtur ordinacioni Dei contraria ipso domino inconsulto. Considerarent secundo quomodo omnes dicte elemosine vocate perpetue erant solum periodice, sicut patet in materia de cessacione legalium et persone privilegiate racione delicti a domino privilegiante proporcionaliter ammovente, ut patet de Datan et Abiron Numeri XVI°, de Hely et suis filiis 1° Regum II° et IV° capitulis, et de sacerdotibus, scribis et phariseis tempore Christi, qui omnes proporcionaliter ad abusum privilegii sunt puniti. Quomodo ergo vendicaremus colorate privilegium ab homine preter Deum, et super hoc exempcionem a tutela et regulacione illius privilegii ab illo [p. 284] qui privilegiat citra Deum? Locus enim a similitudine ex lege veteri hoc non petit; stet homo in limitibus privilegii unius persone et tunc limitari convenit regimen plenum illius privilegii ad illam personam singulariter concedentem. of Tercio notaret sic arguens quomodo clerus veteris testamenti, quando vixit carnaliter, limitatus est per Deum sine solicitudine circa proventus vel redditus adquisitos vel datos humanitus, quid de oblacionibus, primiciis vel loco ad inhabitandum percipiet, quanto magis clerus spiritualis Christi pauperis et egeni excluderet se striccius a mundialibus de alimentis et tegumentis secundum regulam Apostoli 1° Tim. VI° contentatus? Nam Ezechiel. XLIV°, 28— 30, sic scribitur: Non erit autem sacerdotibus hereditas, ego hereditas eorum. Et possessiones non dabitis eis in Israel, ego enim possessio eorum. Victimam et pro peccato et pro delicto ipsi comedent et omne votum in Israel ipsorum erit. Et primitiva omnium pecorum primogenitorum et omnia libamenta ex omnibus que offerunt sacerdotum erunt.

[ENGLISH]

## ¶3 · 284.22–287.20

> [p. 284] Habuerunt autem loca pro inhabitacione et alendis pecoribus (ut patet Josue XXI° et ultimo). Si ergo clerus Aaronita tam carnalis, tam laboriose solicitus circa ceremonias legis tam limitate et stricte habuit temporalia, quanto magis clerus Christi qui exemplo conversacionis et verbo predicacionis docuit mundum relinquere et conversando in celestibus ad eorum annichilationem laicos edocere? Et hec racio legis Dei, Deuteronomii XVIII°, 1, quare precipit populo sub hiis verbis: Non habebunt sacerdotes et Levite et omnes qui de eadem tribu sunt partem et hereditatem cum reliquo populo Israel, quia sacrificia domini et oblaciones eius [p. 285] comedent et nichil aliud accipient de possessione fratrum suorum: Dominus enim ipse est hereditas eorum, sicut locutus est illis. Et sic intelligo scripturam sacram Numeri XVIII°, 20, cum dicitur: Dixitque dominus ad Aaron: In terra eorum nichil possidebitis nec habebitis partem inter eos, ego pars et hereditas tua. Haberent autem sacerdotes de optimis vescibilibus sine sollicitudine (ut patet ex Exodi XIX°, Levitici 1° et IV° et capitulis sequentibus). Ex istis potest colligi conclusio quod moderna cleri dotacio non est fundabilis in altero testamento. Secundo principaliter obicitur per hoc quod dare aliquantam elemosinam pro aliquanto tempore est cum paribus alicuius meriti; dare cum paribus tantam vel maiorem elemosinam per tempus diucius foret meriti amplioris, et per consequens pro tempore legis gracie, quando debet esse superhabundans caritas, debet dari elemosina largissima quoad quantitatem muneris, quoad libertatem donacionis et quoad diuturnitatem temporis. Sed cui donarent laici nisi clero Christi a quo recipiunt elemosinas ampliores? Ergo sancti reges et prelati, leges ecclesie et ostensiones miraculi docent cum racione de maioritate meriti quod talis dotacio ecclesie sit meritoria utrobique. Quis, inquam, dubitat quin, si Petrus meritorie dederit elemosinam et, servato merito, superaddiderit quomodolibet elemosinam ampliorem, quin eciam cresceret meritum aggregatum? Hic dicitur concedendo primam conclusionem: eo quod apostoli et alii cariores Christi discipuli dederunt omnia sua temporalia, sequendo Christum in evangelica paupertate, ita quod nec dacio nec recepcio est [p. 286] per se culpabilis sed carencia boni modi, notandum tamen quod maioritas meriti dantis elemosinam nec absolute attenditur penes quantitatem aut valorem dati nec penes quantitatem temporis pro quo datur, quia iuxta diffinicionem Christi, Luce XXI°, 2, Mulier paupercula mittendo quadrantem in gazophilacium plus omnibus misit. Ideo attendendum est ad caritatem a qua procedit elemosinacio corporalis. Et patet quodl modus elemosinandi respicit discrecionem qua elemosinans relevet indigentem. Ideo evangelium non precipit ut relinquens bona sua det Christi apostolis sed pauperibus ut cecis, claudis atque debilibus. Secundo requirit rectitudo modi elemosine, ut tribuens observet servilem humiliacionem qua sciat se esse nudum ministrum Dei cui prestita sunt bona fortune, ut humiliter ac caritative distribuat. Et tercio requirit modus rectus elemosinandi ut elemosinans observet puram et simplicem intencionem non appetendo mundi gloriam. Et ideo docet Christus Matthei VI°, 2, 3, quod faciendo elemosinam non canes ante te tuba sicut ypocrite, sed nesciat sinistra, hoc est, intencio expectans retribucionem temporalem, quid faciat dextra; pars intencionis qua recte et pure spiritualis retribucio perpetua pro alio seculo expectatur et secundum quod ista plus adequantur cum maiori caritate est maior elemosina in donante. Ex quo patet cum veritate facti quod elemosine vocate perpetue in maiori parte vel semper habent minus de racione elemosine quam dande elemosine temporales. Nam taliter elemosinans deficit communiter in discrecione dando magis egentibus, deficit secundo in humiliacione credendo quod data sunt sua ad ordinandum quomodocunque voluerit sine superiori domino ipsum ut nudum servum suum et organum [p. 287] excitante, et demum communiter in elemosina tam corporali quam spirituali surrepit affeccio vane glorie vel boni utilis temporalis; et (si non fallor) oculus cesaris quodammodo infectus fuerat in hiis tribus. Quis rogo sciret docere quod cesar vel alius dominus secularis in fundando tam publice perpetuas elemosinas non intendit vane gloriam solempnitatis nominis sui et sui generis longis temporibus duraturam? Quod si illud preponderat intencioni dextere, faciendo elemosinas de alieno, peccat mortaliter. Et patet ad formam argumenti concedendo conclusionem et sequelam: Nam maxima elemosina in via est ut quis relinquat penitus civilem possessionem in mundo et ponat vitam presentem pro honore Dei et utilitate ecclesie dicente Christo Johannis XV, i: Maiorem caritatem nemo habet quam ut animam suam ponat quis pro amicis suis, talis ei dat omnia bona sua fortune et omnia bona sua naturalia, et cum iusti sunt omnia, patet quod in tali dacione fundatur elemosina largissima; et patet conclusio.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 283.1: It is objected that there were perpetual foundation under the O. T.
- 283.11: Answer: These were ordained by God,
- 283.21: who could and did withdraw them;
- 283.28: and do not authorise human foundations exempt from regulation.
- 284.6: The clergy of the O. T. was limited as to what it might receive.
- 284.22: Much more should the clergy of Christ set an example of unworldliness.
- 285.13: 2. It is objected a) that the more the alms, the greater the charity,
- 285.19: b) that alms can be given to none better than to the clergy.
- 285.30: Answer: a) True, if the alms are rightly directed;
- 286.2: but merit does not depend wholly on the amount given but on the spirit of the giver.
- 286.13: Alms must be given
- 286.15: 1. to the poor,
- 286.16: 2. as a service to God,
- 286.18: 3. without thought of worldly reward.
- 286.29: The founder of perpetual alms usually fails in all three points.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 283: *auctoritatis* [NW]
  - 283: *III°* [R4]
  - 283: *utrobique* (utro-/bique; main token holds whole word (a = alinea letter)) [R4]
  - 283: *II°* [R3]
  - 283: *puniti* (30 is the line number) [R4]
  - 284: *solicitudine* [R3]
  - 284: *Christi* [R3]
  - 284: *1* (x-height old-style 1, not capital I) [R3]
  - 285: *est* [R3]
  - 285: *Dixitque* (Dixit-/que; main token holds whole word) [R3]
  - 285: *Christi* [R3]
  - 286: *∅* ('of' is the English side-note; main already has de at 202) [INS?]
  - 287: *demum* [R3]
  - 283: *XVI°,* [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 283:
[. Ainmarg.: Contra. Prima obieccio. ~. Cap. In codd. sequitur
lacuna. n. Ainmarg. : Responsio. n. A: inpungnat. 21, A
in marg. : Conclusio. 27. B: cum suis filiis.
8. Henricus de Gandano, Vide inf. pag. 317.

p. 284:
ji. A A,: unius — privilegii deest. (3. A in marg.: In vcteri
testamento erant multc elemosine, religiones et ritus pcrpetui approhati.
Clerus moderate debet habere temporalia (Above i68d without mark of
refercnce). 14. A in marg. : Racio.

p. 285:
3. B: fratruum. 11. A in marg. : Conclusio. i3. A in marg.:
Contra. Secunda obieccio. \.\. A in marg. : Nesciat sinistra quid
faciat dextra. 3o. A in marg. : Responsio.

p. 286:
i. B: carencicia. A in marg. : Conclusio. Nota rectum modum elemo-
sinandi (Bclow 169» without mark of reference). 8. A in marg.:
Conclusio. 19. Codd. Matth. V. 34. A A,: ut organum.

p. 287:
5. A in marg.: Conclusio. 11. A in marg.i Ad argumentum.
11. 12. A Ax: concedo conclusionem.
```

---

## Chunk 13-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-13-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-13-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "287.21–290.19"
divisions: "cap. 13 (heading 'CAP. XIII.' at 274.25); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "675 words; 614 unanimous or majority-real; 56 settled by vote (R2 30, R3a 19, R3b 2, R5a 2, R6a 3); 5 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n324–n327 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 13, part 4: [TITLE]

## ¶1 · 287.21–288.8

> [p. 287] Quoad quantitatem muneris, quoad libertatem donacionis et quoad diuturnitatem temporis patet quod viventes exproprietarie religione perpetua faciunt elemosinas largissimas et ordinatissimas, quia primo miserentur anime sue placentes Deo, et secundo facientes spiritualia opera misericordie toti mundo ex vi communionis sanctorum plus ad honorem Dei prosunt ecclesie quam secularis accumulans quotlibet temporalia domui private secundum religionem preter evangelicam adinvente. Unde absit fidelem credere quod proporcionaliter ad quantitatem molis vel valoris donati in foro seculi attenditur quantitas elemosine donatoris, cum infinitum maiorem elemosinam contingit quantumlibet minus valere in foro seculi. [p. 288] Tunc enim apostoli fecissent elemosinas nimis parcas, et mundiales extollerentur supra precipuos religiosos in merito, dareturque secularibus occasio ad inordinate querendum et ad inordinate retinendum bona fortune, ut in fine condendo grande testamentum dent grandem elemosinam abbathie vel clero, quia certum est quod proporcionaliter ad elemosinam vel opus misericordie viatoris est beatificandus in patria.

[ENGLISH]

## ¶2 · 288.9–289.15

> [p. 288] Unde logici cognoscunt quomodo data elemosina est alia maior; que alia est priori quantumlibet maior elemosina. Unde contingit quod potus aque frigide sit maior elemosina danti ex simpliciori oculo et maiori fervore caritatis, quam fuit dotacio qua Constantinus dotavit ecclesiam, vel elemosina qua rex terrenus fundavit grandissimam abbathiam. Nam nisi spirituale opus misericordie prevaleat corporali, stante isto cursu ecclesie, domini seculares forent nimis exaltati in celo et viri apostolici nimis mediocriter premiati. to Et patet ad questionem qua queritur, cui seculares darent elemosinas nisi clero; nam illis tenentur dare prudenter de quanto sustinerent eorum privilegia data a Christo, et continuarent eorum disposicionem ad rependendum elemosinas spirituales. Alias autem elemosinas darent corporaliter magis egentibus. Unde si ex ceca pietate et falsa misericordia nimis onerant clerum cum possessione civili, contingit eos ex hinc incidere m excommunicacionem et heresim racione ablacionis primevi privilegii concessi a Christo suis discipulis, ut meminit Canon XXIIª d. Omnes. Et ita concedo quod dotacio ecclesie fuit altrinsecus meritoria, sed dotacio ac status in quo Christus ipsam [p. 289] instituit fuit perfeccior. Unde verisimile est quod multi ex defectu serpentine prudencie in ista elemosina ecclesie altrinsecus sunt dampnati; diuturnior autem elemosina est breviori prestancior, sed nemo dicit quod diuturnitas elemosine penes formam diuturnitatis expresse in cartis regulariter attendatur, cum stat elemosinam horalem de correpcione fraterna manere perpetuo in fructu, ubi elemosina cartalis sub nomine perpetuitatis expressa extinguitur infra annum tam in substancia elemosine quam in fructu. Sic ergo dans prudenter, ferventer et paulative elemosinas continue plus crescit et superaddit elemosinas quam ceteris paribus faceret sub signo elemosine perpetue dando simul, quia fervor caritatis et vigil custodia rectificande elemosine forent meritorius conservata.

[ENGLISH]

## ¶3 · 289.16–289.22

> [p. 289] Tercio principaliter arguitur per hoc quod elemosina debet sic dari, ut generi secularium elemosinanti accresceret maior utilitas et generi cleri elemosinandi accresceret plus excitativa securitas ad vigilanter perficiendum officium clericale; sed quis dubitat quin hoc contingeret sub forma dotacionis perpetue? Ergo illa est dotacione temporali prestancior.

[ENGLISH]

## ¶4 · 289.23–290.10

> [p. 289] Hic dicitur quod verum assumitur, unde pro minori quilibet christianus debet credere quod in temporalibus dotacio temporalis excluso signo perpetuitatis humane elemosine foret undiquaque perfeccior: et patet defectus consequencie. Unde pro declaracione prime partis maioris assumpte patet eius veritas ex dictis, cum talis elemosinacio foret factis Christi et apostolorum conformior, et per consequens elemosinanti utilior. Unde Act. III° legitur quomodo possessores agrorum vendebant et ponebant ante pedes apostolorum, non ut hereditarie vel perpetue possiderent, sed ut divideretur singulis prout cuique opus [p. 290] erat. Nec solum servata est illa forma elemosinandi in Judea, ubi Deus scivit apostolos non perpetuo permansuros, sed in Asia, in India, in Ethiopia et ubicunque terrarum christiani conversi sunt et presbiteri constituti; sed indubie illi ex maiori fervore caritatis, ex maiori prudencia ac simplicitate quam nostri succedentes qui sub forma dotacionis perpetue dabant sua et magis quieta, ac in pace Christi plus firmata est ecclesia illa primitiva conversa quam fuit nostra ecclesia cesarea sic dotata.

[ENGLISH]

## ¶5 · 290.11–290.19

> [p. 290] Unde illud magnum scisma factum per Sergium L monachum sicut et illud scisma quod hodie pullulat per duos pseudomonachos cum aliis particularibus divisionibus in ecclesia causata sunt ex insaciabili affeccione cleri ad temporalia, quam nisi occasione dotacionis cesaree verisimiliter non haberent. Si enim non esset ista dotacio, non sic contenderent pro primatu, cum circa preeminenciam servilis humilitatis non fit contencio.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 287.21: Those who live without property give alms best.
- 287.29: The worth of alms does not depend on their amount.
- 288.4: or the miser would be justified by a large bequest.
- 288.20: b) We ought to give to the clergy what enables them to minister spiritually;
- 288.27: all beyond should be given to the poor.
- 289.16: 3. Objection: Perpetual alms profit most, because they make the clergy secure to perform their duty.
- 289.23: Answer: This is a mere assumption, temporary alms would enable them much better to do their duty.
- 290.1: In the primitive Church there were no foundations, but immediate distribution.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 288: *seculares* (K is margin letter) [R4]
  - 288: *XXIIª* [R4]
  - 289: *christianus* [R3]
  - 289: *temporalibus* (tempora-/libus; main token holds whole word (25 line number)) [R4]
  - 289: *perfeccior* [R3]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 287:
5. A in marg.: Conclusio. 11. A in marg.i Ad argumentum.
11. 12. A Ax: concedo conclusionem.

p. 288:
7. A in marg. ; Conclusio. io. B: purior quantumlibct. A in
marg. : Nota. 16. B: prevalct. 20. A in marg. : Conclusio.
?o. B in marg. : Ecclesie dotacio fuit meritoria.
3o. Decr. I pars, d. XXII, c. I.

p. 289:
iC. A in marg. : Contra. Tcrcia obieccio. 23. A in marg. : Rc-
sponsio. 3l. B: quomodo posscssiones.

p. 290:
11. A in marg. : Nota. 20. A in marg. : Conclusio.
IX. Sergius III. (897 — 904). Comp. Gregorovius, Gesch. der
Stadt Rom im Mittelalter III, 242 hodie; id est, 1378; per duos
pseudomonachos scil. per Urbanum VI et Clementem VII.
```
