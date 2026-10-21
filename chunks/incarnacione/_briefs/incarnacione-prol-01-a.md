# Translation brief: incarnacione prol–01-a

You translate these 2 chunk(s) of Wyclif's *Tractatus de benedicta incarnacione* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-prol.md chunks/incarnacione/wyc-incarnacione-01-a.md` once and fix what it reports.
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

# TRANSLATOR CARD — one *De benedicta incarnacione* chunk

This card replaces reading CONVENTIONS, the pilot and Thakkar in full: it is their working core.
Adapted from `chunks/potestate-pape/CARD.md` (2026-10-21), for the first volume whose Latin was
established by blind transcription (B+) and the first early, purely scholastic one. Read it, then
`GLOSSARY.md`, then your scaffold (or your brief, which carries all three). Consult CONVENTIONS.md only
when the card sends you there. Work in `~/wyclif`. Wyclif is approached with **daggers drawn**: the most
recent English versions were "worse than useless" because of four error classes (below). Your English
must survive a hostile reader with the Latin open.

## Work lean (cost is per tool call: each call re-sends your whole context)

1. One call reading what you need (the brief, or CARD + GLOSSARY + scaffold).
2. **One** `bible.py` call with every scripture reference you need (it takes many refs).
3. Plates **only** for a Latin doubt the print plus apparatus cannot settle.
4. Write each finished chunk in **one** Write of the whole file (Latin blocks copied unchanged).
5. Lint once; fix; done. Draft in your head, not in the file.

## The volume

*Tractatus de benedicta incarnacione*, ed. Edward Harris (Wyclif Society, 1886), from the plates of
archive.org `latinworks03wycl` (**leaf = page + 39**; leaf images in `text/incarnacione/raw/leaves/`).
An **early** work: Harris (preface §II) puts it before 1367, in the first years of Wyclif's doctorate
(1363–67), with cross-references to *De universalibus*; the Oriel manuscript's medieval catalogue calls
it *super sententias*, and it sits in a volume of Sentences commentaries. It is the surviving text
closest to Wyclif's lost lectures on book III of the *Sentences*: **the theologian of the schools, not
yet the reformer**. No pope, no endowment, no friars: the whole treatise is the metaphysics of the
incarnation argued against the "modern doctors" (Ockham and the *moderni*), in the forms of the
disputation. A prologue and thirteen chapters; the prologue (pp. 1–2) describes each chapter in one
sentence, and Harris repeats that sentence at the chapter's head (below).

**Sigla** (Harris, preface §III): **A** Vienna 384 (the base of Beer's collation; *Prologus magistri
Johannis de Incarnacione* in red); **B** Vienna 404; **C** Vienna 387 (A, B, C one recension from a common
source, Beer); **O** Oriel College, Oxford, xv (c. 1400, English, two columns; Harris: "the best, as
probably the oldest", nearer C than A or B); **M** London, BL Royal 7 B. iii (15th c.; not a copy but
a **summary** made from a manuscript: the main course of the argument with the illustrations and
authorities left out; collated by F. D. Matthew). Cite variants with these sigla. Harris's text is
**eclectic**: "the best reading" chosen from all five, every rejected reading of A B C O at the foot
(the countless *ille/iste* swaps and trivial word-order variants excepted); the manuscripts' spelling
kept "even when manifestly incorrect" (*methaphisica*, *anthitesis*, *dyabolus*). The chapter breaks are
Wyclif's (the prologue); **the paragraphs are Harris's own** ("on my own responsibility, often a matter
of doubt": only chapters begin a new line in O).

**The page foot** (in your brief as "apparatus", by page) is keyed by **footnote figures**, which stand
in the Latin as superscripts on the word before them (`Prelibato¹ tractatu`): `1 Litera initialis (P) om.
A B C. 3 mesterium O.` Read it for sense, not letter by letter (OCR). The figures are the editor's, not
text: **never carry them into the English**; cite a variant by its page.line.

**Harris's margin and brackets.** Harris prints a running English abstract of the whole treatise down
the margin (≈21,500 words). It is **not reproduced** in this edition (Wilson, 2026-10-21): the headnote
says so once, and no chunk carries side-notes. At each chapter head he prints, in square brackets, the
prologue's Latin sentence for that chapter followed by his own English summary. The scaffold gives that
bracket as its own ¶ block (marked by a comment): **translate the Latin sentence only**, in square
brackets, worded as the prologue renders it; **drop Harris's English** (it is the editor's, like the
margin). Write no note on the bracket.

## The job

The Latin in your scaffold is **established and frozen** (blind transcription, checked word by word
against Fordham and a five-scan vote; residue read on the plate). Fill `[TITLE]` (short, lower case:
"that Christ is a creature: the sense of the fathers"), each `[ENGLISH]`, the notes and the transcription
notes; set `status: translated`; lint; report.

- **Headings:** keep `## ¶k · range` exactly. **Never change a range; never split a paragraph.**
- **Never alter the Latin.** A transcription error you find (a stray mark, a broken word) is REPORTED,
  never repaired in your file: the coordinator repairs the transcription (`text/incarnacione/bt/pNNN.txt`)
  and refreshes the chunk's Latin. A word that looks wrong: read the apparatus for that line first;
  then, if still doubtful, the plate (`text/incarnacione/raw/leaves/nLEAF.jpg`, LEAF = page + 39
  padded to four digits: p. 3 = `n0042.jpg`). A variant that gives the sense → translate it + **T**
  note citing the siglum; a compelling emendation → translate it + **T** note "(our emendation)";
  neither → translate the print and flag it. Never smooth nonsense into sense. **Harris's printed text
  governs** (the standing rule of this edition): translate it unless it will not construe; a manuscript
  reading is chosen only then, and a single manuscript's reading never outweighs the print without
  cause; every departure gets a T note giving both readings. ⚠ Harris is a 19th-century editor of a
  14th-century schoolman: where the print is grammatical but the argument fails, suspect the editor's
  choice among variants before Wyclif's logic, and read the apparatus.
- **English layout:** `[N]` at the same word as `[p. N]` in the Latin (the chunk's first `[p. N]` is
  implicit). Supplied words in `[brackets]`, sparingly. **Quotations** in quotation marks. Your brief
  carries Harris's **italic runs** per page (from the scan's OCR, rough; his quotation bounds and the
  words he took for titles or Greek). They are the editor's judgement, not the manuscript's: follow them
  by default, depart where the source shows otherwise (say so in a note). Reviews do not check
  quotation bounds against the italics. Italicised scripture inside indirect speech is quoted too; where
  quoting would garble the sentence, leave it unquoted and give the reference in an **S** note.
- **Formulae of the disputation** (GLOSSARY §C, ruled 2026-10-01), rendered the same way throughout:
  *instatur* "it is objected" · *obicitur* "it is objected" · *arguitur* "it is argued" (with *per*:
  GLOSSARY) · *dicitur* "it is said" (in an answer: "the answer is") · *respondetur* "the reply is" ·
  *conclusio* "conclusion" · *antecedens / consequens* "antecedent / consequent" · *consequencia*
  "inference", ⛔ never "consequence" · *patet* "it is clear" · *supponitur* "it is supposed" (a premiss
  laid down) · *probatur* "proof:" or "it is proved" · *confirmatur* "this is confirmed".

## The four error classes (Thakkar) — check every sentence

1. **Terms:** GLOSSARY.md governs, one term one rendering. Tag the **first occurrence in the chunk**
   of every §A–C term: `[quiddity]{g:quiditas}`. The key must exist in GLOSSARY.md. A term that looks
   technical but has no row: render it sensibly, untagged, and propose it in your report.
   **CONTEXTUAL** rows hold two senses English splits: choose by context and write a **C** note at
   the first occurrence in the chunk and wherever it leans to the other sense (the dikaiosune rule,
   CONVENTIONS §6).
   ⚠ **This volume's terms are the metaphysics of the incarnation**, and the GLOSSARY, built on the
   political works, has few of them. The rulings that exist: *ens / esse / essencia* "a being / being /
   essence" (⚠ *esse* is ambiguous, note when it matters) · *universale* "universal" · *simpliciter /
   secundum quid* "without qualification / in a certain respect" (⛔ always opposable) · *differencia*
   "difference" · *subiectum* "subject" · *predicamentum* "category" · *racio* (against *substancia*)
   "aspect" · *successivum / permanens* "successive / permanent entity" · *ampliacio* "ampliation" ·
   *sumitur pro* "is taken for" · *dicitur multipliciter* "is said in many ways" · *quiditas* "quiddity".
   For the rest, **render consistently within your brief and PROPOSE the row** (the coordinator rules
   between briefs; the FIRST chunk's proposals are ruled by Wilson). Expect at least: *humanitas*
   (humanity; the human nature — the word on which the first chapter turns: *humanitas sit Christus*),
   *natura*, *persona*, *suppositum*, *ypostasis*, *res communis* (the common thing), *individuum*,
   *singulare*, *assumere / assumpcio* (of the nature: assume / assumption — ⚠ GLOSSARY §C has
   *assumptum* "the assumption" for the logical premiss: keep the two apart with a C note where the
   logical sense occurs), *unire / unio*, *communicacio ydiomatum*, *materia prima*, *forma*,
   *compositum*, *triduum* (the three days in the tomb: *in triduo*), *Verbum* (the Word), *deitas*,
   *creatura* (creature: never "creation" for the created thing), *incommunicans / incommunicantes*
   (of the three natures that do not communicate), *moderni doctores* (the modern doctors), *sancti*
   (the saints, i.e. the fathers), *symbolum* (the creed). Render *homo* "man" (the medieval *homo*
   that *Christus est homo* needs; never "human being" in the formulae).
   Key rulings carried from the political works that still apply: *ecclesia* church (**lower-case**)
   · *caritas* charity · *viator* wayfarer · *ex fide* as faith teaches · *sentencia* teaching ·
   *opinio* opinion · *evidencia* evidence · *fides* faith.
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
   | vero (continuative) | and; but (adversative) | "now", "truly" |
   | verumtamen | nevertheless | "but truly" |
   | unde | hence, so | "whence" (archaic), "where" |
   | per idem | by the same token | "in the same way" |
   | ymmo | indeed, rather (correcting upward) | (omitted) |
   | patet; constat | it is clear; it is evident | |

   "Now" is reserved for the minor premiss, or the step that brings a new premiss to bear. An *autem*
   that only extends the same step is "and". ⚠ The commonest error in *De ecclesia* (close-out, ~50 of
   69 connective fixes): a *sed* that brings the minor premiss of a syllogism closed by *ergo / ideo /
   igitur* rendered "but". Before writing "but" for a *sed*, look ahead for the *ergo*: if one follows,
   it is "now". This volume is syllogism on syllogism: the rule will be tested in every paragraph.
3. **Ordinary words with a medieval sense:** GLOSSARY §D; look up any word whose classical and
   Wyclifite senses may differ, and propose additions.
4. **Syntax:** construe before rendering (main verb, subject, what every relative and genitive
   hangs on). Keep quantifier order where it is meaning (*omnis natura*, *nulla creatura*). Keep
   Wyclif's long periods where English tolerates them. **A doubtful construal is never chosen
   silently:** translate the likelier reading and write a **C** note giving the alternative.
   ⚠ **Predication is the matter here, not just the form.** *Christus est creatura*, *humanitas est
   Christus*, *Verbum est homo*: Wyclif argues about what is predicated of what, with supposition and
   identity in play. Keep subject and predicate in his order, keep *est* as "is" (never "exists" unless
   the Latin is *existit* or the sense is plainly existential, with a C note), and keep *secundum* ("as
   to", "according to") visible: *secundum deitatem / humanitatem* "as to his deity / humanity".

## Scripture

`python3 scripts/w3/bible.py "Ioh 10:30"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering) or
`python3 scripts/w3/bible.py --find "ego et Pater unum sumus"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and write
an **S** note giving the Vulgate. Modern references in the English (John 10:30). The chapter numbers
are Wyclif's, the verse numbers Harris's margin references where he gives them (the headnote says so once).

## Notes

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter:
  **T** text · **C** construal · **G** glossary (passage-specific only; otherwise a tag) · **S** source ·
  **R** reception/context (e.g. a manuscript's marginal note that Harris prints, CONVENTIONS §4; O's
  reader marks *nota bonam rationem*).
- **Density: about one note per 70–100 Latin words**, fewer where the text is plain. Short, factual,
  says what the Latin does and stops. No modern theology, no evaluation.
- **Every identification** other than scripture checked with bible.py gets a ledger row in your
  report with a status: `editor` (Harris's source reference at the page foot or in the margin),
  `to-verify` (from memory: every patristic or scholastic identification you did not read in this
  session), `verified` (you read the source text this session: say where; local PL at
  `~/patrologia/sources/pl/tei/`). ⛔ Never pass memory off as verified. Id `P<chunk>-<n>` (`P01a-1`),
  cited in the note: "(LEDGER P01a-1)". The *sancti* cited are above all Augustine (*De Trinitate*,
  *Enchiridion*, *De fide et symbolo*), Anselm (*Cur Deus homo*, *De incarnatione Verbi*), Damascene,
  Hilary, the Lombard (*Sent.* III) and Grosseteste; the *moderni* are usually unnamed.

## Model of register

`pilots/wyc-ecclesia-01a.md` (De ecclesia pp. 1–5) is a reviewed model of register and note style:
read it for that only (it predates some GLOSSARY rulings; **GLOSSARY governs**). **Chunk `prol`**
carries the `## Headnote` (CONVENTIONS §12 order: occasion, text, the work's move, where it is
answered; date, editor, sigla, the margin abstract not reproduced, the bracketed arguments), each
unverified claim marked `[verify]`.

## Side-notes

None in this volume (above). Nothing to place, nothing to report.

## Finish

1. `status: translated` in the front matter (nothing else changes there).
2. `.venv/bin/python scripts/w3/lint.py chunks/incarnacione/<your chunk>.md` until clean.
3. The four-class check above, sentence by sentence.
4. ⛔ Edit **only your chunk(s)**. No git, no other files. Everything shared goes in your report.

## Report (≤ 200 words per chunk, exactly these heads)

- **Chunk:** id, Latin words, notes.
- **Ledger rows:** in LEDGER.md's table format `| id | chunk / note | claim | status | how / next step |`.
- **Glossary proposals:** Latin · proposed English · where · why.
- **Latin doubts:** page.line · printed · suspicion · settled on the plate?

## Glossary (the 182 rows these chunks use; the full file is GLOSSARY.md)

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
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| symbolum | creed | *Utrumque simbolum* = both creeds, Apostles' and Nicene (T. p. 368). |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | condition | A person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
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
| tollere (instanciam, argumentum) | to dispose of, demolish | T. p. 373. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| decimacio | tithing | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.26). |
| decimantes | tithe-payers | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 359.24). |
| involucrum | wrapping | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 357.9). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| suadere | make the case | To persuade, not to prove. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.2). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk prol: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-prol.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-prol
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "1.3–2.32"
divisions: "prologus (heading 'Johannis Wyclif Tractatus de Benedicta Incarnacione. Prologus.' at 1.0)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "321 words; 314 confirmed by Fordham or the vote; 5 runs stood by rule (both witnesses garbled); 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n40–n41 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, prologue: [TITLE]

## Headnote

[HEADNOTE: see pilots/wyc-ecclesia-01a.md]

## ¶1 · 1.3–1.13

> [p. 1] Prelibato¹ tractatu De Anima qui introductorius est propter incarnacionis misterium² cognoscendum, restat tractatum De Benedicta Incarnacione operosius aggredi cum diligencia,³ reverencia, et timore. Cum diligencia,³ quia nulla materia est intellectui difficilior, et per consequens oportet mentem dare operam plus attentam: cum reverencia, quia nulla⁴ materia theologica est affectui preciosior, cum sub uno comprehendit involucro tocius creacionis⁵ et recreacionis venerabile sacramentum: et cum timore, quia, sicut in nulla materia quis compendiosius promeretur, sic nullibi facilius aut periculosius aberratur.⁶

[ENGLISH]

## ¶2 · 1.14–1.14

> [p. 1] Dividitur autem tractatus iste⁷ in⁸ 13 capitula.

[ENGLISH]

## ¶3 · 1.15–1.18

> [p. 1] Quorum primum, declarando ex testimoniis sanctorum quod humanitas sit Christus et per consequens creatura, dat sensum dictorum⁹ in scripturis et in¹⁰ symbolo¹¹ que videntur huic opposita.

[ENGLISH]

## ¶4 · 1.19–1.20

> [p. 1] Secundum capitulum¹² declarat quomodo ista sentencia discrepat ab heresi Arriana.

[ENGLISH]

## ¶5 · 1.21–1.22

> [p. 1] Tertium capitulum ostendit quod Christus fuit homo in triduo et obicit multipliciter et dissolvit.

[ENGLISH]

## ¶6 · 2.1–2.2

> [p. 2] Quartum capitulum iuxta ponit sentencias modernorum doctorum, ut veritas plus lucescat.

[ENGLISH]

## ¶7 · 2.3–2.5

> [p. 2] Quintum capitulum, supponendo quod Verbum non dimisit humanitatem pro triduo, probat¹ quod nec potuit dimittere naturam quam assumpsit.

[ENGLISH]

## ¶8 · 2.5–2.8

> [p. 2] Sextum capitulum ostendit quod Christus sit univoce homo cum aliis hominibus;² et respondendo objectibus³ declarat quod Christus est, secundum multorum doctorum⁴ testimonia,⁵ creatura.

[ENGLISH]

## ¶9 · 2.9–2.11

> [p. 2] Septimum capitulum declarando Christi mobilitatem explanat sensum scripture multis ambiguum,⁶ quomodo sapiencia summe mobilis⁷ sit habitu inventa ut homo.

[ENGLISH]

## ¶10 · 2.12–2.13

> [p. 2] Capitulum octavum obicit tripliciter contra ydemptitatem specificam⁸ Christi cum aliis et⁹ dissolvit.

[ENGLISH]

## ¶11 · 2.14–2.17

> [p. 2] Capitulum nonum epilogat posicionem de humanitate; et,¹⁰ narrando tres radices causantes modernorum discrepancias, dissolvit tres objectus eorum per¹¹ ordinem.

[ENGLISH]

## ¶12 · 2.18–2.20

> [p. 2] Capitulum decimum suadet¹² 12 evidenciis quod humanitas assumpta sit Christus; et hoc¹³ roborat doctorum testimoniis et exemplis.

[ENGLISH]

## ¶13 · 2.21–2.24

> [p. 2] Capitulum undecimum solvit instancias quibus moderniores doctores videntur fulcire suam sentenciam, recitando decem ludicra que concedentes possibilitatem dimissionis annuunt consequenter.

[ENGLISH]

## ¶14 · 2.25–2.28

> [p. 2] Capitulum duodecimum recitando opiniones varias de assumpcione creature declarat quod, si assumeret multas humanitates, foret¹⁴ multi homines, sicut dictat sentencia sancti Thome.

[ENGLISH]

## ¶15 · 2.29–2.32

> [p. 2] Capitulum tredecimum confirmat¹⁵ aliorum sentencias quod¹⁵ tunc nec foret unus homo nec multi homines, sed¹⁶ et unicus atque multi; et sic concordat modernorum sentencias cum antiquis.¹⁷

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 1: *opposita.* (print = bt (word on next line)) [BT-ONLY]
  - 2: *homo cum aliis hominibus;* (print = bt) [SUB]
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 1:
Prologus. Codex A. habet colore rubro superscriptum : Prologus magistri
de incarnacione.
Codex B. Incipit tractatus de incarnacione Mgi. Jo. Wykleph. Prologus.
Codex C. manu recentiore : De Benedicta Incarnatione Jo. Wiclif.
Codex 0. in ipso textu nullum titulum habet, sed in exteriore angulo
uniuscujusque folii haec addiia sunt : W. de incarnacione Vbi.
1 Litera initialis (P) om. A B C. 3 mesterium 0. 3 dilligencia B.
5 creacionis om. 0. 6 oberratur A B C. 7 ille C. 8 in om. 0. 9 doctorum
10 in om. 0 C. 11 simbolo 0. 12 capitolum A B C ut fere

p. 2:
0. 2 hominibus om. 0. 3 objectionibus 0. 4 doctorum om. C.
A B. 6 anibigue 0. 7 mobilis om. C. 8 specificam om. C.
'o ut C. " in 0. 12 swadet B C. 13 hoc om. B 0.
altera manu C. 15 -15 dicta aliorum quod AB C. 16 set 0, et sie saepe.
A.addit haec rubro colore: Explicit prologus. Incipit de incarnacione capi-
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 1: De Anima | Benedieta Inearnacione | in ipso textu nullum titulum habet, sed in exteriore angulo ad summum uniuscujusque folii haec addiia sunt: | ut fere semper. | Third Report of the Executive Committee, for | The Societtf s Books for | The Funds ancl Position of the Wyclif Society on Bec. | ancl now. Books preparing in Eclitors' hancls. Manuscripts copiecl, | The Bools for | Thanks to Helpers, | Hon. Sec.'s Cash Account, | List of other Societies, | De Civili Dominio, | De Ecclesia, | Dialogus, sive Speculum Militantis Ecclesiae. | De Composicione Hominis,
p. 2: The Society'* Books for | De Dominio Civili, | De Ecclesia | De Ecclesia. | Speculum Ecclesiae Ifilitantis
```

---

## Chunk 01-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-01-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-01-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "3.0–7.12"
divisions: "cap. 1 (heading 'Cap. I.' at 3.0); part 1 of 3, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1206 words; 1204 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n42–n46 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 1, part 1: [TITLE]

## ¶1 · 3.0–3.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 3] [Declarando ex testimoniis sanctorum quod humanitas sit Christus et per consequens creatura, dat sensum dictorum in scripturis et in symbolo que videntur huic opposita. Discussion as to the sense in which it is catholic truth to say: Christ is a creature.]

[ENGLISH]

## ¶2 · 3.2–3.20

> [p. 3] Quia autem spiritualiter viantibus in discendo necesse est primo removere prohibens disciplinam; ac in scriptura sacra et sacris¹ doctoribus de Christo¹ sunt multa scripta² que videntur inperitis contraria; ideo pro solucione eorum in primis supponitur³ quod Christus sit tres nature incommunicantes: scilicet, deitas, corpus, et anima. Patet sic. Christus est Deus et homo perfectus, ut ex fide supponitur: omnis Deus est deitas: omnis homo perfectus est tam corpus quam anima: ergo conclusio. Confirmatur per Augustinum super Ioh. Ome. 47.⁴' Si, inquit, caro animam posuit, quomodo Christus animam posuit? numquid⁵ caro Christus?' Et respondet:' Ita plane et caro Christus et anima Christus et Verbum Christus: nec tamen hec tria⁶ tres Christi, sed unus Christus. Hominem interroga et de eo fac gradum⁷ ad ea que super te sunt, et⁸ si nondum intelligenda, saltem credenda. Quomodo enim unus homo anima et corpus? sic unus Christus Verbum et homo.' Nec credo quod nos ignari ad tantum desipimus quod dicamus hunc sanctum tam crebro sentenciam hereticam inculcare.

[ENGLISH]

## ¶3 · 3.21–4.5

> [p. 3] Ex istis plane⁹ sequitur quod Christus est creatura. Nam omnis natura corporea vel spiritus creatus est creatura: Christus est tam natura corporea quam spiritus creatus, cum sit homo perfectus: ergo Christus est creatura. Sed quia sunt multe scripture que videntur isti sentencie repugnare, ut recitat Magister 3° Sentenciarum Dist. 2ᵃ, ideo ut omnes communiter¹⁰ dissolvantur¹¹ sub uno epilogo; dicitur quod omnes recte intelligentes Christum non esse creaturam [p. 4] concipiunt quod Christus secundum deitatem non est creatura: sicut omnes recte concipientes¹ Christum esse creaturam concipiunt eum secundum humanitatem esse creaturam. Et ista² glosa, si non fallor, satisfacit sub communi involucro omnibus auctoribus in oppositum allegandis.

[ENGLISH]

## ¶4 · 4.6–4.27

> [p. 4] Sed ut illa³ materia particularius denudetur, oportet primo fundare sentenciam huius glose. Et occurrit michi⁴ primo disputacio Augustini ad Felicianum hereticum; ubi post duplicem nativitatem Christi et duplicem eius substanciam vel naturam declaratam tam ex scriptura sacra quam similitudine naturali, sic⁵ ait inter cetera: ‘Non⁶ alius homo corpus, alius animus, quamvis aliud corpus, aliud animus; unus tamen atque idem homo et corpus dicitur et animus. Sic, inquit, in mediatore⁷ Dei et hominum: aliud Dei filius, aliud hominis filius, unus tamen Christus Iesus ex utroque fit: aliud, inquam, pro discrecione⁸ substancie, non⁶ alius pro unitate persone.’ Et per hoc solvit scripturas de Christo,⁹ quarum alique locuntur de ipso secundum deitatem et alie secundum humanitatem. Et posiciones¹⁰ secundum habitudinem¹¹ concedit simpliciter; unde subdit: ‘nec ideo dicimus non pacientem quia ipse faciebat celos,¹² nec ideo non facientem quia non alius tollerabat. Nam si dominice incarnacionis misterium consideremus,¹³ idem sibi in hac humilitate et auctor¹⁴ et opus est.’ Unde et post declaratur esse possibile quod eadem persona simul et semel sed secundum diversam naturam mortem paciatur et vivat, sicut idem sol secundum diversos situs simul tempore diem causat et noctem.

[ENGLISH]

## ¶5 · 4.28–5.10

> [p. 4] Secundum testimonium Augustini est in Ep. 12¹⁵ ad Pascencium et in Epistula 40 ad Dardanum ubi cap. 7° ita inquit: ‘Cum enim Christus sit Deus et homo, Deus utique est; unde dicit: “Ego et Pater unum sumus” Ioh. 10: homo autem; unde dicit: “Pater maior me est,” Ioh. 14: idemque Filius Dei unigenitus a Patre, et filius hominis ex semine David¹⁶ secundum carnem est. Utrumque in illo considerandum [p. 5] est cum loquimur vel cum scriptura de ipso loquitur: et quid et¹ secundum quid de illo dicitur intuendum est. Nam sicut unus homo est anima rationalis² et caro, sic unus Christus est Verbum et homo. Proinde quod ad Verbum attinet, creator est Christus; “omnia enim per ipsum facta sunt;” quod vero³ ad hominem attinet, Christus creatus est; “factus enim est⁴ ex semine David secundum carnem,” et “in similitudinem hominum⁵ factus est.”’ Et post diffuse prosequitur declarando que scripture sibi conveniunt secundum deitatem et que secundum humanitatem.

[ENGLISH]

## ¶6 · 5.11–5.26

> [p. 5] Nec est maior color quod sit creator quia secundum deitatem, quin per idem sit creatura quia secundum humanitatem, specialiter cum sit illa completa humanitas. Quia certum est ex testimonio⁶ Augustini ad Felicianum quod totus homo assumptus passus est mortem, sicut sola caro iacuit in sepulcro, ut testatur Augustinus Ome. 47 ubi super: ‘Confiteris,⁷ inquit, in illum⁷ Christum credere qui est mortuus et sepultus: ergo et sepultum esse Christum non negas. Et tamen sola caro sepulta est: si enim erat ibi anima, non erat mortuus: si autem vera mors erat, ut vera sit eius resurreccio,⁸ sine anima erat in sepulcro, et tamen sepultus est Christus. Ergo Christus erat etiam sine anima caro, quia non erat sepulta nisi caro.’ Unde paulo ante ipse Christus dictus est sola caro. ‘Quomodo,⁹ inquit, probas? Audeo dicere: sola caro⁹ Christi dictus est Christus;’ et probatur¹⁰ per hoc, quod Christus iacuit in sepulcro.¹¹

[ENGLISH]

## ¶7 · 5.27–6.29

> [p. 5] Tercium testimonium Augustini est Ome. 8. super illud Ioh. 2°. ‘Quid michi et tibi, mulier? nondum venit hora mea.’ ‘Dominus,¹² inquit, Iesus Christus Deus erat et homo: secundum quod Deus erat,¹³ matrem non habebat: secundum quod homo erat, matrem habebat. Mater ergo erat carnis, mater humanitatis, mater infirmitatis quam suscepit propter nos. Miraculum autem quod facturus erat [p. 6] secundum¹ deitatem facturus erat et¹ non secundum infirmitatem;² secundum quod Deus erat, non secundum quod infirmus natus erat: sed “infirmum³ Dei forcius hominibus.” Miraculum autem⁴ exigebat mater: at⁵ ille tanquam non cognosceret⁶ viscera humana operaturus facta divina, tanquam diceret; “quod de me fecit miraculum non tu⁷ genuisti: sed quia tu⁸ genuisti infirmitatem meam, tunc te⁹ cognoscam, cum ipsa infirmitas pendebit in cruce:” hoc est enim, “nondum venit hora mea.” Unde et commemorans illam nominacionem extraneam “mulierem” qua¹⁰ vocavit matrem in nupciis Galilee, pendens in cruce dixit matri: “Mulier, ecce filius tuus!” Ioh. 19. Non quod Christus aliquando non cognoscit matrem; in predestinacione, inquit Augustinus, noverat matrem, eciam¹¹ antequam ipse Deus eam crearet, de qua ipse homo crearetur: tunc tamen in effectu¹² agnovit, quando illud quod peperit moriebatur.¹³ Non¹⁴ enim moriebatur per quod facta erat Maria, sed moriebatur¹⁵ quod factum erat ex Maria: non¹⁴ moriebatur eternitas divinitatis, sed moriebatur infirmitas carnis: filius itaque virginis secundum quod creator celi et terre et dominus mundi creator fuit Marie, Deus¹⁶ fuit Marie; secundum autem quod dictum est “factum ex muliere, factum sub lege:” ipse enim¹⁷ dominus Marie est filius Marie; ipse creator Marie creatus ex Maria. Noli mirari: nam ideo David est filius, quia Marie est filius. Audi apostolum dicentem “qui factus est ei¹⁸ ex semine David secundum carnem”: audi eum et dominum David, ‘dixit dominus domino¹⁹ meo: “sede a dextris meis.” Unde¹⁹ et ipse Iesus²⁰ hoc proposuit Iudeis et eos inde convicit.’

[ENGLISH]

## ¶8 · 6.30–7.12

> [p. 6] Et isti regule innititur Augustinus utrobique, ut in libris contra Maximinianum; sicut Ieronimus in Epistula ad Paulam [p. 7] et Eustochium, et alii probabiles doctores. Unde libro primo contra Maximinianum sic loquitur Augustinus: ‘Dicis Patrem infactum quasi Filius factus sit, per quem facta sunt omnia. Scito factum esse Filium sed in¹ forma servi, qui in forma¹ Dei usque adeo non est factus, ut per illum facta sunt omnia.’ Unde et² infra 2° dicit quod Deus Pater non creatorem creavit, sed creatorem³ constituit iuxta illud Psⁱ. 8ⁱ. quod⁴ secundum apostolum et secundum Augustinum⁴ ad litteram verificatur de Christo: ‘minuisti eum⁵ paulo minus ab angelis, gloria et honore coronasti eum, Domine,⁶ et constituisti eum super opera manuum tuarum: omnia subiecisti sub pedibus.’⁷

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference e.o. John x. 30, (4.31); reference 5 John i. 3. (5.5); reference l Cor. i. 25. (6.3); reference Jobn xix. 26. (6.12); reference Rom. i. [A75d] (6.26); reference Ps. cx. (6.27); reference Matt.xxii. 42-45. (6.29); reference Ps. vni. 5, 6. Heb. ii. 7. (7.7).
````

### Apparatus (editor's page-foot notes, OCR; line numbers are the printed page's)

```
p. 3:
spiritualiter viantibus in discendo necesse est The difficuities
prohibens disciplinam ; ac in scriptura sacra apparent contra-
doctoribus de Christo1 sunt multa scripta2 que Scripture oon-
£ 1 cerning Christ
inperitis contraria ; ideo pro solucione eorum in ™J be remoyed
by remembenng
supponitur 3 quod Christus sit tres nature incommuni- JJ ^hrist S*twE-
deitas, corpus, et anima. Patet sic. Christus JjjJjJ- ^ Js
homo perfectus, ut ex fide supponitur : omnis of Tod/and fou^
deitas : omnis | homo perfectus est tam corpus quam cifrist three ' r.a^
conclusio. Confirmatur per Augustinum super bo^and^soui*1;
47. 4 1 Si, inquit, caro animam posuit, quomodo oLn^teaches!1116
animam posuit ? numquid5 caro Christus?' Et re-
Ita plane et caro Christus et anima Christus et
Christus : nec tamen hec tria 6 tres Christi, sed unus
Hominem interroga et de eo fac gradum7 ad ea
te sunt, et 8 si nondum intelligenda, saltem
Quomodo enim unus homo anima et corpus ? sic
Yerbum et homo.' Nec credo quod nos ignari
desipimus quod dicamus hunc sanctum tam crebro
hereticam inculcare.
plane9 sequitur quod Christus est creatura. Nam Christ.beingper-
corporea vel spiritus creatus est creatura : body and soui, is
tam natura corporea quam spmtus creatus, cum
perfectus : ergo Christus est creatura. Sed quia
scripture que videntur isti sentencie repugnare,
Magister 3° Sentenciarum Dist. 2a, ideo ut Peter Lombard
commumter 10 dissolvantur11 sub uno epilogo ; dicitur in which Christ
recte intelligentes Christum non esse creaturam not in his divine
doctoribus de Christo om. A B C. 2 scriptura 0.
oportet ABC. 4 4 ABC; 41 0. 5 numqnara C. 6 tria hec 0.
B ; gradum fac C ; gratiam 0. 8 et si dum non 0. 9 palam 0.
B. 11 dissolva- ad finem lineae -tur om. 0.

p. 4:
Davicl 16 secundum carnem est. U trumque m lllo consicleran-
O. 2 illa A B C ; 1 ille ' et * iste ' variantur saepissime in codd.
0. 4 michi om. 0. 5 sicut B. 6 est add. B. 7 meclitatore 0.
0. 9 de Christo om. 0. 10 ppcones A; pciones B ; p°.e.s C.
secundum liumanitatem 0. 12 celos om. C 0. la consideres A B C.

p. 5:
1 et add. M. 2 ratio 0. 3 enim 0. 4 enim est om. A B C. 5
6 testimoniis A B C. 7-7 confitens, inquit, unum A B C. 8
9-9 quomodo . . . caro om. 0. 10 probatur om. AB C. 11
12 deus A B C. 13 deus erat erat et homo C.

p. 6:
B C. 2 sed secundum A B C. 3 infirmius B. 4 autem om. A B.
6 agnosceret A B C ; cognoscit 0. 7 tu om. 0. 8 tunc B.
B C. 10 mulieris quam 0 ; mulierem quia B. 11 et A B C.
B C. 13 mirabatur A B C.
enim moriebatur per factum erat ex Maria AB; non enim moriebatur per
erat ex Maria C. 15 per add. 0. 16 dominus 0.
0. ltj ei om. 0. 19-19 domino etc. Unde B. 20 Christus 0.

p. 7:
1 informam servi qui formam Dei 0. 2 et om. 0. 3 creaturam
4-4 servi appellacionem (applfn) Augustinus ad 0. 5 eum om. 0. 6
7 petibus 0. 8 sed et C. 9 cum aliis hominibus
10 sine " alta" philosophia in marg. illa man. pr. A ; sine alta la philosophia
la philosophia C 0 ; an prima legendnm? 11 Augustinus om. 0.
13-13 copulans utraque et solita AB C ; copulam utramque naturam solita
u-14 Ille ergo sine seminibus temperatus est semina A B C.
15 ista A B C ; illa 0 ; ulla Aug. ut nensus poscit.
16 seclorum 0. 17 homo 0.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 3: \Declarando ex testimoniis sanctorum quod humanitas sit Christus et per consequens creatura, dat sensum dictorum in scripturis et in symbolo que videntur huic opposita. Discussion as to the sense in ivhich it is catholic truth to say : Christ is a creature.'] | De Civili Dominio. | De Ecclesia | De Composicione Hominis, | De Benedicta Incarnacione | De Benedicta Incarnacione | De Composicione Hominis
p. 4: Fath^areme,' | My Father | greater than i: | The booJcs for | De Benedicta Incarnacione,
p. 5: Woman, what | have itodowirh ' | tnee 1 mine hour | is ' not y et come: | Thanks to Helpers* | Sermones Mixti
p. 6: cfc S&&wffi<p» | Yice-Presidents. | Executive Committee. | BZonorary Secreiary. | Zocal Eonorary Secretaries. | Wales (North) — | JHiddlesex (West) | Torkshire (East Biding)—The | Torkshire (West Riding)—Rev. | The Societifs Publications for | Latin Polemical Works, | The Societfs Publications (£\ \s.) for | JDe Civili Dominio, | De Composicione Hominis, | The Society's Publications for | De Ecclesia | sDialogus, sive Speculum Ecclesia Militantis, | The Societifs Publications for | witt be: — | De Benedicta Incarnacione,
p. 7: x iJe Anima, | De Anima
```
