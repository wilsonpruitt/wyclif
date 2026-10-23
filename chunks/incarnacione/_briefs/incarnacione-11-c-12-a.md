# Translation brief: incarnacione 11-c–12-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-11-c.md chunks/incarnacione/wyc-incarnacione-11-d.md chunks/incarnacione/wyc-incarnacione-12-a.md` once and fix what it reports.
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

## Glossary (the 403 rows these chunks use; the full file is GLOSSARY.md)

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
| ecclesia militans / triumphans / dormiens | the church militant / triumphant / sleeping | *Dormiens* = the souls in purgatory. Not "dormant". |
| pars peregrinans; peregrinari | the pilgrim part; to be a pilgrim | Augustine's *peregrinatio* (Ench. 56). Pilot. |
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
| adolescentula | young maiden | Song 1:2, 6:7 (DR "young maidens"). Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

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
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| procurator; procuratrix | proctor | Pollard's word. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
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
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
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
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
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
| verificari (de) | be true (of) | The logicians' sense; not "verified" (modern "checked"). Ruled 2026-10-22 (Wilson; *Incarn.* 7.6). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
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
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| adnichilare / adnichilacio | annihilate / annihilation | Wyclif's *De adnichilacione*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76). |
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
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
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
| exceptiva | exceptive [proposition] | Beside *exclusiva*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.31). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| quiditativus | quidditative | Beside *quiditas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.24). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| exemplaria / exemplata | exemplars / things exemplified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.6). |
| res secunde intencionis | things of second intention | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 132.25). |
| materia proxima / remota | proximate / remote matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 137.1). |
| personari | be made a person | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 134.10). |
| ydemptificare / ydemptificacio | identify / identification | Make the same (*idem*); the hypostatic union as identification, not conversion or generation. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.19, 147.22). |
| res communis / res communes | the common thing / common things | The realist universal the *moderni* do not conceive (first root of their error). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 144.27). |
| distinccio racionis | distinction of reason | Beside *differencia formalis*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 145.23). |
| conversio naturarum / confusio naturarum | conversion of the natures / confusion of the natures | Kept apart from *conversio* of a proposition. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 143.9). |
| moderni (bare) | the moderns | Beside *moderni doctores* "the modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 142.10). |
| principiare (active) | be the principle of | Beside the passive *principiari* "be constituted from principles". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 147.4). |
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| negacio (constituent of the person) | negation | The moderns' account: a person = nature + negation of dependence. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161–162). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| mocio / motus (paired) | motion (*mocio*) / movement (*motus*) | Only where Wyclif pairs them; otherwise "motion". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 180). |
| posicio anime | the laying-down of the soul | John 10:17–18; not the logical *posicio* "position", C note. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 183.3). |
| causancia / causacio | causing / causation | Kept apart (both at 187.30–34). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 185.16). |
| personare (active) / personacio | make a person / personation | Beside the passive *personari* "be made a person". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 188.16, 188.32). |
| peticio (principii) / petitur | begging [of the question] / is begged | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.23). |
| perfeccio simpliciter | perfection without qualification | After *simpliciter* "without qualification". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 186.1). |
| multiplicative | multiplicatively | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.20). |
| habitudo relativa | relative respect | The "respect" sense of the CONTEXTUAL *habitudo* row. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 193.19). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| vetula | old woman | Ruled 2026-10-02 (*Eccl.* 18, 431–433). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| remissio; remittere | remission; to remit | Headword row (cf. *condonacio* "pardon", *venia* "forgiveness"). Ruled 2026-10-02 (*Eccl.* 23). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| procuratoria potestas | proctorial power | From *procurator* "proctor". Ruled 2026-10-07 (*Pot. pape* 63.9). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| connexio | conditional (proposition) | Logic: the "if … then" proposition. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 189.1). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| demereri | to demerit | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| remisse (of assent) | with slackened [assent] | Opposed to full assent in the degrees of belief. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 328.18). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| procuratorium | proctor's mandate | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 336.11). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| gravandi | those to be charged | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 360.24). |
| indiffinite | without fixed bounds | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.3). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| obviare; obvia (logical) | meet; meeting | Of a case or argument. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 383). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 11-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-11-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-11-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "193.32–197.29"
divisions: "cap. 11 (heading 'Cap. XI.' at 185.0); part 3 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1045 words; 1045 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n232–n236 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 11, part 3: [TITLE]

## ¶1 · 193.32–194.6

> [p. 193] Quantum ad dimissionem nature assumpte patet ex dictis quod Verbum non potest illam dimittere licet contingentissime possit illa⁴ natura Verbo deesse cum sit contingens [p. 194] ad utrumlibet Verbum esse hominem vel fuisse. Movent autem ad negandum dimissionem nature assumpte, hoc est ad dereliccionem illius¹ personalitatis non nature¹ ipsius Verbi Dei, argumenta facta superius 5° ca°; et omnia que monent² quod humanitas sit idem personaliter Verbo Dei, ut tactum est 10° ca°.

[ENGLISH]

## ¶2 · 194.7–194.10

> [p. 194] Et ita de assumpcione multarum humanitatum vel simul vel successive; aut quod alia persona eandem naturam assumat. Et placet michi quod ex hoc pereunt modernorum doctorum vocata subtilia et gloriosa sophismata.

[ENGLISH]

## ¶3 · 194.11–194.20

> [p. 194] Primo, posito quod Verbum omnem naturam humanam a mundi exordio assumpsisset que continue viveret assumpta; tunc species humana non salvaretur per successionem suorum individuorum; quia vel tantum unum foret individuum in specie humana, quod foret totum genus hominum³ et faceret quidquid operatum esset⁴ ab homine vel si essent multa individua, tamen posito illo⁵ essent nature humane non homines;⁶ et sic omne suppositum nature⁷ humane⁷ foret prius naturaliter quam sua species, a qua tamen non caperet quiditatem.

[ENGLISH]

## ¶4 · 194.21–194.29

> [p. 194] 2do dicitur⁸ quod potest, quociens libuerit, fieri mutacio a contradictorio in contradictorium sine mutacione aut generacione aut corrupcione veritatis pertinentis. Ut posito quod in qualibet istarum parcium proporcionalium imparium huius hore⁹ omnis humanitas dimittatur et quelibet permaneat¹⁰ cum omnibus positivis¹¹ continue reassumpta; quod est impossibile, cum negacio non potest incipere; ymo unio, que est relacio tercii modi, non potest terminare mutacionem nisi in aliquo proprie¹² fiat motus.

[ENGLISH]

## ¶5 · 194.30–195.8

> [p. 194] 3° dicitur consequenter quod in fine illius hore fient quotlibet homines, et tamen non fiet aliquid¹³ nec alicuiusmodi positivum,¹³ posito quod quotlibet nature iam assumpte [p. 195] dimittantur immote primo in fine hore. Unde subducta omni mutacione preter talem alternam dimissionem et reassumpcionem foret tempus et motus mirabilis successivus. Nec negabunt quin Deus potest, subducto alio¹ motu quocunque,² alternare mutaciones huiusmodi, cum dependeant solum a volucione libera Dei; et indubie, cum una foret prius quam reliqua, nedum natura sed tempore foret continua³ successio temporalis.

[ENGLISH]

## ¶6 · 195.9–195.17

> [p. 195] 4to conceditur de possibili quod iam non est nisi unicus homo, et infiniti homines ante finem illius hore adnichilabuntur, nec citra generabitur aliquid⁴ positivum, et tamen in fine erunt infiniti homines, posito quod Deus ex omnipotencia sua creet infinitas humanitates in domo illa, quarum infinitum parva sit aliqua, et totidem⁵ creet Rome, et assumat omnes illas usque ad finem⁶ hore in qua⁶ adnichilet omnes Rome et dimittat omnes Oxonie aliter non mutatas.

[ENGLISH]

## ¶7 · 195.18–195.27

> [p. 195] 5to concedunt in casu quod⁷ in ista hora generabuntur vel fient infiniti homines et nichil illorum generabitur vel fiet ab aliquo, sed nec Deus sciet quando aliquis illorum hominum erit, ut divisa⁸ ista hora in suas partes proporcionales minores versus ultimum instans et quod in cuiuslibet illarum parcium prima medietate Deus dimittat unam, et in secunda reassumat reliquam dimittendo, servando in eis omnia positiva: tunc patet conclusio, cum nunquam erit ita⁹ quod isti homines sunt, et per consequens non erit aliquid de numero istorum hominum.

[ENGLISH]

## ¶8 · 195.28–196.11

> [p. 195] 6to concedunt quod in casu sex filii fuerint in b instanti geniti de Maria, in quo instanti non genuit nisi unum, et tamen non potest esse¹⁰ in b instanti nec alium filium nisi Iesum suum unigenitum genuisse, posito quod b fuit instans in quo genuit Iesum et quod post assumpcionem¹¹ multiplicata illa humanitate ad sex loca maneat assumpta a [p. 196] Trinitate in tribus locis et in aliis tribus maneat non assumpta: et tunc patet quod sex homines communicant in corpore Christi quod fuit genitum de Maria; ergo sex homines fuerunt ab ea geniti; et patet quod¹ residuum, illi quidem sex homines, forent genus Dei, quia tres persone divine et alie tres creature, hi² homines et illi³ non-homines, hi² filii et illi³ non-filii; et per consequens beata virgo nunquam genuit hos filios, et per idem nunquam fecit ut esset mater eorum; sicut nec corpus pro mensura, qua incepit esse multi homines, incepit secundum aliquid gigni vel esse filius, cum sola negacio non facit filium.

[ENGLISH]

## ¶9 · 196.12–196.30

> [p. 196] 7° concedunt quod stat infinita loca in b instanti repleri per⁴ istum hominem, qui nec est nec generatur nec generabitur: sed iste idem homo continue usque ad b instans distabit a quolibet illorum nec movebitur nec multiplicabitur ad aliquem⁵ eorum vel e contra, cum tamen ad situm tanquam⁶ ad per se terminum erit⁶ motus, posito quod Pater in divinis incipiat assumere naturam humanam glorificatam in celo; et cum hoc, posito quod in b ultimo instanti illius hore infinitas humanitates assumeret,⁷ que manebunt perpetuo⁸ fixe ad modum coree⁹ disposite: et patet conclusio. Nam Deus Pater non potest generari divinitus nec generaretur humanitus nisi ad generacionem nature pro tempore quo assumeretur, quod non competit seni vel beato. Sicut ergo Filius adquirit loca¹⁰ movendo humanitus, ita Pater adquirens et replens corporee¹¹ illa loca quodammodo moveretur. Sed quomodo moveretur aliquid adquirendo locum, qualitatem, et quantitatem in se subiective, si secundum nullam naturam nec secundum subiectum motus primo motum taliter moveretur?

[ENGLISH]

## ¶10 · 196.31–197.29

> [p. 196] 8° concedunt de possibili quod Petrus in infinitum [p. 197] remittetur¹ inmerito² et nunquam intendetur³ quousque fuerit infinitum Deo carior quam est modo; Paulus autem per idem tempus in infinitum intendetur³ inmerito et tamen⁴ in eodem fine temporis⁵ sine suo demerito erit Deo quantumlibet minus⁶ carus; ex quo videtur quod apud Deum sit excepcio personarum; posito quod Petrus per istam horam remittetur usque ad non gradum meriti exclusive et in fine assumatur a Verbo ypostatice; Paulus autem per idem tempus assumptus continue mereatur et in fine dimittatur: tunc patet conclusio, petito hoc notorio principio quod non est possibile Deum tantum diligere naturam hominis non assumptam sicut naturam propriam quam assumit: tunc posito quod infinitum bonus sit aliquis homo non assumptus, adhuc melior et Deo carior est quecunque humanitas quam assumit. Et revera⁷ talia videntur michi dissona: scilicet quod homo Petrus demereatur continue, quousque fuerit infinitum Deo carus; et Paulus continue mereatur, quousque decidat a summa amicicia Dei sui; cum sceleratissimus peccator contingentissime, ut asserunt, potest assumi⁸; et cum ignorare poterit assumpcionem propriam, non est evidencia dans fidem quin quelibet creatura ypostatice unibilis sit assumpta. Et tunc non video quomodo quis convinceretur ex ydololatria vel cognosceret quiditatem aliquam creature. Concedunt enim quod Deus potest esse lapis et speciei abiectissime creature, potest esse dampnatus, quod est perfeccius. Sed procul a fidelibus ista ludicra venenosa. Unde Augustinus 83 Vet.⁹ et Nov. Test.⁹ Questionum questione 5ª dicit quod nullum animal irracionale potest esse beatum, et multo evidencius nulla inanimata substancia.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 193:
1 efficaciter C.
2-2 temporis . . . prioritate om. O.
3 9gniti^m (? cognitivum) O.
4 verba[?] (sic) A; verba B.

p. 194:
1_1 illius . . . nature om. A B C; ipsius om. O.
2 mouent A B C.
3 humanum O.
4 est A B.
5 ille O.
6 non homines om. A B C.
7_7 humanum O.
8 dicitur om. O.
9 huius hore om. O.
10 p̱i maneat O.
11 pn͠ct℮ O.
12 proprio B.
13_13 aliquid nec alicuius positivi O; aliud nec alicuiusmodi positivum A B C.

p. 195:
1 illo A C.
2 quomodocunque A B C.
3 foret *iterum add.* B.
4 aliud A B C.
5 cottidie C.
6–6 finem in quo O.
7 quod *om.* A B C.
8 dimissa O.
9 ista O.
10 esse *om.* A B C.
11 ascensionem O.

p. 196:
1 quod *om.* A B C.
2 hic A B C; h¹ O.
3 ibi A C; i¹ O; illi B.
4 in A B C.
5 aliquid O.
6_6 tanquam per se . . . erit *cum lacuna viii litt.* A B; tanquam ad per se erit C.
7 assumet O.
8 perpetuum A B C.
9 coree *codd. omn. an pro* choreae ?
10 loca *om.* O.
11 corpore A B.

p. 197:
1 remittereturr (corr. in remittetur) A; remittitur O.

Let me be careful and give the final transcription.

1 remitteretur (corr. in remittetur) A; remittitur O.
2 merito O.
3 intenditus O.
4 tamen om. A B C.
5 temporis om. O.
6 nimis A B.
7 revera om. A B C.
8 sumi O.
9–9 vet. . . . test. om. A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 193: be/ore | given. ^ ratl ^
p. 194: im Z uttaot " m
p. 195: iterum add.
p. 196: codd. omn. an pro
```

---

## Chunk 11-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-11-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-11-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "197.30–201.17"
divisions: "cap. 11 (heading 'Cap. XI.' at 185.0); part 4 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "962 words; 960 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n236–n240 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 11, part 4: [TITLE]

## ¶1 · 197.30–199.2

> [p. 197] 9° videtur de possibili concedendum quod Deus faciendo tres homines eternos, qui non possunt a Deo fieri, tantum perfecit genus humanum, sicut potuit de sua potencia absoluta, licet non plures homines quam illos tres potuit produxisse. [p. 198] Assigno totam multitudinem hominum a Deo producibilium¹ quoad intellectum divinum, et pono² quod tota Trinitas quamlibet talem naturam assumat ypostatice; tunc patet quod natura divina fecit trinitatem, tres homines, quos oportet sic opinantes dicere eternos homines, cum non habeant limitandum peryodum temporalem. Et secunda pars gratis conceditur cum dicunt hominem Iesum non posse fieri. Et tercia pars³ patet ex hoc quod tam perfectum est genus sicut aliquod individuum speciei; et⁴ infinitum perfectus est omnis homo in casu posito; ergo infinitum perfectum genus hominum; ymo, si consideretur, omnis homo foret infinitum perfectus humanitus, quia infinitam perfectam multitudinem tam animarum⁵ quam corporum tanquam partes proprias contineret; ergo infinitum perfectus humanitus foret omnis homo, quia infinitum perfeccior quam data anima vel corpus finitum; patet itaque quod non meliores homines⁶ vel magis graciosos plus Deum amantes concorditer aut plus beatos in corpore et anima omnino impeccabiles et imperfectibiles perfecciores omnimode quam poterit esse aliqua creatura. Et ultima particula patet illis, qui ponunt naturam assumptam esse hominem. Nam si Deus non potest assumere materiam primam vel formam materialem in unitatem suppositi nisi ydemptificaverit⁷ se illi nature, eo quod non est aliquid cuius ipsa est natura; per idem non potest aliam naturam assumere nisi ydemptificaverit se eidem, cum indifferenter cuiuslibet nature create quiditas sit natura. Sed iuxta sentenciam sancti Thome ponent⁸ Verbum posse esse multos homines per idem: nam infiniti homines possunt esse isti tres homines, et per consequens non plures istis tribus hominibus possunt esse. 3° confirmatur ex hoc quod unus illorum trium hominum cum sit Pater in divinis, est omnino incausabilis⁹ et improducibilis:⁹ [p. 199] ergo non plures quam isti tres poterunt esse; quia, data affirmativa¹ opposita, deficit positum.²

[ENGLISH]

## ¶2 · 199.3–200.4

> [p. 199] 10° eliciuntur in casu sic opinanti possibili denominaciones inconpossibiles³ de eodem; posito quod tota Trinitas assumat ypostatice universitatem creabilem vel creatam. In quo casu videtur primo quod, posita eius possibilitate, non debet a catholico negari⁴ simpliciter: cum catholicus debet sustinere ut maximam quod, sicut Deus sit tam bonus intrinsecus sicut aliquid potest intelligi vel eciam cogitari, sic tante perficit universitatem creatam quante potest sustineri quod ipsam perficiat sine⁵ repugnancia racionis, experiencie, vel scripture.⁵ Sed sine repugnancia alicuius istorum sustineri poterit quod Deus universitatem creatam ad tantum perficiat; ergo quilibet catholicus debet illam sentenciam sustinere. Non enim⁶ repugnat racioni pocius quam ipso de possibili posito repugnaret; nec experiencie repugnat cum nullus sensus humanus sciat discutere utrum Deus sit⁷ lapis, asinus,⁷ et sic de ceteris creaturis; nec scriptura de dampnacione hominum vel peccatis aut aliis obviat ne sic fiat, quia post peccatum potest Deus dampnandum assumere; eo quod minus videtur Deo contrarium quod sit racionalis homo vel angelus, quam quod sit omnis bestia hic sit quantificatus, figuratus, senex, agens, motus, et sic de aliis denominacionibus tam substancialibus quam accidentalibus, ibi autem opposite formatus. Nec valet dicere quod posito hoc de facto scriptura sacra illud exprimeret, quia Paulus ‘audivit archana que non licet homini loqui’: ymo ut diceretur ex scriptura hoc sequitur,⁸ cum Deus summe potens et non invidus vel avarus ex bonitate sua non potest se ab ista beneficiencia continere.⁹ Nam iuxta argumentum Veritatis Matt. 7. ‘si vos, cum sitis mali, nostis¹⁰ bona data dare filiis vestris; quanto magis Pater celestis dabit spiritum bonum petentibus se?’ ista consequencia non valeret, si [p. 200] homo posset dimittere beneficienciam quam facillime posset perficere instar¹ Dei: tunc enim posset Deus ex libertate de obligacionis nulli hominum² sequencium² tribuere quamlibet promerenti.

[ENGLISH]

## ¶3 · 200.5–201.17

> [p. 200] Tales autem dilapsus vani ficti ex amplitudine divine potencie forent nidi³ hereticis ad hereses periculosissimas seminandum. Descendendo autem in speciali concedunt in tali casu quod Deus est quelibet eius pars quantitativa infinitum modica, et infinitum longa et lata; et ita, sicut est ‘primus et novissimus,’ sic est maximus et minimus possibilis, longissimus, latissimus, brevissimus, et indivisibilis quoad molem. Cum enim sit omnis ignis et omne corpus omogenium et⁴ ethrogenium, patet quod foret totus mundus multiplicatus dimensionaliter ubique, et sic nichil per se in genere foret in denominacione aliqua maius aut minus reliquo; cum quidlibet tale sit Deus, et per consequens nichil haberet plures partes quantitativas quam tres, que sunt Trinitas increata, super quibus cuncta sunt posita. Addunt eciam quod in casu posito acciones et passiones et cetere forme personales multiplicarentur concomitanter ubique consequenter ad immensam co-existenciam Trinitatis; et sic non est motus successivus; et per consequens neque tempus, cum prius ac posterius in situ deficiant; et sic de multis quibus ego noc sufficerem assentire. Quomodo queso quelibet pars quantitativa corporis foret essencialiter⁵ idem cuilibet? cum tunc pars foret non-pars; quia omne corpus indivisibile, et nulla pars minor aut maior⁶ reliqua; quia essencia divina et Trinitas benedicta, et sic mundus et quelibet pars eius quantitativa summe perfecta; quia realiter ipse Deus et sic tota Trinitas, si foret quelibet pars quantitativa corporis, differret quotlibet differenciis a seipsa. Deduccio omnium istorum patet ex possibilitate casus et principiis opinionis. Videtur enim multis quod [p. 201] sicut Verbum¹ potest esse dominus² sibimet et minister, ac tota generis humani cognacio, sic potest esse totus ignis et quelibet eius pars quantitativa: nec credo racionem diversitatis possibiliter assignandam. 2do dicunt quod, sicut Verbum est tantum unus homo,³ sic quod non multi, ponendo quod mille vel quotlibet humanitates assumpsit sic est tantum unus ignis licet infinitas igneitates assumpserit. Quod non dicunt illi qui ponunt Verbum in casu illo⁴ esse multos homines. Et patet plane ranga⁵ inconveniencium supradicta, cum omnis substancia per se in genere foret Pater, Filius, vel Spiritus sanctus: et sic utrobique illa tria⁶ supposita simul omnes substancie et omnia accidentibus informata sic quod, ubicunque est unus ignis, sunt tres ignes solummodo, qui sunt omnes. Infinitatem autem inconveniencium que secuntur videtur michi stultum deducere, cum gignit sollicitudinem apparencie sine fructu.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 198: *humanitus,* (plate: print = humanitus; the transcription normalised it (Opus coordinator)) [AGREE]
  - 198: *humanitus* (plate: print = humanitus; the transcription normalised it (Opus coordinator)) [AGREE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 1 0 Jeree*f um" (199.10); reference Cor. xii. 4. (199.27); reference Matt. vii. u. (199.31); reference Rev. i. 17. [B152a' (200.10).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 197:
1 remittereturr (corr. in remittetur) A; remittitur O.

Let me be careful and give the final transcription.

1 remitteretur (corr. in remittetur) A; remittitur O.
2 merito O.
3 intenditus O.
4 tamen om. A B C.
5 temporis om. O.
6 nimis A B.
7 revera om. A B C.
8 sumi O.
9–9 vet. . . . test. om. A B C.

p. 198:
1 productibilium A B C.
2 posito A B C; si recte, assignato pro assigno superius legendum.
3 particula O.
4 quod O.
5 naturarum A B C.
6 homines om. A B C
7 ydemptificaret O.
8 ponentis A B C.
9–9 incommunicabilis et improductibilis A B C.

p. 199:
1 mu (materia ?) add. O.
2 positivum O.
3 compossibiles O.
4 perfecta add. A B C.
5–5 sine . . . scripture om. A B C.
6 ergo A B C.
7–7 sit hominis assinus C.
8 sequeretur B.
9 contrahere O.
10 scitis A; nostis . . . se om. B.

p. 200:
1 iusticionem A B; iusta et C.
2-2 bonum sequentis O.
3 vie A B C.
4 vel A B C.
5 numeraliter O.
6 quam *add.* O.

p. 201:
1 non add. B.
2 deus A B C.
3 unus homo om. O.
4 illud O.
5 ranga (aren superscripto) A; arenga B; ranga om. cum lacuna C.
6 tria om. O.
7 variantur O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 201: \_Recitando opiniones varias de assumpcione creature declarat quod, si assumeret multas humanitates, foret multi homines, sicnt dictat sentencia sancti Thome. Against the several opinions that any divine Person can assume (a) any created nature; (b) every substance existing by itself and only such a substance; (c) every rational creature capable ofbliss and only such a creature : it is contended that only the Word could assume human nature, and that only in the man Christ Jesus: and it is argued according to the dictum of St. Thomas that, if the | Worcl assumed mami humanities, he ivould be manu men.\
```

---

## Chunk 12-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-12-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-12-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "201.0–205.24"
divisions: "cap. 12 (heading 'Cap. XII.' at 201.0); part 1 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1074 words; 1074 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n240–n244 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 12, part 1: [TITLE]

## ¶1 · 201.0–201.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 201] [Recitando opiniones varias de assumpcione creature declarat quod, si assumeret multas humanitates, foret multi homines, sicut dictat sentencia sancti Thome. Against the several opinions that any divine Person can assume (a) any created nature; (b) every substance existing by itself and only such a substance; (c) every rational creature capable of bliss and only such a creature: it is contended that only the Word could assume human nature, and that only in the man Christ Jesus: and it is argued according to the dictum of St. Thomas that, if the Word assumed many humanities, he would be many men.]

[ENGLISH]

## ¶2 · 201.18–202.27

> [p. 201] Sed descendendum est ad trimembrem posicionem modernorum qui inani sollicitudine venantur⁷ quid contingeret si Christus multas humanitates assumeret. Falsitas enim [p. 202] dissonat sibi ipsi, teste Gregorio 12 Moralium ca° 14. ‘Alius, inquit, relicta veritate mentiri deliberat ut audiencium animum fallat. Sed quantus labor est custodire sollicite, ne ipsa eius fallacia deprehendi queat! Ponit quippe ante oculos quid aliis veritatem scientibus responderi possit; et cum magno cogitatu pertractat quomodo per argumenta falsitatis documenta¹ veritatis exsuperet; hinc inde se circumtegit; et contra hoc, ubi deprehendi potuerit, veritati similem responsionem querit; qui si utrobique verum diceret, hucusque² sine labore potuisset. Plana quippe est veritatis via et grave est iter mendacii.’³ Et indubie, sicut in agilibus, sic in speculabilibus verificatur ista sentencia; et patet tam exemplariter quam eciam racione. Si, inquam, consideremus pictacias quibus negantes universalia, extensionem temporis, et veritates de anima cum sibi similibus pregravantur, in quot errores incidunt, quot subterfugia querunt, et quam onerose locuntur, ut sub falsitatis pallio simulent veritatem; patesceret in speculabilibus sentencia Gregorii supradicta. Sed et racio illud idem exigit. Veritas enim obiective movet⁴ et instruit ad ipsam vere cognoscendum in animo et proporcionaliter proferendum: sed⁵ ad exprimendum⁵ falsitatem deficit obiectum huiusmodi in natura. Ideo difficultatur falsidicus pallians non existens, ac si absque fundamento vel exemplari aliquis⁶ intendit unum non ens vel vacuum fabricare. Unde et illud potest patescere in varietate sentenciarum de incarnacione hodie ventilata.

[ENGLISH]

## ¶3 · 202.28–203.6

> [p. 202] Ponunt enim hi quod quamlibet naturam creatam quelibet persona divina indifferenter potest assumere: hi quod omnem et solam substanciam per se entem: et hi quod omnem et solam creaturam racionalem beatificabilem: et sic de quotlibet subdicionibus et evidenciis, quas nobis, qui ponimus solum Verbum pure Dominum Iesum Christum posse assumere, [p. 203] non expedit recitare; sed in difficultate, si Verbum multas humanitates assumeret, moderni doctores senciunt satis opposite. Sed pro ulteriori declaracione huius materie iuxta¹ ponam istorum sentencias, ut videatur quomodo exorbitantes a seipsis dissonant, et veritas rectissime in omnibus consonat sibi ipsi.

[ENGLISH]

## ¶4 · 203.7–203.23

> [p. 203] Ponit enim sanctus Thomas super 3ᵐ Sentenciarum Distinccione prima Questione 8ᵃ et 9ᵃ quod, si Verbum multas humanitates assumeret, foret² multi homines; sicut si tres persone eandem humanitatem assumerent, forent omnes et singule idem homo. Et inter omnes veritates, quas laudabiliter de Christo³ scripserat, non estimo aliquam veriorem. Illa enim veritas connexionis est absolute necessaria, quomodolibet fuerit de extremis. Patet sic. Si aliqua sit humanitas, ipsa est homo; ergo si insint multe humanitates, ille sunt multi homines; et per consequens, si Verbum assumit ypostatice⁴ multas humanitates, tunc assumendo facit se multos homines. Antecedens⁵ patet quodammodo ex predictis.⁵ Ymo ex dictis De Anima palam sequitur: quia cum quilibet spiritus hominis per se sit homo, patet quod, si sint multi spiritus tales assumpti, assumuntur et multi homines. Sed⁶ et hoc⁶ patet ex eo quod omnis humanitas est personam esse hominem.

[ENGLISH]

## ¶5 · 203.24–204.10

> [p. 203] Sed quia sanctus Thomas sicut et alii moderni doctores discordant a principiis iam assumptis, ideo oportet arguere contra possibilitatem suppositi aliis evidenciis. Videtur enim quod Christus posset esse quantumlibet monstruosus, quod esse non potest, cum minimum inconveniens sit Deo impossibile; et consequencia videtur ex hoc; quod, mille capitibus incommunicantibus existentibus in eodem corpore⁷ humano et⁷ proporcionaliter de aliis membris organicis, foret ille homo evidentissime monstrum magnum; sed hoc potest esse de Christo, cum omnem humanitatem potest [p. 204] simul assumere: ergo conclusio. Si enim Verbum totam unam cognacionem assumpserit tam maris quam femine, adhuc foret per adversarios solummodo unus homo, et per consequens tantum unum animal ac unum corpus; et super isto forent omnia dicta membra¹ monstruosa² ut estimo. Unde credo quod sanctus Thomas negans multiplicacionem dimensionalem eiusdem corporis, negaret in casu isto quod Christus est solummodo unus homo; nedum quod tunc foret hermofrodita,³ pater et filius, et tota cognacio; verum quia idem⁴ corpus foret dimensionaliter per loca distancia.

[ENGLISH]

## ¶6 · 204.11–204.14

> [p. 204] Sed hic dicitur quod monstruositas et impossibilitas multiplicacionis dimensionalis intelligitur secundum idem corpus; sed in casu posito foret secundum corpora multum disparia habitus talium situum et membrorum.

[ENGLISH]

## ¶7 · 204.15–205.14

> [p. 204] Contra illud tripliciter arguitur.⁵ Primo probatur quod secundum idem corpus habeat Christus istas denominaciones; quia secundum eandem naturam creatam et eandem humanitatem, que est Verbum esse unicum hominem; ergo secundum idem corpus. Si enim secundum seipsum habet ista, et ipse sit idem corpus, ubicunque est homo; sequitur quod secundum idem corpus habet ista, ubicunque sit homo.⁶ Similiter, si omnia ista corpora essent localiter copulata et adunata stante unione⁷ sine generacione vel corrupcione alicuius partis eorum, foret monstrum horribilissimum; quia corpus compositum ex corpore vetule et infantis, viri et uxoris, et sic de tota cognacione. Illud ergo cum fuerit totale et adequatum corpus Christi idem quod prefuit, sicut est modo, sic fuit ante monstruosum. Non enim adquiritur Christo aliqua pars vel partis posicio propter motum localem vel continuacionem⁸; ergo nec aliqua monstruositas secundum se totam. Et hoc est evidencius illis qui ponunt quod omnes partes integri⁹ sunt simul ipsum totum. Similiter non est evidencia contra multiplicacionem dimensionalem [p. 205] eiusdem corporis quin consimile contingit reducere contra hoc quod eadem persona sit dimensionaliter multiplicata secundum diversa corpora, ut quod hic sit senex, hic iuvenis, hic mas, hic femina, hic pater et uxor procreans¹ seipsum infantem, et hic adolescens sepeliens seipsum vetulam,² et ita de aliis denominacionibus aliorum generum. Unde, cum acciones et passiones personales individuantur primo a supposito non³ natura, videtur quod multiplicantur ad multiplicacionem suppositi; et sic idem homo foret quantumlibet dissimilis et contrarius sibi ipsi tam secundum accidencia corporis quam anime, ut sedulus excogitator potest calculare.⁴ Et sic contra principia sancti Thome idem corpus in numero foret quantumlibet multis et disparibus formis substancialibus accidentatum.⁵

[ENGLISH]

## ¶8 · 205.15–205.24

> [p. 205] Item, si Christus potest simul habere⁶ humanitates tam dispariter accidentatas cum hoc quod maneat idem homo, tunc posset pro diversis sitibus habere denominaciones contrarias; et per consequens, coextensis illis humanitatibus, forent accidencia contraria coextensa; et sic idem simul et semel contrariis accidentibus informatum. Sed hoc modicum videtur modernis, si secundum diversas naturas eidem supposito ista insint. Unde concedunt quod qualescunque forme contrarie per eundem situm et idem suppositum, sed secundum diversas naturas, coextendi poterunt.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 201:
1 non add. B.
2 deus A B C.
3 unus homo om. O.
4 illud O.
5 ranga (aren superscripto) A; arenga B; ranga om. cum lacuna C.
6 tria om. O.
7 variantur O.

p. 202:
1 argumenta A B C.
2 utique O.
3 menda^m O.
4 monet A B C.
5_5 sed . . . exprimendum om. O.
6 aliquid B; exemplari tas O.

p. 203:
1 antequam O.
2 forent A C.
3 de Christo om. A B C.
4 ypostatice om. B.
5–5 antecedens . . . predictis om. B C.
6–6 sicut et modo A B C.
7–7 corpore ut (om. humano) A B C.

p. 204:
1 membra om. B.
2 monstruose O.
3 hermifodrita (sc. hermaphrodita) O.
4 illud A B C.
5 arguitur om. O.
6 homo om. A C.
7 unione om. A B C.
8 fortasse contiguacionem legendum: cf. Trialogus, p. 87, l. 23.
9 integre A B.

p. 205:
1 procreatus O.
2 vetulam om. A B C.
3 nam O.
4 9m̃g'e (i.e. coniungere) O.
5 actuatum A C.
6 summe (fortasse pro sumere) B.
7 arguitur om. C O.
8 successivi B.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 201: \_Recitando opiniones varias de assumpcione creature declarat quod, si assumeret multas humanitates, foret multi homines, sicnt dictat sentencia sancti Thome. Against the several opinions that any divine Person can assume (a) any created nature; (b) every substance existing by itself and only such a substance; (c) every rational creature capable ofbliss and only such a creature : it is contended that only the Word could assume human nature, and that only in the man Christ Jesus: and it is argued according to the dictum of St. Thomas that, if the | Worcl assumed mami humanities, he ivould be manu men.\
p. 202: °can alsutne °the | and d (ilZ S 6the%
p. 203: De Anima
p. 205: substantial forms
```
