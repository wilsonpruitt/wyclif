# Translation brief: incarnacione 07-a–07-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-07-a.md chunks/incarnacione/wyc-incarnacione-07-b.md chunks/incarnacione/wyc-incarnacione-07-c.md` once and fix what it reports.
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

## Glossary (the 359 rows these chunks use; the full file is GLOSSARY.md)

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
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| capitaneus | captain | Kept apart from *caput* "head": Wyclif grants the pope captaincy and denies him headship. Ruled 2026-10-01 (*Eccl.* 17.13, 19.21–24, 22.8). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| speculator | watchman | The bishop as watchman (Ezek. 3:17). Ruled 2026-10-02 (*Eccl.* 55.16). |
| ecclesiastici | CONTEXTUAL: clergy / those who belong to the church | Usually the clergy; where Wyclif means every member of the church (*Eccl.* 81.4) render "those who belong to the church" and write a **C** note. Ruled 2026-10-02. |
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
| magnates | magnates | Ruled 2026-09-28. |
| capitalis dominus; tenere de | chief lord; to hold of | Feudal tenure language, kept literal: the lords "hold of Christ as chief lord". Pilot (Dialogus 2.19). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| manus mortua | the dead hand | Mortmain; kept literal because Truth's pun turns on it (*Dial.* 60.18, 61.14–17). Ruled 2026-09-28 (coordinator, delegated) (3 sites). |
| affeccio proprietaria | proprietary affection | Ruled 2026-09-28 (coordinator, delegated). |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| sacramentalia | sacramentals | Ruled 2026-09-28 (coordinator, delegated). |
| secularitas | worldliness | Kept apart from *secularis*, a secular. Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| secularis (noun) | a secular | English keeps Latin's range (secular cleric or layman); a C note where the referent matters. Ruled 2026-09-28 (coordinator, delegated) (80 sites, *secular-*). |
| commercium; commercari | trade; to trade | Ruled 2026-09-28 (21 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| doctrina | doctrine | Kept apart from *sentencia*, teaching. Ruled 2026-09-28 (12 sites). |
| possessionati | the possessioners | Endowed religious. |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| ficticia | fiction | A feigned ground in an objection (*Nec valet ficticia*). Ruled 2026-10-02 (145.19). |
| allegare / allegacio | allege / allegation | To cite as an authority; implies nothing about truth (the period sense). Ruled 2026-10-02 (*Eccl.* 162–165; as earlier chunks). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| sophisticare (transitive) | to counterfeit | Kept apart from *sophisticari*, to play the sophist. Ruled 2026-09-28 (coordinator, delegated). |
| respectus; respectivus | relation; relational | Ruled 2026-09-28 (coordinator, delegated). |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| sophisticari | to play the sophist | Ruled 2026-09-28 (6 sites). |
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
| redarguere | to refute | T. p. 365. |
| proponere | to propose | Against *postponere* (put after), "put forward" may keep the pair visible, with a note (*Dial.* 74.25–26). |
| concludere | to infer | "Conclude" only when a conclusion is literally drawn (T. p. 365). |
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| descripcio | definition | Not "description" (T. p. 363). |
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
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
| reditus | revenue(s) | Ruled 2026-09-28 (23 sites). Exception: *Dial.* 18 (ch. 9 n5), *reditus* = the clergy's "return" (to wealth), on *revertatur* 15.9 / *redire* 15.21; the note gives "revenue" as the alternative. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| capitas | headship | Non-classical abstract of *caput* (*officium capitatis*). Ruled 2026-10-01 (*Eccl.* 18.19; B *capitis*). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| influxus / influere | inflow / flow in | The head's inflow of grace into the members; not "influence" (which renders *influencia*). Ruled 2026-10-02 (33–34). |
| citra Christum | short of Christ | As *citra fidem*. Ruled 2026-10-02 (45.8). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| capitaliter | as head (as chief lord) | Ruled 2026-10-02 (64.33, 76.9). Of a crown worn on the head (Apoc. 12:1, *Pot. pape* 143.20): "at her head", with a C note (2026-10-08). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| capitari / capitatus | to be headed / headed | The verb beside *capitas*. Ruled 2026-10-02 (116.21, 117.2–3). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| mundialitas / secularitas | mundanity / worldliness | Kept apart. Ruled 2026-10-02 (*Eccl.* 9). |
| impetrare | obtain (by request) | Ruled 2026-10-02. |
| falsigraphus | false writer | The one who sets out false figures or texts. Ruled 2026-10-02 (*Eccl.* 9). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
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
| misterium | mystery | Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.3). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| fontaliter | fontally | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 17.13). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| motrix (*anima*, *virtus*) | moving | *Anima motrix* "the moving soul"; as a noun, "mover". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| exinanicio / exinanire / inanicio | emptying / empty | Phil. 2:7 (Douay "emptied himself"); *inanicio* (*Incarn.* 33) the same. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| minoracio | lowering | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 26). |
| humanitus | humanly | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* passim). |
| suscipere (of the soul, the nature) | take up | Kept apart from *assumere* "assume". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 31). |
| suppositum | supposit | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 34.24). |
| in quantum (reduplicative) | insofar as | As *secundum quod*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37.9). |
| synecdochica locucio | synecdochic locution | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 39.14). |
| universitas creaturarum | the totality of creatures | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 37). |
| diccio (logical) | word | A single term in a proposition. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 43.3). |
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
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
| ampliativus | ampliative | Beside *ampliacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 57.29). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| peiorare / peioracio | make worse / worsening | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 65–68). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| adnichilare / adnichilacio | annihilate / annihilation | Wyclif's *De adnichilacione*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76). |
| libere contradictorie | freely, as between contradictories | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 76.15). |
| peccabilis | able to sin | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| capitales doctores | the chief doctors | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| intricaciones sophistice | sophistical entanglements | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 82). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
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
| faccio | making | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.6). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| ministerialiter | ministerially | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 100.17). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| sensibilis | perceptible | "sensible" (T. p. 362) |
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| affectare | to desire | Kept apart from *affeccio*, affection. Ruled 2026-09-28 (3 sites). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| limitare; limites | to assign (an office); limits | "to limit" for the verb (i.e. never "to assign" where it means to restrict, as beside *restringere*, *Eccl.* 217.10, 2026-10-02). The noun *limites* stays "limits" (*in limitibus apostoli*). Ruled 2026-09-28 after a census (13 verb, 5 noun). |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
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
| redempcio temporalium | redemption of the temporal goods | Chapters buying back seized goods. Ruled 2026-10-02 (*Eccl.* 15, 340.15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| redempcio (of a sentence) | redemption | Buying off a penalty; kept apart from *redempcio temporalium*. C note at first use. Ruled 2026-10-02 (*Eccl.* 15, 352.1). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| ecclesia nuncupativa | the church in name only | Ruled 2026-10-02 (*Eccl.* 17, 408.27). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| falsarius | falsifier | The opponent's epithet. Ruled 2026-10-02 (*Eccl.* 17, 414.6). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| unum per accidens | one by accident | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| capitales (noun) | chiefs | Ruled 2026-10-02 (*Eccl.* 18, 424.30). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| limitacio (ad officium) | assignment | Follows *limitare* "to assign" (row above); where it means restriction, "limitation". Ruled 2026-10-02 (*Eccl.* 19, 445). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| ecclesiasticus (sg. noun) | ecclesiastic | Ruled 2026-10-02 (*Eccl.* 19, 453.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| commentum (mendacii) | fabrication | Wyclif numbers the opponent's fabrications. Ruled 2026-10-02 (*Eccl.* 21, 498.31). |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| baptismus flaminis | baptism of the Spirit | Ruled 2026-10-02 (*Eccl.* 21, 514.24). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| affeccio naturalis / deliberativa | natural / deliberative affection | Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| satisfaccio; satisfacere | satisfaction; to make satisfaction | Cf. *satispassio*. Ruled 2026-10-02 (*Eccl.* 23, 556). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
| colorabilis | colourable | Beside *color*, *colorare*. Ruled 2026-10-02 (*Eccl.* 23, 575.1). |
| potestas ordinis | power of order | Ruled 2026-10-02 (*Eccl.* 23, 575.15). |
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| potencia | CONTEXTUAL: potency / power | "Potency" inside Aristotle's analysis of *dynamis* (active / passive potency, rational potency, the potency terminated); "power" elsewhere (God's power, free choice, might). Wyclif uses *potestas* and *potencia* interchangeably (*potestas vel potencia*, *Pot. pape* 4.7): a pair is "power or potency" with a **C** note. Keeps *potencia absoluta* "absolute power". Ruled by Wilson 2026-10-07 (*Pot. pape* 01-a review). |
| potentatus | CONTEXTUAL: sovereignty / potentate | The abstract "sovereignty" (*Pot. pape* 4.27); of the person who holds power "potentate" (*Pot. pape* 14.20, 15.13, 16.17, 20.28, 22.20, 23.13, 27.13), no note needed where the person is plain. Ruled 2026-10-07 (coordinator, delegated). |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| primitas | firstness | Being first in order, as against *primatus*. Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| archivicarius | archvicar | Ruled 2026-10-07 (*Pot. pape* 62.20). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| seculares domini | secular lords | Kept apart from *temporales domini* "temporal lords". Ruled 2026-10-07 (*Pot. pape* 52.16). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| capitalis (civitas, episcopus) | capital (city, bishop) | Rome as capital (ch. 8); *capitalis dominus* stays "chief lord". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 166.28). |
| influencia (celestis) | (celestial) influence | Astrological sense. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 172.1). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| pompare; pompacio; pompa | boast; boasting; boasting | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 204.11). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| capitalitas | capital standing | Rome's standing as capital; cf. *capitalis*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 216.1). |
| media (of an argument) | middle terms | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 222.20). |
| carismata; carisma | CONTEXTUAL: charisms / chrism | "Charisms" (gifts; *Pot. pape* 176.1). Singular *misticum carisma* in Augustine's sense of the anointing that names Christians (*chrisma*, *Pot. pape* 312.16) "chrism", with a T note. Ruled 2026-10-08; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| primicia (virtutum) | being first (in the virtues) | Kept apart from *primatus* "primacy" and *primitas* "firstness". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 228.33). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| archiprepositus | arch-superior | Formed on *prepositi* "superiors". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 300.17). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| sacramentum cesareum | caesarean sacrament | Ironic. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 320.23). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| potissimus; pocior (Antichristus) | foremost; greater | Superlative and comparative kept visible as a pair. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.28, 331.12). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| capitalis eleccio | the chapter's election | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| sophisticare quod (with a clause) | argue sophistically that | Takes *sophisticari*'s sense, not "counterfeit" (which needs an object). Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 354.11). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| specularis prudencia | the prudence of a watchman | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |

---

## Chunk 07-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-07-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-07-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "105.0–109.20"
divisions: "cap. 7 (heading 'Cap. VII.' at 105.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1071 words; 1070 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n144–n148 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 7, part 1: [TITLE]

## ¶1 · 105.0–105.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 105] [Declarando Christi mobilitatem explanat sensum scripture multis ambiguum, quomodo sapiencia summe mobilis sit habitu inventa ut homo. The sense in which Christ is subject to change (mobilis) is defined by discussing Wisdom vii. 24, ‘Wisdom is more moving (mobilior) than any motion,’ and Philipp. ii. 8, ‘found in fashion (habitu) as a man.’]

[ENGLISH]

## ¶2 · 105.11–107.7

> [p. 105] Secundo principaliter arguitur non esse concedendum quod Christus sit mobilis. Nam si Christus sit mobilis, tunc Deus est mobilis: sed nullus Deus est mobilis:³ ergo nec Christus. Minor sic arguitur.⁴ Aliqua res est immobilis: sed⁵ nulla, si non Deus: ergo Deus est immobilis:⁵ et cum unus Deus sit omnis Deus, sequitur quod omnis Deus et per consequens omnis⁶ persona divina sit simpliciter immobilis, et per consequens nulla est mobilis.⁷ Si ergo Deus sit mobilis, et omne aliud a Deo sit⁸ mobile, sequitur quod omne ens⁹ sit mobile, et sic nullum immobile. Ex quo sequitur quod Christus non sit passus, mortuus, aut cum hominibus conversatus, cum tunc esset destructibilis¹⁰ et adnichilabilis. [p. 106] Hic dicitur quod necesse est aliquam rem esse omnino immobilem; quod patet tripliciter. Primo ex hoc quod omne motum oportet inniti alicui fixo immoto: universitas¹ creata est mota: ergo oportet illam inniti alicui fixo immoto:¹ sicut² ergo mixta terrestria innituntur orbi terre, qui non commovebitur secundum centrum fluctuans huc aut illuc, sic omne motum cum sit ordinatum sic moveri ab alio oportet stare in suis limitibus secundum³ ordinacionem principaliter⁴ ordinantis: quia cum moveri sit imperfeccionis et posse movere perfeccionis simpliciter, patet quod prius est pura perfeccio quam imperfeccio exemplata. 2°. patet idem ex hoc quod veritates multe eterne, tam affirmaciones quam negaciones, sunt omnino immobiles; ut ‘quod nichil simul est et non est’; ‘quod multa encia possunt esse,’ etc.⁵ Cum ergo omnem rem racionis oportet fundari in absoluta essencia, sequitur quod oportet dare essenciam vel naturam immobilem, cui innixe predicte⁶ veritates immobilitatem suscipiunt. 3°. patet idem ex hoc quod illa prima natura est in fine perfeccionis possibilis, quia aliter non esset summe perfecta; sed si posset moveri, posset perfici: ergo moveri non poterit. Si autem⁷ moveri posset,⁸ hoc foret potissime obiective: sed eternaliter ordinat omnia, cum non capit suam speculacionem aut⁹ praxim a rebus extra: ergo non movetur¹⁰ a suis effectibus obiective; et multo minus localiter,¹¹ augmentative, vel alterative: aliter enim esset in eo¹² passiva potencia ante actum mixta cum potencia activa, cum aliud sit posse movere et aliud posse moveri: et sic varie posset¹³ perfici et imperfici, quod non competit summe bono. Supposito ergo, quod sit aliqua res et aliquid omnino immobile; consequenter dicendum est quod necesse est quidquid, quod poterit¹⁴ esse,¹⁴ esse mobile. Patet sic. Non est possibile aliquid esse nisi illud sit¹⁵ essencia creata [p. 107] vel essencia¹ increata; omnis essencia creata est mobilis; omnis essencia increata est mobile: ergo conclusio. Minor patet ex hoc quod essencia increata est suppositum mobile:² ergo illa est mobile: consequencia patet, quia ipsa est res mobilis³ eo quod est persona Verbi, que moveri poterit, et nedum hoc, sed habet naturam sibi⁴ unitam secundum quam moveri sufficit.

[ENGLISH]

## ¶3 · 107.8–108.21

> [p. 107] Et sic intelligo illud⁵ Sapiencie 7°, ‘omnibus mobilibus est mobilior sapiencia’: quod dictum, ut michi videtur, potest catholice intelligi et vere ad litteram de Sapiencia eterna⁶ suo tempore incarnata; que, cum attrita⁷ sit secundum humanitatem assumptam propter scelera nostra, bonificans et vivificans omnia ultra hoc quod sufficeret vel⁸ poterit⁸ alia creatura, habuit nimirum mocionem fontalem, qua principiat quasi vita omnem mocionem mundi sensibilis et cuiuslibet sue partis. Sicut ergo Aristoteles 8° Physicorum: ‘Ymaginatur motum primi mobilis esse quasi vitam viventibus cum mediante⁹ illo influitur perfeccio mundo supposito’; sic verissime sine ficticia illa Sapiencia est primum mobile efficacia et dignitate secundum assumptum hominem, mediante cuius motu primo omnium¹⁰ totus mundus ante et post perficitur; cum quelibet alia creatura per Christi passionem ad perfeccionem primariam,¹¹ qua Deo serviret placato¹² et¹² homini, instauratur. Non quod propter devocionem finguntur falsa; sed quod verissime de¹³ vi sermonis secundum seriem verborum primum¹³ mobile sit sapiencia increata; et quod eius motus vel passio perficit *[hominem] plus quam motus celi¹⁴ quamlibet creaturam¹⁵ [aliam] post vel ante. Nam¹⁶ quelibet creatura [p. 108] citra hominem debet ex institucione primaria servire homini; et sic peccato primi hominis, a quo hodie¹ redundanter² haberet perfeccionem ipso stante in originali iusticia, quodammodo peioratur. Cum ergo, per passionem et per consequens per mocionem huius Sapiencie, facta plena satisfaccione,³ sit natura humana gloriosius restituta; patet quod⁴ ista passio rectificat omnem operacionem nature, que humano generi est subiecta: et cum omnis⁵ servitus post et ante facta humano generi, non interveniente ista redempcione, foret quodammodo cassata, patet quod compendiosius motu celi vivificat⁶ preterita⁶ et futura: et cum exinde dolus et peccatum demonum mitigatur, lectum⁷ angelorum consorcium augmentatur, patet quod ultra possibilitatem motus celi spiritualem bonificat creaturam. Nec mirum; quia motor⁸ intrinsecus huius⁹ motus fuit non intelligencia, motrix orbis, sed spiritus¹⁰ preciosissimus¹⁰ Filii hominis et Dei Filii naturalis, qui est ‘tanto melior angelis effectus, quanto differencius pre illis nomen hereditavit;’ ut dicit Apostolus ad Hebre. primo ca°, quando dicit quod ‘Deus proposuit instaurare in Christo omnia, que in celis et que in terra sunt’; ut exponit Gregorius 31° Moralium ca° 38.

[ENGLISH]

## ¶4 · 108.22–109.20

> [p. 108] Sic ergo intelligendo per Sapienciam personaliter Verbum Dei, ut docent Augustinus et Ieronimus,¹¹ concedendum est quod ipsa sit summe mobilis; ymo plus attendendo ad litteram concedi potest quod dicta Sapiencia nedum fuit plus mobilis, sed plus effectualiter movebatur quam alia creatura quoad velocitatem, quoad compendiositatem, et quoad generalitatem. Quoad velocitatem, quia pro instanti sue generacionis plena carismatum; post verisimiliter in sua ascensione movebatur recte tam velociter ut primum mobile circulariter,¹² vel ut est possibile quod aliquid moveatur, quia causa tardacionis post¹³ discipulorum intuitum non est [p. 109] faciliter fingenda: Christus ergo ex se ascendendo a limbo ad celum ultimum pertransiit velocissime longissimum spacium transmeabile. Quoad compendiositatem patet quod eius brevis passio reduxit totum mundum post et ante ad maius temperamentum quam motus perpetuus primi mobilis suffecisset: prima enim secundum Aristotelem sunt quantitate minima. Quoad generalitatem patet, cum Christus sit creatura corporea et creatura incorporea, quarum utraque¹ multipliciter movebatur, quod sit ceteris plus mobilis: movebatur quidem² generacione et morte, augmentacione et alteracione, et demum motu locali multiplici super terram, aquam, et aerem³ pulsione, traccione, veccione et vertigine, ut actu illo imperfecto reduceret suos ad quietem perpetuam. Unde sicut naturalis philosophus commendat motum tanquam signum efficax nedum ad philosophandum sed ad intentum nature perficiendum, sic nimirum commendat theologus voluntariam passionem. Et constat⁴ ex 3° Physicorum quod passio vel est motus vel accidens multum cognatum motui. Sic ergo verissime de virtute sermonis dicitur ‘Sapiencia’ Dei Patris ‘omnibus aliis creaturis mobilior.’

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 109: *multiplici* (bt truncated: print multiplici) [AGREE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference Heb. i. (108.18); reference Eph. i. io. (108.20); reference 30 Heb- xiii- 8- (109.30).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 105:
1 disparate *om.* A B C.
2–2 ad consequentes C; ad comunes *sic* O.
3 est mobilis *om.* O.
4 arguitur *om.* C O.
5–5 sed . . . immobilis *om.* O.
6 omnis *om.* O.
7 immobilis O.
8 sit *om.* B.
9 ems O.
10 desinibilis A B C.

p. 106:
1–1 universitas . . . immoto *om.* A B C. 2–2 sic C. 3 secundum *om.* C.
4–4 principalis A B C. 5 etc. *om.* A B C. 6 et *om.* O.
7 enim A B C. 8 potest A; poterit O. 9 aut *om.* O.
10 moveri; *add.* potest *in marg.* A. 11 locatur O. 12 ea B.
13 potest A B C. 14–14 fuerit O. 15 sicud C.

p. 107:
1 essencia om. A B C.
2 mobile om. A B C.
3 mobilis om. A B C.
4 sibi om. A B C .
5 illud om. O.
6 eterna om. O.
7 att¹tᵃ O.
8 hec (poterit om.) A B ; hec poterit C.
9 meᵗᵉ A B C.
10 omni A B C.
11 pristinam A; p̃riam (i.e. primariam) C O.
12 et placito A B C; placato (et om.) O.
13 de vi sermonis aut secundum seriem (in rasura) verborum (debetur in margine) primum A; sermonis sed causacionem verborum primum B. Cod. O om. vi: cetera cum cod. C ut supra in textu habet.
14 ceⁱ (forsitan pro ceteri) O: at cf. p. 108, l. 11–14.
15 aliam add. O; forsitan retinendum, et hominem post perficit addendum.
16 nam om. O.

p. 108:
1 hodie om. C O.
2 redundancia O.
3 satisfaccio A B C.
4 quod om. C.
5 omnia O.
6 unificat preterit O.
7 letum (i.e. laetum) A B C.
8 mo^r motor sic O.
9 cuius A B C.
10–10 species preciosissima A B; species preciosissime C.
11 Iohannes O.
12 circulatur O.
13 post om. O.

p. 109:
1 tam add. A B; cod. O add. t͡a forsitan pro c^a (creatura).
2 quadam A B.
3 et aerem om. O.
4 patet B.
5 a^or A B C.
6 qm̃ A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 105: \_Declarando Christi mobilitatem explanat sensum | scnpture multis ammguum. quomodo sapiencia summe | mobilis sit habitu inventa ut homo. | The sense in whicli Christ is subject to change | is defined by discussing | ' Wisdom is more moving | than any motion,' and | * found in fashion | as a man.'^
p. 107: ceteia cum cod. | ut supra in textu habet. | (forsitan pro
```

---

## Chunk 07-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-07-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-07-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "109.21–113.29"
divisions: "cap. 7 (heading 'Cap. VII.' at 105.0); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1153 words; 1148 confirmed by Fordham or the vote; 4 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n148–n152 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 7, part 2: [TITLE]

## ¶1 · 109.21–110.17

> [p. 109] Sed obicitur contra hunc sensum per hoc, quod Christus non est ante incarnacionem; et per consequens scriba huius scripture non intendebat ad litteram mobilitatem Sapiencie incarnate. Hinc dicitur quod, quidquid fuerit de consequente, consequencia non valet; quia, cum apud Deum omnia que fuerunt sunt presencia, certum est quod auctor⁵ huius scripture satis cognovit quomodo⁶ ‘Christus maneat in eternum’ iuxta illam vocem vasis eleccionis sue ad Hebre. 13°. ‘Iesus Christus hodie et cras ipse et in secula.’ Et illud egregie declarat Ieronimus in Epist. De Assumpcione Beate Virginis ad Paulam et Eustochium: ‘Christi quidem incarnacionem, hoc est quod Christus suo tempore incarnatur, cognovit patriarcha Abraham iuxta testimonium Veritatis Ioh. 8°. ‘Abraham pater vester exultavit ut videret diem [p. 110] meum,” id est, tempus incarnacionis et non solum diem eternitatis; “vidit et gavisus est.”’ Cui Augustinus Ome. 43 adicit argumentum. ‘Quando, inquit, Abraham, Gen. 24°., misit servum suum, ut peteret uxorem filio suo Ysaac, hoc eum iuramento obstrinxit, ut fideliter quod iubebatur impleret. Magna enim res agebatur, quando Abrahe semini coniugium querebatur. Sed, ut hoc cognosceret servus quod noverat Abraham, quod nepotes non carnaliter affectabat, nec de suo genere carnale aliquid sapiebat; ait servo quem mittebat: “pone manum sub femore meo et iura per Deum celi.” Quid, inquit, sibi vult “Deus celi” ad femur Abrahe?’ Et respondet. ‘Cum per femur genus notatur, illa iuracione signabatur de genere Abrahe venturum in carne Deum celi. Stulti, inquit, reprehendunt prophetam Abraham tamquam pure puerile gesserit in hoc dicto; sed cum credidit benediccionem sui seminis Messiam credidit de suo semine incarnandum.’

[ENGLISH]

## ¶2 · 110.18–110.26

> [p. 110] Et idem 2°. declarat Ieronimus de prophetia¹ patriarche Ysaac sencientis Christum odore prophetico, Gen. 27. quando dixit, ‘Ecce odor filii mei sicut odor agri pleni, quem benedixit Dominus.’ Et ita de singulis patriarchis. Cum enim ipsi eadem fide salvati sunt nobiscum, patet quod ipsi crediderunt incarnacionem Domini sicut et nos; et per consequens Dominum suo tempore incarnari. ‘Constat, inquit² Ieronimus, tempus non preiudicasse³ sacramento uniti hominis ac Dei.’

[ENGLISH]

## ¶3 · 110.27–111.25

> [p. 110] Et patet ad obiectus garulos sophistarum, quibus invehunt contra oraciones ecclesie quibus rogat⁴ Dominum⁴ ‘per⁵ incarnacionem, nativitatem, circumcisionem, baptismum, ieiunium, passionem, mortem, resurreccionem et ascensionem a periculis liberari’; ‘Inanis, inquiunt, est oracio suggesta, cum omnia predicta nec sunt nec possunt esse.’ Sed constat quod unumquodque illorum, cum sit nobis preteritum, et futurum suo tempore patribus veteris testamenti, [quod]⁶ [p. 111] vere est pro suo tempore et per consequens causa misericordiam impetrandi: non quod quidquam scrupulosum¹ in nostra lege celamus,² quod non audeamus disputacioni cuiuscunque philosophantis ostendere. Et illum modum loquendi docet Ieronimus ex illo dicto Iude. ‘Iesus, inquit, populum ex Egipto salvans secundo eos, qui non crediderunt, perdidit:’ et Apostolus 1ª ad Cor. 10°: ‘neque temptemus Christum sicut quidam eorum temptaverunt;’ non quod iam esset Iesus Christus natus ex Maria virgine, sed quia illa illa persona, que tempore suo est Christus, est eterna et sempiterno³ Dei consilio incarnata et⁴ materialis essencia semper presto. Sic ergo⁵ sancti patres, in quocunque tempore fuerunt,⁶ sciverunt vere Christum esse, fuisse, et fore; et⁷ proposiciones formate ab eis fuissent vere— Christus est, fuit, vel erit incarnatus—quamvis tunc non fuisset ita⁸ quod Christus est incarnatus. Nam, ut sepe dixi, sicut proposicio potest esse hic vera cum hoc, quod hic non sit suum primarie significatum, sed satis est quod ipsum sit alicubi⁹: correspondenter proposicio potest esse nunc vera cum hoc, quod nunc non sit suum primarie signatum, sed satis est quod ipsum sit aliquando. Et sic intelligendus est Augustinus cum aliis doctoribus quod eadem est fides patrum tam novi quam veteris testamenti. Nam incarnacio, mors Christi, et adventus ad iudicium sunt fides credita, a qua fide absit falsitas, sive ficticia etc.

[ENGLISH]

## ¶4 · 111.26–112.19

> [p. 111] Unde Gregorius 23° Moralium ca°. 15¹⁰ exponens illud¹¹ Iob. 33°, ‘semel loquetur Deus, et secundo ad¹² ipsum non repetet,’ ita scribit: ‘In Deo ideo dicere quodlibet tempus audacter, licet quod in eo nullum proprie dici¹³ licet.’ Unde¹⁴ notat¹⁴ causam eius 30°. Moralium ca°. 5° dicens quod Deus preteritorum¹⁵ non reminiscitur, cum ipsa que in semetipsis¹⁶ [p. 112] pretereunt eius¹ intuitu semper presencia assistunt: et exemplificat satis notabiliter 34°. Moralium ca°. 5°. tripliciter: unde 9°. Moralium 25 expresserat illud diffusius exponens illud Iob. 10. ‘Numquid sicut dies hominis, dies tui?’ ‘Deo, inquit, nec transacta pretereunt, nec adhuc ventura, que non apparent, desunt; quia is, qui² semper esse habet cuncta sibi presencia, conspicit.’ Et idem dicit Anselmus Monologion 19°. Ideo, ut sepe dixi, nisi omne tempus preteritum vel futurum fuerit Deo presens, paterentur theologi magnas angustias in exposicione³ scripturarum ut Ps. 21°. tempore David dicit dicta Sapiencia: ‘foderunt⁴ manus meas et pedes meos:’ et sic de multis scripturis, que pueriliter essent sine racione posite⁵ sub ita disparatis temporibus nisi ad imprimendum in⁶ nobis quod immensa Dei eternitas coassistit omni tempori preterito et⁷ futuro. Unde ad istum sensum loquitur sapiencia Ecclesiastici 47°: ‘Christus purgavit⁸ peccata ipsius.’ Et patet quod facta instancia non impugnat sensum datum ad istam scripturam, ‘omnibus mobilior est Sapiencia.’

[ENGLISH]

## ¶5 · 112.20–112.32

> [p. 112] Sunt autem multi alii sensus huic littere adaptati.⁹ Ut hi dicunt quod extensive loquendo de motu Sapiencia increata movetur obiective a cognitis terminantibus eius actum. Hi dicunt cum tot sint motus genera quot et entes,¹⁰ et Deus ad omnem punctum mundi continue adquirit dominia, est in illa manerie motus relacionis ‘summe mobilis.’ Tercii autem dicunt quod in omni motu est dare ordinem prioritatis et posterioritatis¹¹ secundum successivam denominacionem¹² subiecti in materia motus, et omne tale secundum esse intelligibile ordinatum et descriptum¹³ est eternaliter in Sapiencia increata, et secundum illas raciones dicitur figurative ‘summe mobilis.’ Sed prior exposicio, cum sit literalior de virtute sermonis, verior, et fidei conformior, plus placeret.

[ENGLISH]

## ¶6 · 113.1–113.29

> [p. 113] Unde quamvis auctor scripture intenderit omnes istos sensus, primum tamen principalius, ut sit introitus ad alios consequentes. Et sic Augustinus de virtute sermonis salvat textus scripture plus imbrigabiles ut illud Ioh. 14,¹ ‘Sermonem quem audistis non est meus, sed eius, qui misit me, Patris.’ Dicit enim illud Ome. 76ᵃ. esse verum de virtute sermonis: ‘non, inquit, miremur, non paveamus:² non est minor Patre, vel impar sibi: non enim mentitus est; “qui me non diligit, sermones meos³ non servat:” non est hic sibi contrarius, sed forte non⁴ sine misterio ibi dixit pluraliter, hic singulariter; volens hic intelligere semetipsum, qui, cum sit Sermo vel Verbum Dei Patris non autem Sermo sui ipsius, verum dixit ad litteram.’ Quod si grammaticus ex accusativo casu offenditur, potest dici quod facta construccione recta non sit⁵ anthitesis. Nam qui non diligit Christum, non servat sermones suos, id est,⁶ sentencias vel veritates, quas precepit observari. Sed ut manifestet quid ex hoc sequitur, subiungit ‘et sermonem quem audistis’ (supple⁷ ‘non servat’); per quam copulacionem docemur methaphisicam quod omnes huiusmodi veritates eterne sunt idem essencialiter Verbo Dei. Et 3°, ut doceat quod ille Sermo sit idem essencialiter Deo Patri, licet personaliter⁸ distinguatur, subiungit ‘non est meus sed eius, qui misit me, Patris.’ Licet autem sensus catholicus posset esse quod sermo vocalis non sit Verbi ex se, modo quo Apostolus dicit solum Patrem habere immortalitatem;⁹ ut exponit Augustinus primo De Trinitate et primo contra Maximinianum caᵒ. 10; tamen¹⁰ prior sensus est subtilior et mihi¹¹ carior.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 110: *carne* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 30 Heb- xiii- 8- (109.30); reference Jude;s. (111.5); reference l Cor. x. 9. (111.7); reference Job xxxiii. 14. (111.27); reference Jobx. (112.4); reference Ps. xxii. 16. (112.11); reference ; as aiso John xiv. 24. 1 1 ° in (113.4); reference l Tim. vi. 16. (113.26).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 109:
1 tam add. A B; cod. O add. t͡a forsitan pro c^a (creatura).
2 quadam A B.
3 et aerem om. O.
4 patet B.
5 a^or A B C.
6 qm̃ A B C.

p. 110:
1 philosophia A B C.
2 inquit *om.* B.
3 predicasse O.
4 orat deum A B C.
5 pro O.
6 *An* quod *sensus causa omittendum*?

CHECK: the main text has figure 4 twice (both "quibus ⁴" and "Dominum ⁴"), but the foot has only one entry for 4 ("orat deum A B C.").

p. 111:
1 scrupulos-(is in rasura) A; scrupulos B C.
2 colamus A B C.
3 semper in O; semper consilio (sic) C.
4 et om. O.
5 sibi O.
6 fuerint O.
7 per add. O.
8 ita om. A B.
9 aliquando A B C.
10 ca°. 3 A B C.
11 idem O.
12 ad om. A B C.
13 dici om. A B C.
14_14 unam vocat O.
15 preterito O.
16 ipsis om. A B C.

p. 112:
1 eius om. O.
2 his que O.
3 exposicionibus O M.
4 fodiunt O.
5 posita C O.
6 in om. A B C.
7 vel O.
8 pugnavit O.
9 dapnâti O.
10 entis A B C.
11 et posterioritatis om. A B C.
12 denotacionem O.
13 discriptum O.

p. 113:
1 numerum om. A B C; 10 O M.
2 paciemus O.
3 sermonem meum A B.
4 non om. O.
5 fit O
6 id est om. O.
7 supplendum B C; non om. C.
8 pater O.
9 immortalem O.
10 cum A B.
11 inde A B.
12 Christus om. O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 113: he emptied him- | seif, taking the
```

---

## Chunk 07-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-07-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-07-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "113.30–117.27"
divisions: "cap. 7 (heading 'Cap. VII.' at 105.0); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1029 words; 1016 confirmed by Fordham or the vote; 12 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n152–n156 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 7, part 3: [TITLE]

## ¶1 · 113.30–115.21

> [p. 113] Et sic intelligendus est sensus Apostoli ad Philipp. 2°. quod Christus,¹² ‘cum in forma Dei esset, non rapinam arbitratus est esse se equalem Deo; sed semetipsum exinanivit formam servi accipiens.’ Pro cuius intellectu notandum quod sicut forma [p. 114] Dei est deitas,¹ sic forma hominis est humanitas. Utraque enim est forma substancialis; cum quelibet persona divina sit illud quo² est Deus,³ quia Deus formaliter deitate;¹ sicut quelibet persona hominis est illud quo² est homo, quia⁴ est homo⁴ formaliter humanitate. Utramque autem harum formarum habet ut subiectus eis formaliter; unam tamen habet absolute necessario; et aliam accepit⁵ ex tempore. Et istam altissimam methaphisicam de formis vellem nostros theologos, etsi non in⁶ methaphisica Aristotelis, saltem in verbis Apostoli compendiose addiscere. Ex quo patet, quod non ex propria reputacione vel arbitrio proprio sine veritate substrata vendicavit se esse equalem Patri, quasi⁷ raperet sibi honorem Patri debitum, ut facit Sathanas; cum naturaliter et communiter inest sibi cum Patre et Spiritu Sancto⁸ esse Deum. Quod co-inest⁹ sibi et Patri, ostenderat quando¹⁰ dixit,¹⁰ ‘Ego et Pater unum sumus.’ Augustinus autem format talem racionem; ‘Nichil quod est naturale¹¹ et essenciale¹¹ supposito est rapina: sed¹² Christum esse equalem Deo est naturale et per se inest Verbo: ergo hoc non est rapina.¹² Sed faciendo se esse naturam visibilem exinanivit misericorditer semetipsum: semetipsum dicit¹³ propter ydemptitatem persone que est filius hominis¹⁴ et Dei Filius:¹⁴ exinanivit dicit,¹⁵ quia fecit se ad¹⁶ extra esse naturam corpoream, que,¹⁷ [cum] in mundi principio prius originem¹⁷ quam formam habeat, est inanis.’ Ad quem sensum, ut exponit Augustinus 12°. Confessionum, scriptura in principio Gen. dicit, ‘terra erat inanis et vacua.’ Nec video quomodo exinanicio¹⁸ pocius¹⁹ possit intelligi quam quod sit²⁰ res extra facta inanis²¹ essencialiter sic ut sit²¹ exinanita. Et hoc est verum de Christo ad litteram, cum sit trium naturarum [p. 115] quelibet. Et hinc vere dicit Veritas, Ioh. 14°. ‘Pater maior me est:’ quia, cum¹ Christus sit tam equivoce divinitas et humanitas, potest respectu predicati absoluti intelligi secundum racionem divinitatis vel secundum racionem humanitatis, sicut exigit predicatum. Et patet ex dictis superius quod non est repugnancia—Pater est maior Christo—et—idem² Pater est³ simpliciter equalis Christo—: ymo, intelligendo personam Christi secundum duas naturas equivoce, non est repugnancia inter ista—Pater est maior Christo—⁴ et—idem Pater non est maior Christo—⁴: nec debent tales predicaciones abici de virtute sermonis quod sunt figurative, quia per idem⁵ negaretur hoc—Ego et Pater unum sumus—Pater et Filius et Spiritus Sanctus sunt unus Deus, etc :—cum in prima sit equivocacio, et in secunda concepcio personarum. Ymo, si non fallor, omnis locucio nostra de Deo est figurativa, ut quandocunque dicitur quod Deus est mobilis, natus, passus etc. est construccio non synecdochica sed figura que antropospatos dicitur, quando scilicet humana passio Deo attribuitur; ab antropos homo et patos passio. Non enim habemus nomina, que sine figura Deum signent.

[ENGLISH]

## ¶2 · 115.22–116.5

> [p. 115] Redeundo ergo ad propositum conceditur quod aliqua res, quia natura divina, est omnino immobilis, sic quod nullo modo moveri poterit, licet sit suppositum mobile, ut puta, Christus passus. Patet ista logica in exemplo. Nam natura divina est Verbum tam eternaliter quam temporaliter genitum, et tamen ipsa non est genita, et talis⁶ essencia materie prime est suppositum ignis compositum ex materia et forma: et tamen ipsa materia non potest sic componi. Petrus comedit, moritur, vel aliter transmutatur; et tamen natura specifica, que est Petrus, non potest taliter transmutari. Ideo in omnibus istis similibus oportet diligenter attendere ad predicacionem secundum essenciam et formalem. Et patet quod non sequitur—Deus est mobilis,⁷ et omne aliud [p. 116] a Deo est mobile: ergo omnis res est mobilis—quia aliqua res non est mobilis. Et si queratur—Quid non est mobile ?—potest dici equivocando, quod nichil non est mobile, quia natura divina est mobile: et sic, intelligendo predicacionem secundum essenciam non formalem,¹ omne, quod² est, est mobile.²

[ENGLISH]

## ¶3 · 116.6–117.9

> [p. 116] Quod si dicatur istam responsionem, cum sapiat contradiccionem, interimere disputaciones theologicas, cum incidit in redargucionem, que est³ meta vilissima respondentis; dicitur quod multum proficeret modum disputandi sophisticum, principaliter propter apparenciam arguentis et redargucionem⁴ patulam respondentis, ex peccato Luciferi introductum, esse⁵ in scolis theologis pretermissum.⁶ In cuius signum prima questio, quam scriptura meminit,⁷ est a dyabolo⁸ introducta. ‘Cur,⁸ inquit serpens, precipit vobis Deus ut non comederetis de omni ligno paradisi?’ Gen. 3°. Unde omnis questio attestatur indubie super ignoranciam vel peccatum. Tamen non negandum est, quin questiones theologice possunt tractari meritorie, cum Veritas quesivit a peccatoribus plurimas questiones. Oportet tamen quod utrobique intendatur Dei gloria augmentanda, sophistarum superbia destruenda, et ignota veritas detegenda: omne⁹ autem quod amplius est in disputacione theologica ‘a malo est:’ ideo questio, sicut et iuramentum, occasione vel pena peccati introducta est. Et ista est sentencia Augustini 2° De Doctrina Christiana 31°, ubi docet in disputacionibus cavere rixandi libidinem et ostentacionem frivolam puerilem. Nec¹⁰ ducunt argucie sophistarum theologos¹¹ ad metam aliam, sed detegit eorum versuciam arundineam qua prius pompaverant; et hoc ex propriis eorum principiis. Unde frequenter, ut colores sapiencie sophistice minus appareant, obvio eis negando negativas, que ad sensum equivocum satis catholice concedi potuerunt¹²; ut, dando exclusivam huius [p. 117] universalis—omnis res est mobilis,—formo sic exclusivam, ut apparencia¹ sophistica sit minus evidens—tantum res mobilis est res—quod est falsum pro rebus eternis. Concedi tamen posset quod nichil aliud quam mobile est res, accipiendo ‘mobile’ essencialiter substantive; et tamen aliud quam mobile est res, posito quod ‘mobile’ predicetur formaliter adiective. Sed Augustinus et alii sancti non curarunt de istis apparenciis sophistarum. Unde in Dialogo ad Felicianum, ‘genuit, inquit, et non genuit Maria Filium Dei.’

[ENGLISH]

## ¶4 · 117.10–117.27

> [p. 117] Sed ulterius arguitur quod Verbum Dei non sit simpliciter mobile racione assumpti hominis. Nam nulla persona movetur propter habitum vel² accidens essencialiter separatum²: sed humanitas Christi est habitus Verbo Dei accidentaliter copulatus: ergo propter eius laceracionem³ vel passionem non sequitur⁴ passio Verbi Dei. Confirmatur triplici exemplo. Primo ex hoc quod homo non laceratur vel comburitur, etsi vestimenta eius taliter⁵ paciantur. 2°. ex hoc quod humanitas conceditur per tempus notabile non fuisse: quando tamen non conceditur Verbum Dei conformiter non fuisse, non ergo sequitur—si ista humanitas movebatur post a non esse acquirendo essendi terminum,⁶ tunc et Verbum—. 3°. confirmatur ex figura Abrahe patriarche, qui cum voluit Gen. 22°. immolare⁷ filium suum Ysaac, non hunc occidit sed arietem, quem vidit post tergum⁸ herentem⁸ cornibus. Cum ergo passio Christi fuit per Ysaac allegorice figurata, videtur quod non persona Christi, sed eius humanitas, fuit passa.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 115: *sumus—Pater* (print = bt (next line)) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference ; as aiso John xiv. 24. 1 1 ° in (113.4); reference l Tim. vi. 16. (113.26); reference John x. 30. (114.16); reference Gen. i. (114.27); reference 30 Petrus (115.29); reference Gen. iii. l. (116.15); reference Matth.v.37. (116.24); reference : 73b] Gen- xxii- 13- (117.26).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 113:
1 numerum om. A B C; 10 O M.
2 paciemus O.
3 sermonem meum A B.
4 non om. O.
5 fit O
6 id est om. O.
7 supplendum B C; non om. C.
8 pater O.
9 immortalem O.
10 cum A B.
11 inde A B.
12 Christus om. O.

p. 114:
1 divinitas; divinitate O.
2 quod O.
3 deus om. O.
4_4 quia . . . homo om. O.
5 accipit O.
6 in om. O.
7 qui A B.
8 sancto om. O.
9 commune A B C.
10_10 quando dixit om. A.
11_11 essenciale et essenciale C.
12_12 sed . . . rapina om. A B C.
13 semetipsum om. A B C; sȝ ipsum O.
14_14 hominis . . . filius om. A B C.
15 dicit om. A B C.
16 ad om. B.
17_17 origine C O; aut cum inserendum aut origine legendum.
18 inanicio A B C.
19 prius O.
20 sit om. O.
21_21 essencia sic et sic A B C.

p. 115:
1 cum *om.* B.
2 me B.
3 est *om.* A B.
4–4 et . . . Christo *om.* O.
5 perinde O.
6 et sic C ; etc O.
7 mobile O.

p. 116:
1 tunc add. A B C.
2-2 quod . . . mobile om. O; quod est mobile C.
3 est om. O.
4 responsionem B.
5 introductum esse om. B.
6 pretermissis C.
7 invenit O.
8-8 introductatur O.
9 omnis B.
10 nunc O.
11 theologum O.
12 poterunt O.

p. 117:
1 evidencia A B C.
2–2 vel . . . separatum *om.* O.
3 accionem M
4 est O.
5 tᵃolitꝛ (totaliter) O.
6 t'im A B C; tm̃ O.
7 ymolare A B C; īmolale O.
8–8 tergêtê herentê B.
9 ageretur C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 113: he emptied him- | seif, taking the
p. 115: s b ^PP 0Sltum m °-
```
