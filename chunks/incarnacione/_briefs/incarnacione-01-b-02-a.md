# Translation brief: incarnacione 01-b–02-a

You translate these 3 chunk(s) of Wyclif's *Tractatus de benedicta incarnacione* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-01-b.md chunks/incarnacione/wyc-incarnacione-01-c.md chunks/incarnacione/wyc-incarnacione-02-a.md` once and fix what it reports.
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
A B C. 3 mesterium O.` From 01-b on it is **read from the plate** (`text/incarnacione/foot/`, 2026-10-22),
not OCR: trust its letters; a `[?]` or `CHECK:` line in it is a doubt to settle on the plate foot. The
figures are the editor's, not text: **never carry them into the English**; cite a variant by its page.line.
**Apparatus discipline** (first-chunk review, 2026-10-22: three of its four errors):
(i) **match a variant to its figure** in the Latin before citing it (a figure *n* belongs to the word
before ^n, not to a nearby word that resembles the variant); (ii) the foot's abbreviations are
**rejected readings, to be expanded** in the note (*ppcones* = *proposiciones*), never "beyond certain
reading"; (iii) where Harris prints **one manuscript (usually O, or M) against A B C** on a word the
argument turns on, write a **T** note giving both, even though the print is kept; (iv) a reading the
English follows that is not the print's is a departure: T note, always.

**Harris's margin and brackets.** Harris prints a running English abstract of the whole treatise down
the margin (≈21,500 words). It is **not reproduced** in this edition (Wilson, 2026-10-21): the headnote
says so once, and no chunk carries side-notes. At each chapter head he prints, in square brackets, the
prologue's Latin sentence for that chapter followed by his own English summary. The scaffold gives that
bracket as its own ¶ block (marked by a comment): **translate the Latin sentence only**, in square
brackets, worded as the prologue renders it, with **the chapter as subject ("it")**, not Wyclif ("he");
**drop Harris's English** (it is the editor's, like the margin). Its terms are tagged like any other
(a first occurrence in the bracket is the chunk's first occurrence). Write no note on the bracket.

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
  implicit). Supplied words in `[brackets]`, sparingly, ⛔ **never in italics** (italic emphasis passes a
  supplied word off as Latin). **Quotations** in quotation marks. Your brief
  carries Harris's **italic runs** per page (from the scan's OCR, rough; his quotation bounds and the
  words he took for titles or Greek). They are the editor's judgement, not the manuscript's: follow them
  by default, depart where the source shows otherwise (say so in a note). Reviews do not check
  quotation bounds against the italics. Italicised scripture inside indirect speech is quoted too; where
  quoting would garble the sentence, leave it unquoted and give the reference in an **S** note.
- **Formulae of the disputation** (ruled 2026-10-01; fixed renderings, **tagged only where GLOSSARY has
  a row**), rendered the same way throughout:
  *instatur* "it is objected" · *obicitur* "it is objected" · *arguitur* "it is argued" (with *per*:
  GLOSSARY) · *dicitur* "it is said" (in an answer: "the answer is") · *respondetur* "the reply is" ·
  *conclusio* "conclusion" · *antecedens / consequens* "antecedent / consequent" · *consequencia*
  "inference", ⛔ never "consequence" · *patet* "it is clear" · *supponitur* "it is supposed" (a premiss
  laid down) · *probatur* "proof:" or "it is proved" · *confirmatur* "this is confirmed" (⛔ not "it is
  confirmed"). *Ex fide* is the formula "as faith teaches" **only when no verb governs *ex*** (*ut ex fide
  supponitur* "as is supposed from faith").
- **Citation formulae:** *ubi supra / ubi super* "in the place cited above" (a reference back to a work
  already cited, ⛔ never a claim about where a passage stands), *ut supra* "as above", *infra* "below".
  *Utrobique* "on both sides / in both places", ⛔ not "everywhere" (*ubique*).

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
   **Ruled from the first chunk (2026-10-22, Wilson; GLOSSARY §C, end): tag only**, with a G note only
   for something specific to the passage (⛔ never a note that restates the row): *humanitas* "the
   humanity" · *incommunicantes* "that do not communicate" · *dimittere / dimissio* "lay aside / the
   laying-aside" · *assumere / assumpcio* "assume / assumption" (⚠ apart from the logician's *assumptum*,
   C note where that sense occurs) · *homo assumptus* "the assumed man" · *triduum* "the three days" ·
   *ydemptitas specifica* "identity of species" · *Verbum* "the Word", pronoun **"he"** · *deitas* "the
   Godhead" · *natura* "nature" · *persona* "person" · *creatura / creator / creatus* · *posicio /
   proposicio / predicacio* "position / proposition / predication" (kept apart) · *verificari de* "be
   true of" · *sacramentum* "sacrament" (G note "= mystery") vs *misterium* "mystery" · *moderni
   doctores* "the modern doctors" · *sancti* "the saints" · *probabiles doctores* "approved doctors" ·
   *Magister* "the Master" · *declarare* "make clear" vs *ostendere* "show" · *epilogus* "recapitulation"
   · *infirmitas* "weakness" · *habitudo* CONTEXTUAL "condition / respect".
   For the rest, **render consistently within your brief and PROPOSE the row** (the coordinator rules
   between briefs). Expect: *suppositum*, *ypostasis*, *res communis* (the common thing), *individuum*,
   *singulare*, *unire / unio*, *communicacio ydiomatum*, *materia prima*, *forma*, *compositum*,
   *symbolum* (the creed; has a row). Render *homo* "man" (the medieval *homo* that *Christus est homo*
   needs; never "human being" in the formulae).
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
   to", "according to") visible, in its place: *secundum deitatem / humanitatem* "as to the Godhead / as
   to the humanity". Reduplicative ***secundum quod*** "insofar as", ⛔ never "in that" (heard as
   "because"). ⛔ **Never supply "as God / as man"** where the Latin has bare apposition (*ipse Deus*) or
   bare predication: the difference between the bare and the reduplicated form is the treatise's matter.
   **Propositions in indirect speech:** where an accusative + infinitive names a proposition whose sense
   is under discussion (*intelligentes Christum non esse creaturam*), render it as the quoted proposition
   ("who understand 'Christ is not a creature'"), not "understand that …", which asserts it.

## Scripture

`python3 scripts/w3/bible.py "Ioh 10:30"` (Vulgate + Douay–Rheims; psalms in Vulgate numbering) or
`python3 scripts/w3/bible.py --find "ego et Pater unum sumus"`. Where Wyclif's Latin agrees with the
Clementine Vulgate, use the **Douay–Rheims wording**. Where he departs, translate *his* Latin and write
an **S** note giving the Vulgate. Modern references in the English (John 10:30). The chapter numbers
are Wyclif's, the verse numbers Harris's margin references where he gives them and ours where he does
not; psalms in Vulgate numbering (Harris's margin uses the Hebrew: Ps. cx = 109). The headnote says so once.

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
  `~/patrologia/sources/pl/tei/`). ⛔ Never pass memory off as verified. Id `I<chunk>-<n>` (`I01b-1`; ⚠ `I`, since `P` is *De potestate pape*),
  cited in the note: "(LEDGER I01b-1)". The *sancti* cited are above all Augustine (*De Trinitate*,
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

## Glossary (the 272 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| canonizare | canonize | The same English whether pope or scripture canonizes (*Dial.* 20.31, 21.1). Ruled 2026-09-28 (6 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| matrix ecclesia | mother church | The local mother church (cathedral or metropolitan); a **C** note at the first occurrence in each chunk, to keep it apart from the church as *mater nostra*. Ruled 2026-10-01 (*Eccl.* 23.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
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
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| metaphisica | metaphysics | *Inter omnes metaphisicas* → "among all the metaphysics": he counts the doctrine of the church as one (T. p. 368). Pilot. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| citra fidem | short of faith | The contrast with *ex fide*: held on evidence, not as faith teaches. Ruled 2026-09-28 (4 sites). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| verificari (de) | be true (of) | The logicians' sense; not "verified" (modern "checked"). Ruled 2026-10-22 (Wilson; *Incarn.* 7.6). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | approved doctors | Ruled 2026-10-22 (Wilson; *Incarn.* 7.1). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| autonomatice / antonomastice | by antonomasia (pre-eminently) | Pilot (*Eccl.* 1.16) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| laxare | loose | Kept apart from *relaxare* "relax". Ruled 2026-10-02 (*Eccl.* 23, 571.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dileccio | love | Kept apart from *caritas* "charity". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-e). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| connexio | conditional (proposition) | Logic: the "if … then" proposition. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 189.1). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 01-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-01-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-01-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "7.13–11.20"
divisions: "cap. 1 (heading 'Cap. I.' at 3.0); part 2 of 3, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1072 words; 1072 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n46–n50 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 1, part 2: [TITLE]

## ¶1 · 7.13–8.23

> [p. 7] Nec dubium quin ex principiis beati Augustini plane sequitur Christum esse creaturam. Quia iuxta suam infringibilem sentenciam Christus nedum est completa humanitas assumpta, sed tam corpus quam anima. Et quis dubitat de ista sequela? Christus est corpus creatum sicut et⁸ spiritus creatus. Ergo Christus est creatura et secundum illam creatus. Nec aliter esset univoce homo nobiscum:⁹ cum omnis alius homo sit duarum naturarum utraque. Nec credo sine [alta]¹⁰ illa philosophia De Anima nos posse recte concipere incarnacionem Verbi. Ideo Augustinus¹¹ Epistula 3ᵃ ad Volusianum sic loquitur: ‘Nunc vero inter Deum et homines mediator apparuit ut in unitate¹² persone¹³ copulans utramque naturam et solita¹³ sublimaret insolitis et insolita solitis temperaret.... Ille¹⁴ ergo sine seminibus operatus est hominem, qui in rerum natura sine seminibus operatus est semina.¹⁴ Ille in suo corpore numeros temporum mensurasque servavit etatum qui sine ulla¹⁵ mutabilitate mutando ordinem contexuit seculorum.¹⁶ Hoc¹⁷ enim crevit in¹⁸ [p. 8] tempore quod cepit ex tempore: Verbum autem in principio, per quod facta sunt omnia tempora, tempus elegit quo susciperet carnem, non tempori¹ cessit ut verteretur in carnem: homo quippe Deo accessit, non Deus a se recessit.’ Et sequitur ad propositum. ‘Sic autem quidam² reddi sibi racionem flagitant, quomodo Deus homini permixtus sit, ut una fieret persona Christi, cum hoc³ semel fieri oporteat. Sed quam racionem reddant ipsi de re quae cotidie⁴ fit, quomodo anima misceatur corpori ut una persona fiat hominis? Nam sicut in unitate⁵ persone anima unitur corpori ut homo sit, ita in unitate⁵ persone Deus unitur⁶ homini ut Christus⁷ sit. In illa ergo persona mixtura est anime et corporis, in hac persona⁸ mixtura est Dei et hominis. Si tamen recedat, auditor⁹ a consuetudine corporum qua⁹ solent duo liquores ita misceri ut neutrum servet suam integritatem.’ Et sequitur. ‘Quia ergo non oportebat ut in plenitudine temporis novum faceret¹⁰ mundum, nova¹¹ fecit in mundo. Homo enim de virgine procreatus et a mortuis in eternam vitam resuscitatus et super celos exaltatus potencius¹² fortasse opus¹³ est quam mundus.’ Quotlibet¹⁴ sunt talia dicta hujus boni hominis, ex quibus aperiri¹⁵ potest sensus scripture loquentis varie de ipso¹⁶ et controversia doctorum sequencium concordari.¹⁷

[ENGLISH]

## ¶2 · 8.24–8.30

> [p. 8] Et patet quod in simbolo Athanasii quando dicitur ‘Filius a Patre solo non est factus nec creatus sed genitus’ loquitur de eo pure secundum deitatem.¹⁸ Aliter enim contradiceret sibi ipsi, cum secundum humanitatem conceptus est a tota Trinitate ex substancia matris: ut dicit idem simbolum quando post introducit Christi incarnacionem secundum quam dicit verissime quod Christus est minor patre.

[ENGLISH]

## ¶3 · 8.31–9.12

> [p. 8] Et idem patet in alio simbolo ecclesie; ubi primo loquens [p. 9] de eo secundum quod Deus est vere dicit ‘genitum non factum, consubstancialem Patri per quem omnia facta sunt.’ Sed post loquendo de Christo ut homine dicit quod ‘incarnatus est de Spiritu Sancto ex Maria virgine et homo factus est.’ Ideo in talibus attendendum est ad regulam beati Augustini ‘quid et secundum quam naturam de Christo dicitur:’ et facile videtur quotquot auctoritates occurrerint¹ concordare. Cum enim sit Christus multorum singulum, sicut essencia divina, species humana, vel aliud universale; patet quia, sicut non repugnat Deum esse genitum et eundem Deum esse ingenitum, sic non repugnat eundem Christum esse creatorem et tamen ex tempore esse creatum.

[ENGLISH]

## ¶4 · 9.13–9.23

> [p. 9] Sed oportet in istis diversas² naturas subintelligere³ cum ydemptitate persone. Unde in primitiva ecclesia quando Christi divinitas fuit minus cognita,⁴ ordinaverunt apostoli quod fideles baptizarentur in nomine domini Iesu Christi, ut patet Actuum 8. ut vel sic Christiani elevarentur in animo⁵ ad credendum Christum esse supremam naturam possibilem⁶ scilicet deitatem. Sed postquam sancti doctores ecclesie ut Augustinus, Ieronimus et ceteri cultores assidui scripturarum intellexerunt quod Christus fuit gigas gemine substancie, scilicet⁷ tam divina substancia quam humana, concesserunt copulative Christum esse tam creatorem quam⁸ creaturam.

[ENGLISH]

## ¶5 · 9.24–10.2

> [p. 9] Unde beatus Ieronimus in fine primi libri super Epistolam ad Galat,⁹ ‘Quia semel,¹⁰ inquit, ad nomen creature venimus et sapiencia in Proverbiis Salomonis Dicit, “deus creavit me¹¹ in inicio viarum suarum antequam quidquam¹² faceret, a principio ab eterno ordinata sum,¹³ et ab antiquis antequam terra fieret”; multique timore ne Christum creaturam dicere compellantur,¹⁴ totum Christi misterium negant, ut dicant non Christum in hac sapiencia sed¹⁵ mundi sapienciam significari:¹⁵ nos libere proclamamus non esse periculum eum [p. 10] dicere¹ creaturam, quem² verum esse hominem² et crucifixum et maledictum tota spei nostre reverencia profitemur.”

[ENGLISH]

## ¶6 · 10.3–10.16

> [p. 10] Nec credo quod sanctus iste intellexit Christum esse creaturam sub racione qua eternaliter genitus; propter tria. Primo quia tunc concederet³ Christum eciam secundum deitatem esse creaturam; et cum creatura dicitur abstractive, sicut substancia vel essencia, tunc Christus esset alia substancia vel essencia quam Pater; quod est heresis Arriana. Et ad tantum non licet catholico laxare terminos, cum omnis creatura secundum Augustinum in Dialogo ad Felicianum et in De Questionibus⁴ Veteris et Nove Legis 122, sit de nichilo facta essencia. Sed constat quod Christus secundum deitatem non est factus ex nichilo; ergo nec secundum deitatem est creatura. Non est ergo de intencione huius sancti et profundi doctoris baptizare et⁵ tam extraneare⁶ a scriptura significacionem huius nominis ‘creatura.’

[ENGLISH]

## ¶7 · 10.17–11.1

> [p. 10] Secundo movet me causa quam beatus Ieronimus innuit. Videtur enim loqui de fidelibus sui temporis negantibus adverbia⁷ scripturarum loquencium⁷ de Christo secundum humanitatem. Sed quis queso fidelium trepidaret concedere⁸ Christum esse genitum⁹ eternaliter de Patre? cum puri philosophi diu ante incarnacionem hoc professi sunt, ut declaravi¹⁰ in tractatu De Trinitate.¹¹ Non ergo timebat concedere Christum esse¹² genitum vel genitum¹² eternaliter adintra; sed non secundum hominem assumptum et¹³ racione cuius concedimus de Christo predicata et gesta hominum ut sanctus doctor exemplificat et clarebit posterius.¹⁴ Unde evidencia Ieronimi est quod concedendum est Christum esse creaturam eo quod concedimus ipsum verum¹⁵ esse [p. 11] hominem et cetera huiusmodi que humanitatem concernunt.

[ENGLISH]

## ¶8 · 11.3–11.20

> [p. 11] Tercio movet me quod nec iste sanctus sapiens nec scriptura alia canonica, si non fallor, alicubi¹ accipit creari² pro gignicione eterna. Supposito ergo quod scriptura tam Salomonis quam Ecclesiastica loquatur de sapiencia increata que est Verbum Dei, ut testatur Ieronimus, et beatus Augustinus Ep 31 declarat ex textu Proverbiorum 8 et 30 quod intencionis Salomonis est dicere, quod Deus habet Filium sapienciam increatam: patet quod de ipsa loquitur nunc secundum deitatem ut eternaliter adintra genita non creata, et nunc ut creata vel creanda: ut nunc dicit secundum deitatem, ‘cum eo eram cuncta componens,’ et nunc ‘ab eterno ordinata sum:’ primum ad deitatem sapiencie referens, et secundum ad eius humanitatem, ut patet Proverbiorum 8. Unde de eius humanitate dicit infra 30.³ ‘Quis ascendit in celum atque descendit etc?⁴ Quod nomen eius aut quod nomen filii eius, si nosti?’ Et isti sensui alludit Apostolus secundum exposicionem Augustini ad Eph.⁵ 4, quando⁶ dicit: ‘qui descendit ipse est qui et ascendit super omnes celos.’

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Ps. vni. 5, 6. Heb. ii. 7. (7.7); reference Acts vffi. 16, 37. (9.17); reference Prov. vffi. 22. (9.26); reference Gall. ABC. quicquam 0. (9.35); reference . Proverbs and (11.9); reference Prov. xxx. 4, 5. (11.17); reference ad Hebre. (11.29).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 7:
1 informam servi qui formam Dei O.
2 et *om.* O.
3 creaturam A B C.
4-4 servi appellacionem (applm̅) Augustinus ad O.
5 eum *om.* O.
6 domine *om.* O.
7 petibus O.
8 sed et C.
9 cum aliis hominibus A B C.
10 sine "alta" philosophia *in marg.* illa *man. pr.* A; sine alta 1ᵃ philosophia B; sine 1ᵃ philosophia C O; *an* prima *legendum*?
11 Augustinus *om.* O.
12 unitatem O.
13-13 copulans utraque et solita A B C; copulam utramque naturam solita O.
14-14 Ille ergo sine seminibus temperatus est semina A B C.
15 ista A B C; illa O; ulla *Aug. ut sensus poscit.*
16 seclorum O.
17 homo O.
18 ȋ ex B.

CHECK: the figure "1" appears twice in the main-text list but the foot has only one entry for 1 (the entry covers both occurrences); the figure 14 is likewise given as a single bracketed entry 14-14.

p. 8:
1 te̅pali̅ O.
2 quidam *om.* B.
3 hoc *om.* O.
4 quotidie A B; cottidie C.
5 unitatem A C.
6 unitatur O.
7 deus B.
8 persona *om.* A B C.
9 auditor a consuedudine corporum quomodo A; auditor a consbbetutine corporum quomodo B; audito a͛ſnene qᵃ O.; qua *Aug.*
10 fieret A B C.
11 novam C.
12 competencius A B.
13 omnipotens A B C.
14 quota O.
15 apparere A B C.
16 Christo A B C.
17 concordare O.
18 divinitatem A B C.
CHECK: figure 5 appears twice in the main text but there is only one entry for 5 at the foot; the entry for 9 is a single long note covering both occurrences of 9. Also the readings in 1 and 9 contain abbreviation marks I could not reproduce exactly: "te̅pali̅" and "a͛ſnene qᵃ" [?].

p. 9:
1 occurrerunt A B C.
2 diversitas O.
3 sub *om.* A B C.
4 nimis incognita O.
5 anima O.
6 possibile O.
7 scilicet *om.* O.
8 quam eciam O.
9 galath. O; Gall. A B C.
10 solum A B C.
11 me *om.* O; in *om.* A B C.
12 quitquam C; quicquam O.
13 sunt C.
14 ne Christum cere compellantur B; appellantur O.
15-15 sed mundum per sapienciam signari A B C.

p. 10:
1 esse A B C.
2 quem verum est et hominem A B; quod verum esse hominem C; quem verbum esse et hominem O.
3 concederem A B C.
4 in de q. veteris A B; in de veteris C; in questionibus veteris O.
5 et *om.* A B C.
6 extranee A B C; extranie O.
7 ad verba scripturam loquentem A B C; adverbia scripturam loquentem O.
8 contendere O.
9 non *add. in marg.* A.
10 declarat O.
11 eternitate B.
12-12 esse genituram vel genitum A B C; genitum vel genitura O.
13 esse O; et M; et *om.* A B C.
14 post A B C.
15 concedimus esse vermem hominem A B C; concedimus ipsam esse vᵐ ē hominem O.

p. 11:
1 alicubi om. A B C.
2 creari om. O.
3 30 om. C.
4 et A B C.
5 epheseos O.
6 qui O.
7 sensum om. A B C.
8 cetera A B.
9 thabernaculo A ut infra saepius.
10 sed B.
11 transit onerata O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 7: x iJe Anima, | De Anima
p. 8: Editor in Chief | Hon. Sec. | Early English Text, | Hon. Sec. | Original Series | Extra Series | New Shalcspere, | Hon. Sec, | Editor in Chief | Hoyi. Sec. | Hellas. Chairman of Committee, | Hon. Sec. | Hon. Sec, | Hon. Sec, | Hon. Sec.
p. 10: De Trinitate. 11 ~Non
p. 11: De Incarnatione Verbi | De Veritate S. Scripturae | De Universalibus, | De Ecclesia, | Doctrinale Fidei, | W. de Incarnatione Verbi
```

---

## Chunk 01-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-01-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-01-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "11.21–13.12"
divisions: "cap. 1 (heading 'Cap. I.' at 3.0); part 3 of 3, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "424 words; 424 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n50–n52 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 1, part 3: [TITLE]

## ¶1 · 11.21–12.12

> [p. 11] Et istum sensum⁷ declarat Ecclesiasticus 24 cap. loquens de eadem sapiencia: primo sic: ‘ego ex ore altissimi prodii primogenita ante omnem creaturam,’ et sic⁸ de multis que conveniunt divinitati. Sed post prosequitur quoad eius humanitatem: ‘tunc precepit et dixit mihi creator omnium, et qui creavit me requievit in tabernaculo⁹ meo:’ dixit, inquam, in plenitudine temporis quando misit me incarnandam; iuxta¹⁰ illud Psalmi 31 iuxta exposicionem Apostoli ad Hebre. 10. ‘holocaustum et propeccato non postulasti; tunc dixi, ecce venio’ scilicet incarnandus; et sic deitas creavit me secundum essenciam corpoream ante omnia secula: que quidem essencia transivit honorata¹¹ a patribus veteris testamenti nunc in gentibus et nunc in patribus, ut patet [p. 12] alibi. Sed in plenitudine temporis quando erectum est tabernaculum ex carne assumpta de beata virgine et forma humanitatis copulata ypostatice, tunc requievit tota Trinitas in assumpto corpore iuxta illud Colos. 2.¹ ‘In ipso, inquit Apostolus, habitat omnis plenitudo divinitatis corporaliter.’ Nam tota Trinitas est eadem divina essencia que est Christus existens illud corpus. Unde et illud tabernaculum figuratum est per quelibet tabernacula veteris testamenti. Et ad istum sensum² loquitur apostolorum capitaneus de corpore quod est ipse: ‘iustum, inquit, arbitror quamdiu sum³ in hoc tabernaculo suscitare vos in commonicione, certus quod velox est deposicio tabernaculi mei.’ 2 Petri 1° capitulo.

[ENGLISH]

## ¶2 · 12.13–12.19

> [p. 12] Sic ergo, intelligendo⁴ per sapienciam Verbum Dei quod est tam deitas⁵ quam raciones quotlibet exemplares et per consequens veritates, quae terminant⁶ creatam sapienciam⁶ obiective, ac ultimo ipsa sapiencia incarnata; possunt⁷ dicta in libris Sapienciae⁸ optime verificari ad litteram de eadem sapiencia incarnata:⁷ ut testantur Augustinus et Ieronimus duo⁹ non parvi pugiles scripturarum.

[ENGLISH]

## ¶3 · 12.20–12.27

> [p. 12] Tercio autem, declinante scola ab antiqua logica¹⁰ de universalibus et a recta metaphisica¹¹ de formis substancialibus, negarunt doctores moderniores concorditer quod homo est anima, vel Christus humanitas, et¹² consequenter quod Christus est creatura, intelligentes autonomatice¹³ Christum solum secundum excellentissimum quod est Christus; et sic licet verum concipiant, multum tamen degenerant a logica scripturarum.

[ENGLISH]

## ¶4 · 12.28–13.2

> [p. 12] Ego autem finaliter¹⁴ concordo cum quocunque catholice loquente in illa materia, concedens cum fidelibus primitive ecclesie quod Christus est purissimus homo possibilis: verumtamen non pure¹⁵ vel tantum est homo, cum sit assumpta [p. 13] humanitas; et cum plene sit divinitas, patet quod est aliud sed non alius quam illa humanitas.

[ENGLISH]

## ¶5 · 13.3–13.6

> [p. 13] Concordo 2° cum approbatis doctoribus ut Augustino Ieronimo et ceteris concedens quod Christus nedum est creator et essencia que nullo¹ modo creari poterit vel moveri, sed eciam² creatura.

[ENGLISH]

## ¶6 · 13.7–13.12

> [p. 13] Concordo 3° cum novellis quod Christus secundum deitatem non est creatura, nec minor Patre, corporalis, mobilis, visibilis, subicibilis, et sic de quocunque quae scriptura ascribit sibi humanitus. Et³ ad istum sensum concedo⁴ affirmativas, modifico negativas.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference . Proverbs and (11.9); reference Prov. xxx. 4, 5. (11.17); reference ad Hebre. (11.29); reference Augustine, Je- (13.6); reference Ecclesiastica (13.6).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 11:
1 alicubi om. A B C.
2 creari om. O.
3 30 om. C.
4 et A B C.
5 epheseos O.
6 qui O.
7 sensum om. A B C.
8 cetera A B.
9 thabernaculo A ut infra saepius.
10 sed B.
11 transit onerata O.

p. 12:
1 colocf. in C; coloc°. ¶ 2°. in O.
2 sensum om. O.
3 sunt O.
4 intendo O.
5 divinitas A B C.
6 terminantâ sapienciam O.
7-7 possunt . . . . incarnata om. A B C.
8 libȝ add. O; pro libris per errorem iterato.
9 non duo A B C O.
10 loyca C.
11 methaphisica O; et sic saepius.
12 et om. A B C.
13 authonomatice A B C.
14 faciliter B.
15 purus B.

p. 13:
1 non A B C.
2 est A B C; eciam O M.
3 et *om.* A B C.
4 concedens O.
5 proposicio A B C.
6 posicionibus B.
7 oppinione C.
8 ad *om.* A B C.
9 tam C.
10 pup^cu? O[?].
11 secessus A B C.
12 cuñulorum O ? *cuniculorum*; tumulorum B.

CHECK: none; figures 1–12 all have entries. Entry 10 (superscript letters after "pup") is uncertain.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 11: De Incarnatione Verbi | De Veritate S. Scripturae | De Universalibus, | De Ecclesia, | Doctrinale Fidei, | W. de Incarnatione Verbi
p. 12: Obicitur quod dico korribilius Arianis quia dico Christum esse materiam primam et sic abiectissimam creaturum.
p. 13: De Universalibus | \_Declarat quomodo ista sentencia discrepat ab heresi Arriana. The assertion of the reality of Chrisfs humanity, by maintaining that as man he is a creature, gives no support to the errors of Arius, Sabellius, or Nestorius.~\
```

---

## Chunk 02-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-02-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-02-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "13.0–17.19"
divisions: "cap. 2 (heading 'Cap. II.' at 13.0); part 1 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1086 words; 1081 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 4 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n52–n56 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 2, part 1: [TITLE]

## ¶1 · 13.0–13.15

> [p. 13] [Declarat quomodo ista sentencia discrepat ab heresi Arriana. The assertion of the reality of Christ's humanity, by maintaining that as man he is a creature, gives no support to the errors of Arius, Sabellius, or Nestorius.] Ex istis per modum corollarii elucescit quomodo ista posicio⁵ differt ab opinionibus⁶ hereticorum de Christo heretice senciencium.

[ENGLISH]

## ¶2 · 13.16–14.7

> [p. 13] Et primo de opinione⁷ Arrii de quo narrat Eusebius in Ecclesiastica Historia li° 10° ca. 13. 'Arrius, inquit, pergens ad⁸ ecclesiam episcoporum et populorum frequencia constipatus, humane necessitatis causa⁹ ad locum publicum¹⁰ declinavit; ubi cum sederet, intestina eius atque omnia viscera in secessu¹¹ cumulorum¹² defluxerunt, et ita in apto [p. 14] loco dignam mortem blasfemie¹ et² fetide mentis² exsolvit.' Et quia secundum Magistrum Sentenciarum in 3°· Dist. 2ᵃ. Arrii hec fuisse perfidia³ legitur ut Christum esse⁴ creaturam fateretur, ut capit a beato Ambrosio primo libro de Trinitate cap. 9°· 'Ideo, inquit Ambrosius, diffusa sunt Arrii viscera et crepuit medius prostratus in faciem ea, quibus Christum⁵ negaverat, feda ora⁶ pollutus.'

[ENGLISH]

## ¶3 · 14.8–14.17

> [p. 14] Quando⁷ ergo illa⁸ opinio videtur Arrio in hoc consentire bonum videtur differenciam⁹ declarare. Nam propterea videtur Magistro et ipsum sequentibus potissime quod non debet concedi simpliciter Christum esse creaturam vel factum sed cum determinacione¹⁰ quod fuit factus secundum hominem. Primo ergo notandum quod nunquam fuit hereticus quin in aliquo dixit verum: omnes enim concesserunt Deum esse: et ideo valde inconsonum est doctori imponere alteri¹¹ heresim Arrianam, nisi prius diligenter notaverit in quibus et quomodo talis heresis est fundata.

[ENGLISH]

## ¶4 · 14.18–14.22

> [p. 14] Stetit ergo heresis Arriana in his tribus precipue. Primo in hoc quod negavit Christum esse Deum deorum et magnum Deum, cum posuit eum¹² esse non eiusdem substancie cum Patre, sed ipsos differre ab invicem eciam secundum deitatem substancialiter sicut¹³ differunt personaliter.

[ENGLISH]

## ¶5 · 14.23–15.31

> [p. 14] Unde Augustinus Epa. 33 ad Bonifacium, 'Ut, inquit, breviter¹⁴ insinuem dilectioni tue quid inter Arrianorum¹⁵ et Donatistarum intersit errorem: Arriani Patris et Filii et Spiritus Sancti diversas esse substancias dicunt; Donatiste autem non hoc¹⁶ dicunt, sed unam Trinitatis substanciam confitentur.' Dixit itaque¹⁷ Arrius quod summa essencia que est Christus sit citra essenciam Dei Patris, ut est essencia angeli vel hominis quos scriptura sacra vocat deos pluraliter, ut allegat Salvator Iudeis Ioh. 10. 'Nonne scriptum est in lege vestra, 'Ego dixi dii estis?' Si igitur eos vocat deos, [p. 15] ad quos sermo Dei factus est, et non potest solvi scriptura; quem Pater sanctificavit et misit in mundum, quomodo et vos dicitis 'blasfemas,'¹ quia dixi 'Filius Dei sum¹?' Et forte ex isto dicto capta est heresis Arriana. Unde dicit Augustinus Ome 48.² quod Iudei audientes illud Ioh. 10. 'Ego et Pater unum sumus,' et intelligentes Christum intendere quod sit eadem substancia cum Patre, 'Iudei, inquit, intellexerunt quod Arriani non intellexerunt; quoniam senserunt non posse dici ''ego et Pater unum sumus,'' nisi ubi equalitas est Patris et Filii. Sed Dominus videns Judeos pre ira non ferre splendorem veritatis, eum temperavit in verbis eis allegans illud Psⁱ· 81.³ ''Ego dixi dii estis etc.''' Nec est putandum quod Veritas illuserit⁴ Iudeis⁵ sophistice in hoc dicto, sed dulciter manuduxit mitigando eorum rancorem ex⁶ scriptura patriarche David plus eis autentica⁷ inter omnes. Cum⁸ enim non fuit in Christo EST et NON, et dixit⁸ eis superius Ioh. 10. quod ipse est omnipotens et eadem substancia cum Patre: patet quod illam sentenciam postmodum non retractat. Minor patet notato textu illius capⁱ. Nam ibi dicitur: 'oves mee vocem meam audiunt et ego vitam eternam do eis, et non rapiet eas⁹ quisquam de manu mea' et cetera que secuntur. Probatur illa trimembris conclusio ex ibi positis. Nam ibi¹⁰ dicitur, 'Pater meus quod dedit michi maius omnibus est:' ergo Pater meus¹¹ est omnipotens, et per consequens 'nemo potest rapere de manu Patris mei,' et ultra sequitur¹² 'nemo potest rapere de manu Patris mei;¹³ et 'Ego et Pater unum sumus;' ergo 'nemo potest rapere oves de manu mea.' Istam itaque connexionem subtilissimam Iudei conceperant quam ignorabant Arriani. Ex quo patet quod in deduccione sequenti eandem conclusionem intenderat sed medio plus occulto.

[ENGLISH]

## ¶6 · 16.1–16.33

> [p. 16] Pro quo notandum quod sicut Judei multum appreciati¹ sunt prophetam² David, sic³ ex eius textu cognoverant quod Messias venturus ex eis foret tam Deus quam homo. Hoc videtur evidens ex argumento Salvatoris facto Phariseis, Mt 22. ubi sic congregatis Phariseis interrogat ab eis⁴ Jesus dicens,⁵ 'Quid vobis videtur de Christo? cuius filius est? dicunt ei, 'David:'⁶ ait illis, 'quomodo ergo David⁷ in spiritu vocat eum dominum dicens: 'dixit Dominus Domino meo, 'sede a dextris, donec ponam inimicos tuos scabellum pedum tuorum.' Si ergo David vocat eum Dominum quomodo filius eius est? Et nemo poterat ei respondere verbum, nec ausus est quisquam ex illa die eum amplius interrogare.' Non enim contendebant⁶ illi legis periti in ampliacione⁸ verbi de presenti scientes ex sensu scripture quod apud Deum sunt cuncta⁹ presencia. Ideo sciverunt Christum vel Messiam esse filium David pro quodam tempore. Sciverunt 2^do illud Psalmi 109 quod Veritas allegavit dictum esse de Christo. Sciverunt 3° quod propheta tam eximius non vocaret filium suum tam pauperem et abiectum Dominum suum secundum naturam ab¹⁰ eo assumptam sed secundum naturam¹⁰ superiorem. Ideo non affuit eis vel ullum¹¹ coloratum subterfugium evadendi. Unde pro 2° argumento Salvatoris supponitur quod Verbum vel Sermo Dei quod idem est, sit eternum idem substancialiter Deo Patri. Patet hoc per illud Psalmi 32¹² 'Verbo Domini celi firmati sunt.' 2^do supponitur quod dictum verbum fuit incarnandum. Patet hoc per illud Psalmi 106¹³ 'misit verbum suum et sanavit eos.' Unde et dictum Verbum vocaverunt prophete concorditer Messiam vel Christum eis promissum. 3° supponitur quod dicti Verbi participacione sit multitudo hominum in¹⁴ Christum directe¹⁴ credencium deificanda participative, sicut carbo ex ignis participacione est ignitus. Patet hoc per illud Ps. 81.¹⁵ 'Ego dixi dii estis.'

[ENGLISH]

## ¶7 · 17.1–17.19

> [p. 17] Istis suppositis formetur racio sic ex sentencia Salvatoris: Ille Sermo vel Verbum, in quo concordant omnes prophete de operibus miraculosis, de tempore et aliis circumstanciis, et illis quibus mittitur salvandis et deificandis, est verus Messias, et per consequens Deus et homo iuxta textus propheticos: sed in me omnia ista conveniunt: ergo sum Deus¹ et homo: et per consequens non solum¹ participacione deificatus.² Ideo hic³ dicit Augustinus; 'Si Sermone⁴ Dei facto ad⁵ homines fiunt ipsi dii, tunc⁶ participando fiunt ipsi dii⁶; et per consequens Sermo ille, quo participant, erit Deus. Si lumine. luminati dii sunt, lumen quod illuminat non est Deus? si calefacti igne salutari⁷ dii efficiuntur, ignis unde calefiunt non est Deus?' Oportet ergo quod⁸ Sermo, quo⁸ fontaliter deificantur homines ex unitate substancie cum suo eternaliter adintra dicente, sit eadem deitas cum dicente; et per consequens non blasfemat⁹ dicendo se naturalem filium Dei esse. Et ex ignorancia huius sensus literalis scripture exciderant¹⁰ Arriani, sicut et Sabelliani, ut recitat Augustinus Ome. 47.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 13: *Nestorius.] Ex* (print = bt (heading end, then Ex istis)) [SUB]
  - 13: *li°* (print = bt (Historia li° 10°; strip misaligned, checked full page)) [SUB]
  - 15: *Psⁱ·* (print = bt) [SUB]
  - 15: *NON,* (print = bt (small caps)) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustine, Je- (13.6); reference Ecclesiastica (13.6); reference Ps. lxxxu. 6. (14.33); reference 2 Cor. i. 18 Vuig. (15.16); reference PsSCcx Si°n °f (16.2); reference Matt. xxii. 4i. (16.5); reference Ps. cx. 1. (16.8); reference Ps. xxxiii. 6. (16.25).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 13:
1 non A B C.
2 est A B C; eciam O M.
3 et *om.* A B C.
4 concedens O.
5 proposicio A B C.
6 posicionibus B.
7 oppinione C.
8 ad *om.* A B C.
9 tam C.
10 pup^cu? O[?].
11 secessus A B C.
12 cuñulorum O ? *cuniculorum*; tumulorum B.

CHECK: none; figures 1–12 all have entries. Entry 10 (superscript letters after "pup") is uncertain.

p. 14:
1 blasfeme O; blasphemie C.
2-2 debitam M.
3 profidea O.
4 esse om. O.
5 Christum om. A B C.
6 hora O.
7 Cum A B C.
8 ista O.
9 drām A B C.
10 declaracione O.
11 doctori alteri imponere A C; doctori altius imponere B.
12 ipsum O.
13 sic C.
14 breviter om. O.
15 arriarrorum O.
16 hoc non A B C.
17 autem O.

p. 15:
1-1 blasfemias quia filius dei sum B; blasfemia etc. C; blasfemo O.
2 ep. 49 A B C.
3 81 om. A C.
4 illusit O.
5 iudeos A B.
6 ex om. O.
7 illis authenticata O.
8 cum enim non fuit in christo est et non dixit A B; cum enim non fuit in christo non est et non dixit C; cum non fuit in christo est et non dixit O.
9 ~~eas~~ sic in cod. A; eas in margine C.
10 ubi A B C.
11 meus om. A B C.
12 sequitur om. O.
13 mei om. O.

p. 16:
1 appresciati O.
2 prophetiam O.
3 sicut A C; sicud B.
4 interrogavit ex eis O.
5 Jesus d. A.
6-6 David etc. Non enim contendebant B.
7 David *om.* A.
8 amplificacione O.
9 omnia sunt B.
10-10 ab eo . . . naturam *om.* O.
11 ullum *om.* O.
12 22 O.
13 108 A B C.
14-14 in ipsum debite A B C.
15 81 *om.* O.

p. 17:
1–1 deus et per consequens homo non solum A B C.
2 deificus *codd. omnes.*
3 hic *om.* A B C.
4 sermonem B; sermo dei factus C.
5 ab B.
6–6 tunc . . . dii *om.* B.
7 salutarii O.
8–8 oportet ergo sermo quo O; oportet ergo quod sermo primo quo A.B.
9 blasfemant C.
10 excidarant B.
11 stat B M.
12 suscipere O M.
13 notissimo A B C.
14 esse *add.* B.
15 Et hoc utrumque esse A C; et hoc utrumque est B.
16 Ephifanius O.
17 Apolinaristis B.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 13: De Universalibus | \_Declarat quomodo ista sentencia discrepat ab heresi Arriana. The assertion of the reality of Chrisfs humanity, by maintaining that as man he is a creature, gives no support to the errors of Arius, Sabellius, or Nestorius.~\
p. 14: De Anima
p. 15: Prologus mgri Johls de Incarnacione. | Explicit prologus. Incipit de Incarnacione Capitolum primum. | Ilomo perfectus, Augustinus: | Creaturam Christum asserentes sicut et negantes quomodo sunt intelligendi; | Persona hominis sifiat ex corpore et anima non videtur distincta ab (Ji)unitate integra et completa facta ex eisdem. | Incipit tractatus de incarnacione mgri Jo. Wyldeph. | Capitolum primum. | aV incarnacoe m ri Jo. Wy. | 1 Ye are gods. y
p. 16: De Bened. Ine. Jo. JFiklifa | ld\ Hic de composicione hominis non est examinatus. | De Benedicta Incamacione 1 | De Incarnacione
p. 17: gaudium, sicut, infirmius, faciliter, purus, racionaliter, suhstancialihus | De Incarnatione
```
