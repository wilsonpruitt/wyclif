# Translation brief: incarnacione 05-d–06-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-05-d.md chunks/incarnacione/wyc-incarnacione-05-e.md chunks/incarnacione/wyc-incarnacione-06-a.md` once and fix what it reports.
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
  (A C O against B, 65.11). An argument that fails without a manuscript's reading is cause as well (O, 61.22). Every departure gets a T note giving both readings. ⚠ Harris is a 19th-century editor of a
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
  Hilary, the Lombard (*Sent.* III) and Grosseteste; the *moderni* are usually unnamed. Harris's index (`sources/ia-ocr/latinworks03wycl.txt`, near l. 23680) lists his identifications of Wyclif's own works (*De Trinitate*, *De adnichilacione* …). ⚠ Thomas's "many men" (one person with several humanities; ch. 12) is the *Scriptum super Sent.* III d. 1 q. 2 a. 5, ⛔ not *ST* III q. 3 a. 7, which concludes "one man" (LEDGER Iprol-3). ⚠ Wyclif counts the Maximinus works as **three books** "contra Maximinianum": his book 1 = the *Collatio cum Maximino* (PL 42, 709–42), books 2–3 = *Contra Maximinum* I–II (his "book 3, c. 22" = II.22); his quotations from book 1 may be Maximinus speaking, not Augustine (LEDGER I01a-9, I02b-4, I02c-5).

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

## Glossary (the 376 rows these chunks use; the full file is GLOSSARY.md)

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
| apocrifa; apocrifus | apocrypha; apocryphal | Wyclif applies it to the saints' chronicles as well as to books outside the canon. Ruled 2026-09-28 (6 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
| iuvencula | young girl | The church militant as Christ's young bride; kept apart from the Song's *adolescentula* "young maiden" (DR). Ruled 2026-10-02 (*Eccl.* pp. 23, 37, 94.27). |
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
| autorizare | authorize | Ruled 2026-09-28 (6 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| laboratores | labourers | The third estate. Ruled 2026-09-28 (coordinator, delegated). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| graduacio; graduati | CONTEXTUAL: graduation / gradation; graduates | Academic "graduation" (Dialogus, 4 sites); of rank or lordship (*graduacio dominii*, *Pot. pape* 293.33, 297) "gradation". Ruled 2026-09-28; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| locus a maiori | the topic from the greater | The dialectical topic; for *a simili* see "the topic from likeness" (2026-09-28 row). Ruled 2026-10-02 (*Eccl.* 144.27). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| autenticus / autenticacio | authentic / authentication | The key term of *Eccl.* 13. Ruled 2026-10-02. |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| locus a simili | the topic from likeness | Wyclif's jibe *a simiali similitudine*: "from apish likeness". Ruled 2026-09-28 (coordinator, delegated) (6 sites). |
| fallacia | fallacy | Ruled 2026-09-28. |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
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
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
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
| philargiria | love of money | 1 Tim. 6:10 *radix omnium malorum cupiditas*. Ruled 2026-10-02. |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| indispensabilis | not to be dispensed | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sacramentum (of the incarnation, of creation) | sacrament | The Augustinian sense, "mystery" (1 Tim. 3:16): G note at the first occurrence in the chunk. Kept apart from *misterium*. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.8). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| paralogismus | paralogism | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
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
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| pars discretiva | discrete part | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.9). |
| dos immortalitatis | dower of immortality | Of the glorified body. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 46.24). |
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
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| dampnificare / dampnificacio | damage / damaging | Kept apart from *dampnum* "loss" and *dampnari* "be damned"; the argument of 65–68 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| adnichilare / adnichilacio | annihilate / annihilation | Wyclif's *De adnichilacione*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| insolubilitas | inextricability | As *insolubiliter*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| monita | admonitions | Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| infidelitas | heathenism, unbelief | "infidelity" (T. p. 362) |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| recencius | more freshly | Pilot (*Dial.* 2.10) |
| indispositus; (se) indisponere | unfit; to make (oneself) unfit | "indisposed" (now "unwell"). Ruled 2026-09-28 (8 sites). |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
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
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| indisposicio | unfitness | Noun of *indispositus*. Ruled 2026-10-02 (*Eccl.* 19). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| locus evidencie | topic of evidence | *locus* = dialectical topic (cf. *locus a maiori*); not "place". Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
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
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
| casus calculatorii | calculatory cases | Ruled 2026-10-02 (*Eccl.* 23, 574.32). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| episcopus suffraganeus | suffragan bishop | Ruled 2026-10-07. |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| Lincolniensis | Lincoln | Robert Grosseteste, bishop of Lincoln (S note at first occurrence), as in *De ecclesia*. Ruled 2026-10-07 (*Pot. pape* 59.8). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| fantasia | imagination | The faculty (scholastic *phantasia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 147.11). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| fantasticus | imaginary | Cf. *fantasia* "imagination". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 203.4). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| locus a simili | the topic from likeness | Dialectical topic. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 240.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| episcopus Nullatensis | a bishop "of Nowhere" | Ruled 2026-10-02 (*Eccl.* 23). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| gradus (of belief) | degree | The four degrees of belief (*Pot. pape* 327.18 ff.). Ruled 2026-10-12 (coordinator, delegated). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| episcopi cesarei | caesarean bishops | Extends *prelatus / sacerdos cesarius*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 331.24). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
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
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 05-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-05-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-05-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "76.32–80.12"
divisions: "cap. 5 (heading 'Cap. V.' at 65.0); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "840 words; 839 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n115–n119 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 5, part 4: [TITLE]

## ¶1 · 76.32–77.27

> [p. 76] Et utinam nos¹¹ scolastici, nescientes probare vel [p. 77] sophistice secundum vivacem¹ scintillam evidencie tales casus, insisteremus circa noticiam et deteccionem² substrate necessarie veritatis a nobis hodie plurimum occultate propter inanem occupacionem circa conclusiones impossibiles, que ex principiis impossibilibus consecuntur³: ut patet specialiter de casibus quibus ponitur Deum creaturam suam adnichilare, vel Verbum naturas prius assumptas dimittere ac alias personas in eisdem naturis assumendo communicare. Conceditur ergo quod, sicut libere contradictorie et per consequens contingentissime assumpsit hominem, sic potest absolute necessario nunc et semper facere vel⁴ causare quod neminem assumpsit, et quod non est vel⁵ fuit vel erit aliqua crcatura, ymo quod ipsummet non fuit vel⁶ erit amplius Verbum Dei. Patet hoc, posito quod non sit tempus. Sed absit ex isto concludere quod Deus potest quidquam adnichilare, vel facere tempus aut unionem predictam cessare. Talis enim non foret potencia contradiccionis ut ad affirmacionem et negacionem, sed potencia adnichilacionis,⁷ destruccionis, sive privacionis. Et patet solucio ad primam confirmacionem cum secunda. Deus enim necessitat se volicionibus⁸ eternis ad omne quod efficit, et tamen non potest efficere nisi summe libere contingenter, cum necessitas illa non sit coaccionis a causa superiori limitante; et per consequens nec pure naturalis inclinacionis, sed necessitas supposicionis, ut alias diffuse exposui. Et patet ad terciam quod Deus non est omnipotens, si posset vinculum dicte corrigie denodare.

[ENGLISH]

## ¶2 · 77.28–78.6

> [p. 77] Et quoad argumenta fundata in loco a simili, vellem quod sic arguentes attenderent et stabilirent sufficientem similitudinem argumentis,⁹ et non quererent questiones novas induendo habitum responsalis vel dicendo negativas, quod ipsi nesciunt racionem diversitatis et alia multa verba preter [p. 78] scolastica. Unde quando assumitur quod tanta est distancia inter terminos creacionis sicut inter terminos adnichilacionis, pure petitur quod antea probaretur. Oporteret¹ ergo primo fundare existenciam adnichilacionis vel eius possibilitatem, et post sollicitari de eius terminis. Sed hoc non probabitur antequam humanitas Christi sit soluta.²

[ENGLISH]

## ¶3 · 78.7–78.15

> [p. 78] Ex istis videtur corelarie³ sequi primo quod neutra natura creata in Christo posset esse humanitas, nisi a Verbo ypostatice sit⁴ assumpta. Patet ex hoc quod aliter natura, que est Christus, dampnificari⁵ poterit; et sic Christus: si enim humanitas Christi posset fuisse⁶ individuum speciei hominis et non Christus, tunc posset peccasse ut unus homo fuisse⁷ alius. Quorum opposita hic suppono, ponendo quod assumpcio ypostatica a Verbo Dei consequitur⁸ ad hominem Iesum, sicut passio consequitur⁹ ad subiectum.

[ENGLISH]

## ¶4 · 78.16–78.20

> [p. 78] 2°. sequitur quod nullam humanitatem aliam Verbum potuit ypostatice assumpsisse. Patet ex hoc, quod aliter Christus posset¹⁰ fuisse alius et¹¹ per consequens alia persona, ut post ostendetur.¹² Cum ergo¹³ consequens sit impossibile, patet quod antecedens inferius.¹⁴

[ENGLISH]

## ¶5 · 78.21–78.28

> [p. 78] 3°.¹⁵ sequitur quod nec Pater nec Donum incarnari potuit,¹⁶ quia aliter Filius posset¹⁷ esse humanitus pater patris. Cum ergo minimum inconsequens¹⁸ sit Deo impossibile absolute, ut capit Anselmus de Incarnacione Verbi cap 6°, patet intentum. Ista tamen dicta erunt magis evidencia postmodum, cum iuxta posite fuerint sentencie modernorum. Nam iste sunt conclusiones Anselmi Cur Deus Homo 6°. et de Incarnacione 7°. et 9°.

[ENGLISH]

## ¶6 · 78.29–79.17

> [p. 78] Ad omnes¹⁹ auctoritates vel dicta auctorum in oppositum alleganda dicitur, sicut in materia De Adnichilacione, quod intelligenda sunt condicionaliter, quod Deus ex se habet [p. 79] potenciam sufficientem: unde potest in talia si voluerit, vel si illa possint¹ fieri. Sic enim dicit Augustinus contra Maximinianum, quod Deus potuit alium filium produxisse. Et isto modo loquendi sepe utitur venerabilis Anselmus, ut patet 2°. Cur Deus Homo cap. 5. Et ex hoc processerunt omnes sollicitaciones inanes² quid illo posito sequeretur.² Verumptamen magna consideracio est et nobis inscrutabilis,³ unde Deus voluit illum hominem pre ceteris assumpsisse, quod rememorat Augustinus Enchiridion 3°. Profecto modus iste, quo natus est Christus de Spiritu Sancto non ut eius filius de Maria virgine, sic⁴ insinuat⁴ nobis graciam Dei, qua homo, nullis precedentibus meritis in ipso exordio nature sue, quo esse cepit, Verbo Dei copularetur in tantam persone unitatem ut idem ipse esset Filius Dei qui filius hominis; ac sic nature humane suscepcione fieret quodammodo ipsa gracia illi homini naturalis que nullum peccatum posset admittere.

[ENGLISH]

## ¶7 · 79.18–80.12

> [p. 79] Oportet ergo theologum capere tanquam principium quod Deus libere⁵ contradictorie⁶ assumpsit illum hominem sicut libere contradictorie⁶ produxit fabricam huius⁷ mundi, et huiusmodi effectuum⁷ causa est eterna⁸ Dei volicio,⁹ et per consequens essencia ac bonitas Dei nostri cuius non est querenda causa ulterior. Et sicut respondetur querenti,¹⁰ ‘Quare Deus produxit mundum in illo loco vel in illo tempore pocius quam quocunque alio?’— quod¹¹ hoc est necessarium ex supposicione, eo quod non posset illum mundum producere nisi ipsum produceret in illo loco et in illo tempore¹¹; ita respondetur querenti—‘ Quare Deus assumpsit illum hominem? ’—quod hoc est quia Deus voluit assumere hominem ad complecionem sue fabrice, et non potuit [p. 80] assumpsisse hominem, nisi illum hominem¹ assumpsisset. Sicut enim ille locus et illud tempus individuatur ab illo mundo, sic quod ubicunque vel quandocunque Deus² produxerit³ illum mundum, hoc fecisset in illo loco et in illo tempore. Sic illa humanitas, que est Iesus,⁴ sufficienter individuatur a Verbo, sic quod posita illa consequitur suppositacio sui a Verbo; et quamcumque aliam humanitatem per impossibile Verbum assumpsisset⁵ illa humanitas foret Iesus. Dimissis ergo casibus et conclusionibus ex illis inaniter coniecturatis,⁶ teneamus confessionem quod dicta ‘scriptura solvi non potest⁷’; quia, si non fallor, maior pars heresum circa incarnacionem Christi in isto devio titubavit.⁸

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Mark ii. 28. (76.9); reference so Augrustine "» passage quoted. (79.9).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 76:
1 protinus C.
2 25 A B C; 72 O.
3 eam B.
4–4 causa creature A B C.
5 perpetuum *om.* O.
6 "est" naturale hoc A B C.
7–7 notum . . . quod *om.* A B.
8 desicionem A B C M; designacionem O; *an* destruccionem *legendum?*
9 potencia ad A B C.
10 et O.
11 nō (*non*) O.

p. 77:
1 unitatem O.
2 decepcionem create in marg. A; vel detepcionem substracte B; et deteccionem substracte C.
3 con- om. A B C.
4 vel om. A B C.
5 vel om. O.
6 nichil O.
7 adilac͠onis (sic) O.
8 volucionibus A B C O.
9 argumenti A B C.

p. 78:
1 oportet A B C.
2 solita O.
3 correlarie A B C.
4 sint A.
5 dampnari A B C; dąpni^ra O.
6 esse A B C.
7 fuisse om. A B C.
8 censetur B C.
9 censetur C.
10 potuisset A B C.
11 non add. O.
12 ostenditur O.
13 ergo om. C.
14 inferens A B C.
15 sic add. O.
16 poterit O.
17 potest A C; potuisset B.
18 inconue^s (i.e. inconveniens) O M.
19 oppositum A B C.

p. 79:
1 talia add. A B C.
2–2 omnes sollicitaciones inanes qui illo posito sequetur A B C; homines solicitantes et amc° (? anxii) quid illo posito sequeretur O.
3 instrumentabilis O.
4–4 sicut filius insinuat O.
5 liberrime A B C.
6–6 assumpsit . . . contradictorie om. A B C.
7–7 huiusmodi et huius effectus A B C; huius mundi et huius effectuum O.
8 trina A B.
9 volucio O, cf. p. 77, n. 8.
10 querenti om. A B C.
11–11 quod . . . tempore om. B.

p. 80:
1 hominem om. O.
2 deus om. A B C.
3 produxisset A B.
4 Christus O.
5 assupserit (sic) O.
6 communicatis O.
7 possit A C; poterit O.
8 titubant A B C; tutubauit O.
9 fuisset O.
10 fotinus et siliaster A B C; fotinus et filaster O.
11–11 eius . . . ut om. A B C.
12 Meitangismonte A B C.
13 patrem et filium A B C.
14–14 Pelianiste et princiani A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 76: De Adnichilacione,
p. 78: De A(hiichilacione,
p. 80: nZl pt potest—the
```

---

## Chunk 05-e: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-05-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-05-e
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "80.13–84.29"
divisions: "cap. 5 (heading 'Cap. V.' at 65.0); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1161 words; 1149 confirmed by Fordham or the vote; 11 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n119–n123 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 5, part 5: [TITLE]

## ¶1 · 80.13–81.26

> [p. 80] Nam aliqui ponebant Christum esse purum hominem et non Deum: aliqui autem e contra dixerunt ipsum esse purum spiritum et non substanciam corpoream ex corpore et anima compositam. In prima parte erant Ebionite tempore beati Iohannis evangeliste dicentes Christum esse purum hominem et non Deum; et ista est heresis 10 quam recitat Augustinus in libro suo de Heresibus. Post eos consecuti sunt Theodosiani heretici, qui divinitatem Christi conformiter negaverunt; et hec est Heresis 33. Post eos consecuti sunt Pauliniani, qui negaverunt Christum semper fuisse,⁹ quia non antequam fuit natus de virgine, et, ut verbis utar Augustini, ‘Christum non aliquid amplius quam hominem putaverunt’; et illa est Heresis 44. Et post eos consecuti sunt Photinus¹⁰ et Philaster¹⁰ cum suis discipulis eadem heresi dampnati, ut recitat Augustinus Heresi 49. Postea consecuti sunt Arriani et Appollinariste negantes tam Christi divinitatem quam eius¹¹ humanitatem ut¹¹ recitat Augustinus Heresi 49 et 55. Meicagismonite¹² negant cum Arrianis eandem esse substanciam Patris et Filii,¹³ ut recitat Augustinus Heresi 58. Proclianiste¹⁴ et Patriciani¹⁴ negaverunt Christi humanitatem, [p. 81] ut patet Heresibus 60 et 61. Et postea consecuti sunt Priscillianiste¹ dicentes cum Manicheis² quod nulla caro est a Deo bono sed a Deo malo, et per consequens Christus non est Deus³ et homo. Hi autem secundum Augustinum Heresi 70 apocrifa sumpserunt tanquam autentica,⁴ scripturam sacram vertentes ut hodie ad suam heresim confirmandam.⁵ Sed et Sabelliani erraverunt⁶ in divinitate Christi concedentes confuse Patrem esse Filium et Spiritum Sanctum,⁷ seducti paralogismo vocato expositorio, ut ibi recitat Augustinus. Nona heresis,⁸ quam Augustinus recitat 73, posuit divinitatem doluisse⁹⁹ cum figeretur¹⁰ caro Christi in cruce: et isti, sicut Patripassiani, haberent hodie fautores plurimos. Nam ut asserunt negantes formas universales, ista foret racio insolubilis lumini¹¹ naturali—Filius Dei patitur, et ipse est deitas; ergo deitas patitur sive dolet—.Et eadem deduccio valeret Sabellianis—Si Verbum patitur, et ipsum est eadem essencia vel substancia in numero, que¹² Pater vel Donum; ergo uterque¹³ eorum¹³ patitur; et per idem quelibet persona divina indifferenter fuit homo, nascitur de virgine et suscepit omnem predicacionem temporalem, quam Verbum suscepit—.Et¹⁴ confirmacio illius est quod maior est unio Verbi ad naturam divinam ac personarum ad invicem¹⁵ quam est corporis ad animam; sed anima naturaliter compatitur corpori; ergo multo magis tam deitas quam utraque persona compatitur Christo passo.

[ENGLISH]

## ¶2 · 81.27–82.30

> [p. 81] Sed constat nutritis in materia De Universalibus quod substancia, essencia, vel natura divina, quod idem est,¹⁶ non potest pati ab aliquo vel moveri. Nec est color—si persona, que est communis humanitas, patitur, tunc et illa—cum natura communis abstracta non recipit formaliter predicaciones huiusmodi personales. Et multo evidencius non [p. 82] oportet Patrem pati, etsi Filius, qui est alia persona et eadem essencia paciatur. Nec esset possibile Verbum pati, Patre non passo; nisi Verbum esset tam aliquid quod non est¹ Pater, quam persona alia quam est Pater. Unde, cum, Verbum sit assumpta humanitas plus distans a Patre quam corpus ab anima, patet quod nec est color concludere—Si anima compatitur corpori, cum utraque sit eadem persona hominis; quod² per idem Pater compatitur Filio—cum inter eos sit distinccio personalis. Unde tales paralogismi heretici plus placent hodie tam iuvenibus quam adultis quam argumenta solida scripturarum. Unde ignorantibus naturam universalium videtur ista deduccio sophistica insolubile argumentum—Si Petrus ridet, Paulus comedit,³ et sic de aliis actibus personalibus; et omnis homo est natura specifica; ergo illa natura specifica sic ridet⁴ aut aliter personaliter operatur—.Et tales argucie, locum et tempus occupantes, ponunt placentes⁵ plurimis in numerum evidenciarum probabilium, sed indubie ut Tharsites.⁶ Alias autem declaravi in materia De Universalibus, quod communis humanitas non ridet vel comedit, quamvis sit quelibet persona hominis, que sic facit. Correspondenter communis deitas non gignit nec gignitur, nec gaudet humanitus nec tristatur; quamvis sit Pater qui gignit, Verbum quod gignitur et secundum assumptum hominem⁷ supra alios mortales patitur et tristatur. Tales intricaciones sophisticas decet theologis⁸ evitando cognoscere, cum sint superficiales colores venenosas hereses palliantes et incautos in logica in errores plurimos inducentes. Et hec est racio quare Augustinus tam sedule recitat hereses de Christo cum suis evidenciis ut caucius caveantur.⁹

[ENGLISH]

## ¶3 · 82.31–84.9

> [p. 82] Sed inter omnes hereses Nestoriana et Eutichiana sunt hodie eo diligencius precavende, quo theologi eciam ‘qui videntur aliquid’ sunt iam ad sapiendum predictas hereses [p. 83] proniores. Scribit enim Augustinus de Heresi 89 et 90 in fine libri sui De Heresibus, quod Nestorius episcopus contra fidem catholicam dogmatizare ausus est, Christum Dominum Deum nostrum hominem esse tantum; nec illud, quod ‘mediator Dei et hominum’ effectus est, in utero virginis de Spiritu Sancto fuisse conceptum; sed postea Deum homini¹ fuisse permixtum, nec Deum-hominem fuisse passum sepultumque² dicebat; evacuare³ contendens omne nostrum remedium, quo Verbum Dei hominem sic suscipere dignatus est in utero virginis, ut una persona fieret Dei et hominis; propter quod sic signanter natus, passus, mortuus, et pro nostris peccatis resurgens, ascendit in celum. Vidit enim iste⁴ Nestorius quod humanitas assumpta non fuit divinitas,⁵ et hinc paralogisatus credidit⁶ quod non fuit Verbum Dei, concedens cum heresi 73 quod Verbum non patitur nisi divinitas⁵ paciatur; et sic, cum illam⁷ esse personam sit suppositum,⁷ dixit quod in Christo fuerunt due persone; et per consequens Christus vel⁸ esset aggregatum ex his, vel persona Verbi non passionata humanitus, ut nec passa, mortua, nec sepulta; quia non vidit quomodo due tam distantes nature possent⁹ esse utraque eadem persona. Quidquid autem moderni dixerunt, illo modo intelligunt eum Augustinus, Boecius, Anselmus, et alii capitales doctores concorditer ante Petrum Lombardum.¹⁰ Aliter enim non tam crebro dicerent,¹¹ quod utraque natura tam corpus quam anima est eadem persona hominis; et quod in Christo tam divinitas⁵ quam humanitas est eadem persona Verbi¹²; et quod aliquid,¹³ quod nos sumus, recenter factum est¹⁴ Verbum; ut dicit Augustinus super Ps. 80. Ome. 48, 2° de Visitacione Infir morum et alibi. Euticiani autem¹⁵ volentes declinare a Nestorianis cum Appollinaristis coinciderant in caribdim, negantes naturam [p. 84] nostram cum proprietatibus et accidentibus ipsam consequentibus per veram humanitatis assumpcionem fuisse in Christo, et per consequens omnes acciones vel denominaciones humanas negant¹ esse in Christo¹ formaliter, nescientes exinde consequi quod² toti corpori Christi mistico auferri oporteat que capiti defuissent; ut, si Christus non patitur vel meretur, multo evidencius nullum³ membrum; cum in capite exemplari oporteat quidquid perfeccionis fuerit⁴ esse in posteriores derivatum.⁴

[ENGLISH]

## ¶4 · 84.10–84.15

> [p. 84] Unde Iudei tempore Christi laboraverunt in ista heresi negantes Christi divinitatem; ut patet Ioh. 10. ‘Non, inquiunt, de bono opere lapidamus⁵ te, sed de blasfemia; quia tu, homo cum sis, facis te ipsum Deum.’ Sed in ista heresi exorbitant Sarraceni⁶ dicentes Iesum prophetam eximium sed non Deum.

[ENGLISH]

## ¶5 · 84.16–84.29

> [p. 84] Iste sunt⁷ hereses, quas cum similibus oportet cavere de Christo, confitendo cum ecclesia⁸ duas plenas substancias esse Christum, deitatem⁹ scilicet et humanitatem; ita quod eadem persona sit perfectus Deus et perfectus homo ex anima racionali et carne in persona Verbi¹⁰ secundum ydemptitatem ypostaticam indissolubiliter coniunctis. Et hinc dicit sanctus evangelista 1 Ioh. 4.¹¹ ‘Omnis, inquit, spiritus,¹² qui confitetur Iesum Christum in carne venisse, ex Deo est; et omnis spiritus, qui solvit Iesum, ex Deo non est; et hic est antichristus de quo audistis quoniam¹³ venit, et nunc iam in mundo est.’ Oportet ergo volentem infringere¹⁴ latebras antichristi confiteri deitatem⁹ et hu- manitatem¹⁵ insolubiliter, personaliter, et formaliter inesse¹⁵ Domino nostro¹⁶ Iesu Christo.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 83: *humanitus,* (plate: print = humanitus; the transcription normalised it (Opus coordinator)) [AGREE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustinus, (83.30).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 80:
1 hominem om. O.
2 deus om. A B C.
3 produxisset A B.
4 Christus O.
5 assupserit (sic) O.
6 communicatis O.
7 possit A C; poterit O.
8 titubant A B C; tutubauit O.
9 fuisset O.
10 fotinus et siliaster A B C; fotinus et filaster O.
11–11 eius . . . ut om. A B C.
12 Meitangismonte A B C.
13 patrem et filium A B C.
14–14 Pelianiste et princiani A B C.

p. 81:
1 Priolianiste A B C; p^lalianiste (sic) O.
2 macheis O.
3 deus bis A B.
4 autenticam O.
5 confrigendam O.
6 errant O.
7 sanctum om. A B C.
8 heresi A B C.
9–9 dicentem doluisse A B C; divinitatem dissoluisse O.
10 fugeretur O.
11 lumine A B C.
12 vel add. A.
13–13 utraque illarum O.
14 suscipit O.
15 ad idem A B C. A inter ad et idem add. verbum in margine.
16 est om. A B C.

p. 82:
1 esset B C. pr. man. C. alt. man. est.
2 et O.
3 comedet O.
4 vel comedet add. O.
5 placenter O; forsitan ponuntur placentes verius legendum?
6 tarlites O.
7 omnis O.
8 theologum O.
9 teneantur C.

p. 83:
1 hominem A B C.
2 que *om.* O.
3 vacuare O.
4 iste *om.* A B C.
5 deitas A B C.
6 credit O.
7–7 illam humanitatem esse personam suppositum O; "personam" (*sic cum noto transpositionis signo*) A B C.
8 nec O.
9 posset O.
10 lûbardum O.
11 docerent O.
12 verbi *om.* O.
13 aliud A B C.
14 esse O.
15 aliud A B C.

p. 84:
1_1 inesse Christo A B C.
2 quot A B C.
3 ullum B.
4_4 fuerit esse in posteros derivatum A B C; fuerit in postores dirivatum O.
5 laudamus C.
6 sarrasseni O.
7 autem A B C.
8 eclīs O.
9 divinitatem O *ut saepe* infra.
10 verbi *om.* O.
11 40 O.
12 sc̃s O.
13 quam A B C.
14 añfugere. (*Qu.* aufugere ?) O.
15_15 humanitatem personaliter inesse *ceteris om.* A B C.
16 nostro *om.* O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 80: nZl pt potest—the
p. 81: Be Universalihus | in margine.
p. 82: treatise on^Uni- | De UhiversaUbus,
p. 83: (sic cum noto transpositionis signo)
```

---

## Chunk 06-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-06-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-06-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "85.0–89.10"
divisions: "cap. 6 (heading 'Cap. VI.' at 85.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1106 words; 1100 confirmed by Fordham or the vote; 5 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n124–n128 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 6, part 1: [TITLE]

## ¶1 · 85.0–85.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 85] [Ostendit quod Christus sit univoce homo cum aliis hominibus; et respondendo obiectibus declarat quod Christus est, secundum multorum doctorum testimonia, creatura. This chapter (A) shows that Christ is a man literally and in the same sense as other men are men; and by the discussion of objections to this statement (B) illustrates further the thesis of Chap. I., that Christ is a creature, in accordance with the testimony of many weighty authorities.]

[ENGLISH]

## ¶2 · 85.2–85.13

> [p. 85] Ex istis videtur consequi quod Christus sit univoce homo cum quolibet fratre suo. Probatur tripliciter. Primo sic. Christus est anima eiusdem racionis cum nostra, sicut et corpus eiusdem specifice racionis, que eciam univoce copulatur; ergo est univoce completa humanitas, et sic homo. Non enim est possibile aliquid complete principiari ex principiis omnino similibus cum adequatis principiis, ex quibus principiatur aliquid, nisi conveniat in natura. Cum ergo humanitas Christi et cuiuscunque alterius hominis sic se respiciunt, sequitur quod sunt idem in specie. Aliter enim Christus non esset pocius homo quam ydolum vel ymago; homo enim solum equivoce non est homo.

[ENGLISH]

## ¶3 · 85.14–86.15

> [p. 85] Confirmatur primo ex hoc, quod nec corpus nec anima, cum sit pars qualitativa suppositi, est¹ per se in specie, sed ipsum suppositum, ad cuius² speciem partes³ huiusmodi reducuntur. Cum ergo Christus secundum deitatem non sit in specie, nec humanitas eius est per se in specie, ut dicunt negantes ipsam esse suppositum; relinquitur quod Christus sit suppositum per se in specie. Sed in qua, rogo, si non fuerit⁴ in humana.⁴ Nec audebit catholicus dicere quod corpus et anima Christi erant solum fantastica non consimilis speciei cum partibus aliorum hominum. Quando autem [p. 86] communicatur cum hominibus ponentibus—‘omnia universalia esse signa,’—oportet aliter loqui: ut posito, quod¹ omnis natura¹ humana sit assumpta² a Verbo, et ipsum proferat voces et³ scripta talia—‘homo est animal racionale’—et⁴ correspondenter eliciat conceptus ut nos facimus; tunc sicut non exinde deficeret species humana ex parte rei, sic⁵ forent talia signa univoca vera ut prius, posito quod isti conceptus maneant post assumpciones significantes⁶ naturaliter et univoce sicut ante. Aliter enim, solo Christo existente de specie humana, vere sciret ad sensum⁷ univocum priorem nedum quod nemo est Deus, sed quod nemo est animal; cum species non esset, deficiente quocunque eius supposito.⁸ Quod videtur mihi insanum dicere, cum Christus maxime perficeret genus suum; et per consequens si omnis homo sit Deus, non exinde tollitur species hominis.

[ENGLISH]

## ¶4 · 86.16–86.29

> [p. 86] 2°. confirmatur ex hoc quod Christus est formaliter homo humanitate consimilis racionis cum humanitate alterius: ergo est univoce homo cum alio. Patet consequencia eo quod, quantumcunque⁹ subiecta variantur, dummodo¹⁰ forme, a quibus recipiunt predicaciones huiusmodi, sunt consimilis racionis, predicaciones sunt univoce; ut, quantumcunque subiecta¹¹ corpora¹¹ variantur, dummodo habent per totum albedines consimilis racionis, sunt alba univoce.¹² Quod autem humanitates¹³ Christi et aliorum essencialiter conveniunt exinde evidet, quod dimissa humanitate foret illa consimilis racionis cum alia; ergo cum unio sit sibi accidentalis, eo quod potest¹⁴ manere eadem essencia denudata;¹⁵ sequitur quod stante unione erit eiusdem racionis substancialis¹⁶ cum alia.

[ENGLISH]

## ¶5 · 86.30–87.13

> [p. 86] 3°. confirmatur ex hoc quod Christus est homo, et non Pater neque¹⁷ Donum; quod non esset, nisi Christus plus conveniret¹⁸ cum homine quam Pater; ergo est maior conveniencia [p. 87] Christi ad hominem quam Patris ad hominem, vel quam ante assumpcionem fuerat. Et cum non¹ sit pertinens conveniencia nisi vel in genere vel in specie, sequitur¹ quod Christus factus homo convenit in genere cum aliis hominibus, et per idem in specie;² quia aliter non foret humanitate nobis similior quam perante, cum conveniencia presupponit unionem.³ Noto ergo gradu⁴ similitudinis⁵ vel conveniencie, tunc, cum omnis conveniencia accidentalis presupponit convenienciam substancie generalem, oportet quod secundum humanitatem, qua factus est nobis similis, conveniat nobiscum in⁶ genere vel in⁶ specie, cum conveniencia in humanitate sit alterius racionis⁷ quam conveniencia in aliquo accidente⁷ novem⁸ generum.

[ENGLISH]

## ¶6 · 87.14–88.2

> [p. 87] Item omne suppositum speciei humane⁹ est homo univoce; Christus est suppositum speciei humane,⁹ cum sit filius hominis; ergo est homo univoce. Maior patet ex hoc, quod omne tale suppositum est illa species, et per consequens quiditas vel racio speciei. Et sic eadem est communis racio illi individuo et cuilibet¹⁰ eidem sibi¹⁰ in specie. Cum ergo illa descriptive dicuntur univoce predicata; quibus competit eadem racio predicati, patet quod non potest esse individuum speciei humane nisi sit homo univoce; aliter enim individuum esset homo, et non diffinicio vel quiditas hominis; et hoc esset ponere hominem non esse hominem. Minor¹¹ autem argumenti patet ex fide. Nam secundum Apostolum ed Hebre. 2. ‘nusquam angelos apprehendit, sed semen Abrahe ut fieret per omnia fratribus consimilis¹²;’ quia tam secundum naturam corpoream quam¹³ incorpoream,¹³ et illa sunt omnia. Et consequenter¹⁴ similatus est fratribus suis secundum omnia accidencia positiva¹⁵ naturaliter consequencia¹⁶ has naturas. Aliter enim non esset ‘mediator [p. 88] Dei et hominum homo Christus,’¹ ut dicit Apostolus prima ad² Thimo. 2.

[ENGLISH]

## ¶7 · 88.3–88.28

> [p. 88] Confirmatur primo ex testimonio Augustini. Nam in De Vera Religione 27; ‘Ipsa, inquit, natura suscipienda erat que liberanda.’ Et 2°. De Visitacione Infirmorum; ‘Homo Deus participatus est nostre³ humanitatis ut nos participemur sue divinitatis;’ et sequitur; ‘quod tu es, fieri dignatus est.’ Et ad idem vadit processus Anselmi in libro suo Cur Deus Homo; et De Incarnacione Verbi; ‘quod aliter non fuisset competens satisfaccio pro peccato primi hominis, nisi individuum eiusdem nature, et sic idem in specie, solveret debitum, quod natura debuit creatori⁴ suo.’ Nec memini me legisse in scripturis alicuius doctoris famosi oppositum. Unde Lincolniensis⁵ in suo Exameron dicit quod Christus est homo eiusdem racionis cum⁶ aliis. Et idem dicit sanctus Thomas et omnes ponentes universalia ex parte rei. Sed et multi non ponentes universalia preter signa; quia multi philosophi, sive fideles sive infideles, conversantes cum Christo et ipsum sencientes, ut apostoli,⁷ haberent conceptum specificum in anima, qui signaret illis⁸ univoce illum cum aliis; quia aliter fuisset Christus illusor maximus, qui ad hoc ostendit eius humanitatem humanis sensibus, et verbo docuit ipsum esse verum hominem. Philosophi ergo habentes terminos vel conceptus specificos, quos vere predicarent de pronominibus demonstrantibus⁹ recto Christum¹⁰ cum aliis, haberent¹⁰ conceptus univocos Christo et aliis: et hoc sufficit ad univocacionem ac ydemptitatem specificam iuxta sic loquentes. Ergo conclusio.

[ENGLISH]

## ¶8 · 88.29–89.10

> [p. 88] Confirmatur tripliciter. Primo ex hoc quod peccatum est illudere communicantes per verba vel signa sophistica; sed sic fecisset Christus potissime, si non habuisset aliquam denominacionem univocam cum aliqua creatura; ergo peccasset maxime. Pro assumpto dicitur Ecclesiastici 37. ‘Qui [p. 89] sophistice loquitur, odibilis est.’ Et Enchiridion 14. ‘Verbis uti ad fallaciam, non ad quod instituta sunt, peccatum est.’ Christus autem sepe¹ dixit se esse filium hominis et naturaliter ostendit se esse accidentatum² multipliciter; necnon et² passionem et mortem et resurreccionem predixit Apostolis ut patet Matth. 16, unde Petro dicenti sibi, ‘Absit hoc a te, Domine;’ respondit Veritas; ‘Vade post me, Sathana: non sapis ea, que Dei sunt.’ Et tamen eandem sentenciam Petri dicunt modo scolastici. Sequitur quod vel Christus fuit falsissimus³ vel illi sunt racionabiliter arguendi.³

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 88: *ad* (print = bt (Et ad idem)) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference of™angeis? Heb! (87.29); reference I. Tim. ii. 5. (88.1).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 85:
1 est om. O.
2 eius O.
3 per consequens A B C.
4-4 fuerat in humana A B C.

p. 86:
1 posito natura (*sic cum lacuna*) O.
2 servata B; asserta C.
3 vel A B C.
4 animal *om.* C; racionale *om.* O.
5 sit B; sicut C.
6 signantes A B C.
7 sensus O.
8 supposita O.
9 et *add.* O.
10 dm̃ nō O.
11-11 substrata corporum A B C.
12 unitate A C; veritate B.
13 humanitas A B C.
14 possunt O.
15 denudata *om. cum lacuna* O.
16 substancialis *om.* O.
17 vel A B C.
18 inveniret O.

CHECK: the main-text list gives figure 1 twice, but the foot has only one entry for 1 (a gap in the printed entry: "posito [gap] natura"); the figures 11 and 11 are covered by the single entry "11-11".

p. 87:
1–1 et cum non p̲t͛e conveniencia nisi vel in genere sequitur O.
2 speciei O.
3 univocacionem A B C.
4 gradus A B C; gradû O.
5 similis C.
6 in om. O.
7–7 quam . . . accidente om. B.
8 9ᵘᵉ (=commune) O.
9–9 est homo . . . humane om. B C.
10–10 eidem simili A; idem simili B; idem s. C.
11 maior O.
12 similis A B C.
13–13 quam incorpoream om. O.
14 correspondenter A B C.
15 posita A B C.
16 conveniencia A B C.

p. 88:
1 Iesus add. O.
2 prima ad om. A B C.
3 mater B.
4 deo. A B C.
5 ut lync°· O ; ut patet lincołn B.
6 racionis om. O.
7 philosophi C.
8 i⁹ (= illius) O.
9 in add. A B O.
10_10 Christum tum cum haberet C.

p. 89:
1 se O.
2–2 autenticum multipliciter necnon et A B C; accidentū instituī et O.
3–3 falsum vel arguendi *ceteris om.* O.
4–4 enunciante talia et consequencia A B C.
5 enim B.
6 consequencia *om. cum lacuna* C.
7 non *om.* O.
8–8 nec potest O.
9 esse *om.* B.
10–10 nisi . . . synecdochica *om.* A B C.
11 predicacō O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 85: \_Ostendit quod Christm sit univoce Jiomo cum aliis hominibus; et respondendo obiectibus declarat quocl Christus est, secundum multorum doctorum testimonia, creatura. T/iis chapter | shoivs that Christ is a man literally and in the same sense as other men are men; and by the discussion of objections to this statement | illustrates further the thesis of Chap. L, that Christ is a creature, in | accordance with the testimony ofmany weighty authorities.~\
p. 87: of™angeis?
p. 88: Yxx. and Vuig.
```
