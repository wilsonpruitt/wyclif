# Translation brief: incarnacione 10-g–11-b

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-10-g.md chunks/incarnacione/wyc-incarnacione-11-a.md chunks/incarnacione/wyc-incarnacione-11-b.md` once and fix what it reports.
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

## Glossary (the 372 rows these chunks use; the full file is GLOSSARY.md)

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
| viator | wayfarer | One still on the road, not yet in the homeland. Loserth: "a traveller on earth". Pilot. |
| via / patria | the way / the homeland | *Beatitudo patrie* → "the blessedness of the homeland". Pilot. The earthly sense (one's native country) is also "homeland"; a note where it matters (*Dial.* 54.2). |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| infidelis | unbeliever; with a dative, faithless (to) | Two senses by construction. Pairs with *infidelitas*, unbelief. Ruled 2026-09-28 (10 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| filii imitacionis | sons of imitation | Children of Abraham by imitating him, not by flesh. Ruled 2026-10-02 (89.27, 90.7). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |
| vicarius Christi | vicar of Christ | The card's ruling, now a row. Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). Third referent, the logician's arrangement of terms in a proposition (*Incarn.* 49.10): "ordering", with a **C** note; ruled 2026-10-22 (coordinator, delegated). |
| magnates | magnates | Ruled 2026-09-28. |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| vicarius deitatis / vicarius humanitatis Christi | vicar of the Godhead / vicar of Christ's humanity | King and priest respectively (*Dial.* 2.14–16; *Off. reg.* 13, 137). Pilot. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| credulitas | credence | With *credere*, believe (*Dial.* 23.17–24.4). Ruled 2026-09-28. |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
| differencia | difference (logical *differentia*) | Pilot (*Eccl.* 1.10). |
| subiectum / passio | subject / attribute | *Passio* in the *Posterior Analytics* sense (a proper attribute), never "passion". Pilot. |
| dicitur multipliciter | is said in many ways | Aristotle's *pollachōs legetai*. Pilot. |
| sumitur pro | is taken for | Supposition language. Pilot. |
| simpliciter / secundum quid | **without qualification / in a certain respect** | ⛔ Always opposable. Never "simply", "wholly", "directly", "naturally" etc. (T. p. 364). |
| necessitas supposicionis / ex supposicione | necessity of supposition / necessity on supposition | Conditional necessity. Pilot (*Eccl.* 3.21); *ex supposicione* ruled 2026-10-02 (34.12, 38.22). |
| de congruo / de condigno | by congruity / by condignity | Pilot. |
| consequencia | inference | ⛔ Not "consequence" (T. p. 361 n. 13). |
| consequens / antecedens | consequent / antecedent | |
| sequitur | it follows | Introduces a stated inference, often quoted in the next words. Pilot (*Eccl.* 2.21). Not tagged where it is not an inference ("the third law follows", *Dial.* ch. 5). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| claudit contradictionem / contradictorium | it implies a contradiction | Stronger than "is against reason". Keep the escalation visible. Pilot (*Eccl.* 5.4). |
| instancia; objectum | objection | ⛔ Not "instance" (T. p. 373). Also "urgency" (*ad instanciam*, at someone's urging, *Eccl.* 154.16), with a **C** note (2026-10-02). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| dulia / latria | dulia / latria | Kept as the theologians' terms, glossed once per chunk. Ruled 2026-10-02 (95.17). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
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
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
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
| suscipere / suscepcio (of the soul, the nature) | take up / taking-up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
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
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| inconsequens | inconsistency | Kept apart from *inconveniens* (an unfitting conclusion). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.23). |
| Donum | the Gift | The Holy Spirit. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 78.21). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| illusor | deceiver | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88). |
| mobilis / mobilitas | movable / movability | Of Christ's humanity (ch. 7). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.11). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| signum / signatum | sign / thing signified | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 91.2–6). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| illusivus | deceptive | Beside *illusor*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 92.9). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| faccio | making | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.6). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| accidens | accident | The category; *accidit* "befalls". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitacio | habitation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 120.14). |
| incepcio | beginning | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 121.16). |
| conversio (of a proposition) | conversion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.30). |
| humanitacio | humanation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 126.12). |
| deduccio | deduction | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 124.21). |
| racio (individual, personal) | account | *Racio individui / persone* "the account of an individual / a person", as *racio speciei*; not "aspect" (the row against *substancia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 8, 129–132). |
| vir (against *homo*) | man (*vir*) | Where Wyclif sets *vir* against *homo*, the Latin in parentheses. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 129.15–26). |
| univocare / univocari | make univocal / be univocal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 131.3). |
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
| assumere personale | personal assuming | The infinitive used as a noun; kept apart from *assumpcio personalis* "personal assumption". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 146.33). |
| moderniores (bare) | the more modern | Beside *moderniores doctores* "the more modern doctors". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 151.17). |
| supposicio simplex / supposicio personalis | simple supposition / personal supposition | Supposition theory. *Simpliciter / personaliter supponere* "stand with simple / personal supposition": NOT the *simpliciter / secundum quid* pair, C note where the two could be confused. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152.5–12). |
| concretum / abstractum | concrete [term] / abstract [term] | *Homo* the concrete, *humanitas* the abstract. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 152). |
| transsumpcio | transumption | Beside *transsumptive*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 153.28). |
| filiacio | sonship | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 154–155). |
| personalitas | personality | The scholastic term: what makes a person a person, not character. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 155). |
| aliud / alius | another thing / another one | The neuter against the masculine (*aliud et aliud, non alius et alius*): natures against persons. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 160.1–2). |
| in quid (predicari in quid) | in quid | Kept in Latin (predication of what a thing is, as against *in quale*), glossed at first use in a chunk. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 162.22). |
| suppositari | be supposited | Verb beside *suppositum*, *suppositacio*. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161). |
| dependencia actualis / potencialis / obediencialis | actual dependence / potential dependence / obediential dependence | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 161.23–162.4). |
| substancia prima / substancia secunda | first substance / second substance | Aristotle, *Cat.* 5. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.25). |
| a simili | by likeness | Bare, as an argument form; beside *locus a simili* "the topic from likeness". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 166.16). |
| reduplicativa | reduplicative [proposition] | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.6). |
| racio substancialis | substantial account | As *racio individui* "account". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.21). |
| doctores signorum | the doctors of signs | The logicians who reason from terms, not things. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 170.26). |
| ydemptitas numeralis | numerical identity | Beside *ydemptitas specifica* "identity of species". Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 172). |
| suppositalis | of a supposit | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| accidens absolutum | absolute accident | Quantity and quality, against relative accidents. Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 176). |
| beatificabilitas | beatifiability | Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| passionaliter | as an attribute | Beside *passio* (the proper attribute). Ruled 2026-10-23 (coordinator, delegated; *Incarn.* 181). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

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
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| intendere (a thesis) | maintain | Scholastic "hold, argue for": *intendimus quod* → "we maintain that" (epil-a 86.4, 90.19). "Intend" only for purpose. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| oculata fide | with our own eyes | Ruled 2026-10-02 (*Eccl.* 15, 352.27). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
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
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| memoriale | memorial | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| pars quanta / quota | a part of a quantity / a proportional part | As at 519.1. Ruled 2026-10-02 (*Eccl.* 23, 572.29). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| vicarius Petri | vicar of Peter | Kept apart from *vicarius Christi*. Ruled 2026-10-02 (*Eccl.* 23, 575.31). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| gentilitas | paganism | Kept apart from *infidelitas* "heathenism, unbelief". Ruled 2026-10-07 (*Pot. pape* 29.26). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| sessiva / sesina | seisin | *Sesina* the spelling at *Incarn.* 33. So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| memorativa potencia | memorative power | A faculty of the soul (the "power" sense of *potencia*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 219.27). |
| carismata; carisma | CONTEXTUAL: charisms / chrism | "Charisms" (gifts; *Pot. pape* 176.1). Singular *misticum carisma* in Augustine's sense of the anointing that names Christians (*chrisma*, *Pot. pape* 312.16) "chrism", with a T note. Ruled 2026-10-08; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
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
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |
| nimis | exceedingly | Medieval intensive (= *valde*); "too much" only where excess is the point. Ruled 2026-10-12 (close-out R2; *Pot. pape* 169.2). |

---

## Chunk 10-g: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-10-g.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-10-g
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "182.32–184.23"
divisions: "cap. 10 (heading 'Cap. X.' at 160.0); part 7 of 7, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "474 words; 472 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n221–n223 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 10, part 7: [TITLE]

## ¶1 · 182.32–184.14

> [p. 182] Tercio confirmatur ex hoc quod nichil sufficit redimere genus humanum perfecte, ut modo redimitur, nisi ipsum sit [p. 183] Deus: humanitas Christi sic redimit: ergo est Deus. Ipsa¹ enim fuit passa omni passione, qua Christus dedit sanguinem in redempcionem ut Christus, et sic de posicione anime ac commercio quo mercatus est Christus. Cum ergo per² passionem et tales formas fiebat redempcio, sequitur quod ipsa fecit redempcionem; aliter enim³ non esset illa humanitas tante⁴ diligenda nec latria adoranda. Cum tamen indubie quilibet⁵ Christianus debet tantum diligere humanitatem Christi quantum⁵ et Christum sub racione qua homo: ymo hec idem sunt et colenda eadem pietate in numero, ut ostendit Magister 3°⁶ Sentenciarum Dist. 8. ex⁷ testimonio beati Augustini. Christus enim ex hoc quod est ista humanitas et per consequens creatura adorari debet yperdulia, et omnis alia creatura venerari debet tantum⁸ dulia. Nam excellens honor debet⁸ Christo attribui, qui ex unione ypostatica est creator ac eciam creatura; et illa vocatur significanter yperdulia; et cum hoc, cum idem Christus sit creator, debet latria soli deo debita adorari. Correspondenter humanitas Christi cum sit Verbum, debet adorari latria,⁹ et cum in se sit creatura debet adorari⁹ yperdulia sicut Christus. Et sic tam Christus quam ista humanitas, que est personaliter ipse Christus, debet secundum duplicem racionem eadem tam latria quam yperdulia adorari: sed absit hoc, nisi illa humanitas foret¹⁰ Christus! Ex quo patet quod non solum deitati, sed soli deo est latria exhibenda. Nec est putandum quod humanitas Christi adoranda sit latria solum secundum ordinem ad alterum, sicut crux, ymago, vel pars Christi quantitativa, sed¹¹ tanquam corpus animatum, sumptum de virgine, passum pro nobis, dolens et merens, et per consequens vere positum precium pro redempcione humani generis: ‘empti enim estis¹² precio [p. 184] magno,’ ut dicit Apostolus prima ad Cor. 6° et 7°: et ad id precium atque commercium explanat expressius: ‘Deus, inquit, proprio Filio non pepercit, sed pro nobis omnibus tradidit illum’: et indubie sic fecit tota Trinitas: unde ad Gal. 2°, ‘in fide vivo Filii Dei, qui dilexit me et tradidit semetipsum pro me’: et indubie precium traditum fuit Christi humanitas; unde¹ si per impossibile humanitas Christi dimissa¹ fuerit personalitati proprie conversans nobiscum ut proximis, ego diligerem eum ut salvatorem et redemptorem meum, adoraremque eum latria sicut prius: nulli enim alteri hominum adeo potero obligari. Nec video quin iste homo dimissus, sine peccato vel merito decedens, foret supra angelos et omnes alios homines merito exaltandus propter meritum quo meruit ypostatice copulatus.

[ENGLISH]

## ¶2 · 184.15–184.23

> [p. 184] Tales sunt multe² evidencie² ex quibus credi debet—si illa humanitas sit aliquid, tunc est Christus—et sic intelligo illud ad Titum 3°; ‘cum³ autem benignitas et humanitas apparuit³ salvatoris nostri Dei’ etc. Illa quidem humanitas est mas de quo Baruch 3° ‘in terris visus est et cum hominibus conversatus est’; ipse enim est ‘vir quem femina circumdedit.’ Ierem. 31°. Et hinc dicit Augustinus in De Vera Religione quod ‘Verbum virum suscepit natus ex femina.’

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Gal. ii. 20. (184.5); reference Tit. iii. 4. (184.17); reference Jer. xxxi. 22, (184.21).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 182:
1 temporalis A B C.
2 et beatificante A B C.
3–3 a causa finali om. A B C.
4 forma om. C.
5 aliud om. C O.
6 mobile om. C.
7 ut O.
8 et O.

p. 183:
1 ipâ A B C; ipm̃ (i.e. ipsum) O.
2 per om. A B C.
3 enim om. A B C.
4 tantum tante (sic) A C.
5–5 Christus debet diligere humanitatem tantum quantum B.
6 3° om. O.
7 hoc add. A.
8 tantum . . . debet om. O.
9–9 latria . . . adorari om. O.
10 Christus sit B.
11 sit C O.
12 est O.

p. 184:
1_1 que si dimissa fuerit (per impossibile humanitas Christi om.) A B C.
2_2 multe evidencie om. A B C.
3_3 cum autem et humanitas apparuerit A C; cum autem et apparuerit B.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 182: XeL 'maxL*' | dentofly so
p. 183: dulia \pov\€la)
```

---

## Chunk 11-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-11-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-11-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "185.0–189.33"
divisions: "cap. 11 (heading 'Cap. XI.' at 185.0); part 1 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1256 words; 1251 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n224–n228 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 11, part 1: [TITLE]

## ¶1 · 185.0–185.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 185] [Solvit instancias quibus moderniores doctores videntur fulcire suam sentenciam, recitando decem ludicra que concedentes possibilitatem dimissionis annuunt consequenter. Discussion of Duns Scotus’ theory of the Incarnation including the analogy of Transubstantiation in the Eucharist (pp. 189-191); followed by a refutation of the hypothesis that Christ could have assumed many humanities.]

[ENGLISH]

## ¶2 · 185.2–185.22

> [p. 185] Superest¹ videre evidencias ex quibus fulcitur opinio huic sentencie² mee in verbis contraria.² Declarat autem Doctor Subtilis istam opinionem in principio 3ⁱⁱ Sentenciarum satis subtiliter. ‘Accidens, inquit, duplicem habitudinem habet ad subiectum: scilicet, informantis ad informatum; et talis racio includit imperfeccionem subiecti, quia potenciam ad actum quo subiectum perficitur: aliam autem habitudinem ut naturaliter posterius dependens a subiecto causaliter; et ista habitudo attestatur perfeccionem subiecti et imperfeccionem forme dependentis. Sic, inquit, simillime natura assumpta habet duplicem habitudinem ad Verbum, vel sub racione causandi sicut generaliter omnis creatura dependet a tota Trinitate; et illa habitudo presupponit in creatura posse naturale imperfeccionem sapiens, quod oportet habere actum causancie divine inseparabiliter comitantem. 2ᵃ autem habitudo est, qua natura assumpta secundum potenciam obediencialem potest esse natura Verbi, et illa potencia non potest actuari nisi per miraculum, et dicit quodammodo perfeccionem in persona assumente³; terminare itaque dependenciam creature secundum istam racionem est ypostatice assumere dictam creaturam.’

[ENGLISH]

## ¶3 · 185.23–186.17

> [p. 185] Et ista sentencia placet michi. Nam omne subiectum accidentis includit in se analogice racionem causantis ad [p. 186] suum causatum quod est in Deo equivoce perfeccionis simpliciter. Verumptamen omnis causancia, qua subiectum causat inherens accidens, sapit imperfeccionem subiecti, quia causanciam materialem vel subiectivam qua est in¹ potencia perfici¹ tali forma. Unde non est dare aliam singularem habitudinem, qua subiectum potest causare accidens sine hoc, quod ipso informetur. Sed quelibet singularis racio vel causa includit racionem analogam, que secundum illud² quod est perfeccionis simpliciter, soli Deo³ potest competere. Nec sequitur ex miraculosa transsubstanciacione in eucaristia quod vel qualitas vel inherens quantitas⁴ possit per se⁵ existere sine informacione et essenciali dependencia ad subiectum. Ad tantum ergo valet illa sentencia, quod vere ponit in qualibet racione creata lucere potenciam unde Deus potest humanitati Christi⁶ ypostatice copulari, sed quod aliam naturam possit assumere probari non poterit vel exemplariter edoceri.

[ENGLISH]

## ¶4 · 186.18–186.20

> [p. 186] Quod autem Verbum potest assumere naturam humanam faciendo ipsam esse naturam sui et non ipsum Verbum probat Doctor quintuplici racione.

[ENGLISH]

## ¶5 · 186.21–186.22

> [p. 186] Primo ex hoc, quod nullum ex hoc sequitur inconveniens⁷ ex parte assumentis nec⁸ assumpti.⁸

[ENGLISH]

## ¶6 · 186.23–187.16

> [p. 186] Sed in ista racione falsum petitur; cum personalis unio, qua humanitas fieret natura hominis, implicaret⁹ illam humanitatem fieri unum personaliter cum sumente. Natura enim completa substancialis cuicumque supposito est generaliter idem suppositum. Et si humanitas sit natura completa Verbi, tunc est essencia¹⁰ et substancia Verbi eo quod natura perfecta et essencia convertuntur, et si est essencia vel substancia Verbi, tunc est¹⁰ Verbum; cum cuiuslibet rei create vel increate idem est essencia vel substancia et [p. 187] res cuius est essencia. Ideo Verbum non potest facere humanitatem esse naturam Verbi, nisi fecerit ipsam esse essenciam ac substanciam Verbi, et per consequens ipsum Verbum. Nec sequitur—ista natura humana est natura Dei; ergo est natura divina—quia talia abstracta cum huiusmodi possessivis convocant¹ possessionem sui primitivi cum quadam racione reduplicandi; ut, si humanitas Christi sit essencia, natura, vel substancia divina, tunc est natura Dei sub racione qua Deus, quod solum est deitas; et si deitas sit natura humana, tunc est natura humana sub racione qua homo; et sic deitate foret Verbum formaliter homo, et humanitate Deus; quod est impossibile. Et patet quod multum refert² dicere—deitas est natura hominis— et—ipsa est natura humana; humanitas est natura Dei— et—ipsa est natura divina—; cum ille nature tam dispares conveniunt in eodem supposito.

[ENGLISH]

## ¶7 · 187.17–187.21

> [p. 187] 2° arguit Doctor per hoc quod persona divina potest terminare quamcumque dependenciam creature, quam dependenciam terminare foret³ perfeccionis; sed perfeccionis simpliciter est posse facere naturam creatam esse naturam Dei; ergo Deus hoc potest.

[ENGLISH]

## ¶8 · 187.22–188.13

> [p. 187] Sine dubio verum concluditur, sed infidelis diceret quod minor foret pura peticio. Unde quia videmus, quod Deus producit per se multos effectus ut substancias, sicut fide capimus de mundi principio; eliciunt quidam tanquam principium quod deitas vicem cuiuscunque cause secunde supplere poterit. Et ex illo pullulant plurime vanitates; quia certum est quod nullius cause materialis vel subiective vicem deitas supplere poterit, hoc est, causare formam eadem causacione sive simillima subducto subiecto; quia tunc deitas posset esse ignea et quomodolibet informata; quod dementis est dicere. Ideo causare materialiter vel subiective non potest sibi competere; ymo nullum accidens vel formam materialem potest Deus sine causancia⁴ [p. 188] substancie per se producere: ut, sicut non potest producere motum meum, nisi ego movear hoc causando, sic de qualibet forma materiali. Ymo de accidente spirituali idem dicitur; ut non potest actum volendi creature producere nisi ipsa creatura nedum concurrat cum eo subiective causando, sed et eciam coagendo. Ymo si ultra perspicitur, nullius secundi agentis potest deitas vicem supplere agendo univoce. Ideo vicis supplecio, cum dicit inferioritatis condicionem vicariam, non potest deitati competere. Quando ergo per se miraculose opus perficit,¹ quod posset facere agens secundum² alia² accione in genere cum suo regimine instrumentaliter efficere, non supplet vicem agentis; nec e contra cum conformantur in genere.

[ENGLISH]

## ¶9 · 188.14–188.16

> [p. 188] 3° arguit Doctor quod natura assumpta est prius essencia singularis quam suppositatur; ergo pro illo priori potest Deus personare illam naturam in alio.

[ENGLISH]

## ¶10 · 188.17–188.25

> [p. 188] Sed hic videtur michi quod consequencia sit neganda. Nam iuxta illud sequeretur quod quilibet potest esse quilibet. Nam Petrus prius origine est essencia quam substancia; ergo pro illo priori Deus posset facere eum nonsubstanciam; et, cum prius sit substancia quam corpus, et prius corpus quam animal, et prius animal quam homo, eo quod omne superius est causa sui inferioris; sequitur quod posset indifferenter fieri cuiuscunque speciei substancie tam secundum corpus quam animam.

[ENGLISH]

## ¶11 · 188.26–189.28

> [p. 188] Sed ulterius pro materia argumenti dicitur quod, quam primo quoad consequenciam humanitas Christi est ista singularis natura, tam primo est ipsa persona Verbi. Non enim posset derelinqui non assumpta, nec post assumpcionem dimitti; quia tunc indubie, sicut incepcio humanitatis presupponeretur prioritate consequente assumpcionem,³ ita personacio creata, cum esse individuum racionalis nature sit esse personam. Et patet quod Christus prius est persona, suppositum, vel ypostasis quam ipse est natura singularis; [p. 189] sed generaliter e¹ contra primo, sicut substancia est natura singularis date speciei, ut Christus,¹ eque primo est suppositum humane nature, sicut est persona hominis. Ideo Christus prius est persona quam est persona hominis vel substancia singularis. Verumptamen non est ordo inter divinum suppositum² et personam divinam tanquam inter generalius et contraccius, sicut est in personalitatibus creatis. Sed et in illis non oportet, si Petrus sit prius suppositum substancie quam persona humane nature, quod potest³ esse suppositum non persona, ut patet ex dictis superius. Singularitas ergo Christi est posterior sua personalitate, et causatur ex condicionibus individuantibus, ut puta ex illo corpore et illa anima cum illa unione ypostatica et aliis que secuntur. Ex quo videtur michi quod Christus non potest aliam naturam assumere, quia tunc posset esse alius homo; et per consequens ista persona, ut post deducetur; quod est impossibile. Et consequencia patet ex hoc quod, si alia fuerint principia individuancia, tunc foret aliud individuum speciei humane et per consequens alius homo. Nec est color quod tempus aut aliud accidens requisitum individuat substanciam,⁴ nisi ut multo evidencius unio ypostatica individuaverat dominum Iesum Christum, ut dicit Anselmus in De Incarnacione 7°. Nec obest quod Christus sit prius suppositum et individuum speciei humane, quam habeat predictam unionem; quia, sicut prius est homo quam iste homo, sic prius est individuum speciei humane, quam hoc individuum, et prius est ista⁵ unio quam ipse sit hoc⁵ individuum.

[ENGLISH]

## ¶12 · 189.29–189.33

> [p. 189] 4ᵗᵒ confirmatur ex hoc quod accidens potest Deus facere per se esse, ut patet de eucaristia; ergo per idem potest facere substanciam inherere: tantum enim distat de inherente facere non inherens, sicut de non-inherente facere quod adhereat persone nature superioris.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 187: *sequitur—ista* (print = bt) [SUB]
  - 187: *dicere—deitas* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference couid be Psome- (188.21).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 185:
1 insuper est A B.
2–2 huic sentencie contraria in verbis A B C.
3 assumentem O.

p. 186:
1_1 in (sic in rasura alt. manu A) imposita perficit B ; imposita perfici C.
2 idem B C.
3 deo om. O.
4 ·n· add. O. quod compendium alibi in hoc cod. enim significat, in hoc loco forsitan non valet.
5 per se om. O.
6 Christi om. O.
7 inconsequens A B C.
8_8 nec assumpti om. O.
9 implicat A B C.
10_10 essencia . . . tunc est om. B.

p. 187:
1 An pro convocant in codd. omn. repertum connotant potius legendum?
2 referret O.
3 esset O.
4 communicancia A B C.

p. 188:
1 perficit altera man. corr. perficiunt A.
2–2 solum illa B.
3 ad add. O.

p. 189:
1–1 e contra . . . Christus om. A B C.
2 individuum A B C.
3 possit O.
4 nisi om. C; ut om. O.
5–5 illi unio quam ille hoc O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 185: \_8ohit instancias quibus modemiores doctores videntur fulcire saam sentenciam, recitando decem ludicra que concedentes possibilitatem dimissionis annuunt consequenter. Discussion of Duns Scotus' theort/ of the Incamation J J J | invludinq the analoqy of Transiibstantiation in the Eucharist | followed by a refutation of the hypothesis j£b£ that Christ could have assumed many humanities.~\ | ^^Sg^rkc-
p. 186: aUegeT°j\re | natura perfecta | (sic in rasara alt. manu
p. 187: An pro
p. 188: time i_ • t no i n •
```

---

## Chunk 11-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-11-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-11-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "189.34–193.31"
divisions: "cap. 11 (heading 'Cap. XI.' at 185.0); part 2 of 4, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1063 words; 1061 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n228–n232 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 11, part 2: [TITLE]

## ¶1 · 189.34–191.16

> [p. 189] Hic dicitur quod loquendo de accidente inherente, ipsum [p. 190] non poterit per se esse, cum omne tale sit modus substancie, sed cum¹ omnis creatura sit accidens Deo adheretque² sibi tam essencialiter sicut accidens ad subiectum; patet quod accidens potest Deus facere per se esse, non sic quin alicui, scilicet Deo, adhereat, sed quod nulli formaliter inhereat; sicut est de toto predicamento substancie, quod non potest sic formaliter inherere. Si tamen racio predicta procederet, argueret direccius quod homo et quelibet alia substancia poterit inherere, sicut quantitas et qualitas creduntur hodie per se esse: quod ego non video. Ideo alias dixi quod, sicut³ univocando de accidente respectivo, cuiusmodi sunt⁴ relacio, accio, passio etc., nullum illorum poterit esse nisi insit substancie ut subiecto: sic nec qualitas nec quantitas, cum sint univoce accidencia sicut illa. De qualitate consentit sanctus Thomas, quod ipsa non potest esse nisi insit quantitati. Et de quantitate est michi evidencius, cum sit substanciam esse quantam, et non potest exspectare rarefaccionem et condensacionem et ceteras mutaciones, quas in benedicta eucaristia oculariter experimur. Ideo, ut alias dixi, esset nimis magna⁵ sensus illusio, nisi esset in eucaristia unum quantum diversimode qualificatum et accidentatum ac mobile. Et illud subicitur quantitati, qualitati et ceteris accidentibus que videmus. Sed quoad questionem—quid est de tali essencia ?—non sollicitor; licet sint quotlibet dicta sanctorum que sonant quod sit panis vel vinum; que forte intelligenda sunt, quod essencia subiecta illis accidentibus post transsubstanciacionem est panis⁶ ante transsubstanciacionem, et virtute transsubstanciacionis desinit esse quid vel substancia, et manet eadem essencia conformiter accidentata. Illa autem non fit corpus Christi sed fit signum signans nobis ineffabiliter quod ad omnem punctum sui sit sacramentaliter corpus Christi et concomitanter⁷ anima et omnia alia Christi accidencia absoluta. Nec est [p. 191] de substancia fidei viatorum¹ scire quid est illa essencia; sed satis est cognoscere questionem si est de ista cum transsubstanciacione et ceteris veritatibus que sacramento eucaristie sunt annexe. Non ergo sequitur—si Christus potest facere corpus suum virtute verborum sacramentalium esse ad omnem punctum illius essencie; ergo potest facere quod humanitas non² sit suppositum, vel quomodocunque aliter per terminos magistrales aliter³ extraneetur racio—⁴ in omnibus enim similibus evidenciis est pura peticio.⁴ Illud autem quod de eucaristia fides orthodoxa artat nos credere potest catholicus philosophice sustinere. Si enim secundum perspectivos corpus multiplicatur intencionaliter vere presens,⁵ ubicunque species eius agitur, et habet ibi efficaciam operandi; quod magisterium Deo facere corpus suum esse ad omnem punctum hostie sacramentaliter et effectus spirituales efficaciter operari!

[ENGLISH]

## ¶2 · 191.17–191.21

> [p. 191] 5ᵗᵒ confirmatur ex hoc quod accidencia maxime distancia potest Deus facere unitive concurrere in eodem, ut omnia novem genera⁶ accidencium sunt idem subiecto. Ergo per idem naturam humanam potest Deus facere inesse subiecto divino cum hoc, quod non realiter sit subiectum.

[ENGLISH]

## ¶3 · 191.22–192.8

> [p. 191] Sed hic dicitur quod loquendo de unione ypostatica oppositum sequitur ex assumpto. Unde omnes iste evidencie confirmare possunt fidelem credere quod duas naturas potest Deus unire personaliter in eadem ypostasi ad sensum expositum. Sed quod Verbum assumens non sit natura assumpta, nec iste raciones nec alie possibiles⁷ poterunt⁷ edocere. Unde quam mirum est quod natura divina et humana tam distantes sint utraque eadem persona, tam mirum est et idem in numero, quod Deus sit homo. Unde accidencium ad subiecta non est unio ypostatica, cum sint essencie a subiecto generaliter condistincte sine communicacione ydiomatum, ut substancia fiat tale accidens vel e contra. Ideo sicut in materia de Trinitate trinitas creata [p. 192] memorie, racionis, et voluntatis anime est inter omnes hucusque inventas simillima pro Trinitate increata viatoribus cognoscenda; sic in materia de Incarnacione ypostatica unio creati spiritus ad naturam corpoream, ut utrumque sit eadem persona hominis, est inter alias plus propinqua; nec possunt,¹ si non fallor, fieri evidencie ut, vel probetur talis impossibilitas unionis, vel quod Deus aliam naturam possit assumere, aut assumptam dimittere.

[ENGLISH]

## ¶4 · 192.9–192.14

> [p. 192] Sed instatur per hoc, quod gracia unionis foret gracia maxima possibilis creature, ut illa humanitas fiat Deus; et omnis gracia creata presupponit inesse tam gratificatum quam ipsum gratificans; ergo gracia unionis presupponit naturam assumptam, et per consequens ipsa natura prius est quam de facto assumitur.

[ENGLISH]

## ¶5 · 192.15–193.16

> [p. 192] Hic dicitur quod conclusio est concedenda, cum omne per se superius sit prius natura vel origine quam suum inferius; et per consequens et² prius quam passio vel accidens sibi inest. Sed ex hoc non sequitur quod illa humanitas potest esse non assumpta, etsi sit non assumpta pro illa mensura nature sive originis. Sed notandum quod duplex est gracia unionis. Prima increata, qua Verbum voluit eternaliter humanitatem illam sibi ypostatice copulare; et illa potest intelligi tripliciter, scilicet essencialiter, personaliter, sive formaliter, ut patet alibi. 2ᵈᵃ autem est gracia creata qua humanitas est sic formaliter³ grata Deo. Et ista gracia licet sit natura⁴ vel origine posterior⁵ quam subiectum, non tamen est possibile quod dicta humanitas temporaliter ipsam procedat sic quod mereatur graciam unionis; sicut Augustinus innuit Enchiridion 29°, cum non sit possibile ipsam manere per instans temporis⁶ non assumptam. Et sicut in aliis hominibus presupponitur gracia preveniens ad meritum, sic in Christo gracia unionis presupponitur naturaliter ad Christi meritum, etsi meritum [p. 193] pro instanti unionis naturaliter consequatur. Et istum credo esse sensum Augustini 17° De Civitate Dei ca°... ‘In rebus, inquit, per tempus exortis summa gracia est quod Deus in unitate persone homini nullis precedentibus meritis copulatur;’ non quod gracia sit membrum in corpore vel anima colligans unionem; sed quia ista unio sit gracia non preventa habitu disponente. Unde illa unio cum sit relacio racionis est posterius subiecta humanitate quoad genus cause materialis, et tamen est efficienter¹ prius quam Christus est hoc singulare vel individuum hominis, ut tangitur superius. Sed caveatur de prioritate² temporis aut prioritate² quoad consequenciam, cum omnia ista pro omni tempore Christi se mutuo consequantur. Unde Augustinus Enchiridion dicit quod ista unio fuit illi homini quodammodo naturalis, cum iste homo non poterit esse sine illa.

[ENGLISH]

## ¶6 · 193.17–193.31

> [p. 193] Et si queritur de subiecto eius primo dicitur quod anima est subiectum primum unionis creati spiritus, non quod sit infusus habitus, sed habitudo relativa. Alia autem unio corporis ad Verbum subiectatur multiplicative in corpore sicut filiacio temporalis, que est habitudo secundum quam cognitum³ causatum naturaliter est productum a suo simili in natura. Et per istas particulas patet quod Spiritus sanctus non est Filius Patris, nec vermis est filius hominis, ut docet Augustinus Enchiridion 3°, nec inanimatum est filius sui naturaliter generantis. Correspondenter unio est habitudo, secundum quam una natura alteri ydemptitate ypostatica copulatur; et illa dupliciter secundum diversitatem nature increate assumentis et nature create suppositis copulate. Nec est extraneum vocare illam unionem graciam cum sit donum perfectissimum gratis datum.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 189:
1–1 e contra . . . Christus om. A B C.
2 individuum A B C.
3 possit O.
4 nisi om. C; ut om. O.
5–5 illi unio quam ille hoc O.

p. 190:
1 tamen add. A B C.
2 adhereret quia B C; et A; pr. man.
3 sic A B C.
4 cuiuscunque O.
5 magna om. C.
6 cum add. A B C.
7 comitanter A B; comicantus C.

p. 191:
1 viatoris O.
2 sit non O.
3 Nonne aliter sic in omnibus codd. repetitum omitti debet ?
4–4 in . . . peticio om. B.
5 prius B C; et pr. m. A.
6 novem om. A B C.
7–7 p°les poterint A B C.

p. 192:
1 putant B.
2 et om. O.
3 formaliter om. O.
4 natura in ras. al. man. A; ullam B; nulla C.
5 posterius O.
6 per instanti A C; pro instanti B.

p. 193:
1 efficaciter C.
2-2 temporis . . . prioritate om. O.
3 9gniti^m (? cognitivum) O.
4 verba[?] (sic) A; verba B.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 190: l\\y Ce a dhere Ct ^o
p. 192: gmce of union | grace of vnton | in ras. al. man.
p. 193: be/ore | given. ^ ratl ^
```
