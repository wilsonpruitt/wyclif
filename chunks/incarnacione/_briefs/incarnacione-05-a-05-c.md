# Translation brief: incarnacione 05-a–05-c

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
5. Run `cd /Users/wilsonpruitt/wyclif && .venv/bin/python scripts/w3/lint.py chunks/incarnacione/wyc-incarnacione-05-a.md chunks/incarnacione/wyc-incarnacione-05-b.md chunks/incarnacione/wyc-incarnacione-05-c.md` once and fix what it reports.
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

## Glossary (the 310 rows these chunks use; the full file is GLOSSARY.md)

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
| sponsa / sponsus | bride / bridegroom | |
| corpus Christi misticum | the mystical body of Christ | |
| mater nostra | our mother | Church as mother is the governing figure of *De ecclesia* I. |
| fides explicita / implicita | explicit faith / implicit faith | The scholastic pair (*Dial.* 28.16–17). Ruled 2026-09-28. |
| articulus fidei | article of faith | Ruled 2026-09-28 (4 sites). |
| Christicole | worshippers of Christ | Ruled 2026-09-28. |
| litere fraternitatum | letters of fraternity | Friars' letters admitting a benefactor to the order's suffrages. Ruled 2026-09-28 (4 sites). |
| viantes | those on the road | The participle beside *viator* (wayfarer); kept distinct so the reader sees which word Wyclif used. Ruled 2026-10-01 (≈22 sites in *De ecclesia*; first *Eccl.* 10.12). |
| universitas fidelium | the whole body of the faithful | Ruled 2026-10-02 (*Eccl.* 37.13). |
| exempcio | exemption | Ruled 2026-10-02 (*Eccl.* 9). |

## B. Lordship, law, office

| Latin | English | Note |
|---|---|---|
| dominium | **lordship** | Not "dominion". Titles: *De civili dominio* → *On Civil Lordship*; *De dominio divino* → *On Divine Lordship*. |
| dominus; dominari | lord; to exercise lordship / to lord it | Pick by context (neutral vs. pejorative) and note the pejorative. |
| dominium civile / naturale / evangelicum | civil / natural / evangelical lordship | |
| dominacio | exercise of lordship | Kept apart from *dominium*. Ruled 2026-09-28 (6 sites). |
| ordinacio; ordinancia | ordinance; of the sacrament, ordination | Two senses by referent (not CONTEXTUAL): the sacrament (*clericorum ordinacio*, *Dial.* 50.21) is "ordination"; everywhere else "ordinance". Ruled 2026-09-28 (22 sites). Third referent, the logician's arrangement of terms in a proposition (*Incarn.* 49.10): "ordering", with a **C** note; ruled 2026-10-22 (coordinator, delegated). |
| consuetudo | custom | Ruled 2026-09-28 (28 sites). |
| magnates | magnates | Ruled 2026-09-28. |
| servicium | service | Pair with *dominium* (T. p. 363 n. 19 on the definitions). Liturgical *servicia ecclesie*, "services of the church", is untagged. Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius | right / law | ⚠ Two senses (subjective right vs. body of law). The chunk's note picks one wherever it matters. |
| lex dei / lex Christi / lex evangelica | God's law / the law of Christ / the gospel law | |
| deitas / divinitas | the Godhead / divinity | Kept distinct; B reads *divinitatis* at *Dial.* 2.13. |
| potencia regulata racione | power regulated by reason | Pilot. |
| decime; pars decima | tithes; the tenth part | |
| temporalia | temporal goods | |
| curatus | curate | In the old sense: a priest with the cure of souls. Note at first occurrence per work. |
| temporales domini | temporal lords | Kept apart from *mundani domini*, worldly lords. Ruled 2026-09-28 (coordinator, delegated) (22 sites). |
| milicia; milites | knighthood; knights | The second estate; Pollard's word. Ruled 2026-09-28 (coordinator, delegated). *Milites Christi / antichristi* (the Pauline figure, 2 Tim. 2:3 DR "good soldier of Christ Jesus") → "soldiers"; the estate stays "knights". Ruled 2026-09-29 (coordinator, delegated, close-out). |
| ius patronatus | right of patronage | Ruled 2026-09-28 (coordinator, delegated). |
| commutacio; commutare | exchange; to exchange | The argument on true and false trade turns on it (*Dial.* cap. 33). Ruled 2026-09-28 (coordinator, delegated) (8 sites). |
| citare; citacio | to cite; citation | Summons to a church court. Ruled 2026-09-28 (coordinator, delegated) (12 sites). |
| suspendere; suspencio | to suspend; suspension | Note the pun on hanging where live (*Dial.* 57.10–16). Ruled 2026-09-28 (coordinator, delegated). |
| episcopus; dominus episcopus | bishop; the lord bishop | *Dominis episcopis* → "the lord bishops". The courtesy is his, possibly barbed; don't sharpen it. Pilot. |
| claustrales | cloisterers | Ruled 2026-09-28 (20 sites). |
| thema | theme | The scripture text of a sermon. Ruled 2026-09-28 (2 sites). |
| possessionati | the possessioners | Endowed religious. |
| lex gracie | the law of grace | The new law, opposed to *lex vetus*. Ruled 2026-09-28 (*Dial.* 10.3; 7 sites). |
| heretica pravitas | heretical depravity | The heresy courts' formula; keep it recognisable. Ruled 2026-09-28 (*Dial.* 7.5, 7.8). |
| plenitudo potestatis | plenitude of power | The canonists' term for papal power. Ruled 2026-10-01 (6 sites in *De ecclesia*; first 13.6). |
| de virtute sermonis | in the proper sense of the words | Wyclif's recurring formula for the literal force of an expression. Ruled 2026-10-02 (*Eccl.* 115.6, 115.8). |
| gracia preveniens / comitans / concomitans / consumans | prevenient / accompanying / concomitant / consummating grace | Ruled 2026-10-02 (06-g). |
| insolubilia | insolubles | The logicians' paradoxes of self-reference. Ruled 2026-10-02 (*Eccl.* 175.11). |
| contribules | countrymen | Lev. 25:17 (DR). Ruled 2026-10-02 (208.2, 214.20, 214.27). |
| elemosina temporalis / perpetua | temporary alms / perpetual alms | "Temporary" keeps it apart from *temporalia*; *perpetua* answers to frankalmoign. Where the sense is alms *paid in* temporal goods (as 335.11), "alms in temporal goods", with a C note. Ruled 2026-10-02 (*Eccl.* 13, 15). |

## C. Logic, disputation, metaphysics

| Latin | English | Note |
|---|---|---|
| inconveniencia; inconveniens | CONTEXTUAL: an absurdity (in argument) · troubles, ill consequences (in affairs) | One word for what does not fit: the absurd consequence of a premiss, and the disorder that follows from an act. Dikaiosune rule: English by context, **C** note at first occurrence in each chunk and wherever it leans the other way (*Dial.* 22.16 troubles; 23.2, 23.16 absurdities). Ruled 2026-09-28 (3 sites). |
| argumentum topicum | topical argument | Merely probable, not demonstrative. Ruled 2026-09-28 (4 sites). |
| medium inductivum | a middle term that leads on | Ruled 2026-09-28 (*Dial.* 25.5). |
| ars obligacionis | the art of obligation | The disputation genre *de obligationibus*. Ruled 2026-09-28 (2 sites). |
| assumptum | the assumption | The premiss taken for the argument. Ruled 2026-09-28 (3 sites). |
| sentenciare | to pronounce | The verb of *sentencia*. Ruled 2026-09-28 (2 sites). |
| predicamentum | category | The Aristotelian category; never "predicament" (*Dial.* 92.1: the standard member of a category). Ruled 2026-09-28 (coordinator, delegated). |
| sequela | CONTEXTUAL: what follows / following | The logical consequence "what follows"; of following Christ (*sequela Christi*) "following" (*Pot. pape* 63.13). Ruled 2026-09-28; second sense 2026-10-07. |
| racio (against *substancia*) | aspect | This technical sense only; *racio* elsewhere by context. Ruled 2026-09-28 (coordinator, delegated). |
| insinuativus | implied | Paired with *expressus*, express. Ruled 2026-09-28. |
| quid nominis | what the name means | Not "the name" (T. p. 365). Pilot (*Eccl.* 5.11). |
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
| instatur; obicitur | it is objected | The disputation's objection formulae (*Eccl.*). Ruled 2026-10-01 (Wilson, with the *De ecclesia* card). |
| dicitur (opening an answer) | the answer is | Elsewhere "it is said" (*Hic dicitur quod …*, *Eccl.* 26.8: "To this the answer is that …"). Ruled 2026-10-01 (Wilson). |
| respondetur | the reply is | Ruled 2026-10-01 (Wilson). |
| glosare | to gloss | Interpret so as to remove the difficulty (T. p. 366). |
| successivum / permanens | successive entity / permanent entity | T. p. 368 n. 31. |
| ens / esse / essencia | a being / being (existence) / essence | ⚠ *Esse* is ambiguous; note when it matters. |
| universale; ydea | universal; idea | |
| liberum arbitrium | free choice | The scholastic term, not "free will" (*voluntas*). Ruled 2026-09-28 (*Dial.* 4.15). |
| ex fide | as faith teaches; with a genitive, from the faith of [scripture] | "It is of faith", on scripture's authority. *Ex fide scripture / duplicis testamenti* → "from the faith of scripture / of the twofold testament". Ruled 2026-09-28 after a census (30 sites in the *Dialogus*). An adjective works like the genitive: *ex fide catholica* → "from the catholic faith". Not the formula when a verb or participle governs *ex* (*racio capta ex fide* → "reason drawn from faith", epil-a). Ruled 2026-09-29 (coordinator, delegated, close-out). |
| sentencia | CONTEXTUAL: teaching / sentence | The position taught, incl. Falsehood's (*tua sentencia*, "your teaching"). Not "sentence" for a position taught. Ruled 2026-09-28 (51 sites in the *Dialogus*). A judicial sentence (of excommunication) is "sentence", with a **C** note (*Eccl.* 221.33, 2026-10-02). |
| evidencia | evidence | "Proof" only where it names a demonstration, with a note. Ruled 2026-09-28 (41 sites). |
| concessio | grant | Of property or privilege. Ruled 2026-09-28 (5 sites). |
| formido (*sine / cum formidine*) | misgiving | The scholastic "fear of the opposite" that qualifies assent; "fear" only where it is plainly the emotion. Ruled 2026-10-01 (19 sites in *De ecclesia*; first 5.24). |
| obicitur per | it is objected, by appeal to | Parallel to *arguitur per*. Ruled 2026-10-01 (*Eccl.* 21.27). |
| aggregative | aggregatively | The church taken as an aggregate of its members. Ruled 2026-10-02 (26.21). |
| de inesse | as a matter of fact | The assertoric (non-modal) proposition. Ruled 2026-10-02 (31.22). |
| sillogismus expositorius / expositorie | expository syllogism / expositorily | A syllogism with a singular middle term. Ruled 2026-10-02 (28.13, 31.11). |
| color (*non est color*) | colour (a plausible ground) | The period sense, as in "colour of title"; never "pretext". A **C** note at the first occurrence in each chunk. Ruled 2026-10-02 (Wilson; *Eccl.* 21.18, 23.5, 23.7). |
| glosa | gloss | The noun beside *glosare*. Ruled 2026-10-02 (52.10). |
| libertas arbitrii | freedom of choice | Beside *liberum arbitrium*. Ruled 2026-10-02 (60.18). |
| concorporacio | concorporation | Incorporation into one body (Loserth's own English). Ruled 2026-10-02 (73.11). |
| participium | participation | Not the grammatical participle, except where Wyclif is doing grammar (*Pot. pape* 21.24 *participium neutrum*, G note). Ruled 2026-10-02 (85.6). |
| conclusio | conclusion | The disputation formula (card). Ruled 2026-10-02. |
| terminus communis | common term | Aristotle's common boundary of a continuum (*Cat.* 6). Ruled 2026-10-02 (*Eccl.* 104.23 ff., 107.23). |
| ingratitudo | ingratitude | Toward a person. Ruled 2026-10-02 (156.8). |
| colorare | give colour to | The verb beside *color*. Ruled 2026-10-02 (163.2). |
| minoritas | lesser standing | Beside *maioritas* "greatness". Ruled 2026-10-02 (172.22). |
| laureola | aureole | The theologians' special crown (of virgins, martyrs, doctors). Ruled 2026-10-02. |
| humanitas | the humanity | The nature the Word assumed, body and soul; with the article (*humanitas sit Christus*, "the humanity is Christ"). Not "the human nature", which is *natura humana*. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| dimittere / dimissio (*naturam*) | lay aside / the laying-aside | Letting go the assumed nature, so the union would be dissolved. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 2.23). |
| assumere / assumpcio (*naturam*) | assume / assumption | Of the nature, as in the fathers. ⚠ Kept apart from the logician's *assumptum* "the assumption" (above): C note where the logical sense occurs. Ruled 2026-10-22 (Wilson; *Incarn.* prol, 1). |
| triduum (*in triduo*) | the three days | Death to resurrection, body in the tomb (Lombard, *Sent.* III d. 22). Ruled 2026-10-22 (Wilson; *Incarn.* prol). |
| Verbum | the Word | Pronoun **"he"** (as Douay–Rheims John 1:3, "by him"), never "it", though the Latin is neuter. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.3–4). |
| homo assumptus | the assumed man | A term of art (the Lombard's first opinion, *Sent.* III d. 6); keep "assumed" before "man", never "the man assumed". Ruled 2026-10-22 (Wilson; *Incarn.* 5.15). |
| secundum quod (reduplicative) | insofar as | ⛔ Never "in that" (heard as "because", which inverts the logic). Ruled 2026-10-22 (Wilson; *Incarn.* 5.29–6.24). |
| secundum deitatem / secundum humanitatem | as to the Godhead / as to the humanity | The rule of reduplication; keep it in Wyclif's place in the sentence. ⛔ Never supply "as God / as man" where the Latin has bare apposition (*ipse Deus*) or bare predication. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| natura | nature | Ruled 2026-10-22 (Wilson; *Incarn.* 3.4). |
| persona | person | Ruled 2026-10-22 (Wilson; *Incarn.* 4.14). |
| creatura / creator / creatus | creature / creator / created | ⛔ Never "creation" for the created thing. Ruled 2026-10-22 (Wilson; *Incarn.* 1). |
| posicio / proposicio / predicacio | position / proposition / predication | Kept apart: the apparatus shows the three trading places (*Incarn.* 4.15). Ruled 2026-10-22 (Wilson). |
| moderni doctores / moderniores doctores | the modern doctors / the more modern doctors | Ockham and the *moderni*, usually unnamed. Ruled 2026-10-22 (Wilson; *Incarn.* prol 2.1). |
| sancti | the saints | The fathers. Ruled 2026-10-22 (Wilson; *Incarn.* prol 1.15). |
| probabiles doctores | reputable doctors | *Probabilis*: worthy of credence (cf. *probabiliter*). Ruled 2026-10-22 (Wilson; *Incarn.* 7.1) as "approved doctors"; changed the same day (coordinator) to free "approved" for *approbati*. |
| abstractive | abstractively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 10.6). |
| copulative (adv.) | conjunctively | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 9.23). |
| ypostatice | hypostatically | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 12.2). |
| determinacio | determination | A qualifying addition to a predicate (*cum determinacione*). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 14.11). |
| Sermo (beside *Verbum*) | Speech | The divine title, capitalised; *Verbum* stays "the Word". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 16–17). |
| de vi vocis | by the force of the words | Kept apart from *de virtute sermonis* "in the proper sense of the words". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20, 28). |
| natura specifica | the nature of the species | After *ydemptitas specifica*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 20). |
| determinaciones ecclesie | the church's determinations | Rulings of the church, not the logician's *determinacio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 24). |
| nedum | not only | "Let alone" where the sense is a fortiori. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 21, 24). |
| materia prima | prime matter | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
| gracia unionis | the grace of union | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 25). |
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
| in effectu | in actual fact | As against in potency or in name; ⛔ not "in effect" (modern "virtually"). Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 47.10). |
| animare | animate | The argument turns on it (45.30–46.4). Ruled 2026-10-22 (coordinator, delegated). |
| communicacio ydiomatum | communication of idioms | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.1). |
| predicacio actualis / aptitudinalis / habitudinalis / mixtim | actual / aptitudinal / habitudinal / mixed predication | *Habitudinalis* is its own term (the four MSS at 49.6), not under *habitudo*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.5–16). |
| denominativum | denominative | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.30). |
| Doctor Subtilis | the Subtle Doctor | Scotus. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 49.24). |
| convertibilis / converti | convertible / be convertible | Of terms. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 52.29). |
| previe requisitum | required beforehand | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 53.25). |
| forma totalitatis | form of totality | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 50.7). |
| quantus | quantified | The adjective beside *quantitas*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.22). |
| suppositacio | suppositation | Kept apart from *supposicio* "supposition". Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.31). |
| construccio synecdochica | synecdochic construction | Beside *synecdochica locucio*. Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.5). |
| carneus / carnalis | fleshy / carnal | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 56.21). |
| moderniores loquentes | the more modern speakers | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 59.21). |
| supposibilis | that can be supposited | Ruled 2026-10-22 (coordinator, delegated; *Incarn.* 64.14). |
| Magister | the Master | Peter Lombard. Ruled 2026-10-22 (Wilson; *Incarn.* 3.24). |
| declarare / ostendere | make clear / show | Kept apart (both in one sentence, prol 2.5–7). Ruled 2026-10-22 (Wilson). |
| infirmitas (of Christ's flesh) | weakness | Ruled 2026-10-22 (Wilson; *Incarn.* 5.31–6.11). |

## D. False friends and ordinary words that mislead

| Latin | English | Note |
|---|---|---|
| apostema | abscess | A recurring medical figure. Ruled 2026-09-28 (3 sites). |
| sub divo | in the open air | The refrain of cap. 21. Ruled 2026-09-28 (10 sites). |
| ingratus | displeasing (to God) | *Ingratus deo*: unpleasing to God. "Ungrateful" only where a person is ungrateful to someone. Ruled 2026-09-28 (5 sites). |
| solvere (oaths, charters) | to dissolve | Not "pay" in this use. Ruled 2026-09-28 (coordinator, delegated). |
| magisterium | rule; of teaching, the teaching office | Provisional; by context, C note (*Dial.* 83.15). Ruled 2026-09-28 (coordinator, delegated). |
| subtiliare | to lighten; to refine (argue subtly) | CONTEXTUAL. "Lighten" provisional in *Dial.* 67.19, 68.11 (C note); "refine, argue subtly" of argument (*Pot. pape* 260.8, 2026-10-08). |
| impresenciarum | nowadays, at present | (T. p. 366) |
| ut plurimum | for the most part | "to the highest degree" (T. p. 366) |
| ignorare | to be ignorant of | "ignore" (T. p. 366) |
| arguitur per | it is argued by appeal to | "X raises objections" (T. p. 366) |
| in necessitatis articulo | at the point of need | Pilot |
| processus (of a book) | the course, the argument | Pilot (*Eccl.* 2.28) |
| conversacio | manner of life | "conversation". Ruled 2026-09-28 (6 sites). |
| gratitudo | kindness (received) | "gratitude". Ruled 2026-09-28. |
| habere conscienciam super | to be troubled in conscience over | Ruled 2026-09-28 (5 sites). |
| prioritas; majoritas | priority; greatness | Paired with *prior / major* in the argument (*Dial.* 12.4–8). Ruled 2026-09-28. |
| servitivus | serviceable | Ruled 2026-09-28. |
| ius poli / ius fori | the law of heaven / the law of the court | Augustine's pair. Ruled 2026-10-02 (*Eccl.* 14). |
| dispensator | dispenser | As DR 1 Cor. 4:1–2; kept apart from *procurator* "proctor". Ruled 2026-10-02 (*Eccl.* 14). Inside a DR quotation of Titus 1:7, DR's "steward" (2026-10-08). |
| in capite (tenure) | in chief | Feudal tenure from the king directly. Ruled 2026-10-02 (*Eccl.* 14). |
| ritus | rite | Any usage or observance, not only liturgical. Ruled 2026-10-02 (*Eccl.* 14). |
| catholicare / hereticare | to declare catholic / to pronounce heretical | Ruled 2026-10-02 (*Eccl.* 14). |
| dominatus | lordly rule | Bernard's word (*apostolis interdicitur dominatus*); kept apart from *dominium* "lordship". Ruled 2026-10-02 (*Eccl.* 14). |
| ablacio | taking-away | Set against *restituere*/*restitucio*. Ruled 2026-10-02 (*Eccl.* 15). |
| nominetenus clerici | clerics in name only | Recurs (*solum nomine sacerdotes*, 347). Ruled 2026-10-02 (*Eccl.* 15, 340.19). Of a pope (*Pot. pape* 147.31): "pope in name only" (2026-10-08). |
| cognoscere super | take cognizance of | Legal sense. Ruled 2026-10-02 (*Eccl.* 15, 340.31). |
| signa (of an argument) | stages | Ruled 2026-10-02 (*Eccl.* 15, 351.19). |
| dii subterranei | gods beneath the earth | Ruled 2026-10-02 (*Eccl.* 15, 357.30). |
| dominabilia | the things held in lordship | Ruled 2026-10-02 (*Eccl.* 16, 378.6). |
| potencia absoluta | absolute power | Ruled 2026-10-02 (*Eccl.* 16, 375). |
| milicia / milites (the clergy as paid spiritual army) | soldiery / soldiers | Under the Pauline-figure clause of the 09-28 *milicia; milites* row, which governs; G note at use. The captive knight (381.1–2) stays "knight". Ruled 2026-10-02 (*Eccl.* 16, 384–385). |
| amerciare; multacio | amerce; fine | Legal terms. Ruled 2026-10-02 (*Eccl.* 16, 387.19–21). |
| signabile | signifiable; assignable | CONTEXTUAL. The logical noun (*omne signabile*, what can be signified) is "signifiable" (*Eccl.* 17, 398.29). As an adjective on a degree, instant or step (*in quocumque gradu/profectu signabili*) it is "assignable", any one could name (*Pot. pape* 11-j, 11-k). Ruled 2026-10-02; extended 2026-10-12 (close-out R3). |
| denominacio; denominare | naming; to name | The argument turns on it. Ruled 2026-10-02 (*Eccl.* 17, 391.17, 398.2). |
| dotes (docium) beatorum | the dowries of the blessed | Ruled 2026-10-02 (*Eccl.* 17, 396.6). |
| christianus in figura / in effectu / in fructu | Christian in figure / in effect / in fruit | Ruled 2026-10-02 (*Eccl.* 17, 397–398). |
| color rethoricus | rhetorical colour | The figure of speech, distinct from *color* "plausible ground". Ruled 2026-10-02 (*Eccl.* 17, 405.3). |
| argumentum ad hominem | argument to the man | Ruled 2026-10-02 (*Eccl.* 17, 405.13). |
| pars quantitativa | quantitative part | Ruled 2026-10-02 (*Eccl.* 17, 406–407). |
| secundum presentem iusticiam | according to present justice | As against predestination; "present justice" is the established rendering (11 chunks; 18-a conformed). Ruled 2026-10-02 (*Eccl.* 18, 415–416). |
| species specialissima | most special species | Ruled 2026-10-02 (*Eccl.* 18, 418). |
| persona successiva | successive person | Ruled 2026-10-02 (*Eccl.* 17, 414.1). |
| transsumptive | transumptively | Ruled 2026-10-02 (*Eccl.* 18, 431.30). |
| circumscriptive | circumscriptively | Ruled 2026-10-02 (*Eccl.* 18, 423.24). |
| possessionatus (adj.) | possessioned | The adjective beside the noun *possessionati* "the possessioners". Ruled 2026-10-02 (*Eccl.* 18, 434–435). |
| gracia gratificans | grace that makes pleasing | Ruled 2026-10-02 (*Eccl.* 18, 441.8). |
| responsalis | the respondent | Ruled 2026-10-02 (*Eccl.* 19, 445.24). |
| termini magistrales | masters' terms | Ruled 2026-10-02 (*Eccl.* 19, 445.23). |
| continuacio | continuity | Ruled 2026-10-02 (*Eccl.* 18, 436.19). |
| precaria | precarial grant | Wyclif defines it (*Eccl.* 453.21). Ruled 2026-10-02 (*Eccl.* 19). |
| vir ecclesiasticus | churchman | Ruled 2026-10-02 (*Eccl.* 19, 450.18, 451.10). |
| lex cesarea | caesarean law | Of the *clerus cesareus* family (pejorative), not neutral "imperial/civil law". Ruled 2026-10-02 (*Eccl.* 19, 451.17). |
| evidencia topica | topical evidence | Pairs with *argumentum topicum*. Ruled 2026-10-02 (*Eccl.* 19). |
| porisma | porism | A consequence drawn from a principle; kept apart from *corollarium* "corollary". Ruled 2026-10-02 (*Eccl.* 19, 462.22). |
| translative | by transference | Kept apart from *transsumptive* "transumptively". Ruled 2026-10-02 (*Eccl.* 19, 467.10). |
| rectiloqui | those who speak correctly | Ruled 2026-10-02 (*Eccl.* 19, 468.15). |
| raciones exemplares / seminales | exemplary reasons / seminal reasons | Augustine's terms; "seminal reasons" already used at 06-d. Ruled 2026-10-02 (*Eccl.* 20, 473.18). |
| institor | merchant | After Douay "merchant's ship" (Prov. 31:14); *mercantes* = "traders". Ruled 2026-10-02 (*Eccl.* 20, 478.20). |
| predicacio secundum causam | predication by cause | One of Wyclif's modes of predication. Ruled 2026-10-02 (*Eccl.* 20, 481.14). |
| beatitudo essencialis / accidentalis | essential / accidental blessedness | The scholastic pair; follows *beatitudo* "blessedness". Ruled 2026-10-02 (*Eccl.* 20, 490.15). |
| signacio / significacio | signification | B treats them as one word (492.9–10, 493.1). Ruled 2026-10-02 (*Eccl.* 21, 491). |
| dampnacio | CONTEXTUAL: damnation / condemnation | Thomas's broad/strict senses turn on it; Douay "condemnation" kept in Luke 23:40. Ruled 2026-10-02 (*Eccl.* 21, 495.24). Of a judgement passed on a teaching (*dampnacio istius sentencie tamquam heretice*, *Pot. pape* 84.10) "condemnation"; ruled 2026-10-07. |
| signaculum | seal | Ruled 2026-10-02 (*Eccl.* 21, 500.21). |
| partes potestative / subiective / aliquote | potestative / subjective / aliquot parts | The scholastic division of wholes. Ruled 2026-10-02 (*Eccl.* 21, 509.3–5). |
| pars integralis | integral part | Ruled 2026-10-02 (*Eccl.* 21, 514.15). |
| res sacramenti | reality of the sacrament | Ruled 2026-10-02 (*Eccl.* 21, 511.8). |
| gracie gratis date | graces freely given | Kept apart from *gracia gratificans*. Ruled 2026-10-02 (*Eccl.* 21, 512.13). |
| beatificacio | beatification | Ruled 2026-10-02 (*Eccl.* 22). |
| perfeccio secunda (mundi) | second perfection | Ruled 2026-10-02 (*Eccl.* 22). |
| oracio absoluta / condicionata | absolute / conditional prayer | Ruled 2026-10-02 (*Eccl.* 22). |
| bonum honestum / utile / delectabile | honourable / useful / pleasurable good | Ruled 2026-10-02 (*Eccl.* 22). |
| liga | league | Ruled 2026-10-02 (*Eccl.* 22). |
| beatitudo circularis | circular blessedness | Hostiensis's term. Ruled 2026-10-02 (*Eccl.* 22). |
| forum penitencie / penitenciale; forum ecclesie / Dei | court of penance; court of the church / of God | Ruled 2026-10-02 (*Eccl.* 23, 550.15). |
| supererogare; supererogacio | pay out beyond [what is owed]; supererogation | *supererogata merita* "supererogated merits". Ruled 2026-10-02 (*Eccl.* 23, 551). |
| reatus pene | liability to punishment | Ruled 2026-10-02 (*Eccl.* 23, 552.4). |
| participative / iuvative | participatively / helpingly | Ruled 2026-10-02 (*Eccl.* 23, 558.2). |
| in athomo | in an individual | The logicians' *atomus*. Ruled 2026-10-02 (*Eccl.* 23, 558.4). |
| potestas iudiciaria | judicial power | Ruled 2026-10-02 (*Eccl.* 23, 565.26). |
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
| superintendencia | oversight | The bishop's office as *episcopus* "overseer". Ruled 2026-10-07 (*Pot. pape* 73.20). |
| repugnare; repugnancia | to be incompatible; incompatibility | The logical sense; not "to fight". Ruled 2026-10-07 (*Pot. pape* 73–75). |
| primogenitura | primogeniture | Ruled 2026-10-07 (*Pot. pape* 103.2). |
| potestas regiminis | power of rule | Paired with *potestas ordinis* "power of order". Ruled 2026-10-07 (*Pot. pape* 115.2). |
| potestas dominativa | lordly power | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.23). |
| relacio racionis | relation of reason | Scholastic term (a relation in the mind only). Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 3.7). |
| debitum (coniugale), ex debito | the (marriage) debt | Of spouses (1 Cor 7:3–4): "the marriage debt", not "what is owed". Ruled 2026-10-07 (*Pot. pape* 5.8). |
| maneries | kind | Ruled 2026-10-07 (coordinator, delegated; *Pot. pape* 4.17). |
| status (disposicionis, virtutis, …) | state (of disposition, of virtue, …) | Ch. 6 turns on it (a man's state changed by sin). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 06-g). |
| primas (noun) | primate | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| dominari (with a negative, 1 Pet. 5:3) | lord it (over) | DR "lording it over". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 07-a). |
| gracia concomitancie | by reason of concomitance | ⚠ Not *gracia concomitans* "concomitant grace": *gracia* + genitive = "for the sake of". Ruled 2026-10-08 (*Pot. pape* 06-h). |
| generalis attornatus | general attorney | Legal term (a proctor with general powers). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 140.10). |
| paterfamilias | householder | DR's word (Matt. 20:1 etc.). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 164.8). |
| regulariter | as a rule | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 165.2). |
| impertinens; impertinencia | irrelevant; irrelevance | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 179–180). |
| eleccio equivoca | equivocal election | Ch. 8's two elections (God's and men's). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 177.4). |
| apostolicus (noun, not the papal title) | an apostolic man | Where it is the pope's title, "the apostolic [lord]" with a G note. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 175.24). |
| connexio | conditional (proposition) | Logic: the "if … then" proposition. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 189.1). |
| irregularitas | irregularity | Canonical impediment to orders or office. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 190.30). |
| seniores; maiores natu | elders; the ancients | Inside a DR quotation, DR's word ("ancients", Acts 20:17). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 200). |
| servitus (laboris) | servitude | Kept apart from *servicium* "service". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 211.33). |
| carismata; carisma | CONTEXTUAL: charisms / chrism | "Charisms" (gifts; *Pot. pape* 176.1). Singular *misticum carisma* in Augustine's sense of the anointing that names Christians (*chrisma*, *Pot. pape* 312.16) "chrism", with a T note. Ruled 2026-10-08; CONTEXTUAL 2026-10-12 (coordinator, delegated). |
| potestas vicaria | vicarial power | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 236.10). |
| ordo cesareus / divinus | the caesarean / divine order | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.15). |
| malum culpe / pene | the evil of fault / of penalty | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 245.19). |
| neutra | neutral things | Things neither commanded nor forbidden (obedience *in neutris*). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 248.19). |
| reputative; assertive | by estimation; assertively | Opposed to *ex revelacione*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 251.26, 257.22). |
| eleccio passiva / activa | passive / active election | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 254.31). |
| imperium (vicarium, autoritativum) | command (vicarial, authoritative) | The power to command (*par in parem non habet imperium*); "empire" only of the Empire. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 263.2). |
| corripere; correpcio | reprove; reproof | Kept apart from *corrigere; correccio* "correct; correction"; *correpcio fraterna* stays "fraternal correction". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 264.14). |
| credulitas explicita / implicita | explicit / implicit credence | Beside *fides explicita / implicita*. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 10-k). |
| preponderancia; dispensacio | preponderance; dispensation | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 266.11, 268.4). |
| sensus compositus / divisus | composite / divided sense | The logicians' pair. Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 269.15). |
| precellencia | pre-excellence | Kept apart from *preeminencia* "preeminence". Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 274.33). |
| preternecessarius | beyond necessity | Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 276.22). |
| superhumerale; racionale | superhumeral; rational | The ephod and the breastplate (DR). Ruled 2026-10-08 (coordinator, delegated; *Pot. pape* 11-e). |
| demereri | to demerit | Ruled 2026-10-02 (*Eccl.* 23). |
| bonificare | make good | Ruled 2026-10-02 (*Eccl.* 23). |
| precellenter | pre-excellently | Adverb beside *precellencia* "pre-excellence". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 291.2). |
| potencia ordinata | ordained power | Pair of *potencia absoluta* "absolute power". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.11). |
| necessarioritas | greater necessity | Non-classical comparative abstract. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 308.1). |
| vita suffraganea | the suffragan life | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 313.21). |
| interludium | interlude | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 322.25). |
| raciones topice | topical arguments | With *evidencia topica*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 329.27). |
| gracia (papal provision) | grace | The papal grant of a benefice; untagged. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-h). |
| persona populi | the person of the people | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 347.10). |
| dominativa forma | lordly form | After *potestas dominativa*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 349.4). |
| proventus | proceeds | Kept apart from *redditus* "revenues". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 353.25). |
| principatus (pl., given to churches) | principalities | I.e. prelacies. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 366.14). |
| contracta / contrata | district | Loserth glosses "country". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 372.33). |
| papatus; racio papatus | papacy; the nature of the papacy | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 365.17). |
| dicere (logical use) | signify | Of a term or name. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 367.15). |
| coloracior | more colourable | Comparative, with the *color* / *colorabilis* rows. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 384.15). |
| diccio procuratoria | proctorial pronouncement | C note gives *dicio* "authority" as the alternative. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 386). |
| ars cesarea | the caesarean art | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| servitus ydolorum | servitude of idols | Beside *servitus laboris*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 12-t). |
| ingeniacio | wit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 394). |
| principaliter (*secundo/tercio principaliter*) | as a main head | Marks the compendium's main divisions against the counts within them. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* comp.). |
| precellere | excel | Verb beside *precellencia* "pre-excellence"; not "pre-excel". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 399.28). |
| cesaree (adv.) | in caesarean fashion | After *papa cesareus*. Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 403.25). |
| est dare | one may posit | Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 405). |
| insolubiliter | inextricably | Kept apart from *insolubilia* "insolubles". Ruled 2026-10-12 (coordinator, delegated; *Pot. pape* 404). |
| probabiliter | with probability; by probable argument | Scholastic: argued from probable premisses, as against demonstration; not the modern hedge "probably". Ruled 2026-10-12 (close-out R1; *Pot. pape* 52.3). |

---

## Chunk 05-a: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-05-a.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-05-a
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "65.0–68.4"
divisions: "cap. 5 (heading 'Cap. V.' at 65.0); part 1 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "627 words; 625 confirmed by Fordham or the vote; 1 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n104–n107 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 5, part 1: [TITLE]

## ¶1 · 65.0–65.0

<!-- the editor's bracketed argument at the chapter head: a Latin summary, then his own English
     summary in the same bracket (see the volume CARD for what is translated) -->

> [p. 65] [Supponendo quod Verbum non dimisit humanitatem pro triduo, probat quod nec potuit dimittere naturam quam assumpsit. Assuming as already proved that the Word did not as a matter of fact in the three days lay aside the human nature which he had taken up; it is here proved to be impossible that he should so lay it aside.]

[ENGLISH]

## ¶2 · 65.18–65.20

> [p. 65] Viso¹¹ quod Verbum non dimisit de facto in sancto triduo corpus vel animam: restat ostendere quod Deus non potuit dimittere naturam hominis quam assumpsit.

[ENGLISH]

## ¶3 · 65.21–68.4

> [p. 65] Probatur tripliciter. Primo sic. Deus non potest dampnificare naturam aliquam sine suo demerito¹² precedente: sed [p. 66] si dimitteret naturam assumptam, eam sic dampnificaret: ergo et cetera.¹ Maior patet ex hoc, quod dampnificacio est creature racionali² mali illacio inutilis,² que non potest sibi inexistere nisi oriatur principaliter a se ipsa, iuxta sentenciam beati Iohannis Chrisostomi et aliorum doctorum communiter. Confirmatur. Si Deus aufert creature racionali bonum aliquod, iustum et pulcrum est illud auferri et per consequens non sonat³ in malum inutile: et sic⁴ servata immunitate peccati non est dampnum. Nam si Deus dampnificat hominem, quia facit eum iuste carere bono possibili; tunc infinitum multum dampnificaret quamlibet beatificabilem creaturam; et, ut communiter deducitur, infinitum impediret quodlibet opus suum. 2°. Confirmatur⁵ ex hoc, quod infliccio⁶ pene perpetue pro peccato non dampnificat sed meliorat dampnatum in tantum quod, si esset in eleccione⁷ sua sic dampnari post peccatum vel vacare⁸ impunem,⁹ eligeret racionabiliter sic dampnari: ergo a maiori vel pari, si Deus aufert ab aliquo¹⁰ sine suo demerito¹⁰ quodvis bonum, cum sit pulcrum et bonum quod ita faciat nedum toti universitati¹¹ sed persone, que aliter frustratorie¹² occuparet; sequitur quod talis ablacio non sit dampnificacio; cum nec pro illa ablacione nec pro eius causa racionabiliter¹³ sit dolendum. Ex quo¹⁴ videtur 3°. quod innocens hoc videns eligeret¹⁵ racionabiliter sic privari: et cum nemo¹⁶ potest racionabiliter eligere¹⁶ dampnificari, sequitur quod Deus non dampnificat creaturam, sed solum ipsamet¹⁷ seipsam¹⁸ vel aliud alliciens ad peccandum. Ymo si bene consideretur, omnis dampnificacio sapit iniuriacionem, que non potest per se bono et iusto competere, quin pocius bonificare et corrigere. Minor autem argumenti sic [p. 67] probatur. Humanitas assumpta a Verbo non potest demereri previe suam dimissionem: ergo, illa dimissa, hoc sibi contingeret sine suo demerito. Antecedens patet per hoc, quod non potest demereri stante unione, quia tunc Verbum peccaret: et si pro instanti dissolucionis vel post peccaret, patet quod demeritum [dimissionem] sequetur;¹ et per consequens non dampnificaretur ex suo demerito precedente. Quod autem dimissio² foret dampnosa humanitati Christi ex hoc evidet, quod deperdicio gracie unionis foret deperdicio maximi boni possibilis intrinseci creature:³ et per consequens tum⁴ loco illius non succederet tantum bonum: sequitur quod humanitas ipsam perdens foret notabiliter peiorata, et per consequens dampnificata. Valorem autem ypostatice unionis suppono⁵ ex dictis et dicendis: per illam enim fuit homo assumptus idem personaliter Verbo Dei. Magna ergo peioracio sua foret quod dimitteretur sine suo demerito tanquam extranea. Non enim pertinet ad dictum Cesarem semper Augustum⁶ sic peiorare sine suo demerito carissimam⁷ creaturam: quia indubie creatura dimissa pro instanti dimissionis posset racionabiliter conqueri de ingratitudine Dei sui, cum continue ante fecit quidquid debuit, et finaliter reciperet pro ‘retribucione⁸ mercedis’ tantum dampnum.⁸ Non ergo foret spes⁹ in tali Deo. Et hinc nimirum¹⁰ dicit Augustinus Ome. 47: ‘Absit¹¹ quod Christus pro triduo animam suam dimiserit:¹² ipsam enim inseparabiliter habuit:’ unde indubie, si post peccaret, dimissio gracie unionis preservantis ne peccet foret causa principalis peccati: quia si affirmacio sit causa affirmacionis, negacio est causa negacionis, ut absencia naute est causa periclitacionis navis ex 2° Physicorum. Illud ergo peccatum, ex dimissione originatum, esset Deo principaliter imputandum, cum non ex parte creature, sed Dei, causatur talis absencia: talis¹³ ergo [p. 68] Deus excederet in malicia deum Manicheorum,¹ qui sine² demerito servi sui absentaret se pro temptacionis tempore non iuvando. Unde et illam racionem tangit sanctus Thomas De Christo,³ articulo 70.⁴

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 67: *‘retribucione mercedis’* (bt ran the words together; print has two words (footnote 8 between)) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference 5 Augustinus, (65.5); reference Heb. ii. 2. (67.22); reference Augustine shud- (67.23).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 65:
1 auderunt B; audire O.
2 credissem O.
3 animas B.
4–4 porci secundum presentis C.
5 poterit A C O.
6 foret A C O.
7 bovinum A B C.
8–8 esse veracissime B; (ee̅ȝ) essent variatissime O (sc. nature vel sentencie).
9 animalis O.
10 vanum igitur O.
11 Littera initialis om. A B C.
12 merito B.

p. 66:
1 etc. in marg. A.
2–2 inutilis illacio om. mali O.
3 soluat O.
4 sic om. O.
5 idem add. O.
6 influccio A B C.
7 elleccione O.
8 viare cum litura in medio verbo A; viare B; vitare C.
9 impune O.
10 sine suo demerito om. A B C.
11 universo O.
12 frustracione O.
13 racionaliter et sic postea B.
14 quo in margine O.
15 debet eligere B; eligeret A sed addit in margine debet eligere.
16 sic (sit B) racionabiliter eligeret A B C.
17 ipsam A B C.
18 se ipsam om. O.

p. 67:
1 sequetur et in margine suple dimissione A; sequitur O; sequetur B C.
2 dimissa B.
3 a creatura O.
4 tum om. O.
5 suppo° A B C.
6 augustutum O.
7 kr͡aʒ[?] B; bm͡aʒ[?] (i.e. beatissimam) O.
8–8 mercedis tantum premium A B C; mercedem O.
9 species B O.
10 mimirum A.
11 absit om. O.
12 dimiseret O.
13 talis om. O.

p. 68:
1 manichiorum O.
2 sint B.
3 Aquino C.
4 50 O.
5 vel *add. altera manu* O.
6_6 coesse. Secundo Christus si A B C.
7 possibiliter O.
8 contingisse O.
9 alia A B C.
10 reliquie A B C.
11_11 *Locus uncinis inclusus in codd.* C. O. *prorsus deest.*
12_12 securitas . . . gaudii B *in marg.*
13_13 contradiccionem anime esse C.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 65: [_Supponendo quod Verbum non dimisit humanitatem pro triduo, probat quod nec potuit dimittere naturam quam assumpsit. Assuming as already proved that the Word did not as a matter of fact in the three days lay aside the human nature which he had taken up; it is here proved to be impossible that he should so lay it aside.~\
p. 68: QU-od. | P er accidens | per se | per se | Lotus nncinis inclusus in codd.
```

---

## Chunk 05-b: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-05-b.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-05-b
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "68.5–72.18"
divisions: "cap. 5 (heading 'Cap. V.' at 65.0); part 2 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1154 words; 1150 confirmed by Fordham or the vote; 3 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n107–n111 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 5, part 2: [TITLE]

## ¶1 · 68.5–70.3

> [p. 68] Item quilibet beatus in celo est tam insolubiliter Deo connexus quod repugnat illi statui miseriam peccati in anima succedere vel⁵ coesse: sed Christus ab instanti unionis fuit perfeccius beatus secundum animam quam alius, cum fuerit sanctus sanctorum: ergo multo magis repugnat anime sue peccatum succedere vel⁶ coesse: sed si⁶ dimissio foret possibilis,⁷ hoc potuit contigisse:⁸ ergo illa⁹ dimissio non fuit possibilis. Maior probatur ex hoc. Omnes beati sunt immortales et impeccabiles, sicut omnes rectiloqui¹⁰ confitentur: non quia non possunt peccare, quia multi prius tempore suo peccant; sed sunt in gracia confirmacionis et glorie, cui repugnat peccatum vel miseriam coexistere, vel post illam succedere: patet ergo quod beatitudo est qualitas implicans securitatem perpetuitatis pleni gaudii et exclusionis miserie. [Eciam¹¹¹² securitas perpetuitatis pleni gaudii¹² et exclusionis miserie est per seipsum securitas talis, cum sit deveniendum ad ultimum formale, quo formaliter et non alio est quis securus de perpetuitate pleni gaudii et exclusionis miserie. Sed contradiccionem implicat tali coexistere in subiecto suo vel post illam in ipso subiecto suo miseriam succedere: igitur etcetera.]¹¹ Unde omnes theologi concorditer confitentur, quod¹³ contradiccionem claudit aliquem esse¹³ vel fuisse beatum cum hoc quod fiat postmodum non beatus. Nec valet dicere quod beatitudo per accidens sit beatitudo, quia ipsa est ultima forma abstracta, qua quis est beatus formaliter. Ideo, si illa non sit per se beatitudo, non superest quid aliud per se foret. [p. 69] Sicut ergo iusticia non potest esse non iusticia et de formis similibus;¹ sic status beatitudinis non potest esse non huiusmodi² status. Unde notum est methaphisicis quod tales forme abstracte non suscipiunt sic³ predicacionem per accidens ut concreta: si enim beatitudo sit per accidens beatitudo—cum non sit processus in infinitum; sed, cum omne per accidens sit reducibile ad aliquid⁴ per se, est devenire ad ultimum formale, quo quis est beatus—et illud per se et non per accidens est beatitudo: et de tali est michi sermo. Confirmatur. Si A qualitas⁵ sit nunc beatitudo et potest manere et⁶ desinere esse beatitudo; per idem post esse potest reincipere esse beatitudo. Quo concesso, patet quod preter A, quod non sufficit denominare hominem beatum, requiritur forma superaddita; et sic non A, sed forma sibi adveniens,⁷ foret beatitudo. Patet ergo, quod cum beatitudo et confirmacio non possunt esse, nisi sint perpetue; nec possunt esse nisi huiusmodi quod, eo ipso quod insunt, reponunt hominem in statu cui repugnat miseriam succedere vel coesse; nec dependet beatitudo pocius a futuro, quam qualitates alie absolute;⁸ tunc enim non forent beati de sua beatitudine securati. Minor ergo argumenti patet generaliter omni professori fidei incarnacionis: cum anima Christi ab instanti sue creacionis fuit plena omni genere carismatum, habens clariorem⁹ visionem divine essencie quam alia creatura, et per consequens plenam fruicionem ad tantam noticiam naturaliter¹⁰ consequentem. Cum ergo ‘vita eterna sit¹¹ sic cognoscere Deum Patrem ac Dominum Iesum Christum,’ ut testatur Veritas Ioh. 17; patet quod anima Christi ab instanti sue creacionis perpetue est beata.¹² Nec audivi hoc negatum ab aliquo, cum palam sequitur ex incarnacione. Si enim homo solum¹³ intelligit quod intelligit mens¹³ [p. 70] ypostatice copulata; per locum a sufficienti similitudine spiritus Iesu cognoscit quidquid cognoverat¹ ipse Iesus specialiter cum sit personaliter Verbum Dei.

[ENGLISH]

## ¶2 · 70.4–70.32

> [p. 70] Ex istis colligitur talis racio. Tam determinatum et necessarium est ipsum hominem fuisse assumptum, quam necessarium est mundum vel aliquid aliud prefuisse: sed non potuit fuisse assumptus nisi fuisset exinde beatus: ergo tam necessarium est ipsum fuisse beatum quam necessarium est aliquid prefuisse: sed pretericiones huiusmodi non possunt solvi: ergo nec beatitudo vel assumpcio Domini nostri Iesu Christi. 2°. confirmatur ex hoc; quod anima Christi actu elicito vidit clare in Verbo omnia preterita vel futura; et per consequens clare vidit perpetuitatem sue beatitudinis; et ultra, cum illa visio² non potuit defuisse vel verti in ignoranciam aut³ aliud genus entis; sequitur quod illa anima non potuit desinere esse beata vel Verbo ypostatice copulata. 3°. confirmatur ex testimonio Leonis Pape in quodam sermone dicentis: ‘tanta fuit unicio⁴ Dei et hominis ut nec supplicio posset⁵ dirimi nec morte distingui.’ Nec obest isti sentencie divina dispensacio, qua voluit Verbum suum ad tempus esse corpus, non plene sed quasi arraliter tunc⁶ beatum, et per consequens esse animam secundum actuacionem corporis et racionem, qua⁷ ipsam respicit, quantumlibet dolorosam.⁸ Nam ille homo est multarum naturarum quelibet,⁹ secundum quarum unam¹⁰ fuit ad tempus abiectus viator, et simul secundum aliam perfectissimus comprehensor: et sic simul summe gaudens et summe tristis secundum vires et raciones dispares, ut¹¹ ostenditur consequenter: et dico¹¹ quod arraliter habuit in via dotes corporis, cum dote subtilitatis exivit sponsus de clauso utero,¹² dote agilitatis ambulavit super aquas, dote incorruptibilitatis et claritatis in transfiguracione emicuit.¹³

[ENGLISH]

## ¶3 · 70.33–71.15

> [p. 70] 3°. per deducens ad impossibile patet idem.¹⁴ Nam si [p. 71] humanitas ypostatice copulata posset dimitti et sic dampnari pro peccato, et tam caro quam anima est personaliter ipsum Verbum; sequitur quod Verbum Dei peccare¹ poterit et dampnari; quod nephas² est dicere. Patet consequencia supposito fundamento, cum arguitur ab inferiori ad suum superius personale, cui per se competit accio personalis. Sequitur ergo—hec humanitas potest peccare: hec humanitas est persona Verbi: ergo persona Verbi potest peccare—. Nam persona Verbi nedum est hec³ humanitas, sed aliquid aliud³ quia divinitas; ideo est superior⁴ vel communior quam⁴ est hec⁵ humanitas. Unde, sicut sequitur quod Filius Dei fuit natus humanitus, conversatus,⁶ passus, mortuus, et sepultus, et ascendit, eo quod humanitas, que fuit dictus Filius, sic se habuit; ita eciam sequeretur quod Verbum peccaret, si humanitas, que fuit dictum Verbum, peccaret.

[ENGLISH]

## ¶4 · 71.16–72.18

> [p. 71] Confirmatur ex testimonio moderniorum⁷ dicencium quod hec humanitas non posset⁸ ypostatice copulari peccando nisi Verbum exinde peccaret;⁹ et, quod plus est,¹⁰ racione unionis prioris Verbum denominatum est secundum moderniores jacuisse pro triduo in sepulcro, et ad sensum consimilem peccasse in casu, quo¹¹ natura dimissa pro tunc peccaverit. Que, rogo, causa diversitatis sensus Spiritus¹² Sancti in isto articulo fidei ‘Christus descendit ad inferos, fuit mortuus et sepultus;’ hoc est, non illa persona, sed pars eius pro tempore quo¹³ non fuit pars vel ypostatice copulata,¹⁴ sic se habuit; quin ad sensum simillimum concederet, quod natura dimissa et postmodum reassumpta, si peccaret interim, denominaret Filium sic peccare?¹⁵ Ponatur ergo quod in die parasceues anima Christi¹⁶ perfecerit liberacionem patrum a limbo,¹⁶ et pro tunc agitetur¹⁷ corpus a demone multos homines conquassando et quod in [p. 72] sancto¹ sabbato †reuniatur² anima corpori suspensa ypostatica unione, et peccet ante nonam adulterio, homicidio, blasfemia, et omni genere peccatorum; et post nonam peniteat, et procreet legitime, ac juste condempnet multos ad mortem, assumpta humanitate in prima sabbati in unitatem suppositi Verbi Dei: quem casum moderni admittunt et magis mirabiles tanquam necessario possibiles; in quo casu videtur juxta glosam quam dant³ articulis fidei quod⁴ omnes dicte operaciones in triduo redundarent in Christum vel aliter fingeret⁵ ex instinctu Spiritus Sancti sensum impossibilem et insolitum. Certum est itaque Christum non istos homines suffocasse,⁶ virginitatis laureolam⁷ ex procreacione seminis perdidisse, irregularitatem incurrisse, vel remansisse in eo vestigia peccatorum. Et conformi racione nec iacuit sepultus nec descendit ad inferos, nisi conformi racione denominaciones predicte in casu⁸ posito sibi insint,⁸ vel aliter dicatur sentencia supradicta, quod mansit pro dicto triduo unio ypostatica ad utrumque.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 71: *hec humanitas,* (bt ran together; print hec ³ humanitas (two words)) [SUB]
- **Omitted per §3.5 / kept in the English** (margin matter): reference s. John xvii. 3. (69.28); reference l Cor. i. 25. (72.30).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 68:
1 manichiorum O.
2 sint B.
3 Aquino C.
4 50 O.
5 vel *add. altera manu* O.
6_6 coesse. Secundo Christus si A B C.
7 possibiliter O.
8 contingisse O.
9 alia A B C.
10 reliquie A B C.
11_11 *Locus uncinis inclusus in codd.* C. O. *prorsus deest.*
12_12 securitas . . . gaudii B *in marg.*
13_13 contradiccionem anime esse C.

p. 69:
1 substancialibus B.
2 hei[?] (sic) C.
3 sicut A; sed C.
4 aliquod A B C.
5 a qütis O.
6 manere et om. O.
7 a deveniens O.
8 forsitan abstracte legendum.
9 cariorem O.
10 generaliter A C.
11 sic sit A B; sie sit C; sit sic O.
12 beatificata A B C.
13 intelligit (rasura) mens A; intelligit mens B; intelligit quod mens C.

p. 70:
1 cognoverit O.
2 visus o B.
3 vel A B.
4 unio A B C.
5 potest A B C.
6 esse *add.* A B C.
7 quam O.
8 dolosam O.
9 qualibet B.
10 una A.
11–11 ut ostenditur ut dico A B C.
12 uthero B.
13 enituit O.
14 illud A B C.

p. 71:
1 dei deprecari B.
2 nefas B.
3-3 humanitas . . . aliud om. B
4 quam communior quam B.
5 ista; om. est O.
6 conversatus om. B
7 modernorum O.
8 potest B C.
9 peccaverit O.
10 est om. O.
11 qua A B C.
12 spiritus om. O.
13 qui O.
14 copulativa O.
15 peccaret O.
16-16 perfeceret libacionem patrum a libo O.
17 agetur C.

CHECK: the main-text figure list includes a second 4 (4, 4), but the foot has only one entry for 4 (the printed entry "4 quam communior quam B." is the only one).

p. 72:
1 isto C.
2 reniatur A C; revivatur B; revinatur *in margine* C; reunciatur O; *certe aut* revinciatur *aut* reuniatur *legendum*.
3 dant autores A B; dat autores C.
4 quod *om.* O.
5 finge (*lacuna*) ex instinctu C; fīgᵗ O.
6 suffocare O.
7 aureolam A B C.
8–8 sibi posito insunt A B; posito sibi nismit (*sic*) C.
9 cum eo *om.* O.
10–10 a persecutoribus et flagellacionibus; sed *om.* iudeorum A B C; a persecucionibus in flagellacionibus iudeorum sed O.
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 68: QU-od. | P er accidens | per se | per se | Lotus nncinis inclusus in codd.
p. 69: per accidens | omne per accidens | aliquid 4, per se, | illud per se | non per accidens
```

---

## Chunk 05-c: write to `/Users/wilsonpruitt/wyclif/chunks/incarnacione/wyc-incarnacione-05-c.md`

### Scaffold

````markdown
---
chunk_id: wyc-incarnacione-05-c
work_la: Tractatus de benedicta incarnacione
work_en: On the Blessed Incarnation
volume_slug: incarnacione
editor: Edward Harris
year: 1886
pages: "72.19–76.31"
divisions: "cap. 5 (heading 'Cap. V.' at 65.0); part 3 of 5, split at the editor's ¶ (CONVENTIONS §1)"
latin_source: B+ (blind transcription, checked against Fordham and the vote)
witnesses: [fordham, johanniswyclift01wyclgoog, johanniswyclift03wyclgoog, johanniswycliftr00wycl, johanniswycliftr06wycl, latinworks03wycl, tractatusdebened00wycl]
check: "1151 words; 1148 confirmed by Fordham or the vote; 2 runs stood by rule (both witnesses garbled); 1 read on the plate (see Transcription notes)"
italics: none
plates: "archive.org latinworks03wycl, leaves n111–n115 (printed p. = leaf − 39)"
status: draft
---

# *De benedicta incarnacione*, chapter 5, part 3: [TITLE]

## ¶1 · 72.19–73.3

> [p. 72] Ex istis colligitur quod, si beatus alius tantum adheret Deo quod non potest post beatitudinem dissolvi unio, qua est unus spiritus cum eo;⁹ multo magis natura Christi, que ultra hoc ypostatice est unita: ut si homo, qui potest peccare, habet per graciam quod sit impeccabilis, immortalis, et sic de aliis que peioracionem sapiunt: quanto magis natura humana in fine bonitatis possibilis exaltata, que omnino peccare non poterit, ab illa gracia dimitti non poterit. Unde, quamvis Mt. 27 secundum naturam completam creatam clamet Christus; ‘Deus meus, Deus meus, utquid me dereliquisti?’ non tamen dimisit ypostaticam unionem, sed dereliquit illud ‘infirmum Dei,’ quod est suppositum ‘forcius’ ad tempus, inconservatum a¹⁰ persecucionibus et flagellacionibus Iudeorum; sed¹⁰ nunquam [p. 73] dimisit vel simpliciter dereliquit, quia dimissio dicit existenciam dimissi et separacionem ypostaticam ab eodem, quod non fuit in triduo.

[ENGLISH]

## ¶2 · 73.4–75.5

> [p. 73] Quod si quis in evidenciam huius veritatis olim famose expectat testimonium scripture, ecce Veritas Ioh. 10. alloquitur Phariseos: ‘non potest, inquit, solvi scriptura, quem Pater sanctificavit et misit in mundum.’ Pro cuius intellectu sunt tria notanda per ordinem.¹ Primo quod Veritas non loquitur de scriptura nostra artificiali aggregata ex ficturis² atramenti et pellibus mortuorum; tum quia talis scriptura cottidie per artifices potest solvi; tum eciam quia illi non competit sanctificacio et missio in mundum: sed illa scriptura est ‘liber vite’ cui inscribuntur omnia, cum sit intrinsecus Sermo Dei. Et ad illum sensum exponit Augustitinus Ome. 44.³ ‘Forte, inquit, aliquis dicit⁴: Si pater eum sanctificavit, ergo⁵ aliquando non erat sanctus; sed si sic eum sanctificavit,⁵ quomodo genuit? ut enim sanctus esset, gignendo ei⁶ dedit, quia sanctum eum genuit.’ Et respondet posterius ad obiectum. ‘Si, inquit, quod sanctificatur aliquando, non erat sanctum; quomodo dicimus Deo Patri —“sanctificetur nomen tuum”—?’ Ille ergo, qui est absolute necessario in se sanctus, fit sanctus⁷ in nobis per prevenientem graciam, noticiam, et operacionem, et confessionem meritoriam.⁸ Unde Spiritus Sanctus ad relinquendum nobis exemplar, quod loquitur de scriptura vitali, subdit in genere masculino— ‘quem Pater sanctificavit’— innuendo nobis relacionem faciendam ad Filium. Mos⁹ enim est scripture et Augustini per adiectivos¹⁰ masculinos personas concipere et per neutros¹⁰ naturas. Et isti modo¹¹ loquendi alludit Apostolus ad Gall. 3°; ‘non, inquit,¹² dicit seminibus quasi in multis, sed semini tuo, qui est Christus.’ Indubie, sicut sanctus Apostolus notavit¹³ numerum, sic et genus. [p. 74] 2°. supponitur quod Veritas non loquitur de solucione mentis a corpore vel Patris a Filio in hoc dicto: de prima non, quia supra Ioh. 2°. dicit Veritas Iudeis prophetice quod solverent templum corporis sui ab anima et ipse in tribus diebus excitaret illud. Cum ergo ‘non fuit in eo EST et NON,’ patet quod hic non intellexit corpus non posse solvi ab anima. Nec alius sensus est pertinens; tum quia ligacio¹ et solucio est duarum naturarum ad invicem et non personarum eiusdem summe indivisibilis essencie; tum eciam, quia ille sensus fuisset dictis impertinens, non eis ambiguus. Ideo relinquitur 3°. per locum a sufficienti divisione quod intellexit insolubilitatem deitatis ab humanitate, quas expressit nomine ‘scripture,’ ut vel sic scrutarentur scripturas, que testimonium perhibent² de istis duabus naturis sic ypostatice copulatis. Unde et Ioh. 5. dicitur³ ‘scrutamini⁴ scripturas in quibus vos putatis vitam eternam habere, et ille sunt que testimonium perhibent² de me.’ Non enim haberent evidenciam dicere quod blasfemat dicendo se esse Dei Filium naturalem apposito sufficienti scrutinio scripturarum. Nam si in lege scriptum sit de Messia vel Christo futuro in duabus naturis et una ypostasi—quod⁵ vinculum propter unionem⁶ ypostaticam ad infinitam personam non potest includi⁷ fine temporis, sicut potest unio participative deificatorum per Sermonem Dei⁸ factum ad eos et non eis personaliter copulatum—quomodo est color concludendi blasfemiam⁹ ex assercione filiacionis naturalis? Medium autem per quod tenet ista inveccio est veritas quod ‘non potest solvi’ hec ‘scriptura’ ad sensum expositum. Nam ex illo¹⁰ sequitur quod sit natura increata in supposito Verbi, et cum¹¹ hoc natura creata temporaliter sed¹² insolubiliter copulata. Unde signantissime Veritas dicit negativam quod ‘non potest solvi scriptura;’ quia, licet sancti in patria sint Deo inseparabiliter copulati, tamen contingentissime possunt solvi, cum sint pro [p. 75] tempore suo viantes¹ peccabiles. Homo autem assumptus a Verbo Dominus Iesus Christus pro nullo tempore peccare poterit. Et² patet conclusio.² Nec³ aliter haberent sancti doctores evidenciam imprecandi anathema eis qui concedunt dimissionem vel solucionem huiusmodi naturarum.

[ENGLISH]

## ¶3 · 75.6–75.10

> [p. 75] Sed contra illud obicitur. Quicquid Deus contingenter et libere contradictorie facit, potest alias eciam adnichilando⁴ destruere: sed libere contradictorie assumpsit hominem: ergo potest nedum ipsum dimittere sed adnichilando⁴ destruere.

[ENGLISH]

## ¶4 · 75.11–75.22

> [p. 75] Confirmatur tripliciter. Primo ex hoc, quod idem est iudicium de una creatura et qualibet, cum tanta sit utrobique divina libertas: sed aliquam creaturam Deus potest adnichilare: ergo⁵ quamlibet. 2°. per hoc quod aliter Deus esset necessitatus ad conservandam dictam unionem, et sic non libere contradictorie eam servat. 3°. ex hoc quod Deus non esset omnipotens, nisi posset tam contingentem et fragilem⁶ nedum dissolvere,⁷ sed et adnichilare.⁷ Tales⁸ sunt multe⁸ instancie, que omnes currunt sub uno circulo quod Deus non esset omnipotens nisi posset in talia. Vel taliter⁹ arguunt per locum a simili;— Si Deus creare poterit et utrobique tanta¹⁰ est¹⁰ distancia; ergo per idem¹¹ adnichilare poterit.

[ENGLISH]

## ¶5 · 75.23–76.2

> [p. 75] Pro isto dico sicut alias sepe dixi quod ad omnipotenciam Dei consequitur perficere construere et non destruere, creare¹² et non adnichilare; et sic de actibus positivis privacionibus repugnantibus separatis. Unde sicut repugnat¹³ pure creaturam esse et non posse deficere, sic repugnat omnipotencie Creatoris posse adnichilare peiorare dampnificare vel de¹⁴ se destruere creaturam. Peccatum autem¹⁵ quod non est creatura Deus destruit, peccantes solum per accidens racione peccati punit vel meliorando consumit.¹⁶ [p. 76] Et sic ex omnipotencia Dei sequitur oppositum predictorum et patet quod assumptum est inpossibile.

[ENGLISH]

## ¶6 · 76.3–76.14

> [p. 76] Pro cuius¹ intellectu pono triplex exemplum ut alias posui. Primum logicum. Nam Deus produxit tempus perpetuum, sicut testatur scriptura et sepe meminit Augustinus. Nam Ps. 73.² dicitur ‘estatem et ver tu plasmasti ea.’³ Et idem est iudicium de toto⁴ tempore,⁴ et signanter dicit Veritas Marc. 2ᶜ· quod ‘Filius hominis est dominus sabbati’ et sic Deus. Et tamen notum est quod Deus de potencia absoluta non potest tempus perpetuum⁵ adnichilare sive destruere, ymo, quod plus est, tempus vel motum finire ante finem sue periodi naturalis. Modicus ergo color est concludere, si Deus libere contradictorie datum effectum produxerit, quod potest ipsum destruere.

[ENGLISH]

## ¶7 · 76.15–76.19

> [p. 76] 2ᵐ exemplum naturale⁶ est de hoc⁶ quod Deus libere condictorie produxit mundum ex nichilo et tamen non potest ipsum destruere nec aliam substancialem essenciam ut patet in materia De Adnichilacione, ne fiat vacuum vel defectus in Deo formaliter.

[ENGLISH]

## ¶8 · 76.20–76.23

> [p. 76] 3ᵐ exemplum est methaphisicum. Nam Deus produxit veritatem talem, de preterito me fuisse, et hoc liberrime contingenter; et tamen notum⁷ est quod⁷ de potencia sua absoluta non potest ipsam destruere vel eius desicionem⁸ permittere.

[ENGLISH]

## ¶9 · 76.24–76.31

> [p. 76] Talia quotlibet exempla reliquit nobis Deus, ut consideremus eius bonitatem et naturalem condicionem ad positive posse bene agere et non male. Sicut enim est actus purus non admixtus⁹ potencia ante⁹ actum, sic potest per se proficiendo tendere in esse positivum, et non deficiendo per se tendere in¹⁰ non esse, ut, licet modicum sit, mentiri vel aliter peccando male agere; Deus tamen ex omnipotencia hoc non potest.

[ENGLISH]

## Notes

## Transcription notes

- **Plate readings** (CONVENTIONS §3.4; page · reading · note):
  - 76: *2ᶜ·* (plate: print = bt (raised mark after 2) (Opus coordinator)) [AGREE]
- **Omitted per §3.5 / kept in the English** (margin matter): reference l Cor. i. 25. (72.30); reference Matth. vi. 9. (73.21); reference 3® Gal. m. 16. (73.30); reference fr° £? John n° 19' [A 84c] (74.3); reference s. John v. 35. (74.25); reference Mark ii. 28. (76.9).
````

### Apparatus (editor's page-foot notes, read from the plate; line numbers are the printed page's)

```
p. 72:
1 isto C.
2 reniatur A C; revivatur B; revinatur *in margine* C; reunciatur O; *certe aut* revinciatur *aut* reuniatur *legendum*.
3 dant autores A B; dat autores C.
4 quod *om.* O.
5 finge (*lacuna*) ex instinctu C; fīgᵗ O.
6 suffocare O.
7 aureolam A B C.
8–8 sibi posito insunt A B; posito sibi nismit (*sic*) C.
9 cum eo *om.* O.
10–10 a persecutoribus et flagellacionibus; sed *om.* iudeorum A B C; a persecucionibus in flagellacionibus iudeorum sed O.

p. 73:
1 pro ordine O.
2 figuris A B C.
3 48 O.
4 diceret A B C.
5–5 ergo . . . sanctificavit om. A B C.
6 et A B C.
7 firmius O.
8 meritoriam. Ad. Unde (sic) C.
9 mous O.
10–10 adiecciones masculinas—neutras A B C.
11 moi A B. (the printed "moi" has a circumflex arc over the "oi")
12 enim A B C.
13 numeravit C M.

p. 74:
1 ligamentum O ; pertinens. Cum ligacio C.
2 prohibent O.
3 dicit A B C.
4 scruta num A C ; scruta in B.
5 ypostasis B.
6 unione O.
7 concludi A B C.
8 domini A B C.
9 blasfemia A B C.
10 2°. A B C.
11 tamen C.
12 scilicet A B C.

p. 75:
1 euantes O.
2–2 ut patet oculo A B C.
3 nam C.
4 anichilando ut infra saepius A B C.
5 in add. O.
6 nedum prima manu nodum altera manu A C; nodum B; nedum O; nisi posset creaturam tam contingentem dissolvere M; et certe aut creaturam supplendum aut unionem subaudiendum est.
7–7 sed et adnichilare om. O M; et om. B.
8–8 sunt multe om. A B C.
9 aliter O.
10–10 est tanta B C. est carisata A.
11 perinde O.
12 creare om. O.
13 repugnant O.
14 per O.
15 autem om. O.
14 consumat C.
CHECK: the last entry is printed with figure 14 (a second "14"), but it belongs to text figure 16 ("consumit"); no entry is printed with figure 16.
CHECK (coordinator): text figure(s) 16 have no entry read here: read the plate foot before citing.

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
```

### Italics (the editor's italic runs, OCR, one per |: his quotation bounds, evidence only)

```
p. 75: supplendum aut
p. 76: De Adnichilacione,
```
