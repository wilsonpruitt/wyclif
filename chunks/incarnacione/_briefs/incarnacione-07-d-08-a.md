# Translation brief: incarnacione 07-d–08-a

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-07-d.md chunks/incarnacione/wyc-incarnacione-07-e.md chunks/incarnacione/wyc-incarnacione-08-a.md` once and fix what it reports.
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

## Glossary (the 297 rows these chunks use; the full file is GLOSSARY.md)

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
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides formata / informis | formed faith / unformed faith | Faith formed by charity. Pilot. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| membrum | member | The card's key ruling, now a row (with *caput*). Ruled 2026-10-02. |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| tercia pars ecclesie | the third part of the church | The commons (*Dial.* 85.15, 85.22). Ruled 2026-09-28 (coordinator, delegated). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| religio privata; secta | private religion; sect | His name for the religious orders. Keep "sect". |
| religiosi | the religious | Members of the orders. Ruled 2026-09-28 (8 sites). |
| possessionati | the possessioners | Endowed religious. |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| habitudo | CONTEXTUAL: condition / respect | "Condition": a person's present state, set against predestination (Richard of St Victor). *Habitudo ad*: "condition toward", a relation (180). Ruled 2026-10-02 (*Eccl.* 72.24). "Respect": the logical relation under which a predicate holds (*posiciones secundum habitudinem*), with a **C** note; ruled 2026-10-22 (Wilson; *Incarn.* 4.16). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
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
| argucie; argucia | stratagems, quibbles; a quibble | T. p. 367. |
| sophisma | sophism | A proposition that can apparently be proved and disproved (T. p. 360 n. 10). |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| philosophia sermocinalis / realis | the philosophy of language / the philosophy of reality | T. pp. 364–5. |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| confuse / confusus (*fides, noticia*) | indistinct(ly) | The scholastic *cognitio confusa*: known in the whole, not in its parts; never "confused". Ruled 2026-10-02 (42.19, 46.2, 46.6). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| vocatus (*vocata bona, vocata ecclesia*) | so-called | Ruled 2026-10-02 (55.6, 62.7). |
| digestio | digestion | The recurring figure of the four digestions (Rom. 8:30). Ruled 2026-10-02 (60.29 ff.). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| compossibilis | compossible | Ruled 2026-10-02 (271.13). |
| satispassio | satispassion | Set against *satisfaccio*. Ruled 2026-10-02 (270.11). |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| triduum (*in triduo*) | the three days | Death to resurrection, body in the tomb (Lombard, *Sent.* III d. 22). Ruled 2026-10-22 (Wilson; *Incarn.* prol). |
| ydemptitas specifica | identity of species | That Christ and other men are of one species. Not "specific identity" (reads as "particular"). Ruled 2026-10-22 (Wilson; *Incarn.* prol, 8). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter; so also *Sapiencia* where Wisdom is the Word in person (*Incarn.* 7, coordinator). Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". With the agent expressed (*homo assumptus a Verbo*) "the man assumed by the Word", which cannot be misread (coordinator, 2026-10-22). Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| sophistice | sophistically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 15). |
| de vi vocis / de vi sermonis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
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
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| passio (against *accio*) | being-acted-on | The category; G note at the first occurrence in a chunk. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 60.13). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| per se / per accidens | of itself / by accident | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 68–72). |
| locus a sufficienti similitudine / a divisione | the topic from sufficient likeness / from division | As *locus a simili*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| pretericio | being past | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| solvere / solucio (of the union) | loose / loosing | Except inside a Douay quotation (John 10:35 "cannot be broken"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ypostasis | hypostasis | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| medium (logical) | middle term | Of a syllogism; elsewhere "means" by context. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 5). |
| ydemptitas ypostatica | hypostatic identity | Beside *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 84.20). |
| passionatus | subject to passion | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 83). |
| eiusdem / consimilis / alterius racionis | of the same / like / another kind | The species-sense of *racio*; *racio speciei* "the account of the species" (Aristotle's *logos*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.4, 87.17). |
| principiari | be constituted from principles | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 85.7). |
| univocacio | univocation | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.27). |
| accidentatus | subject to accidents | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.4). |
| in recto / in obliquo | in the direct case / in an oblique case | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 88.25). |
| mobilis / mobilitas | movable / movability | Of Christ's humanity (ch. 7). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.11). |
| passibilis | passible | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.12). |
| conveniencia / convenire (*in*) | agreement / agree | The argument of 90–91 turns on it; not "fittingness" (that is *congruencia*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 90). |
| predicacio synecdochica | synecdochic predication | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.27). |
| humidum infantile / radicale | the moisture of infancy / radical moisture | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 94.9). |
| conversari | live one's life (among men) | Beside *conversacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 89.25). |
| esse intelligibile | intelligible being | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 99.23). |
| extraneare | estrange | *Affeccio extraneandi* "an affection of estrangement". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 98.16). |
| mobile (noun) / primum mobile | a movable / the first movable | Against the adjective *mobilis*; ch. 7 turns on it. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 107, 116). |
| res racionis | thing of reason | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| universitas creata | the created totality | Beside *universitas creaturarum*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 106). |
| significatum | significate | Kept apart from *signatum* "thing signified". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 111). |
| predicacio secundum essenciam / formalis | predication by essence / formal predication | Wyclif's modes of predication (cf. *predicacio secundum causam*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 115–116). |
| forma substancialis | substantial form | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| exclusiva | the exclusive [proposition] | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 116–117). |
| concepcio (figure) | conception | The grammatical figure. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| habitus (of the humanity) | habit | The Lombard's third opinion (*Sent.* III d. 6). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 7). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| philocaptus | besotted | "philo-captive" (T. p. 363) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| detegere | to expose | "wipe away" (T. p. 366) |
| disciplinabilis | teachable | "impressionable" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| precipui sacerdotes | leading priests | Kept apart from *principes sacerdotum*, "chief priests". Ruled 2026-09-28. |
| pietas / pie | piety / piously | Kept apart from *misericordia* "mercy". Ruled 2026-10-02 (*Eccl.* 12). |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| salvacio | salvation | Covers bodily and eternal; Wyclif pairs the senses. Ruled 2026-10-02 (*Eccl.* 15, 345.24–26). |
| virtus | power (faculty) / virtue (moral habit) | Split by sense. Ruled 2026-10-02 (*Eccl.* 15, 345). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| collacio | conferral | Of a gift or endowment; paired with *ablacio* "taking-away". Ruled 2026-10-02 (*Eccl.* 16, 385–386). |
| monstracio | muster | Ruled 2026-10-02 (*Eccl.* 16, 384.11). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| habitus fidei | habit of faith | Ruled 2026-10-02 (*Eccl.* 17, 407–408). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| proprietarius | proprietary | Ruled 2026-10-02 (*Eccl.* 18, 425.5, 427.15). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| quadriga diaboli | the devil's four-horse chariot | Ruled 2026-10-02 (*Eccl.* 18, 427.12). |
| equivoce | equivocally | Ruled 2026-10-02 (*Eccl.* 19, 444; as in 05-a, 06-b, 06-f). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| confundere (supposition) | make (a term) stand confusedly | The logic of supposition; distinct from the *confuse/confusus* "indistinct" row. Ruled 2026-10-02 (*Eccl.* 19, 463.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| sophista | sophist | Kept apart from *sophisma*. Ruled 2026-10-02 (*Eccl.* 21, 495.15). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| univoce | univocally | Ruled 2026-10-02 (*Eccl.* 21, 514.4). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
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
| potestas iurisdiccionis | power of jurisdiction | Paired with *potestas ordinis*. Ruled 2026-10-02 (*Eccl.* 23). |
| potestas | power | Always "power" (*De pot. pape*, Wilson 2026-10-07). Its kin by row: *potestas ordinis*, *iurisdiccionis*, *iudiciaria*. |
| Ardmacanus; dominus Ardmacanus | Armachanus; the lord of Armagh | Richard FitzRalph. The bare name stays "Armachanus" (as in *De ecclesia*); with *dominus* "the lord of Armagh" (card). Ruled 2026-10-07. |
| conficere | to consecrate (the eucharist) | Of the priest at the altar; otherwise "to make up, compose". Ruled 2026-10-07 (*Pot. pape* 11.20). |
| licencia | licence | Permission granted; never "power". Wyclif usually sets it against *potestas*, but can also identify the two where power is defined as a grant (*illa licencia est potestas*, *Pot. pape* 21.29): render "licence" either way and let the argument show which. Ruled 2026-10-07 (*Pot. pape* 41.21); qualified 2026-10-12 (close-out R1).|
| primatus | primacy | Peter's and the pope's; *preeminencia* stays "preeminence". Ruled 2026-10-07 (*Pot. pape* ch. 3). |
| auctoritas | authority | Ruled 2026-10-07 (*Pot. pape* 63.16). |
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| auctoritativus, autoritativus | authoritative | Beside *auctoritas* "authority". Ruled 2026-10-07 (*Pot. pape* 76–78). |
| decretiste | decretists | The commentators on Gratian. Ruled 2026-10-07 (*Pot. pape* 81.27). |
| religiositas | religiousness | Ruled 2026-10-07 (*Pot. pape* 86.21). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| correpcio fraterna | fraternal correction | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-i). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| claves potestatis / auctoritatis (sciencie) | keys of power / of authority (of knowledge) | The pair kept fixed. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 141.18). |
| propriacio | owning | The opposite of *expropriacio*; kept apart from *appropriacio* "appropriation". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 161.24). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| sessiva / sesina | seisin | *Sesina* the spelling at *Incarn.* 33. So the manuscripts (Loserth 170.8, *ita cod.*); feudal possession that perfects a title. Ruled 2026-10-08 (coordinator, delegated). |
| quaternarius / denarius / quadragenarius | the four / the ten / the forty | Number exegesis (the 153 fishes, ch. 7). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 154–155). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| replicatur; replicatum | it is rejoined; rejoinder | A further objection against an answer; kept apart from *respondetur* "the reply is" (so 04-b). Ruled 2026-10-08 (coordinator, delegated; conformed 10-e, 10-g). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| equivocacio | equivocation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.1). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| questores | questors | Kept apart from *perdoniste* "pardoners". Ruled 2026-10-02 (*Eccl.* 23, 584). |
| correptibilis | open to reproof | Beside *corripere* "reprove". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 301.3). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| sophisticacio | sophistry | Noun beside *sophisticare*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 337.25). |
| evangelizans | preacher of the gospel | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-g). |
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
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 07-d: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-07-d.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-07-d
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "117.28–121.7"
divisions: "cap. 7 (heading 'Cap. VII.' at 105.0); part 4 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "870 words; 870 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n156–n160 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 7, part 4: [TITLE]

## ¶1 · 117.28–118.8

> [p. 117] Hic dicitur quod non esset concedendum Verbum pati propter passionem sue humanitatis, nisi Verbum esset personaliter illa humanitas. Sed quia Verbum ex integro est illa humanitas tam secundum corpus quam secundum animam, et acciones ac passiones sunt primo suppositorum; patet quod illa humanitas non pateretur vel ageret,⁹ nisi [p. 118] quia Verbum, quod est eadem ypostasis vel persona, sic agit vel patitur. Firmiter itaque est tenendum quod Verbum Dei et per consequens Deus ipse pendebat dolens et passus in cruce, et sic de ceteris humanis actibus quos evangelium de Iesu prosequitur. Et sic, licet humanitas Christi sit essencia, substancia, vel natura separata non conservative sed essencialiter a deitate, que Christus est; non tamen sic separatur quin sit persona Christi.

[ENGLISH]

## ¶2 · 118.9–118.30

> [p. 118] Sed pro nomine ‘habitus’ est notandum quod ‘habitus’ quadrupliciter sumitur, ut exponit Augustinus 83 Questionum Questione 73ᵃ. exponendo illud Apostoli ad Philipp. 2°. ‘habitu inventus est ut homo.’ Primo pro sapiencia, que est veritas, quam addiscimus, que manens¹ non mota movet animam, quam informat. 2°. pro alimentis habitis mutantibus corpus, quod nutriunt, et digestione mutatis. Omne quidem substanciale nobis adiacens, quod mutat et mutatur adiacendo subiecto, dicitur ‘habitus’ huiusmodi²: ‘habitus’² quidem, quia denominat subiectum habere quod sibi accidentaliter adiacet. 3ᵐ. genus est quando habituata formantur a subiectis habituatis³ †perfeccius quam quando membris aptata induuntur.†³ 4ᵐ. genus habitus, ut anulus in digito. Omnia autem hec quatuor, cum⁴ denominant substanciam habituari vel habere, dicuntur in predicacione secundum essenciam esse⁵ ‘habitus;’ ut ‘motus’ dicitur materialiter esse res, que est motu dicto formaliter acquisita, ut patet 3°. Physicorum 9°· 4°. Sumitur autem sufficiencia illorum quatuor penes hoc, quod primus habitus mutat substanciam cui advenit et⁶ non mutatur; secundus⁷ mutat et mutatur⁷; tercius mutatur et non mutat; quartus nec mutat necessario nec mutatur.

[ENGLISH]

## ¶3 · 118.31–119.10

> [p. 118] Sed preter hec quatuor, que⁸ in se sunt⁸ substancie, sumitur habitus apud philosophos formaliter ad duos⁹ sensus [p. 119] equivocos. Primo pro qualitate preternaturali¹ de prima specie qualitatis; sive² sit² corporis habitus, ut sanitas; sive habitus anime, ut virtus intellectualis aut moralis³; habitus autem spiritualis ex habitu primo modo dicto³ materialiter generatur, sicut⁴ habitus corporalis efficitur ex secundo. Sed secundo modo sumitur habitus pro forma respectiva de 10°. genere, quod est habere, possessio, vel habicio, et talis habitus causatur ab habitu tercio et quarto modis materialiter intellectis: ‘divicie’ enim denominant homines divites,⁵ possessionatos, vel habentes formaliter.

[ENGLISH]

## ¶4 · 119.11–119.27

> [p. 119] Et patet quod ille sex maneries habitus sunt satis equivoce. Dicitur ergo quod humanitas assumpta a Verbo est habitus tercii modi, cum accidit enti in actu, non mutans vel faciens ipsam aliam personam quam prefuit. Ideo dicunt sancti quod humanitas est quasi vestis detegens deitatem;⁶ et religiosi, qui Christum induunt, habent habitus⁷ corporis; hoc notantes, quod⁸ accidit Deo humanitas, sed non⁹ inseparabiliter. Ideo dicit Augustinus in Dialogo ad Felicianum quod humanitas est accidens Verbo, non quod sit res inherens ut accidencia novem generum, cum sit precipua creata substancia; nec quod sit coëva Verbo vel sicut passio naturaliter consequens¹⁰ ad subiectum; sed contingenter ex tempore nobis ineffabiliter¹¹ inest Verbo non mutando naturam, cui advenit, sed formata¹² mirabiliter, quia Verbo Dei ydemptificata vel ypostatice copulata: cum secundum Augustinum primo De Trinitate, ‘talis fuit unio¹³ incarnacionis, que Deum faceret¹⁴ hominem et hominem Deum.’

[ENGLISH]

## ¶5 · 119.28–120.18

> [p. 119] Et patet quod dicta humanitas est forma in tribus conveniens cum formis per se in genere accidentis. Primo in hoc quod presupponit naturam, cui contingenter advenit, longe priorem ipsa naturaliter, quam accidens presupponit creatam substanciam, quam informat. 2°. in hoc quod non facit [p. 120] naturam, cui advenit, esse¹ quid vel aliud² quam absolute necessario semper erat.³ Et 3°. quod non potest esse sine supposito Verbi Dei, cui inseparabiliter sed contingenter adheret. Et constat quod proprietates proporcionales analogice conveniunt generi accidentis: assimilatur autem passionibus, que dicuntur per se egredi de propriis principiis⁴ subiectorum; cum non potest abesse, postquam infuit, cum inseparabiliter consequitur⁵ ad Verbum, sicut passio ad subiectum; sed, sicut accidentia separabilia, deesse poterit a subiecto. Convenit 2°. cum accidentibus absolutis per se in genere, cum sit per se substancia motiva et mobilis denominans subiectum proprie et per se moveri formaliter. 3°. convenit⁶ cum accidentibus respectivis. Nam, sicut relaciones, habitaciones, et respectus consimiles non exinde movent naturam, cui inherenter adveniunt; sic indubie ‘forma servi,’ que est humanitas, non potest movere naturam divinam, cum deitas solum denominacione respectiva denominatur ex eius adiacencia summe mirabili.⁷

[ENGLISH]

## ¶6 · 120.19–121.7

> [p. 120] Convenit autem cum ceteris formis substancialibus⁸ in his tribus. Primo quod facit suppositum, cui advenit, esse aliud quam prefuit; quia, postquam Verbum fuit pure deitas, nunc est homo. 2°. in hoc quod est idem ypostatice cum subiecto, cui advenit. Sicut generaliter omnis forma substancialis est idem essencialiter vel personaliter⁹ cum subiecto forme et composito ex eisdem; sic, inquam, ista humanitas; cum sit eiusdem racionis cum aliis et idem personaliter Verbo Dei, licet Verbum commune sit natura divina, que non potest esse illa humanitas; sed cum sit individuum humane nature homo Iesus Christus, suscipit saltem in predicacione et secundum essenciam predicata temporalia, que historia evangelica de Christo contexuit, ut post declarabitur. Et patet mira subtilitas in verbis Apostoli quando dicit ‘habitu inventus ut homo’: non enim video alium terminum, quo [p. 121] posset apcius quoad auditorii intelleccionem, copiosius quoad philosophicam consideracionem, aut expressius quoad fidei explanacionem, humanitatem Christi exprimere. Ideo respectu¹ sentencie Apostoli, qui fuit prudentissimus predicator, et Augustini sui discipuli, qui fuit scripture sacre subtilissimus explanator, oportet nos ignaros colla mentis submittere.

[ENGLISH]

## Notes

## Transcription notes

- **Omitted per §3.5 / kept in the English** (margin matter): reference : 73b] Gen- xxii- 13- (117.26); reference Augustinum (119.29).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
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

p. 118:
1 movens A B C.
2-2 huiusmodi habitus om. O.
3-3 habituatis quam quando membrum aptata induitur A B C; habituatis proficitur quam quando membris aptata induitur O; lectionem superius in textu datam non sine dubitatione ipse conieci.
4 cum om. B.
5 est O.
6 et om. O.
7-7 secundus . . . mutatur om. O.
8-8 que non sunt A B C.
9 suos O.

p. 119:
1 passionali A B C; pr̈ n̈li O.
2_2 sumpsit O.
3_3 moralis aut habitus specialis. Et ille ex habitu primo dicto A B C.
4 sive A B.
5 divites *om.* A B C.
6 divinitatem O.
7 habitum B.
8 quod *om.* C O.
9 non *om.* A B C.
10 consequitur O.
11 inefficabiliter O.
12 unita C.
13 unionis A.
14 facere O.

p. 120:
1 esse om. A B C.
2 aliquid O.
3 erit A.
4 principiis om. A B C.
5 cum non inseparabiliter consequitur verbum A B C.
6 conveniunt B.
7 miracli O.
8 specialiter add. A C.
9 personaliter corr. altera manu personali A.

CHECK: the figure for the eighth entry looks like a raised "o" (printed "ᵒ") rather than "8"; I read it as 8, since the main-text figures 1–9 otherwise have no entry for 8.

p. 121:
1 rti O.
2 confirmacionum *om. cum lacuna* C.
3 efficiens C.
4–4 vîtus fîo O.
5 sint A B C.
6 assumpte racione forme A B C.
7 alη (aliquando) B; autem O.
8 ymo locus C.
9 fugurante O.
10 pertinent A B C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 118: lectionem superius in textu datam non sine dubitatione ipse conieci.
p. 119: f° rma P er se in L | genere acci-
p. 120: absoiutum per se | in genere. | forma sui-
```

---

## Chunk 07-e: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-07-e.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-07-e
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "121.8–122.29"
divisions: "cap. 7 (heading 'Cap. VII.' at 105.0); part 5 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "459 words; 459 confirmed by Fordham or the vote; 0 runs stood by rule (both witnesses garbled); 0 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n160–n161 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 7, part 5: [TITLE]

## ¶1 · 121.8–122.24

> [p. 121] Quantum ad primam trium confirmacionum² patet quod similitudo non est sufficiens³; cum humanitas Christi non solum sit ut vestimentum Verbo, vel ignis⁴ ferro,⁴ sed vera Christi quiditas, idem personaliter cum subiecto. Ad 2ᵃᵐ negatur consequencia quod mocio, passio, et similia positiva, cum sint predicata personalia, sunt⁵ persone Verbi racione⁶ forme assumpte⁶ principaliter tribuenda. Non sic autem negaciones, que non sunt predicata personalia. Ideo dixi superius quod incepcio non est esse et prius non fuisse, sed causatur ex illis; cum stat illa esse eterna et incepcionem solum instantaneam, et faciens incepcionem non potest facere dictam negacionem. Ideo non oportet, si Deus temporaliter generatur, quod ante⁷ non fuit; cum satis est quod sit illud ex vi generacionis, quod non effectualiter fuit ante. Ad 3ᵃᵐ patet quod non oportet in toto esse correspondenciam figurati cuiuslibet ad figuram. Unde satis est quod Abraham ducens filium significet Deum Patrem, qui de facto duxit et obtulit super montem Calvarie filium suum unigenitum, sicut Ysaac unigenitus imolatus⁸ est super montem ubi templum constitutum est. Ipse quidem fuit forma risus domini nostri Iesu Christi: et satis est quod humanitas idem personaliter Ysaac nostro, sicut aries est idem genere cum Ysaac figurante,⁹ sic passa et occisa persona Verbi secundum deitatem et animam semper salva; et sic de aliis, que huic loco non pertinet¹⁰ applicare. Sed constat repugnare figure quod sit in toto conformitas; quia tunc evidenter [p. 122] sequeretur¹ Christi mobilitas; cum Ysaac portavit ligna sicut Christus crucem, ligatus est super² struem, sicut Christus affixus est ad crucem. Igitur cum Ysaac noster ex partibus³ quantitativis componitur, que tam⁴ varie movebantur: et, mota parte tocius, movetur et totum, cuius est pars; sequitur quod Christus compositus ex illis partibus movebatur. Nec credo⁵ philosophum dicere Deum esse hominem, nisi consequenter dicat eum componi ex partibus, et consequenter moveri ad motum progressivum parcium⁶; cum⁷ impossibile sit aliquid non moveri, quod tamen subiective habeat in se motum.⁷ Unde Ieronimus exponendo fidem catholicam: ‘passus est, inquit, Dei Filius non putative sed vere.’ Et idem docet Augustinus in Enchiridion 40: et Decretalis in Clementinis De Summa Trinitate et Fide Catholica: ‘confitemur, inquit, Filium Dei, una cum Patre eternaliter subsistentem, partes nostre nature simul unitas, ex quibus ipse verus Deus in se existens fieret⁸ verus homo, (humanum videlicet⁹ corpus et animam intellectivam seu racionalem, ipsum corpus vere et per se et essencialiter informantem,) assumpsisse ex tempore in virginali thalamo ad unitatem sue ypostasis¹⁰ seu persone: et quod in hac assumpta natura ipsum Dei Verbum pro omni operanda salute non solum affigi cruci et in ea mori voluit, sed eciam emisso iam spiritu perforari lancea sustinuit latus suum.’

[ENGLISH]

## ¶2 · 122.25–122.26

> [p. 122] Ecce primo univocacio¹¹ Christi cum fratribus propter¹² convenienciam¹² in natura specifica.

[ENGLISH]

## ¶3 · 122.27–122.27

> [p. 122] Ecce 2°. vera passio Iesu Christi.

[ENGLISH]

## ¶4 · 122.28–122.29

> [p. 122] Et 3°. cum passus sit et mortuus, sequitur quod fuit homo pro illo triduo.

[ENGLISH]

## Notes

## Transcription notes
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 121:
1 rti O.
2 confirmacionum *om. cum lacuna* C.
3 efficiens C.
4–4 vîtus fîo O.
5 sint A B C.
6 assumpte racione forme A B C.
7 alη (aliquando) B; autem O.
8 ymo locus C.
9 fugurante O.
10 pertinent A B C.

p. 122:
1 sequitur A B C.
2 ad A B C.
3 nostris add. A B C.
4 tn (tamen) B.
5 credo om. B.
6 per totum C.
7–7 cum . . . motum om. B.
8 foret O.
9 scilicet B.
10 ypostatice A B C.
11 unic͡o (unicio ?) O.
12 propter convenienciam specificam (sic) A; propter pm (propriam an primam?) convenienciam O.

Note: there is a small "u" printed above "pm" in entry 12, which I could not place with certainty.

CHECK: none
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
(none recorded)
```

---

## Chunk 08-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-08-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-08-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "123.0–127.4"
divisions: "cap. 8 (heading 'Cap. VIII.' at 123.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1053 words; 1041 confirmed by Fordham or the vote; 9 runs stood by rule (both witnesses garbled); 3 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n162–n166 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 8, part 1: [TITLE]

## ¶1 · 123.0–123.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 123] [Obicit tripliciter contra ydemptitatem specificam Christi cum aliis, et dissolvit. Examination of three objections to the statement that Christ is man in the same sense of the word as other men: i.e. that Christ is of the same species as other men.]

[ENGLISH]

## ¶2 · 123.2–123.12

> [p. 123] Ex istis patet solucio argumentorum factorum communiter ad probandum quod Christus non sit univoce homo cum aliis. Primo per hoc, quod nichil reponitur in specie per aliquod sibi accidentale: sed humanitas Christi est sibi accidentalis: ergo non est in nova specie propter illam: sed ante incarnacionem non fuit eiusdem speciei nobiscum: ergo nec¹ post propter² adventiciam unionem. Confirmatur per locum a simili. Nam si homo de novo acquirat albedinem vel quamcumque formam aliam accidentaliter³ inherentem, non ex hoc⁴ est disparis speciei: ergo per idem nec Christus propter humanitatem tam adventiciam.

[ENGLISH]

## ¶3 · 123.13–123.21

> [p. 123] Quantum ad illud patet ex dictis quod falsum assumitur. Nam Verbum, quod prius erat super omnem speciem, per assumpcionem humanitatis factum est in nostra specie et ‘sub lege.’ Et quantum ad similitudinem⁵ patet ex dictis racionis diversitas. Si enim per impossibile albedo vel alia forma inherens esset illud, quo subiectum esset aliquid vel aliud quam prius fuerat, (sicut⁶ humanitate fit Verbum aliquid aliud quam prius fuerat),⁶ procederet racio per locum a simili: sed antecedens est impossibile.

[ENGLISH]

## ¶4 · 123.22–124.16

> [p. 123] Et si multiplicentur argumenta sophistica ad probandum quod, quicquid est Verbum, eternaliter fuit Verbum; patet ex dictis de formis solucio. Nam aliquid, quia aliqua [p. 124] forma substancialis vel natura,¹ nunc est Verbum, quod non in primo instanti temporis erat Verbum. Non enim antequam ‘Verbum caro factum est’ ‘in plenitudine temporis,’ erat homo; et certum² est quod esse hominem est esse aliquid: ideo quando fiebat homo, fiebat aliquid,³ quod prius non fuerat. Verumptamen omne suppositum, ypostasis, vel persona, que est, vel que⁴ fuit, Verbum, eternaliter erat⁵ Verbum. Sed absit ex isto concludere—ergo quicquid.⁶ Aliud enim, sed⁷ non alius, est Verbum post incarnacionem quam prefuit.⁸ Et sic querenti—Quis est⁹ nunc Filius Dei, qui non semper erat ?—Idem—dicitur¹⁰: quod nullus¹¹ est vel esse potest Filius Dei naturalis, nisi¹² qui absolute necessario semper erat. Sed querenti—Quid est Filius Dei, quod ante incarnacionem ipse non fuerat ?—dicitur quod— Natura humana sive humanitas; et illa est quiditas suppositi vel persone—.

[ENGLISH]

## ¶5 · 124.17–124.23

> [p. 124] Et patet solucio ad tales argucias—Omnis¹³ persona, que est Verbum, eternaliter erat Verbum: sed quicquid iam est¹⁴ Verbum est persona, que est Verbum: ergo, quicquid iam est Verbum,¹⁵ eternaliter erat Verbum. Omnes quidem deducciones tales sophistice sanantur¹⁶ per noticiam fallacie accidentis. Nam persone Verbi accidentalis est quiditas in genere, sicut substancie create accidentalis est qualitas.

[ENGLISH]

## ¶6 · 124.24–124.29

> [p. 124] Et si 3°. sic arguatur—Hoc¹⁷ Verbum in principio erat Verbum, et hoc Verbum est hec humanitas; ergo hec humanitas in principio erat Verbum—patet quod idem est ac si sic argueretur—In principio fuit, quod hoc est Verbum; et hoc Verbum est ille homo; ergo tunc fuit, quod ipsum est homo; sic enim significat humanitas simpliciter abstractive.

[ENGLISH]

## ¶7 · 124.30–125.23

> [p. 124] Et si 4°. sophista replicet per conversionem ab exclusivis aut exceptivis—Tantum hoc nunc est Verbum—demonstrando personam Verbi—et hoc eternaliter erat Verbum; [p. 125] ergo nichil iam est Verbum, nisi quod eternaliter erat Verbum—constat quod antecedens est verum et consequens falsum. Licet enim tantum hoc sit Verbum, non tamen tantum ista humanitas est Verbum: cum deitas,¹ que est aliud quam illa humanitas, est Verbum et² eternaliter erat Verbum. Et patet quod, licet tantum homo et tantum Deus sit Verbum, non tantum humanitas, nec nichil preter deitatem est Verbum. Nam aliud quam deitas et aliud quam humanitas est Verbum; sed nec alius nec aliud quam Deus vel homo est Verbum. Si enim tantum deitas esset Iesus, tunc Pater in divinis non esset aliqualiter³ maior Iesu. Et constat quomodo exclusive ac exceptive sint suis universalibus adaptande; ut sic dicto—omnis Iesus est humanitas—⁴ licet correspondenter dare istam⁴ exclusivam— tantum persona, que est humanitas, est Iesus—et proporcionaliter exceptivam et non conformissimam⁵ sophisticacionem contingit habere de quolibet alio homine, qui per se est homo, sed adventicie natura corporea.⁶ Unde quilibet nostrum in finali resurreccione erit aliud quam erat⁷ in morte, quia alia natura; cum in resurreccione erit tam natura corporea quam natura incorporea; in morte autem dumtaxat natura incorporea. Sed non erit alius: ymo solummodo idem ipse, cum non potest esse nisi eadem persona.

[ENGLISH]

## ¶8 · 125.24–126.6

> [p. 125] Et illam methaphisicam intexuit⁸ ille magnus philosophus sanctus Iob 19 ca°. quando dixit; ‘in carne mea videbo Deum salvatorem meum, ego ipse, inquit, et non alius.’ Unde Gregorius 18 Moralium ca°. 32. ‘Quamvis Christus sit aliud ex Patre aliud ex matre,⁹ non tamen est alius ex Patre alius ex virgine: sed ipse eternus ex Patre, temporaliter ex matre⁹; ipse,¹⁰ qui fecit, factus¹⁰; ipse auctor operis, ipse opus auctoris; manens unus ex utraque et in¹¹ utraque natura¹²; nec naturarum¹¹ copulacione confusus, [p. 126] nec naturarum distinccione geminatus.’¹ Ecce aliud sancti doctoris testimonium de² sentencia supradicta.² Et sic intelligendus est Augustinus in Dialogo ad Felicianum circa medium et alibi crebrius, quando dicit: ‘quamvis enim aliud corpus, aliud animus, unus tamen atque idem homo et corpus dicitur et animus.’

[ENGLISH]

## ¶9 · 126.7–127.4

> [p. 126] 2°. principaliter arguitur contra ydemptitatem specificam Christi cum aliis ex hoc quod³ ipse solum per accidens et quilibet alius per se est homo. Sed patet ex dictis quod non sequitur. Cum illud accidens, quo Christus est homo formaliter, quod Apostolus vocat humanitacionem⁴ et habitum,⁴ sit eiusdem racionis cum formis, quibus confratres Christi sunt homines formaliter, et non est accidens simpliciter. Sed quia Christus est gigas gemine substancie, scilicet, deitas et humanitas, quarum inferior contingenter inest superiori; ideo dicitur⁵ humanitas ad sensum expositum accidens Verbo Dei. Et si queritur⁶ utrum Christus⁷ sit per se homo, videtur michi quod sic. Nam cum ‘Christus’ dicit duas formas, scilicet deitatem et humanitatem,⁸ ydemptificatas⁹ in eadem persona, et potest supponere simpliciter pro utraque: patet quod, intelligendo eum secundum humanitatem, ipse eque per se est homo sicut aliquod¹⁰ individuum sui generis; cum eque vere causatur¹¹ ex partibus qualitativis et quiditativis consimilis racionis, et eque dependet a corpore et anima a specie et genere cum suis differenciis, sicut Petrus. Nec est color, si Christus sit per accidens homo quia secundum deitatem, quod non sit per se homo: quia¹² extra deitatem est humanitas Christi, que est per se homo,¹² cum de sua essencia sit universalis¹³ humanitas. Et ita sicut duplici nativitate nascitur Verbum Dei, sic videtur michi quod duplici [p. 127] racionalitate¹ satis equivoce est ipsum² racionale. Nam² quoad creatam substanciam causatur³ ab humanitate et racionalitate¹ communi sicut alie creature: et hinc competit sibi primus modus predicandi per se ex 2°. posteriorum.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 124: *argucias—Omnis* (print = bt) [SUB]
  - 125: *dicto—omnis* (print = bt) [SUB]
  - 125: *Iesus—et* (print = bt) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference John i. 14. (124.3); reference 25 Job xlx- 26"27- (125.25); reference So Gregory (125.27); reference Augustinus (127.11).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 123:
1 nec om. O.
2 propter om. O.
3 accidenter O.
4 exinde O.
5 consimilitudinem O.
6–6 ( ) om. A B; sic humanitatem fit verbum aliquod aliud quam fuerat prius C.

p. 124:
1 m (materia) O. [with a small "u" raised above the m]
2 iterum O.
3 aliud O.
4 que *om.* A B C.
5 fuit A B C.
6 quicquam *om.* ergo A B; quod quitquam C.
7 et A B C.
8 ante A B C.
9 esset B.
10 eidem A B C.
11 erat *add.* B.
12 non qui B.
13 omnes persona O.
14 est *om.* O.
15 et *add.* A B C.
16 sonantur O.
17 arguitur A; obicitur B.

Corrected for the plain-text format:

1 m͞u (materia) O.
2 iterum O.
3 aliud O.
4 que om. A B C.
5 fuit A B C.
6 quicquam om. ergo A B; quod quitquam C.
7 et A B C.
8 ante A B C.
9 esset B.
10 eidem A B C.
11 erat add. B.
12 non qui B.
13 omnes persona O.
14 est om. O.
15 et add. A B C.
16 sonantur O.
17 arguitur A; obicitur B.

p. 125:
1 divinitas O ut saepe infra.
2 et om.O.
3 a’q°° (aliquo modo) B.
4–4 habet correspondenter istam O.
5 non om. A B C; ɔformissia˥ O.
6 nature corporee A B C.
7 erit O.
8 texuit A B C.
9–9 non . . . matre om. B.
10–10 ipse qui fecit ipse qui factus est A B C.
11–11 in utramque natura nec naturam O.
12 natura om. A B C.

CHECK: the figures 4, 9, 10 and 11 each appear twice in the text and are given as paired entries (4–4, 9–9, 10–10, 11–11). Every figure has an entry, and no extra figures occur at the foot.

p. 126:
1 genitus O.
2-2 de s͡cia sepe dicta A B C; de sm͡a sepe dicta O.
3 quod *om.* A B C.
4-4 humanitatem et hominem A B C.
5 debet B.
6 queratur A B C.
7 Iesus A B C.
8 que sunt *add.* A B C.
9 ydemptitas *codd. omn.*
10 aliquid O.
11 causantur O.
12-12 quia . . . homo *om.* C; quia extra deitatem est ho̶ humanitas Christi que est *etc.* A; quia extra deitatem est homo humanitas Christi que est *etc.* B; quia extra deitatem est humanitas Christi qui est *etc.* O.
13 illius A B C.

p. 127:
1 racionabilitate A B C.
2–2 ipsum homo. Nam. B.
3 cîttur *vix per rasuras distingui potest in* A; creatur B.
4–4 secundum . . . quos *in margine* O.
5 habuerunt A; habuerat C.
6 quantitate A B C.
7 *numerus in omn. codd. om.*
8 aut C.
9 9 A B C.
10 nisi per accepcionem O.
11 attendendo A B C.
12 filio . . . filio A B C.
13 ppr (proporcionaliter) habeat A C; pⁿbiliter (probabiliter) *om.* habeat B.
14 *Nonne* hominem *legendum*?
15–15 sic . . . hominem *om.* O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 123: [Obicit tripliciter contra ydemptitatem specificam Christi cum aliis, et dissolvit. Examination of three objections to the statement that Christ is man in the same sense of the ivord as other men : | that Christ is of the same | as other tnen.~\
p. 126: thly P pe)a se! denS | tB ex °i uo ^
p. 127: a ^ l ^ a ' le racionale | rociofialis sub- | stancia ex cor- 1 1 | pore et anima | habens corpus. | vix per rasuras distingui poiest in
```
