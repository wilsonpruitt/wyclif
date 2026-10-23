# Translation brief: incarnacione 10-a–10-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-10-a.md chunks/incarnacione/wyc-incarnacione-10-b.md chunks/incarnacione/wyc-incarnacione-10-c.md` once and fix what it reports.
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

## Glossary (the 331 rows these chunks use; the full file is GLOSSARY.md)

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
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| ecclesia laycalis / secularis | the lay church / the secular church | Ruled 2026-10-02 (154.15, 156.3). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| famosior | best-known [sense] | Pilot. |
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
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere (of the soul, the nature) | take up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| pars qualitativa | qualitative part | Body or soul as the parts that make up a man by kind; set against *pars quantitativa*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.5). |
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
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| mobilis / mobilitas | movable / movability | Of Christ's humanity (ch. 7). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.11). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| quiditativus | quidditative | Beside *quiditas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.24). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| univocare / univocari | make univocal / be univocal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.3). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| complexio | complexion | The mixture of qualities. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137–138). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| colorate | with colour enough | With a plausible ground (cf. *color*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.26). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| subsistencia | subsistence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 148.10). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ecclesia cesarea | the caesarean church | The church as endowed by Caesar; pairs with *clerus cesareus* (§B). Ruled 2026-10-02 (*Eccl.* 13). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| ordo per accidens | order by accident | Ruled 2026-10-02 (*Eccl.* 21, 514.29). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| suadere | make the case | To persuade, not to prove. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.2). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |

---

## Chunk 10-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "160.0–164.27"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 1 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1140 words; 1140 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n199–n203 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 1: [TITLE]

## ¶1 · 160.0–160.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 160] [Suadet 12 evidenciis quod humanitas assumpta sit Christus; et hoc roborat doctorum testimoniis et exemplis. The proposition that the humanity assumed is Christ proved by twelve arguments; and supported by the authority of the Fathers.]

[ENGLISH]

## ¶2 · 160.10–161.2

> [p. 160] Quia maior pars variacionis in ista materia stat in methaphisica de humanitate assumpta; ideo expedit iuxta ponere sentencias contrarias supradictis. Dicunt enim moderni concorditer¹ quod humanitas Christi nec est homo, nec suppositum, vel persona, licet sit substancia racionalis composita² ex corpore² et anima, que sunt partes hominis Iesu Christi; sed dimissa illa natura suppositacioni proprie,³ ut⁴ possit per possibile⁴ quod maneat non assumpta, tunc foret homo et modo non est homo. Ideo dicunt quod diffinicio hominis negacionem includit formaliter, ita quod descriptive homo sit substancia ex corpore et anima intellectiva composita⁵ non suppositata suppositacione⁶ aliena. Et quia ultima differencia deficit nature assumpte cum [p. 161] suppositatur suppositacione Verbi; ideo¹ stante assumpcione ypostatica non est homo.

[ENGLISH]

## ¶3 · 161.3–161.19

> [p. 161] Ista sentencia² iam famosa est michi et forte aliis magis difficilis quam aliqua sentencia antiquorum doctorum superius inculcata. Primo ergo videtur quod Christi humanitas non suppositatur suppositacione aliena: nam³ nec est nec fit suppositum: et omne suppositari est fieri vel esse suppositum: ergo non suppositatur. Preterea si aliqua suppositacione suppositatur cum illa nulli⁴ alii creature⁴ conveniat, videtur quod sit suppositacio sibi propria, et sic non aliqualiter aliena. Confirmatur ex hoc quod suppositacio qua suppositatur formaliter est solummodo temporalis et per consequens dependet ab illa humanitate, sicut accidens respectivum dependet essencialiter ab extremo. Quod si dicatur suppositacionem illam esse suppositum Verbi, tunc indubie cuiuslibet suppositi creati suppositacio dependet a suppositacione aliena, quia a supposito increato et ad illud finaliter terminatur; et per consequens nullum esset suppositum creatum.

[ENGLISH]

## ¶4 · 161.20–162.11

> [p. 161] Sed hic dicit Doctor Subtilis super 3° Sentenciarum Dist. 1ᵃ Questione articuli 3ⁱ quod est dare triplicem⁵ negacionem, sicut et triplicem dependenciam pertinentem. Aliquid enim⁶ actualiter dependet a suppositacione aliena, quando est natura completa suppositi nature superioris; ut humanitas Christi⁷ non est suppositum, sed natura suppositi Verbi; et si Verbum faceret ipsam esse non naturam persone⁸ superioris, tunc esset suppositum et persona. Nichil⁹ ergo deficit ad hoc quod sit persona nisi ista negacio quod non est natura suppositi superioris nature. Ideo suppositacio, quam habet in potencia terminatur suppositacione Verbi, que non actu sed potencia est aliena a suppositacione nature humane. 2ᵃ dependencia vocatur potencialis;¹⁰ quando scilicet [p. 162] natura racionalis dependet a supposito increato a quo potest assumi, sed nondum assumitur in unitatem persone; sed et talem negacionem oportet naturam creatam habere, ut sit persona¹ hominis. 3ᵃ est dependencia obediencialis,² qua omne suppositum substancie essencialis dependet a qualibet persona increata, sed eciam³ potest assumi in unitatem suppositi increati, ut sit communicacio⁴ ydiomatum, et ut ipso facto natura persone increate vere Deus sit lapis vel lignum vel cuiuscunque speciei substancie⁵ individuum; sicut Deus iam est individuum speciei⁵ humane, licet natura talis non possit esse⁶ persona divina.

[ENGLISH]

## ¶5 · 162.12–162.25

> [p. 162] Dimissa autem contencione verbali, quod suppositacio Verbi non est aliena a suppositacione nature assumpte, cum illa non sit; arguitur primo contra illud⁷ per hoc quod omnis homo-non-Deus per se est homo: omnis natura humana completa non assumpta est homo: ergo omnis talis natura per se est homo, et per consequens non potest vicissim nunc esse homo et nunc non-homo. Maior licet sit famosa apud philosophos potest⁸ ex hoc patescere, quia aliter humanitas non esset species vel quiditas cuiuscunque persone⁹ hominis; cum potest manere idem quod est modo¹⁰ et non homo. Non ergo predicatur homo in quid de aliquo supposito¹¹ humano; et per idem nulla potest esse per se species in genere substancie, cum omnis substancia potest esse idem quod est, et non esse individuum huius speciei.

[ENGLISH]

## ¶6 · 162.26–163.13

> [p. 162] Item impossibile est aliquid esse accidentaliter alicuiusmodi¹² nisi sibi insit accidens a quo est huiusmodi formaliter sicut patet ponenti respectus et accidencia distincta: sed omnis homo iuxta hanc viam accidentaliter est homo: ergo est dare formam accidentalem qua est homo formaliter. Sed et hoc concedunt plurimi dicentes quod in assumpcione ypostatica negacio supradicta corrumpitur et in dimissione [p. 163] ypostatica generatur: et per illam est homo formaliter aliquid positivum, ut nichil, in quantum caret visu vel non habet hoc vel illud, est aliquid. Ex quo sequitur quod nichil in quantum homo vel persona hominis est aliquid vel alicuiusmodi¹ positivum; cum quicquid aut cuiusmodicunque² homo nunc est, assistente negacione quod non suppositatur² suppositacione aliena, potest esse adveniente suppositacione aliena ipso facto non³ homine vel persona. Quod est contra Augustinum 7° De Trinitate 9° volente, quod persona in quantum huiusmodi, est aliquid, non ad aliquid. Si ergo nemo potest fieri qualis aut quantus nisi moveatur, multo magis nemo potest fieri homo cum hoc quod non exinde moveatur; aliter enim non esset generacio.

[ENGLISH]

## ¶7 · 163.14–163.33

> [p. 163] Item eo ipso quod forma inseparabilis inest⁴ mere formaliter alicui, ipsum denominat⁵: sed humanitas est forma inseparabiliter existens cuicumque nature humane: ergo si inest alicui singulari nature ipsam denominat⁵: sed non potest denominare quicquam primo formaliter nisi hominem: ergo, si inest nature create formaliter, ipsa est homo. Cum⁶ ergo humanitas manet continue in natura humana assumpta, videtur quod stante assumpcione erit homo continue sicut prius. Minor videtur ex hoc quod omnis homo est formaliter humanitate homo, sicut mobile movetur motu formaliter, album denominatur albedine, et paciens passione. Humanitas ergo manens post unionem denominat⁵ formaliter Christum esse hominem et non dicta negacio: ymo cum ipse sit homo⁷ nobiscum univoce et in⁷ sua racione, non oportet negacionem ponere, sed ipse humanitate est homo formaliter, videlicet⁸ quod eadem sit racio cuiuslibet fratris sui. Ipse enim non potest suppositari suppositacione aliena, nec negacione; sed humanitate oportet ipsum esse singulare speciei humane formaliter: ergo per idem et alios univoce consimilis speciei.

[ENGLISH]

## ¶8 · 164.1–164.27

> [p. 164] Item iuxta dicta De Universalibus omnis humanitas est suppositum humanum esse hominem: sed, posito quod Verbum assumat ypostatice naturam Petri, manebit ista assumpta humanitas: ergo manebit quod idem suppositum est homo; et sic personam manentem personam Verbum assumeret. Pro¹ assumpto non est facile fingere, quid sit humanitas, quam Apostolus vocat ‘formam servi,’² nisi esset³ hominis vel humana essencia. Et ex isto⁴ videtur quod alia nova humanitas incepit⁵ esse homo, quando Christus incepit esse homo, humanitate⁵ Petri extincta per assumpcionem; quia quod Verbum est homo, tunc incipit⁶ esse et quod Petrus est homo tunc desinit. Ex quo patet quod non assumpsit naturam Petri, cum illa natura manet modo⁷ tantum distans a Verbo ut prius. Nam illa res, que prius⁸ fuit suppositum Petri, nec est natura nec persona divina, nec est homo modo sicut nec Christus est natura humana: per antecedens⁹ vero ista res et Christus conveniebant in specie sic quod uterque fuit homo ut suppono¹⁰: ergo maior fuit conveniencia tunc quam modo. Nec valet dicere quod Christus est homo formaliter non negacione¹¹ nec humanitate, sed ypostatica unione; quia sic foret racio qua¹² Christus est homo multum equivoca a racione qua quicumque alius est homo¹³; quod indubie sequitur¹³ multiplici racione. Nam quilibet alius homo dicitur formaliter homo negative¹⁴ et per consequens racione increata; Christus autem dicitur homo per unionem ypostaticam, que nulli alii potest competere.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 160:
1 concorditer om. A B; conco C. 
2 ɔncorpe ex cor^e C.
3 pp^e (i.e. prope) O.
4–4 ut posito proporcionale A; ait posito per possibile B; ut posito possibile C.
5 composit O.
6 supp~~esitata~~ (rasura al. man.) A; supposicione B C.

Let me give the final version cleanly:

1 concorditer om. A B; conco C.
2 ɔncorpe ex cor^e C.
3 p̶pe (i.e. prope) O.
4–4 ut posito proporcionale A; ait posito per possibile B; ut posito possibile C.
5 composit O.
6 suppesitata (rasura al. man.) A; supposicione B C.

p. 161:
1 ymo B C.
2 sentenciam O.
3 et iam O.
4–4 nulli n^e (i.e. nature) O.
5 dare om. B.
6 enim om. O.
7 Christi om. O.
8 p^e codd. omn.: quod compendium etiam per se significare potest.
9 vel O.
10 personalis A B C.

p. 162:
1 pars A B C.
2 obediencialis om. A B relicto xii litterarum spatio: et sine spatio om. C.
3 et O.
4 communicacio om. C.
5–5 substancie . . . speciei om. O.
6 posset A B C; possit persona om. esse O.
7 idem A B C.
8 potest om. O.
9 per se B.
10 numero C.
11 supposito om. O.
12 modi om. A B C.

p. 163:
1 modi *om.* A B C.
2 supponitur A B C.
3 in O.
4 inest *om.* A B C.
5 denominant A B C.
6 et *add.* B.
7–7 homo unitate in (*spatio viii litt. relicto*) A B; homo unitate in C.
8 vī. (*i.e.* unde) O.

CHECK: the footnote figures printed at the foot are 1, 2, 3, 4, 5, 6, 7–7 and 8. The main text figures 1, 2, 2, 3, 4, 5, 5, 6, 5, 7, 7, 8 are mostly on the part of the page above the crop. The main text visible here shows only 5, 7, 7, 8. Figure 5 is printed once at the foot, and the entry 7–7 covers both figure 7s.

p. 164:
1 et add. A B C.
2 servi om. B.
3 esse A B C.
4 quo B.
5-5 incepit quando Christus incepit esse homo humanitate A B C; incepit esse homo humanitate O.
6 incepit C O.
7 non B.
8 prius om. O.
9 per ante A B C; per añ O.
10 supp° A B C.
11 non negacione om. O.
12 quia O.
13-13 homo et dubie sequitur quod O.
14 negacione A B C; netiẽ͡ O.
15 Christo om. O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 160: evidenciis quod humanitas assumpta sit Christus; et Jioc roborat doctorum testimoniis et exemplis. The proposition that the humanity assumed is Christ proved by twelve arguments; and supported by the authority of the Fathers.~\ | reasonable sub- | stance composed | non sup- ^ n [ c [ 0 | positata suppo- | non supp>ositata suppositacione* aliena.
p. 161: ^tio aitena P .° Sl ' | ot w i ta pen a
p. 163: suppositacione aliena,
p. 164: De Universalibus | 7 r r butthe^fo?™ | se humanitas
```

---

## Chunk 10-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "164.28–167.22"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 2 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "753 words; 748 confirmed by Fordham or the vote; 5 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n203–n206 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 2: [TITLE]

## ¶1 · 164.28–166.7

> [p. 164] Item quilibet alius homo a Christo¹⁵ est per se humanitas; Christus secundum istam viam non potest esse humanitas: ergo non est univoce homo cum alio. Maior patet ex hoc quod licet omnis homo per accidens sit homo, tamen eo ipso [p. 165] quod est¹ humanitas, cum iuxta hanc viam post assumpcionem manebit non homo sed humanitas: sed cum illa humanitas non inceperit² esse per assumpcionem, sequitur quod prius manserat iste homo. Hoc 2° confirmatur ex eo quod omne per accidens oportet³ reduci ad aliquid per se³: sed Petrus est per accidens homo: ergo est prius per se aliquid, quod potissime foret humanitas. 3° per istud⁴ quod ista humanitas adequate individuatur ex eisdem principiis ex quibus iste homo: ergo sunt idem: non ergo potest esse ordo causandi inter eos. Et consequencia principalis ex hoc videtur quod, dato antecedente, Christus et quicumque alius homo non forent eiusdem nature univoce. Nam quilibet alius homo foret natura humana in recto: Christus non potest esse natura humana sed nature humane: igitur sicut Deus non predicatur univoce de creatura, de qua solum dicitur in obliquo, et de persona divina, de qua dicitur in recto; sic nec humanitas dicitur univoce de Christo et aliis: et per consequens non sunt univoce eiusdem nature: ymo cum humanitas sit nomen competentissimum speciei per se predicatum de suis suppositis⁵ et non homo, humanitas autem non potest predicari in recto de Christo, videtur quod Christus non sit eiusdem speciei cum homine. Confirmatur ex hoc quod Christus non potest esse alicuius⁶ speciei: ergo Christus non est singulare⁷ speciei humane. Nam⁸ per adversarios non potest esse⁶ aliquid nisi deitas, sed⁹ ipsa¹⁰ non potest esse aliquid speciei humane⁸: ergo Christus non potest esse aliquid speciei humane. Si enim deitas foret illius speciei, tunc foret causabilis passibilis et activa, sicut alia individua speciei: quod est impossibile. Ideo, si non fallor, repugnat isti vie,¹¹ quod Christus sit eiusdem speciei cum aliis. Et in ista methaphisica vellem me studuisse, quando sollicitabam¹² me, si quantitas, motus, [p. 166] et cetera accidencia distinguantur. Subtilior enim est distinccio humanitatis a Verbo quam accidentis huiusmodi a subiecto; cum¹ secundum moderniores² Petrus inficians³ in ista hora per assumpcionem et dimissionem potest esse homo et post non homo⁴ sine⁵ generacione vel corrupcione alicuius rei vel motu aliquo pertinente; quod non contingit eciam de relacione.

[ENGLISH]

## ¶2 · 166.8–167.15

> [p. 166] Item iuxta nunc tacta, si illa humanitas non sit Christus, sed Christus tam extranee differt et essencialiter et personaliter⁶ ab illa; tunc Christus per incarnacionem non est aliquid⁷ nisi quod fuit eternaliter, cum sit solum deitas sicut ante: sed in deitate non univocatur cum aliqua creatura: ergo nichil vel non aliquid⁸ est Christus, in quo univocatur cum aliqua creatura.⁹ Sequitur enim—Christus est univoce homo cum aliis: ergo est univoce aliquid cum alio—sicut a simili,¹⁰ si Christus sit univoce albus cum Petro, tunc est univoce coloratus, et qualis cum eo, et ita de aliis generibus quibuscumque. Et sequitur—Christus est univoce aliquid cum aliqua creatura; ergo¹¹ aliquid est Christus in quo ipse univocatur cum aliqua creatura—quod non esset possibile,¹² si solum deitas foret Christus: oportet ergo speciem humanam, que est communis humanitas, esse Christum; et per consequens non solum naturam divinam, cum illa sit natura plurimum separata a natura humana: ymo cum¹³ nulla substancia secunda inest supposito nisi mediante substancia prima, patet quod non communis humanitas foret Christus, nisi singularis¹⁴ humanitas, que natura assumpta foret¹⁴ Christus: patet igitur,¹⁵ si Christus sit eiusdem speciei nobiscum, quod ista species in athomo¹⁶ vel individuo foret Christus; et sic aliquid, quod non eternaliter fuit [p. 167] Christus. Et sic intelligit Augustinus Enchiridion 29°,¹ ‘Utraque, inquit, substancia, divina scilicet atque humana, Filius est unicus Dei Patris omnipotentis, de quo procedit Spiritus² Sanctus; utraque³ unus, sed aliud propter Verbum, et aliud propter hominem.’ Unde prius 28°⁴ miratur quomodo ille homo fit⁵ una persona cum Deo. Et in libro De Predestinacione Sanctorum bene post medium: ‘Ille, inquit, homo ut a Verbo Patri coeterno in unitate persone assumptus Filius Dei unigenitus esset! Unde⁶ hoc meruit? Faciente, inquit, et suscipiente Deo Verbo,⁷ ipse homo, ex quo esse cepit, Filius Dei unigenitus⁸ esse cepit.’ Ideo ut exponit 13 De Trinitate 37°. ‘Gracia Dei in hoc commendatur quod Christus tanta unitate Deo sit coniunctus,⁹ ut una cum illo persona Filius Dei fieret, nullis eius precedentibus meritis.’

[ENGLISH]

## ¶3 · 167.16–167.22

> [p. 167] Sed hic datur duplex responsio. Prima quod non est equivocacio vel univocacio nisi in signis solummodo, et sic nulla res est quicquam univoce sive equivoce, sed signa dicuntur quedam equivoce et quedam univoce. 2ª responsio modernorum doctorum stat in glosa Augustini et aliorum sic loquencium, quod ipsi non intendunt¹⁰ naturam assumptam esse Verbum sed naturam¹¹ Verbi.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 164:
1 et add. A B C.
2 servi om. B.
3 esse A B C.
4 quo B.
5-5 incepit quando Christus incepit esse homo humanitate A B C; incepit esse homo humanitate O.
6 incepit C O.
7 non B.
8 prius om. O.
9 per ante A B C; per añ O.
10 supp° A B C.
11 non negacione om. O.
12 quia O.
13-13 homo et dubie sequitur quod O.
14 negacione A B C; netiẽ͡ O.
15 Christo om. O.

p. 165:
1 e' (*rasura*) ē A; eûȷ B; eûȷ est C.
2 incepit B; incipit O.
3–3 oportet alicui per se C; oportet inniti alicui per se O.
4 ex isto B; per idem O.
5 compositis O.
6–6 alicuius . . . esse *om.* O.
7 simpliciter C.
8–8 nam . . . humane *bis* A C.
9 sed *om.* O.
10 ipse C.
11 die O.
12 sollicitabor A B C.

p. 166:
1 tamen A B C.
2 modernos O.
3 inficiens A B; infi in ista C; ınfınicıes O.
4 homo *om.* A B C.
5 sive (*corr. ex* sine) A.
6 potencialiter O.
7 aliud B.
8 aliquando C.
9 ergo non aliquid . . . creatura *iterum* A B C.
10 inassimili B O.
11 et O.
12 et *add.* O.
13 st (sicut) *add.* O.
14_14 humanitatis (que est natura *in rasura*) humana foret A; humanitatis que est natura humana foret B C.
15 ergo A B C.
16 athopio B; in *cum lacuna* C; attomo O.

p. 167:
1 nono A B C.
2 Spiritus om. A B O; ~~spus~~ scus C.
3 utrumque O.
4 28 om. spatio relicto C.
5 sit A B C.
6 cum add. A B C.
7 deo ~~cum verbo~~ A.
8 unicus O.
9 conuictus (forsitan pro convinctus) O.
10 intendunt in margine A; om. B.
11 sed natura A B C; secundum naturam O.
12 pro om. A B C.
13 nisi Christus om. O.
14 sit om. O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 164: De Universalibus | 7 r r butthe^fo?™ | se humanitas
p. 166: (corr. ex
```

---

## Chunk 10-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "167.23–171.13"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 3 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "970 words; 966 confirmed by Fordham or the vote; 4 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n206–n210 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 3: [TITLE]

## ¶1 · 167.23–169.5

> [p. 167] Contra primum verbale sophisticum non delector pro¹² nunc arguere, quia intencio loquencium de rebus univocis est cognoscere, si res similes in racione vel quiditate communicant, vel si de creata essencia Christi est quod ipse sit homo, sicut est de essencia cuiuscunque alterius singularis hominis quod sit homo. Aliter enim secundum verbales logicos non predicaretur iste terminus homo in quid de Verbo et secundum rectam methaphisicam; nisi Christus¹³ secundum humanitatem, vel secundum quod homo sit aliquid sit¹⁴ sic quod humanitas [p. 168] sit causa, quare ipse est idem.¹ Aliter non foret univoce homo cum aliis humanitate specifica. Sicut enim² quantitate est subiectum quantum, qualitate quale, et ita de ceteris; sic substancia vel quiditate est quid vel aliquid formaliter: et ita, sicut adveniente qualitate fit subiectum eo³ ipso quale quod prius³ non fuerat; sic adveniente⁴ substancia vel quiditate fit subiectum eo ipso aliquid quod prius non fuerat. Cum ergo humanitas st per consequens quiditas advenit Christo formaliter, sequitur quod secundum illam fit aliquid quod prius non fuerat, et per consequens est dare,⁵ quod aliquid est⁵ Christus per incarnacionem, in quo convenit cum homine plus quam ante: et cum quid dicit naturam ut quis dicit personam, sequitur quod post incarnacionem alia substancialis essencia est Christus, que⁶ prius non fuerat: quia aliter indubie in nullo esset univoce vel conveniens creature plus quam ante. Sicut ergo pertinenter queritur et solvitur—⁷ Qualis est Petrus post alteracionem,⁷ qualis prius non fuerat ?—sic pertinenter queritur et solvitur—Quid est Christus⁸ post incarnacionem, quod ante non fuerat?—⁹ et illud est substancia,⁹ natura, et essencia creata Dominus Iesus Christus, que¹⁰ est Verbum esse hominem; quia aliter indubie homo non predicaretur in quid de Verbo: nec Christus, in quantum homo esset aliquid, quod nedum contradicit principiis philosophicis, sed eciam Decretali*¹¹ Cum Christus¹² libro 7° De Hereticis. Quomodo queso dicerent¹³ doctores tam veteres quam novi quod aliquid cepit esse Christus, nisi aliquid per incarnacionem fuerit factum Christus? Aliter non oportuit Decretalem libro 7° De Hereticis sic scripsisse: ‘Cum Christus perfectus Deus [p. 169] et perfectus homo, mandamus quatenus¹ sub anathemate interdicas—Ne quis de ceteris² audeat dicere, Christum non esse aliquid secundum quod homo—quia sicut Christus verus est Deus, ita verus est homo ex anima racionali et humana carne³ subsistens.’³

[ENGLISH]

## ¶2 · 169.6–170.15

> [p. 169] Ex qua Decretali patet primo quod Christus, quia homo, est aliquid quod ante non fuerat; 2° quod sit univoce homo cum aliis. Nam aliter non esset verus homo ex elementis⁴ univocis cum aliis principiis fratrum suorum. Aliter enim non esset vere homo, sicut nec Spiritus Sanctus est vere columba. Habito ergo quod sit univoce homo cum aliis, ut dicit Augustinus in quodam Sermone De Trinitate: patet quod est univoce animal, corpus, et substancia cum aliis; et per consequens substancia, que est Christus, est univoce substancia cum aliis substanciis creatis: et⁵ cum nulla natura divina sit univoce substancia cum aliis creatis substanciis⁵; sequitur quod creata substancia assumpta est univoce⁶ et Christus cum aliis⁶ substanciis. Confirmatur tripliciter. Omnis⁷ substancia unica univoce⁷ subiecta est accidentibus cum aliis creatis substanciis: sed illa non potest esse substancia, essencia, vel natura divina: ergo relinquitur quod alia substancia, ita quod sit gigas gemine substancie, ut canit ecclesia. Item Christus cum sit univoce homo, animal, corpus, et substancia cum aliis est species et genus hominis; et omne tale universale est creatum secundum se totum: ergo Christus est aliquod creatum. Item si Decretalis solum intelligit Christum esse aliquid secundum quod homo; quia omnis homo est aliquid, et, si Christus est homo, ipse est aliquid; tunc conceditur, quod Christus secundum quod quantus, qualis, vel quomodolibet aliter accidentatus foret aliquid; quod notum est repugnare logice, methaphisice, et sensui Decretalis. Sic enim dicerent quod omnis homo secundum quod peccator est aliquid placens: et Christus [p. 170] secundum quod homo natus ex virgine creavit mundum, cum ut sic inanitus sit equalis Deo¹ Patri; et per consequens secundum quod minor Patre est equalis Patri. Sed quis, rogo, hereticus negaret quin Christus, si est homo, est aliquid? Ideo certum est quod nec Decretalis nec hereticus intelligit sic reduplicativam; sed ut iste terminus secundum signat causam formalem specificam, que est causa subiectiva, unde Christus sit aliquid ut pugnarius substancie. Unde videtur michi indubie quod quicunque concedit de Christo communicacionem ydiomatum et denominacionem univocam accidencium cum creatura, habet concedere consequenter,² quod Christus sit duplex substancia et per consequens creatura. Nam increata non potest esse creato accidenti absoluto subiecta; quia tunc foret mole magna et specialis,³ ut alie create substancie.*⁴

[ENGLISH]

## ¶3 · 170.16–170.27

> [p. 170] Confirmatur ex hoc, quod post incarnacionem fideles sciverunt quid est Verbum,. quod per ante nec Deus sciverat esse Verbum: ergo aliquid tunc fuit⁵ Verbum quod prius non fuerat. Infideles ergo nescientes ipsum esse Deum sciverunt quid⁶ fuerat: ergo fuit aliquid preter deitatem. Cum ergo aliqua racio substancialis post incarnacionem Verbo conveniat, que non prius convenerat, que non potest poni, nisi hoc quod Verbum est homo; sequitur quod hec sit racio substancialis non aliena a Christo, ut nunc fingitur. Nec sollicitor⁷ aptare verba, ut pertineret volenti contendere cum doctoribus signorum⁸; quia ex dictis⁹ patet materialiter sentencia et racio Augustini.

[ENGLISH]

## ¶4 · 170.28–171.13

> [p. 170] Illud confirmari potest tripliciter. Primo ex hoc: Verbum assumendo hominem assumpsit aliquid; ergo cum omne assumere sit facere, sequitur, quod faciendo se esse¹⁰ hominem, fecit se esse aliquid; et per consequens per assumpcionem fuit aliquid quod prius non fuerat. 2° confirmatur. Posito quod¹¹ [p. 171] pro instanti incarnacionis Petrus fidelis cognoscat Verbum divinum nunc esse Deum et ignoret quod nunc sit homo; tunc patet quod sequitur—Verbum divinum nunc non est aliquid quin iste Petrus nunc¹ cognoscat ipsum esse aliquid: sed Verbum divinum nunc est homo: ergo Petrus cognoscit ipsum nunc esse hominem—. Hic enim non est fallacia accidentis, cum Christus, in quantum homo, sit aliquid: et consequens est falsum: ideo relinquitur quod maior: ex quo sequitur aliquid esse nunc Verbum, quod Petrus nunc ignorat esse Verbum, quod non potest poni deitas. 3° confirmatur ex hoc quod quantitas et cetera accidencia non sunt essencialiter distincta² a subiectis: ergo multo evidencius humanitas est homo.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 167:
1 nono A B C.
2 Spiritus om. A B O; ~~spus~~ scus C.
3 utrumque O.
4 28 om. spatio relicto C.
5 sit A B C.
6 cum add. A B C.
7 deo ~~cum verbo~~ A.
8 unicus O.
9 conuictus (forsitan pro convinctus) O.
10 intendunt in margine A; om. B.
11 sed natura A B C; secundum naturam O.
12 pro om. A B C.
13 nisi Christus om. O.
14 sit om. O.

p. 168:
1 aliud in rasura O.
2 ergo A B C.
3_3 quale eo ipso quale prius B.
4 sic deveniente A B; si adveniente O.
5_5 dare quod aliquid est A B; dare quod est C.
6 qui (al man. corr. que) A; qui B.
7_7 qualis . . . alteracionem om. O.
8 et add. O.
9 et idem substancia A B C.
10 qui A B C.
11 Totus hic locus post verbum decretali usque ad confirmatur, p. 170, l. 15, in codice O. omissus est.
12 Cum Christus om. O.
13 debeñt C.

p. 169:
1 qts A; 9t9 B; 9tmus C.
2 cetero B C.
3 carne assumpta vel subsistens C.
4 elementis om. spatio relicto C.
5_5 et . . . substanciis om. B.
6_6 an univoce homo cum aliis legendum?
7_7 ee substancia univoce C.

p. 170:
1 deo om. C.
2 communitur (al. man. corr. consequenter) A; communiter C.
3 speciabilis B.
4 v. p. 168, n. 11.
5 fuerat A B C.
6 quod B.
7 Nolicitor O.
8 terminorum O.
9 signis C.
10 esse om. O.
11 quod om. O.

p. 171:
1 nunc om. B; non O.
2 distincte O.
3 tercium A B C; sed de secunda responsione (p. 167, l. 20) nunc agitur.
4 secum om. A B C.
5 sed C.
6–6 sed plus pallientes O.
7 negacionem C.
8 sed O.
9 quia sit O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 168: Cum L christusvhich. Q um Christus 12 | in rasura | (al man. corr. | Totus hic locus post verbum | in codice 0. 07)1 f MS £St
p. 169: Christum non | esse aliquid secundum quod homo | (secundum qu»d x 1 | gigas gemine substancie; | secundum quod homo
p. 170: iTcimdum ^qwk
```
