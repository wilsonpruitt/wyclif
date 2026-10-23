# Translation brief: incarnacione 10-d–10-f

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-10-d.md chunks/incarnacione/wyc-incarnacione-10-e.md chunks/incarnacione/wyc-incarnacione-10-f.md` once and fix what it reports.
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

## Glossary (the 334 rows these chunks use; the full file is GLOSSARY.md)

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
| pars peregrinans; peregrinari | the pilgrim part; to be a pilgrim | Augustine's *peregrinatio* (Ench. 56). Pilot. |
| predestinatus, -i | the predestinate (sg. "a predestinate [person]") | Never "the elect", which is *electi* and gets "the elect". |
| prescitus, -i | **the foreknown** | ⭐ Wyclif's technical term for those God foreknows will be damned. It is **not** "the reprobate" (*reprobi* → "the reprobate"). Explain it in a note at its first occurrence in **each work**. The English word misleads on its own and Penn explains it only once (T. p. 361 n. 12). Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| beneficium ecclesiasticum | ecclesiastical benefice | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| quiditas | quiddity | Kept. Explain at first use per work ("what a thing is"). |
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
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
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| ampliacio | ampliation | Logical term (T. p. 364 n. 23). |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
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
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| approbati doctores | approved doctors | Kept apart from *probabiles doctores*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 13.3). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| unio | union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39). |
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
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| adnichilare / adnichilacio | annihilate / annihilation | Wyclif's *De adnichilacione*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
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
| sermo vocalis | the spoken word | Against *Sermo* "Speech", the divine title. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 113). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| denominacio respectiva | relational naming | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.17). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| quiditativus | quidditative | Beside *quiditas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.24). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| univocare / univocari | make univocal / be univocal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.3). |
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
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| nativitas | nativity | Christ's twofold birth. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| negacio (constituent of the person) | negation | The moderns' account: a person = nature + negation of dependence. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161–162). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| magisterium | rule; of teaching, the teaching office; *quale magisterium* "what a feat of mastery" (*Incarn.* 137.14) | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| raciuncula | little argument | The opponent's ten arguments. Ruled 2026-10-02 (*Eccl.* 17, 398.15). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| adequata ecclesia | the adequate church | C note at use. Ruled 2026-10-02 (*Eccl.* 17, 393). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| diffinicio | definition | Beside *descripcio* (also "definition", frozen row governs): where the two stand together a C note gives the Latin. Ruled 2026-10-02 (*Eccl.* 17, 403.25). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
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
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| incompossibilis | incompossible | Beside *compossibilis*. Ruled 2026-10-02 (*Eccl.* 22, 522.1). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| relaxare; relaxacio | to relax; relaxation | Ruled 2026-10-02 (*Eccl.* 23, 554.9). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| palliacio; palliare | cloaking; to cloak | Ruled 2026-10-02 (*Eccl.* 23, 566.27). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| Lincolniensis | Lincoln | Robert Grosseteste, bishop of Lincoln (S note at first occurrence), as in *De ecclesia*. Ruled 2026-10-07 (*Pot. pape* 59.8). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| extollencia | exaltation | Self-exaltation of the proud. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.5). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| pallium privilegii | cloak of privilege | Kept apart from *palliacio* "cloaking". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-a). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |

---

## Chunk 10-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "171.14–175.16"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 4 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1079 words; 1075 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n210–n214 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 4: [TITLE]

## ¶1 · 171.14–173.7

> [p. 171] Quoad 2ᵈᵃᵐ³ patet cuilibet volenti advertere, quod glosa est nimis extranea preter mentem sanctorum; ut quando Augustinus, Gregorius, Ieronimus, Anselmus, et alii dicunt, quod utraque substancia, scilicet divina et humana, est Christus, dicit glosa ipsos per hoc intendere, quod altera non est Christus, sed natura eius, nec conveniens secum⁴ in essencia nec persona. Pro certo inter omnes glosas, quas unquam audiveram est hec inculcior, glosare dicta sanctorum directe per sua opposita. Si,⁵ inquam, ista glosa sufficeret, quis formidaret auctoritatem sibi oppositam? Sed⁶ ut pallient⁶ glosam suam, dimittunt verbaliter negativam⁷ dicentes quod Augustinus intendit utramque naturam esse naturam Christi. Quando autem queritur utrum Augustinus intendit utramque naturam esse Christum, dicunt quod non, sed utramque esse naturam Christi. Et quando ulterius opponitur, si⁸ intenderit naturam humanam esse Christum, sicut intendit naturam divinam esse Christum, dicunt quod non: et sic⁹ finaliter incidunt in glosam yronicam supradictam. Sed quam sinistrum est dicere quod tam subtiles logici et [p. 172] philosophi tam pii et prudentes theologi in precipua materia fidei, capciosissimis hereticis circumsepti, dicerent tam crebro et patule quod utraque natura Christi est Deus, quia persona Christi, si finaliter intenderent quod altera est Deus, et¹ altera non est Deus.¹ Et nimis leve² verbum est dicere Augustinum intendere,³ quando dicit³ ‘aliud Deus aliud homo sed non alius, quia non alia persona,’⁴ quod est⁴ quod ipse per hoc intendit, quod non natura alterius persone sit Christi deitas sive humanitas: tum quia glosa illa seipsam interimit falsitate, cum natura divina sit natura alterius persone quam Filii, quia tam Patris quam Doni⁵; tum eciam quia verba essent nimis impertinencia suis sentenciis. Nam Augustinus persepe asserit, quod anima sit Christus et⁶ caro Christus, sicut deitas Christus et humanitas Christus,⁶ utrumque aliud a reliquo sed non alius⁷; ut patet super Ioh. Ome. 47. 78 et sepe alibi ut patet superius. Et ad hunc sensum ut verba sonant ac raciones concordant, exponunt eum Anselmus, Hugo de Sancto Victore, et alii. Unde De Incarnacione ca° 6° in fine sic scribit Anselmus; ‘suscepit Verbum hominem in unitatem persone, ut due nature, scilicet⁸ divina et humana, sint una persona.’ Et hoc dicit Augustinus in Dialogo ad Felicianum; ‘aliud, inquit, Dei Filius, aliud hominis filius, sed non alius:’ et primo De Trinitate 9° ca°; ‘forma Dei⁹ formam⁹ hominis accepit, utraque¹⁰ Deus utraque homo’; et sic de quotlibet similibus, ex quibus patet quod sensus datus Augustini primo De Trinitate¹¹ 16° sit nimis sophisticus,¹¹ quando dicit, ‘talis fuit illa suscepcio, que hominem faceret Deum et Deum hominem’; hoc est, ut inquiunt, ‘illa suscepcio fecit quod homo est Deus, et e contra.’ Quis dubitat eciam laicus¹² de conversione illorum? Non ergo oportuit Augustinum [p. 173] exponere quod idem sit—Deum esse hominem—et—hominem esse Deum. Intenditur¹ ergo, ut alibi sepe dicit, quod natura illa sit² Deus et Deus sit illa natura ypostatice assumendo.³ Et sic favorabilius et coloracius sunt moderni glosandi, qui dicunt quod humanitas non est Deus. Intendunt enim quod Deus nec per se nec formaliter nec secundum essenciam deitatis sit humanitas.

[ENGLISH]

## ¶2 · 173.8–173.20

> [p. 173] Et si queratur qualis predicacio sit⁴ ista—Deus est homo sive humanitas—, dicitur quod equivocando in nomine accidentis ut⁵ supra; hoc⁵ est, per accidens; sicut et hec— Petrus est bipedalis—secundum⁶ negantes quantitates distingui est predicacio secundum essenciam; non quod deitas sit natura humana, sed quod persona deitatis sit illa essencia. Est eciam in parte predicacio causalis et formalis, cum humanitas causata a Deo sit ‘forma servi,⁷ secundum quam Deus est servus obediens Trinitati. Et patet quod humanitas cum sit forma temporalis distinguitur a Verbo, licet sit ypostatice ipsum Verbum. Nec sequitur per locum a simili quod substancia sit sua quantitas; cum non possit esse personalis unio substancie ad accidens inherens formaliter.

[ENGLISH]

## ¶3 · 173.21–174.17

> [p. 173] Item si sint aliqua duo, quorum omnes partes sint idem inter se, et⁸ ipsa sunt idem⁹ inter se: sed Christus et eius humanitas sunt duo distincta quorum omnes partes sunt idem inter se: ergo⁹ et ipsa tota eisdem¹⁰ adequale composita. Minor¹¹ patet ex hoc quod quelibet pars corporis Christi sicut et totum ipsum corpus et anima est pars humanitatis Christi et e contra; cum Christus non habet partem¹² qualitativam aut quantitativam, nisi secundum humanitatem eo quod secundum deitatem sit indivisibilis omnino. Et maior patet eis qui ponunt omne totum compositum ex partibus esse insimul¹³ illas partes; hoc autem [p. 174] hic supponitur. Et patet cum ista multitudo parcium sit Christus et ista eadem multitudo sit ista humanitas, quod Christus et ista humanitas sunt idem alicui tercio; et per consequens inter se: et cum nulla ydemptitas sit pertinens nisi fuerit personalis, sequitur quod Christus et illa humanitas sunt eadem¹ persona.¹ Et istam sentenciam videtur sapere prima conclusio 5ᵗⁱ² Elementorum Euclidis: ‘si fuerint quotlibet quantitates aliquarum totidem eque multiplices, ut eque maiores aut eque minores, aut singule singulis equales, quemadmodum una³ illarum³ ad sui comparem; necesse est totum aggregatum ex his singulariter⁴ se habere.’ Quod eque evidenter videtur de ydemptitate tocius ad totum, presupposita ydemptitate numerali⁵ cuiuscunque partis ad partem sibi correlatam,⁶ sicut de⁷ paritate proporcionum, sicut patet† applicati.⁸ Nam si sint aliqua duo, et quelibet pars unius ydemptificata fuerit parti alterius et e contra; tunc unum⁹ ydemptificatur¹⁰ primo alteri.

[ENGLISH]

## ¶4 · 174.18–174.29

> [p. 174] Pono ergo quod Verbum incipiat a pedibus Petri usque ad caput assumendo ypostatice quamlibet partem quantitivam aut qualitativam Petri, sic quod primo in fine hore tam corpus quam anima sit ypostatice assumpta: et patet, posito quod Verbum non aliunde habuerit partem aliquam, nec assumptum dimiserit ante finem, quod quelibet pars Petri fiet idem parti Verbi; et quelibet pars Verbi fiet¹¹ pars Petri,¹¹ posito quod in hora alia dimittatur. Nec fingendum quod ydemptificabuntur totali ydemptificacione, nisi Christus et Petrus vel eius natura. Si ergo quamlibet¹² partem humanitatis Christi fecit esse partem sui, tunc se totum fecit totam illam naturam, ut loquitur Augustinus.

[ENGLISH]

## ¶5 · 174.30–175.16

> [p. 174] Et potest confirmari tripliciter.¹³ Primo per hoc quod Christus non est¹⁴ infinitum bonus homo, sed tantum [p. 175] finite bonus ut ·homo; licet sit infinitum bonus Deus, ut hic supponitur: sed omnis bonitas humana, quam habet, resultat precise¹ ex eisdem principiis ex quibus resultat bonitas humanitatis: ergo precise¹ eadem est Christi secundum quod homo, que est bonitas sue humanitatis, cum bonitas et entitas convertuntur: sequitur quod eadem sit entitas Christi, que et sue humanitatis. Sed et hoc² sonat vocabulum et omnia que movent concedere Christum esse creaturam. Non enim est dare, que creatura esset Christus, nisi foret illa humanitas: bonitates enim non possunt dici incommunicantes; et, si in aliquo communicant, communicant³ secundum⁴ totum; nec est inconveniens sed necessarium, quod Christus habeat quiditatem creatam, cum sit univoce homo cum aliis habens denominaciones accidentales creatas, quod sonat in amplius imperfectum: aliter enim non, in quantum homo, foret aliquid.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 173: *sit—Deum* (print = bt) [SUB]
  - 173: *hominem—et—hominem* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Augustine not only asserts that c x ' * (172.8); reference Petrus est (173.15).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
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

p. 172:
1_1 et . . . deus *om.* O.
2 leve *om.* O.
3_3 intenderet aliud B.
4 quod est *om.* A B C.
5 ~~dei~~ A; dōi B.
6_6 et . . . Christus *om.* B.
7 alius *om.* C.
8 scilicet *om.* O.
9 for^n (*idem verbum in utroque loco*) O.
10 utrumque B.
11_11 racio sit nimis sophistica A B C.
12 logicus A B; laycus C.

p. 173:
1 intendunt A B C.
2 fit O.
3 assumenda (corr. ex assumendo) A.
4 est O.
5–5 accidentis hic (ut supra om.) B.
6 septipedalis A B; bipedalitas O.
7 servi om. O.
8 et om. A B C.
9–9 idem sed sic est de Christo et eius humanitate ergo A B C.
10 ex eis A B C.
11 maior A B C.
12 partem om. O.
13 in simile A B C; ınſımƚ[?] O.

p. 174:
1-1 idem persona etc. O.
2 conclusio 7 A B C; 9° 5ti O.
3-3 una illarum om. O.
4 singulariter om. O.
5 naturali A B C.
6 coloratam O.
7 de om. O.
8 applicati A B C; applιti O. an applicatis aut applicacione legendum?
9 una A B.
10 ydemptificabitur O.
11-11 fiet pars verbi A B C; fiat pars petri O.
12 qualibet A.
13 tripliciter om. O.
14 est om. O.

p. 175:
1 p~e (i.e. pure) O.
2 sed ex hoc A B; secundo C.
3 communicat semel A B C.
4 se add. A B C.
5 isti A B C.
6–6 est ·a· motum ad ·b· moto A; est amotu a’d moto B; est a motu ad a b moto C; est ·a· motum aliquid est ·b· motum O.
7–7 aliquid predicatarum A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 172: God is man | ts God x - 1
p. 173: seif, formally, | «ccordmg to | ± the essence | ^GoS^^man | p a e Taccidlns V .° Ca
```

---

## Chunk 10-e: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-e
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "175.17–179.19"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 5 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1088 words; 1087 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n214–n218 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 5: [TITLE]

## ¶1 · 175.17–176.2

> [p. 175] 2ᵈᵒ confirmatur ex hoc quod eadem in numero est quantitas, qua ista⁵ duo quantificantur, eadem qualitas qua qualificantur; et sic de motu et ceteris accidentibus quibuscunque, que insunt Christo humanitus, ut patet posterius: quod non esset nisi foret ydemptitas in subiecto: ergo idem est iste homo et ista humanitas. Cum ergo accidens non sit nisi modus subiecti, patet quod ad numeracionem subiectorum oportet accidencia numerari; ut, si aliquid est⁶ A motum, aliud est B motum;⁶ alia est mocio A mobilis, et alia est mocio B mobilis; neutra⁷ autem predictarum⁷ substanciarum est pars alterius, cum preter humanitatem vel eius partes non restat signare aliam partem Christi. Ideo humanitas nec est pars quantitativa nec qualitativa Christi; et per consequens, si essent distincte substancie, omnia accidencia, que insunt eis formaliter, distinguerentur; cuius impossibilitatem suppono ex alibi declaratis. Non enim est [p. 176] possibile puncta¹ et quantitates, qualitates, et ceteras formas simillimas coextendi.

[ENGLISH]

## ¶2 · 176.3–176.26

> [p. 176] Et ex isto capitur 3° quod omnis differencia substancialis vel accidentalis, qua Verbum secundum humanitatem differt ab alio supposito vel natura, est differencia qua humanitas Christi differt ab eodem. Ex quo sequitur ulterius, quod nulla est differencia, qua Christus humanitus differt ab illa humanitate: et cum non sit possibile quod aliquid differat ab aliquo, nisi aliqua differencia differat ab eodem; patet quod non est differencia inter Christum et illam humanitatem assumptam. Patet ex hoc quod omnis substancialis differencia capitur vel a materia vel a forma: sed omnis talis pars Christi est pars sue humanitatis et e contra, sicut et omne aliud accidens absolutum: ergo non superest fundamentum, unde caperetur differencia Christi humanitus, nisi ab illa natura assumpta. Nec valet dicere quod solum secundum naturam divinam differt ab illa; quia² sic³ tantum differret³ ab illa² sicut Pater, et precise⁴ convenirent, non obstante unione ypostatica, appropriate⁵ ad Verbum: et tunc non plus conveniret⁶ Verbum cum aliqua creatura⁷ post incarnacionem quam ante; et per consequens non foret eiusdem speciei vel generis cum aliqua creatura,⁷ eo quod tantum differt ab ista humanitate cum qua maxime conveniret inter omnes creaturas, quantum differret si esset pure Deus et illa homo, cum differencia amplior non sit fundabilis.

[ENGLISH]

## ¶3 · 176.27–177.22

> [p. 176] Item humanitas Christi habet causas completas et denominaciones positivas,⁸ que non possunt nisi homini competere: ergo est homo. Et, cum non potest poni alius homo, quam Christus; quia sic Verbum gereret in se monstruose duos homines, quia personam quam assumeret ad suam personam sed non in unitatem persone, et ipsemet foret alius homo, et illi concurrerent faciendo redempcionis commercium: [p. 177] oportet ergo quod illa humanitas¹ sit idem homo, qui Christus. Assumptum videtur primo ex hoc quod illa humanitas¹ est substancia² corporea racionalis ad ymaginem Dei facta, et hoc³ sufficit ad esse hominis secundum Augustinum et Lincolniensem ut patet superius. Nec valet ficta⁴ negacio, quod sic nemo esset formaliter humanitate homo; nec in quantum homo esset aliquid vel alicuius generis pocius quam in quantum peccator, quod non consonat philosophie vel fidei; ymo nemo sciret an esset homo. Quod autem illa humanitas sit substancia racionalis, omnes concorditer confitentur, cum sit composita⁵ ex corpore Christi et eius anima. Ideo, si illa non esset substancia, nesciretur quid esset, aut que alia res esset substancia; et ultra videtur, cum omnis substancia sit substancia prima vel secunda, quod illa humanitas sit substancia prima, et per consequens individuum speciei vel generis. Et cum non solum sit in genere substancie vel corporis, sed⁶ inferius in genere animalis, eo quod est sensitiva et racionalis et per consequens substancia animata sensibilis; sequitur quod sit animal. Non enim est racio quod negacio caderet in diffinicione animalis pocius quam in diffinicione cuiuscunque substancie, cum omnis singularis substancia sit suppositum.

[ENGLISH]

## ¶4 · 177.23–179.19

> [p. 177] Confirmatur. Anima Christi, corpus, et unio eorum cum suis consequentibus sufficiunt principiare humanitatem esse hominem, et non impediuntur propter Verbi incarnacionem: ergo de facto constituunt illam in esse hominis. Maior patet ex quolibet alio homine principiato et individuato per corpus et animam unita cum suis consequentibus: ymo videtur quod absolute necessario sequitur⁷ positis istis principiis cum unione predicta, quod individuum constituatur in specie. Nam non est⁸ possibile quod forma⁹ elementi vel mixti inanimati informet¹⁰ proporcionatam materiam, nisi eo ipso constituatur elementum vel mixtum in sua [p. 178] specie: ergo cum totum genus animalis sit perfeccius et¹ eque plene ab intrinseco principiatum; sequitur quod est dare principia intrinseca et eorum unionem, cum quibus non stat quod individuum illius generis non resultet. Si enim non sit² possibile quod albedo informet subiectum, nisi eo ipso³ constituatur unum album; eque⁴ evidenter, si anima informat proporcionatum subiectum, oportet quod⁵ ex eis constituitur in signanda⁶ specie individuum animalis. Quod autem natura Christi non impeditur ne sit animal, probatur sic. Per assumpcionem est humanitas Christi summe exaltata et in perfeccione ultima creature possibili collocata: ergo non est ab aliqua perfeccione naturali, quam naturaliter appeteret, prepedita: cum ergo omnis perfeccio substancialis sit suppositum, vel presupponit suppositum ut subiectum, et omnis perfeccio accidentalis presupponit essencialem, et suppositum sic perfectum; videtur quod, si natura assumpta⁷ sit, ut sic, a racione suppositi exclusa, et⁸ a perfeccione maxima sit prepedita. Quomodo ergo non tristaretur languens circa perfeccionem possibilem a qua deficit per ypostaticam unionem? Maxima quidem perfeccio creature possibilis est beatitudo, sicut philosophi et theologi profitentur concorditer cum scriptura: modo illa beatitudo consistit in clara visione et fruicione divine essencie iuxta vocem Veritatis Ioh. 17;⁹ ‘hec est vita eterna ut cognoscant etc.’; ergo illa creatura cum¹⁰ non potest¹¹ esse¹¹ suppositum stante unione et per consequens non exercere¹² actus suppositales, non potest, ut sic, perfeccionem talem attingere. Sed et hoc¹³ concedunt concorditer dicentes quod ista natura, cum non sit suppositum, nec agit nec patitur. Unde et illud Psalmi 44ᵗⁱ ad litteram dictum de Christo, ‘beatus quem¹⁴ elegisti et assumpsisti,’ dicunt esse falsum de virtute sermonis: sed sic intelligitur—beatus, cuius est natura, quam [p. 179] elegisti et assumpsisti—ista autem natura non est beata, cum non sit suppositum, quia per idem meruit redempcionem generis humani, quod non sufficit creatura, nec est colenda vel latria adoranda: illud ergo, quod nunquam exercuit actus suppositales, non est beatum. Sed rogo attendat lector et iudicet,¹ que istarum viarum² sit auribus fidelium magis pia; vel dicere quod natura illa per assumpcionem est beatissima creaturarum; (sic quod³ non deficit sibi esse hominis vel persone racio⁴ per se agendi et paciendi ac recipiendi formaliter felicitatem et cuiuscunque generis perfeccionem; sic quod assumpcio extollat eam ad omne genus perfeccionis et non vinculat eam excludendo a perfeccione huiusmodi;) quam dicere eius oppositum? quia non dubium quin esse hominem summe merentem ex passione maxime acceptabili Trinitati, et postmodum esse beatum beatitudine maxima⁵ possibili creature, est perfeccionis denominacio. Illam autem tollit adversa posicio, et illam ponit expresse nostra posicio concorditer cum antiquis doctoribus et scriptura.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Ps. lxv. (178.30).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 175:
1 p~e (i.e. pure) O.
2 sed ex hoc A B; secundo C.
3 communicat semel A B C.
4 se add. A B C.
5 isti A B C.
6–6 est ·a· motum ad ·b· moto A; est amotu a’d moto B; est a motu ad a b moto C; est ·a· motum aliquid est ·b· motum O.
7–7 aliquid predicatarum A B C.

p. 176:
1 pun9 O.
2_2 quia . . . illa om. A.
3_3 sicut differet (om. tantum) B.
4 p~cie A B C; p~e O; cf. p. 175, n. 1.
5 apP1etate[?] O.
6 communicaret A.
7_7 post . . . creatura om A B C.
8 positas A B C.

p. 177:
1-1 sit . . . humanitas *om.* O.
2 substancia *om.* A B C.
3 sic A B C.
4 facta A B C.
5 compositum B; componitur (*om.* sit) O.
6 secundum O.
7 consequitur O.
8 non est *om.* O.
9 formale A B C.
10 informaret A B.

p. 178:
1 et om. A B C.
2 est A B C.
3 eo ipso om. B.
4 que O.
5 oportet quod om. C O.
6 in assignanda A B.
7 assumpta om. A B C.
8 quod A B C.
9 14 O.
10 cum om. A B C.
11 pre ê O.
12 exercendo A B C.
13 sed secundo C.
14 quam O.

p. 179:
1 indiget O.
2 viarum om. A B C.
3 quid O.
4 racio om. B.
5 maxime A B C.
6–6 illa crevit a quantitate infantili C; illa humanitas crevit infacili O.
7 sic A B C.
8 accidentibus A B C.
9 partibus om. A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 177: fat^^l 7 bldii | aftfrThe SuS»
```

---

## Chunk 10-f: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-f.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-f
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "179.20–182.31"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 6 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "883 words; 883 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n218–n221 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 6: [TITLE]

## ¶1 · 179.20–181.12

> [p. 179] Sed ne dicatur tales denominaciones humanitatis non posse probabiliter sustineri, cum non sit persona; arguitur primo sic ad illam probandam. Nam illa humanitas est mole magna et accidentaliter qualis cum aliis denominacionibus corporeis accidencium; ergo per idem habet denominaciones spirituales accidentales secundum animam. Probatur consequencia eo quod dato antecedente⁶ illa humanitas crevit a quantitate infantili⁶ usque ad quantitatem virilem, et hoc⁷ secundum omnes condiciones augmentacioni proprie competentes: ergo augmentabatur, et per idem ambulabat super terram et mare, predicavit, manducavit, et sic de ceteris actibus⁸ animalibus, que Christo conveniebant. Nam, cum componitur ex omnibus partibus,⁹ ex quibus et Christus; fuit ex se mobilis, sicut et Christus: et per consequens [p. 180] sufficeret exspirando aerem a suo pulmone secundum suam ymaginativam et¹ cetera² vocis organa formare voces simillime sicut Christus. Non enim haberet organa sensuum² et operum suppositalium superflua; sic quod, habendo oculos et aures et instrumenta vocalia, preclusa esset sibi via per positivam³ assumpcionem ne sufficiat plus sentire quam surdus et mutus; sic quod sufficiencia senciendi et personaliter operandi foret per negacionem,⁴ qua⁵ imperficitur relaxata. Patet ergo, cum⁶ humanitas Christi habet de propriis tam formas quam organa ad humanitus operandum, nec ligatur ex benedicta unione, qua⁷ tantum perficitur; quod sufficit, ut loquitur scriptura, humanitus operari. Et confirmatur ex hoc quod Christus non predicat,⁸ vel ambulat,⁸ nec ‘interpellat pro nobis’ ‘factus obediens,’ nisi secundum illam humanitatem. Sed quandocunque duobus nate⁹ sunt inesse denominaciones et non uni nisi¹⁰ per reliquum, sequitur quod illi reliquo denominacio inest primo iuxta illud principium Aristotelis primo Posteriorum; ‘propter quod unumquodque et illud magis.’ Ergo prius taliter¹¹ predicavit et ceteros actus humanos fecit illa humanitas quam Christus, cum solum secundum illam sic fecerat: sic enim iuxta sentenciam 5ᵗᵒ Physicorum: si homo sit sanus secundum thoracem vel moveatur secundum partem, tunc illa pars primo movetur et totum per accidens. Cum ergo denominaciones humane insunt Verbo secundum illam humanitatem, que est primum et completum subiectum eorum; videtur quod prius insunt sibi quam Verbo, cum non possunt inesse Verbo nisi per illam, et sibi possunt inesse cum hoc quod non insunt Verbo; ut signato motu progressivo Christi certum est quod iste non potuit fuisse sine illa humanitate, cum motus ex 5ᵗᵒ Physicorum individuatur¹² a spacio, a [p. 181] tempore, et subiecto. Si ergo Christus secundum aliam humanitatem moveretur pro eodem loco et tempore secundum quamlibet eius partem quantitativam, alius foret motus. Cum igitur illi humanitati dimisse potest inesse dictus motus sine hoc quod insit Verbo, ut dicitur, et Verbo non possit inesse nisi sibi infuerit¹; patet² quod naturaliter prius sibi inest.³ Si enim denominacio creata post naturaliter insit Verbo hoc foret² secundum deitatem vel secundum humanitatem vel mixtim; non secundum deitatem quia nulla forma accidentalis inest sibi nisi secundum naturam qua est mobilis; si secundum humanitatem sive parcialiter⁴ sive totaliter; tunc illi humanitati naturaliter prius inest.

[ENGLISH]

## ¶2 · 181.13–182.8

> [p. 181] Et indubie⁵ idem videtur iudicium de spirituali denominacione secundum animam. Nam si anime sanctorum sunt beate in celo, ymo et corpora; quanto magis completa Christi humanitas, cum habeat in se primo subiective omnem creatam beatitudinem qua Christus humanitus est beatus. Augustinus itaque, qui ponit quod anima prius nedum intelligit ymo sentit quam totum compositum, diceret quod anima Christi in celo haberet visionem et fruicionem beatificam ultra quamcunque aliam animam. Nec est fingendum quod assumpcio ligat spiritum Iesu ne beatifice delectetur. Et per idem habendo quatuor⁶ dotes corporis foret perfecte et complete beata eadem beatitudine, qua est Christus; et idem est iudicium de omnibus accidentibus creatis que humanitus⁷ insunt Christo. Quomodo, queso, aliter adorarem eam latria, si non tantum benefecit michi ut crux Christi? aut quomodo dimissa recoleret de operibus Christi sui, vel maneret inter passionem et mortem dimissa a Deo corpore fatigata⁸ si nichil antea⁹ fuit passa. Dimissa ergo in uno loco et Christo assumente eam in alio, foret plus quam Christi germanus, ut patet de convenienciis substancialium [p. 182] et accidentalium: et non est conveniencia amplior nisi fuerit personalis; in nullo itaque casu Verbum assumeret personam, que esset natura Verbi passa et quomodolibet temporaliter¹ formata; ut patet de comitancia absolutorum conmultiplicatorum cum taliter multiplicatis; et sic facta revelacione illi homini quod adnichilabitur, patet quod dolor redundaret in Christum, nulli autem alteri homini posset sic affici.

[ENGLISH]

## ¶3 · 182.9–182.31

> [p. 182] Quo dato, videtur multipliciter quod humanitas Christi sit homo, et sic persona Verbi. Nam nichil est risibile nisi homo; humanitas Christi est risibilis, cum sufficiat predicare: ergo est homo. Maior patet ex hoc quod risibilitas est propria passio hominis convertibilis cum specie. Et idem est iudicium de passione mortalitatis capta a causa materiali, de productivitate sui similis in specie, que competit sibi passionaliter a causa efficiente, et de beatificabilitate² secundum corpus et animam que competit sibi a³ causa finali.³ Cum ergo predicaciones huiusmodi solum possunt formaliter inesse suppositis, videtur, cum humanitati Christi insunt, quod ipsa sit suppositum Verbi. Secundo confirmatur idem ex hoc quod omnis forma⁴ accidentalis non est aliud⁵ nisi subiectum accidentaliter se habere; ut mocio est mobile⁶ moveri, locucio est ipsum loqui, et ita de ceteris, ut hic supponitur. Cum ergo eodem accidente informatur Christus et ista humanitas, sequitur quod idem est Christus et illa humanitas: vel⁷ si Christus non sit illa humanitas sed movetur secundum illam, alia est mocio Christi et alius motus eius: et ita numerarentur omnes forme complete accidentales in Christo secundum numerum subiectorum: quod⁸ est impossibile, cum nullum tale accidens foret pars alterius, sed quelibet pars unius pars alterius et e contra.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 179:
1 indiget O.
2 viarum om. A B C.
3 quid O.
4 racio om. B.
5 maxime A B C.
6–6 illa crevit a quantitate infantili C; illa humanitas crevit infacili O.
7 sic A B C.
8 accidentibus A B C.
9 partibus om. A B C.

p. 180:
1 et *om.* A B C.
2–2 cetera vocis organa formare simillime *etc.* A; cetera organa formare vocis simillime *etc.* B; cetera vocis organa sensuum (formare . . . organa *om.*) C.
3 propositum A B; perpositam C.
4 mediacionem A B C.
5 quia O.
6 quod A B C.
7 quam O.
8–8 predicavit vel meruit A B C.
9 innate B; sunt *om.* C.
10 unica per (*om.* nisi) A B C.
11 câliter (*i.e.* causaliter) O.
12 indîatur O.

p. 181:
1 infuerit om. O.
2–2 patet quod si naturaliter prius insit verbo hoc foret (cett. om.) A B C.
3 in esse O.
4 particulariter O.
5 et indubie om. O.
6 quatuor om. B.
7 humana O.
8 fangata O.
9 anna (an pro anima ?) O.

p. 182:
1 temporalis A B C.
2 et beatificante A B C.
3–3 a causa finali om. A B C.
4 forma om. C.
5 aliud om. C O.
6 mobile om. C.
7 ut O.
8 et O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 181: secundum ani~ mam
p. 182: XeL 'maxL*' | dentofly so
```
