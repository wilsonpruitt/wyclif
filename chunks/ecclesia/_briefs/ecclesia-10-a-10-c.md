# Translation brief: ecclesia 10-a–10-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-10-a.md chunks/ecclesia/wyc-ecclesia-10-b.md chunks/ecclesia/wyc-ecclesia-10-c.md` once and fix what it reports.
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
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| presciencia | foreknowledge | |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| placitare | plead at law | Ruled 2026-10-02 (85.8). |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| regalia | regality | The king's royal right. Ruled 2026-10-02 (*Eccl.* 148.3, 151.12, 152.12). |
| forisfacere | commit forfeiture | Ruled 2026-10-02 (152.13). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| expropriacio | renunciation of property | Never "expropriation" (seizure). Ruled 2026-10-02 (*Eccl.* 9). |

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
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| prescripcio | prescription | The legal title by long use. Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| patronus | patron | Of a benefice. Ruled 2026-09-28 (coordinator, delegated) (13 sites). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| indulgencie | indulgences | Ruled 2026-09-28 (7 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| curia romana | the Roman curia | Ruled 2026-09-28 (*Dial.* 7.8; 5 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| exproprietarii / exproprietarie | the propertyless / without property | The friars who profess to own nothing. Ruled 2026-09-28 (6 sites); the adverb 2026-10-02 (*Eccl.* 169.6). |
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |

---

## Chunk 10-a: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-10-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-10-a
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "204.28–206.26"
divisions: "cap. 10 (heading 'CAP. X.' at 204.27); part 1 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "405 words; 359 unanimous or majority-real; 42 settled by vote (R2 28, R3a 12, R5a 2); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n241–n243 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 10, part 1: [TITLE]

## ¶1 · 204.28–206.10

> [p. 204] Istis premissis descendendum est specialiter ad privilegium Westmonasterii super quo versatur contencio. Supponatur itaque in primis (ut patet ex vera copia ministrata) quod dictum Westmonasterium habeat [p. 205] privilegium concessum ab Edgaro et sancto Edwardo confessore, concessum (inquam) sibi et ecclesie sub hac forma: Cognoscat, inquit Edgarus, magnitudo seu utilitas vestra quam discernimus et in perpetuum mansurum iubemus atque constituimus ut pro reverencia reliquiarum gloriosissimi apostoli Petri et quiete monachorum ibidem Deo famulancium, honor et laus eidem ecclesie habeatur, ut quisquis f ugitivorum pro quolibet scelere ad prefatam basilicam sancti Petri fugiens precinctum eius intraverit sive pedes vel pedester, sive eques vel equester, sive de curia regali sive de civitate seu villa, seu cuiuscunque condicionis sit, quocunque delicto facinoris contra nos vel succesores reges Anglie vel contra alium quemlibet fidelem sancte ecclesie foris factus sit, relaxetur et liberetur et vitam atque membra absque ulla contradiccione optineat. Preterea interminamur divina auctoritate et nostra, ut neque nos neque successores nostri neque ullus episcopus nec quicunque alius de iudiciaria potestate in ipsam sanctam basilicam vel in manentes in ipsa vel in homines qui cum sua substancia vel rebus ad ipsam tradere vel devovere se voluerint, nisi per voluntatem abbatis et suorum monachorum, ullam unquam habeant potestatem, sed sit hec mater ecclesia libera et absoluta ab omni invasione vel inquietudine omnium hominum cuiuscunque ordinis vel potestatis. Obsecramus eciam omnes successores nostros reges et [p. 206] principes per sanctam et individuam trinitatem et per adventum iusti iudicis, ut quoniam ex munificencia antecessorum nostrorum ipse locus videtur esse dicatus, nullus episcoporum vel abbatum aut eorum ordinatores vel quelibet persona possit quoquo ordine de loco ipso aliquid auferre aut aliquam potestatem sibi in ipso monasterio usurpare vel aliquid quasi per commutacionis titulum absque voluntate ipsius congregacionis vel nostrum permissum minuere presumat.

[ENGLISH]

## ¶2 · 206.11–206.11

> [p. 206] In carta vero sancti Edwardi sic scribitur:

[ENGLISH]

## ¶3 · 206.12–206.26

> [p. 206] Sit hic sancta mater ecclesia peculiaris patroni nostri et domini et magni apostoliter beati Petri libera et absoluta ab omni invasione et inquietudine omnium hominum cuiuscunque ordinis vel potestatis esse videantur. Et in alia carta eiusdem sancti sic scribitur: Preterea in perpetuum confirmo ut quisquis fugitivorum de quocunque loco pro quacunque causa cuiuscunque condicionis sit ipsum sanctum locum vel precinctum eius fugiens intraverit membrorum suorum ac vite inpunitatem consequatur cum omnimoda libertate, nec aliquis aliud quidlibet ab ecclesia illa vel a terris ad eam pertinentibus per vim aut consuetudinem exigat. Hec sunt verba magis pregnancia pro libertate dicti monasterii que omnia sunt per bullas Nicolai III. postmodum confirmata.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 205.3: Westminster privileges granted by Edgar,
- 206.12: and St. Edward.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 204: *CAP. X.* [HEAD]
  - 206: *inquietudine* (3 is the argument numeral; no s) [R3]
  - 205: *eciam* [THIN]
  - 205: *nostros* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 204:
n. Propter quadrigas in Cant. Canticor. VI, n. 14. i5. B: altis
stautibus. 28. A in marg. : Nota de privilcgio Westermonasterii
(Above 15;1 witliout mark of rcfcrcncc).

p. 205:
4. In carta: decernimus. 7. ibi: et pro quiele. 8. ibi:
eiusdem ccclesie habeator id est ut. 10. ibid : beati apostoli Petri.
12. i3. In codd. villa cniuscunque ; correxi c privilegio; vide Cod. dipl aev.
Sax. II, 366. i3. In codd. facinoriter. Corr. c priv. 22. ad
ipsam in codd. deest. Addidi c priv. 27. vel potestatis; adde: esse
videantur.
3. Comp. tom II, pag. 3*33. Cod. diplom. aevi Saxonici (ed.
Kemhle). Kemble gives the exact words of the greater part of
this charter.

p. 206:
2. i. In privil.: qucmndmodum cx munificencia. 12. B: sit dccst.
i3. In codd. etc. beati; correxi c carta Edwnrdi. 16. In codd: vi-
deatur; correxi c dipl. ap. Iscmble I. c. pag. 186. 16. A: sancti sancti.
20. In diplom. Iidwardi hic locus sic habetur: intmunis sit otnnmo
ac plenam libertatem consequattir. Sequentia quacre pag. seq. 2j. In
codd.: consuetum; corrcxi c cnrta Edwardi.
11. Cod. dipl. aevi Sax. tom IV. sub num. DCCCXXV, pag.
1S1. Comp. pag. 173 seqq. 16. Comp. Codicis dipl. aev.
Sax. tom. IV, p. 186. 26. Bullam Nicolai III. liuic diplomati
insertam invenies in Cod. dipl. 1. c. pag. 1 83- In Monastico Angli-
cano (edd. Dodsworth et Dugdale Londini i655) pag. 5>|. Bullas
hoc diploma confirmantes (ut supra memoratum est) non viili.
```

---

## Chunk 10-b: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-10-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-10-b
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "207.1–211.31"
divisions: "cap. 10 (heading 'CAP. X.' at 204.27); part 2 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1167 words; 1054 unanimous or majority-real; 105 settled by vote (R2 65, R3a 32, R3b 1, R5a 6, R6a 1); 8 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n244–n248 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 10, part 2: [TITLE]

## ¶1 · 207.1–210.10

> [p. 207] Quod autem hec possunt racionabiliter concedi, sic ostenditur: Omnia que possunt sonare in pietatem ac misericordiam, que homo potest de facto concedere, possunt racionabiliter concedi. Sed huiusmodi sunt omnia in dictis privilegiis annotata, ergo conclusio. Maior patet racione meriti quod non potest esse nisi racionabile, et minor patet ex hoc quod omne delictum commissum in hominem nedum potest sed debet remittere, et per consequens, tam rex quam totum regnum potest remittere iniusticiam quamlibet fugitivi. Confirmatur de debito de quo minime videretur; nam Matthei VI°, 12, docet Christus nos orare, ut Deus dimittat nobis debita nostra sicut et nos dimittimus debitoribus nostris, ubi docemur non dimitti nobis a Deo, nisi dimiserimus ex corde debita nostris confratribus. Secundo confirmatur ex parabola Salvatoris Matthei XVIII° de servo suffocante unum de conservis suis, postquam longe maiora debita a suo domino sunt dimissa. Serve nequam, inquit, omne debitum dimisi tibi, quoniam rogasti me, nonne ergo oportuit te misereri conservi tui, sicutego tui misertus sum? Et iratus dominus eius tradidit eum tortoribus, quoadusque redderet universum debitum. Sic, inquit, et pater meus celestis faciet vobis, si non remiseritis unusquisque fratri suo de cordibus vestris. Unde eodem capitulo docet Petrum in persona ecclesie quod usque septuagies septies, hoc est, quociens in ipsum peccaverit, dimitteret debitum fratri sue. Frater enim non incurrit culpabiliter debitum nisi excedendo decalogum mandatorum. Tercio confirmatur ex lege veteri, nam Levitici XXV° datur lex de anno septimo, quod tunc sabbatizabunt et anno quinquagesimo redibunt ad possessiones suas, [p. 208] eritque remissio plena debiti cuiuscunque. Nolite, inquit, affligere contribules vestros, sed timeat unusquisque Deum suum. Et breviter utrumque testamentum testatur creberrime misericordiam faciendam. Unde Matthei V°, 7, quando Christus tradidit legem suam, hortatus est ad misericordiam sub obtentu misericordie consequende. Beati, inquit, misericordes, quoniam ipsi misericordiam consequentur. Unde ad exprimendum quod misericordia in novo testamento debet excellere dicit discipulis Matthei IX°, 1: Euntes discite quid est: Misericordiam volo et non sacrificium. Et super talibus fundat se beatus Gregorius, exponens illud Matthei XXII°, 2, Simile factum est regnum celorum homini regi qui fecit nupcias filio suo, et ponitur in canone XXIII, q. IV: Cum in lege scriptum sit, diliges amicum tuum et odio habebis inimicum tuum, accepta tunc licencia, cum iustum fuerit ut Dei suosque adversarios quanta possent virtute comprimerent, eosque in ore gladii ferirent quod in novo procul dubio testamento compescitur cum per semetipsam veritas predicet dicens: Diligite inimicos vestros, benefacite hiis qui oderunt vos. Et post exponens illud evangelii: Thauri mei et altilia occisa sunt, venite ad nupcias. Quid, inquit, per thauros nisi veteris testamenti patres signantur. Nam dum ex permissione legis acceperant, quatinus adversarios suos odii retribucione percuterent, ut ita dicam, quid aliud quam thauri erant, qui inimicos suos cornu virtutis corporee feriebant? Quid enim per altilia nisi patres novi testamenti figurantur qui dum graciam interne pinguedinis percipiunt o terrenis [p. 209] desideriis innitentes, quasi contemplacionis penna sese ad sublimia sublevant? Ex istis videtur hunc sanctum intendere quod in magnis nupciis sancte matris ecclesie membra eius rudia pascenda sunt exemplo patrum testamenti veteris tamquam carnibus thaurinis qui contra infideles usi sunt ex mandato domini feritate; modo vero adveniente Christo mitissimo pascendi sunt laucius evacuatis grossis carnibus veteris testamenti, in secundo ferculo novi testamenti porrectis eis altilibus; quod fit, dum ad exemplum Christi et suorum discipulorum ob amorem sui paciuntur iniurias. Et utinam ista leccio esset per nos sacerdotes tam sermone quam opere efficaciter in populo predicata. Tunc enim non foret tanta sanguinis effusio nec tanta conturbans ecclesiam Christi per membra diaboli a lege Christi declinacio. Accipio itaque istam sentenciam tamquam catholicam et tocius ecclesie directivam et dico ulterius quod ipsa nedum non confirmat sed infirmat privilegium supradictum, quia (ut patet ex dicta sentencia et fide scripture) non est privilegium, nisi de quanto sonat in misericordiam privilegiantis et privilegiati et omnino in honorem Dei et utilitatem sancte matris ecclesie; quod cum capit instanciam de isto, ideo interimit se ipsum. Unde ista condicio debet subintelligi de natura privilegii in opere cuiuscunque privilegiantis ecclesiam, cum Deus non potest privilegiare aliquam partem ecclesie, condicione ista penitus pretermissa, quia tunc foret sibi ipsi et sponse sue contrarius. Ideo necesse est privilegiantes ecclesiam cavere precipue ne ex ignorancia scripture et cecitate seculi officiant matri sue cui debent proficere. Non enim solum debent attendere ad illud quod posset sonare in misericordiam et edificacionem ecclesie, sed ad illud quod verisimiliter [p. 210] secundum legem scripture sonaret in caritatem et utilitatem ecclesie, quia cum omnia facta sceleratissima possent occasione misericordie Dei sonare ad profectum ecclesie, patronus ecclesie indifferenter omnia talia ordinaret. Sic ergo conceditur quod tam rex quam regnum nostrum nedum potest sed debet de lege caritatis (que est ius communissimum contra quod non fit dispensacio) remittere omnes iniurias fratris sui, nedum hospitati infra basilicam sed ubicunque terrarum fuerit, sub divo, in celo vel purgatorio.

[ENGLISH]

## ¶2 · 210.11–211.3

> [p. 210] Nam cum remittere iniuriam sit caritatem ignoscere ipsam quoad dampnacionem vel vindictam, volendo iniuriantem transire impunem de quanto placuerit domino capitali, patet quod omnis christianus debet cedendo Christo remittere (quantum in ipso est) omnem fratris iniuriam. Nam ut sic meritorie defert Deo qui Deuteronomii XXXII°, 35,- dicit: Mea est ulcio et ego retribuam. bt sic est duplex remissio, scilicet debiti spiritualis quo quilibet christianus debet prodesse in vita caritatis cuilibet membro ecclesie; et illud debitum incurrit quilibet peccator (in quantum huiusmodi), cum ex lege caritatis et communione sanctorum iniuriatur Deo et toti ecclesie, ut patet XXIIIª q. IV. Hec autem, et recitatur proximo capitulo. Talem autem remissionem debet quilibet peccator habere quoad omnem iniuriam fratris sui, cum debet humiliter iudicium puniendi Deo relinquere. Secunda autem est remissio debiti corporalis, quam ut quis fecerit, cedit iuri illud debitum repetendi. Et qui non concipit istam duplicem remissionem debiti, est valde indispositus ad concipiendum materiam privilegiorum ecclesie vel [p. 211] scripturas. Sic enim loquuntur tractantes materiam de indulgenciis quod Deus remittit culpam et expetit penam. Ideo impetratur absolucio tam a pena quam culpa.

[ENGLISH]

## ¶3 · 211.4–211.31

> [p. 211] Ex istis patet quod stat hominem meritorie et plene remittere fratri debitum et tamen eum impetere excommunicare et quandocunque meritorie occidere pro eodem. Nam capio Petrum qui licite repetit in foro contencioso debitum a suo debitore, Paulum rite excommunicantem suum debitorem, et Linum meritorie persequentem suum debitorem usque ad mortem, ut puta, decapitacionem, suspensionem vel aliam mortem corporalem: patet possibilitas casus ex hoc quod aliter leges ecclesie de contencione, excommunicacione et occisione hominum forent heretice, quia legi caritatis contrarie. Stat ergo hominem meritorie exequi legem talem et cum de necessitate salutis tenetur iniuriam et debitum spirituale remittere, patet conclusio. Ymmo cum licet excommunicare accessorie, et per accidens sic persequi hominem pro debito corporali, videtur quod stat illud remittere et tamen ad salutem anime debitoris ex caritate fraterna quolibet istorum trium modorum eum persequi et torquere. Nemo enim meritorie sic persequitur principaliter propter debitum corporale, sed propter spirituale debitum et iniuriam factam Deo, remittendoque eum divino iudicio diligit ipsum in domino. Cum quo stat quod ex revelacione vel lege divina moveatur licite ad taliter cruciandum, sive ex sola detencione debiti committatur Dei iniuria, sive alia superveniens sit commixta; utrobique enim excommunicatur vel occiditur confuse pro omnibus, sicut Deus dampnat prescitum pro peccatis singulis que commisit.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 207.1: It is argued that these grants may reasonably be made: 1. because all that tends to mercy is lawful;
- 207.16: 2. by the parable of the wicked servant, which shows that debt should be forgiven;
- 207.31: 3. by the Sabbathical year of the old Law.
- 208.5: Christ also teaches us to be merciful;
- 209.3: and we are to follow the New Testament rather than the Old.
- 209.18: The duty of forgiveness does nothing to support a mischievous privilege.
- 210.5: Otherwise all offences ought to be forgiven: out of sanctuary as well as in.
- 210.17: Remission is of two kinds: a) of the spiritual debt: and this must be left to God;
- 210.25: b) of the material debt; which a man may forgive yet leave to be exacted by the law.
- 211.4: Forgiveness does not bar a request for punishment;

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 207: *Serve* (italic) [R3]
  - 208: *eritque* [R3]
  - 208: *sacrificium* (sacri-/ficium hyphenated; main token holds whole word) [R3]
  - 209: *magnis* [R3]
  - 209: *infirmat* [R4]
  - 210: *regnum* [R4]
  - 210: *impunem* [R4]
  - 211: *accessorie* [NW]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 207:
l. A in marg. : Racio. 20. In codd. qnando rogasii; corr. c
Malth. XVIII, 32. 24. A A,: diniiscrilis.
3i. Cf. Lev. XXV, i3, 17.

p. 208:
19. Lecturam in ore habet Gratianus, ut meminit Fditio Maurina ;
Gregor. Hom. XXXVIII: iure gladii. 26. li: promissioue. 3i. In
codd. elernis desideriis. Correxi e Gregor. I. c.
12. Homil. XXXVIII. in Matth. Opp. tom I. pag. 1 636 vid.
Decr. II. pars, causa XXIII, q. 4, cap. XVI.

p. 209:
18. A vn marg. : Responsio

p. 210:
5. A in marg. : Conclusio. n. A in marg. : Quid est remittere
iniuriam. i5. B: concedendo. 17. A in marg.: Duplex remissio.
B in marg. man. alt. : Remissio duplex. 28. A,: debiti scilicet, in
cod. 'A scilicet extinctum est.

p. 211:
3. addit: a culpa. A in marg. : Conclusio. Nota quomodo mali ex
caritatc sunt pcrscqucndi. 6. A A, : quomodocunque. 7. A
in marg. : Casus. 17. A in marg. : Conclusio.
7. De Peiro, Paulo et Lino cf. Wyclif, De civili dominio
pag. 3y.
```

---

## Chunk 10-c: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-10-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-10-c
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "212.1–216.26"
divisions: "cap. 10 (heading 'CAP. X.' at 204.27); part 3 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "1088 words; 998 unanimous or majority-real; 79 settled by vote (R2 43, R3a 26, R3b 1, R5a 7, R6a 2); 11 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n249–n253 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 10, part 3: [TITLE]

## ¶1 · 212.1–212.19

> [p. 212] Ex istis patet tercio, cum erga omnem punitum F oportet punientem servare cantatis amorem ac difficile vel impossibile est viantem caritative persequi fratrem suum contencione, excommunicacione vel occisione in visceribus caritatis, lex Christi est certissima qui, inquit, aufert que tua sunt, ne repetas, Luce VI°, 30 (quod alias diffuse exposui); Benedicite persequentibus vos, benedicite et nolite maledicere, ad Rom. XII°, 14, et si quis te percusserit ad maxillam dexteram, prebe ei et alteram Matthei V°, 39. Ille autem qui nescit erga inimicum quem cruciat servare regulas caritatis, non licet declinare ab istis consiliis. Unde Archidiaconus super XXXIII, q. V. Excomunicatorum, dicit quod non licet quemquam occidere nisi ex dileccione occisi preponderante dileccionem cuiuslibet temporalis, multo magis hoc astrueret purus theologus. Unde desidia predicacionis illius veritatis catholice fuit causa occisionis duplicis multi populi; remittat Deus episcopis qui ipsam dominis intrepide predicarent.

[ENGLISH]

## ¶2 · 212.20–214.3

> [p. 212] Ex istis patet solucio ad primum obiectum de quinta peticione oracionis dominice; nam secundum Augustinum, libro II°, De Sermone Domini in monte c° X°, peticio intelligitur de spirituali debito (ut alias diffuse exposui): Debitum, inquit, peccatum dici manifestum est. Non ergo quisquis hic urgetur pecuniam debitori dimittere, sed quecunque alius in eum peccaverit, quia tunc non reciperet a volente dare debitum, nec peteret a potente avaro qui inops animo inexcusabiliter detinet alienum. Et tum conclusio Augustini est: Si modeste ac leniter omnimodo quis egerit, ut [p. 213] sibi restituatur a tali, non tam intendens fructum pecunie, quam ut hominem corrigat cui indubie perniciosum est detinere, cum habeat unde reddat; non solum non peccabit sed proderit plurimum eciam debitori; aliter enim dum alienam pecuniam lucrum vult facere, dampnum fidei pacietur. Cum ergo sensus pretensus huius privilegii excludit hanc elemosinam, cum protegit indifferenter potentem et nolentem aliena reddere quam eciam inpotentem, manifestum est quod ponit obstaculum regulis caritatis. Per hec patet responsio ad secundum, cum dictum Christi intelligitur de debito culpe cuius satisfactoriam solucionem omnis christianus tenetur humiliter iudici supremo remittere. Si enim intelligeretur de corporali debito, tunc omnes religiosi possessionati et clerici tenerentur ex privilegio Christi quo amplius obligantur eius consiliis et preceptis, remittere et non repetere omne eis debitum corporale; et tamen dicitur quod sine misericordia exigunt eciam ab inpotentibus tale debitum per exacciones seculares et ecclesiasticas censuras ardencius quam domini seculares. Non ergo est eis privilegium fovere hostes ecclesie, ne sibi satisfaciant, cum tamen sufficiant, quia (ut alias dixi) Deus non potest licenciare hominem, ut servet debitum sine hoc quod satisfaciat saltem Deo, quia- nisi satisfaciat restitucione vel meritoria punicione, est dampnandus. Deus autem non potest licenciare hominem ad peccandum; hoc autem foret privilegium tali ecclesie quod haberet a suis patronis seculares divicias ad ministrandum fugitivis impotentibus se iuvare, et (quantum facultas suppetit) pro ipsis restituere, quia hoc sonaret utrimque in opus misericordie, non autem defensio cuiuscunque fugitivi quantumlibet excomunicati, [p. 214] quantumcunque defensio cadat fugitivo ad dampnum anime et iniuriatis ad detrimentum, nec non ad perturbacionem regni atque ecclesie.

[ENGLISH]

## ¶3 · 214.4–214.22

> [p. 214] Ad tercium dicitur quod tam sabbatizacio pro anno septimo quam remissio pro anno iubileo fuit valde racionabilis pro tempore suo, nunc autem pro tempore legis gracie quando colimus octonarium, debemus habere amorem fertiliorem: sicut enim septenarius numerus virginitatis habet solum unitatem pro parte aliquota, octonarius autem habet unum, duo et quattuor que septem constituunt, sic patres veteris testamenti erant in caritate plus steriles quam patres sub lege gracie qui colunt ex integro septenarium; qui signat unici Dei cultum et preter hoc unionem Christi et ecclesie que est unitas septenario superaddita in numerum priorem, redundans quoad partes aliquotas. Et sic debemus nos tempore legis gracie habere diffusiorem amorem et ampliorem continenciam, quam habuerunt patres veteris testamenti, quia nedum habemus contribules, sed fratres germanos singulos christianos, cum omnes nati sumus spiritualiter de eodem patre Christo et eadem matre ecclesia.

[ENGLISH]

## ¶4 · 214.23–215.10

> [p. 214] Et rogo innitentem isti evidencie notare, primo quomodo nos sacerdotes Christi debemus esse magis misericordes et magis religiosi quam sacerdotes veteris testamenti. Notet secundo quomodo non licuit sacerdotibus Aaronitis acquirere sibi redditus vel seculare dominium, sed in partem dominii forent de porcione sibi limitata a domino contentati (ut patet Ezechielis XLIV°, 28); alie autem tribus impetrantes possessiones a suis contribulibus non exheredarent eos perpetuo, sed in anno iubileo restituerent diutissime impetrata. Et notet tercio per iuxtaposicionem [p. 215] conversacionis cleri nostri eciam religiosi, si sit proporcionalis correspondencia utrobique. Dicitur enim quod clerus eciam vocatus religiosus exheredat multos de fratribus eciam pro suo perpetuo, vocantes hoc perquisitum Christi patrimonium, cum tamen Christus omnino exproprietarie pendebat nudus in cruce, scisso velo templi, ad denotandum Judeis et gentibus quod spiritualis hereditas est simpliciter appetenda et terrena possessio contempnenda (ut expositum est... cap. libri sexti).

[ENGLISH]

## ¶5 · 215.11–216.11

> [p. 215] Tunc enim essemus altilia de puro frumento, pasta ad exemplariter nutriendum filios, ut fecerunt sancti patres, vice quorum fungimur saltem in nomine, ut congregemus pecunias, non ut sanemus animas. Modo autem pervertimur in corvos perfidos, pastos de cadavere extra navem ecclesie, et tamquam aves rapacissime in altum ascendimus, non ad pericula et commoda spiritualia ecclesie speculandum sed lumina habemus acutissima, membra velocissima et rostra retentissima ad predandum; et cum beatus Gregorius, pastor precipuus, dicit XXI° Moralium, cap. IV°, satis asperum verbum atque terrificum: Festina, inquit, consolacio bonorum est consideratus finis malorum. Dum enim ex eorum interitu malum conspiciunt quod evadunt, bene existimant quidquid adversum in hac vita paciuntur. Eant ergo nunc reprobi et delectacionum suarum desideria compleant: in finis sui dampnacione sensuri sunt, quia mortem male viventes amaverunt. Transitorio autem verbere affligantur electi ut a pravitate flagella corrigant quos paterna pietas ad hereditatem servat. Modo etenim flagellatur iustus, [p. 216] et verbere discipline corrigitur, quia ad eterne hereditatis patrimonium preparatur. In suis autem voluptatibus relaxatur iniustus, et quanto eis temporalia bona suppetunt, tanto eterna denegantur. Vituli, inquit, qui mactandi sunt in liberioribus pastibus relinquuntur; non quin stat vere divitem, in temporalibus affluentem, regnum celorum acquirere, sed tunc oportet Deum miraculose agere quod aput homines est impossibile, convertendo mundo divitem ab affeccione temporalium et carnalium voluptate, et omnino in extremis suis finire in evangelica paupertate (ut patet Luce XIV°).

[ENGLISH]

## ¶6 · 216.12–216.26

> [p. 216] Unde quia probabile est paucos mundi divites sic facere, ideo argumentum topicum est quod multi tales moriuntur in peccato finalis inpenitencie. Ideo dicit Gregorius (ubi supra): Negantur electis in hac vita bona terrena, quia et egris quibus spes vivendi est nequaquam a medico cuncta que appetunt conceduntur. Dantur autem reprobis bona que in hac vita appetunt, quia desperatis egris omne quod desiderant non negatur. Attendamus ergo ad doctrinam Christi in opere et sermone et videbimus quod filios suos carissimos non sic dotat, et tum nos faciendo elemosinas debemus capere exemplum a Christo. Et patet quod dicte raciones super pietate milvina pretense non concludunt nec rectificant sed excludunt privilegia supradicta.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 212.1: but we must not punish if we cannot do it in love.
- 212.21: In the Lord's prayer "debts" means "sins".
- 213.11: Money debts may be claimed from those who can pay.
- 214.4: As to the Sabbatical year we ought to be more merciful than the Fathers of O. T.,
- 214.23: our clergy especially;
- 214.32: but it is not so.
- 215.3: Even the regular clergy disherits many men in perpetuity.
- 216.12: Danger of riches.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 212: *patet* [R3]
  - 212: *ac* (158ᵇ is the folio mark) [R3]
  - 212: *certissima* (5 is the line number) [R4]
  - 212: *II°* (libro II°) [R3]
  - 213: *quod* (158ᶜ is the folio mark) [R4]
  - 214: *iubileo* [NW]
  - 215: *Christi* (5 is the line number) [R3]
  - 215: *Christus* [R3]
  - 216: *facere* (tall ascender = f) [R3]
  - 212: *ut* (30 is the line number glued) [THIN]
  - 215: *flagellatur* [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 212:
i. A in marg. : Conclusio. 9. R: in maxilla dextera. i3. In
codd. Excomnmnicantes. i5. AA,: preponderantem. 20. A in
marg.: Triplex solucio. 22. A in marg. : Augustinus. 24. A in
marg. : Dimittere debita quid est? 20. A in marg.: Conclusio.
3o. In codd. omnino quis; corr. ex Aug. I. c.
22. Comp. August. Opp. III, p. II, pag. 214, 211.

p. 213:
i. A: intendcs A,: intendendo. 5. A. A, : aliter enim — pacietur
deest. 21. A in marg.: Conclusio. 27. Codd.: I)eus autcm;
rectius : Deus enim.

p. 214:
4. A in marg.: Qualitcr sabbatizacio pro anno septimo et rcmissio
pro anno iubileo fuit valida tempore suo et non iam. 18. continuum
in codd. 20. A: contribulos. 23. A in marg. : Status cleri.
Nota tria. B. in marg. man. alt. : Nota pro sacerdotibus.

p. 215:
6. B: ex proprietate. g. io. exposimm est: sequitur lacuna in
codd. 20. A in marg.: Gregorius. 22. A in marg. : Nota de
tribulacione bonorum et prosperitate malorum in hac vita. 25. leve
existimant in textu s. Gregorii; quidquid adversi: ib. 3i. Nunc
etenim in textu s. Greg.
22. Opp. tom I. pag. 681.

p. 216:
3. ib.: Quia tanto ci temporalia bona suppetunt, quanto aeterna
denegantur. 5. ib.: in liberis. i5. A in marg. : Grcgorius. B in
marg. : Bona terrena quare electis negantur. 17. A: cunta pro
cuncta. 21. A A,: et videamus. 24. B in marg. man. alt.:
Pietas Milvina. 27. A in marg. : Prima racio.
```
