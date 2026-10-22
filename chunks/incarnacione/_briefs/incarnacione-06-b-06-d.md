# Translation brief: incarnacione 06-b–06-d

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-06-b.md chunks/incarnacione/wyc-incarnacione-06-c.md chunks/incarnacione/wyc-incarnacione-06-d.md` once and fix what it reports.
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

## Glossary (the 360 rows these chunks use; the full file is GLOSSARY.md)

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
| caritas | charity | ⛔ Never "love". *Amor* and *dilectio* → "love". The argument often turns on charity as the Holy Spirit (Lombard, *Sent.* I d.17). |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| obedienciarius | one who obeys | Non-classical agent noun: the subject bound to obey (not the monastic officer). Ruled 2026-10-02 (*Eccl.* 39.3). |
| caput | head | The card's key ruling, now a row: Christ alone is head of the church; kept apart from *capitaneus* "captain". Ruled 2026-10-02. |
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
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| appropriare; appropriacio | to appropriate; appropriation | Canon law: a parish church annexed to a college or house. Ruled 2026-09-28 (coordinator, delegated) (4 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| mortificacio | amortization | Land put into mortmain; with *manus mortua*. Ruled 2026-09-28 (coordinator, delegated) (2 sites). Of a privilege that dies by abuse (*mortificacio privilegii*, *Eccl.* 200.17): "mortification", with a G note (2026-10-02). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| papa | pope | Ruled 2026-09-28 (34 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| humidum radicale / fluens | radical / flowing moisture | The physicians' terms. Ruled 2026-10-02 (75.19). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| distrahens | diminishing qualifier | The logicians' *determinacio distrahens*, which takes away from what it qualifies ("a dead man"). Ruled 2026-10-02 (*Eccl.* 128.3). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| opinio | opinion | Opposed to *fides* throughout (*Dial.* 20.24–31). Ruled 2026-09-28 (11 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
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
| famosior | best-known [sense] | Pilot. |
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
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
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
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
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
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| subintelligere | understand as implied | Recurs through *Eccl.* 12. Ruled 2026-10-02. |
| distribucio accomoda | accommodated distribution | The logicians' term. Ruled 2026-10-02 (268.19). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
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
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humiliacio | humbling | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26–28). |
| immediate | without intermediary | The scholastic sense, ⛔ not "at once". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 30.30). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere (of the soul, the nature) | take up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| individuum | individual | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 35.7). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| synecdochica locucio | synecdochic locution | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39.14). |
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
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| illusor | deceiver | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| insensibilis | imperceptible; of a thing that cannot feel, without sensation | Two senses by referent: what cannot be perceived / what cannot perceive (*lapis insensibilis*, *Dial.* 56.3). Kept visibly paired with *sensibilis*. Ruled 2026-09-28 (3 sites). |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| discoli | froward | Douay–Rheims (1 Pet. 2:18). Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| mulier aliena | strange woman | Proverbs' figure. Pilot |
| mulier fortis | valiant woman | DR Prov. 31:10. Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| mundialis (noun) | worldly man | Beside *mundialitas*. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| humidum naturale | natural moisture | Synonym of *humidum radicale* (row above); G note at use. Ruled 2026-10-02 (*Eccl.* 17, 410.2). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| legiste | legists | Civil lawyers. Ruled 2026-10-02 (*Eccl.* 18, 420.20). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| bona de genere | good in kind | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| papa superstes | the surviving pope | Ruled 2026-10-02 (*Eccl.* 23, 567). |
| venia | forgiveness | Kept apart from *condonacio* "pardon". Ruled 2026-10-02 (*Eccl.* 23, 573.4). |
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
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| trahere in consequenciam | draw into a precedent | The legal idiom; *consequencia* stays "inference". Ruled 2026-10-07 (*Pot. pape* 94.13). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| Lincolniensis | Lincoln | Robert Grosseteste, bishop of Lincoln (S note at first occurrence), as in *De ecclesia*. Ruled 2026-10-07 (*Pot. pape* 59.8). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| heresis realis | real heresy (heresy in deed) | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 159.13). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| papa cesareus | caesarean pope | The pope as endowed temporal lord (chs. 10–12). Ruled 2026-10-08 (coordinator, delegated). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| summus sacerdos | high priest | DR; kept apart from *summus pontifex* "highest pontiff". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 265.20). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| summum sacerdocium | high priesthood | Cf. *summus sacerdos* "high priest". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-c, 11-d). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| pontifex (Old Testament, unqualified) | pontiff | Kept apart from *sacerdos* "priest"; *summus pontifex* of the Jewish priesthood is "high priest" (see *summi pontifices*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* ch. 11). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| refuga | deserter | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 325.27). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
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
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 06-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-06-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-06-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "89.11–92.16"
divisions: "cap. 6 (heading 'Cap. VI.' at 85.0); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "820 words; 817 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 2 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n128–n131 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 6, part 2: [TITLE]

## ¶1 · 89.11–90.5

> [p. 89] 2°. per hoc quod Christus non foret mobilis, sensibilis, passibilis, subditus patri vel parentibus secundum quod homo: que tamen glosa est maximum refugium negantibus de virtute sermonis scripturam sacram de Christo enunciantem⁴ talia. Et consequens⁴ sic probatur. Christus non⁵ secundum quod homo est univoce aliquid, nec aliqualiter accidentatus cum aliqua creatura: ergo non secundum quod homo est huiusmodi, ut predicitur. Patet consequencia⁶ ex hoc quod non est color concedendi, quod Christus secundum quod homo est sic formatus, nisi vel quia homo est sic denominatus, vel quia illa humanitas est sic formata. Primum non valet, cum non⁷ sit possibile Christum sic informari ut dicunt. Nec⁸ secundum prodest,⁸ cum illam humanitatem ponunt esse⁹ non suppositum, cui soli debetur accio. Et sic nec illam ponunt concipi, nasci, conversari, pati, ascendere, vel quascumque tales predicaciones personales suscipere. Cum ergo non sit predicacio synecdochica, nisi¹⁰ pars primo et principaliter recipit predicacionem,¹¹ que exinde secundario toti tribuitur; sequitur quod hec non est construccio synecdochica—Christus¹⁰ secundum humanitatem fatigatur, sicut tristatur aut moritur —cum repugnat illam humanitatem sic denominari; ut [p. 90] homo non est albus secundum faciem nisi facies sit alba. Et illa est acuta obex contra negantes scripturas cum glosa seipsam inficit¹ plus quam textus. Non ergo Christus secundum quod homo est alicuiusmodi,² nisi racio hominis univoce sibi conveniat; quia aliter, quid sibi et homini?³

[ENGLISH]

## ¶2 · 90.6–90.32

> [p. 90] 3°. confirmatur sic. Ad hoc quod satisfaciat⁴ pro peccato nature vel generis,⁵ oportet quod natura, que peccaverat, emerendo⁶ restituat:⁶ sed genus humanum peccavit in Adam et suis posteris: ergo oportet idem genus secundum aliquod eius suppositum ut satisfaciat⁷ pro peccato; sed non potuit secundum pure⁸ hominem: ergo relinquitur quod suppositum impeccabile satisfaciat assumendo eandem naturam in aliqua essencia singulari: quod et factum est per Verbum,⁹ ut superius dixerat Augustinus. Et illam¹⁰ racionem tangit Anselmus 2°· Cur Deus Homo ca°. 8. que, licet non sapiat negantibus universalia, saperet tamen cuicunque pio theologo.¹¹ Aliter enim non conveniencius assumendo humanitatem redemisset Deus peccatum hominis, quam peccatum angeli; cum plus convenit Christus post incarnacionem¹² secundum humanitatem angelo quam homini.¹² Nam ‘dii’ solum participative non plus in natura cum Deo conveniunt quam ante participacionem: sed tam equivoce dicitur ‘homo’ de Deo et de angelis¹³ quam equivoce ‘deus’ de creatura et natura divina dicitur: ergo tam equivoce disconveniunt Verbum et homo post incarnacionem sicut ante: sed ante plus conveniebat angelo quam homini: ergo¹⁴ modo. Quid ergo pertinuit¹⁵ Christi¹⁵ meritum humano generi a quo tante distitit? Non ergo satisfecit illud genus hominum quod peccavit; et per consequens manet in pleno debito sicut ante; quod est contra Apostolum ad Colos. 2. dicentem quod ‘in Christo Deus delevit cirographum decreti, quod erat nobis contrarium.’

[ENGLISH]

## ¶3 · 91.1–91.11

> [p. 91] Confirmatur. Vel est conveniencia maxima, qua Christiani cum Christo conveniunt tantum ex parte signorum, vel tantum ex parte naturarum¹ conveniencium, vel mixtim. Primum dictum est nimium² puerile, specialiter cum hoc signum ‘homo’ summe equivoce significat Christum et alios. Si ex parte signatorum, vel oportet dare eis naturam communem, vel aliter dicere quod in nullo conveniunt, nisi in quo differunt; et³ sic, ut plus conveniunt, plus differunt³; et cum tanta sit conveniencia quanta differencia et e contra; si⁴ igitur in infinitum differunt, in infinitum conveniunt, et e contra.⁴

[ENGLISH]

## ¶4 · 91.12–92.16

> [p. 91] Item, si Christus non sit univoce homo cum aliis, tunc nullum accidens consequens eius humanitatem foret univoce accidens cum accidentibus correspondentibus in suis fratribus. Consequens interimeret totam fidem, spem, et caritatem de Christi incarnacione, et falsificaret scripturas eque nequiter velut Eutichiani et alii heretici supra dicti. Et consequencia patet ex hoc, quod omne accidens individuatur, specificatur, et habet totam essenciam suam a subiecto. Ergo, si subiecta in nullo univoco conveniunt, a maiori vel pari nec accidencia que secuntur; ut, si angelus non sit eiusdem speciei secundum copulatum corpus cum nostro corpore, tunc nec⁵ accidencia, que appropriate⁶ consecuntur nostra corpora, conveniunt eis nisi equivoce; ut, angelus non dormit, comedit, sentit, gignit, et sic de accidentibus competentibus toti homini: aliter enim essent procreati ab incubis et succubis filii diaboli naturales, et non filii hominum nec proximorum parentum; quod nemo dicit. Si ergo locucio animati⁷ psittaci⁸ vel⁸ inanimati organi non est univoce⁹ locucio cum humana, saltem secundum speciem specialissimam¹⁰ propter diversitatem specificam¹¹ subiectorum; multo magis nullum accidens Christum consequens foret eiusdem [p. 92] racionis cum accidente create substancie; cum subiecta nec specie, nec genere, nec in aliquo univoco convenirent. Non enim plus convenit Christus nobiscum quam deitas, ut sic opinantes concorditer confitentur; et per consequens, cum accidencia non sint nisi modi create substancie, sequitur quod nulla accidencia de genere¹ Iesu nostro² conveniant; ut non pocius conceptus est, vel natus humanitus, ambulavit, predicavit, paciebatur sitim, esuriem, opprobria vel flagella, quam deitas ipsa; et sic fuit obiectum maxime illusivum, cum nec fuit quantus, nec qualis, nec aliquod³ aliorum⁴ encium, cum non sit mobilis aut sensibilis eo quod omne tale accidens univocum cum aliis⁵ requirit primum subiectum univocum quod informat. Sed Christus in nullo substanciali est nobis similis, ut dicitur; ergo nec in aliquo accidentali: non enim tantum conveniret sicut elementum, minera, bufo, bestia, vel quelibet⁶ creatura.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 89: *ciantem* (print = bt (enun-/ciantem)) [SUB]
  - 91: *locucio* (plate (full page n0130 l. 28): print = bt (Opus coordinator)) [AGREE]
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
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

p. 90:
1 interficit B.
2 modi *om.* A B C.
3 hominis O.
4 satisfiat A B C.
5 ergo A B C.
6 emendando resipiscat A B C; emêdo restituat O.
7 satisfacere B; *et altera manu* A.
8 purum A B C.
9 per sanctum filium B.
10 2^am A.
11 catholico C.
12–12 incarnacionem cum angelo quam cum homine A B C.
13 aliis *codd. omn.*
14 et *add.* C.
15–15 participavit Christus A B C

p. 91:
1 signatorum A B C.
2 intutum O.
3–3 et sic . . . differunt om. A B C.
4–4 si igitur . . . contra om. O.
5 nec om. O.
6 appropriate om. B; appPiete (Qu. a proprietate ?) O.
7 animati om. O.
8–8 siccati (in marg. secati) vel A; securati et B; secati vel C; sithaci vel O.
9 equivoce B.
10 sensitivam A B C.
11 factam A B C.

p. 92:
1 de add. O.
2 Christo B.
3 aliud A B C.
4 illorum B.
5 ~~aliis~~ (antecedens in marg.) A; accidens B.
6 quecunque A B C.
7 filiis om. B.
8–8 nec in genere om. O.
9 conveniunt A B; correspondent C.
10 attribuit om. O.
11 credimus O.
12 non om. A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 90: codcl. omn.
p. 92: ftance or acd-
```

---

## Chunk 06-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-06-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-06-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "92.17–96.29"
divisions: "cap. 6 (heading 'Cap. VI.' at 85.0); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1167 words; 1163 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n131–n135 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 6, part 3: [TITLE]

## ¶1 · 92.17–94.22

> [p. 92] Ideo dicunt sic opinantes consequenter, sed minus catholice, quod Christus non est mobilis vel accidentatus humanitus. Quod si verum est, tunc indubie non est homo in aliquo fratribus suis consimilis. Quomodo, rogo, haberet fratres, si non sit univoce filius hominis habens eundem patrem et matrem remotos cum filiis⁷ aliis, et sic temporaliter conceptus, genitus, atque natus, et sic consequenter, ut canit historia evangelica, conversatus? aut quomodo esset nedum in substancia vel natura vel in aliquo accidente fratribus suis consimilis, si nec⁸ in genere,⁸ nec in specie, nec in accidente univoco convenirent⁹? Pro certo dicat qui audet! quia ego non audeo tantum subvertere totum sensum historicum scripturarum, cum evangelium sicut et vetus testamentum expresse et absolute attribuit¹⁰ sibi denominaciones accidentales creatas. Quomodo, queso, crederemus¹¹ aliquid de Christo, si non¹² assercionem propriam, [p. 93] qua dicit, ‘palpate et videte, quoniam spiritus carnem et ossa non habet, sicut me videtis habere.’ Ioh. ult°.? ex qua¹ doctrina hauserat ille celicus paranymphus,² quando in principio capituli sui dicit, ‘Quod fuit ab inicio, quod audivimus, quod vidimus oculis nostris,³ quod perspeximus, et manus nostre contrectaverunt de Verbo vite, anunciamus vobis’? Et Apostolus ad Hebre. 4°. ‘habentes pontificem magnum, qui penetravit celos Iesum Filium Dei, teneamus spei nostre confessionem:⁴ non enim habemus pontificem, qui non possit compati⁵ infirmitatibus nostris; temptatum autem per omnia pro similitudine absque peccato.’ Quod dictum Apostoli ego nescio aliter exponere quam expositum est a sanctis doctoribus. Per hoc ergo quod Iesus est filius Dei, est ‘pontifex magnus⁶ superior Aaronitis.’⁶ Per hoc quod potestate propria ‘penetravit celos,’ solus ascendit⁷ trahens alios secum. Per hoc quod potest compati nobis in natura communi assumpta, factus est nobis propicius; quia ad Hebre. 5°. dicitur ‘cum esset Filius Dei, didicit ex his, que passus est, obedienciam.’ Experiencia enim temptacionis multimodis⁸ didicit⁹ humanitus, que aliter non sic sciret.¹⁰ Temptatus¹¹ enim erat tripliciter a dyabolo, ut patet Matth 4°; et quadrupliciter¹² a Iudeis de potencia, sapiencia, misericordia, et iusticia, ut patet ex decursu evangelii. Non autem intrinsece a seipso. Quarto fuit illa temptacio nobis pro similitudine exemplari ad docendum nos gratis compati et vincere temptatores,¹³ quia capitaneus apostolorum 1 Pet. 2°. vere testatur quod ‘Christus passus est pro nobis,¹⁴ vobis relinquens exemplum ut sequamini¹⁴ vestigia eius.’ Ista est exposicio sana, cui oportet nos insistere non superaddendo aliam¹⁵ pre timore impugnacionis sophistice de vi vocis. Non quod fuit in capite nostro¹⁶ ficta passio et non [p. 94] vera, ut dixerunt heretici supradicti; sed veram conversacionem, veram passionem, veram mortem, et alias predicaciones sustinuit; ut meminit Augustinus esse de substancia fidei in De Vera Religione 29°. et Enchiridion 4°¹ ca°. ‘Nos, inquit,² patimur egencias et dolores, sed³ indubie magis ipse; nam “pro nobis egenus factus est.”’ 2 Cor. 8°. Et cum in perfecta etate, tenerrima complexione,⁴ sensu vivacissimo,⁵ non mortificato aliquo membro, in media etate, non supernatante humido⁶ infantili⁷ sit passus, patet quod in nullo alio est pena vel ‘dolor tantus sicut fuerat dolor suus,’ ut cecinit Isa. 53°. Secundo fratres sui fossi sunt sub terra vel lapide, sed ipse plus, cum Dominus mundi sepultus est sumptibus alienis, ut meminit Augustinus in De Questionibus Veteris et Nove Legis ca° 59:⁸ et, ut breviter dicatur, quicquid debuit facere fecit ad summum, cum oporteat⁹ principia exemplaria esse ultima⁹; et eo fecit hec omnia excellencius, quo ipse fuit humanitas copulata ypostatice deitati. Cum ergo omnes ille maneries accidencium creatorum infuerunt sibi formaliter, et omne tale accidens requirit subiectum sibi proporcionatum; sequitur quod Christus subiectus eis sit idem in specie cum subiectis accidencium consimilis speciei.

[ENGLISH]

## ¶2 · 94.23–94.33

> [p. 94] Sed arguendo contra illud videtur primo tripliciter quod non debet concedi simpliciter quod Christus sit mobilis. Nam¹⁰ non foret evidencia concludendi quod Christus sit mobilis,¹⁰ nisi ex hoc quod secundum humanitatem est mobilis. Sed talis deduccio non procedit, cum arguitur a¹¹ secundum quid ad¹¹ simpliciter. Ergo non est medium concludendi¹² quod Christus sit mobilis. Sicut ergo non sequitur—Christus secundum humanitatem est creatura; ergo Christus est creatura—; ita non sequitur—Christus secundum humanitatem est mobilis; ergo Christus est mobilis.

[ENGLISH]

## ¶3 · 95.1–95.23

> [p. 95] Hic dicitur concedendo quod Christus est mobilis cum humanitas sua sit mobilis. Et dicant, qui sciunt, quia pro certo non puto aliam creaturam, sed neque Deum cognoscere quod Deus sit mobilis, nisi ex hoc quod creatura est mobilis que Deo ypostatice copulatur. Et per locum a sufficienti similitudine concedi debet simpliciter quod Christus est creatura, quia tota humanitas eius sibi copulata ypostatice est creatura.¹ Sicut enim negacio includitur in racione creature, que negacio non potest competere divinitati; sic in motu et qualibet forma substanciali vel accidentali in genere: et per consequens, negato quod Christus est creatura, negari debet quodlibet per se inferius; ut, quod est homo, animal, corpus, anima, sive substancia, et multo evidencius quod sit mole magnus, accidentaliter² qualis, filius hominis, predicans,³ passus, locatus, temporaliter natus, sedens, vestitus; quia quodlibet istorum⁴ est inferius, indignius, et humilius⁵ quam esse substanciam, et⁶ presupponit substanciam tanquam subiectum dans eis esse accidentale in genere. Omne itaque per se in genere dicit esse suum possibile esse pro aliqua mensura, pro qua non habet existenciam actualem; et per consequens omne per se in genere dicit se esse creaturam includendo neminem esse primitatis divine.

[ENGLISH]

## ¶4 · 95.24–96.15

> [p. 95] Unde scriptura sacra⁷ anunciat Christum simpliciter esse factum, ut ad Gal. 4°. ‘misit Deus Filium suum factum ex muliere, factum sub lege.’ ‘Non⁸ sunt audiendi, inquit Beda, qui legunt “natum ex muliere”’⁹ Et credo quod nullus dicit hoc determinatum ‘ex muliere’ esse terminum distrahentem quin sequatur—factus ex muliere; ergo factus—; sicut sequitur—compositus ex corpore et anima; ergo compositus—. Et ideo dicit Augustinus Enchiridion 29, quod illam creaturam, quam virgo concepit et peperit, quamvis ad solam personam Filii pertinentem, tota Trinitas [p. 96] fecit; et illam creaturam declarat esse Filium Dei tempore¹ immediate sequente. Et idem dicit in Sermone de Vigilia Epiphanie; ‘magnum misterium fuit, quod creator creari voluit’: et in Sermone Domini in Monte; ‘voluit esse creatura, qui est creator.’ Item ad Hebre. 3°. scribit Apostolus: ‘considerate apostolum et pontificem confessionis nostre² Iesum, qui fidelis est ei qui fecit illum.’ Ecce hic dicit absolute quod Deus fecit Iesum. Unde Leo Papa in quodam sermone; ‘nova et inaudita convencio, Deus qui eternaliter erat, fit creatura.’ Et Lincolniensis in sermone De Natali Domini; ‘in spectaculo³ creacionis⁴ conspicitur creator faciens creaturam; in isto spectaculo³ conspicitur creator factus creatura.’ Et Johannes Damascenus ca°. 50. ‘Christus est creatus et increatus:’ unde et ca°. 92 concedit quod Christus est creatura.

[ENGLISH]

## ¶5 · 96.16–96.29

> [p. 96] Item nichil habet Deum ut superiorem nisi creatura: Christus sic habet:⁵ ergo est creatura. Minor⁶ patet ex confessione Veritatis Matth. 27. ‘Deus meus’; et Ioh. 20. ‘vade ad fratres meos et dic eis: Ascendo ad Patrem meum et Patrem vestrum,⁷ Deum meum et Deum vestrum’⁷; et ad Ephes. 1°. ‘Deus Domini nostri Iesu Christi, Pater glorie, det vobis spiritum sapiencie’; et 1ᵃ ad Cor. 3°. ‘vos⁸ estis Christi, Christus autem Dei’; et infra 11°, ‘caput vero Christi Deus.’ Et ad idem sonat tota scriptura de humanitate Christi; et specialiter illud Veritatis ‘Pater maior me est.’ Ioh. 14⁹; et illud ‘seipsum exinanivit, formam servi accipiens’ ad Phil. 2, ut exponit Augustinus primo libro Contra Maximinianum. Non enim audebant¹⁰ sancti doctores inficere scripturam suspicione falsitatis, ut hodie.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 94: *in nullo alio est* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Heb. iii. i. (96.5); reference and by John of [C 66b] (96.13).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 92:
1 de add. O.
2 Christo B.
3 aliud A B C.
4 illorum B.
5 ~~aliis~~ (antecedens in marg.) A; accidens B.
6 quecunque A B C.
7 filiis om. B.
8–8 nec in genere om. O.
9 conveniunt A B; correspondent C.
10 attribuit om. O.
11 credimus O.
12 non om. A B C.

p. 93:
1 quadam O.
2 peranimphus A C; peranyniphus B; selitus paranı̄phus O.
3 oculis nostris om. B.
4 confessionem om. A B C.
5 compari O.
6–6 C om. superior; O om. Aaronitis, uterque cum lacuna.
7 ascendens A B C.
8 multitudine A B C; multi^do O.
9 dicit A B C.
10 foret A B C.
11 tempestatus O.
12 quadrupliciter om. O.
13 temptaciones A B C.
14–14 nobis . . . sequamur A B C.
15 alicui A; aliquam B.
16 nostro om. A B C O; e cod. M. inserui.

p. 94:
1 40 O.
2 ergo O.
3 sed om. A B C.
4 et add. A C; at add. B.
5 vacuissimo A B C.
6 humido om. cum lacuna C.
7 infantuli O.
8 79 O.
9–9 principalia . . . ultra A B C.
10–10 nam . . . mobilis om. A B C.
11–11 a quo ad O.
12 concedendi A B C.

p. 95:
1 creata O.
2 accnt^er (i.e. accidenter) O.
3 predicant O.
4 n̄ (i.e. nomen) add. O.
5 minus A B C; vmis O.
6 sed C O.
7 sacra om. C.
8 notum C.
9 sed factum ex muliere add. C O.

p. 96:
1 tempore om. O.
2 vestre C O.
3 speculo B.
4 creaturarum A B C; c^is O.
5 esse add. O.
6 maior O.
7–7 et deum etc. C; deum . . . vestrum om. O.
8 nos C.
9 15 A B C.
10 audiebant O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 92: ftance or acd-
p. 93: [ J e ^ ts m ' the 2 ^
p. 94: secundum quid
p. 95: ft natum
p. 96: jy eus
```

---

## Chunk 06-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-06-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-06-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "96.30–100.18"
divisions: "cap. 6 (heading 'Cap. VI.' at 85.0); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "979 words; 977 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n135–n139 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 6, part 4: [TITLE]

## ¶1 · 96.30–97.9

> [p. 96] Unde Doctor Subtilis super Distinccione 11. 3ⁱⁱ Sentenciarum dicit quod hec proposicio—Christus est creatura—est concedenda simpliciter, si bene intelligatur, sed negabatur propter hereses dicencium Christum esse pure creaturam: [p. 97] et fingit postmodum responsiones ei, cui non placet sic dicere. Concedit autem consequenter simpliciter cum Augustino quod Christus incepit esse¹ sicut generabatur ex tempore. Unde Doctor Bonaventura super eadem Distinccione dicit quod doctores magis hoc² respiciunt, quod potest esse via in falsitatem vel errorem, quam quod ipsa de se sit falsa vel erronea. Unde concedit³ consequenter quod Christus est homo creatus et non⁴ homo eternus, cum sit secundus Adam habens multos homines seniores.

[ENGLISH]

## ¶2 · 97.10–98.3

> [p. 97] Quandocunque ergo ego dico, quod Christus est creatus vel factus, intelligo catholice, sicut⁵ scriptura sacra et sancti doctores me edocent, quod Christus secundum humanitatem est creatus⁶ vel taliter temporaliter denominatus. Et illam regulam dat⁶ sanctus Thomas 4°. Contra Gentiles 48. ‘Nihil, inquit, Deo proprium enunciatur de Christo nisi racione humanitatis vel expressate vel subintellecte: nec⁷ e contrario quoad denominaciones eternas, quas homo ille recipit secundum divinitatem.’ Et sic eum gloso ac alios quosdam, quando dicunt quod Christus non est creatura; intelligunt enim quod Christus non est secundum divinitatem creatura: quod est necessarium, cum oppositum sit hereticum. Et quod ille sit sensus suus videtur, quia super 2ᵐ. Sentenciarum Dist. 11. Quest. 4⁸ dicit quod accidencia creata dicuntur de Filio Dei, non quod ipsa persona eterna his⁹ informatur, sed quod natura assumpta⁹ his¹⁰ informatur. Quod dictum ego nescio sane concipere nisi intelligendo quod persona Verbi non informetur¹¹ accidentibus creatis secundum deitatem, sed quod ipsa principaliter informetur eis secundum humanitatem. Nam Verbum predicat et agit actos humanos, informatur virtutibus et beatitudine, sicut substancialiter informatur anima intellectiva et creata racionabilitate.¹² Ideo certum est quod persona Verbi informatur istis accidentibus ac formis creatis, nisi coincidatur in opinionem negantem [p. 98] mobilitatem Christi simpliciter. Et illa glosa est evidencior et famosior quam glosa data a modernis ad scripturam sacram et dicta sanctorum.

[ENGLISH]

## ¶3 · 98.4–98.19

> [p. 98] Quidam enim dicunt quod talis modus loquendi transit¹ in abusum: alii quod doctores desipuerunt ignorantes logicam: tercii² quod dixerunt impossibilia et heretica propter devocionem³ exhortacionis.³ Sed quarti recte intelligunt quod dicta intelliguntur de Christo secundum humanitatem; et ipsi vere intelligunt, specialiter si ponant quod Christus est illa humanitas et non in construccione synecdochica; cum illa humanitas sit totus Christus, et non⁴ pars eius⁴ formaliter. Synecdochica enim locucio⁵ vel evidencia est⁵ a quo⁶ ad simpliciter, quando parti principaliter attribuitur denominacio, et secundario suo toti; ut hic homo est racionalis vel quantus. Unde quantum ad priores glosantes dicitur quod affeccione inordinata extraneandi in logica, postposita glorificacione scripture, ‘dicentes se esse sapientes stulti facti sunt’: in cuius signum vix duo concordant tam in sentencia quam in glosa.

[ENGLISH]

## ¶4 · 98.20–98.33

> [p. 98] Sed obicitur tripliciter contra illud. Primo per hoc quod, si Christus creatus est, tunc est productus ex nichilo, et per consequens aliquando non fuit: quod est impossibile, cum sit Deus. Sed rogo sic arguentes attendere quomodo per⁷ idem non sequeretur⁷ quod, si⁸ Christus generatus est ex tempore, conceptus, et natus de virgine, ergo habuit esse post non esse: cum omnis generacio substancie sit produccio a non esse substancie ad esse secundum philosophos. Nec negandus est ‘liber generacionis Iesu filii David, filii Abrahe,’ ut patet Matth. 1°; vel conceptus⁹ aut partus virginis, ut patet Luce 1° et 2°; duplicem enim nativitatem Christi catholici concorditer confitentur. Nec est racio quod creacio non competit¹⁰ Christo secundum esse suum temporale, sicut competit sibi generacio aut incepcio.

[ENGLISH]

## ¶5 · 99.1–99.18

> [p. 99] Conceditur ergo quod Christus creatus est nedum secundum animam, que est Christus, sed secundum corpus. Nam generatus est secundum corpus, et hoc generacione univoca sicut univoce est homo. Sed omnis alia generacio substancie presupponit eius creacionem: ergo et Christi generacio temporalis. Omnis itaque temporalis nativitas, sicut et motus nature create sensibilis aut insensibilis, presupponit creacionem ut causam, cum prius naturaliter sit creacio simpliciter quam aliqua mocio naturalis. Ex quo plane sequitur, quod omne naturaliter motum prius naturaliter creatur quam naturaliter sic movetur. Cum ergo Christus naturaliter movetur, et per consequens accidens creatum inest sibi formaliter; sequitur quod prius naturaliter est creatus¹: quia aliter¹ indubie non esset denominatus univoce cum ceteris creaturis. Conceditur ergo quod Christus productus est ex nichilo, et sic aliquando non fuit. Primum patet de anima et de corporea essencia in mundi principio; et secunda pars patet intelligendo Christum secundum illam naturam, qua creatus est.

[ENGLISH]

## ¶6 · 99.19–99.33

> [p. 99] Sed in istis² oportet cavere diligenter et excludere tres sensus erroneos quando dicitur Christum aliquando non fuisse. Primo cavendo ne credatur Christum³ aliquando secundum deitatem non fuisse, cum Christus eternaliter fuit Deus. 2°· ne credatur Christum secundum esse intelligibile humanitatis ac predestinacionem Dei aliquando non fuisse, cum eternaliter habet esse intelligibile predestinatum esse Filius Dei. Et 3° ne credatur aliquando non habere esse⁴ essencie materialis, cum⁵ massa essencie materialis⁵ et corporee, que est Christus, sit in mundi principio et non possit deficere. Exclusis ergo istis tribus sensibus erroneis, claret quartus,⁶ verus sensus catholicus, quod Christus secundum existenciam humanitatis aliquando non fuit. Quod⁷ cum sit verum⁷ et implicans Christum aliquando non fuisse, eo quod ipse est illa humanitas, est catholice concedendum.

[ENGLISH]

## ¶7 · 99.34–100.18

> [p. 99] Quod si moveat quemquam quod Christus est creatus vel [p. 100] factus ex nichilo; rogo, quomodo diceretur, si pro instanti incarnacionis corpus Christi subito per¹ totum creatum limitaretur,¹ et anima tunc² creata sibi pro eodem instanti uniretur, et pro eodem instanti natura completa ypostatice sumeretur? Numquid credimus quod Christus non tunc temporaliter produceretur? Baptisemus³ ergo illam faccionem sive produccionem subitam. Et patet quod non superest nomen competens nisi ‘creacio’ cum tota humanitas a solo Deo⁴ producitur ex puro⁵ nichilo precedente temporaliter in effectum: et cum produccio per se et proprie terminatur ad suppositum, relinquitur, quod Christus in illo casu sit factus ex nichilo; et sic omnia argumenta, que viderentur⁶ militare contra creacionem Christi in⁷ faccione ex virgine, procederent contra illud preter hoc, quod essencia corporea, que est Christus, creata⁸ est in mundi principio et interim per patriarchas ac demum per beatam virginem ministerialiter alterata; et revera hoc, licet sit⁹ gloriosius,⁹ est magis mirabile.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference Heb. iii. i. (96.5); reference and by John of [C 66b] (96.13); reference Rom. i. 22. (98.19); reference Matth. i. (98.30).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 96:
1 tempore om. O.
2 vestre C O.
3 speculo B.
4 creaturarum A B C; c^is O.
5 esse add. O.
6 maior O.
7–7 et deum etc. C; deum . . . vestrum om. O.
8 nos C.
9 15 A B C.
10 audiebant O.

p. 97:
1 esse om. O.
2 hoc om. A B C.
3 concepit A B C.
4 unus A B C.
5 sicut om. C.
6–6 vel (rasura) temporaliter denominatus et (rasura) dat A; vel creavit vel temporaliter denominatus et (ceteris ad enunciatur om.) B; vel talis temporaliter denominatus est et illam rᵃᵐ dat C.
7 et A B C.
8 9 A B C.
9–9 informatur . . . assumpta in marg. O.
10 eis O.
11 informatur A B C.
12 rǒlitate O.

p. 98:
1 transit om. C.
2 alii B; et pr. manu A.
3-3 devocionis exhortacionem A B C.
4-4 non per consequens eius C.
5-5 locucio est vel evidencia codd omn.
6 a quo alt. manu A; a secundum B; a s' C.
7-7 perinde non sequitur O.
8 si om. O.
9 vel conceptus om. C.
10 convent C.

p. 99:
1_1 creatus quam aliter quia aliter C.
2 illo A B C.
3 secundum A.
4 esse om. O.
5_5 cum . . . materialis om. O.
6 quartus om. A B C.
7_7 cum tamen est verum C.

p. 100:
1_1 crearetur et liniamentaretur M.
2 pro tunc O.
3 baptizaremus O.
4 Deo *om.* B.
5 ex po^z (*pro* ex p^zo) B C; ex pure O.
6 videntur A B C.
7 ex A B C.
8 creata *om.* O.
9 sit graciosius A B C.
10 analogis C.
11 famosma O.
12 nedum B.
13_13 de Christi humanitatis O.
14 audiamus O C.
15 fidem *om.* O.
16_16 nobis . . . et *om.* O.
17 modo C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 96: jy eus
p. 98: b comtt?Kdf° na | alt. manu
```
