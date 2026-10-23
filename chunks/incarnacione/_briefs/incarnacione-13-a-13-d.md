# Translation brief: incarnacione 13-a–13-d

You translate these 4 chunk(s) of Wyclif's *Tractatus de benedicta incarnacione* in a single pass. Everything you need is in this file:
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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-13-a.md chunks/incarnacione/wyc-incarnacione-13-b.md chunks/incarnacione/wyc-incarnacione-13-c.md chunks/incarnacione/wyc-incarnacione-13-d.md` once and fix what it reports.
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
  neither → translate the print and flag it. Never smooth nonsense into sense. ⛔ **In this volume the manuscripts
  outrank Harris** (Wilson, 2026-10-22: Harris is less trusted than Loserth). Where the manuscripts agree
  **against** the print (all of A B C O, or a majority backed by the source Wyclif quotes: the Vulgate, a
  father's text), translate the manuscripts unless their reading will not construe; Harris's own
  emendations against every manuscript are set aside on the same terms. T note: "*X*, with A B C O,
  against the print's *Y*". Otherwise the print stands: a single manuscript's reading (M's above all, a
  summary) never outweighs it without cause; **the source Wyclif quotes, read and agreeing with that
  manuscript, is cause** (*In III Sent.* "d. 22", O + Bonaventure against the print's "12", 49.4). **Families:** A B C are one recension (Beer), so A B C alone against the print and O is one witness, not
  a majority; agreement **across the families** (O with any of A B C) against the print is what outranks it
  (A C O against B, 65.11). An argument that fails without a manuscript's reading is cause as well (O, 61.22). A **spelling-only** variant the rule adopts (*volucionibus*) changes no English and needs no T note. Every departure gets a T note giving both readings. ⚠ Harris is a 19th-century editor of a
  14th-century schoolman: where the print is grammatical but the argument fails, suspect the editor's
  choice among variants before Wyclif's logic, and read the apparatus.
- **English layout:** `[N]` at the same word as `[p. N]` in the Latin (the chunk's first `[p. N]` is
  implicit). Supplied words in `[brackets]`, sparingly, ⛔ **never in italics** (italic emphasis passes a
  supplied word off as Latin). **Quotations** in quotation marks. Your brief
  carries Harris's **italic runs** per page (from the scan's OCR, rough, ⚠ page numbers drift: a run not in your page's Latin belongs to another page; his quotation bounds and the
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
   doctores* "the modern doctors" · *sancti* "the saints" · *probabiles doctores* "reputable doctors" vs *approbati doctores* "approved doctors" ·
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

- `[^n]` from 1, the marker placed in the same edit as its note, each opening with a type letter **with a full stop** (`**C.**`; the site strips only that form):
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
  Hilary, the Lombard (*Sent.* III) and Grosseteste; the *moderni* are usually unnamed. Harris's index (`sources/ia-ocr/latinworks03wycl.txt`, near l. 23680) lists his identifications of Wyclif's own works (*De Trinitate*, *De adnichilacione* …). ⚠ Thomas's "many men" (one person with several humanities; ch. 12) is the *Scriptum super Sent.* III d. 1 q. 2 a. 5, ⛔ not *ST* III q. 3 a. 7, which concludes "one man" (LEDGER Iprol-3). ⚠ Wyclif counts the Maximinus works as **three books** "contra Maximinianum": his book 1 = the *Collatio cum Maximino* (PL 42, 709–42), books 2–3 = *Contra Maximinum* I–II (his "book 3, c. 22" = II.22); his quotations from book 1 may be Maximinus speaking, not Augustine (LEDGER I01a-9, I02b-4, I02c-5). ⚠ Wyclif's chapter numbers for Anselm's *De incarnatione Verbi* run **one above Migne's** from c. 6 on (his "6" = Migne V = Schmitt 10; his "7" = Migne VI = Schmitt 11; his "1" = Schmitt 1 = Migne II): give Wyclif's number and the modern one, "c. 7 in Wyclif's numbering (Schmitt c. 11; PL 158, c. VI)" (LEDGER I09a-1).

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

## Glossary (the 435 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| prepositura | office of superior | The abstract beside *prepositi*. Ruled 2026-10-02 (95.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). Third referent, the logician's arrangement of terms in a proposition (*Incarn.* 49.10): "ordering", with a **C** note; ruled 2026-10-22 (coordinator, delegated). |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| prepositi | superiors | Heads of houses; kept apart from *prelatus*. Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
| occasionaliter | by occasion | Occasion, not cause. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| incommunicans / incommunicantes (*nature*) | that do not communicate (with one another) | None predicated of, or shared with, another (Godhead, body, soul). Not "incommunicable": keep the participle. Ruled 2026-10-22 (Wilson; *Incarn.* 1.4). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| immediate | without intermediary | The scholastic sense, ⛔ not "at once". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 30.30). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| suppositacio | suppositation | Kept apart from *supposicio* "supposition". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.31). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| faccio | making | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.6). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| figura / figuratum | figure / thing figured | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.23). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| analogicari | be said analogically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.27). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| subsistencia | subsistence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 148.10). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| concretum / abstractum | concrete [term] / abstract [term] | *Homo* the concrete, *humanitas* the abstract. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152). |
| filiacio | sonship | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 154–155). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| nativitas | nativity | Christ's twofold birth. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| reduplicativa | reduplicative [proposition] | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.6). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| sensibilis (in the definition of animal) | sentient | *Substancia animata sensibilis*: able to sense. Elsewhere the §D row "perceptible" holds; G note at first use. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 177). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| peticio (principii) / petitur | begging [of the question] / is begged | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.23). |
| vicem supplere / vicis supplecio | supply the place / the supplying of a place | God supplying the place of a second cause. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 187.26). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| remitti / intendi (of a quality, merit) | be remitted / be intensified | The intension and remission of forms; not *remissio* of sin. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 197.1–7). |
| in divinis | among the divine [persons] | Keeps "Godhead" for *deitas*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 196.18). |
| partes proporcionales | proportional parts | The halving division of a continuum. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 194.24). |
| multiplicacio dimensionalis | dimensional multiplication | One body in several places by its dimensions. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.6). |
| habitus (= possession, *habere*) | the having | The category of having, C note; kept apart from *habitus* "habit". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.14). |
| proporcio racionalis | rational proportion | The mathematical ratio. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 207.7). |
| a maiori vel pari | from the greater or from the equal | Arguments *a maiori*; cf. *locus a maiori*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.5). |
| sensibile commune | common sensible | Aristotle's common sensibles (number, motion, figure); the term of art, against the §D row "perceptible". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 209.23). |
| communioritas | greater commonness | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 210.15). |
| multiplicacio concomitancie | multiplication of concomitance | Cf. *gracia concomitancie*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.21). |
| nomen appellativum | appellative name | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 213.29). |
| imposicio primaria | primary imposition | Of a term's first assignment to signify. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 214). |
| assertibile | assertible | The thing a proposition asserts. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| superioritas / inferioritas terminorum | superiority / inferiority of terms | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 215). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| cohabitacio | joint dwelling | Ruled 2026-09-28 (coordinator, delegated). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| laude digni | worthy of praise | (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| mendicacio; mendicare; mendicitas | begging; to beg; beggary | Kept apart; *mendicitas* is DR's "beggary" (Prov. 30:8). Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
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
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| continuacio (of bodies, the act) / discontinuacio; continuare / discontinuare | continuation / discontinuation; make continuous / make discontinuous | The making of several bodies into one continuum (*Incarn.* ch. 12), G note at first use: not "carrying on". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 204.30, 211.12). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| habilis / habilitas; habilitare | qualified / qualification; to qualify | The positive of *inhabilis* "unqualified". Ruled 2026-10-02 (*Eccl.* 19, 469.4). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| discrasia | distemper | Physicians' term. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 223.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| prepositus (participle of *preponere*) | the one preferred | CONTEXTUAL beside *prepositi* "superiors" (the noun); untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| gravandi | those to be charged | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 360.24). |
| indiffinite | without fixed bounds | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.3). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 13-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-13-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-13-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "216.0–220.22"
divisions: "cap. 13 (heading 'Cap. XIII.' at 216.0); part 1 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1188 words; 1187 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n255–n259 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 13, part 1: [TITLE]

## ¶1 · 216.0–216.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 216] [Confirmat aliorum sentencias quod, si omnes humanitates assumeret, tunc nec foret unus homo nec multi homines, sed et unicus atque multi; et sic concordat modernorum sentencias cum antiquis. Assuming, as proved in the last chapter (p. 203), the truth of the dictum of St. Thomas that if Christ assumed many humanities, He would be many men: the modern view is supported that He assumed all humanities, and was thereby both THE ONE MAN and also many men; and thus opinions are reconciled and the unity of truth established.]

[ENGLISH]

## ¶2 · 216.8–216.12

> [p. 216] Habito quod Christus assumendo multas humanitates foret consequenter multi homines, ut sentenciat sanctus Thomas; probatur quod, si omnes humanitates assumeret, foret unicus homo tantum, ut recentissimi scribentes asserunt satis vere.

[ENGLISH]

## ¶3 · 216.13–217.9

> [p. 216] Nam hoc posito, omnis homo foret omnis homo; ergo foret solummodo unus homo. Antecedens patet per exponentes, cum homo Christus sit omnis homo; ut patet per conversionem, omnis homo est Christus. Nam si in tali casu non omnis homo sit Christus, cum nulla natura assumpta sit homo, ut dicunt concorditer; sequitur quod aliqua¹ persona de specie humana non sit Christus, et illam personam oportet in casu posito dicere Verbum Dei. Sed constat quod illa [p. 217] est Christus; cum ergo Verbum sit omnis homo, quod quidem Verbum est aliquis homo; sequitur quod aliquis homo sit omnis homo; et tamen¹ nichil est homo nisi illud Verbum; sequitur ex posicione² quod omnis homo sit omnis homo. Quo habito³ probo quod repugnat huic multos homines esse. Nam si duo homines sunt, tunc⁴ duo homines sunt⁴ duo homines, et per consequens sunt duo homines differentes, et sic unus illorum non est reliquus; consequens contra datum, cum omnis homo sit omnis homo.

[ENGLISH]

## ¶4 · 217.10–217.25

> [p. 217] Item si Verbum in tali casu sit multi homines⁵ propter multitudinem formarum, quas predicatum significat; tunc forme ille sive nature plurificate essent Verbum; consequens impossibile sic dicenti; et consequencia ex hoc deducitur⁶ quod predicatum nunquam dicitur pluraliter de subiecto nisi quodlibet illorum pluraliter significatorum per predicatum vere dicatur⁷ de subiecto; ut natura divina non est multe persone, nisi quelibet illarum personarum sit deitas.⁸ Cum ergo pluralitas in casu posito⁹ sit solummodo¹⁰ in naturis, que non sunt homines: videtur¹¹ quod alienum sit concedere Verbum esse multos homines¹¹ propter illarum naturarum multitudinem, quarum¹² nulla est homo; ut Petrus non est multa accidencia, licet sit album et musicum, quia tunc esset¹³ multe substancie accidentate, et per consequens multi homines, et per idem infinite substancie; et patet prima consequencia¹⁴ eo quod Petrus est precise¹⁵ substancia.

[ENGLISH]

## ¶5 · 217.26–218.12

> [p. 217] Item si Verbum ad multitudinem¹⁶ humanitatum sit multi homines, et omnis homo est individuum; tunc est multa individua, et per consequens multe persone; quod est impossibile. Et consequencia sic probatur. Si Christus est multi homines, et per se homo est substancia; tunc est multe substancie¹⁷ individue racionalis nature non aliene [p. 218] suppositate¹; et per consequens multe persone; quod foret absurdissimum, quod Deus esset mille persone, ut puta totus populus Christianus; cum ista posicio negat hominem communem. Minus ergo colorate una persona speciei humane² foret communicata tot hominibus quot foret omnis et singuli eorundem, quam quod natura specifica foret unum quodque eius suppositum, quia ibi maneret suppositorum distinccio cum ydemptitate nature specifice. Hic autem est idem singularis homo omnium hominum quilibet; et per consequens omnis homo est³ omnis homo; persona ergo que communicatur tot substanciis ydemptitate⁴ non foret incommunicabilis existencie.

[ENGLISH]

## ¶6 · 218.13–218.22

> [p. 218] Item si in casu posito Verbum sit multi homines differentes, ut puta Iesus, Petrus, Paulus; tunc illi homines differunt potissime per sua principia intrinseca, scilicet per corpus et animam; sed non in hoc differunt homines; ergo non restat in eis principium differendi. Minor probatur eo quod omnis homo habet omne corpus humanum vel animam suam partem, et per consequens per appropriatas habitaciones talium non est dare distinccionem hominum. Antecedens patet per Doctorem: concedit⁵ enim⁵ quod Iesus est Petrus, et tamen illi non sunt unus homo, sed duo homines.

[ENGLISH]

## ¶7 · 218.23–218.32

> [p. 218] Ex prima parte sequitur quod Iesus habet corpus et animam Petri tanquam suas partes, et per idem omnem partem qualitativam hominis. Sicut⁶ enim conceditur ex posicione⁷ quod homo Christus Iesus⁸ creavit stellas, quia Verbum, quod est Iesus Christus,⁹ sic fecit; et ita de quibuscunque predicatis personalibus, que Verbo conveniunt, cum homo concretum sit terminus personalis; ita concedi debet quod iste idem homo componitur ex corpore Petri et eius anima, sicut Verbum, quod est iste homo, ex eis¹⁰ componitur.¹¹

[ENGLISH]

## ¶8 · 219.1–219.33

> [p. 219] Quoad 2ᵈᵃᵐ partem non video colorem in dicto, nisi per homines appropriate intelligat humanitates; et tunc foret proposicio sibi impossibilis; vel aliter concedat quod Verbum est omnes illi homines; et per consequens, Iesus est Paulus, cum hec nomina personalitatem¹ significant. Sed iste homo non est iste homo, cum tale subiectum cum persona Verbi connotat individuacionem, ab isto corpore et ista anima non personaliter sed simpliciter. Sed tunc videtur concedendum quod iste homo non potest istam naturam dimittere vel aliud corpus et aliam animam assumere; nec quod ille homo fuit, antequam fuit homo; et per consequens non creavit mundum, nec est Deus; et per consequens Verbum non est isti multi homines sicut prius, cum non sit eorum personalis assumpcio; cum tunc persona eterna foret quilibet eorundem. Et perirent tales sillogismi in quocunque modo —omne Verbum divinum est Iesus; omnis homo compositus ex corpore Petri et eius anima est Verbum divinum; ergo omnis homo compositus ex corpore Petri et eius anima est Iesus—. Et sic arguendo in 2ᵈᵒ modo prime figure— nullus homo compositus ex corpore Iesu et eius anima est² homo Petrus; sed omne Verbum divinum est homo compositus ex corpore Iesu et eius anima²; ergo nullum Verbum divinum est homo Petrus—et sic de ceteris quibuslibet sillogismis. Nec tollit³ ista responsio raciones predictas quin, si⁴ Verbum sit multi homines, tunc est multe substancie vel nature, et sic multe persone; et per consequens simpliciter creatura; quod negat posicio. Nam Deus in casu isto est mille⁵ res et quelibet earundem, et per consequens quelibet earundem⁶ mille verum est Deus; et cum non eternaliter essent Deus, sequitur quod⁷ inceperant esse Deus; ex quo sequitur quod⁷ sunt creature; et sic Deus esset multe creature et quelibet earundem; quod non sapit,⁸ nisi concedatur humanitatem esse⁹ Christum.⁹

[ENGLISH]

## ¶9 · 220.1–220.22

> [p. 220] Item si Christus in tali casu sit multi homines, tunc dimittendo paulative naturas assumptas multi homines per ordinem desinerent esse Christus; quia dimittendo naturam Petri non remaneret ille homo; quia sic per assumpcionem paulativam non fieret multi homines, sed remaneret precise idem homo. Concesso ergo consequente videtur primo quod aliquid desinit esse Christus, quia aliquis homo, et per consequens natura¹ creata¹ est Christus. Patet deduccio querendo sollicite, quid est illud quod desinit esse Christus. Nam si omnis homo, qui nunc est Christus eternaliter fuit Christus, tunc non multi homines sed solum Deus est Christus. Concesso ergo quod per dimissiones huiusmodi paulativas alique res, quia aliqui homines, desinerent² esse Christus; tunc palam sequitur quod multe substancie create forent Christus, cum quelibet illarum rerum, que desinerent esse Christus, non foret natura vel substancia divina, sed alia: et cum non ad dimissionem huiusmodi consequitur alicuius rei corrupcio; sequitur cum veris quod ille res, que desinerent² esse Christus, remanerent non-Christus; et non superest que foret talis res derelicta, nisi foret assumpta humanitas; ergo relinquitur³ concedendum quod humanitas assumpta foret Christus; et hoc videtur michi sequi formaliter si Christus ex unione ypostatica sit multi homines.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 216:
1 alia C.

p. 217:
1 quod O.
2 expositorie A B C.
3 posito B.
4–4 tunc . . . sunt om. O.
5 homines om. A.
6 reducitur O.
7 dicantur O.
8 deus B; divinitas O.
9 posito om. A B C.
10 modo om. A B C.
11 videtur . . . homines om. C O.
12 qua B.
13 est A B C.
14 conclusio A B C.
15 precise (an potius per se ?) om. cum lacuna iii litt. O.
16 multitudinem om. O.
17 substancie om. O.

p. 218:
1 supponente B; suppo^te O.
2 humane *om.* A B C.
3 est *om.* O.
4 ydempti^te A B C.
5 concedit enim *om.* C.
6 sic AB.
7 expositorie A B C; *cf. p.* 217, *n.* 2.
8 Iesus *om.* O.
9 Christus *om.* O.
10 ex eis *om.* O.
11 ex corpore Petri et eius anima sicut verbum quod est ille homo *add.* O.

p. 219:
1 recipiant add. B.
2-2 est . . . anima om. C.
3 valet B.
4 sic pr. man. A B C.
5 multe A B C.
6 earum A B C.
7-7 inceperant . . . quod om. O.
8 capit O.
9-9 humanitas . . . Christus O.

p. 220:
1–1 nulla creatura B.
2 desiverint O.
3 derelinquitur B C.
4 idem A B C.
5 iuxta *om.* C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 216: [Confirmat aliorum sentencias quod, si omnes humanitates assumeret, tunc nec foret unus homo nec muHi homines, sed et unicus atque multi ; et sic concordat modemorum sentencias cum antiquis. Assuming, as proved in the last chapter | the truth of the dictum of St. Thomas that if Christ assumed many humanities, He would be many men : the modem vieu) is supported that He assumed | humanities, and was thereby both | and also many men ; and thus opinions are reconciled ancl the unity of truth established.']
```

---

## Chunk 13-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-13-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-13-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "220.23–223.16"
divisions: "cap. 13 (heading 'Cap. XIII.' at 216.0); part 2 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "741 words; 741 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n259–n262 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 13, part 2: [TITLE]

## ¶1 · 220.23–221.3

> [p. 220] Propter tales evidencias dicit Doctor Subtilis super 3° Sentenciarum Distinccione prima Questione 3ᵃ quod, si Christus multas humanitates assumpserit, non esset multi homines nec unicus homo; sed et istud⁴ debet catholicus concedere tanquam sequens. Nam Christus non esset unicus homo, si multas humanitates assumpserit iuxta⁵ proximo capitulo declarata; nec esset multi homines iuxta proxime replicata; ergo conclusio. Certum est tamen quod esset homo, si sic esset. Nam si essent multe uniones ypostatice humanitatum ad Verbum, tunc aliqua humanitas foret ypostatice copulata; et omnis talis unio ponit secundum [p. 221] communicacionem ydiomatum Verbum esse hominem; ergo hoc posito Deus foret unus homo, et per idem multi homines.

[ENGLISH]

## ¶2 · 221.4–221.17

> [p. 221] Item impossibile est Deum esse hominem postquam non fuit homo, nisi per novam ypostaticam unionem. Sed, dimissis omnibus humanitatibus assumptis usque ad unam, foret Verbum homo sine nova ypostatica unione: ergo per ante erat stante ista unione continue idem homo. Si enim Verbum omnem humanitatem assumeret, non exinde periret sed perficeretur species humana, ut patet ex dictis; sed cum non posset¹ esse species hominis sine individuo hominis, quia destructis primis² substanciis² impossibile est aliquod aliorum remanere; sequitur quod illo posito foret homo aliquis singularis nullus si non Christus; ergo illo posito Christus foret unus homo. Quod ego non verto in dubium; sed credo quod ex Spiritu sancto diversificate sunt iste tres sentencie per locum a sufficienti divisione.

[ENGLISH]

## ¶3 · 221.18–221.26

> [p. 221] Quarum prima, ut sanctus Thomas cum suis sequacibus, dicit, quod Christus assumendo multas humanitates foret multi homines consequenter: 2ᵈᵃ opinio modernorum loquencium dicit quod Christus ·hoc posito foret solummodo solus homo: 3ᵃ Doctoris subtilis dicit quod hoc posito nec foret multi homines nec unicus homo tantum. Et quamlibet illarum sentenciarum credo esse absolute necessariam, cum Verbum nullam humanitatem potest assumere preter Dominum Iesum Christum.

[ENGLISH]

## ¶4 · 221.27–222.12

> [p. 221] Ideo opposito posito est quidlibet formaliter inferendum. Et patet concordancia doctorum in infringibili³ stipite veritatis; et per idem plane sequitur quod non multe persone divine possunt eandem humanitatem assumere eo quod tunc essent idem homo ad ydemptitatem humanitatis, ut dicit prima sentencia; essent eciam multi homines propter multitudinem personarum, quarum quelibet foret homo, ut dicit 2ᵈᵃ sentencia; essent 3° nec unicus nec multi, ut dicit [p. 222] 3ᵃ sentencia, eo quod denominaciones multiplicantur vel ydemptificantur ex multiplicacione vel ydemptificacione formarum; cum omnis forma sit essenciam vel personam in aliquo formaliter se habere; multe ergo humanitates forent multas personas esse homines, et una humanitas foret essenciam esse unum hominem. Sed certum est, si multe¹ persone divine sunt¹ unus homo, sunt et una persona, et sic eadem creata substancia, et per consequens persona eadem foret quelibet persona divina; et sic foret nedum confusio personarum, sed persona illa communis creata et assumpta foret cuilibet persone divine ydemptificata; quod esse non potest.

[ENGLISH]

## ¶5 · 222.13–223.16

> [p. 222] Et per idem nec Pater nec Spiritus sanctus potest humanitatem assumere; quia non eandem quam Verbum, ut patet ex dictis; nec alias separatas, quia deficit principium iniciantis,² mittentis, vel principiantis Patrem incarnandum. Quamvis enim tota Trinitas incarnavit Verbum et misit Spiritum sanctum, hoc tamen solum³ originaliter fit ex Patre, ‘qui sic dilexit mundum, ut Filium suum unigenitum daret,’ Ioh⁴ 3°; cum sic⁴ fuissent tres Filii Dei; et, cum non adoptivi, omnes fuissent filii naturales; quod esse non potest. Et 3° Deus foret triplex substancia, quia tres persone hominum; et de lege evangelica quilibet subiectus et obediens cuilibet; et in casu Pater in divinis filius vel nepos naturalis Filii vel Spiritus sancti, et sic sibi⁵ obediens tanquam superiori, ut Abraham offerebat Melchisedech ad Heb. 7°. Ymo, quantumcunque extraneas cognaciones assumpserint, forent plus convenientes quam cognati aliqui vel germani; cum omnes sint eadem essencia singularissima, eadem latria adorandi. Et sicut in divinitate nullus reliquo plus colendus sit, sic⁶ secundum humanitatem nullus honore alteri⁷ preponendus; et per consequens non foret eorum facilis cohabitacio propter repugnanciam maioritatis in [p. 223] susceptis hominibus, et occasionem date opinionis, quis altero sit melior; cum in doctrina, conversacione, et merito differrent ab invicem, sicut in personalitate et humanitate assumptis secundum quotlibet condiciones individuantes. Que si appareant nobis non sequi vel non esse inconveniencia plus quam Verbum esse hominem, tamen satis est quod sanctis appareat hoc non posse essencie¹ divine competere, nec ex scripturis vel racionibus edoceri sic posse fieri. Ad quid ergo sollicitaremur aggravantes fidem circa illud quod absolute necessarium est non esse? Non,² ymo si problema³ de possibilitate⁴ talium⁵ non fuerit nichil venturum,⁵ ego non vagarer circa conclusiones, que illo posito sequerentur; sed pie dubitarem possibilitatem casuum; nec admitterem casus huiusmodi cum suis sequentibus, nisi aliunde michi fuerint evidentes, ne forte sustinerem repugnans fidei arroganter, pertinaciter, vel aliter viciose.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Johniii. 16. (222.20); reference Heb. vii. i. (222.27).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 220:
1–1 nulla creatura B.
2 desiverint O.
3 derelinquitur B C.
4 idem A B C.
5 iuxta *om.* C.

p. 221:
1 possit O.
2–2 priñs (i.e. principiis) O.
3 singulari O.

p. 222:
1–1 multe . . . sunt *bis* B.
2 inicantis *om.* O.
3 solum *om.* B.
4–4 ioh . . . sic *om.* O.
5 eis O.
6 nec *add.* A B C.
7 alterius O.

Wait, I need to check the readings and the formatting rules against the image. The image shows "inicantis" in a form I read as "iniciantis", and "om." is printed as "o*m*." with a damaged mark.

1–1 multe . . . sunt bis B.
2 iniciantis om. O.
3 solum om. B.
4–4 ioh . . . sic om. O.
5 eis O.
6 nec add. A B C.
7 alterius O.

1–1 multe . . . sunt bis B.
2 iniciantis om. O.
3 solum om. B.
4–4 ioh . . . sic om. O.
5 eis O.
6 nec add. A B C.
7 alterius O.

p. 223:
1 decencie O.
2 non om. A B C.
3 probleuma A B; propleuma C.
4 a verbo possibilitate usque ad verbum aliquid infra l. 24, sequitur alia manus in cod. A.
5–5 talium fuerint mihi neutram A B C.
6 sint C.
7 quod nunc [?]ecurrit prima manus in cod. A, cf. not. 4 supra.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 223: sequitur alia manus in cod. | cf. not.
```

---

## Chunk 13-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-13-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-13-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "223.17–227.32"
divisions: "cap. 13 (heading 'Cap. XIII.' at 216.0); part 3 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1109 words; 1105 confirmed by Fordham or the vote; 4 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n262–n266 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 13, part 3: [TITLE]

## ¶1 · 223.17–225.5

> [p. 223] Unde miror quomodo moderni negantes Christum esse creaturam, et cum hoc admittentes tres personas divinas eandem humanitatem vel tres omnimode separatas assumere, dicunt quod substancia divina est tres homines et per consequens tres substancie; non enim tres substancie increate, cum tunc eternaliter ita essent. Si autem sit⁶ tres create substancie, tunc tres creature forent substancia divina per conversionem; et sic aliquid quod⁷ prius non fuerat. Si enim iste tres substancie differunt personaliter, tunc tres persone divine sunt tres substancie, quas notum est oportere distingui a communi divina substancia. Et si dicatur quod, postquam eternaliter erant persone et non substancie, facte sunt substancie, hoc est equivoce ad eternam substanciam vel personam; quia aliter unica substancia et non plures foret Trinitas increata. Et multo evidencius si tantum una humanitas sit assumpta a tota Trinitate, non essent tres [p. 224] materiales substancie, ut puta tria animalia vel tria corpora; et sic de ceteris passionibus humanis cum ceteris accidentibus separabilibus; quia adequatum corpus, compositum ex isto corpore et ista anima, est omne animal quod est homo in dato situ, eo quod eadem sunt principia singulorum, ut deductum est superius. Ymo videtur quod quilibet illorum trium hominum habeat peccatum maximum naturale, cum quilibet caret proprio capite, et sic de ceteris organis quibuscunque; et per idem sunt unum¹ corpus tantum. Licet autem tres persone assumendo tres homines forent indubie tres create substancie; tamen inconveniens est quod increata substancia sic plurificetur² in multas substancias, cum divina substancia non in plura dispergitur, sed in ipsam omnis pluralitas creature unite³ colligitur; quamvis enim Verbum sit due substancie, divina scilicet et humana, divina tamen substancia est tantum una substancia, cum non sit substancia creata: accipiendo enim huiusmodi substanciam pro natura et substanciam personaliter, sic non ponitur⁴ in numerum cum divina,⁵ cum sit ipsa. Unde videtur quod subiectum abstractum contrahat predicatum ad supponendum simpliciter pro natura, quando sic dicitur—substancia divina est substancia creata—et per consequens proposicio est neganda. Sed cum subiecto personali conceditur quod Verbum est substancia creata, quia homo et humanitas, quod non est deitas. Cuius racionis diversitas est variacio a supposicione simplici in personalem secundum limitacionem personalis termini vel abstracti. Et tunc non oportet concedere quod substancia increata sit creata substancia; licet Verbum, quod est increata substancia, sit creata substancia. Trinitas ergo foret in casu illo tres create substancie; et per consequens necessaria⁶ esset ad⁷ finem attingendum⁷ tanta in Deo pluralitas naturarum; quod est impossibile; cum ad redempcionem humani generis, ad beatitudinem hominis secundum [p. 225] corpus et animam, et quemlibet alium effectum eque sufficit Christi incarnacio, sicut incarnacio horum trium. Sicut ergo non sunt ponendi plures dii propter impossibilitatem superflui, sic nec plurium personarum incarnacio propter causam consimilem.

[ENGLISH]

## ¶2 · 225.6–225.20

> [p. 225] Ponunt autem doctores congruenciam¹ in Christo quare incarnatus est et nec Pater nec Spiritus sanctus. Primo quia² Verbum,² quod est naturalis ymago Patris; per quod factus est homo ad Dei ymaginem, per eandem ymaginem debuit reformari. Unde ex proprietate ymaginis fuit consonancius quod ymago ymaginem assumeret, quam potencia vel benevolencia alterius persone. Forme enim est reformare deformitatem; sapiencie vincere peccati maliciam remissibilem ex ignorancia contractam; et ymaginis exemplaris fabricam turpatam ad dictam ymaginem prius factam [revocare].³ Verumptamen sicut vir non peccavit nisi excitante muliere et dyabolo, et sic iuvamine alterius⁴ debuit relevari:⁵ sic nec persona Verbi fecit redempcionis misterium sine coefficiencia Trinitatis, aliter tamen Verbum quam duo alii.

[ENGLISH]

## ¶3 · 225.21–225.31

> [p. 225] 2ᵈᵒ cum Verbum sit Dei Filius naturalis, habet in⁶ Trinitate⁶ principium a quo mittatur, in cuius auctoritate vel virtute operetur obedienter humanitus. Unde filiacio temporalis habet proprietates analogas in Filio naturali aliter quam haberet in Patre vel Spiritu. Nam utrobique nascitur ex suo principio, et manet Filius faciens nos filios adoptivos⁷ et⁸ heredes, ut ipse est primogenitus;⁸ et hoc sine confusione filiorum⁹ cognacionis in Deo, quod Patri innascibili non potest competere. Et si iste conveniencie videntur nobis ignaris modice, tamen sunt apud Deum, qui ponderat cuncta, ad regulam infringibiliter perficiende.

[ENGLISH]

## ¶4 · 226.1–226.24

> [p. 226] 3° concludendo¹ breviter, non est aliqua Verbi proprietas quin limitat Verbo² congruere² incarnacionis misterium ultra quam aliis. Mediam quidem³ personam oportet esse mediatorem Dei et hominum; Verbum eternaliter de corde ingenito eructatum decet verbis predicacionis ostendere Patrem suum Ioh. 17°. ‘Pater, manifestavi nomen tuum;’ ‘Dei virtus atque Dei sapiencia,’ prima ad Cor. 1°, debuit vicium ex ignorancia superare;⁴ ut homo, qui⁴ in sapiencia conditus est per insipienciam perditus appetendo equalitatem increate sapiencie, per illam sapienciam restauretur, et dyabolus usurpando acceptam virtutem et potenciam⁵ per dantem⁶ virtutem et⁵ bracchium deprimeretur, Luc 1°. ‘fecit potenciam in bracchio suo.’ Et sicut secundum Augustinum est equalitas immediate consequens ad suum principium, sic ab eo specialiter omnis morbi inequalitas ad temperanciam reducatur: ut inequalitas sanitatis in qua dyabolus cecidit, appetendo equalitatem divine auctoritatis sive potencie, secundum iudicium datum Filio per impotenciam puniatur, qua non possit a peccato in Spiritum⁷ sanctum resurgere; inequalitas autem, in qua homo ignoranter peccando in sapienciam, stulte appetendo eius equalitatem, ceciderat, est⁸ precise equalitatis terminus,⁹ cum sit sapiencia, verbum, virtus, pulcritudo, et species reducenda; et ita de ceteris sacramentis que scriptura de Christo commemorat.

[ENGLISH]

## ¶5 · 226.26–226.30

> [p. 226] Redeundo igitur ad propositum ex dictis colligitur quod quelibet trium predictarum opinionum sentenciat¹⁰ fidei consonum quoad superius recitatum. Et sic concordande sunt apparentes doctorum repugnancie in tam alta materia fidei Christiane.

[ENGLISH]

## ¶6 · 226.31–227.26

> [p. 226] Quod si obicitur omnes tres sectas concorditer admittere quod quelibet persona¹¹ divina eandem naturam assumat [p. 227] vel quotlibet¹ separatim; dicitur tripliciter concordando istam radicem. Primo quod in ista materia opinative locuti sunt nichil temere asserendo, ut patet ex scriptis eorum. 2ᵈᵒ quod ipsi intelligunt ipsam possibilitatem condicionaliter, si Deus voluerit; ad modum loquendi Anselmi. Vel 3° si replicando inutiliter de sensibus eorum argueretur, quod ipsi sic simpliciter sencierunt, potest dici quod non ad laudem eorum opinio eorum forsitan fuit talis. Et taliter glosant ipsi superiores doctores, quorum sensus pocius debet credi. Sed non valet—si isti sic senciunt opinando; ergo verum—cum per idem contradiccio sequeretur; ipsi enim discrepant a seipsis. Sed et sanctus Thomas super Dist. 6. 3ⁱⁱ Sentenciarum Questione....,² dicit quod sentencia concedens humanitatem assumptam esse Christum non est heretica, licet sit impossibilis in precipua materia fidei. De quo miror, cum tot sancti doctores qui in aliis materiis ambigue sunt locuti, illam sentenciam in materia fidei affirmaverant tam constanter. Cum ergo pium et salubre foret de fide Christiana sentenciam impossibilem tocius fidei corruptivam investigando excludere, videtur quod ecclesia sollicite discuteret quid in ista materia foret catholice sustinendum; quia certum est quod una pars est formaliter impossibilis; ex qua sequitur oppositum tocius fidei, ymo ut noverunt logici, quidlibet inferendum; et talis latens error in principio per vias inopinatas infirmat partes fidei consequenter.

[ENGLISH]

## ¶7 · 227.27–227.32

> [p. 227] Sed forte preter instancias factas superius arguitur possibilitas trium casuum abiectorum, scilicet quod quelibet persona divina indifferenter poterit incarnari; quia eadem persona multas humanitates simul vel successive potest assumere et quocienslibet potest dimittere; ac 3° quod multe possunt eandem humanitatem assumere.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Luke i. 5i. (226.13).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 223:
1 decencie O.
2 non om. A B C.
3 probleuma A B; propleuma C.
4 a verbo possibilitate usque ad verbum aliquid infra l. 24, sequitur alia manus in cod. A.
5–5 talium fuerint mihi neutram A B C.
6 sint C.
7 quod nunc [?]ecurrit prima manus in cod. A, cf. not. 4 supra.

p. 224:
1 unicum O.
2 plurificaretur A B C.
3 univoce A B C.
4 potest A B C.
5 substancia *add.* A B C.
6 necessarium O.
7–7 ad finem a . . . *cum lacuna* C; ad finem aliquem O.

p. 225:
1 convenienciam A B C.
2-2 quia verbum om. O.
3 aut revocare aut aliquid simile sensui necessarium est.
4 aliter quam dyabolus add. A B C; alter quam dyabolus add. O. nempe utraque lectio ut glossa omittenda.
5 revelari O.
6 intrinsece A B C.
7 adopcionis O.
8-8 et ... primogenitus bis. O.
9 vel add. C O.

p. 226:
1 concludo O.
2 congrue (om. verbo) O.
3 quippe O.
4–4 homo autem A B; ut autem C; ut qui O.
5–5 potenciam . . . et om. B.
6 datam A B C.
7 peccatum C.
8 per add. O.
9 terminum O.
10 senciat fide O.
11 natura B.

p. 227:
1 quotlibet (litt. t in rasura al. man.) A; quidlibet B; quodlibet C.
2 lacuna pro numero in codd. omn.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 223: sequitur alia manus in cod. | cf. not.
p. 225: de f° rmed - | nempe utraque lectio ut glossa omittenda.
p. 227: si Deus voluerit
```

---

## Chunk 13-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-13-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-13-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "227.33–232.7"
divisions: "cap. 13 (heading 'Cap. XIII.' at 216.0); part 4 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1112 words; 1109 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n266–n271 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 13, part 4: [TITLE]

## ¶1 · 227.33–228.3

> [p. 227] Primo generatur ex hoc quod precipui moderni doctores catholici et subtiles in scripturis reliquerant possibilitates [p. 228] omnium istorum casuum cum suis probacionibus et solucionibus obiectorum; quod non est veri simile de talibus ac tantis doctoribus nisi subsit possibilitas eorundem: ergo etc.

[ENGLISH]

## ¶2 · 228.4–228.21

> [p. 228] Hic dicitur ut supra quod variacio in methaphisica et honoris extraneandi ambicio est in causa. In cuius signum vix duos invenies quin discordent. Alii autem superiores doctores ut Augustinus, Ieronimus, Gregorius, et Anselmus cum suis sequacibus dicunt concorditer quod Christus post incarnacionem est aliquid, quod prius non fuerat, ut patet superius; et illi concordant cum racione, et verbaliter ac sentencialiter cum scriptura. Nec sequitur ex illo quod posteriores erant heretici, cum sentenciam hereticam potest catholicus sine pertinacia defendere, sicut credo in proposito contigisse. Verumptamen vanum est excludere illos simpliciter a peccato; cum laborando circa¹ veram sentenciam secundum studium bonum² de genere contingit catholicum presumptiva superbia vel³ inani gloria peccare facillime; quanto magis defendendo impossibile, licet intencio secundum aliquid sit recta et vera sentencia: quodlibet enim⁴ impossibile disperiret,⁵ si per se sine mixtura veri defensum fuerit!

[ENGLISH]

## ¶3 · 228.22–228.26

> [p. 228] 2ᵈᵒ obicitur per raciones sancti Thome Questione 7. 3ⁱⁱ et duabus sequentibus. ‘Omnis, inquit, necessitas et impossibilitas Deo subicitur.’ Cum ergo voluntati Dei omnis impossibilitas subicitur, sequitur quod Patrem incarnari non sit sibi impossibile.⁶

[ENGLISH]

## ¶4 · 228.27–229.8

> [p. 228] Hic videtur michi quod argumentum peccat tam in materia quam in forma. In materia, quia solum veritas Deo subicitur; nulla impossibilitas est veritas; ergo assumptum peccat. Quod si intelligamus per impossibilitatem signi impossibilis falsitatem vel veritatem negativam, que est absoluta necessitas, nichil ad propositum; sed ad oppositum adducitur. Nam non prodest quod hoc signum sit impossibile—Pater [p. 229] potest incarnari—vel—quod necessario non potest esse quod Pater potest incarnari—ad concludendum propositum. Nec oportet instare pro improbacione argumenti, cum reductum ad formam patenter peteret; sicut facit secundum argumentum, quo capit humanam naturam infinitum distare a qualibet persona divina, et omnium¹ eque distancium est eque possibilis coniunccio. Nam maior est impossibilis, et sensus minoris petitur.

[ENGLISH]

## ¶5 · 229.9–229.10

> [p. 229] 3° arguitur ex hoc quod posse assumere carnem est dignitatis² in Filio; ergo Patri potest competere.

[ENGLISH]

## ¶6 · 229.11–229.14

> [p. 229] Sed iuxta illud sequeretur quod gigni conveniat Patri, cum sit dignitatis in Filio. Dicitur ergo cum isto sancto quod Deus non potest incarnari in persona alia de potencia ordinata; sed, si voluerit de potencia absoluta.

[ENGLISH]

## ¶7 · 229.15–229.30

> [p. 229] Et conformiter dicitur ad argumenta quibus videtur probare quod eadem natura potest assumi a qualibet personarum. Primo ex hoc quod omnis humanitas est indifferenter ad ymaginem Trinitatis, et³ illa est racio assumendi; ymo cum Verbum humanitatem assumpserit,⁴ est ipsa similior et habilior⁵ ut ab utraque reliqua assumatur. Constat quidem quod faccio ad ymaginem Dei non est communis racio ut quelibet humanitas⁶ a qualibet⁶ persona assumi poterit, quia sic omnis homo posset esse Trinitas increata; sed Christo inest racio singularis, unde ille singulariter a Verbo assumi poterit; et petitur utrobique probandum. Unde multum distat unio potenciarum anime eidem organo et⁷ unio humanitatis ad Filium; ita quod non sequitur per locum a simili—si multe potencie anime possunt simul uniri eidem organo,⁷ ergo per idem multe persone divine possunt uniri⁸ ypostatice eidem corpori—.

[ENGLISH]

## ¶8 · 229.31–230.18

> [p. 229] Quod si queratur⁹ racio diversitatis, satis est quod hoc facto tres persone possent¹⁰ esse unus homo et quelibet [p. 230] persona divina multi homines; sicut consequenter annuit sanctus Thomas, et¹ hoc posito non sic esset, ut patet ex dictis. Quantum ad argumenta, que facit Doctor subtilis in principio 3ⁱⁱ pro hac parte, respondet ipsemet satis clare. Quod si addatur— Verbum divinum liberius copulatum Christo quam aliquam² carnem carni ypostatice copulatam; sed anima potest multis carnibus copulari; ergo multo magis Verbum alii humanitati—; dicitur quod consequencia non valet per locum a simili. Nam Verbum liberius produxit hoc tempus perpetuum quam Petrus hunc filium; et tamen Verbum non potuit produxisse aliud tempus, quod nec sit illud nec eius pars, licet Petrus potuit alium filium produxisse, ymo filium qui non fuisset pertinens huic nato. Conceditur tamen quod quamcunque carnem spiritus assumpserit vel sibi personaliter uniret,³ foret solummodo idem homo. Et sic licet homo posset esse aliud quam est modo, quia alia natura corporea, non tamen aliud suppositum vel persona, ut patet in materia De Anima.

[ENGLISH]

## ¶9 · 230.19–231.22

> [p. 230] Ex istis colligitur quomodo aliqua insint Verbo pure in quantum Deus; aliqua⁴ in quantum homo; et⁴ aliqua mixtim. In quantum Deus, creavit mundum; in quantum homo, passus est mortem; et in quantum Deus et homo, redemit hominem. Nec debet signum reduplicatum intelligi utrobique, ut dicat⁵ consequenciam formalem logicam et causalem; sicut hic Christus in quantum homo est creatura; sed et⁶ quomodolibet dicit causam, ut licet potest esse Deus et non produxisse mundum, tamen deitas fuit⁷ causa quare produxit mundum et non sua humanitas. Et licet deitas fuit⁸ causa quare paciebatur, non tamen secundum illam; quia tunc fuisset causa formalis vel⁹ subiectum passionis; conceditur tamen quod humanitas fuit causa⁹ formalis Christi et causa subiectiva mortis: et sic in quantum homo passus est mortem, quia secundum humanitatem. Et [p. 231] intelligendum est in quantum, ut dicat¹ generaliter causam² quamlibet parcialem vel totalem, completam vel incompletam. Ego non video quin sane concedi poterit quod, in quantum Deus, paciebatur; cum deitas fuit per se causa illius passionis, sed non secundum deitatem, cum tunc deitas principaliter pateretur. Redempcio autem humani generis pro offensa dicit infinitatem precii proporcionaliter ad delictum; et sic oportet redimentem esse precium infinitum; et per consequens Deum; et preter hoc oportet quod distinguatur essencialiter a solvente, cum non sit possibile quidquam³ mercari primo et immediate secundum seipsum; et per consequens oportet precium, quod secundum deitatem est infinitum, esse naturam alienam⁴ creatam. Cum autem nulla alia potuit pertinere nisi illa que peccaverat, que compendiosissime sit⁵ et satisfaciens et precium, mercans et mercatum, reconcilians et reconciliatum; relinquitur quod oportet ipsam esse humanitatem ‘mediatorem⁶ Dei et hominum, hominem Christum Iesum.’ Et sic quidquid infuit sibi formaliter,⁷ infuit sibi⁷ in quantum Deus; licet non omne, quod sibi infuit, inerat secundum quod Deus, nec in quantum homo. Deitas enim fuit per se causa cuiuscunque causati, quod sic infuit Iesu nostro.

[ENGLISH]

## ¶10 · 231.23–231.31

> [p. 231] Et si obicitur quod Christus, si in quantum Deus moriebatur, tunc est de racione Dei mori, et indifferenter quelibet persona divina morietur; patet quod consequencia non valet; cum non sit de racione hominis ita mori, cum homo posset esse naturalissime et nec mori⁸ nec esse mortalis, id est non habere aptitudinem naturalem nec necessitatem preternaturalem, ut suo tempore moriatur. Ideo tales reduplicative sumuntur satis equivoce ut patet in logica, quam equivocacionem specialiter in illa materia oportet attendere.

[ENGLISH]

## ¶11 · 231.32–232.7

> [p. 231] Ex dictis⁸ ergo patet quodammodo qualiter scriptura sacra cum antiquis sanctis doctoribus in materia de Incarnacione [p. 232] Domini ad litteram est sustinenda; et quomodo iacula sophistica modernorum sunt scuto veritatis infallibilis repellenda, ac eorum discordancia equivoca detegenda; ut sic possit theologus in tractando dubia Incarnacionis realia libere sine formidine impugnacionis sophistice procedere in dicenda ad laudem, gloriam, et honorem eiusdem Domini nostri Iesu Christi. Amen.¹

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 229: *incarnari—vel—quod* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 1 Tim- 5- (231.17).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 227:
1 quotlibet (litt. t in rasura al. man.) A; quidlibet B; quodlibet C.
2 lacuna pro numero in codd. omn.

p. 228:
1 circa (i.e. omittendum) B.
2 hominum O.
3 vel om. A B C.
4 libet om. A B C: pro quidem in omn. codd. inventum enim supposui.
5 disparet[?] A; disparet B C.
CHECK: the figure 1 is not visible before "circa (i.e. omittendum) B." at the top of the apparatus, so the entry may be cut off or continued from above. In entry 5 the first "disparet" looks struck through or overprinted, so its reading is uncertain.
CHECK (coordinator): text figure(s) 6 have no entry read here: read the plate foot before citing.

p. 229:
1 omni A B C.
2 dignitas A B C.
3 in add. O.
4 assumpsit O.
5 humilior A B C; hîlior O.
6–6 humanitas a qualibet om. O.
7–7 et . . . organo om. B.
8 pro uniri codd. A B ad finem sentencie copulari exhibent; cod. C. neutrum habet.
9 queritur A B C.
10 possunt A B.

p. 230:
1 in O.
2 aliam C O.
3 unierit C; vineret O.
4–4 aliqua . . . et om. O.
5 ut dicat om. O.
6 in O.
7 divinitas sint O.
8 divinitas sit O.
9–9 vel . . . causa om. C.

p. 231:
1 dicit *codd. omn.*
2 causam *om.* B.
3 quemquam O.
4 aliam O.
5 sit *om.* A B C.
6 mediatorem *om.* A.
7–7 formaliter . . . sibi *om.* B.
8 mîori O.
9 istis A B.
CHECK: the main text carries figures 1–8 only (7 and 8 twice), but the foot has an entry for 9, which has no figure in the main text visible here. The main text's figures 1–6 are not visible in this part of the page.
CHECK (coordinator): entry figure(s) 9 have no figure in the transcription: read the plate foot before citing.

p. 232:
NONE
CHECK (coordinator): text figure(s) 1 have no entry read here: read the plate foot before citing.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 227: si Deus voluerit
p. 229: si voluerit de potencia ahsoluta.
p. 230: De Anima.
p. 231: in quantum,
```
