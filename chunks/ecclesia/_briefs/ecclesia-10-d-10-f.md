# Translation brief: ecclesia 10-d–10-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/ecclesia/wyc-ecclesia-10-d.md chunks/ecclesia/wyc-ecclesia-10-e.md chunks/ecclesia/wyc-ecclesia-10-f.md` once and fix what it reports.
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

## Glossary (the 144 rows these chunks use; the full file is GLOSSARY.md)

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
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| sacerdotes vulgares | common priests | The adjective; kept apart from *vulgares*, "the common people". Ruled 2026-09-28 (2 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| suffragia | suffrages | The prayers and good works shared out by the church or an order. Ruled 2026-09-28 (11 sites). |
| suffragari | to aid by intercession | The verb of *suffragia*. Ruled 2026-09-28 (2 sites). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| elemosinarius | almsman | The one who receives alms (cf. *elemosinatus*). Ruled 2026-10-02 (46.21). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| privilegium / privilegiare / privilegiacio | privilege / to privilege / privileging | The key term of *Eccl.* 8–9. Ruled 2026-10-02. |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| regnum | kingdom | Every sense: the political state as well as the kingdom of God and scripture's kingdoms. Not "realm". Wilson, Ruled 2026-09-28 (27 sites). |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| titulus | title | As in title to property. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| potencia regulata racione | power regulated by reason | Pilot. |
| elemosina | alms | |
| elemosinare; elemosinatus | to give alms to; almsman | The almsman is the beneficiary of an endowment. Ruled 2026-09-28 (coordinator, delegated) (2 sites). |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| sacerdos / presbiter | priest / presbyter | ⚠ Kept distinct: Wyclif's argument on orders needs the difference visible. |
| clerus; clericus | the clergy; cleric | |
| clerus cesareus | the caesarean clergy | Wyclif's term for clergy in secular office. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| coactivus; cohercere, cohersitivus | coactive; coerce, coercive | Kept apart: *potencia coactiva* "coactive power" (the ruler's), *cohercere* "coerce". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| legalitas | legal standing | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| censura | censure | Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| prelatus / sacerdos cesarius | caesarean prelate / priest | Extends *clerus cesareus*. Ruled 2026-09-28 (22 sites, *cesar-*). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| frater | friar (of the mendicants) / brother | By context. |
| possessionati | the possessioners | Endowed religious. |
| protestacio; protestari | declaration; to declare solemnly | ⭐ The submission formula ("if anyone can teach me this is contrary to scripture or reason, I will humbly retract"). Penn and Lahey both inverted it (T. pp. 369, 378). Render it as a retraction offer, never as defiance. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori / a simili | the topic from the greater / from the like | The dialectical topics. Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | what follows | Ruled 2026-09-28 (coordinator, delegated). |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | teaching | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence". Ruled 2026-09-28 (51 sites in the *Dialogus*). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). |
| participium | participation | Not the grammatical participle. Ruled 2026-10-02 (85.6). |
| suffragium sensus | aid of sense | As *suffragium* "aid"; not the church's *suffragia*. Ruled 2026-10-02 (97.22). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| inobedienciarius | disobedient man | The negative of *obedienciarius*. Ruled 2026-10-02 (146.11). |
| suffragium (*legis, privilegii*) | aid | As *suffragium* "aid" (01-a) and *suffragium sensus*. Ruled 2026-10-02 (149.29, 152.8). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| inhabilis | unqualified (to hold office) | "unwieldy" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb. The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| prevaricator; prevaricancia | transgressor; transgression | Ruled 2026-09-28. *Basali prevaricancia* (*Dial.* 9.24) is doubtful: see its C note. |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| prevaricari | to transgress | The verb of *prevaricator*. Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |

---

## Chunk 10-d: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-10-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-10-d
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "216.27–220.25"
divisions: "cap. 10 (heading 'CAP. X.' at 204.27); part 4 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "931 words; 859 unanimous or majority-real; 59 settled by vote (R2 31, R3a 23, R3b 2, R5a 3); 13 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n253–n257 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 10, part 4: [TITLE]

## ¶1 · 216.27–217.8

> [p. 216] Ideo restat iam quarto obicere contra illa. Videtur primo: Si tenor privilegiorum debet sic intelligi nude ad litteram, tunc posito quod exercitus inimicorum invadat Angliam, debet in illo loco habere refugium, sic quod post recreacionem posset animosius predari provinciam. Nam quelibet persona talis exercitus est [p. 217] aliquis homo de aliquo loco veniens, pedester vel equester, intrans illum locum ex causa aliqua, sed omnis talis iuxta tenorem verborum privilegii habebit in loco illo immunitatem omnimodam, ergo quelibet persona talis exercitus virtute privilegii, quam diu voluerit, quiescet ibi pacifice; si enim in aliquo casu capit instanciam, oportet nuda verba abicere et sapere sanam sentenciam.

[ENGLISH]

## ¶2 · 217.9–218.13

> [p. 217] Hic dixit mihi quidam ingeniosus legista quod quelibet persona talis exercitus gaudebit hoc privilegio, cum non oportet propter tales casus inpossibiles limitare vel restringere privilegia regum. Illud autem capit calumpniam multiplicem aput quemlibet mentis compotem. Nam nec rex potuit concedere tale privilegium nec clerus debuit ipsum ut privilegium sibi admittere, cum non potest regno nostro vel parti eius esse privilegium fovere destructores regni et tocius ecclesie Anglicane, sicut non est privilegium alicui se ipsum deteriorando destruere. Ideo quicunque impetraverit vel defenderit hoc ut privilegium regno nostro, tamquam infidelis Deo et regno degenerat. Nec valet dicere quod talis comitiva non possit consurgere et regnum nostrum invadere, cum in tribus conquestibus scilicet Britonum, Saxonum et Normanorum hoc contigit, ymmo tales depopulatores tempore regis Edwardi secundi surrexerant et cardinales in comitatu Dunelmie spoliarunt, et in nobili regno Francie, in Lumbardia et in aliis regnis potentibus tales comitive depopulantes nostris temporibus surrexerunt: ymmo diebus istis regna nunquam vel raro sunt sine talibus vel corporaliter vel spiritualiter confederatis ad destruccionem eorum, cum talis corruptela sub pallio privilegii posset per se regnum perdere. [p. 218] Item, rex non potest quicquam rite concedere quod vergeret ad enervacionem regni sui vel iniuriam sui populi, sed utrumque contingeret datis verbis recitati privilegii, secundum nudum verbalem conceptum. Ergo non subiacet potestati regis privilegium tale concedere. Maior patet ex dictis de privilegio, cum nichil sit privilegium, nisi quod directe vergit ad utilitatem sancte matris ecclesie; destruccio autem regni nostri et iniuria facta suo populo non potest directe vergere ad honorem Dei et utilitatem sancte matris ecclesie, ergo non subiacet potestati regis alicuius privilegium tale concedere; Deus enim non potest in contradiccionem.

[ENGLISH]

## ¶3 · 218.14–219.22

> [p. 218] Et confirmacio est quod officium regis terreni in quantum huiusmodi) est ecclesiam sanctam defendere, inimicos eius rigide cohercere et cunctis sed specialiter suis legiis iusticiam observare (ut patet libro III° cap°. Minor autem sic ostenditur: Nichil plus enervaret regnum quam tutela facinorosorum sine correpcione legitima. Unde Ecclesiastici X°, 8, scribitur: Regnum de gente in gentem transfertur propter iniusticias, iniurias, contumelias et diversos dolos; sed nichil plus cederet ad fomentum istorum quattuor quam concedere cuilibet libertatem quod, quidquid facinoris perpetraverit, fugiendo ad tam patentem locum non erit ab aliquo castigatus; ergo hoc evidenter minaretur ruinam regno. Si enim hoc privilegium esset per totam Angliam concessum, quomodo staret regnum? Rex enim non haberet potestatem ad cohercendum civiliter homines legios suos, et tunc non foret univoce rex eorum vel populi qui sue non subiacet potestati. Nec est racio quare rex posset concedere libertatem tanto loco, [p. 219] [quin per idem et patrie, et sic alius rex alii patrie, et sic quousque tota Anglia fuerit libertata. Si enim totalis exempcio extingueret totam regiam potestatem, particularis exempcio extingueret partem eius, cum de tanto non haberet rex potestatem loci vel persone incolentis ad castigandum ipsam, quantumcunque in regem vel regnum deliquerit, et sic non foret rex tocius Anglie, cum locus exemptus foret in regno, sed non de regno. Non enim haberet rex tantam potestatem ad subiugandum incolas talis loci sicut habet potestatem ad puniendum gentem Francie, cum tantum eximuntur a cohercione regia sicut incole Almanie vel omnino aliene provincie. Et quantum ad iniuriam populi, patet quod vendicatur libertas, ut quantumcunque sceleste quis iniuriatus fuerit proximo, homicidio, furto, mechia, prevaricando in omnem speciem mandatorum decalogi, fugiat ad illum locum et precluditur iniuriato iusticie complementum, cum nec tenetur per se vel procuratorem ibi vel alibi stare iuri, et tamen rex Anglie in coronacione sua iuratus est religione laudabili quod non negabit sed concedet iusticiam cuicunque.

[ENGLISH]

## ¶4 · 219.23–219.28

> [p. 219] O si totum regnum esset sic privilegiatum quoad omne factum scelestum et undique proclamatum licitum mendacium, qualem nidum haberet diabolus in Anglia ad protegendum in delictis verbi et operis populum tenebrarum? Revera in baratro non habet tale privilegium.

[ENGLISH]

## ¶5 · 219.29–220.25

> [p. 219] Unde quesivi ab adversariis duos casus: Primo, si predans, furans vel mutuans quantumlibet magnum thesaurum ab alia ecclesia et illuc fugiens cum thesauro habebit ad sensum expositum omnimodam libertatem. Et dictum est mihi quod sic; tum quia verba privilegii a quibus non licet recedere generaliter [p. 220] illud sonant, tum eciam quia aliter foret nimis suspectum, negando laycis complementum iusticie et faciendo clero iusticiam. Sed tunc sequitur, primo quod rex qui potuit concedere ut sceleratissimi homines in perpetuum iniuste detineant reliquias et quecunque bona immunis ecclesie posset concedere ut iusti auferant temporalia ab ecclesia delinquente. Nam per se notum est quod ille qui potest concedere magis elongatum a communi iure potest concedere consonancius iuri Dei. Et iterum notum est quod maius peccatum foret iniuste, pertinaciter et obstinate detinere rem alienam, quam foret iniusta ablacio, quia pro primo est homo excommunicandus tamquam hereticus, et pro secundo non, nisi affuerit contumax obstinacia, ut noverant legiste. Ideo non dubium, si rex potest concedere privilegium ut quilibet regni sui habeat libertatem ad perpetuo detinendum iniuste ablata de sancta matre ecclesia, multo magis potest concedere licenciam, ut iusti auferant elemosinas suas quibus fraudantes regnum et sanctam matrem ecclesiam abutuntur. Unde inconsonum factum est et sibi ipsi contrarium tam ferventer defendere illud tamquam privilegium catholicum et solicite laborare, quando raciones deficiunt, ad dampnandum aliud tamquam hereticum.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 216.27: This privilege would allow a hostile army to be harboured.
- 217.22: Such a danger is not purely fanciful.
- 218.1: To give such a privilege is beyond the King's power;
- 218.24: since such a refuge for criminals would ruin the realm;
- 219.14: and cause injustice to individuals.
- 219.29: Difficult case for the supporters of the privilege.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 216: *primo* (glued 'army to' is the English side-note) [R4]
  - 217: *aliquis* (K 158ᵈ are margin letter and folio mark) [R3]
  - 217: *legista* [NW]
  - 217: *impetraverit* (im-/petraverit hyphenated; main token holds whole word) [R4]
  - 218: *legiis* [NW]
  - 218: *III°* [R4]
  - 219: *cohercione* [NW]
  - 220: *∅* (print has sus-/pectum; main already holds suspectum whole at pos 8) [INS?]
  - 220: *consonancius* [NW]
  - 220: *legiste* [NW]
  - 219: *quin* (alinea L and 159b folio mark glued) [THIN]
  - 219: *idem* [THIN]
  - 217: *quod* (159ª is the folio mark, dropped) [OVERRIDE-MARK]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 216:
3. ib.: Quia tanto ci temporalia bona suppetunt, quanto aeterna
denegantur. 5. ib.: in liberis. i5. A in marg. : Grcgorius. B in
marg. : Bona terrena quare electis negantur. 17. A: cunta pro
cuncta. 21. A A,: et videamus. 24. B in marg. man. alt.:
Pietas Milvina. 27. A in marg. : Prima racio.

p. 217:
9. A in marg.: Responsio qucdara. 10. A: hoc hoc. 26. H:
sccundi deest. Recte: surrexcrunt. 33 B: privilegio.
25. See Walsingham I, pag. i5i.

p. 218:
i. A in marg. : Secunda racio. (Above i5q* without mark of rcferencc.)
5. A in marg.: Nota de privilegiis ut supra. 6. Maior; in codd.:
am (assumptum); recte aor (= maior); vide 1. 18: Minor autem. 7. B
quod deest. 14. A in marg. : Officium regis. 22. A in marg. :
Contra privilegia locorum. (Below i5q* without mark of reference.)
28. A in marg. : Casus.

p. 219:
23. A in marg.: Casus. 2y. A in marg. : Prima qucstio.
29. 3o. B: si predicans. 32. 33. B: omnimoda libertate.

p. 220:
3. A in marg. : Bona racio. i5. Aj correxit: novcrunt. 27. A
in marg.: Conclusio.
```

---

## Chunk 10-e: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-10-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-10-e
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "220.26–224.13"
divisions: "cap. 10 (heading 'CAP. X.' at 204.27); part 5 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "868 words; 786 unanimous or majority-real; 66 settled by vote (INS 1, R2 34, R3a 25, R3b 1, R5a 4, R6a 1); 16 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n257–n261 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 10, part 5: [TITLE]

## ¶1 · 220.26–221.16

> [p. 220] Ego autem dico consonancius pro privilegiis sancte matris ecclesie quod rex non potest cuiquam concedere libertatem ad violente auferendum et multo evidencius ad iniuste detinendum aliquod bonum de quocunque membro ecclesie, nisi prius peccaverit hoc merendo. Nec est hic sophisma: Rex concedit malefico libertatem, ut non puniatur et ut maneat in perpetuum inaccusatus de crimine, sed non concedit sibi licenciam ad peccandum vel cuiquam iniuriandum; nam licenciare [p. 221] ad formaliter atque notorie antecedens ad quamcunque iniuriam est licenciare ad ipsam iniuriam; ut si Deus dat mihi licenciam ad frangendum caput presbyteri, et hoc non potest fieri sine facinore, tunc Deus dat mihi licenciam ad facinus perpetrandum. Correspondenter, notato scelerato fugitivo quiescente in dicto monasterio cum rapina pro suo perpetuo, queratur ab eo vel defendente hoc privilegium, a quo habet licenciam sic pausandi. Si dicatur quod non habet, tunc licitum est collacionem tam illicitam removere. Si dicatur quod a rege habet illam licenciam, sequitur cum veris quod rex licenciat ad antecedens formaliter ad peccatum, et longe coloracius dici poterit quod rex legitime licenciat ad auferendum temporalia, sed nullo modo ad faciendum iniuriam cuicunque, nam ablacio fieri potest legitime sed non talis detencio.

[ENGLISH]

## ¶2 · 221.17–224.13

> [p. 221] Secundo quesivi, si fugitivus huiusmodi possit excommunicari, dum fuerit in loco illo pro facinore exterius perpetrato, vel si excomunicatus extra locum et fugiens ad ipsum ne virtute brevis regii capiatur ad carcerem, habebit in dicto monasterio libertatem? Et dictum est mihi quod non, quia leges humane non derogant legibus et iuri ecclesie, et specialiter ut inobedientissimis excommunicandis apponatur anime medicina; aliter enim liceret excludere et privilegiare spiritualiter infirmum, ut sordescat in crimine nec accipiat correccionem ab homine; quod cum sit contra legem correpcionis fraterne, Matthei XVIII°, 1, Si peccaverit in te frater tuus etc, manifestum videtur quod talis defensio non habet privilegium sed pravilegium Antichristi. Ymmo cum talis sit plene et non minus excommunicatus a Deo, non obstante quod sentencia non sit lata ab homine, sequitur [p. 222] iuxta fidem scripture et leges ecclesie quod non est communicandum cum tali, nisi forte ut convertatur, ne inficiat gregem Christi. the Ex quotlibet talibus evidenciis dicitur quod licet talem fugitivum excommunicare et post quadraginta dies excommunicacionis carceri mancipare. Sed dato isto sequitur, cum licet excommunicare pro quocunque facinore, quod fugitivus talis facinorosus sit statim excommunicandus et consequenter post quadraginta dies incarcerandus, et cum non habebitpost excommunicacionem maiorem favorem quam ethnicus et publicanus, videtur quod sit de monasterio extrahendus et in carcere publico cum aliis excommunicatis tamquam alienus a filiis ecclesie detrudendus. Unde cum in dubiis via securior est tenenda, et vel est, dubium vel probabile quod fovens taliter criminosum erit particeps criminis ex consensu vel culpabilis, negando coreccionis suffragium, quod foret verum privilegium, oppositum hinc privilegio, videtur, cum cursus legis communis sit via securior, quod illa sit pocius sustinenda. Quomodo rogo tenderet ad profectum persone pro querenda beatitudine indifferenter omnes facinorosos, diabolicos et inimicos ecclesie in domo sua protegere et medicinam correpcionis et censuras ecclesie quibus sanarentur ab eis precludere? Revera nec hoc nec participacio rapine sonat religiosis ad commodum. Nam Hely non propter fomentum malicie filiorum sed propter remissionem correpcionis filiorum punitus fuit morte et privatus summo sacerdocio in sua posteritate, ut patet I° Regum, II° et IV° capitulis, et III° Regum II°. Hoc ergo posset sonare in privilegium dicti loci quod fugitivos inpotentes, de quibus foret spes conversionis ad frugem melioris vite, in vite necessariis et pecuniis debitis de regis elemosinis misericorditer relevarent et predas latronum [p. 223] illatas fideliter restituerent. Hoc enim esset elemosina et sic privilegium cedens undique ad utilitatem parcium, ad honorem Dei et profectum ecclesie (ut sepe superius inculcavi). Tercio principaliter arguitur ex hoc quod omne bonum utile est fundabile in scriptura iuxta conclusionem secundam capituli VIIIⁱ, sed non est fundabile in scriptura nec in lege ecclesie quod locum vel personam sic generaliter privilegiare liceat. Ergo non est bonum utile ecclesie et sic non privilegium alicui sic facere. Minor patet ex hoc quod in veteri testamento cautum est de civitatibus refugii, ut dictum est capitulo VII°; nullibi autem signatum est refugium pro sceleratis, sed limitatum est ut pro occisione casuali preter propositum habeat occisor refugium, ut patet Levitici XXV°, Deuteronomii XIX° et Josue XX°. In novo autem testamento non signatur tale refugium, sed precipitur Matthei XVIII°, 17, quod talis sceleratus sit sicut ethnicus et publicanus. Unde ergo nobis autoritas ad hostes Dei ac sancte ecclesie taliter protegendum, specialiter cum legalis correccio sive punicio foret plus misericors atque iusta, tempore autem legis gracie obligamur ad misericordiam ampliorem? Quantum autem ad iura canonica, videtur mihi quod specincantur quinque casus in quibus malefici a defensione ecclesie excluduntur; tres autem casus exprimuntur III° Decretalium, De Immunitate Ecclesiarum, capitulo Inter alia, sub hac forma: Hoc verum est, scilicet quod fugientes ad ecclesiam habebunt [p. 224] immunitatem nisi publicus latro fuerit vel nocturnus populator agrorum qui, dum itinera frequentata vel publicas stratas obsidet aggressionis insidiis, ab ecclesia extrahi potest, inpunitate non prestita secundum canonicas sancciones. Si vero servus fuerit qui confugerit ad ecclesiam, postquam de inpunitate sua dominus eius clericis iuramentum prestiterit, ad servicium domini sui redire compellatur eciam invitus, alioquin a domino poterit occupari. Ecce tres casus in quibus licet fugitivum invitum extrahere, et libro V°, De Homicidio, ponitur pro lege illud Exodi XXI°, 14, Si quis per industriam occiderit, ab altari meo evellas eum, ut moriatur.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 220.26: We maintain that the king cannot give a privilege to rob or detain wrongfully.
- 221.17: Another case.
- 222.4: At least the criminals ought to be excommunicated and after forty days imprisoned.
- 223.5: 3rd chief argument: Such privileges have no foundation in Scripture.
- 223.24: Exceptions made in Canon Law to right of sanctuary:
- 224.1: 1. a public thief,
- 224.3: 2. a waster of fields,
- 224.6: 3. an escaped slave,
- 224.9: 4. a wilful homicide.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 220: *Ego* [R3]
  - 220: *consonancius* [NW]
  - 221: *ad* (N 159ᶜ are margin letter and folio mark) [R4]
  - 221: *formaliter* [R4]
  - 221: *tuus* (italic) [R3]
  - 222: *licet* (O is the alinea letter) [R3]
  - 222: *I°* (I° Regum) [R3]
  - 222: *II°* [R3]
  - 222: *III°* [R4]
  - 223: *arguitur* [R4]
  - 223: *VIIIⁱ* (superscript i after VIII) [R4]
  - 223: *III°* [R4]
  - 224: *immunitatem* ('1. a public thief,' is the English side-note) [R3]
  - 224: *iuramentum* (italic) [R4]
  - 223: *illatas* (alinea O and 159d folio mark glued) [THIN]
  - 223: *habebunt* (asterisk mark follows) [THIN]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 220:
3. A in marg. : Bona racio. i5. Aj correxit: novcrunt. 27. A
in marg.: Conclusio.

p. 221:
10. A A,: cnbacionem. 16. B: sed non est talis detencio. 17. A
m marg. : Secunda questio. 20. breve i. e. mandatum. 22. A
in marg. : Responsio. 28. B in marg. : Matth. VIII.

p. 222:
(none)

p. 223:
5. A in marg. : Tercia racio. 7. A A,: cap. XVIII. 8. B:
quod locum deest. 12. cautum; fortasse tantum legendum.
12. 13. A cap. XVI. B: VI. i5. 16. AA: LeviticiXV. 24. A in
marg.: Nota qui malefici a defensione ecclesic excluduntur. B in marg. :
Nota quinque casus (in) quibus a sanctuario extrahitur fugitivus.
7. Vide supra pag. 173. 16. Vide supra pag. 147.
27. Dec. Greg. IX. lib. III, tit. XI. IX, cap. VI, mutatis verbis:
scilicet quod fugientes ad ecclesiam habebunt immunitatem.

p. 224:
2. In codd. : frequcnlat. Corr. c decr. sup. mem. 12. occiderit sc. :
proximum suum el pcr insidias. 23. Jn codd.: ct deest. Addidi e
decr. supra mem.
if>. ib. cap. X. 28. Sec. Decr. sec. pars, causa XVII, q.
IV, c. IX.
```

---

## Chunk 10-f: write to `/Users/wilsonpruitt/wyclif/chunks/ecclesia/wyc-ecclesia-10-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-ecclesia-10-f
work_la: Tractatus de ecclesia
work_en: On the Church
volume_slug: ecclesia
editor: Johann Loserth
year: 1886
pages: "224.14–227.18"
divisions: "cap. 10 (heading 'CAP. X.' at 204.27); part 6 of 6, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: three-witness
witnesses: [iohanniswyclift00mattgoog, iohanniswycliftr00wycluoft, iohanniswycliftr04wycl, latinworks10wycl, tractatusdeeccl00wycl, tractatusdeeccle00wycl]
check: "734 words; 638 unanimous or majority-real; 75 settled by vote (R2 51, R3a 18, R5a 5, R6a 1); 21 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks10wycl, leaves n261–n264 (printed p. = leaf − 37)"
status: draft
---

# *De ecclesia*, chapter 10, part 6: [TITLE]

## ¶1 · 224.14–226.11

> [p. 224] Et ut videtur mihi, quintus casus exprimitur in 111° Decretalium, in fine tituli De Immunitate Ecclesie, cum inquit: In eo in quo delinquit puniri quis debeat, et frustra legis auxilium invocet qui committit in legem: mandamus quatenus nuncietis publice tales non debere gaudere immunitatis privilegio quo faciunt se indignos. Et ipsos indignos prius exprimit sub hiis verbis: Nonnulli inpunitatem suorum excessuum per defensionem ecclesie obtinere sperantes, homicidia et mutulaciones membrorum in ipsis ecclesiis vel earum cimiteriis committere non verentur, qui nisi per ecclesiam ad quam confugiunt crederent se defendi, nullatenus fuerant commissuri. Unde glosa dicit quod omnes leges que videntur istis contrarie, ut XVIIª, q. IVª et cetere leges, sonantes in presidium maleficorum in sanctuario, intelliguntur de dignis tali presidio. Hugucius, inquit, male dixit, [p. 225] concordando decretales et decreta, quod dicta decretalis intelligitur de illis qui fugientes ad ecclesiam non deliquerunt in ea vel cimiterio eius sed alibi. Talibus, inquit Hugucius, ab ecclesia prestatur immunitas. r Sed revera cum ecclesia, sponsa Christi, sit undique ligata vinculis caritatis, infinitum plus respiceret ad delictum in quodlibet membrum eius quam ad sedacionem loci corporei. Et quia basilica infinitum minus diligitur quam membrum ecclesie, patet quod ubicunque terrarum quis peccat mortaliter, ecclesia debet plus ad peccatum respicere quam ad locum. Nam locus est impertinens offense ecclesie que non debet personas vel signa inanimata sic accipere, nisi forte locus sit per accidens principium noscendi et augendi gravedinem culpe. Quicunque, inquam, plus offenderunt in Deum, plus offendunt in totam sanctam matrem ecclesiam et quodlibet eius membrum ex vi communionis sanctorum et communicacionis membrorum diaboli, cum caput in quod primo delinquitur sit ubique. Ideo bene dicit glossa, III° Decretalium, quod illi qui in quamcunque ecclesiam deliquerint sunt ut sic indigni habere immunitatem cuiuscunque ecclesie: Illi, inquit, non habent immunitatem ab ecclesia, quia reddiderunt se indignos eius presidio, etsi fuerint stulti in culpa, sint sapientes in pena, ut dicit beatus Gregorius, sicut recitatur XXXVIIIª distinctione: Qui ea. Unde non est racio (sicut tangit predicta glossa) quare in istis quinque casibus excluduntur malefactores ab immunitate ecclesie, nisi quia ecclesia in istis casibus sensibilibus percipit indignitatem talium ex peccato notorio quam indignitatem [p. 226] aliorum qui aput Deum sunt magis indigni eo quod gravius peccaverunt. Unde leges civiles quas iura canonica non reprobant alios maleficos exprimunt ut homicidas, adulteros et raptores virginum quos collacio tercia docet extrahere; et idem indubie est de quocunque peccante mortaliter, quia omnis talis ut sic est inimicus Dei et sancte matris ecclesie, ut patet XXIIIª q. IVª (sicut recitavi superius in fine proximi capituli). Nam distancia loci non impedit quin peccans offendat in Deum et subtrahat ab ecclesia spirituale suffragium.

[ENGLISH]

## ¶2 · 226.12–226.29

> [p. 226] Ideo ubicunque sub divo quis magis offenderit, de tanto redditur magis inhabilis ad percipiendum defensionem ecclesie. Quod probatur tripliciter primo per hoc quod secundum regulam iuris per se notam frustra invocat legis auxilium qui offendit in legem, sed talis manens facinorosus offendit in legem ecclesie et totam sanctam matrem ecclesiam, ergo frustra invocat suffragium legum ecclesie, cum ex culpa sua per decretum sponsi ad ipsum redditur tam indignus. Item, secundum sentenciam Christi Matthei V°, 25, necesse est legem Christi esse adversariam peccatori et accusantem eum quamdiu sorduerit in peccato: Esto, inquit, consenciens adversario tuo cito, dum es in via cum illo. Cum ergo lex Christi mitissima non excusat sed accusat, non protegit sed prodit, omnes tales dum manserint primo legifero inimici, sequitur quod omnes leges ancillantes Christo non debent procurare defensionem hostis ecclesie in peccato.

[ENGLISH]

## ¶3 · 226.30–227.18

> [p. 226] Item, secundum beatum Gregorium (ut sepe repecii) privilegium omnino debet amittere qui sibi permissa abutitur potestate, sed omnis manens facinorosus intra locum refugii propter securitatem privilegii sibi permissa abutitur potestate, ergo debet ut sic carere loci suffragio. [p. 227] Est enim ad propositum dare duplex genus privilegii, scilicet privilegium quod residet in incolis loci talis et privilegium quod individuatur in persona fugitivi, cum quilibet talis dignus habere privilegii prioris suffragium, habet in se singulare privilegium a privilegio ecclesie exemplatum cuius proteccionem est dignus amittere dum ingratus fuerit matri sue. Et hic rogo primo professores iuris canonici considerare quomodo dictum vocatum privilegium nedum non fundatur in iure suo, sed manifeste repugnat eidem, cum lex ecclesie dicit quod in nullo dictorum quinque casuum fugitivus ad ecclesiam habebit refugium, sed privilegium pretensum dicit quod in quolibet eorum habebit refugium, et cum iste sensus videtur tam patenter repugnare iuri canonico, legi scripture et legi consciencie, verecundum et periculosum esset vocatum privilegium tam dampnabile et hereticum tam instanter defendere, veris privilegiis ecclesie pretermissis.

[ENGLISH]

## Loserth's side-notes (PD, verbatim; not our translation)

- 224.14: The 5th exception applies to the Westminster case.
- 225.5: The Church should have regard to the crime, not to the place where it was committed.
- 226.3: The civil law withdraws from sanctuary those guilty of homicide, adultery and rape.
- 226.12: All offenders are so far unfit to be shielded by the Church; a) because he who has broken a law cannot claim the benefit of it;
- 226.21: b) Christ's law is an adversary to the sinner;
- 226.30: c) in remaining wicked the refugee abuses the privilege and so forfeits it.
- 227.1: The privilege is twofold: to the inhabitants of the place and to the fugitive, who forfeits it, if he is ungrateful.

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 224: *fine* [R3]
  - 224: *Ecclesie* (italic; 15 is the line number) [R4]
  - 224: *XVIIª* [R4]
  - 224: *IVª* [R4]
  - 225: *quod* (Q 160ª are margin letter and folio mark) [R3]
  - 225: *III°* (20 is the line number) [R4]
  - 226: *aliorum* [R3]
  - 226: *∅* ('law' is the English side-note (The civil law)) [R4]
  - 226: *IVª* [R4]
  - 226: *tripliciter* (one unhyphenated printed word; main splits it tripli | citer (pos 101)) [THIN]
  - 226: *∅* (citer is the tail of tripliciter (pos 100); no separate word) [THIN]
  - 226: *primo* [THIN]
  - 226: *per* (a is the margin letter) [THIN]
  - 226: *Christi* [R3]
  - 226: *Christi* (25 is the line number) [R3]
  - 226: *facinorosus* (f with crossbar, tall) [NW]
  - 227: *individuatur* [R3]
  - 227: *quilibet* [R4]
  - 227: *privilegii* [R3]
  - 227: *prioris* (5 is the line number) [NW]
  - 226: *V°, 25,* (print has verse 25 at line end; following b is an alinea letter) [OVERRIDE-VERSE]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 224:
2. In codd. : frequcnlat. Corr. c decr. sup. mem. 12. occiderit sc. :
proximum suum el pcr insidias. 23. Jn codd.: ct deest. Addidi e
decr. supra mem.
if>. ib. cap. X. 28. Sec. Decr. sec. pars, causa XVII, q.
IV, c. IX.

p. 225:
5. A in marg. : Nota hic. i5. A in m.irg. : Conclnsio. 3o. per-
cipit; scil. plus percipit.
i. et 20. comp. glossam ad decret. Greg. IX, lib. III, tit. XLIX,
cap. X. De Hugutio vid. Savigny, Gesch. cles romischen Rechts
im Mittelalter, V, 425. 2G. Decr. prim. pars dist. XXXVIII, c. X.

p. 226:
3. A in marg.: Nota. 32. 33. B: contra locum.
5. Vide supra pag. 144 et seqq. 8. Vide supra pag. 201.

p. 227:
1. A B in marg. : Duplex privilegium. 8. A in marg. : Nota.
18. B: vires. 20. A in marg. : (black ink and red ink): Cap. nm.
28. B concedere.
28. Decr. II pars, causa XXV, q. I, c. XVI et Decr. Greg. IX,
Iib. V, tit. XXXIX, cap. XXXI.
```
